# Projeto OpenClaw Shopee

## Objetivo
Criar ou atualizar um blog/site de afiliados usando os arquivos já gerados pela curadoria e pelo agente de conteúdo.

O resultado deve ser simples, bonito, responsivo e funcional para exibir produtos da Shopee selecionados por potencial comercial estimado.

## Pasta base
Use esta pasta como base:

```text
~/Documents/shopee/openclaw/
```

Se o usuário informar outro caminho, use o caminho informado.

## Pasta obrigatória de saída
Todo o blog deve ser criado ou atualizado dentro de:

```text
~/Documents/shopee/openclaw/site_openclaw/
```

Regras:

- não criar pasta paralela fora de `site_openclaw/`
- não espalhar arquivos do site fora de `site_openclaw/`
- preservar os arquivos que já existirem em `site_openclaw/`, especialmente `hero.png` e `data/`

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

Se algum arquivo não existir, continuar com os disponíveis e registrar a ausência em log.

## Arquivos alternativos
Se `produtos_escolhidos.*` não existir, usar nesta ordem:

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

## Linguagem pública
A comunicação do site deve ser pensada para público final, com linguagem comercial simples, clara e convidativa.

Preferir:

- títulos fáceis de entender
- chamadas curtas e diretas
- foco em utilidade, estilo, preço e contexto de uso
- texto que ajude a pessoa a explorar e comprar
- sensação de vitrine organizada e confiável

Evitar:

- linguagem técnica
- explicação de bastidor
- termos de laboratório, curadoria interna ou análise de dados
- promessas exageradas ou afirmações que não possam ser sustentadas

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
- seção Hero
- produtos em destaque
- grade de produtos
- filtro por categoria
- página ou seção de blog
- cards de produto
- botão para acessar o produto
- rodapé simples

## Hero
Criar um Hero visual com:

- título claro
- subtítulo curto
- chamada para ver os achadinhos
- imagem Hero ou placeholder

Usar a ideia de:

```text
imagem/prompt_hero_blog_openclaw.md
```

Se já existir `site_openclaw/hero.png`, usar esse arquivo.

Se não houver imagem final, criar placeholder visual bonito e registrar a pendência.

## Produtos
Usar o melhor JSON de produtos disponível.

Cada card deve exibir, quando houver:

- imagem
- título limpo
- categoria
- preço
- rating
- status de oportunidade
- motivo da escolha
- CTA para abrir o link original

Se existir `link_gerado_shopee`, usar esse link.
Se não existir `link_gerado_shopee`, não publicar o produto no site.

Regras:

- não usar `product_url` como fallback público
- não criar botão falso
- não exibir produto com link pendente
- publicar apenas produtos com link final pronto para clique

## Blog
Usar os artigos existentes em:

```text
blog/artigos/
```

Criar area de blog com:

- listagem de artigos
- título
- descrição curta
- categoria
- slug
- link para leitura

Se os artigos estiverem em Markdown, renderizar ou converter para páginas estáticas.

Se não houver conteúdo real, não inventar artigos. Mostrar claramente que o conteúdo está em preparação.

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
- palavras-chave secundárias

Não inventar SEO se os campos não existirem.

## Assets
Organizar assets em:

```text
site_openclaw/assets/
```

Se for necessário gerar imagem ou vídeo por API:

- pedir aprovação antes
- mostrar o prompt usado
- mostrar o caminho de saída
- mostrar o nome do arquivo

Só gerar após aprovação explícita.

## Implementacao
Se ainda não houver projeto criado, preferir:

```text
HTML, CSS e JavaScript simples
```

Se já existir stack pronta no local, aproveitar a stack existente.

Não complicar a arquitetura sem necessidade.

## Estilo visual
Usar um estilo:

- limpo
- leve
- moderno
- comercial
- responsivo
- agradável para blog de achadinhos
- com bom espaçamento
- com cards bem legíveis
- com visual confiável

Evitar:

- visual poluído
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
- decisões tomadas
- confirmação de que nada foi criado fora de `site_openclaw/`

## Validação final
Antes de encerrar, validar:

- site criado ou atualizado
- produtos carregando corretamente
- blog/artigos aparecendo quando existirem
- links de produtos preservados
- linguagem pública comercial, clara e sem exposição técnica de bastidor
- layout responsivo básico funcionando
- logs atualizados

## Resultado esperado
Ao final, entregar somente:

```text
1. resumo curto do que foi criado
2. caminho da pasta do site
3. arquivos principais criados ou alterados
4. como rodar/testar localmente
5. pendências ou limitações encontradas
```
