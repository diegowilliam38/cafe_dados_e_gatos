# Nanobot no Windows com Docker Desktop

Guia copy-paste para instalar e executar o **HKUDS/nanobot** no Windows usando Docker Desktop e PowerShell.

> O método oficial com Docker constrói a imagem localmente a partir do repositório. Não use imagens Docker de terceiros com suas chaves de API.

## Pré-requisitos

- Windows 10 ou Windows 11
- Docker Desktop em execução
- Git
- WSL 2 habilitado para o Docker Desktop
- Uma chave de API de um provedor de modelo compatível

## Verificar o ambiente

```powershell
docker version
```

Mostra as versões do cliente e do servidor Docker. O Docker Desktop precisa estar aberto.

```powershell
docker compose version
```

Confirma que o Docker Compose está disponível.

```powershell
docker info
```

Verifica se o mecanismo do Docker está funcionando.

```powershell
git --version
```

Confirma que o Git está instalado.

```powershell
wsl --status
```

Mostra o estado e a versão padrão do WSL.

```powershell
docker run --rm hello-world
```

Baixa e executa um contêiner de teste. O contêiner é removido automaticamente ao terminar.

## Verificar as portas

```powershell
Get-NetTCPConnection -LocalPort 8765,8900,18790 -ErrorAction SilentlyContinue
```

Verifica se as portas usadas pelo Nanobot já estão ocupadas:

- `8765`: WebUI
- `8900`: API compatível com OpenAI
- `18790`: endpoint de saúde do gateway

Nenhuma saída significa que não foi encontrada uma conexão usando essas portas.

## Criar a pasta do projeto

```powershell
New-Item -ItemType Directory -Force -Path "$HOME\Documents\laboratorios"
Set-Location "$HOME\Documents\laboratorios"
```

Cria uma pasta para os laboratórios e entra nela.

## Baixar o repositório oficial

```powershell
git clone https://github.com/HKUDS/nanobot.git
Set-Location nanobot
```

Clona o repositório oficial e entra na pasta do projeto.

## Confirmar a origem do código

```powershell
git remote -v
git branch --show-current
git log -1 --oneline
```

Mostra o repositório remoto, a branch atual e o commit mais recente baixado.

## Construir a imagem

```powershell
docker compose build
```

Constrói localmente a imagem Docker usando o `Dockerfile` incluído no repositório.

## Criar a configuração inicial

```powershell
docker compose run --rm nanobot-cli onboard
```

Cria a configuração e o workspace persistente na pasta:

```text
C:\Users\SEU_USUARIO\.nanobot
```

O contêiner temporário é removido após a execução.

Para usar o assistente interativo:

```powershell
docker compose run --rm nanobot-cli onboard --wizard
```

## Abrir o arquivo de configuração

```powershell
notepad "$HOME\.nanobot\config.json"
```

Abre o arquivo de configuração no Bloco de Notas para adicionar o provedor, a chave de API e o modelo.

Não publique o conteúdo desse arquivo caso ele contenha credenciais.

## Verificar a configuração

```powershell
docker compose run --rm nanobot-cli status
```

Mostra o estado da configuração, do workspace, dos provedores e dos canais.

É normal que provedores não configurados apareçam como `not set`.

## Fazer um teste pelo terminal

```powershell
docker compose run --rm nanobot-cli agent -m "Responda apenas: Nanobot funcionando."
```

Envia uma mensagem única ao agente para confirmar que configuração, provedor e modelo estão funcionando.

## Abrir o chat interativo

```powershell
docker compose run --rm nanobot-cli agent
```

Inicia uma conversa interativa no terminal.

Use `Ctrl+C` para encerrar.

## Iniciar o gateway e a WebUI

```powershell
docker compose up -d nanobot-gateway
```

Inicia o gateway em segundo plano.

Abra no navegador:

```text
http://127.0.0.1:8765
```

A porta `8765` corresponde à WebUI.

## Verificar os contêineres

```powershell
docker compose ps
```

Mostra os serviços do projeto e o estado de cada contêiner.

## Acompanhar os logs

```powershell
docker compose logs -f nanobot-gateway
```

Mostra os logs do gateway em tempo real.

Use `Ctrl+C` para sair dos logs sem parar o contêiner.

Para exibir somente as últimas 100 linhas:

```powershell
docker compose logs --tail 100 nanobot-gateway
```

## Iniciar a API compatível com OpenAI

```powershell
docker compose up -d nanobot-api
```

Inicia a API local em:

```text
http://127.0.0.1:8900
```

## Verificar o endpoint de saúde

```powershell
Invoke-WebRequest http://127.0.0.1:18790
```

Consulta o endpoint de saúde do gateway.

## Reiniciar após alterar a configuração

```powershell
docker compose restart nanobot-gateway
```

Reinicia o gateway para que ele releia o arquivo `config.json`.

Para reiniciar a API:

```powershell
docker compose restart nanobot-api
```

## Parar os serviços

```powershell
docker compose stop
```

Para os contêineres sem removê-los.

## Iniciar novamente

```powershell
docker compose start
```

Inicia os contêineres que foram parados.

## Parar e remover os contêineres

```powershell
docker compose down
```

Para e remove os contêineres e a rede criada pelo Compose.

A configuração e o workspace permanecem em:

```text
C:\Users\SEU_USUARIO\.nanobot
```

## Atualizar o Nanobot

```powershell
Set-Location "$HOME\Documents\laboratorios\nanobot"
git pull
docker compose build --no-cache
docker compose up -d nanobot-gateway
```

Baixa as alterações do repositório, reconstrói a imagem sem reutilizar o cache e inicia novamente o gateway.

## Remover a imagem construída

```powershell
docker compose down
docker image ls
```

Para os serviços e mostra as imagens disponíveis.

Depois de identificar o nome da imagem do projeto:

```powershell
docker image rm NOME_DA_IMAGEM
```

Remove a imagem selecionada.

## Remover o projeto

```powershell
Set-Location "$HOME\Documents\laboratorios"
Remove-Item -Recurse -Force ".\nanobot"
```

Apaga os arquivos clonados do repositório.

## Remover também configurações, memória e workspace

```powershell
Remove-Item -Recurse -Force "$HOME\.nanobot"
```

Apaga permanentemente configuração, credenciais, sessões, memória, workspace, automações e demais dados persistentes do Nanobot.

Execute somente quando não precisar mais desses dados.

## Fontes oficiais

- Repositório: `https://github.com/HKUDS/nanobot`
- Documentação no repositório: `https://github.com/HKUDS/nanobot/tree/main/docs`
- Guia de implantação: `https://github.com/HKUDS/nanobot/blob/main/docs/deployment.md`
