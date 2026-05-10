# Como instalar o Hermes Workspace

## Pasta no GitHub

Criar a pasta:

```text
Hermes/Hermes Workspace/
```

Arquivos:

```text
Hermes/Hermes Workspace/instalacao.md
```

## O que vamos fazer

```text
instalar dependências
baixar o Hermes Workspace
configurar o arquivo .env
apontar para o Hermes Gateway
subir a interface em localhost:3000
testar o funcionamento
```

## Portas usadas

```text
Hermes Workspace  -> http://localhost:3000
Hermes Gateway    -> http://127.0.0.1:8642
Hermes Dashboard  -> http://127.0.0.1:9119
Ollama            -> http://127.0.0.1:11434
```

## Requisitos

```text
Linux, macOS ou WSL2
Node.js 22+
pnpm
git
curl
Hermes Agent instalado
backend compatível com OpenAI
```

## 1. Entrar no terminal

No Linux ou WSL2:

```bash
cd ~
```

## 2. Atualizar o sistema

```bash
sudo apt update
```

## 3. Instalar dependências básicas

```bash
sudo apt install -y git curl python3 python3-pip
```

## 4. Verificar Node

```bash
node --version
```

Precisa ser Node 22 ou superior.

Se já estiver correto, seguir para o passo do pnpm.

## 5. Instalar Node 22 com NVM

```bash
curl -fsSL https://raw.githubusercontent.com/nvm-sh/nvm/v0.40.1/install.sh | bash
```

Fechar e abrir o terminal novamente.

Depois:

```bash
nvm install 22
nvm use 22
node --version
```

## 6. Instalar pnpm

```bash
corepack enable
corepack prepare pnpm@latest --activate
pnpm --version
```

## 7. Verificar se o Hermes existe

```bash
hermes --version
```

Se o comando não existir, instalar o Hermes Agent primeiro.

## 8. Backup antes de mexer

```bash
mkdir -p ~/.hermes/backups
cp ~/.hermes/config.yaml ~/.hermes/backups/config.yaml.bak 2>/dev/null || true
cp ~/.hermes/.env ~/.hermes/backups/env.bak 2>/dev/null || true
```

## 9. Baixar o Hermes Workspace

```bash
cd ~
git clone https://github.com/outsourc-e/hermes-workspace.git
cd hermes-workspace
```

## 10. Instalar dependências

```bash
pnpm install
```

## 11. Criar o arquivo .env

```bash
cp .env.example .env
```

## 12. Configurar a URL do Hermes Gateway

```bash
printf '\nHERMES_API_URL=http://127.0.0.1:8642\n' >> .env
```

## 13. Conferir o .env

```bash
cat .env
```

## 14. Subir o Hermes Gateway

Abrir outro terminal:

```bash
hermes gateway run
```

Se for a primeira vez, pode pedir configuração do Hermes.

## 15. Subir o Hermes Workspace

Voltar para o terminal da pasta do Workspace:

```bash
cd ~/hermes-workspace
pnpm dev
```

## 16. Abrir no navegador

```text
http://localhost:3000
```

## 17. Teste inicial

No chat do Workspace, enviar:

```text
Oi, você está conectado ao Hermes Agent?
```

## 18. Se pedir backend

Usar:

```text
http://127.0.0.1:8642
```

## 19. Instalação rápida oficial

O site também mostra um instalador de uma linha:

```bash
curl -fsSL https://hermes-workspace.com/install.sh | bash
```

## 20. Instalação rápida pelo GitHub

```bash
curl -fsSL https://raw.githubusercontent.com/outsourc-e/hermes-workspace/main/install.sh | bash
```

## 21. O que o instalador faz

Segundo o script do projeto, ele faz:

```text
verifica Node 22+
verifica git
verifica pnpm
instala Hermes Agent via instalador oficial da Nous, se necessário
clona o Hermes Workspace
cria/configura .env
ativa o Hermes API server
instala dependências
linka skills incluídas
```

## 22. Observação sobre curl | bash

Para vídeo e ambiente de teste, o comando rápido é prático.

Para ambiente principal, prefira clonar o repositório e olhar o script antes:

```bash
cd ~
git clone https://github.com/outsourc-e/hermes-workspace.git
cd hermes-workspace
less install.sh
```

## 23. Rodar usando o instalador com pasta personalizada

```bash
INSTALL_DIR="$HOME/frankenstein-ias/apps/hermes-workspace" bash -c "$(curl -fsSL https://raw.githubusercontent.com/outsourc-e/hermes-workspace/main/install.sh)"
```

## 24. Rodar manualmente na pasta do Projeto Robô Frank

```bash
mkdir -p ~/frankenstein-ias/apps
cd ~/frankenstein-ias/apps
git clone https://github.com/outsourc-e/hermes-workspace.git
cd hermes-workspace
pnpm install
cp .env.example .env
printf '\nHERMES_API_URL=http://127.0.0.1:8642\n' >> .env
pnpm dev
```

Abrir:

```text
http://localhost:3000
```

## 25. Usar com Ollama em modo portátil

Este modo não usa os recursos completos do Hermes Agent.

Ele aponta o Workspace direto para um backend OpenAI-compatible.

Se o Ollama estiver com endpoint OpenAI-compatible ativo:

```bash
cd ~/hermes-workspace
HERMES_API_URL=http://127.0.0.1:11434/v1 pnpm dev
```

Abrir:

```text
http://localhost:3000
```

Observação:

```text
chat pode funcionar
memória, skills, jobs e sessions podem não funcionar
isso é esperado no modo portátil
```

## 26. Usar com Hermes Gateway para recursos completos

O modo mais completo é:

```text
Hermes Workspace -> Hermes Gateway -> Hermes Agent -> Provedor/modelo
```

Subir Gateway:

```bash
hermes gateway run
```

Subir Workspace:

```bash
cd ~/hermes-workspace
pnpm dev
```

Abrir:

```text
http://localhost:3000
```

## 27. Atualizar Hermes Workspace

```bash
cd ~/hermes-workspace
git pull
pnpm install
pnpm dev
```

## 28. Parar o Workspace

No terminal onde ele está rodando:

```text
CTRL + C
```

## 29. Remover apenas o Hermes Workspace

```bash
cd ~
rm -rf ~/hermes-workspace
```

## 30. Remover a versão dentro do Projeto Robô Frank

```bash
rm -rf ~/frankenstein-ias/apps/hermes-workspace
```

## 31. Restaurar backup da configuração do Hermes

```bash
cp ~/.hermes/backups/config.yaml.bak ~/.hermes/config.yaml 2>/dev/null || true
cp ~/.hermes/backups/env.bak ~/.hermes/.env 2>/dev/null || true
```

## 32. Limpar dependências opcionais

```bash
rm -rf ~/.cache/pnpm
```

## 33. O que não remover

Não remover estas pastas se você quer manter o Hermes Agent instalado:

```text
~/.hermes
~/.local/bin/hermes
```

## 34. Remoção total do Hermes Workspace com backups preservados

```bash
mkdir -p ~/backups-hermes-workspace
cp -r ~/hermes-workspace ~/backups-hermes-workspace/hermes-workspace-bak 2>/dev/null || true
rm -rf ~/hermes-workspace
```

## 35. Teste para saber se a porta 3000 está ocupada

```bash
ss -ltnp | grep 3000 || true
```

## 36. Teste para saber se o Gateway está respondendo

```bash
curl http://127.0.0.1:8642/v1/models
```

## 37. Teste para saber se o Workspace está rodando

```bash
curl http://localhost:3000
```

## 38. Se a porta 3000 estiver ocupada

```bash
cd ~/hermes-workspace
PORT=3001 pnpm dev
```

Abrir:

```text
http://localhost:3001
```

## 39. Se der erro de Node

```bash
node --version
```

Se for menor que 22:

```bash
nvm install 22
nvm use 22
```

## 40. Se der erro de pnpm

```bash
corepack enable
corepack prepare pnpm@latest --activate
pnpm --version
```

## 41. Se o Hermes não responder

```bash
hermes --version
hermes gateway run
```

## 42. Se o chat abrir mas recursos avançados não aparecerem

Isso pode acontecer quando o backend é apenas OpenAI-compatible, mas não expõe as APIs extras do Hermes Agent.

Verificar se está usando:

```text
http://127.0.0.1:8642
```

e não apenas:

```text
http://127.0.0.1:11434/v1
```

## 43. Se mexeu nas configurações e quebrou

Restaurar:

```bash
cp ~/.hermes/backups/config.yaml.bak ~/.hermes/config.yaml
```

Depois reiniciar o Gateway:

```bash
hermes gateway run
```

## 44. Comandos mínimos para rodar

Terminal 1:

```bash
hermes gateway run
```

Terminal 2:

```bash
cd ~/hermes-workspace
pnpm dev
```

Navegador:

```text
http://localhost:3000
```
