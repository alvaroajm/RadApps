#!/usr/bin/env python3
"""Check HTML structure, local links, asset versions and the original app catalogue."""
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit
from hashlib import sha256
import re

ROOT=Path(__file__).resolve().parents[1]
VOID={'area','base','br','col','embed','hr','img','input','link','meta','param','source','track','wbr'}
errors=[]
class Check(HTMLParser):
    def __init__(self,path):
        super().__init__(convert_charrefs=True)
        self.path=path; self.stack=[]; self.ids=set(); self.refs=[]; self.apps=[]; self.h1=0
    def handle_starttag(self,tag,attributes):
        attrs=dict(attributes)
        if 'id' in attrs:
            if attrs['id'] in self.ids: errors.append(f'{self.path}: duplicate id {attrs["id"]}')
            self.ids.add(attrs['id'])
        if tag=='h1': self.h1+=1
        if tag=='img' and 'alt' not in attrs: errors.append(f'{self.path}: image without alt')
        if tag in ('section','div','ul','p') and 'p' in self.stack: errors.append(f'{self.path}: {tag} inside p')
        if tag=='a' and 'a' in self.stack: errors.append(f'{self.path}: nested link')
        for key in ('href','src'):
            if key in attrs: self.refs.append(attrs[key])
        if attrs.get('class')=='app-tile': self.apps.append(attrs['href'])
        if tag not in VOID: self.stack.append(tag)
    def handle_endtag(self,tag):
        if tag in VOID: return
        if not self.stack or self.stack[-1]!=tag: errors.append(f'{self.path}: closing {tag}, stack {self.stack[-4:]}')
        else: self.stack.pop()

parsed={}
for path in ROOT.rglob('*.html'):
    p=Check(path.relative_to(ROOT)); p.feed(path.read_text()); parsed[path]=p
    if p.stack: errors.append(f'{p.path}: unclosed {p.stack}')
    if p.h1!=1: errors.append(f'{p.path}: {p.h1} h1 elements')
expected=[f'https://alvaro-menezes.com/apps/{slug}.html' for slug in ('aspects','hemorad','puberty','gfr','tirads','hepfe','orads','nlung')]
for path,p in parsed.items():
    if path in (ROOT/'index.html',ROOT/'en/index.html') and p.apps!=expected: errors.append(f'{p.path}: app catalogue mismatch')
    for ref in p.refs:
        u=urlsplit(ref)
        if u.scheme or u.netloc: continue
        dest=(ROOT/u.path.lstrip('/')) if u.path.startswith('/') else path.parent/u.path if u.path else path
        if dest.is_dir(): dest=dest/'index.html'
        if not dest.exists(): errors.append(f'{p.path}: missing {ref}')
        elif u.fragment and dest in parsed and u.fragment not in parsed[dest].ids: errors.append(f'{p.path}: missing anchor {ref}')
        if u.query.startswith('v=') and dest.is_file():
            if u.query[2:]!=sha256(dest.read_bytes()).hexdigest()[:12]: errors.append(f'{p.path}: stale hash {ref}')
for css in (ROOT/'assets').glob('*.css'):
    for ref in re.findall(r'url\([\'\"]?([^\)\'\"]+)',css.read_text()):
        if not (css.parent/ref).exists(): errors.append(f'{css}: missing {ref}')
if errors:
    print('\n'.join(errors)); raise SystemExit(1)
print(f'PASS: {len(parsed)} HTML pages; structure, headings, anchors, local assets, hashes and eight app links including ASPECTS, HemoRad and Puberty Calc.')
