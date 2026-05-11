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

## Exemplo de arquitetura híbrida com Ollama e Groq

O Hermes Agent pode usar modelos diferentes para agentes diferentes.

Exemplo:

```text
Hermes Agent
├── Orchestrator → Ollama / qwen2.5:14b
├── Coder → Ollama / qwen2.5-coder:7b
├── Researcher → Groq / llama-3.3-70b-versatile
└── Fast Agent → Groq / llama-3.1-8b-instant
```

Neste exemplo:

- Dois agentes usam Ollama local
- Dois agentes usam Groq cloud
- Cada agente pode ter função diferente
- O Hermes pode delegar tarefas entre eles

Exemplo conceitual de configuração:

```yaml
model:
  provider: "ollama"
  model: "qwen2.5:14b"

delegation:
  provider: "groq"
  model: "llama-3.3-70b-versatile"
```

Também é possível usar somente Ollama local.

Exemplo:

```text
Orchestrator → qwen2.5:14b
Coder → qwen2.5-coder:7b
Fast Agent → phi4-mini
Researcher → gemma3:12b
```

Neste caso todos os agentes usam Ollama.

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
