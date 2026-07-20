# Nanobot no Windows com Docker Desktop

Guia para executar o **HKUDS/nanobot** no Windows com **PowerShell 7**, **Docker Desktop**, **Ollama Cloud com `gemma4:cloud`** e **MiniMax**.

> Este guia não usa modelos locais. O Ollama funciona como cliente para um modelo hospedado na nuvem.

## Pré-requisitos

- Windows 10 ou Windows 11
- PowerShell 7
- Docker Desktop em execução
- Git
- Ollama instalado e conectado a uma conta
- Chave de API MiniMax, caso esse provedor seja testado

## Verificar o ambiente

```powershell
docker version
docker compose version
git --version
ollama --version
$PSVersionTable.PSVersion
```

## Baixar o repositório oficial

```powershell
Set-Location "$HOME\Documents"
git clone https://github.com/HKUDS/nanobot.git
Set-Location nanobot
```

## Confirmar a pasta correta

```powershell
Get-ChildItem Dockerfile
Get-ChildItem docker-compose.yml
```

Os dois arquivos precisam aparecer antes de continuar.

## Construir a imagem

```powershell
docker build -t nanobot .
```

## Criar a configuração inicial

Comando publicado no fluxo oficial com Docker Compose:

```powershell
docker compose run --rm nanobot-cli onboard
```

### Erro encontrado no Windows

No teste com Docker Desktop, o comando anterior construiu a imagem e criou o contêiner, mas terminou com:

```text
[entrypoint] warning: chown /home/nanobot/.nanobot failed
[entrypoint] error: started as root but setpriv privilege drop failed - refusing to run as root
```

O `docker-compose.yml` remove as capabilities Linux e o `entrypoint` tenta reduzir os privilégios do processo iniciado como root. No ambiente testado, essa redução falhou.

Execute diretamente como o usuário interno não-root do Nanobot, UID `1000`:

```powershell
docker compose run --rm --user 1000:1000 nanobot-cli onboard
```

Para usar o assistente guiado:

```powershell
docker compose run --rm --user 1000:1000 nanobot-cli onboard --wizard
```

A configuração e o workspace ficam em:

```text
C:\Users\SEU_USUARIO\.nanobot
```

## Abrir a configuração

```powershell
notepad "$HOME\.nanobot\config.json"
```

Não publique esse arquivo caso ele contenha credenciais.

# Opção 1 - Ollama Cloud com Gemma 4

## Entrar na conta Ollama

```powershell
ollama signin
```

## Testar o modelo cloud

```powershell
ollama run gemma4:cloud
```

Use `/bye` para sair.

## Confirmar a API do Ollama

```powershell
Invoke-RestMethod http://localhost:11434/v1/models
```

## Configurar o Nanobot para acessar o Ollama do Windows

Dentro do contêiner, `localhost` aponta para o próprio contêiner. Para acessar o Ollama instalado no Windows, use `host.docker.internal`.

Adicione ou mescle no `config.json`:

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

# Opção 2 - MiniMax

Adicione ou mescle no `config.json`:

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

Não mostre a chave durante a gravação e não envie o `config.json` ao GitHub.

## Alternar o modelo ativo

Para Gemma 4 Cloud:

```json
{
  "agents": {
    "defaults": {
      "modelPreset": "gemma4-cloud"
    }
  }
}
```

Para MiniMax:

```json
{
  "agents": {
    "defaults": {
      "modelPreset": "minimax"
    }
  }
}
```

# WebUI do Nanobot

## Configuração para Docker

Adicione ou ajuste no `config.json`:

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

## Verificar a configuração

Como o erro de privilégios também pode afetar comandos posteriores, mantenha o usuário interno:

```powershell
docker compose run --rm --user 1000:1000 nanobot-cli status
```

## Testar o agente pela CLI

```powershell
docker compose run --rm --user 1000:1000 nanobot-cli agent -m "Responda apenas: Nanobot funcionando."
```

## Iniciar o gateway e a WebUI

```powershell
docker compose up -d nanobot-gateway
```

Abra:

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

Use `Ctrl+C` para sair dos logs.

## Reiniciar após alterar a configuração

```powershell
docker compose restart nanobot-gateway
```

## Parar os serviços

```powershell
docker compose down
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

## Remover configuração, memória e workspace

```powershell
Remove-Item -Recurse -Force "$HOME\.nanobot"
```

Esse comando apaga permanentemente configuração, credenciais, memória, sessões e workspace.

## Fontes oficiais

- Nanobot: `https://github.com/HKUDS/nanobot`
- Deployment: `https://github.com/HKUDS/nanobot/blob/main/docs/deployment.md`
- Configuração: `https://github.com/HKUDS/nanobot/blob/main/docs/configuration.md`
- Ollama Cloud: `https://docs.ollama.com/cloud`
- Gemma 4: `https://ollama.com/library/gemma4`
- MiniMax API: `https://platform.minimax.io/docs/guides/text-generation`
