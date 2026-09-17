# RadApps

Site institucional bilíngue de aplicativos para Radiologia.

- Produção: https://radapps.app
- Repositório: https://github.com/alvaroajm/RadApps
- Hospedagem: GitHub Pages, branch `main`, raiz; domínio e DNS na Cloudflare.
- Referência visual: https://alvaro-menezes.com — fonte conferida no commit `437f07b5947f628b07af61ae7f11d0812a357688` em 17/09/2026.

## Desenvolvimento

```sh
python3 scripts/build_site.py
python3 scripts/check_site.py
node --check assets/site.js
node --check assets/theme-init.js
python3 -m http.server 4173 --bind 127.0.0.1
```

Abra http://127.0.0.1:4173. Não há dependências de build, cadastro, banco de dados, telemetria, cookies de marketing ou upload de exames.

O gerador mantém páginas completas em português e inglês, metadados, URLs canônicas, hreflang e sitemap. Edite o conteúdo em `scripts/build_site.py` e execute o gerador; evite alterar manualmente os HTML gerados. Os ativos locais são versionados por SHA-256. O tema utiliza apenas `radapps-theme` no localStorage; idioma é mantido na URL.

## Conteúdo e identidade

As duas imagens de marca foram fornecidas pelo proprietário e são preservadas integralmente. Os ícones e descrições dos cinco aplicativos são os da homepage pessoal; os aplicativos continuam hospedados nos destinos originais. Não foram copiadas calculadoras nem declaradas versões nas lojas.

As fontes Inter e Playfair Display são servidas localmente; licenças em `assets/fonts`. A publicação do código não concede autorização de uso da marca ou de materiais de terceiros.

## Publicação

Confirme o remoto `alvaroajm/RadApps`, `CNAME=radapps.app` e a zona `radapps.app` antes de qualquer alteração. Gere, valide, faça commit e push para `main`. Confira a implantação de Pages e as respostas HTTPS no domínio, incluindo os hashes dos ativos.

## Documentos institucionais

Termos de uso, privacidade, cookies e preferências, aviso médico e acessibilidade, nos dois idiomas. Eles descrevem este site institucional e não substituem a documentação de cada aplicativo. O responsável é identificado como Álvaro Menezes; não foi inventado CNPJ, razão social ou registro sanitário. O e-mail de contato é o já publicado na homepage pessoal.

Antes de vendas, cadastros, telemetria, processamento de dados de saúde ou publicação nas lojas, atualizar a documentação conforme a operação efetiva, confirmar os dados empresariais e obter revisão jurídica e avaliação regulatória específica dos produtos. Os avisos não conferem regularização sanitária.

Referências consultadas em 17/09/2026:

- [LGPD](https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709.htm)
- [ANPD — Cookies e proteção de dados pessoais](https://www.gov.br/anpd/pt-br/centrais-de-conteudo/materiais-educativos-e-publicacoes/guia_orientativo_cookies_e_protecao_de_dados_pessoais)
- [Anvisa — Software como dispositivo médico](https://www.gov.br/anvisa/pt-br/centraisdeconteudo/publicacoes/produtos-para-a-saude/manuais/software-como-dispositivo-medico-perguntas-e-respostas)
- [GitHub Pages — Domínio personalizado](https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site/managing-a-custom-domain-for-your-github-pages-site)
