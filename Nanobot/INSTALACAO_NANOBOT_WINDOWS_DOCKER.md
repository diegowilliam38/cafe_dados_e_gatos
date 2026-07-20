# Nanobot com Docker Compose — comandos oficiais

Este documento reproduz o fluxo oficial do projeto **HKUDS/nanobot** para construção e execução com Docker Compose.

> Os comandos abaixo foram mantidos no formato publicado pela documentação oficial. Não foram convertidos para PowerShell nem adaptados para outro shell.

## Fontes oficiais

- Repositório: `https://github.com/HKUDS/nanobot`
- Guia de implantação: `https://github.com/HKUDS/nanobot/blob/main/docs/deployment.md`

## Antes de usar o Docker

A documentação oficial recomenda confirmar primeiro que a configuração, o provedor, o modelo e o workspace funcionam localmente:

```bash
nanobot status
nanobot agent -m "Hello!"
```

O comando `nanobot status` mostra a configuração e o workspace usados pela instância.

O comando `nanobot agent -m "Hello!"` confirma que instalação, configuração, provedor, modelo e escrita no workspace estão funcionando antes de adicionar a camada Docker.

## Construir a imagem oficial

O uso oficial com Docker atualmente significa construir a imagem diretamente a partir do repositório, usando o `Dockerfile` incluído.

```bash
docker build -t nanobot .
```

Constrói a imagem local com o nome `nanobot`.

## Construir com dependências adicionais

Para incluir um extra regular do Python, como suporte ao Bedrock:

```bash
docker build --build-arg NANOBOT_EXTRAS=bedrock -t nanobot .
```

Para incluir antecipadamente dependências de canais específicos:

```bash
docker build --build-arg NANOBOT_CHANNELS=telegram,slack -t nanobot .
```

A imagem padrão já inclui as dependências do WhatsApp.

## Inicializar a configuração com Docker

```bash
docker run -v ~/.nanobot:/home/nanobot/.nanobot --rm nanobot onboard
```

Cria a configuração inicial e mantém os dados do Nanobot no diretório persistente `~/.nanobot` do host.

O contêiner lê a configuração em:

```text
/home/nanobot/.nanobot
```

## Editar a configuração

```bash
vim ~/.nanobot/config.json
```

Abre o arquivo de configuração para adicionar provedores, modelos, chaves e canais.

API keys, tokens e demais segredos não devem ficar expostos nem ser publicados no GitHub.

## Configuração necessária para WebUI no Docker

Por padrão, o gateway e o canal WebSocket usam `127.0.0.1` dentro do contêiner. O encaminhamento de portas do Docker não consegue alcançar a interface de loopback interna do contêiner.

Para acessar a WebUI pelo host ou pela rede local, a documentação oficial orienta definir os dois hosts como `0.0.0.0` e proteger a emissão de token com um segredo:

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

Quando o host do WebSocket é `0.0.0.0`, o canal não inicia sem `token` ou `tokenIssueSecret`.

## Executar o gateway com Docker

```bash
docker run \
  --cap-drop ALL \
  -v ~/.nanobot:/home/nanobot/.nanobot \
  -p 18790:18790 -p 8765:8765 \
  nanobot gateway
```

Executa o gateway, publica o endpoint de saúde na porta `18790` e publica o WebSocket/WebUI na porta `8765`.

## Executar um comando único

```bash
docker run -v ~/.nanobot:/home/nanobot/.nanobot --rm nanobot agent -m "Hello!"
```

Envia uma mensagem única ao agente.

```bash
docker run -v ~/.nanobot:/home/nanobot/.nanobot --rm nanobot status
```

Mostra o estado da configuração e do workspace dentro do contêiner.

## Fluxo oficial com Docker Compose

### Inicializar a configuração

```bash
docker compose run --rm nanobot-cli onboard
```

Executa a configuração inicial usando o serviço `nanobot-cli`.

### Editar a configuração

```bash
vim ~/.nanobot/config.json
```

Abre o arquivo de configuração persistente no host.

### Iniciar o gateway

```bash
docker compose up -d nanobot-gateway
```

Inicia o gateway em segundo plano.

### Testar o agente pela CLI

```bash
docker compose run --rm nanobot-cli agent -m "Hello!"
```

Executa uma mensagem de teste por meio do serviço de CLI.

### Acompanhar os logs

```bash
docker compose logs -f nanobot-gateway
```

Exibe os logs do gateway continuamente.

Use `Ctrl+C` para sair da visualização dos logs.

### Parar os serviços

```bash
docker compose down
```

Para e remove os contêineres e a rede criados pelo Docker Compose.

## Construir canais específicos com Docker Compose

```bash
NANOBOT_CHANNELS=telegram,slack docker compose build
```

Constrói a imagem com as dependências dos canais Telegram e Slack já incluídas.

## Bubblewrap opcional

Somente quando a configuração contiver:

```json
{
  "tools": {
    "exec": {
      "sandbox": "bwrap"
    }
  }
}
```

Use também o arquivo de override oficial:

```bash
docker compose -f docker-compose.yml -f docker-compose.bwrap.yml up -d nanobot-gateway
```

Para executar uma mensagem com o mesmo override:

```bash
docker compose -f docker-compose.yml -f docker-compose.bwrap.yml run --rm nanobot-cli agent -m "Hello!"
```

Esse override concede `CAP_SYS_ADMIN` e desativa o confinamento AppArmor/seccomp para permitir que o Bubblewrap crie namespaces aninhados. Deve ser usado somente quando o sandbox `bwrap` estiver habilitado.

## Observações oficiais de segurança

- A imagem executa o Nanobot como usuário não-root `nanobot`, UID `1000`.
- A configuração deve ser montada em `/home/nanobot/.nanobot`, e não em `/root/.nanobot`.
- O arquivo padrão do Compose remove todas as capabilities Linux e mantém os perfis padrão AppArmor/seccomp do Docker.
- Imagens publicadas no Docker Hub por terceiros não são mantidas nem verificadas pelo projeto HKUDS/nanobot.
- Não monte chaves de API ou tokens em imagens de terceiros sem confiar no responsável pela publicação.
- O endpoint de saúde do gateway é mínimo e não possui autenticação.
- Reinicie o processo depois de alterar o arquivo `config.json`, pois os processos de longa duração leem a configuração durante a inicialização.

## Portas padrão

```text
8765  WebSocket e WebUI
18790 Endpoint de saúde do gateway
8900  nanobot serve
```
