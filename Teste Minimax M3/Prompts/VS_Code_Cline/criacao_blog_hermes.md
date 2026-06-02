# PROMPT CLINE — CRIAR BLOG DE AFILIADOS SHOPEE

Crie um blog/site de afiliados usando os arquivos já gerados pela curadoria e pelo agente de conteúdo.

## Pasta base do projeto

Use esta pasta como base:

```text
~/Documents/shopee/hermes/
```

Se eu informar outro caminho, use o caminho informado.

## Objetivo

Criar um blog/site simples, bonito, responsivo e funcional para exibir produtos da Shopee selecionados por **potencial comercial estimado**.

O site deve usar os dados e conteúdos já gerados nas etapas anteriores.

## Arquivos de entrada

Use como base principal:

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

Se algum arquivo não existir, continue com os arquivos disponíveis e registre a ausência em um log.

## Regras de linguagem

Não use:

```text
mais vendido
campeão de vendas
produto que mais vende
venda comprovada
sucesso garantido
```

Use linguagem como:

```text
potencial comercial estimado
produto bem avaliado no dataset
preço dentro do recorte analisado
boa aderência ao ticket de R$ 20 a R$ 80
categoria com prioridade comercial
curadoria de achadinhos
```

## Estrutura do site

Crie um site com:

```text
página inicial
seção Hero
seção de produtos em destaque
grade de produtos
filtro por categoria
filtro por status de oportunidade
filtro por faixa de preço
página ou seção de blog
páginas/artigos de blog
cards de produto
botão para acessar o produto original
aviso metodológico
rodapé simples
```

## Hero

Crie um Hero visual para o blog com:

```text
título claro
subtítulo curto
chamada para ver os achadinhos
imagem ou espaço reservado para imagem Hero
```

Use a ideia do arquivo:

```text
imagem/prompt_hero_blog_hermes.md
```

Se já existir imagem gerada, use-a.

Procure por imagens em:

```text
assets_generated/images/
site_hermes/public/images/
```

Se não houver imagem, crie um placeholder visual bonito e registre que a imagem final ainda precisa ser gerada.

## Produtos

Use:

```text
data/final/produtos_escolhidos.json
```

Cada card de produto deve exibir:

```text
imagem
título limpo
categoria
preço
rating
status de oportunidade
motivo da escolha
CTA para abrir o link original
```

O botão do produto deve apontar para:

```text
product_url
```

Se `product_url` estiver ausente, não criar botão falso.

## Blog

Use os artigos existentes em:

```text
blog/artigos/
```

Crie uma área de blog com:

```text
listagem de artigos
título do artigo
descrição curta
categoria
slug
link para leitura
```

Se os artigos estiverem em Markdown, implemente leitura/renderização simples ou converta para páginas estáticas.

## SEO

Use os arquivos:

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

Não invente SEO se os campos não existirem.

## Aviso metodológico obrigatório

Inclua no site um aviso visível, em linguagem simples:

```text
Os produtos exibidos foram selecionados por potencial comercial estimado com base no dataset analisado, considerando preço, rating, categoria e qualidade do cadastro. O dataset não contém quantidade vendida, portanto este site não afirma que os produtos são os mais vendidos.
```

## Assets

Organize os assets em:

```text
site_hermes/public/images/
site_hermes/public/videos/
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

Se ainda não houver projeto criado, crie um site simples usando uma stack adequada.

Preferência:

```text
HTML, CSS e JavaScript simples
```

Se já existir projeto React, Vite ou Next.js, aproveite a stack existente.

Não complique a arquitetura sem necessidade.

## Estilo visual

Use um estilo:

```text
limpo
leve
moderno
comercial
responsivo
agradável para blog de achadinhos
bom espaçamento
cards bem legíveis
visual confiável
```

Evite:

```text
visual poluído
cores agressivas demais
excesso de banners
texto pequeno
cards confusos
promessas exageradas
```

## Logs

Crie ou atualize:

```text
logs/site_build_log.md
```

Registre:

```text
arquivos de entrada usados
arquivos ausentes
estrutura criada
componentes criados
assets usados
erros encontrados
decisões tomadas
```

## Validação final

Antes de encerrar, valide:

```text
site criado ou atualizado
produtos carregando corretamente
blog/artigos aparecendo
links de produtos preservados
aviso metodológico visível
layout responsivo básico funcionando
logs atualizados
```

## Resultado esperado

Ao final, entregue somente:

```text
1. resumo curto do que foi criado
2. caminho da pasta do site
3. arquivos principais criados ou alterados
4. como rodar/testar localmente
5. pendências ou limitações encontradas
```