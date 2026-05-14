# Como instalar Hermes Agent, Hermes Workspace e Hermes Desktop no Windows 11 com Docker Desktop, WSL2 e Ollama

## Objetivo

Instalar o ambiente básico do Hermes no Windows 11, com o menor número possível de passos e sem misturar instalações.

Este guia usa:

- Hermes Agent em Docker
- Hermes Dashboard dentro do mesmo container do Hermes Agent
- Hermes Workspace em Docker usando imagem pronta
- Hermes Desktop instalado no Windows
- Ollama rodando no Windows
- Ubuntu WSL2 apenas como terminal para comandos Docker

---

# Arquitetura usada

```text
Windows 11
├── Docker Desktop
├── Ollama Windows
├── Hermes Desktop
├── Navegador
│   ├── Hermes Dashboard
│   └── Hermes Workspace
└── WSL2 Ubuntu
    └── Terminal para comandos Docker

Docker
├── hermes-agent
│   ├── Hermes Gateway
│   └── Hermes Dashboard
└── hermes-workspace
```

---

# Decisões deste guia

```text
Hermes Agent: Docker
Hermes Dashboard: dentro do mesmo container do Hermes Agent
Hermes Workspace: Docker com imagem pronta
Hermes Desktop: aplicativo normal no Windows
Ollama: Windows
```

Não fazer neste guia:

```text
Não criar Dockerfile manual para o Workspace.
Não criar container separado para o Dashboard.
Não clonar o repositório do Workspace para a instalação básica.
Não usar o botão Get Started do Hermes Desktop para instalar outro Agent local, a menos que seja outro vídeo.
```

---

# Parte 1 - Preparar Docker Desktop e WSL2

## 1. Abrir Docker Desktop

Onde fazer: Windows

Abrir o Docker Desktop e esperar aparecer:

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

---

# Parte 2 - Criar arquivo .env básico

## 4. Criar .env

Onde rodar: Ubuntu/WSL

```bash
cd "$HOME/hermes-docker"
nano .env
```

Colar:

```env
API_SERVER_KEY=12345678
HERMES_PASSWORD=12345678
COOKIE_SECURE=0
```

Salvar:

```text
CTRL + O
ENTER
CTRL + X
```

## 5. O que é cada linha

```text
API_SERVER_KEY = chave para acessar o Hermes Agent Gateway
HERMES_PASSWORD = senha para entrar no Hermes Workspace
COOKIE_SECURE=0 = necessário para login local via http://localhost
```

Para gravação local, pode usar:

```text
12345678
```

Para uso real, trocar depois por uma senha mais forte.

---

# Parte 3 - Criar docker-compose.yml

## 6. Criar docker-compose.yml

Onde rodar: Ubuntu/WSL

```bash
cd "$HOME/hermes-docker"
nano docker-compose.yml
```

Colar:

```yaml
services:
  hermes-agent:
    image: nousresearch/hermes-agent:latest
    container_name: hermes-agent
    restart: unless-stopped
    command: ["gateway", "run"]
    env_file:
      - .env
    environment:
      API_SERVER_ENABLED: "true"
      API_SERVER_HOST: "0.0.0.0"
      API_SERVER_KEY: "${API_SERVER_KEY}"
      HERMES_DASHBOARD: "1"
    volumes:
      - hermes-data:/opt/data
    healthcheck:
      test: ["CMD-SHELL", "curl -fsS http://localhost:8642/health || exit 1"]
      interval: 10s
      timeout: 5s
      retries: 5
      start_period: 15s
    ports:
      - "8642:8642"
      - "9119:9119"

  hermes-workspace:
    image: ghcr.io/outsourc-e/hermes-workspace:latest
    container_name: hermes-workspace
    restart: unless-stopped
    depends_on:
      hermes-agent:
        condition: service_healthy
    env_file:
      - .env
    environment:
      HERMES_API_URL: "http://hermes-agent:8642"
      HERMES_API_TOKEN: "${API_SERVER_KEY}"
      HERMES_PASSWORD: "${HERMES_PASSWORD}"
      COOKIE_SECURE: "${COOKIE_SECURE}"
    ports:
      - "127.0.0.1:3000:3000"

volumes:
  hermes-data:
```

Salvar:

```text
CTRL + O
ENTER
CTRL + X
```

---

# Parte 4 - Subir Hermes Agent, Dashboard e Workspace

## 7. Baixar imagens

Onde rodar: Ubuntu/WSL

```bash
cd "$HOME/hermes-docker"
docker compose pull
```

## 8. Subir containers

Onde rodar: Ubuntu/WSL

```bash
cd "$HOME/hermes-docker"
docker compose up -d
```

## 9. Verificar containers

Onde rodar: Ubuntu/WSL

```bash
docker ps
```

Esperado:

```text
hermes-agent
hermes-workspace
```

O Dashboard não aparece como container separado.

Ele roda dentro do container:

```text
hermes-agent
```

---

# Parte 5 - Testar Hermes Agent, Dashboard e Workspace

## 10. Testar Hermes Agent

Onde rodar: Ubuntu/WSL

```bash
curl "http://localhost:8642/health"
```

Se responder, o Hermes Agent está no ar.

## 11. Abrir Hermes Dashboard

Onde abrir: navegador do Windows

```text
http://localhost:9119
```

## 12. Abrir Hermes Workspace

Onde abrir: navegador do Windows

```text
http://localhost:3000
```

Senha:

```text
12345678
```

Se o Workspace não fizer login e aparecer aviso de cookie no log, conferir se o `.env` tem:

```env
COOKIE_SECURE=0
```

Depois recriar o Workspace:

```bash
cd "$HOME/hermes-docker"
docker compose up -d --force-recreate hermes-workspace
```

---

# Parte 6 - Configurar modelo no Hermes

## 13. Entrar no Hermes Agent

Onde rodar: Ubuntu/WSL

```bash
docker exec -it hermes-agent hermes
```

Se o comando acima não abrir, usar:

```bash
docker exec -it hermes-agent /opt/hermes/.venv/bin/hermes
```

## 14. Configurar provedor/modelo

Dentro do Hermes, rodar a configuração de modelo.

Para Ollama no Windows, usar endpoint compatível com OpenAI:

```text
http://host.docker.internal:11434/v1
```

API key:

```text
deixar vazio
```

Modelo usado no teste:

```text
gemma4:31b-cloud
```

Nome de exibição:

```text
ollama
```

Se for usar outro modelo que já existe no Ollama, trocar apenas o nome do modelo.

## 15. Testar chat pelo terminal

Onde rodar: Ubuntu/WSL

```bash
docker exec -it hermes-agent /opt/hermes/.venv/bin/hermes chat
```

Mensagem de teste:

```text
Responda apenas: Hermes funcionando.
```

Se responder, o modelo está funcionando.

---

# Parte 7 - Configurar modelo pelo Dashboard

Também é possível ajustar o modelo pelo Dashboard.

Abrir:

```text
http://localhost:9119/config
```

Em General, preencher:

```text
Model:
ollama/gemma4:31b-cloud
```

Manter:

```text
Model Context Length:
0
```

Depois clicar em:

```text
Save
```

E reiniciar o Gateway pelo Dashboard ou pelo terminal:

```bash
docker restart hermes-agent
```

---

# Parte 8 - Ajuste de permissão do Workspace para criar agentes

Se ao criar agente/perfil no Workspace aparecer erro parecido com:

```text
EACCES: permission denied, mkdir "/home/workspace/.hermes/profiles/sage"
```

Rodar:

```bash
docker exec -u root -it hermes-workspace sh -lc "mkdir -p /home/workspace/.hermes/profiles && chown -R workspace:workspace /home/workspace/.hermes"
```

Se der erro dizendo que o usuário `workspace` não existe, usar:

```bash
docker exec -u root -it hermes-workspace sh -lc "mkdir -p /home/workspace/.hermes/profiles && chown -R 1000:1000 /home/workspace/.hermes"
```

Depois reiniciar o Workspace:

```bash
cd "$HOME/hermes-docker"
docker compose restart hermes-workspace
```

---

# Parte 9 - Instalar Hermes Desktop no Windows

## 16. Baixar Hermes Desktop

Onde fazer: Windows

Abrir:

```text
https://github.com/fathah/hermes-desktop/releases
```

Baixar o instalador do Windows:

```text
hermes-desktop-0.3.7-setup.exe
```

Ou a versão `.exe` mais recente disponível.

Não baixar para Windows:

```text
.blockmap
.AppImage
.dmg
.rpm
.deb
```

## 17. Instalar Hermes Desktop

Onde fazer: Windows

Executar o instalador `.exe`.

Se o Windows SmartScreen aparecer, conferir se o arquivo veio da página oficial de releases e clicar em:

```text
More info
Run anyway
```

---

# Parte 10 - Conectar Hermes Desktop no Hermes Agent do Docker

No Hermes Desktop, usar:

```text
Connect to Remote Hermes
```

Não usar:

```text
Get Started
```

O botão `Get Started` tenta instalar outro Hermes Agent local no Windows.

## 18. Dados de conexão

Server URL:

```text
http://127.0.0.1:8642
```

API Key:

```text
12345678
```

Se conectar, o Desktop pode mostrar:

```text
Connected to remote Hermes
```

Em modo remoto, algumas funções administrativas podem não aparecer no Desktop.

Usar assim:

```text
Dashboard = configuração completa
Workspace = interface web
Desktop = cliente remoto com limitações
```

---

# Parte 11 - Instalar Hermes local pelo Desktop

Esta parte é opcional.

Usar apenas se quiser que o Hermes Desktop instale um Hermes Agent local no Windows.

Isso cria outro ambiente, separado do Docker.

## 19. Pré-requisitos no Windows

Instalar:

```text
Git for Windows
Python 3.11
Node.js LTS
```

Testar no PowerShell:

```powershell
git --version
py -3.11 --version
node --version
npm --version
```

Se o `npm --version` falhar por política de execução, rodar:

```powershell
Set-ExecutionPolicy -Scope CurrentUser RemoteSigned
```

Confirmar com:

```text
S
```

Depois testar:

```powershell
npm --version
```

## 20. Python 3.11

Se veio Python 3.14, não tem problema.

Instalar Python 3.11 pelo Python Manager:

```powershell
py install 3.11
```

Testar:

```powershell
py -3.11 --version
```

---

# Parte 12 - Claw3D no Hermes Desktop

O Claw3D é opcional.

Ele é uma visualização 3D dos agentes.

Se o Hermes Desktop mostrar:

```text
Failed to run git: spawn git ENOENT
```

Instalar Git for Windows.

Se mostrar:

```text
Failed to run npm: spawn npm ENOENT
```

Instalar Node.js LTS e conferir:

```powershell
node --version
npm --version
where.exe npm
```

Esperado:

```text
C:\Program Files\nodejs\npm
C:\Program Files\nodejs\npm.cmd
```

Se o PowerShell enxerga `npm`, mas o Hermes Desktop continua dando `spawn npm ENOENT`, fechar totalmente o Hermes Desktop e abrir de novo.

Se continuar, reiniciar o Windows.

Se ainda continuar, provavelmente é limitação do instalador automático do Claw3D no Windows.

Nesse caso, instalar manualmente:

```powershell
cd $env:USERPROFILE
git clone https://github.com/iamlukethedev/Claw3D.git
cd Claw3D
npm install
npm run dev
```

Atenção: se o Claw3D usar a porta `3000`, pode conflitar com o Hermes Workspace.

---

# Parte 13 - Comandos úteis

## Ver containers

Onde rodar: Ubuntu/WSL

```bash
docker ps
```

## Ver logs de tudo

Onde rodar: Ubuntu/WSL

```bash
cd "$HOME/hermes-docker"
docker compose logs -f
```

## Ver logs do Agent

```bash
docker logs -f hermes-agent
```

## Ver logs do Workspace

```bash
docker logs -f hermes-workspace
```

## Parar tudo sem apagar dados

Onde rodar: Ubuntu/WSL

```bash
cd "$HOME/hermes-docker"
docker compose down
```

## Subir tudo de novo

Onde rodar: Ubuntu/WSL

```bash
cd "$HOME/hermes-docker"
docker compose up -d
```

## Reiniciar tudo

Onde rodar: Ubuntu/WSL

```bash
cd "$HOME/hermes-docker"
docker compose restart
```

## Atualizar imagens

Onde rodar: Ubuntu/WSL

```bash
cd "$HOME/hermes-docker"
docker compose pull
docker compose up -d
```

## Recriar apenas o Workspace

```bash
cd "$HOME/hermes-docker"
docker compose up -d --force-recreate hermes-workspace
```

## Entrar no chat do Hermes pelo terminal

```bash
docker exec -it hermes-agent /opt/hermes/.venv/bin/hermes chat
```

---

# Parte 14 - Depois de reiniciar o Windows

Abrir o Docker Desktop e esperar:

```text
Engine running
```

Abrir Ubuntu/WSL:

```powershell
wsl -d Ubuntu
```

Subir o Hermes:

```bash
cd "$HOME/hermes-docker"
docker compose up -d
```

Verificar:

```bash
docker ps
```

Abrir:

```text
Dashboard:
http://localhost:9119

Workspace:
http://localhost:3000
```

---

# Parte 15 - Fechar Docker Desktop

Para parar os containers sem apagar dados:

```bash
cd "$HOME/hermes-docker"
docker compose down
```

Depois, no Windows:

```text
Ícone da baleia perto do relógio
Botão direito
Quit Docker Desktop
```

---

# Parte 16 - Remover Hermes do Docker sem apagar dados persistentes

Use esta opção para remover os containers e a rede do Compose, mas manter o volume com dados do Hermes.

Onde rodar: Ubuntu/WSL

```bash
cd "$HOME/hermes-docker"
docker compose down
```

Opcional: remover as imagens baixadas.

```bash
docker rmi nousresearch/hermes-agent:latest ghcr.io/outsourc-e/hermes-workspace:latest
```

Verificar se o volume ainda existe:

```bash
docker volume ls | grep hermes
```

Neste modo, os dados persistentes continuam salvos no volume:

```text
hermes-docker_hermes-data
```

Para instalar de novo depois, basta voltar para a pasta e subir novamente:

```bash
cd "$HOME/hermes-docker"
docker compose pull
docker compose up -d
```

---

# Parte 17 - Remover Hermes do Docker apagando dados persistentes

Use esta opção para apagar tudo do ambiente Docker deste guia.

Atenção: isso remove containers, rede e volume persistente do Hermes.

Onde rodar: Ubuntu/WSL

```bash
cd "$HOME/hermes-docker"
docker compose down -v
```

Remover imagens, se quiser limpar também os downloads:

```bash
docker rmi nousresearch/hermes-agent:latest ghcr.io/outsourc-e/hermes-workspace:latest
```

Remover a pasta do projeto:

```bash
rm -rf "$HOME/hermes-docker"
```

Verificar se ainda ficou algum container:

```bash
docker ps -a | grep hermes
```

Verificar se ainda ficou algum volume:

```bash
docker volume ls | grep hermes
```

Se ainda aparecer o volume persistente, remover manualmente:

```bash
docker volume rm hermes-docker_hermes-data
```

Se o nome do volume for diferente, listar e copiar o nome correto:

```bash
docker volume ls
```

---

# Parte 18 - Remover Hermes Desktop do Windows

Onde fazer: Windows

Abrir:

```text
Configurações > Aplicativos > Aplicativos instalados
```

Procurar:

```text
Hermes Desktop
```

Clicar em:

```text
Desinstalar
```

Se o Desktop instalou Hermes Agent local pelo botão `Get Started`, pode ter criado arquivos adicionais no perfil do usuário.

Verificar estas pastas no Windows:

```text
C:\Users\SEU_USUARIO\.hermes
C:\Users\SEU_USUARIO\AppData\Local\Hermes
C:\Users\SEU_USUARIO\AppData\Roaming\Hermes
C:\Users\SEU_USUARIO\AppData\Local\Programs\Hermes Desktop
```

Apagar apenas se tiver certeza de que não precisa mais dos dados locais.

---

# Parte 19 - Remover Claw3D manual

Se o Claw3D foi instalado manualmente no PowerShell, remover a pasta clonada.

Onde rodar: PowerShell

```powershell
cd $env:USERPROFILE
Remove-Item -Recurse -Force .\Claw3D
```

Se o Claw3D foi instalado pelo Hermes Desktop, procurar dentro das pastas do Hermes Desktop ou do usuário.

Verificar:

```text
C:\Users\SEU_USUARIO\Claw3D
C:\Users\SEU_USUARIO\.hermes
C:\Users\SEU_USUARIO\AppData\Roaming\Hermes
C:\Users\SEU_USUARIO\AppData\Local\Hermes
```

---

# Parte 20 - Limpeza opcional do Docker Desktop

Use apenas se quiser limpar recursos não usados do Docker.

Atenção: pode remover imagens, containers parados, redes e cache não usados por outros projetos.

Onde rodar: Ubuntu/WSL

```bash
docker system prune
```

Para limpeza mais agressiva:

```bash
docker system prune -a
```

Para remover volumes não usados:

```bash
docker volume prune
```

Não use `docker volume prune` se tiver volumes importantes de outros projetos.

---

# URLs finais

Hermes Agent API:

```text
http://localhost:8642
```

Hermes Dashboard:

```text
http://localhost:9119
```

Hermes Workspace:

```text
http://localhost:3000
```

Hermes Desktop:

```text
Aplicativo instalado no Windows
```

---

# Fontes

Hermes Agent Docker:

```text
https://github.com/NousResearch/hermes-agent/blob/main/website/docs/user-guide/docker.md
https://github.com/NousResearch/hermes-agent/blob/main/docker-compose.yml
```

Hermes Workspace Docker:

```text
https://github.com/outsourc-e/hermes-workspace
https://github.com/outsourc-e/hermes-workspace/blob/main/docker-compose.yml
```

Hermes Desktop:

```text
https://github.com/fathah/hermes-desktop
https://github.com/fathah/hermes-desktop/releases
```

Claw3D:

```text
https://github.com/iamlukethedev/Claw3D
```
