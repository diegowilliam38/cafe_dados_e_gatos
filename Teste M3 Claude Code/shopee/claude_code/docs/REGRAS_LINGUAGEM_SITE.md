# Regras de linguagem do site público

Este site é uma **vitrine editorial de achadinhos da Shopee**. Ele não
é um relatório técnico nem um painel de rankings. Toda comunicação
visual deve soar como uma seleção feita com carinho para apresentar
ideias — nunca como uma promessa de resultado.

---

## ❌ Nunca usar no site

- "potencial comercial estimado"
- "score"
- "score_potencial_comercial"
- "ranking"
- "curadoria técnica"
- "modelo usado"
- "ambiente"
- "ferramenta de orquestração"
- "mais vendido"
- "campeão de vendas"
- "produto que mais vende"
- "venda comprovada"
- "sucesso garantido"
- "garantia de venda"
- "garantia de comissão"
- A palavra **"curadoria"** (o site vende achadinhos para o público,
  não é uma página de curadoria interna)
- Termos técnicos como `itemid`, `porte_estimado` (visíveis ao usuário),
  `score_potencial_comercial`, `metodo_curadoria_version`, etc.

## ✅ Linguagem preferida

Títulos e chamadas delicadas:

- Achadinhos Shopee
- Dica de Presente
- Selecionados da Semana
- Garimpos para Conferir
- Ideias úteis para o dia a dia
- Achadinhos por categoria
- Delicadeza que encanta

Subtítulos por categoria (exemplos):

- Moda — *Toques de estilo para todos os momentos*
- Beleza — *Pequenos gestos que cuidam de você*
- Acessórios para Celular — *Detalhes que protegem com charme*
- Casa — *Conforto e beleza para o seu lar*
- Cozinha — *Aconchego em cada receita*
- Organização — *Harmonia para o seu dia a dia*
- Pets — *Carinho para quem te ama de verdade*
- Papelaria — *Inspiração em cada anotação*
- Infantil — *Delícias para os pequenos*
- Fitness — *Bem-estar com leveza*

Textos públicos sugeridos:

- "Uma seleção delicada de achadinhos para você conhecer, organizada por categorias."
- "Ideias de produtos úteis, criativos e encantadores para o seu dia a dia."
- "Antes de comprar, confira preço, prazo, avaliações e condições diretamente na Shopee."

Aviso público obrigatório (presente no rodapé):

> "Os preços, disponibilidade e condições podem mudar. Confira sempre as
> informações atualizadas diretamente na Shopee antes de comprar."

## ✅ Call-to-action dos botões

- "Ver achadinho"
- "Conferir na Shopee"
- "Ver dica"
- "Abrir produto"

Sempre apontando para `product_link` original (nunca `product_short link`,
nunca link encurtado, nunca link inventado).

## ✅ Identidade visual

- Paleta: rosé gold, blush, nude, creme, branco quente.
- Tipografia: serifada (Playfair Display) para títulos; sans-serif leve
  (Quicksand) para corpo.
- Sombras suaves, cantos arredondados, transições delicadas.
- Atraente para o público feminino, sem ser infantil nem apelativo.

## ✅ Visível × não visível

| Campo técnico no JSON           | Site exibe? |
|---------------------------------|-------------|
| `categoria_final`               | sim (badge) |
| `title_clean`                   | sim         |
| `price`                         | sim, se > `sale_price` |
| `sale_price`                    | sim (preço principal) |
| `discount_percentage`           | sim, se existir |
| `item_rating`                   | sim (estrelas) |
| `image_link`                    | sim         |
| `product_link`                  | sim (botão) |
| `porte_estimado`                | sim, quando pequeno/grande (texto curto) |
| `itemid`                        | não         |
| `score_potencial_comercial`     | não         |
