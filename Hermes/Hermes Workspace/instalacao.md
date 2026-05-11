# Como instalar Hermes Agent e Hermes Workspace no Windows 10 com WSL2, Docker e Ollama no Linux

## Objetivo

Instalar o Hermes Agent usando Docker dentro do Ubuntu no WSL2 e usar o Hermes Workspace como painel web para acessar o Hermes pelo navegador do Windows.

Neste fluxo, o Ollama também fica instalado dentro do Linux/WSL.

## Arquitetura usada

```text
Windows 10
└── Navegador do Windows
    └── Acessa o Hermes Workspace em http://localhost:3000

Ubuntu no WSL2
├── Ollama Linux
│   └── Porta 11434
├── Docker
│   └── Hermes Agent em container
│       └── Usa o Ollama do WSL
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
sudo apt install -y curl git build-essential ca-certificates gnupg lsb-release
```

## 7. Instalar Docker dentro do Ubuntu/WSL

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

## 8. Liberar Docker para o usuário atual

Onde rodar: Ubuntu/WSL

```bash
sudo usermod -aG docker "$USER"
```

Feche o Ubuntu e abra novamente.

Depois teste:

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
curl -fsSL "https://ollama.com/install.sh" | sh
```

## 10. Iniciar o Ollama no WSL

Onde rodar: Ubuntu/WSL

```bash
ollama serve
```

Deixe esse terminal aberto.

## 11. Testar o Ollama no WSL

Onde rodar: outro terminal Ubuntu/WSL

```bash
curl "http://127.0.0.1:11434/api/tags"
```

Se responder sem erro de conexão, o Ollama está ativo.

## 12. Baixar um modelo no Ollama

Onde rodar: Ubuntu/WSL

Escolha um modelo leve para testar primeiro.

```bash
ollama pull phi3:mini
```

Ou use outro modelo que já esteja disponível na sua máquina.

Para listar modelos:

```bash
ollama list
```

## 13. Criar pasta do Hermes

Onde rodar: Ubuntu/WSL

```bash
mkdir -p "$HOME/hermes-docker"
cd "$HOME/hermes-docker"
```

## 14. Criar arquivo docker-compose.yml do Hermes

Onde rodar: Ubuntu/WSL

```bash
nano "docker-compose.yml"
```

Cole o conteúdo abaixo:

```yaml
services:
  hermes:
    image: ghcr.io/nousresearch/hermes-agent:latest
    container_name: hermes-agent
    restart: unless-stopped
    network_mode: "host"
    environment:
      OLLAMA_BASE_URL: "http://127.0.0.1:11434"
      HERMES_HOST: "0.0.0.0"
      HERMES_PORT: "8642"
    volumes:
      - ./data:/data
```

Salve e saia.

No nano:

```text
CTRL + O
ENTER
CTRL + X
```

## 15. Subir o Hermes em Docker

Onde rodar: Ubuntu/WSL dentro da pasta "hermes-docker"

```bash
cd "$HOME/hermes-docker"
docker compose up -d
```

## 16. Ver logs do Hermes

Onde rodar: Ubuntu/WSL

```bash
docker logs -f hermes-agent
```

Para sair dos logs:

```text
CTRL + C
```

## 17. Testar Hermes Gateway

Onde rodar: Ubuntu/WSL

```bash
curl "http://127.0.0.1:8642/health"
```

Se responder sem erro de conexão, o Hermes Gateway está ativo.

## 18. Testar se o container acessa o Ollama

Onde rodar: Ubuntu/WSL

```bash
docker exec -it hermes-agent sh
```

Dentro do container, teste:

```bash
curl "http://127.0.0.1:11434/api/tags"
```

Depois saia do container:

```bash
exit
```

## 19. Instalar Node.js 22 para o Hermes Workspace

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

## 20. Instalar pnpm

Onde rodar: Ubuntu/WSL

```bash
sudo npm install -g pnpm
```

Verificar:

```bash
pnpm -v
```

## 21. Instalar Hermes Workspace

Onde rodar: Ubuntu/WSL

```bash
cd "$HOME"
git clone "https://github.com/outsourc-e/hermes-workspace.git"
cd "hermes-workspace"
pnpm install
cp ".env.example" ".env"
```

## 22. Configurar Hermes Workspace

Onde rodar: Ubuntu/WSL dentro da pasta "hermes-workspace"

```bash
cd "$HOME/hermes-workspace"
printf "\nHERMES_API_URL=http://127.0.0.1:8642\n" >> ".env"
printf "HERMES_DASHBOARD_URL=http://127.0.0.1:9119\n" >> ".env"
```

## 23. Iniciar Hermes Workspace

Onde rodar: Ubuntu/WSL dentro da pasta "hermes-workspace"

```bash
cd "$HOME/hermes-workspace"
pnpm dev
```

Deixe esse terminal aberto.

## 24. Abrir o Hermes Workspace

Onde rodar: navegador do Windows

Acesse:

```text
http://localhost:3000
```

## 25. Teste básico no Workspace

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

## 26. Parar o Hermes em Docker

Onde rodar: Ubuntu/WSL

```bash
cd "$HOME/hermes-docker"
docker compose down
```

## 27. Subir novamente o Hermes em Docker

Onde rodar: Ubuntu/WSL

```bash
cd "$HOME/hermes-docker"
docker compose up -d
```

## 28. Remover Hermes em Docker mantendo os dados

Onde rodar: Ubuntu/WSL

```bash
cd "$HOME/hermes-docker"
docker compose down
```

## 29. Remover Hermes em Docker apagando os dados persistentes

Atenção: este comando apaga a pasta local de dados do Hermes criada neste tutorial.

Onde rodar: Ubuntu/WSL

```bash
cd "$HOME/hermes-docker"
docker compose down
rm -rf "$HOME/hermes-docker/data"
```

## 30. Remover Hermes Workspace

Onde rodar: Ubuntu/WSL

```bash
rm -rf "$HOME/hermes-workspace"
```
