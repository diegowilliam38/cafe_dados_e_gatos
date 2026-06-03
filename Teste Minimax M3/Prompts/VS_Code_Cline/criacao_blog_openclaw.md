# PROMPT CLINE — CRIAR BLOG DE AFILIADOS SHOPEE COM DADOS DO OPENCLAW

Crie um blog/site de afiliados usando os arquivos já gerados pela curadoria feita no OpenClaw.

A parte de imagem é separada.  
Não gere imagem automaticamente nesta etapa.

---

## Pasta base do projeto

Use esta pasta como base:

```text
~/Documents/shopee/openclaw/

Se eu informar outro caminho, use o caminho informado.

Objetivo

Criar um blog/site simples, bonito, responsivo e funcional para exibir produtos da Shopee selecionados por potencial comercial estimado.

O site deve usar os dados já gerados pela curadoria do OpenClaw.

O foco é criar uma estrutura funcional para exibir produtos, categorias, filtros, cards e aviso metodológico.

Arquivos de entrada principais

Use como fonte principal de produtos:

data/final/produtos_escolhidos.json
data/final/produtos_escolhidos.csv

Se esses arquivos não existirem, use como fallback:

data/final/produtos_site_por_categoria.json
data/final/produtos_site_por_categoria.csv

Se nenhum desses arquivos existir, pare e avise Denise.

Arquivos opcionais

Use se existirem:

blog/pautas/01_mapa_editorial.md
blog/pautas/02_pautas_blog.json
blog/pautas/02_pautas_blog.md
blog/artigos/
blog/seo/seo_blog.json
blog/seo/seo_blog.csv

Se algum arquivo opcional não existir, continue com os arquivos disponíveis e registre a ausência no log.

Parte de imagem

A parte de imagem é um prompt separado.

Não gere imagem nesta etapa.

Não use API de imagem nesta etapa.

Não crie prompt de imagem nesta etapa.

Apenas prepare o site para receber imagem futuramente.

O Hero deve ter:

título claro
subtítulo curto
chamada para ver os achadinhos
espaço reservado para imagem Hero

Se já existir imagem pronta, use-a.

Procure por imagens em:

assets_generated/images/
site_openclaw/public/images/

Se não houver imagem, crie um placeholder visual bonito e registre no log:

imagem hero ainda não gerada
Regras de linguagem

Não use:

mais vendido
campeão de vendas
produto que mais vende
venda comprovada
sucesso garantido
garantia de venda
garantia de comissão

Use linguagem como:

potencial comercial estimado
produto bem avaliado no dataset
preço dentro do recorte analisado
boa aderência ao ticket de R$ 20 a R$ 80
categoria com prioridade comercial
curadoria de achadinhos
produto selecionado pela curadoria
Estrutura do site

Crie um site com:

página inicial
seção Hero
seção de produtos em destaque
grade de produtos
filtro por categoria
filtro por status de oportunidade
filtro por faixa de preço
página ou seção de blog, se houver artigos
cards de produto
botão para acessar o produto original
aviso metodológico
rodapé simples
Stack preferida

Use preferencialmente:

HTML
CSS
JavaScript simples

Se já existir projeto React, Vite ou Next.js dentro da pasta, aproveite a stack existente.

Não complique a arquitetura sem necessidade.

Pasta do site

Crie ou atualize o site em:

site_openclaw/

Organize os arquivos principais assim, se estiver usando HTML, CSS e JavaScript simples:

site_openclaw/
├── index.html
├── produtos.html
├── blog.html
├── css/
│   └── style.css
├── js/
│   └── app.js
├── data/
│   ├── produtos_escolhidos.json
│   └── produtos_site_por_categoria.json
└── public/
    ├── images/
    └── videos/

Se a estrutura existente for diferente, adapte sem apagar arquivos importantes.

Dados dos produtos

O site deve carregar os produtos a partir de:

site_openclaw/data/produtos_escolhidos.json

Se o arquivo original usado for:

data/final/produtos_escolhidos.json

copie para:

site_openclaw/data/produtos_escolhidos.json

Se o fallback usado for:

data/final/produtos_site_por_categoria.json

copie para:

site_openclaw/data/produtos_escolhidos.json

Assim o site sempre lê o mesmo arquivo final.

Campos esperados dos produtos

Cada produto pode conter campos como:

itemid
categoria_final
title_clean
sale_price
item_rating
image_link
product_url
product_link
product_short link
link_gerado_shopee
status_oportunidade
motivo_escolha
score_potencial_comercial

Se algum campo não existir, adapte usando os campos disponíveis.

Regra para URL do produto

O botão do produto deve apontar para o melhor link disponível nesta ordem:

link_gerado_shopee
product_url
product_short link
product_link

Se nenhum link existir, não criar botão falso.

Não inventar link.

Não alterar link original.

Não adicionar parâmetro manualmente.

Não criar link de afiliado automaticamente.

Cards de produto

Cada card deve exibir, quando disponível:

imagem
título limpo
categoria
preço
rating
status de oportunidade
motivo da escolha
botão para acessar o produto original

Se image_link existir, usar como imagem do produto.

Se não existir imagem, usar placeholder visual simples.

Categorias

O site deve trabalhar com estas categorias:

moda
beleza
acessórios para celular
casa
cozinha
organização
pets
papelaria
infantil
fitness

Criar filtro por categoria.

O site deve suportar no máximo:

20 produtos por categoria
200 produtos no total

Se o arquivo tiver mais de 20 produtos em alguma categoria, exibir apenas os 20 primeiros daquela categoria e registrar no log.

Filtros

Criar filtros simples para:

categoria
status de oportunidade
faixa de preço

Faixas de preço sugeridas:

R$ 20 a R$ 40
R$ 40 a R$ 60
R$ 60 a R$ 80

Se status_oportunidade não existir, criar uma classificação simples no front-end com base no score:

score alto = destaque
score médio = boa oportunidade
score baixo = oportunidade moderada

Se não houver score, ocultar esse filtro ou usar apenas categoria e preço.

Produtos em destaque

Na página inicial, exibir uma seção de produtos em destaque.

Critério:

maior score_potencial_comercial
melhor item_rating
produto com imagem
produto com link válido

Mostrar poucos produtos na home.

Sugestão:

8 a 12 produtos em destaque
Blog

Se existirem artigos em:

blog/artigos/

crie uma área de blog com:

listagem de artigos
título do artigo
descrição curta
categoria
slug
link para leitura

Se os artigos estiverem em Markdown, implemente leitura/renderização simples ou converta para páginas estáticas.

Se não houver artigos, crie apenas uma seção simples dizendo:

Em breve, novos guias de achadinhos e curadorias por categoria.
SEO

Se existirem:

blog/seo/seo_blog.json
blog/seo/seo_blog.csv

aplique quando possível:

title
meta description
slug
palavra-chave principal
palavras-chave secundárias

Não invente SEO se os campos não existirem.

Se não houver SEO, crie metadados simples e honestos para o site.

Aviso metodológico obrigatório

Inclua no site um aviso visível, em linguagem simples:

Os produtos exibidos foram selecionados por potencial comercial estimado com base no dataset analisado, considerando preço, rating, categoria e qualidade do cadastro. O dataset não contém quantidade vendida, portanto este site não afirma que os produtos são os mais vendidos.

Esse aviso deve aparecer na página inicial e/ou no rodapé.

Estilo visual

Use um estilo:

limpo
leve
moderno
comercial
responsivo
agradável para blog de achadinhos
bom espaçamento
cards bem legíveis
visual confiável

Evite:

visual poluído
cores agressivas demais
excesso de banners
texto pequeno
cards confusos
promessas exageradas
Assets

Organize os assets em:

site_openclaw/public/images/
site_openclaw/public/videos/

Não gere imagem.

Não gere vídeo.

Não chame API de imagem.

Não chame API de vídeo.

Apenas use arquivos existentes ou placeholders.

Log obrigatório

Crie ou atualize:

logs/site_build_log.md

Registrar:

data e hora da execução
arquivos de entrada usados
arquivos ausentes
arquivo de produtos usado
estrutura criada
componentes criados
assets usados
se imagem hero foi encontrada ou não
erros encontrados
decisões tomadas
Validação final

Antes de encerrar, valide:

site criado ou atualizado
arquivo de produtos copiado para site_openclaw/data/
produtos carregando corretamente
filtros funcionando
links de produtos preservados
aviso metodológico visível
layout responsivo básico funcionando
blog criado ou placeholder exibido
logs atualizados
nenhuma imagem foi gerada automaticamente
nenhum vídeo foi gerado automaticamente
Resultado esperado

Ao final, entregue somente:

1. resumo curto do que foi criado
2. caminho da pasta do site
3. arquivos principais criados ou alterados
4. como rodar/testar localmente
5. pendências ou limitações encontradas
Observação final

Este site deve consumir a saída da curadoria feita no OpenClaw.

A curadoria pode vir com os nomes:

produtos_escolhidos.json
produtos_escolhidos.csv

ou, como fallback:

produtos_site_por_categoria.json
produtos_site_por_categoria.csv

O site deve funcionar com os arquivos disponíveis, sem inventar dados, sem prometer vendas e sem gerar assets visuais nesta etapa.
