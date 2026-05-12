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

## 3. Confirmar se o Ubuntu está em WSL2

Onde rodar: PowerShell

```powershell
wsl -l -v
```

Se o Ubuntu não estiver como versão 2, rode:

```powershell
wsl --set-version Ubuntu 2
```

Defina o WSL2 como padrão:

```powershell
wsl --set-default-version 2
```

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
sudo apt install -y curl git build-essential ca-certificates gnupg lsb-release zstd
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

## 9. Instalar dependência zstd antes do Ollama

Onde rodar: Ubuntu/WSL

```bash
sudo apt update
sudo apt install -y zstd
```

## 10. Instalar Ollama no Linux/WSL

Onde rodar: Ubuntu/WSL

```bash
curl -fsSL "https://ollama.com/install.sh" | sh
```

## 11. Iniciar o Ollama no WSL

Onde rodar: Ubuntu/WSL

```bash
ollama serve
```

Deixe esse terminal aberto.

## 12. Testar o Ollama no WSL

Onde rodar: outro terminal Ubuntu/WSL

```bash
curl "http://127.0.0.1:11434/api/tags"
```

Se responder sem erro de conexão, o Ollama está ativo.

## 13. Baixar um modelo no Ollama

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

## 14. Baixar a imagem correta do Hermes Agent

Onde rodar: Ubuntu/WSL

```bash
docker pull nousresearch/hermes-agent:latest
```

Não use esta imagem neste fluxo:

```text
ghcr.io/nousresearch/hermes-agent:latest
```

Se aparecer erro "denied" com "ghcr.io/nousresearch/hermes-agent:latest", troque para:

```text
nousresearch/hermes-agent:latest
```

## 15. Criar pasta de dados persistentes do Hermes

Onde rodar: Ubuntu/WSL

```bash
mkdir -p "$HOME/.hermes"
```

## 16. Rodar configuração inicial do Hermes Agent

Onde rodar: Ubuntu/WSL

```bash
docker run -it --rm \
  -v "$HOME/.hermes:/opt/data" \
  nousresearch/hermes-agent:latest setup
```

Siga o assistente de configuração do Hermes.

## 17. Subir o Hermes Agent direto pelo Docker

Onde rodar: Ubuntu/WSL

```bash
docker run -d \
  --name hermes-agent \
  --restart unless-stopped \
  --network host \
  -v "$HOME/.hermes:/opt/data" \
  -e OLLAMA_BASE_URL="http://127.0.0.1:11434" \
  -e HERMES_HOST="0.0.0.0" \
  -e HERMES_PORT="8642" \
  nousresearch/hermes-agent:latest gateway run
```

## 18. Ver logs do Hermes

Onde rodar: Ubuntu/WSL

```bash
docker logs -f hermes-agent
```

Para sair dos logs:

```text
CTRL + C
```

## 19. Testar Hermes Gateway

Onde rodar: Ubuntu/WSL

```bash
curl "http://127.0.0.1:8642/health"
```

Se responder sem erro de conexão, o Hermes Gateway está ativo.

## 20. Testar se o Hermes acessa o Ollama

Onde rodar: Ubuntu/WSL

```bash
curl "http://127.0.0.1:11434/api/tags"
```

Se o Ollama responder, o endereço usado pelo Hermes está correto no WSL.

## 21. Instalar Node.js 22 para o Hermes Workspace

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

## 22. Instalar pnpm

Onde rodar: Ubuntu/WSL

```bash
sudo npm install -g pnpm
```

Verificar:

```bash
pnpm -v
```

## 23. Instalar Hermes Workspace

Onde rodar: Ubuntu/WSL

```bash
cd "$HOME"
git clone "https://github.com/outsourc-e/hermes-workspace.git"
cd "hermes-workspace"
pnpm install
cp ".env.example" ".env"
```

## 24. Configurar Hermes Workspace

Onde rodar: Ubuntu/WSL dentro da pasta "hermes-workspace"

```bash
cd "$HOME/hermes-workspace"
printf "\nHERMES_API_URL=http://127.0.0.1:8642\n" >> ".env"
printf "HERMES_DASHBOARD_URL=http://127.0.0.1:9119\n" >> ".env"
```

## 25. Iniciar Hermes Workspace

Onde rodar: Ubuntu/WSL dentro da pasta "hermes-workspace"

```bash
cd "$HOME/hermes-workspace"
pnpm dev
```

Deixe esse terminal aberto.

## 26. Abrir o Hermes Workspace

Onde rodar: navegador do Windows

Acesse:

```text
http://localhost:3000
```

## 27. Teste básico no Workspace

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

## 28. Parar o Hermes Agent em Docker

Onde rodar: Ubuntu/WSL

```bash
docker stop hermes-agent
```

## 29. Subir novamente o Hermes Agent em Docker

Onde rodar: Ubuntu/WSL

```bash
docker start hermes-agent
```

## 30. Remover Hermes Agent mantendo os dados

Onde rodar: Ubuntu/WSL

```bash
docker stop hermes-agent
```

Depois remova o container pelo Docker somente se tiver certeza.

## 31. Remover Hermes Agent apagando os dados persistentes

Atenção: este procedimento apaga a pasta local de dados do Hermes criada neste tutorial.

Onde rodar: Ubuntu/WSL

```bash
docker stop hermes-agent
```

Depois remova manualmente o container e apague a pasta "$HOME/.hermes" somente se tiver certeza.

## 32. Remover Hermes Workspace

Onde rodar: Ubuntu/WSL

Apague manualmente a pasta "$HOME/hermes-workspace" somente se tiver certeza.
