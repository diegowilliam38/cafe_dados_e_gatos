# Projeto OpenClaw Shopee

## Checklist

### Pasta base
Usar:

```text
~/Documents/shopee/openclaw/
```

Se o usuário informar outro caminho, usar o caminho informado.

### Pasta de saída
Criar ou atualizar o blog somente em:

```text
~/Documents/shopee/openclaw/site_openclaw/
```

- não criar pasta paralela fora de `site_openclaw/`
- não criar arquivos do site fora de `site_openclaw/`
- preservar arquivos já existentes em `site_openclaw/`, principalmente `hero.png` e `data/`

### Arquivos de entrada principais
Usar, quando existirem:

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

Se algum arquivo não existir, continuar com os disponíveis e registrar a ausência em `logs/site_build_log.md`.

### Arquivos alternativos
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

### Estrutura esperada
Criar dentro de `site_openclaw/`:

```text
index.html
produtos.html
blog.html
anuncios-top10.html
assets/
```

### Hero

- usar `imagem/prompt_hero_blog_openclaw.md` como referência
- se `site_openclaw/hero.png` existir, usar esse arquivo
- se não existir imagem final, criar placeholder e registrar isso no log

### Produtos

- usar o melhor JSON disponível
- cada card deve exibir imagem, título, categoria, preço, rating e CTA
- se existir `link_gerado_shopee`, usar esse link
- se não existir `link_gerado_shopee`, não publicar o produto
- não usar `product_url` como fallback público
- não exibir produto com link pendente

### Blog

- usar `blog/artigos/` se existir
- se houver conteúdo real, listar e renderizar
- se não houver conteúdo real, não inventar artigos

### SEO

- usar `blog/seo/seo_blog.json` e `blog/seo/seo_blog.csv` se existirem
- aplicar apenas os campos que existirem

### Assets

- organizar assets em `site_openclaw/assets/`
- se precisar gerar imagem ou vídeo por API, pedir aprovação antes
- antes de gerar, mostrar prompt, caminho de saída e nome do arquivo

### Implementação

- preferir HTML, CSS e JavaScript simples
- se já existir stack pronta no local, aproveitar a stack existente

### Log
Criar ou atualizar:

```text
logs/site_build_log.md
```

Registrar:

- arquivos usados
- arquivos ausentes
- estrutura criada
- assets usados
- erros encontrados
- decisões tomadas
- confirmação de que nada foi criado fora de `site_openclaw/`

### Validação final

- confirmar que o site foi criado ou atualizado
- confirmar que os produtos carregam corretamente
- confirmar que só há produtos publicados com `link_gerado_shopee`
- confirmar que o blog usa conteúdo real quando existir
- confirmar que os logs foram atualizados

### Resultado esperado
Entregar somente:

```text
1. resumo curto
2. caminho da pasta do site
3. arquivos principais criados ou alterados
4. como rodar/testar localmente
5. pendências ou limitações
```
