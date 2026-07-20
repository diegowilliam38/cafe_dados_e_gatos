# Nanobot no Windows com Docker Desktop

Guia direto para executar o **HKUDS/nanobot** no Windows usando **PowerShell 7**, **Docker Desktop**, **MiniMax** e **Ollama Cloud com Gemma 4**.

> Este material não usa modelos locais. O Ollama será usado como cliente para o modelo cloud `gemma4:cloud`.

## Pré-requisitos

- Windows 10 ou Windows 11
- PowerShell 7
- Docker Desktop em execução
- Git
- Ollama instalado e conectado a uma conta Ollama
- Uma chave de API MiniMax, caso esse provedor também seja testado

## Verificar o ambiente

```powershell
docker version
docker compose version
git --version
ollama --version
$PSVersionTable.PSVersion
```

Confirma que Docker, Docker Compose, Git, Ollama e PowerShell 7 estão disponíveis.

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

Para usar o assistente interativo:

```powershell
docker compose run --rm nanobot-cli onboard --wizard
```

A configuração e o workspace ficam na pasta `.nanobot` do usuário.

## Abrir a configuração

```powershell
notepad "$HOME\.nanobot\config.json"
```

Não publique esse arquivo caso ele contenha credenciais.

# Opção 1 — Ollama Cloud com Gemma 4

## Entrar na conta Ollama

```powershell
ollama signin
```

Os modelos cloud do Ollama exigem uma conta conectada.

## Testar o Gemma 4 Cloud no Windows

```powershell
ollama run gemma4:cloud
```

O modelo é executado na infraestrutura cloud do Ollama. O computador local atua como cliente e não precisa carregar os pesos do modelo na GPU.

Use `Ctrl+D` ou `/bye` para sair da conversa.

## Confirmar a API do Ollama

```powershell
Invoke-RestMethod http://localhost:11434/v1/models
```

Confirma que o serviço do Ollama está acessível no Windows.

## Configurar o Nanobot para alcançar o Ollama do Windows

Como o Nanobot está dentro de um contêiner, `localhost` apontaria para o próprio contêiner. Use `host.docker.internal` para alcançar o Ollama que está rodando no Windows.

Adicione ou mescle estes blocos no `config.json`:

```json
{
  "providers": {
    "ollama": {
      "apiBase": "http://host.docker.internal:11434/v1"
    }
  },
  "modelPresets": {
    "gemma4-cloud": {
      "label": "Gemma 4 Cloud",
      "provider": "ollama",
      "model": "gemma4:cloud",
      "maxTokens": 4096,
      "contextWindowTokens": 256000,
      "temperature": 0.2
    }
  },
  "agents": {
    "defaults": {
      "modelPreset": "gemma4-cloud"
    }
  }
}
```

# Opção 2 — MiniMax

O Nanobot possui provedores próprios para MiniMax. Para modelos com raciocínio, a documentação do projeto mantém uma integração separada pelo endpoint compatível com Anthropic.

Adicione ou mescle estes blocos no `config.json`:

```json
{
  "providers": {
    "minimaxAnthropic": {
      "apiKey": "COLOQUE_SUA_CHAVE_MINIMAX_AQUI"
    }
  },
  "modelPresets": {
    "minimax": {
      "label": "MiniMax M2.7",
      "provider": "minimax_anthropic",
      "model": "MiniMax-M2.7",
      "maxTokens": 4096,
      "contextWindowTokens": 204800,
      "temperature": 1.0
    }
  },
  "agents": {
    "defaults": {
      "modelPreset": "minimax"
    }
  }
}
```

Não mostre a chave durante a gravação e não envie o `config.json` para o GitHub.

## Alternar entre Gemma 4 Cloud e MiniMax

Mantenha os dois presets no mesmo `config.json` e altere apenas:

```json
{
  "agents": {
    "defaults": {
      "modelPreset": "gemma4-cloud"
    }
  }
}
```

ou:

```json
{
  "agents": {
    "defaults": {
      "modelPreset": "minimax"
    }
  }
}
```

Reinicie o gateway depois de mudar o preset.

# WebUI do Nanobot

## Configuração necessária no Docker

Adicione ou ajuste estes blocos no `config.json`:

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

## Acompanhar os logs

```powershell
docker compose logs -f nanobot-gateway
```

Use `Ctrl+C` para sair dos logs sem parar o contêiner.

## Reiniciar após alterar a configuração

```powershell
docker compose restart nanobot-gateway
```

## Parar os serviços

```powershell
docker compose down
```

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

## Remover o projeto

```powershell
docker compose down
Set-Location "$HOME\Documents"
Remove-Item -Recurse -Force ".\nanobot"
```

## Remover também configuração, memória e workspace

```powershell
Remove-Item -Recurse -Force "$HOME\.nanobot"
```

Este comando apaga permanentemente configuração, credenciais, memória, sessões e workspace.

## Fontes oficiais

- Nanobot: `https://github.com/HKUDS/nanobot`
- Deployment do Nanobot: `https://github.com/HKUDS/nanobot/blob/main/docs/deployment.md`
- Configuração do Nanobot: `https://github.com/HKUDS/nanobot/blob/main/docs/configuration.md`
- Ollama Cloud: `https://docs.ollama.com/cloud`
- Gemma 4 no Ollama: `https://ollama.com/library/gemma4`
- MiniMax API: `https://platform.minimax.io/docs/guides/text-generation`
