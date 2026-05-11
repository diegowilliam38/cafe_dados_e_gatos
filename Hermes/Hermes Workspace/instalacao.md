# Como instalar Hermes Agent e Hermes Workspace no Windows com WSL2 e Docker

## Objetivo

Instalar o Hermes Agent dentro do Ubuntu no WSL2 e instalar o Hermes Workspace como painel web para usar o Hermes pelo navegador do Windows.

## Arquitetura usada

- Windows como sistema principal
- Ubuntu rodando dentro do WSL2
- Hermes Agent instalado dentro do Ubuntu/WSL
- Hermes Gateway rodando dentro do Ubuntu/WSL
- Hermes Dashboard rodando dentro do Ubuntu/WSL
- Hermes Workspace rodando dentro do Ubuntu/WSL
- Navegador do Windows acessando o Workspace
- Docker Desktop integrado ao WSL2 quando necessário

## Portas usadas

- Hermes Gateway: "http://127.0.0.1:8642"
- Hermes Dashboard: "http://127.0.0.1:9119"
- Hermes Workspace: "http://localhost:3000"

## 1. Verificar se o WSL está instalado

Onde rodar: PowerShell

```powershell
wsl --status
```

## 2. Instalar Ubuntu no WSL2

Onde rodar: PowerShell como Administrador

```powershell
wsl --install -d Ubuntu
```

Se o Windows pedir, reinicie o computador.

## 3. Corrigir erro do WSL no Windows 10

Use esta etapa se aparecer erro parecido com:

```text
WslRegisterDistribution failed with error: 0x80080005
Error: 0x80080005 Falha na execução do servidor
```

Onde rodar: PowerShell como Administrador

```powershell
dism.exe /online /enable-feature /featurename:Microsoft-Windows-Subsystem-Linux /all /norestart
```

Depois rode:

```powershell
dism.exe /online /enable-feature /featurename:VirtualMachinePlatform /all /norestart
```

Reinicie o computador.

Depois da reinicialização, abra o PowerShell como Administrador novamente e rode:

```powershell
wsl --set-default-version 2
```

Tente instalar ou abrir o Ubuntu novamente:

```powershell
wsl --install -d Ubuntu
```

Se o comando acima informar que o Ubuntu já está instalado, abra pelo Menu Iniciar.

Se ainda der erro no WSL2, instale o kernel oficial do WSL2 pela Microsoft:

```text
https://aka.ms/wsl2kernel
```

Depois reinicie o computador e tente abrir o Ubuntu novamente.

## 4. Abrir o Ubuntu

Onde rodar: Menu Iniciar do Windows

Procure por:

```text
Ubuntu
```

Na primeira abertura, crie um usuário e uma senha para o Linux.

## 5. Atualizar o Ubuntu

Onde rodar: Ubuntu/WSL

```bash
sudo apt update
sudo apt upgrade -y
```

## 6. Instalar dependências básicas

Onde rodar: Ubuntu/WSL

```bash
sudo apt install -y curl git build-essential ca-certificates
```

## 7. Instalar Node.js 22

Onde rodar: Ubuntu/WSL

```bash
curl -fsSL "https://deb.nodesource.com/setup_22.x" | sudo -E bash -
sudo apt install -y nodejs
```

Verificar:

```bash
node -v
npm -v
```

## 8. Instalar pnpm

Onde rodar: Ubuntu/WSL

```bash
sudo npm install -g pnpm
```

Verificar:

```bash
pnpm -v
```

## 9. Instalar Hermes Agent dentro do WSL

Onde rodar: Ubuntu/WSL

```bash
curl -fsSL "https://raw.githubusercontent.com/NousResearch/hermes-agent/main/scripts/install.sh" | bash
```

Feche o terminal Ubuntu e abra novamente.

Verificar instalação:

```bash
hermes --version
```

## 10. Configurar Hermes Agent

Onde rodar: Ubuntu/WSL

```bash
hermes setup
```

Configure o provedor e o modelo que será usado.

## 11. Testar Hermes Agent

Onde rodar: Ubuntu/WSL

```bash
hermes
```

Para sair:

```text
CTRL + C
```

## 12. Iniciar Hermes Gateway

Onde rodar: Ubuntu/WSL

```bash
hermes gateway run
```

Deixe esse terminal aberto.

## 13. Testar Hermes Gateway

Onde rodar: outro terminal Ubuntu/WSL

```bash
curl "http://127.0.0.1:8642/health"
```

Se responder sem erro de conexão, o gateway está ativo.

## 14. Iniciar Hermes Dashboard

Onde rodar: outro terminal Ubuntu/WSL

```bash
hermes dashboard
```

Deixe esse terminal aberto.

## 15. Testar Hermes Dashboard

Onde rodar: outro terminal Ubuntu/WSL

```bash
curl "http://127.0.0.1:9119/api/status"
```

Se responder sem erro de conexão, o dashboard está ativo.

## 16. Instalar Hermes Workspace

Onde rodar: Ubuntu/WSL

```bash
cd ~
git clone "https://github.com/outsourc-e/hermes-workspace.git"
cd hermes-workspace
pnpm install
cp ".env.example" ".env"
```

## 17. Configurar Hermes Workspace

Onde rodar: Ubuntu/WSL dentro da pasta "hermes-workspace"

```bash
cd "$HOME/hermes-workspace"
printf "\nHERMES_API_URL=http://127.0.0.1:8642\n" >> ".env"
printf "HERMES_DASHBOARD_URL=http://127.0.0.1:9119\n" >> ".env"
```

## 18. Iniciar Hermes Workspace

Onde rodar: Ubuntu/WSL dentro da pasta "hermes-workspace"

```bash
cd "$HOME/hermes-workspace"
pnpm dev
```

Deixe esse terminal aberto.

## 19. Abrir o Hermes Workspace

Onde rodar: navegador do Windows

Acesse:

```text
http://localhost:3000
```

## 20. Teste básico no Workspace

Onde rodar: navegador do Windows

Faça estes testes:

```text
Abrir o Hermes Workspace
Conferir se conectou ao Hermes Gateway
Enviar uma mensagem simples
Verificar se sessões aparecem
Verificar se memória aparece
Verificar se skills aparecem
Verificar se painel funciona como interface do Hermes Agent
```

## 21. Instalar Docker Desktop no Windows

Onde rodar: Windows

Baixe e instale o Docker Desktop pelo site oficial.

Durante a instalação, mantenha habilitada a opção de usar WSL2.

Depois de instalar, abra o Docker Desktop.

## 22. Ativar integração do Docker com Ubuntu/WSL

Onde rodar: Docker Desktop no Windows

Acesse:

```text
Settings > Resources > WSL Integration
```

Ative a integração para:

```text
Ubuntu
```

Clique em:

```text
Apply & Restart
```

## 23. Testar Docker dentro do WSL

Onde rodar: Ubuntu/WSL

```bash
docker --version
docker compose version
docker ps
```

Se os comandos responderem sem erro, o Docker está funcionando dentro do WSL.

## 24. Testar container simples

Onde rodar: Ubuntu/WSL

```bash
docker run "hello-world"
```

## 25. Parar Hermes Workspace

Onde rodar: terminal onde o Workspace está rodando

```text
CTRL + C
```

## 26. Parar Hermes Dashboard

Onde rodar: terminal onde o Dashboard está rodando

```text
CTRL + C
```

## 27. Parar Hermes Gateway

Onde rodar: terminal onde o Gateway está rodando

```text
CTRL + C
```

## 28. Atualizar Hermes Agent

Onde rodar: Ubuntu/WSL

```bash
hermes update
```

Se esse comando não existir na versão instalada, use novamente o instalador oficial:

```bash
curl -fsSL "https://raw.githubusercontent.com/NousResearch/hermes-agent/main/scripts/install.sh" | bash
```

## 29. Atualizar Hermes Workspace

Onde rodar: Ubuntu/WSL

```bash
cd "$HOME/hermes-workspace"
git pull
pnpm install
```

Depois, iniciar novamente:

```bash
pnpm dev
```

## 30. Remover somente Hermes Workspace

Aviso: este comando apaga a pasta do Hermes Workspace.

Não apaga a configuração principal do Hermes Agent.

Onde rodar: Ubuntu/WSL

```bash
rm -rf "$HOME/hermes-workspace"
```

## 31. Fazer backup dos dados do Hermes Agent

Aviso: a pasta ".hermes" pode conter configurações, memória, sessões, skills e dados persistentes do Hermes Agent.

Onde rodar: Ubuntu/WSL

```bash
cp -r "$HOME/.hermes" "$HOME/backup-hermes"
```

## 32. Remover Hermes Agent e dados persistentes

Aviso: este comando pode apagar configurações, memória, sessões, skills e dados persistentes do Hermes Agent.

Faça backup antes.

Onde rodar: Ubuntu/WSL

```bash
rm -rf "$HOME/.hermes"
rm -f "$HOME/.local/bin/hermes"
```

## 33. Verificar se Hermes foi removido

Onde rodar: Ubuntu/WSL

```bash
which hermes
hermes --version
```

Se o comando não for encontrado, o Hermes foi removido do PATH atual.

## 34. Observação importante

Este guia não instala o Hermes como aplicativo nativo puro no Windows.

O Hermes Agent roda dentro do Ubuntu no WSL2.

O Docker Desktop fica integrado ao WSL2.

O navegador do Windows acessa o Workspace usando a porta local.

## 35. Estrutura final esperada

Ao final, o ambiente fica assim:

```text
Windows
├── Navegador
│   └── Acessa "http://localhost:3000"
├── Docker Desktop
│   └── Integrado ao Ubuntu/WSL
└── WSL2
    └── Ubuntu
        ├── Hermes Agent
        ├── Hermes Gateway em "http://127.0.0.1:8642"
        ├── Hermes Dashboard em "http://127.0.0.1:9119"
        └── Hermes Workspace em "http://localhost:3000"
```
