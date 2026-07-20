# Nanobot no Windows com Docker Desktop

Guia direto para executar o **HKUDS/nanobot** no Windows usando **PowerShell 7** e **Docker Desktop**.

## Pré-requisitos

- Windows 10 ou Windows 11
- PowerShell 7
- Docker Desktop em execução
- Git
- Uma chave de API de provedor compatível

## Verificar o ambiente

```powershell
docker version
docker compose version
git --version
$PSVersionTable.PSVersion
```

Confirma que Docker, Docker Compose, Git e PowerShell 7 estão disponíveis.

## Baixar o repositório oficial

```powershell
Set-Location "$HOME\Documents"
git clone https://github.com/HKUDS/nanobot.git
Set-Location nanobot
```

Baixa o código-fonte oficial e entra na pasta onde estão o `Dockerfile` e o `docker-compose.yml`.

## Confirmar que está na pasta correta

```powershell
Get-ChildItem Dockerfile
Get-ChildItem docker-compose.yml
```

Os dois arquivos precisam aparecer antes de continuar.

## Construir a imagem

```powershell
docker build -t nanobot .
```

Constrói localmente a imagem Docker usando o `Dockerfile` oficial do projeto.

## Criar a configuração inicial

```powershell
docker compose run --rm nanobot-cli onboard
```

Cria a configuração e o workspace persistente na pasta `.nanobot` do usuário.

Para usar o assistente interativo:

```powershell
docker compose run --rm nanobot-cli onboard --wizard
```

## Abrir a configuração

```powershell
notepad "$HOME\.nanobot\config.json"
```

Abre o arquivo para configurar provedor, modelo, chave de API e WebUI.

Não publique esse arquivo caso ele contenha credenciais.

## Configuração necessária para a WebUI no Docker

Adicione ou ajuste os blocos abaixo no `config.json`:

```json
{
  "gateway": {
    "host": "0.0.0.0"
  },
  "channels": {
    "websocket": {
      "host": "0.0.0.0",
      "port": 8765,
      "tokenIssueSecret": "troque-por-um-segredo-forte"
    }
  }
}
```

O `tokenIssueSecret` deve ser substituído por um valor forte e exclusivo.

## Verificar a configuração

```powershell
docker compose run --rm nanobot-cli status
```

Mostra o estado da configuração, do workspace, dos provedores e dos canais.

## Testar o agente pela CLI

```powershell
docker compose run --rm nanobot-cli agent -m "Responda apenas: Nanobot funcionando."
```

Confirma que o provedor, o modelo e a configuração estão funcionando.

## Iniciar o gateway e a WebUI

```powershell
docker compose up -d nanobot-gateway
```

Abra no navegador:

```text
http://localhost:8765
```

## Verificar os contêineres

```powershell
docker compose ps
```

Mostra os serviços e o estado dos contêineres.

## Acompanhar os logs

```powershell
docker compose logs -f nanobot-gateway
```

Use `Ctrl+C` para sair dos logs sem parar o contêiner.

## Iniciar a API compatível com OpenAI

```powershell
docker compose up -d nanobot-api
```

A API fica disponível em:

```text
http://localhost:8900
```

## Reiniciar após alterar a configuração

```powershell
docker compose restart nanobot-gateway
```

Reinicia o gateway para aplicar alterações feitas no `config.json`.

## Parar os serviços

```powershell
docker compose down
```

Para e remove os contêineres e a rede do projeto.

A configuração e o workspace permanecem em:

```text
C:\Users\SEU_USUARIO\.nanobot
```

## Atualizar o Nanobot

```powershell
Set-Location "$HOME\Documents\nanobot"
git pull
docker compose build --no-cache
docker compose up -d nanobot-gateway
```

Baixa as alterações do repositório, reconstrói a imagem e inicia novamente o gateway.

## Remover o projeto

```powershell
docker compose down
Set-Location "$HOME\Documents"
Remove-Item -Recurse -Force ".\nanobot"
```

Remove os contêineres e os arquivos clonados do projeto.

## Remover também configuração, memória e workspace

```powershell
Remove-Item -Recurse -Force "$HOME\.nanobot"
```

Apaga permanentemente configuração, credenciais, memória, sessões e workspace do Nanobot.

## Fonte oficial

- Repositório: `https://github.com/HKUDS/nanobot`
- Guia de deployment: `https://github.com/HKUDS/nanobot/blob/main/docs/deployment.md`
