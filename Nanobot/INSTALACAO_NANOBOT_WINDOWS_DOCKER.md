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

Primeiro vá para a pasta Documentos:

```powershell
Set-Location "$HOME\Documents"
```

Depois clone o projeto:

```powershell
git clone https://github.com/HKUDS/nanobot.git
```

Quando o download terminar, entre na pasta:

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

Em seguida, escolha:

```text
Gateway
```

Altere apenas o campo:

```text
Host: 127.0.0.1
```

para:

```text
Host: 0.0.0.0
```

Mantenha a porta padrão:

```text
Port: 18790
```

Finalize em **Done** e depois escolha **Save and Exit**.

Essa alteração deve ser feita diretamente pelo wizard. Não é necessário editar manualmente o arquivo `config.json`.

## Verificar a configuração

```powershell
docker compose run --rm --user 1000:1000 nanobot-cli status
```

## Testar o agente pela CLI

```powershell
docker compose run --rm --user 1000:1000 nanobot-cli agent -m "Responda apenas: Nanobot funcionando."
```

O teste precisa responder antes de iniciar a WebUI.

## Iniciar o gateway

O comando abaixo pode criar o serviço, mas o gateway pode entrar em reinicialização pelo mesmo erro de `setpriv`:

```powershell
docker compose up -d nanobot-gateway
```

Confira os logs somente depois que o comando anterior terminar:

```powershell
docker compose logs --tail 80 nanobot-gateway
```

Se aparecer novamente `refusing to run as root`, primeiro pare o Compose:

```powershell
docker compose down
```

Espere o comando terminar. Depois inicie o gateway como usuário `1000:1000`:

```powershell
docker compose run -d --name nanobot-gateway --service-ports --user 1000:1000 nanobot-gateway
```

Confirme que o contêiner está ativo:

```powershell
docker ps
```

## Confirmar o acesso da WebUI

Confira os logs:

```powershell
docker logs --tail 40 nanobot-gateway
```

O resultado correto deve mostrar o serviço ouvindo em uma interface acessível pelo Docker, por exemplo:

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

## O que causava a WebUI em branco

O gateway e o modelo podiam funcionar normalmente, mas a interface permanecia em branco porque o serviço estava vinculado ao loopback interno do contêiner.

No Docker:

```text
127.0.0.1 dentro do contêiner não é o localhost do Windows
```

Ao alterar o host para `0.0.0.0` pelo wizard, o Docker consegue encaminhar a porta publicada até o serviço dentro do contêiner.

## Configurar outros modelos depois

Depois que a WebUI abrir, outros provedores e modelos podem ser configurados diretamente pela interface, em:

```text
Settings → Models
```

Para a instalação inicial, o `gemma4:cloud` pelo Ollama é suficiente.

## Verificar o gateway

```powershell
curl.exe http://127.0.0.1:18790/health
```

A resposta esperada é:

```json
{"status":"ok"}
```

## Parar o Nanobot

Como o gateway foi criado com `docker compose run`, remova-o com:

```powershell
docker rm -f nanobot-gateway
```

## Atualizar o projeto

Entre na pasta do projeto:

```powershell
Set-Location "$HOME\Documents\nanobot"
```

Atualize o código:

```powershell
git pull
```

Quando terminar, reconstrua a imagem:

```powershell
docker compose build --no-cache
```

## Remover o projeto

Primeiro remova o gateway:

```powershell
docker rm -f nanobot-gateway
```

Depois encerre os serviços restantes:

```powershell
docker compose down
```

Saia da pasta do projeto:

```powershell
Set-Location "$HOME\Documents"
```

Por último, remova a pasta:

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
