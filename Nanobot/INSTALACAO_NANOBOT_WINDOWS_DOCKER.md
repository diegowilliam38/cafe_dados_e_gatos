# Nanobot no Windows com Docker Desktop

Guia testado para executar o **HKUDS/nanobot** no Windows com **PowerShell 7**, **Docker Desktop** e **Ollama Cloud usando `gemma4:cloud`**.

> Para começar, configure apenas o Ollama com o Gemma 4 Cloud. Outros provedores e modelos podem ser adicionados depois pela própria WebUI.

## Pré-requisitos

- Windows 10 ou 11
- PowerShell 7
- Docker Desktop em execução
- Git
- Ollama instalado e conectado a uma conta

## Verificar o ambiente

Execute um comando por vez:

```powershell
docker version
```

```powershell
docker compose version
```

```powershell
git --version
```

```powershell
ollama --version
```

```powershell
$PSVersionTable.PSVersion
```

## Baixar o repositório oficial

```powershell
Set-Location "$HOME\Documents"
```

```powershell
git clone https://github.com/HKUDS/nanobot.git
```

```powershell
Set-Location nanobot
```

## Confirmar a pasta correta

```powershell
Get-ChildItem Dockerfile
```

```powershell
Get-ChildItem docker-compose.yml
```

Os dois arquivos precisam aparecer.

## Construir a imagem

```powershell
docker build -t nanobot .
```

Espere a construção terminar antes de continuar.

## Primeiro comando oficial e erro encontrado

O fluxo oficial usa:

```powershell
docker compose run --rm nanobot-cli onboard
```

No Docker Desktop para Windows, esse comando pode terminar com:

```text
[entrypoint] warning: chown /home/nanobot/.nanobot failed
[entrypoint] error: started as root but setpriv privilege drop failed - refusing to run as root
```

O contêiner inicia como `root`, mas não consegue reduzir os privilégios. Execute diretamente como o usuário interno do Nanobot:

```powershell
docker compose run --rm --user 1000:1000 nanobot-cli onboard --wizard
```

## Configurar o Ollama Cloud com Gemma 4

No Windows, faça login:

```powershell
ollama signin
```

Depois teste o modelo:

```powershell
ollama run gemma4:cloud
```

Use `/bye` para sair.

No wizard do Nanobot, configure:

```text
Model: gemma4:cloud
Provider: ollama
API Base: http://host.docker.internal:11434/v1
```

Dentro do contêiner, `localhost` aponta para o próprio contêiner. Por isso usamos `host.docker.internal` para alcançar o Ollama instalado no Windows.

## Alterar o Gateway no próprio wizard

Depois de configurar o Gemma, continue no wizard e entre em:

```text
Advanced Settings
```

Escolha:

```text
Gateway
```

Altere:

```text
Host: 127.0.0.1
```

para:

```text
Host: 0.0.0.0
```

Mantenha:

```text
Port: 18790
```

Finalize em **Done** e depois em **Save and Exit**.

Essa é a forma preferencial, porque evita editar o `config.json` manualmente.

## Verificar a configuração

```powershell
docker compose run --rm --user 1000:1000 nanobot-cli status
```

## Testar o agente pela CLI

```powershell
docker compose run --rm --user 1000:1000 nanobot-cli agent -m "Responda apenas: Nanobot funcionando."
```

O teste precisa responder antes de iniciar a WebUI.

## Iniciar o gateway e segundo erro encontrado

O comando abaixo pode criar o serviço, mas o gateway pode entrar em reinicialização pelo mesmo erro de `setpriv`:

```powershell
docker compose up -d nanobot-gateway
```

Confira os logs depois que o comando terminar:

```powershell
docker compose logs --tail 80 nanobot-gateway
```

Se aparecer novamente `refusing to run as root`, pare o Compose:

```powershell
docker compose down
```

Depois inicie o gateway como usuário `1000:1000`:

```powershell
docker compose run -d --name nanobot-gateway --service-ports --user 1000:1000 nanobot-gateway
```

Confirme:

```powershell
docker ps
```

## Erro da WebUI em branco

Mesmo com o modelo e o gateway funcionando, a WebUI pode continuar em branco.

Evidência típica nos logs:

```text
WebSocket server listening on ws://127.0.0.1:8765/
```

O endpoint de saúde pode funcionar normalmente:

```text
http://127.0.0.1:18790/health
```

com:

```json
{"status":"ok"}
```

A causa é:

```text
127.0.0.1 dentro do contêiner não é o localhost do Windows
```

Quando o serviço fica preso ao loopback interno do contêiner, o Docker publica a porta, mas não consegue encaminhar o navegador do Windows até ela.

## Correção preferencial pelo wizard

Execute novamente:

```powershell
docker compose run --rm --user 1000:1000 nanobot-cli onboard --wizard
```

Entre em:

```text
Advanced Settings → Gateway
```

Confirme:

```text
Host: 0.0.0.0
Port: 18790
```

Salve em **Done** e **Save and Exit**.

## Correção manual de emergência

Use este procedimento apenas se o wizard não salvar a alteração ou se os logs continuarem mostrando `127.0.0.1:8765`.

O bloco abaixo pertence ao mesmo procedimento e pode ser colado inteiro no PowerShell:

```powershell
$configPath = "$env:USERPROFILE\.nanobot\config.json"
Copy-Item $configPath "$configPath.bak" -Force

$config = Get-Content -Raw -LiteralPath $configPath | ConvertFrom-Json
$config.channels.websocket.host = "0.0.0.0"

$json = $config | ConvertTo-Json -Depth 100
$utf8SemBom = New-Object System.Text.UTF8Encoding($false)
[System.IO.File]::WriteAllText($configPath, $json, $utf8SemBom)
```

O comando cria um backup em:

```text
config.json.bak
```

Não substitua a gravação final por `Set-Content -Encoding utf8`. Dependendo da versão do PowerShell, ele pode inserir um marcador UTF-8 BOM, e o Nanobot pode recusar o arquivo com:

```text
Unexpected UTF-8 BOM
```

Se esse erro já tiver acontecido, o mesmo bloco acima regrava o JSON como UTF-8 sem BOM.

O `tokenIssueSecret` precisa estar configurado para o Nanobot aceitar `0.0.0.0` com proteção.

## Recriar o gateway após a alteração

Primeiro remova o contêiner anterior:

```powershell
docker rm -f nanobot-gateway
```

Depois recrie:

```powershell
docker compose run -d --name nanobot-gateway --service-ports --user 1000:1000 nanobot-gateway
```

Confira os logs:

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

Depois abra no navegador:

```text
http://localhost:8765
```

## Verificar o gateway

```powershell
curl.exe http://127.0.0.1:18790/health
```

Resposta esperada:

```json
{"status":"ok"}
```

## Configurar outros modelos depois

Depois que a WebUI abrir, outros provedores e modelos podem ser configurados em:

```text
Settings → Models
```

Para a instalação inicial, o `gemma4:cloud` pelo Ollama é suficiente.

## Parar o Nanobot

```powershell
docker rm -f nanobot-gateway
```

## Atualizar o projeto

```powershell
Set-Location "$HOME\Documents\nanobot"
```

```powershell
git pull
```

```powershell
docker compose build --no-cache
```

## Remover o projeto

```powershell
docker rm -f nanobot-gateway
```

```powershell
docker compose down
```

```powershell
Set-Location "$HOME\Documents"
```

```powershell
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
