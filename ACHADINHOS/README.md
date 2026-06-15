# AUTOMAÇÃO ACHADINHOS SHOPEE 

Esta versão entrega a automação.

## Automação

Suba para o repositório o conteúdo desta pasta:

```text
colocar_no_git/
```

Estrutura da automação:

```text
colocar_no_git/
├── .env.example
├── .github/
├── config/
├── lib/
├── scripts/
├── output/
└── requirements.txt
```

O que cada parte faz:

* `.env.example`: modelo para teste local
* `.github/`: workflows do GitHub Actions
* `config/`: configuração do catálogo
* `lib/`: código de apoio da automação
* `scripts/`: scripts que geram catálogo, banners e deploy
* `output/`: onde os JSONs gerados ficam salvos
* `requirements.txt`: dependências Python

## Setup

1. crie um repositório novo
2. copie o conteúdo de `colocar_no_git/` para a raiz do repo
3. ajuste `config/catalog_config.json` se quiser mudar limite, modo ou pasta remota
4. crie os secrets `SHOPEE_APP_ID` e `SHOPEE_SECRET`
5. rode os workflows em `Actions`

## Secrets

Obrigatórios:

* `SHOPEE_APP_ID`
* `SHOPEE_SECRET`

Opcional:

* `SHOPEE_API_URL`

URL padrão:

```text
https://open-api.affiliate.shopee.com.br/graphql
```

FTP opcional:

* `FTP_HOST`
* `FTP_USERNAME`
* `FTP_PASSWORD`
* `FTP_REMOTE_DIR`

## .env e GitHub

`.env.example` serve para rodar localmente.

No GitHub, o que vale mesmo são os secrets:

* `SHOPEE_APP_ID`
* `SHOPEE_SECRET`
* `SHOPEE_API_URL` se precisar trocar a URL padrão
* `FTP_HOST`, `FTP_USERNAME`, `FTP_PASSWORD`, `FTP_REMOTE_DIR` se quiser publicar por FTP

## Como isso funciona na prática

Esta automação faz duas coisas diferentes:

1. conversar com a Shopee para buscar os produtos
2. guardar o resultado dessa busca em arquivos JSON

Para a primeira parte funcionar, o GitHub precisa das credenciais da Shopee.
Por isso existem os secrets:

* `SHOPEE_APP_ID`
* `SHOPEE_SECRET`

Sem esses dois dados, o workflow não consegue falar com a API da Shopee.
Nesse caso, ele não consegue montar o catálogo.

Quando esses dados existem e estão corretos, a automação gera os arquivos em:

```text
output/catalog/
```

Essa pasta `output/` faz parte normal do projeto.
Ela existe porque os scripts precisam de um lugar para salvar os arquivos prontos.

O arquivo `.env.example` entra só para quem quiser testar tudo localmente no computador.
No GitHub, a configuração importante fica nos `Secrets`, não no `.env`.

Os dados de FTP são outra etapa.
Eles não servem para buscar produtos da Shopee.
Eles servem apenas para publicar os arquivos gerados em outro lugar, como um servidor.

Por isso:

* sem `SHOPEE_APP_ID` e `SHOPEE_SECRET`, o catálogo não é gerado
* com `SHOPEE_APP_ID` e `SHOPEE_SECRET`, o catálogo é gerado em `output/catalog/`
* com os dados de FTP, além de gerar, o workflow também consegue publicar esses arquivos automaticamente

Se a pessoa quiser apenas gerar os arquivos e depois baixar manualmente, os dados de FTP não são obrigatórios.
Se quiser publicar direto no site, cadastre `FTP_HOST`, `FTP_USERNAME` e `FTP_PASSWORD`.
O `FTP_REMOTE_DIR` sobrescreve a pasta remota; se ele ficar vazio, vale `deploy.remote_dir` em `config/catalog_config.json`.

## Saída

Os JSONs ficam em:

```text
output/catalog/
```

Arquivos principais:

* `categories.json`
* `categories/<slug>.json`
* `highlights/best-sellers.json`
* `highlights/top-discounts.json`
* `manifest.json`

## Execução local

```bash
cd colocar_no_git
cp .env.example .env
pip3 install -r requirements.txt
python3 scripts/build_catalog.py --verbose
python3 scripts/build_banners.py --verbose
```

## Configuração do catálogo

Edite `config/catalog_config.json` se quiser ajustar:

* modo do catálogo: `promocoes` ou `full`
* quantidade de produtos por categoria
* limite dos destaques
* desconto mínimo
* preço mínimo
* whitelist de categorias
* blacklist de categorias

Padrão recomendado:

```json
{
  "catalog": {
    "mode": "promocoes",
    "limit_per_category": 200,
    "min_discount_pct": 1
  }
}
```
# Se quiser plugar em um site

Se voce quiser usar a automacao como fonte de um site, basta consumir os arquivos JSON gerados dentro de:

output/catalog/

O objetivo deste kit e justamente separar a geracao dos dados da exibicao.

Ou seja, a automacao gera os produtos, organiza as categorias, cria os destaques e entrega tudo em JSON.

A partir dai, voce pode escolher a tecnologia que preferir para exibir.

Por exemplo:

categories.json pode ser usado para montar o menu principal de categorias.
categories/<slug>.json pode alimentar paginas individuais de categoria.
highlights/best-sellers.json pode preencher a area de produtos mais vendidos.
highlights/top-discounts.json pode preencher uma secao de promocoes.
manifest.json pode ser usado para verificar a data da ultima atualizacao do catalogo.

Uma abordagem comum e configurar o GitHub Actions para atualizar os arquivos automaticamente e publicar os JSONs em uma hospedagem.

Dessa forma, o site apenas le os dados gerados pela automacao, sem precisar consultar a API da Shopee diretamente.

Isso reduz processamento, simplifica a manutencao e permite que o catalogo seja atualizado automaticamente nos horarios definidos no workflow.

Fluxo completo da automacao
API Affiliate Shopee
        |
        v
build_catalog.py
        |
        v
output/catalog/
        |
        +--> categories.json
        +--> categories/<slug>.json
        +--> best-sellers.json
        +--> top-discounts.json
        +--> manifest.json
        |
        v
GitHub Actions
        |
        +--> Artefato GitHub
        |
        +--> FTP (opcional)
        |
        v
Site / Loja / Dashboard
O que este material entrega

Este pacote foi pensado para entregar a parte mais importante do processo: a automacao.

Ele coleta os produtos da Shopee, organiza os dados, gera os arquivos estruturados e permite atualizar tudo automaticamente usando GitHub Actions.

A partir dessa base, voce pode criar seu proprio site, integrar com um projeto existente ou utilizar os JSONs em qualquer outra aplicacao.

Todo o material foi organizado para ser simples de configurar, modificar e expandir conforme a necessidade de cada projeto.

Use `mode: "promocoes"` para trazer apenas produtos com desconto.
Use `mode: "full"` para aceitar produtos mesmo sem desconto.


