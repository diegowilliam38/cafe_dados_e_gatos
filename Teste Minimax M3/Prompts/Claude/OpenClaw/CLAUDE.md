# Projeto OpenClaw Shopee

## Objetivo
Criar ou atualizar um blog/site de afiliados usando os arquivos ja gerados pela curadoria e pelo agente de conteudo.

O resultado deve ser simples, bonito, responsivo e funcional para exibir produtos da Shopee selecionados por potencial comercial estimado.

## Pasta base
Use esta pasta como base:

```text
~/Documents/shopee/openclaw/
```

Se o usuario informar outro caminho, use o caminho informado.

## Pasta obrigatoria de saida
Todo o blog deve ser criado ou atualizado dentro de:

```text
~/Documents/shopee/openclaw/site_openclaw/
```

Regras:

- nao criar pasta paralela fora de `site_openclaw/`
- nao espalhar arquivos do site fora de `site_openclaw/`
- preservar os arquivos que ja existirem em `site_openclaw/`, especialmente `hero.png` e `data/`

## Arquivos de entrada
Usar como base principal, quando existirem:

```text
data/final/produtos_escolhidos.json
data/final/produtos_escolhidos.csv
blog/pautas/01_mapa_editorial.md
blog/pautas/02_pautas_blog.json
blog/pautas/02_pautas_blog.md
blog/artigos/
blog/seo/seo_blog.json
blog/seo/seo_blog.csv
imagem/prompt_hero_blog_openclaw.md
video_api/prompts/
video_api/roteiros/
```

Se algum arquivo nao existir, continuar com os disponiveis e registrar a ausencia em log.

## Arquivos alternativos
Se `produtos_escolhidos.*` nao existir, usar nesta ordem:

```text
data/final/produtos_curadoria_final.json
data/final/produtos_curadoria_final.csv
data/final/produtos_site_por_categoria.json
data/final/produtos_site_por_categoria.csv
site_openclaw/data/produtos_site_por_categoria.json
site_openclaw/data/produtos_site_por_categoria.csv
```

Para links, priorizar:

```text
site_openclaw/data/links_shopee_manual.csv
data/final/links_shopee_manual.csv
```

## Regras de linguagem
Nao use:

```text
mais vendido
campeao de vendas
produto que mais vende
venda comprovada
sucesso garantido
```

Usar linguagem como:

```text
potencial comercial estimado
curadoria de achadinhos
produto bem avaliado dentro do recorte analisado
preco dentro do recorte analisado
categoria com prioridade comercial
```

## Estrutura esperada do site
Criar dentro de `site_openclaw/`:

```text
index.html
produtos.html
blog.html
anuncios-top10.html
assets/
```

O site deve ter:

- pagina inicial
- secao Hero
- produtos em destaque
- grade de produtos
- filtro por categoria
- pagina ou secao de blog
- cards de produto
- botao para acessar o produto
- rodape simples

## Hero
Criar um Hero visual com:

- titulo claro
- subtitulo curto
- chamada para ver os achadinhos
- imagem Hero ou placeholder

Usar a ideia de:

```text
imagem/prompt_hero_blog_openclaw.md
```

Se ja existir `site_openclaw/hero.png`, usar esse arquivo.

Se nao houver imagem final, criar placeholder visual bonito e registrar a pendencia.

## Produtos
Usar o melhor JSON de produtos disponivel.

Cada card deve exibir, quando houver:

- imagem
- titulo limpo
- categoria
- preco
- rating
- status de oportunidade
- motivo da escolha
- CTA para abrir o link original

Se existir `link_gerado_shopee`, usar esse link.
Se nao existir `link_gerado_shopee` mas existir `product_url`, usar `product_url`.
Se nenhum link existir, nao criar botao falso.

## Blog
Usar os artigos existentes em:

```text
blog/artigos/
```

Criar area de blog com:

- listagem de artigos
- titulo
- descricao curta
- categoria
- slug
- link para leitura

Se os artigos estiverem em Markdown, renderizar ou converter para paginas estaticas.

Se nao houver conteudo real, nao inventar artigos. Mostrar claramente que o conteudo esta em preparacao.

## SEO
Usar, quando existirem:

```text
blog/seo/seo_blog.json
blog/seo/seo_blog.csv
```

Aplicar quando possivel:

- title
- meta description
- slug
- palavra-chave principal
- palavras-chave secundarias

Nao inventar SEO se os campos nao existirem.

## Metodologia
A metodologia deve orientar a escrita e a selecao do conteudo, mas nao deve aparecer como aviso tecnico na interface publica.

Regras:

- nao expor texto de bastidor, auditoria ou laboratorio na pagina publica
- nao explicar dataset, heuristica, score interno ou processo de curadoria automatizada para o visitante final
- usar isso apenas como regra interna para manter linguagem segura e coerente
- a comunicacao publica deve parecer editorial e comercial, nao tecnica

## Assets
Organizar assets em:

```text
site_openclaw/assets/
```

Se for necessario gerar imagem ou video por API:

- pedir aprovacao antes
- mostrar o prompt usado
- mostrar o caminho de saida
- mostrar o nome do arquivo

So gerar apos aprovacao explicita.

## Implementacao
Se ainda nao houver projeto criado, preferir:

```text
HTML, CSS e JavaScript simples
```

Se ja existir stack pronta no local, aproveitar a stack existente.

Nao complicar a arquitetura sem necessidade.

## Estilo visual
Usar um estilo:

- limpo
- leve
- moderno
- comercial
- responsivo
- agradavel para blog de achadinhos
- com bom espacamento
- com cards bem legiveis
- com visual confiavel

Evitar:

- visual poluido
- cores agressivas demais
- excesso de banners
- texto pequeno
- cards confusos
- promessas exageradas

## Logs
Criar ou atualizar:

```text
logs/site_build_log.md
```

Registrar:

- arquivos de entrada usados
- arquivos ausentes
- estrutura criada
- componentes criados
- assets usados
- erros encontrados
- decisoes tomadas
- confirmacao de que nada foi criado fora de `site_openclaw/`

## Validacao final
Antes de encerrar, validar:

- site criado ou atualizado
- produtos carregando corretamente
- blog/artigos aparecendo quando existirem
- links de produtos preservados
- linguagem publica comercial, clara e sem exposicao tecnica de bastidor
- layout responsivo basico funcionando
- logs atualizados

## Resultado esperado
Ao final, entregar somente:

```text
1. resumo curto do que foi criado
2. caminho da pasta do site
3. arquivos principais criados ou alterados
4. como rodar/testar localmente
5. pendencias ou limitacoes encontradas
```
