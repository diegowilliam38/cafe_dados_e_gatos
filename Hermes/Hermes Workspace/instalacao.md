# Hermes Agent + Hermes Workspace no Windows 11 com Docker Desktop + WSL2

## Arquitetura

```text
Windows 11
├── Docker Desktop
├── Ollama Windows
└── Hermes Workspace no navegador

WSL2 Ubuntu
└── Terminal para comandos
```

## 1. Abrir Docker Desktop

Esperar aparecer:

```text
Engine running
```

## 2. Abrir Ubuntu WSL

Onde rodar: PowerShell

```powershell
wsl -d Ubuntu
```

## 3. Criar pasta do projeto

Onde rodar: Ubuntu/WSL

```bash
mkdir -p "$HOME/hermes-docker"
cd "$HOME/hermes-docker"
```

## 4. Criar pasta persistente

```bash
mkdir -p "$HOME/hermes-docker/data"
```

## 5. Criar docker-compose.yml

```bash
nano docker-compose.yml
```

Colar:

```yaml
services:
  hermes-agent:
    image: nousresearch/hermes-agent:latest
    container_name: hermes-agent
    restart: unless-stopped
    volumes:
      - ./data:/opt/data
    environment:
      API_SERVER_ENABLED: "true"
      API_SERVER_HOST: "0.0.0.0"
      API_SERVER_PORT: "8642"
      API_SERVER_KEY: "12345678"
      API_SERVER_CORS_ORIGINS: "*"
    ports:
      - "8642:8642"
    command: gateway run

  hermes-dashboard:
    image: nousresearch/hermes-agent:latest
    container_name: hermes-dashboard
    restart: unless-stopped
    volumes:
      - ./data:/opt/data
    ports:
      - "9119:9119"
    command: dashboard --host 127.0.0.1 --port 9119 --no-open --tui
```

Salvar:

```text
CTRL + O
ENTER
CTRL + X
```

## 6. Baixar Hermes Agent

```bash
docker pull nousresearch/hermes-agent:latest
```

## 7. Configurar modelo

```bash
docker run -it --rm \
  -v "$HOME/hermes-docker/data:/opt/data" \
  nousresearch/hermes-agent:latest model
```

Usar:

```text
API base URL:
http://host.docker.internal:11434/v1

API key:
deixar vazio

Modelo:
gemma4:31b-cloud

Display name:
ollama
```

## 8. Subir Hermes

```bash
cd "$HOME/hermes-docker"
docker compose up -d
```

## 9. Verificar containers

```bash
docker ps
```

Esperado:

```text
hermes-agent
hermes-dashboard
```

## 10. Testar Hermes

```bash
curl "http://localhost:8642/health"
```

## 11. Abrir Dashboard

```text
http://localhost:9119
```

## 12. Entrar no chat Hermes

```bash
docker exec -it hermes-agent /opt/hermes/.venv/bin/hermes chat
```

## 13. Clonar Hermes Workspace

```bash
cd "$HOME/hermes-docker"

git clone "https://github.com/outsourc-e/hermes-workspace.git"
```

## 14. Entrar na pasta

```bash
cd "$HOME/hermes-docker/hermes-workspace"
```

## 15. Criar .env

```bash
cp ".env.example" ".env"
```

## 16. Configurar .env

```bash
cat >> ".env" << "EOF"

HERMES_API_URL=http://host.docker.internal:8642
HERMES_DASHBOARD_URL=http://host.docker.internal:9119
HERMES_API_TOKEN=12345678

EOF
```

## 17. Criar Dockerfile

```bash
nano Dockerfile
```

Colar:

```Dockerfile
FROM node:22-bookworm

WORKDIR /app

RUN corepack enable

COPY package.json pnpm-lock.yaml* ./

RUN pnpm install

COPY . .

EXPOSE 3000

CMD ["pnpm", "dev", "--host", "0.0.0.0"]
```

Salvar:

```text
CTRL + O
ENTER
CTRL + X
```

## 18. Editar docker-compose.yml

```bash
cd "$HOME/hermes-docker"

nano docker-compose.yml
```

Deixar assim:

```yaml
services:
  hermes-agent:
    image: nousresearch/hermes-agent:latest
    container_name: hermes-agent
    restart: unless-stopped
    volumes:
      - ./data:/opt/data
    environment:
      API_SERVER_ENABLED: "true"
      API_SERVER_HOST: "0.0.0.0"
      API_SERVER_PORT: "8642"
      API_SERVER_KEY: "12345678"
      API_SERVER_CORS_ORIGINS: "*"
    ports:
      - "8642:8642"
    command: gateway run

  hermes-dashboard:
    image: nousresearch/hermes-agent:latest
    container_name: hermes-dashboard
    restart: unless-stopped
    volumes:
      - ./data:/opt/data
    ports:
      - "9119:9119"
    command: dashboard --host 127.0.0.1 --port 9119 --no-open --tui

  hermes-workspace:
    build:
      context: ./hermes-workspace
    container_name: hermes-workspace
    restart: unless-stopped
    env_file:
      - ./hermes-workspace/.env
    ports:
      - "3000:3000"
```

Salvar:

```text
CTRL + O
ENTER
CTRL + X
```

## 19. Subir tudo

```bash
cd "$HOME/hermes-docker"

docker compose up -d --build
```

## 20. Verificar containers

```bash
docker ps
```

Esperado:

```text
hermes-agent
hermes-dashboard
hermes-workspace
```

## 21. Abrir Hermes Workspace

```text
http://localhost:3000
```

## 22. Ver logs

Hermes Agent:

```bash
docker logs -f hermes-agent
```

Hermes Dashboard:

```bash
docker logs -f hermes-dashboard
```

Hermes Workspace:

```bash
docker logs -f hermes-workspace
```
