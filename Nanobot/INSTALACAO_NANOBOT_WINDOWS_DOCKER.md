# Nanobot no Windows com Docker Desktop

Guia testado para executar o **HKUDS/nanobot** no Windows com **PowerShell 7**, **Docker Desktop**, **Ollama Cloud com `gemma4:cloud`** e **MiniMax**.

> O Ollama é usado como cliente para um modelo hospedado na nuvem.

## Pré-requisitos

- Windows 10 ou 11
- PowerShell 7
- Docker Desktop em execução
- Git
- Ollama instalado e conectado a uma conta
- Chave de API MiniMax, caso esse provedor seja usado

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

Os dois arquivos precisam aparecer.

## Construir a imagem

```powershell
docker build -t nanobot .
```

## Primeiro comando oficial e erro encontrado

O fluxo oficial usa:

```powershell
docker compose run --rm nanobot-cli onboard
```

No Docker Desktop para Windows, o comando pode terminar com:

```text
[entrypoint] warning: chown /home/nanobot/.nanobot failed
[entrypoint] error: started as root but setpriv privilege drop failed - refusing to run as root
```

O contêiner inicia como `root`, mas não consegue reduzir os privilégios. Execute diretamente como o usuário interno do Nanobot:

```powershell
docker compose run --rm --user 1000:1000 nanobot-cli onboard --wizard
```

No wizard, escolha **Quick Start** ou **Advanced Settings**.

## Configurar o Ollama Cloud

No Windows:

```powershell
ollama signin
ollama run gemma4:cloud
```

Use `/bye` para sair.

No Nanobot, configure:

```text
Model: gemma4:cloud
Provider: ollama
API Base: http://host.docker.internal:11434/v1
```

Dentro do contêiner, `localhost` aponta para o próprio contêiner. `host.docker.internal` permite alcançar o Ollama instalado no Windows.

## Configurar o MiniMax

Crie um preset separado e informe o identificador exato do modelo disponível em sua conta, a chave de API e o provedor correspondente. Não mostre credenciais durante a gravação.

## Verificar a configuração

```powershell
docker compose run --rm --user 1000:1000 nanobot-cli status
```

## Testar o agente pela CLI

```powershell
docker compose run --rm --user 1000:1000 nanobot-cli agent -m "Responda apenas: Nanobot funcionando."
```

O teste precisa responder antes de iniciar a WebUI.

## Iniciar o gateway: segundo erro de privilégios

O comando abaixo pode criar o serviço, mas o gateway entra em reinicialização pelo mesmo erro de `setpriv`:

```powershell
docker compose up -d nanobot-gateway
```

Confira:

```powershell
docker compose logs --tail 80 nanobot-gateway
```

Se aparecer novamente `refusing to run as root`, pare o Compose e inicie o gateway como usuário `1000:1000`:

```powershell
docker compose down
docker compose run -d --name nanobot-gateway --service-ports --user 1000:1000 nanobot-gateway
```

Confirme que o contêiner está ativo:

```powershell
docker ps
```

## Corrigir a WebUI em branco no Docker

Mesmo com o gateway saudável, a WebUI pode ficar em branco porque o WebSocket está ouvindo em `127.0.0.1:8765` **dentro do contêiner**. O Docker publica a porta, mas não alcança o loopback interno.

Evidência típica:

```text
WebSocket server listening on ws://127.0.0.1:8765/
```

O endpoint de saúde pode funcionar normalmente em `http://127.0.0.1:18790/health`, retornando:

```json
{"status":"ok"}
```

Crie um backup, altere somente o host do WebSocket e salve o JSON como **UTF-8 sem BOM**:

```powershell
$configPath = "$env:USERPROFILE\.nanobot\config.json"
Copy-Item $configPath "$configPath.bak" -Force

$config = Get-Content -Raw -LiteralPath $configPath | ConvertFrom-Json
$config.channels.websocket.host = "0.0.0.0"

$json = $config | ConvertTo-Json -Depth 100
$utf8SemBom = New-Object System.Text.UTF8Encoding($false)
[System.IO.File]::WriteAllText($configPath, $json, $utf8SemBom)
```

> Não use `Set-Content -Encoding utf8` nesse trecho. Dependendo da versão do PowerShell, ele pode gravar um marcador UTF-8 BOM, e o Nanobot pode recusar o arquivo com o erro `Unexpected UTF-8 BOM`.

O `tokenIssueSecret` precisa estar configurado para o Nanobot aceitar `0.0.0.0` com proteção.

Reinicie o contêiner criado manualmente:

```powershell
docker rm -f nanobot-gateway
docker compose run -d --name nanobot-gateway --service-ports --user 1000:1000 nanobot-gateway
```

Confirme nos logs:

```powershell
docker logs --tail 40 nanobot-gateway
```

O resultado correto é:

```text
WebSocket server listening on ws://0.0.0.0:8765/
```

Teste a WebUI:

```powershell
curl.exe -I http://127.0.0.1:8765/
```

Depois abra:

```text
http://localhost:8765
```

## Restringir a WebUI ao próprio computador

Para não publicar a porta 8765 em toda a rede, posteriormente altere no `docker-compose.yml`:

```yaml
- "8765:8765"
```

para:

```yaml
- "127.0.0.1:8765:8765"
```

Prefira fazer essa mudança em um `docker-compose.override.yml` para preservar o arquivo oficial.

## Verificar o gateway

```powershell
curl.exe http://127.0.0.1:18790/health
```

## Parar o Nanobot

Como o gateway foi criado com `docker compose run`, remova-o com:

```powershell
docker rm -f nanobot-gateway
```

## Atualizar o projeto

```powershell
Set-Location "$HOME\Documents\nanobot"
git pull
docker compose build --no-cache
```

## Remover o projeto

```powershell
docker rm -f nanobot-gateway
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
- WebUI: `https://github.com/HKUDS/nanobot/blob/main/docs/webui.md`
- Configuração: `https://github.com/HKUDS/nanobot/blob/main/docs/configuration.md`
- Ollama Cloud: `https://docs.ollama.com/cloud`
- Gemma 4: `https://ollama.com/library/gemma4`
