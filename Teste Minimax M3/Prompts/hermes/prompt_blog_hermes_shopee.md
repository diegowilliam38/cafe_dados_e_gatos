# PROMPT CLINE — CRIAR BLOG DE PRODUTOS SHOPEE COM HERMES

Crie um blog moderno de produtos da Shopee usando os arquivos já gerados pela curadoria Hermes e pelo agente de conteúdo.

O objetivo é entregar um blog bonito, responsivo, funcional e fácil de publicar, com aparência comercial e editorial.

Use uma stack simples e adequada para o resultado. Pode usar HTML, CSS, JavaScript, React, Tailwind CSS, Vite ou outra estrutura simples de front-end.

## Pasta base do projeto

Use esta pasta como base:

```text
~/Documents/shopee/hermes/
```

Se eu informar outro caminho, use o caminho informado.

## Objetivo do blog

Criar um blog de achados, recomendações e conteúdos sobre produtos da Shopee.

O blog deve usar os dados e conteúdos já gerados nas etapas anteriores.

A comunicação deve parecer de um blog real de produtos, não de relatório técnico.

Use linguagem simples, comercial e natural.

Exemplos de linguagem adequada:

```text
achados selecionados para facilitar sua escolha
produtos organizados para você explorar
ideias úteis para o dia a dia
opções interessantes para conhecer
seleções simples para ajudar na decisão
```

## Arquivos de entrada

Use como base principal os arquivos disponíveis em:

```text
data/final/produtos_escolhidos.json
data/final/produtos_escolhidos.csv
data/final/links_shopee_manual.csv
blog/pautas/01_mapa_editorial.md
blog/pautas/02_pautas_blog.json
blog/pautas/02_pautas_blog.md
blog/artigos/
blog/seo/seo_blog.json
blog/seo/seo_blog.csv
imagem/prompt_hero_blog_hermes.md
video_api/prompts/
video_api/roteiros/
```

Se algum arquivo não existir, continue com os arquivos disponíveis e registre a ausência no log.

## Estrutura do blog

Crie um blog com estas áreas principais:

```text
Home
Produtos
Blog
Anúncios copiáveis
```

A estrutura pode ser feita com arquivos HTML ou com componentes/rotas React, conforme a solução escolhida.

O resultado final deve entregar páginas ou rotas equivalentes a:

```text
index.html
produtos.html
blog.html
anuncios-top10.html
```

## Home

A home deve apresentar o blog e destacar alguns produtos.

Inclua:

```text
cabeçalho com nome do blog
menu simples
seção Hero bonita
chamada para ver os produtos
chamada para acessar conteúdos do blog
produtos em destaque
bloco curto explicando o propósito do blog
rodapé
```

Use a ideia do arquivo:

```text
imagem/prompt_hero_blog_hermes.md
```

Se já existir imagem gerada, use-a.

Procure por imagens em:

```text
assets_generated/images/
blog_hermes/public/images/
```

Se não houver imagem, crie um placeholder visual bonito e registre que a imagem final ainda precisa ser gerada.

## Produtos

Use o arquivo principal:

```text
data/final/produtos_escolhidos.json
```

Cada card de produto deve exibir, quando disponível:

```text
imagem
título limpo
categoria
preço
rating
descrição curta
motivo comercial em linguagem simples
botão de ação
status de link pendente, quando necessário
```

Use as imagens disponíveis nos dados dos produtos.

Priorize campos como:

```text
image_url
image_link
```

Se algum produto não tiver imagem, use um placeholder simples.

## Links dos produtos

Use `itemid` para cruzar os produtos com o arquivo:

```text
data/final/links_shopee_manual.csv
```

A coluna correta para o botão final do produto é:

```text
link_gerado_shopee
```

Quando `link_gerado_shopee` estiver preenchido, use esse link no botão.

Quando `link_gerado_shopee` estiver vazio, mostre:

```text
Link pendente
```

Use textos de botão como:

```text
Ver produto
Conferir oferta
Ver na Shopee
```

Abra links externos em nova aba com atributos adequados para links patrocinados.

Preserve `product_url` apenas como dado original, se existir. O botão final do blog deve usar `link_gerado_shopee`.

## Blog

Use os conteúdos existentes em:

```text
blog/artigos/
blog/pautas/
blog/seo/
blog/referencias/
```

Crie uma área editorial com:

```text
listagem de artigos
cards de leitura
título do conteúdo
descrição curta
categoria
slug ou link interno
```

Se os artigos estiverem em Markdown, implemente leitura/renderização simples ou converta para páginas estáticas.

Se não houver conteúdo real, mostre uma mensagem simples de conteúdo em preparação.

Exemplo:

```text
Conteúdo em preparação. Em breve, este blog terá dicas, listas e achados selecionados para ajudar você a escolher melhor.
```

## SEO

Use os arquivos disponíveis em:

```text
blog/seo/seo_blog.json
blog/seo/seo_blog.csv
```

Aplique quando possível:

```text
title
meta description
slug
palavra-chave principal
palavras-chave secundárias
```

## Página oculta de anúncios copiáveis

Crie uma página auxiliar chamada:

```text
anuncios-top10.html
```

Essa página será usada apenas para copiar anúncios em HTML.

Ela deve ser acessível por URL direta e não deve aparecer no menu, na home, no rodapé, na página de produtos nem na página do blog.

Inclua na página:

```html
<meta name="robots" content="noindex,nofollow">
```

Use apenas os 10 primeiros produtos da lista final.

Para cada produto, crie:

```text
uma prévia visual do anúncio
um bloco com o código HTML copiável
um botão para copiar o código
um status indicando se o link está preenchido ou pendente
```

O código copiável deve ser HTML simples, com CSS inline e independente do layout principal do blog.

O código copiável deve conter:

```text
imagem
nome do produto
preço, quando existir
botão de chamada para ação
CSS inline
```

Para o link do anúncio:

```text
se link_gerado_shopee estiver preenchido, usar link_gerado_shopee
se link_gerado_shopee estiver vazio, usar "#LINK_GERADO_SHOPEE_PENDENTE"
```

Se o link estiver pendente, mostre aviso claro para Denise preencher o link antes de publicar o anúncio.

## Visual desejado

O blog deve ter aparência moderna, bonita e comercial.

Priorize:

```text
layout limpo
boa leitura
responsividade no celular
cards organizados
imagens proporcionais
botões claros
menu simples
rodapé bem acabado
aparência de blog confiável
```

Pode usar Tailwind, componentes React ou CSS próprio para melhorar o visual.

## Linguagem do blog

Use linguagem comercial simples, natural e segura.

Evite promessas exageradas ou afirmações que dependem de dados não disponíveis, como:

```text
mais vendido
campeão de vendas
produto que mais vende
venda comprovada
sucesso garantido
garantia de venda
garantia de comissão
melhor produto do mercado
```

Evite expor termos técnicos internos nas páginas principais do blog, como:

```text
dataset
score
ranking heurístico
modelo usado
CSV
curadoria automatizada
```

Esses termos podem aparecer apenas em logs técnicos, se necessário.

## Assets

Organize os assets em:

```text
blog_hermes/public/images/
blog_hermes/public/videos/
```

Se for necessário gerar imagem ou vídeo usando API configurada no projeto, peça aprovação antes de executar.

Antes de gerar qualquer asset visual, mostre:

```text
prompt usado
caminho de saída
nome do arquivo
```

Só gere após aprovação explícita.

## Implementação

Crie ou atualize o projeto dentro de:

```text
~/Documents/shopee/hermes/blog_hermes/
```

Escolha a implementação que entregar melhor resultado visual e que seja simples de revisar.

Pode usar:

```text
HTML/CSS/JS simples
React com Vite
Tailwind CSS
componentes próprios
```

## Log obrigatório

Ao final, crie ou atualize:

```text
logs/blog_build_log.md
```

Registre:

```text
tecnologia usada
arquivos criados ou alterados
arquivos de entrada encontrados
arquivos de entrada ausentes
quantidade de produtos carregados
quantidade de produtos com link preenchido
quantidade de produtos com link pendente
conteúdos de blog encontrados
pendências
como rodar ou abrir o blog localmente
```

## Validação

Antes de finalizar, confira:

```text
produtos_escolhidos.json existe
produtos_escolhidos.csv existe
links_shopee_manual.csv existe
os produtos foram carregados
o cruzamento por itemid foi feito
os links usam link_gerado_shopee quando preenchido
produtos sem link mostram Link pendente
a home parece um blog moderno
a página de produtos está organizada em cards
a página de blog usa conteúdo real quando existir
a página de blog não inventa artigos quando não houver conteúdo
anuncios-top10.html foi criada
anuncios-top10.html usa apenas os 10 primeiros produtos
anuncios-top10.html não aparece no menu nem na home
os anúncios copiáveis têm HTML simples com CSS inline
nenhum link da Shopee foi alterado automaticamente
```

## Resultado esperado

Ao final, informe:

```text
tecnologia usada
páginas ou componentes criados/atualizados
quantidade de produtos carregados
quantidade de produtos com link preenchido
quantidade de produtos com link pendente
caminho da página anuncios-top10.html
se a página de blog encontrou conteúdo real ou ficou como conteúdo em preparação
qualquer erro ou pendência encontrada
```
