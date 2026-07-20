# Nanobot — instalação oficial e implantação com Docker

Este documento separa os métodos de **instalação** publicados no README oficial do Nanobot da opção de **implantação e execução com Docker** publicada no guia de deployment.

> Docker não aparece na documentação principal como método de instalação. A instalação a partir do código-fonte é feita clonando o repositório com Git. O Docker é usado depois como runtime de implantação e execução.

## Fontes oficiais

- Repositório: `https://github.com/HKUDS/nanobot`
- README: `https://github.com/HKUDS/nanobot/blob/main/README.md`
- Guia de implantação: `https://github.com/HKUDS/nanobot/blob/main/docs/deployment.md`

## Instalação oficial em um comando

### macOS ou Linux

```bash
curl -fsSL https://raw.githubusercontent.com/HKUDS/nanobot/main/scripts/install.sh | sh
```

Instala ou atualiza o pacote `nanobot-ai` e inicia o assistente `nanobot onboard --wizard`.

### Windows PowerShell

```powershell
irm https://raw.githubusercontent.com/HKUDS/nanobot/main/scripts/install.ps1 | iex
```

Instala ou atualiza o pacote `nanobot-ai` e inicia o assistente `nanobot onboard --wizard`.

## Instalação com uv

```bash
uv tool install nanobot-ai
```

Instala o pacote oficial publicado no PyPI usando `uv`.

## Instalação pelo PyPI com pip

```bash
python -m pip install nanobot-ai
```

Instala o pacote oficial publicado no PyPI usando o Python do ambiente atual.

## Instalação a partir do código-fonte com Git

O método chamado **Install from source** no README oficial clona o código-fonte com Git.

`bun` ou `npm` precisa estar disponível. Execute dentro de um ambiente virtual ativado:

```bash
git clone https://github.com/HKUDS/nanobot.git
cd nanobot
python -m pip install .
```

O primeiro comando clona o repositório oficial.

O segundo entra na pasta clonada.

O terceiro instala o Nanobot a partir do código-fonte local.

### Ajuste oficial para Windows quando o pip não consegue iniciar o npm

```powershell
cd webui
npm.cmd install --package-lock=false
npm.cmd run build
cd ..
python -m pip install .
```

Constrói a WebUI manualmente e repete a instalação a partir do código-fonte.

## Verificar a instalação

```bash
nanobot --version
```

Mostra a versão instalada do Nanobot.

## Inicializar

```bash
nanobot onboard
```

Cria a configuração e o workspace.

Para usar o assistente interativo:

```bash
nanobot onboard --wizard
```

## Verificar configuração e modelo antes de implantar

```bash
nanobot status
nanobot agent -m "Hello!"
```

O primeiro comando mostra a configuração e o workspace usados pela instância.

O segundo confirma que instalação, configuração, provedor, modelo e escrita no workspace estão funcionando.

# Implantação oficial com Docker

A documentação de deployment apresenta Docker Compose como runtime para manter WebUI, canais, heartbeat, Dream, tarefas cron e conexões do agente em execução.

O uso oficial com Docker exige construir a imagem diretamente a partir do repositório clonado. Imagens de terceiros no Docker Hub não são mantidas nem verificadas pelo projeto.

## Construir a imagem

```bash
docker build -t nanobot .
```

Constrói localmente a imagem usando o `Dockerfile` incluído no repositório.

## Inicializar a configuração com Docker

```bash
docker run -v ~/.nanobot:/home/nanobot/.nanobot --rm nanobot onboard
```

Cria a configuração inicial e mantém os dados no diretório persistente `~/.nanobot` do host.

## Editar a configuração

```bash
vim ~/.nanobot/config.json
```

Abre o arquivo de configuração para adicionar provedores, modelos, chaves e canais.

## Configuração necessária para a WebUI no Docker

Por padrão, o gateway e o canal WebSocket usam `127.0.0.1` dentro do contêiner. Para acessar a WebUI pelo host, a documentação oficial orienta definir os hosts como `0.0.0.0` e proteger a emissão de token:

```json
{
  "gateway": {
    "host": "0.0.0.0"
  },
  "channels": {
    "websocket": {
      "host": "0.0.0.0",
      "port": 8765,
      "tokenIssueSecret": "your-secret-here"
    }
  }
}
```

Quando o WebSocket usa `0.0.0.0`, o canal não inicia sem `token` ou `tokenIssueSecret`.

## Executar o gateway com Docker

```bash
docker run \
  --cap-drop ALL \
  -v ~/.nanobot:/home/nanobot/.nanobot \
  -p 18790:18790 -p 8765:8765 \
  nanobot gateway
```

Publica o endpoint de saúde na porta `18790` e o WebSocket/WebUI na porta `8765`.

## Fluxo oficial com Docker Compose

```bash
docker compose run --rm nanobot-cli onboard
vim ~/.nanobot/config.json
docker compose up -d nanobot-gateway
```

Inicializa a configuração, abre o arquivo de configuração e inicia o gateway em segundo plano.

## Testar o agente pela CLI

```bash
docker compose run --rm nanobot-cli agent -m "Hello!"
```

Executa uma mensagem de teste usando o serviço de CLI.

## Acompanhar os logs

```bash
docker compose logs -f nanobot-gateway
```

Exibe os logs do gateway continuamente.

## Parar os serviços

```bash
docker compose down
```

Para e remove os contêineres e a rede criados pelo Docker Compose.

## Portas padrão

```text
8765  WebSocket e WebUI
18790 Endpoint de saúde do gateway
8900  nanobot serve
```

## Observações oficiais de segurança

- A imagem executa o Nanobot como usuário não-root `nanobot`, UID `1000`.
- A configuração deve ser montada em `/home/nanobot/.nanobot`, e não em `/root/.nanobot`.
- A imagem deve ser construída a partir do repositório oficial.
- Não monte chaves de API ou tokens em imagens de terceiros sem confiar no responsável pela publicação.
- O endpoint de saúde do gateway é mínimo e não possui autenticação.
- Reinicie o processo depois de alterar `config.json`, pois os processos de longa duração leem a configuração durante a inicialização.
