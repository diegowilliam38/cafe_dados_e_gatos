# Teste M3 Claude Code

Projeto de curadoria de produtos da Shopee com **Python/Pandas + site estático alimentado por JSON**, construído a partir de um prompt operacional e entregue como pacote reutilizável.

Este diretório reúne duas partes do trabalho:

- `Prompts/Prompt1.md`: o briefing completo usado para orientar a construção.
- `shopee.zip`: a entrega compactada com scripts, dados finais, documentação, logs e o site estático.

## Visão Geral

O objetivo deste projeto foi transformar um CSV bruto da Shopee em uma vitrine editorial de achadinhos, com separação clara entre:

- **camada interna**: análise, curadoria, score, logs e arquivos auditáveis;
- **camada pública**: site estático com linguagem leve, sem expor termos técnicos.

O fluxo foi desenhado para futuras atualizações com o menor atrito possível: trocar o CSV bruto, executar o script principal e regenerar dados + site.

## O Que Foi Entregue

Dentro de `shopee.zip`, o projeto inclui:

- script principal de curadoria em Python;
- arquivos CSV e JSON finais;
- arquivo manual para aplicação de links da Shopee;
- logs de execução;
- documentação de regras;
- site estático que lê os produtos via JSON.

Estrutura principal do pacote:

```text
shopee/
├── raw/
└── claude_code/
    ├── data/
    │   ├── processed/
    │   └── final/
    ├── docs/
    ├── logs/
    ├── scripts/
    └── site/
        ├── css/
        ├── data/
        ├── js/
        └── index.html
```

## Fluxo de Curadoria

O pipeline implementado no projeto segue esta lógica:

1. localizar um único CSV bruto em `raw/`;
2. contar linhas totais e produtos únicos por `itemid`;
3. filtrar itens sem `product_link`;
4. manter produtos na faixa de preço desejada;
5. aplicar critério mínimo de avaliação;
6. classificar categorias usando apenas `global_category1` e `global_category2`;
7. estimar `porte_estimado` apenas com sinais da descrição;
8. calcular um score interno de potencial comercial;
9. limitar a seleção final a 4 produtos por categoria;
10. gerar arquivos finais e copiar os públicos para o site.

Um ponto importante deste projeto é a disciplina editorial: o site não exibe score, ranking técnico, metadados do modelo nem promessas comerciais indevidas.

## Resultado da Execução

Com base no log principal incluído no pacote:

- CSV usado: `1005_200149_Shopee Brasil - 2022_20260604T051655_1.csv`
- Total de linhas: `10000`
- Produtos únicos por `itemid`: `10000`
- Removidos por preço: `4103`
- Removidos por nota: `47`
- Removidos por categoria não identificada: `822`
- Produtos finais após limite editorial: `40`

Distribuição final por categoria:

| Categoria | Quantidade |
| --- | ---: |
| acessórios para celular | 4 |
| beleza | 4 |
| casa | 4 |
| cozinha | 4 |
| fitness | 4 |
| infantil | 4 |
| moda | 4 |
| organização | 4 |
| papelaria | 4 |
| pets | 4 |

## Site Gerado

O site foi construído para ler os dados dinamicamente a partir de JSON, sem cards fixos no HTML.

Na prática, isso significa:

- atualização mais simples;
- separação entre conteúdo e apresentação;
- manutenção mais segura;
- reaproveitamento do fluxo em novas cargas de CSV.

Arquivos centrais do site dentro do pacote:

- `shopee/claude_code/site/index.html`
- `shopee/claude_code/site/css/style.css`
- `shopee/claude_code/site/js/app.js`
- `shopee/claude_code/site/data/achadinhos.json`

## Como Explorar Este Projeto

Se você abriu esta pasta pelo GitHub, o caminho mais útil é:

1. ler `Prompts/Prompt1.md` para entender o escopo e as regras;
2. baixar `shopee.zip`;
3. extrair o conteúdo localmente;
4. abrir a pasta `shopee/claude_code/`;
5. consultar o `README.md` interno e os arquivos em `docs/`, `logs/`, `scripts/` e `site/`.

## Atualização Futura

Depois de extrair o pacote, a atualização esperada é simples:

```bash
cd ~/Documents/shopee/claude_code
python3 scripts/gerar_curadoria_shopee.py
```

Para visualizar o site localmente:

```bash
cd ~/Documents/shopee/claude_code/site
python3 -m http.server 8000
```

## Destaques Técnicos

- Curadoria reproduzível com Python/Pandas
- Site estático orientado a dados
- Logs auditáveis de execução
- Regras explícitas de linguagem pública
- Separação entre dados internos e vitrine pública
- Processo reaproveitável para novas cargas

## Limitações

- O pacote publicado nesta pasta está compactado em `shopee.zip`, então a navegação pelo GitHub não mostra os arquivos internos diretamente.
- A seleção final é editorialmente limitada a 4 produtos por categoria.
- Produtos sem categoria confiável pelas colunas globais ficam de fora da vitrine final.
- O arquivo de links da Shopee depende de preenchimento manual em uma etapa posterior.

## Contexto do Teste

Este projeto faz parte de um experimento comparativo de execução assistida por IA, com foco em:

- interpretação de prompt detalhado;
- automação de curadoria com regras;
- geração de documentação;
- produção de uma entrega reaproveitável, não só de um protótipo visual.
