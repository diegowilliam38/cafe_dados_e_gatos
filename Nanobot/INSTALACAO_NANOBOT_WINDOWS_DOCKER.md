# Nanobot no Windows com Docker Desktop

Guia direto para executar o **HKUDS/nanobot** no Windows usando **PowerShell 7**, **Docker Desktop**, **Ollama Cloud com `gemma4:cloud`** e **MiniMax**.

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

## Configurar pelo assistente guiado

Use o wizard para escolher provedor, endpoint, modelo e dados da WebUI sem editar o `config.json` manualmente:

```powershell
docker compose run --rm --user 1000:1000 nanobot-cli onboard --wizard
```

No menu, escolha **Quick Start** ou **Advanced Settings**, conforme aparecer na versão instalada.

Para este vídeo, configure uma destas opções:

- Ollama com o modelo cloud `gemma4:cloud`;
- MiniMax com a sua chave de API e o modelo disponível na conta.

Não mostre chaves, tokens ou senhas durante a gravação.

## Erro observado no Windows

O comando oficial sem `--user` pode falhar assim:

```powershell
docker compose run --rm nanobot-cli onboard
```

Mensagem observada:

```text
[entrypoint] warning: chown /home/nanobot/.nanobot failed
[entrypoint] error: started as root but setpriv privilege drop failed - refusing to run as root
```

Nesse caso, execute o wizard diretamente como o usuário interno não-root do Nanobot:

```powershell
docker compose run --rm --user 1000:1000 nanobot-cli onboard --wizard
```

## Testar o Gemma 4 Cloud no Ollama

```powershell
ollama signin
ollama run gemma4:cloud
```

Use `/bye` para sair.

## Verificar a configuração

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

Abra no navegador:

```text
http://localhost:8765
```

Depois de abrir a interface, ajustes de provedor e modelo podem ser feitos em **Settings → Models**, quando essa opção estiver disponível na versão instalada.

## Verificar os contêineres

```powershell
docker compose ps
```

## Acompanhar os logs

```powershell
docker compose logs -f nanobot-gateway
```

Use `Ctrl+C` para sair dos logs.

## Reiniciar após uma alteração

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
