# Teste Minimax M3

Este diretório reúne um laboratório prático de uso do `MiniMax M3` para fluxos de curadoria Shopee, geração de prompts visuais e montagem de site/blog comercial.

O foco aqui não é apenas testar um modelo. A proposta é documentar um processo reutilizável para:

- selecionar produtos com `potencial comercial estimado`
- organizar dados finais para publicação
- preparar prompt de imagem Hero
- preparar prompt de vídeo para ComfyUI
- montar um site/blog a partir dos arquivos gerados
- comparar o mesmo fluxo em ambientes diferentes

## O que esta pasta cobre

O conteúdo atual está organizado para quatro trilhas de trabalho:

- `Hermes`
- `OpenClaw`
- `Claude Code`
- `VS Code + Cline`

Na prática, `Hermes` e `OpenClaw` concentram a etapa de curadoria e preparação dos materiais.

Depois disso, a construção do site pode seguir por dois caminhos:

- via `Claude Code`, com checklists específicos para `site_hermes/` e `site_openclaw/`
- via `VS Code + Cline`, pensado como alternativa para quem não usa Claude Code

## Objetivo do teste

Este conjunto de prompts foi pensado para validar como o `MiniMax M3` se comporta em uma cadeia de trabalho mais completa, incluindo:

- leitura e filtragem de CSV da Shopee
- classificação de produtos por critérios auditáveis
- separação por categorias finais do site
- geração de arquivos prontos para uso
- criação de assets textuais para imagem e vídeo
- orientação de build para blog/site responsivo

## Estrutura da pasta

```text
Teste Minimax M3/
├── README.md
└── Prompts/
    ├── Claude/
    │   ├── Hermes/
    │   │   └── CLAUDE.md
    │   └── OpenClaw/
    │       └── CLAUDE.md
    ├── hermes/
    │   ├── prompt_hermes_shopee.md
    │   └── prompt_video_comfyui_hermes_shopee.md
    ├── hero/
    │   ├── promtp_hero_Hermes.md
    │   └── promtp_hero_openclaw.md
    ├── openclaw/
    │   ├── prompt_openclaw_shopee.md
    │   └── prompt_video_comfyui_openclaw_shopee.md
    └── VS_Code_Cline/
        ├── criacao_blog_hermes.md
        └── criacao_blog_openclaw.md
```

## Como o fluxo está dividido

### `Prompts/hermes/`

Aqui ficam os prompts do fluxo Hermes para curadoria e vídeo.

Principais pontos:

- uso do agente `Frank`
- análise do CSV com `Python/Pandas`
- seleção de produtos por faixa de preço, nota e disponibilidade de link
- geração de arquivos finais para site
- preparação de prompt para vídeo curto no ComfyUI

### `Prompts/openclaw/`

Traz o fluxo equivalente para `OpenClaw`, com a mesma linha metodológica da curadoria.

Principais pontos:

- execução direta no ambiente OpenClaw
- análise e filtragem de CSV da Shopee
- produção de arquivos finais para publicação
- preparação de prompt para vídeo curto

### `Prompts/hero/`

Contém os prompts para criação da imagem Hero do blog.

Nessa etapa, a ideia é usar os produtos finais como referência visual para gerar uma Hero:

- horizontal
- comercial
- limpa
- moderna
- alinhada à estética de um blog de achadinhos

### `Prompts/Claude/`

Aqui estão os checklists para quem vai montar o site usando `Claude Code`.

Esses arquivos orientam:

- pasta base de cada projeto
- pasta correta de saída
- arquivos de entrada prioritários
- validações finais
- regras para publicação somente com `link_gerado_shopee`

Hoje essa é a trilha mais direta para quem já trabalha com Claude Code.

### `Prompts/VS_Code_Cline/`

Essa trilha foi mantida como alternativa para quem prefere usar `Cline` no `VS Code`.

Os prompts dessa pasta orientam a criação de um blog com:

- Home
- Produtos
- Blog
- página oculta de anúncios copiáveis

Eles aproveitam os dados já gerados nas etapas anteriores e descrevem o visual, a linguagem comercial e os cuidados com links e SEO.

## Regra metodológica central

Um dos pontos mais importantes deste teste é a padronização editorial.

Os prompts insistem em uma regra:

- não tratar os produtos como `mais vendidos`
- não prometer venda real
- não sugerir comissão garantida
- usar a expressão `potencial comercial estimado`

Isso faz com que o experimento não seja apenas técnico. Ele também testa uma forma mais segura e auditável de curadoria comercial.

## Regras recorrentes nos prompts

Ao longo dos arquivos, aparecem algumas decisões consistentes:

- usar `product_link` como link principal
- não usar `product_short link` como link oficial do site
- não inventar categorias manualmente
- definir categoria final somente por `global_category1` e `global_category2`
- usar `description` apenas como apoio para `porte_estimado`
- limitar os arquivos finais a até `4 produtos por categoria`
- registrar logs e validações de execução

## Ordem sugerida de leitura

Se a ideia for entender o processo de ponta a ponta, esta é uma boa sequência:

1. `Prompts/hermes/prompt_hermes_shopee.md` ou `Prompts/openclaw/prompt_openclaw_shopee.md`
2. `Prompts/hero/promtp_hero_Hermes.md` ou `Prompts/hero/promtp_hero_openclaw.md`
3. `Prompts/hermes/prompt_video_comfyui_hermes_shopee.md` ou `Prompts/openclaw/prompt_video_comfyui_openclaw_shopee.md`
4. `Prompts/Claude/Hermes/CLAUDE.md` ou `Prompts/Claude/OpenClaw/CLAUDE.md`
5. `Prompts/VS_Code_Cline/criacao_blog_hermes.md` ou `Prompts/VS_Code_Cline/criacao_blog_openclaw.md`

## O que este repositório entrega hoje

Neste estágio, esta pasta funciona principalmente como:

- acervo de prompts
- documentação de fluxo
- base de comparação entre ambientes
- guia para transformar curadoria em site/blog publicável

Ela não depende de um único orquestrador e pode servir tanto para testes comparativos quanto para reaproveitamento prático do pipeline.

## Desconto MiniMax

🚀 **GANHE 12% DE DESCONTO no Plano MiniMax Token Plan:**  
[https://platform.minimax.io/subscribe/coding-plan?code=LSRdjVVKt6&source=link](https://platform.minimax.io/subscribe/coding-plan?code=LSRdjVVKt6&source=link)

Aproveite o preço promocional do MiniMax M2.7 com o cupom do canal Café com Dados e Gatos.

## Links oficiais da plataforma

- MiniMax Cloud Platform: [https://minimax.io](https://minimax.io)
- Documentação Oficial da API: [https://minimax.io/docs/guides/text-generation](https://minimax.io/docs/guides/text-generation)
