# Como instalar Hermes Agent e Hermes Workspace no Windows 11 com WSL2, Docker e Ollama no Linux

## Objetivo

Instalar o Hermes Agent usando Docker dentro do Ubuntu no WSL2 e usar o Hermes Workspace como painel web para acessar o Hermes pelo navegador do Windows.

Neste fluxo, o Ollama também fica instalado dentro do Linux/WSL.

## Arquitetura usada

```text
Windows 11
└── Navegador do Windows
    └── Acessa o Hermes Workspace em http://localhost:3000

Ubuntu no WSL2
├── Ollama Linux
│   └── Porta 11434
├── Docker
│   └── Hermes Agent em container
│       └── Usa o Ollama do WSL
├── Hermes Gateway/API
│   └── Porta 8642
├── Hermes Dashboard
│   └── Porta 9119
└── Hermes Workspace
    └── Painel web para usar o Hermes pelo navegador
```

## Portas usadas

```text
Ollama: http://127.0.0.1:11434
Hermes Gateway: http://127.0.0.1:8642
Hermes Dashboard: http://127.0.0.1:9119
Hermes Workspace: http://localhost:3000
```

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

## 3. Confirmar se o Ubuntu está em WSL2

Onde rodar: PowerShell

```powershell
wsl -l -v
```

## 4. Atualizar o Ubuntu

Onde rodar: Ubuntu/WSL

```bash
sudo apt update
sudo apt upgrade -y
```

## 5. Instalar dependências básicas

Onde rodar: Ubuntu/WSL

```bash
sudo apt install -y curl git build-essential ca-certificates gnupg lsb-release zstd
```

## 6. Instalar Docker no Ubuntu/WSL

Onde rodar: Ubuntu/WSL

```bash
sudo apt update
sudo apt install -y ca-certificates curl gnupg
```

```bash
sudo install -m 0755 -d /etc/apt/keyrings
```

```bash
curl -fsSL "https://download.docker.com/linux/ubuntu/gpg" | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg
```

```bash
sudo chmod a+r /etc/apt/keyrings/docker.gpg
```

```bash
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu \
  $(. /etc/os-release && echo "$VERSION_CODENAME") stable" | \
  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
```

```bash
sudo apt update
```

```bash
sudo apt install -y docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
```

## 7. Liberar Docker para o usuário atual

Onde rodar: Ubuntu/WSL

```bash
sudo usermod -aG docker "$USER"
```

Feche o Ubuntu e abra novamente.

## 8. Testar Docker

Onde rodar: Ubuntu/WSL

```bash
docker --version
```

```bash
docker compose version
```

```bash
docker run --rm hello-world
```

## 9. Instalar Ollama no Linux/WSL

Onde rodar: Ubuntu/WSL

```bash
sudo apt update
sudo apt install -y zstd
```

```bash
curl -fsSL "https://ollama.com/install.sh" | sh
```

## 10. Iniciar Ollama

Onde rodar: Ubuntu/WSL

```bash
ollama serve
```

## 11. Testar Ollama

Onde rodar: outro terminal Ubuntu/WSL

```bash
curl "http://127.0.0.1:11434/api/tags"
```

```bash
curl "http://127.0.0.1:11434/v1/models"
```

## 12. Baixar modelo

Onde rodar: Ubuntu/WSL

```bash
ollama pull gemma4:31b-cloud
```

## 13. Criar pasta do Hermes

Onde rodar: Ubuntu/WSL

```bash
cd "$HOME"
```

```bash
mkdir -p "$HOME/hermes-docker/data"
```

```bash
cd "$HOME/hermes-docker"
```

## 14. Baixar imagem correta do Hermes Agent

Onde rodar: Ubuntu/WSL

```bash
docker pull nousresearch/hermes-agent:latest
```

Se aparecer erro:

```text
TLS handshake timeout
```

Rode novamente o mesmo comando.

Não use:

```text
ghcr.io/nousresearch/hermes-agent:latest
```

## 15. Configurar modelo do Hermes

Onde rodar: Ubuntu/WSL

```bash
docker run -it --rm \
  --network host \
  -v "$HOME/hermes-docker/data:/opt/data" \
  nousresearch/hermes-agent:latest model
```

## Configuração usada

### API base URL

```text
http://127.0.0.1:11434/v1
```

### API key

Deixar vazio.

### Modelo

```text
gemma4:31b-cloud
```

### Context length

Deixar vazio para auto-detect.

### Display name

```text
ollama
```

## Importante sobre WSL2 + Docker + Ollama

No WSL2 com Docker Engine rodando dentro do Ubuntu:

```bash
--network host
```

Sem isso o container do Hermes não consegue acessar corretamente o Ollama local.

## 16. Subir Hermes Gateway/API

Onde rodar: Ubuntu/WSL

```bash
docker run -d \
  --name hermes-agent \
  --restart unless-stopped \
  --network host \
  -v "$HOME/hermes-docker/data:/opt/data" \
  -e API_SERVER_ENABLED=true \
  -e API_SERVER_HOST=0.0.0.0 \
  -e API_SERVER_PORT=8642 \
  -e API_SERVER_KEY=12345678 \
  -e API_SERVER_CORS_ORIGINS="*" \
  nousresearch/hermes-agent:latest gateway run
```

## 17. Entrar no chat/CLI do Hermes

Onde rodar: Ubuntu/WSL

```bash
docker exec -it hermes-agent /opt/hermes/.venv/bin/hermes chat
```

## 18. Ver logs do Hermes

Onde rodar: Ubuntu/WSL

```bash
docker logs -f hermes-agent
```

## 19. Testar Hermes Gateway

Onde rodar: Ubuntu/WSL

```bash
curl "http://127.0.0.1:8642/health"
```

## 20. Subir Hermes Dashboard

Onde rodar: Ubuntu/WSL

```bash
docker run -d \
  --name hermes-dashboard \
  --restart unless-stopped \
  --network host \
  -v "$HOME/hermes-docker/data:/opt/data" \
  nousresearch/hermes-agent:latest dashboard --host 127.0.0.1 --port 9119 --no-open --tui
```

## Importante sobre o Dashboard

NÃO usar:

```bash
--host 0.0.0.0
```

As versões atuais do Hermes recusam iniciar o dashboard dessa forma por segurança e o container entra em restart infinito.

Erro encontrado:

```text
Refusing to bind to 0.0.0.0 — the dashboard exposes API keys and config without robust authentication.
```

## 21. Abrir Hermes Dashboard

Onde rodar: navegador do Windows

```text
http://localhost:9119
```

## 22. Ver logs do Dashboard

Onde rodar: Ubuntu/WSL

```bash
docker logs hermes-dashboard
```

## 23. Verificar containers

Onde rodar: Ubuntu/WSL

```bash
docker ps
```

Containers esperados:

```text
hermes-agent
hermes-dashboard
```

## 24. Reiniciar containers

### Reiniciar Gateway

```bash
docker rm -f hermes-agent
```

Depois subir novamente o gateway.

### Reiniciar Dashboard

```bash
docker rm -f hermes-dashboard
```

Depois subir novamente o dashboard.

## 25. Instalar Node.js 22

Onde rodar: Ubuntu/WSL

```bash
curl -fsSL "https://deb.nodesource.com/setup_22.x" | sudo -E bash -
sudo apt install -y nodejs
```

## 26. Instalar pnpm

Onde rodar: Ubuntu/WSL

```bash
sudo npm install -g pnpm
```

## 27. Instalar Hermes Workspace

Onde rodar: Ubuntu/WSL

```bash
cd "$HOME"
git clone "https://github.com/outsourc-e/hermes-workspace.git"
cd "hermes-workspace"
pnpm install
cp ".env.example" ".env"
```

## 28. Configurar Hermes Workspace

Onde rodar: Ubuntu/WSL

```bash
cd "$HOME/hermes-workspace"
printf "\nHERMES_API_URL=http://127.0.0.1:8642\n" >> ".env"
printf "HERMES_DASHBOARD_URL=http://127.0.0.1:9119\n" >> ".env"
```

## 29. Iniciar Hermes Workspace

Onde rodar: Ubuntu/WSL

```bash
cd "$HOME/hermes-workspace"
pnpm dev
```

## 30. Abrir Hermes Workspace

Onde rodar: navegador do Windows

```text
http://localhost:3000
```
