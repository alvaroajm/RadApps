# RadApps

Site institucional bilíngue de aplicativos para Radiologia.

- Produção: https://radapps.app
- Repositório: https://github.com/alvaroajm/RadApps
- Hospedagem: GitHub Pages, branch `main`, raiz; domínio, DNS e proxy de segurança na Cloudflare.
- Referência visual: https://alvaro-menezes.com — fonte conferida no commit `437f07b5947f628b07af61ae7f11d0812a357688` em 17/09/2026.

## Desenvolvimento

```sh
python3 scripts/build_site.py
python3 scripts/check_site.py
node --check assets/site.js
node --check assets/theme-init.js
python3 -m http.server 4173 --bind 127.0.0.1
```

Abra http://127.0.0.1:4173. Não há dependências de build, cadastro, banco de dados, cookies de marketing ou upload de exames.

O gerador mantém páginas completas em português e inglês, metadados, URLs canônicas, hreflang e sitemap. Edite o conteúdo em `scripts/build_site.py` e execute o gerador; evite alterar manualmente os HTML gerados. Os ativos locais são versionados por SHA-256. O tema utiliza apenas `radapps-theme` no localStorage; idioma é mantido na URL.

## Conteúdo e identidade

As duas imagens de marca foram fornecidas pelo proprietário e são preservadas integralmente. Os ícones e descrições dos seis aplicativos são os da homepage pessoal; os aplicativos continuam hospedados nos destinos originais. Não foram copiadas calculadoras nem declaradas versões nas lojas.

As fontes Inter e Playfair Display são servidas localmente; licenças em `assets/fonts`. A publicação do código não concede autorização de uso da marca ou de materiais de terceiros.

## Publicação

Confirme o remoto `alvaroajm/RadApps`, `CNAME=radapps.app` e a zona `radapps.app` antes de qualquer alteração. Gere, valide, faça commit e push para `main`. Confira a implantação de Pages e as respostas HTTPS no domínio, incluindo os hashes dos ativos.

## Segurança e busca

Configuração aplicada e verificada em 17/09/2026:

- `radapps.app` e `www.radapps.app`: CNAME com proxy para `alvaroajm.github.io`.
- Cloudflare SSL Full (strict), redirecionamento HTTP → HTTPS, TLS mínimo 1.2 e TLS 1.3 ativo. Certificados universais ativos; HTTPS também exigido no GitHub Pages.
- DNSSEC ativo, registro DS publicado automaticamente pelo Cloudflare Registrar; resposta autenticada confirmada no resolvedor do Google.
- Proteção gerenciada gratuita da Cloudflare ativa. Bot Fight e Under Attack não foram habilitados.
- Regra de resposta `RadApps - security response headers`, restrita a estes dois hosts: `X-Content-Type-Options: nosniff`, `X-Frame-Options: DENY`, `Referrer-Policy: strict-origin-when-cross-origin`, `Permissions-Policy: camera=(), microphone=(), geolocation=()`, `Content-Security-Policy: frame-ancestors 'none'; upgrade-insecure-requests` e `Strict-Transport-Security: max-age=15552000`. A CSP HTTP complementa a CSP mais restritiva do HTML, cujo hash JSON-LD é calculado pelo gerador.
- Search Console: propriedade de domínio `radapps.app` verificada por TXT. Preservar esse registro DNS. Sitemap processado pelo Google, com 12 páginas encontradas; indexação solicitada e aceita para `/` e `/en/`. Isso não confirma inclusão no índice nem garante posição nos resultados.
- Metadados PT/EN, dados estruturados de organização/site/página/catálogo e alternâncias de idioma no sitemap. A página 404 retorna status 404 e `noindex`.

Validação: 12 páginas públicas com HTTP 200, cabeçalhos e JSON-LD corretos; robots e sitemap acessíveis; HTTP e www redirecionam corretamente; TLS 1.1 recusado e TLS 1.2 aceito; navegação PT/EN sem erros de console.

Cloudflare Web Analytics está habilitado com injeção automática para `radapps.app` (site `45f70c335f1f498594f25cbf9f16c0ff`). Não adicionar um segundo beacon ao HTML. A CSP permite scripts de `https://static.cloudflareinsights.com` e conexões ao próprio domínio (`/cdn-cgi/rum`), preservando as demais restrições. Privacidade e cookies descrevem a medição nos dois idiomas. O teste local não injeta o beacon: a injeção ocorre no proxy de produção.

As configurações da Cloudflare e o Search Console são externos ao repositório. Após troca de hospedagem, conferir certificado válido na origem, SSL estrito e redirecionamentos antes de alterar DNS. Não remover o certificado da origem: o proxy o valida. O HSTS exige que HTTPS continue disponível pelo prazo anunciado.

Revisão de busca em 18/09/2026: a inspeção individual no Search Console confirmou que a homepage em português está indexada; o relatório agregado de indexação ainda estava em processamento. O sitemap estava processado, com 12 páginas encontradas. Isso não equivale a 12 páginas indexadas nem comprova posicionamento ou tráfego orgânico.

A homepage descreve a finalidade dos seis aplicativos em português e inglês, com links para suas páginas originais. As páginas institucionais têm metadescrições específicas e `BreadcrumbList`. A página 404 permanece `noindex` e não declara traduções da homepage. Atualize `PAGE_MODIFIED` no gerador quando o conteúdo da página correspondente mudar; não atualize datas apenas por executar o build.

O cache da Cloudflare permite HTML das 12 páginas públicas sem parâmetros, cookies ou Authorization, respeitando o prazo da origem (600 segundos). CSS e JavaScript com `?v=` têm cache de um mês: manter os hashes atualizados é obrigatório. Após publicação, confira também as URLs sem parâmetros; um `?deploy=` verifica a origem, mas não comprova que o HTML comum saiu do cache.

## Documentos institucionais

Termos de uso, privacidade, cookies e preferências, aviso médico e acessibilidade, nos dois idiomas. Eles descrevem este site institucional e não substituem a documentação de cada aplicativo. O responsável é identificado como Álvaro Menezes; não foi inventado CNPJ, razão social ou registro sanitário. O e-mail de contato é o já publicado na homepage pessoal.

Antes de vendas, cadastros, outras formas de telemetria, processamento de dados de saúde ou publicação nas lojas, atualizar a documentação conforme a operação efetiva, confirmar os dados empresariais e obter revisão jurídica e avaliação regulatória específica dos produtos. Os avisos não conferem regularização sanitária.

Referências consultadas em 17/09/2026:

- [LGPD](https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709.htm)
- [ANPD — Cookies e proteção de dados pessoais](https://www.gov.br/anpd/pt-br/centrais-de-conteudo/materiais-educativos-e-publicacoes/guia_orientativo_cookies_e_protecao_de_dados_pessoais)
- [Anvisa — Software como dispositivo médico](https://www.gov.br/anvisa/pt-br/centraisdeconteudo/publicacoes/produtos-para-a-saude/manuais/software-como-dispositivo-medico-perguntas-e-respostas)
- [GitHub Pages — Domínio personalizado](https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site/managing-a-custom-domain-for-your-github-pages-site)
