# Como instalar Hermes Agent na Hetzner para o Hermes TikTok Commerce Lab

## Objetivo

Instalar uma infraestrutura híbrida em uma VPS Ubuntu da Hetzner para o projeto **Hermes TikTok Commerce Lab**.

Título explicativo:

```text
Como usar Hermes Agent para vender no TikTok com IA
```

O objetivo técnico continua sendo preparar o Hermes Agent, Hermes Workspace, OpenSpec e serviços auxiliares na Hetzner.

O TikTok é o caso de uso final.

A infraestrutura continua sendo Hermes na Hetzner.

![[projeto.png]]

```text
Tailscale
Ollama
SearXNG em Docker
Hermes Agent sem Docker
Hermes Dashboard sem Docker
Hermes Workspace sem Docker
OpenSpec
Agentes criados no Hermes Workspace
```

## Arquitetura

```text
VPS Ubuntu Hetzner
|-- Tailscale
|-- Ollama
|-- Docker
|   `-- SearXNG
|-- Hermes Agent
|-- Hermes Dashboard
|-- Hermes Workspace
|-- OpenSpec
`-- Agentes criados no Workspace
```

## Portas usadas

```text
22     SSH
8080   SearXNG
8642   Hermes Gateway/API
9119   Hermes Dashboard
3000   Hermes Workspace
11434  Ollama
```

---

# 1. Acessar VPS

## 1.1. Entrar via SSH

```bash
ssh root@IP_PUBLICO_DA_VPS
```

---

# 2. Preparar Ubuntu

## 2.1. Atualizar sistema

```bash
apt update && apt upgrade -y
```

## 2.2. Instalar pacotes básicos

```bash
apt install -y curl git nano ufw ca-certificates gnupg build-essential unzip lsof net-tools
```

---

# 3. Instalar Tailscale

## 3.1. Instalar

```bash
curl -fsSL https://tailscale.com/install.sh | sh
```

## 3.2. Conectar VPS

```bash
tailscale up
```

## 3.3. Ver IP privado

```bash
tailscale ip -4
```

---

# 4. Configurar firewall

## 4.1. Permitir SSH

```bash
ufw allow OpenSSH
```

## 4.2. Bloquear portas públicas

```bash
ufw deny 3000/tcp
ufw deny 8080/tcp
ufw deny 8642/tcp
ufw deny 9119/tcp
ufw deny 11434/tcp
```

## 4.3. Ativar firewall

```bash
ufw enable
```

---

# 5. Instalar Ollama

## 5.1. Instalar

```bash
curl -fsSL https://ollama.com/install.sh | sh
```

## 5.2. Iniciar serviço

```bash
systemctl start ollama
```

## 5.3. Habilitar inicialização automática

```bash
systemctl enable ollama
```

## 5.4. Conferir versão

```bash
ollama --version
```

## 5.5. Baixar modelo

```bash
ollama pull gemma4:31b-cloud
```

## 5.6. Testar modelo

```bash
ollama run gemma4:31b-cloud
```

---

# 6. Instalar Docker para SearXNG

## 6.1. Instalar Docker

```bash
curl -fsSL https://get.docker.com | sh
```

## 6.2. Habilitar Docker

```bash
systemctl enable docker
```

```bash
systemctl start docker
```

## 6.3. Conferir Docker

```bash
docker --version
```

```bash
docker compose version
```

## 6.4. Criar pasta do SearXNG

```bash
mkdir -p ~/searxng/core-config
```

```bash
cd ~/searxng
```

Observação:

```text
O comando mkdir -p ~/searxng/core-config cria as duas pastas:
~/searxng
~/searxng/core-config
```

## 6.5. Baixar compose oficial atualizado

O repositório antigo `searxng/searxng-docker` foi substituído para novas instalações.

Use o compose atual do repositório oficial `searxng/searxng`.

```bash
curl -fsSL -O https://raw.githubusercontent.com/searxng/searxng/master/container/docker-compose.yml
```

```bash
curl -fsSL -O https://raw.githubusercontent.com/searxng/searxng/master/container/.env.example
```

## 6.6. Conferir se baixou certo

```bash
ls -la
```

```bash
head -n 10 docker-compose.yml
```

O esperado é aparecer algo parecido com:

```text
name: searxng

services:
  core:
```

Se aparecer `404` ou se o arquivo tiver somente poucos bytes, o download veio errado.

## 6.7. Criar arquivo .env

```bash
cp .env.example .env
```

```bash
nano .env
```

Para o teste inicial, pode salvar sem alterar nada.

Salvar:

```text
CTRL + O
ENTER
CTRL + X
```

## 6.8. Subir SearXNG

```bash
docker compose up -d
```

## 6.9. Conferir containers

```bash
docker compose ps
```

O esperado é aparecer algo como:

```text
searxng-core
searxng-valkey
```

## 6.10. Testar localmente

```bash
curl -I http://127.0.0.1:8080
```

## 6.11. Testar pelo navegador

Acesse usando o IP privado do Tailscale:

```text
http://IP_TAILSCALE_DA_VPS:8080
```

## 6.12. Logs do SearXNG

```bash
docker compose logs -f
```

Se quiser ver apenas o serviço principal:

```bash
docker compose logs -f core
```

## 6.13. Parar SearXNG

```bash
docker compose down
```

## 6.14. Atualizar SearXNG no futuro

```bash
cd ~/searxng
```

```bash
docker compose down
```

```bash
docker compose pull
```

```bash
docker compose up -d
```

## 6.15. Corrigir download quebrado

Se aparecer erro parecido com:

```text
non-string key at top level: 404
```

ou se o arquivo `docker-compose.yaml` tiver só 14 bytes, apague a pasta e baixe de novo:

```bash
cd ~
```

```bash
docker compose -f ~/searxng/docker-compose.yml down 2>/dev/null || true
```

```bash
rm -rf ~/searxng
```

```bash
mkdir -p ~/searxng/core-config
```

```bash
cd ~/searxng
```

```bash
curl -fsSL -O https://raw.githubusercontent.com/searxng/searxng/master/container/docker-compose.yml
```

```bash
curl -fsSL -O https://raw.githubusercontent.com/searxng/searxng/master/container/.env.example
```

```bash
cp .env.example .env
```

```bash
docker compose up -d
```

```bash
docker compose ps
```

---

# 7. Instalar Node.js e pnpm

## 7.1. Instalar Node.js 22

```bash
curl -fsSL https://deb.nodesource.com/setup_22.x | bash -
```

```bash
apt install -y nodejs
```

## 7.2. Instalar pnpm

```bash
npm install -g pnpm
```

---

# 8. Instalar Hermes Agent

## 8.1. Voltar para a pasta principal

```bash
cd ~
```

## 8.2. Instalar Hermes Agent pelo instalador oficial

O pacote antigo `@nousresearch/hermes-agent` no npm não deve mais ser usado para esta instalação.

Use o instalador oficial do repositório do Hermes Agent:

```bash
curl -fsSL https://raw.githubusercontent.com/NousResearch/hermes-agent/main/scripts/install.sh | bash
```

## 8.3. Recarregar shell

```bash
source ~/.bashrc
```

Se estiver usando Zsh:

```bash
source ~/.zshrc
```

## 8.4. Conferir instalação

```bash
hermes --version
```

Se o comando acima não funcionar, teste:

```bash
~/.local/bin/hermes --version
```

Se funcionar com `~/.local/bin/hermes`, adicione o caminho ao shell:

```bash
echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.bashrc
```

```bash
source ~/.bashrc
```

## 8.5. Rodar setup

```bash
hermes setup
```

## 8.6. Configurar modelo

Durante o setup, configure o provedor/modelo conforme o ambiente usado.

Para Ollama local ou Ollama Cloud compatível com endpoint local:

```text
Base URL:
http://127.0.0.1:11434/v1

Modelo:
gemma4:31b-cloud
```

Se o Hermes pedir formato com provedor, use:

```text
ollama/gemma4:31b-cloud
```

## 8.7. Diagnóstico

```bash
hermes doctor
```

## 8.8. Testar chat no terminal

```bash
hermes
```

Para sair, use:

```text
CTRL + D
```

---

# 9. Configurar Hermes Agent Gateway/API

## 9.1. Criar .env do Hermes Agent

```bash
nano ~/.hermes/.env
```

Cole:

```env
SEARXNG_URL=http://127.0.0.1:8080
API_SERVER_ENABLED=true
API_SERVER_HOST=0.0.0.0
API_SERVER_PORT=8642
API_SERVER_KEY=12345678
API_SERVER_CORS_ORIGINS=*
```

Salvar:

```text
CTRL + O
ENTER
CTRL + X
```

## 9.2. Explicação

```text
SEARXNG_URL
URL local do SearXNG.

API_SERVER_ENABLED
Ativa o Gateway/API do Hermes Agent.

API_SERVER_HOST
Host do Gateway/API.

API_SERVER_PORT
Porta usada pelo Gateway/API.

API_SERVER_KEY
Chave técnica da API do Hermes Agent.

API_SERVER_CORS_ORIGINS
Permite conexões externas ao Gateway/API.
```

## 9.3. Testar Gateway

```bash
hermes gateway run
```

Em outro terminal:

```bash
curl http://127.0.0.1:8642/health
```

Esperado:

```json
{"status":"ok","platform":"hermes-agent"}
```

Se o comando `hermes gateway run` não existir na versão instalada, confira a ajuda:

```bash
hermes gateway --help
```

E use o comando indicado pela própria versão instalada.

---

# 10. Criar serviço do Hermes Gateway (opcional)

Esta etapa é opcional.

Use esta etapa se quiser que o Hermes Gateway continue rodando depois de fechar o SSH e volte automaticamente após reboot da VPS.

## 10.1. Criar pasta

```bash
mkdir -p ~/.config/systemd/user
```

## 10.2. Criar serviço

```bash
nano ~/.config/systemd/user/hermes-gateway.service
```

Cole:

```ini
[Unit]
Description=Hermes Gateway
After=network.target

[Service]
Type=simple
WorkingDirectory=/root
Environment=PATH=/root/.local/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
ExecStart=/usr/bin/env hermes gateway run
Restart=always
RestartSec=5

[Install]
WantedBy=default.target
```

Salvar:

```text
CTRL + O
ENTER
CTRL + X
```

## 10.3. Ativar

```bash
systemctl --user daemon-reload
```

```bash
systemctl --user enable hermes-gateway
```

```bash
systemctl --user start hermes-gateway
```

```bash
loginctl enable-linger root
```

---

# 11. Configurar Hermes Dashboard

## 11.1. Conferir comando do Dashboard

```bash
hermes dashboard --help
```

## 11.2. Testar manualmente

```bash
hermes dashboard --host 0.0.0.0 --port 9119 --no-open --insecure
```

Se a versão instalada não aceitar alguma opção, rode o dashboard simples:

```bash
hermes dashboard
```

E depois confira a porta usada pela própria saída do terminal.

## 11.3. Criar serviço

```bash
nano /etc/systemd/system/hermes-dashboard.service
```

Cole:

```ini
[Unit]
Description=Hermes Dashboard
After=network.target

[Service]
Type=simple
User=root
WorkingDirectory=/root
Environment=PATH=/root/.local/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
ExecStart=/usr/bin/env hermes dashboard --host 0.0.0.0 --port 9119 --no-open --insecure
Restart=always
RestartSec=5

[Install]
WantedBy=multi-user.target
```

Salvar:

```text
CTRL + O
ENTER
CTRL + X
```

## 11.4. Ativar

```bash
systemctl daemon-reload
```

```bash
systemctl enable hermes-dashboard
```

```bash
systemctl start hermes-dashboard
```

---

# 12. Instalar Hermes Workspace

## 12.1. Clonar repositório

```bash
cd ~
```

```bash
git clone https://github.com/outsourc-e/hermes-workspace.git
```

```bash
cd ~/hermes-workspace
```

## 12.2. Instalar dependências

```bash
pnpm install
```

## 12.3. Autorizar builds do pnpm se aparecer o aviso

Se o `pnpm install` mostrar uma mensagem parecida com:

```text
Run "pnpm approve-builds" to pick which dependencies should be allowed to run scripts.
```

Execute:

```bash
pnpm approve-builds
```

Na tela interativa, selecione os pacotes indicados e aprove.

Pacotes comuns nessa etapa:

```text
electron
electron-winstaller
esbuild
unrs-resolver
```

Se aparecer apenas esses pacotes, você pode marcar todos e confirmar.

Se o comando informar que não há pacotes aguardando aprovação, siga para a próxima etapa.

## 12.4. Criar .env do Workspace

Se existir `.env.example`, copie para `.env`:

```bash
cp .env.example .env
```

Depois edite:

```bash
nano .env
```

Cole ou ajuste estas variáveis:

```env
HERMES_API_URL=http://IP_TAILSCALE_DA_VPS:8642
HERMES_DASHBOARD_URL=http://IP_TAILSCALE_DA_VPS:9119
HERMES_API_TOKEN=12345678
HERMES_PASSWORD=12345678
COOKIE_SECURE=0
HOST=0.0.0.0
PORT=3000
```

Salvar:

```text
CTRL + O
ENTER
CTRL + X
```

## 12.5. Explicação

```text
HERMES_API_URL
URL do Hermes Gateway/API.

HERMES_DASHBOARD_URL
URL do Hermes Dashboard.

HERMES_API_TOKEN
Token usado pelo Workspace.
Deve ter o mesmo valor de API_SERVER_KEY.

HERMES_PASSWORD
Senha de login do Workspace.

COOKIE_SECURE=0
Permite login sem HTTPS.

HOST
Host do Workspace.

PORT
Porta do Workspace.
```

## 12.6. Ajustar IP automaticamente (opcional caso não tenha alterado o tailscale)

```bash
TAILSCALE_IP="$(tailscale ip -4 | head -n1)"
```

```bash
sed -i "s|IP_TAILSCALE_DA_VPS|$TAILSCALE_IP|g" ~/hermes-workspace/.env
```

## 12.7. Conferir .env sem mostrar senha no vídeo

```bash
grep -E "HERMES_API_URL|HERMES_DASHBOARD_URL|COOKIE_SECURE|HOST|PORT" ~/hermes-workspace/.env
```

---

# 13. Testar Hermes Workspace

## 13.1. Subir manualmente

```bash
cd ~/hermes-workspace
```

```bash
pnpm dev --host 0.0.0.0
```

Se a versão instalada não aceitar `--host`, use:

```bash
pnpm dev
```

## 13.2. Acessar

```text
http://IP_TAILSCALE_DA_VPS:3000
```

Senha:

```text
12345678
```

---

# 14. Criar serviço do Hermes Workspace (opcional)

Esta etapa é opcional.

Use esta etapa se quiser que o Hermes Workspace continue rodando depois de fechar o SSH e volte automaticamente após reboot da VPS.

## 14.1. Criar serviço

```bash
nano ~/.config/systemd/user/hermes-workspace.service
```

Cole:

```ini
[Unit]
Description=Hermes Workspace
After=network.target hermes-gateway.service

[Service]
Type=simple
WorkingDirectory=/root/hermes-workspace
Environment=PATH=/root/.local/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
ExecStart=/usr/bin/env pnpm dev --host 0.0.0.0
Restart=always
RestartSec=5

[Install]
WantedBy=default.target
```

Salvar:

```text
CTRL + O
ENTER
CTRL + X
```

## 14.2. Ativar

```bash
systemctl --user daemon-reload
```

```bash
systemctl --user enable hermes-workspace
```

```bash
systemctl --user start hermes-workspace
```

---

# 15. Regra de autenticação

```text
API_SERVER_KEY e HERMES_API_TOKEN devem ter o mesmo valor.

HERMES_PASSWORD é a senha usada para login no Workspace.

API_SERVER_KEY não é senha de login.
```

---

# 16. URLs finais

## SearXNG

```text
http://IP_TAILSCALE_DA_VPS:8080
```

## Hermes Gateway/API

```text
http://IP_TAILSCALE_DA_VPS:8642/health
```

## Hermes Dashboard

```text
http://IP_TAILSCALE_DA_VPS:9119
```

## Hermes Workspace

```text
http://IP_TAILSCALE_DA_VPS:3000
```

---

# 17. Comandos úteis

## 17.1. Ver containers do SearXNG

```bash
cd ~/searxng
docker compose ps
```

## 17.2. Logs do SearXNG

```bash
cd ~/searxng
docker compose logs -f
```

Se quiser ver apenas o serviço principal:

```bash
cd ~/searxng
docker compose logs -f core
```

## 17.3. Status do Hermes Gateway

```bash
systemctl --user status hermes-gateway
```

## 17.4. Status do Hermes Dashboard

```bash
systemctl status hermes-dashboard
```

## 17.5. Status do Hermes Workspace

```bash
systemctl --user status hermes-workspace
```

## 17.6. Logs do Hermes Gateway

```bash
journalctl --user -u hermes-gateway -f
```

## 17.7. Logs do Hermes Dashboard

```bash
journalctl -u hermes-dashboard -f
```

## 17.8. Logs do Hermes Workspace

```bash
journalctl --user -u hermes-workspace -f
```

---

# 18. Instalar OpenSpec

Esta etapa é opcional, mas recomendada para organizar o projeto antes da execução dos agentes.

Use esta etapa se quiser adicionar uma camada de especificação antes das tarefas do Hermes.

```text
Hermes Workspace
Interface visual para criar e usar agentes.

OpenSpec
Estrutura de planejamento do projeto antes da execução.
```

## 18.1. Conferir versão do Node.js

```bash
node --version
```

Esperado:

```text
Node.js 20.19.0 ou superior
```

Nesta instalação, o Node.js 22 já foi instalado anteriormente.

## 18.2. Instalar ou atualizar OpenSpec

```bash
npm install -g @fission-ai/openspec@latest
```

## 18.3. Conferir instalação

```bash
openspec --version
```

## 18.4. Criar pasta do projeto

```bash
mkdir -p ~/projetos/hermes-tiktok-commerce-lab
```

```bash
cd ~/projetos/hermes-tiktok-commerce-lab
```

## 18.5. Iniciar OpenSpec no projeto

```bash
openspec init
```

Durante a configuração, escolha a opção de assistente compatível disponível.

Se o Hermes não aparecer como opção direta, use a opção genérica ou a opção que gere instruções compartilhadas para agentes.

## 18.6. Atualizar instruções do OpenSpec

```bash
openspec update
```

Use este comando dentro do projeto quando quiser regenerar instruções e comandos do OpenSpec.

## 18.7. Conferir estrutura criada

```bash
ls -la
```

```bash
find . -maxdepth 3 -type f | sort
```

A estrutura pode variar conforme a versão, mas normalmente inclui arquivos de instrução e uma pasta `openspec`.

## 18.8. Prompt para criar proposta OpenSpec

Use este prompt no Codex ou no assistente conectado ao projeto:

```text
/opsx:propose Criar a estrutura profissional do projeto Hermes TikTok Commerce Lab, com documentação organizada, exemplos de configuração, scripts auxiliares, segurança, operação, agentes do Hermes Workspace, fluxo de trabalho com OpenSpec e caso de uso final em afiliados no TikTok.
```

O projeto deve mostrar como usar Hermes Agent, Hermes Workspace, OpenSpec e agentes de IA para organizar uma operação de afiliados no TikTok.

A infraestrutura continua sendo:

```text
VPS Ubuntu Hetzner
Tailscale
Firewall
Ollama / Ollama Cloud
Docker apenas para SearXNG
Hermes Agent sem Docker
Hermes Gateway/API
Hermes Dashboard sem Docker
Hermes Workspace sem Docker
OpenSpec
Agentes criados no Hermes Workspace
```

O fluxo inicial é manual e revisado por humano:

```text
Hermes organiza pesquisa, roteiro, calendário, tarefas, revisão e documentação.
Humano revisa.
Humano produz ou finaliza o criativo na ferramenta escolhida.
Humano aprova antes de publicar.
```

Não afirmar que existe integração automática com TikTok, PipClip, Canva, CapCut ou ComfyUI se ela não estiver implementada.

## 18.9. Revisar antes de aplicar

Antes de aplicar, confira:

```text
1. O escopo está correto?
2. O Hermes Agent está sem Docker?
3. O Docker está sendo usado apenas para SearXNG?
4. O Tailscale aparece no começo?
5. As portas estão corretas?
6. O TikTok aparece como caso de uso final, não como infraestrutura?
7. A documentação separa instalação, segurança, operação, agentes e ferramentas visuais?
8. Não há senhas reais?
9. Não há tokens reais?
10. Não há IP sensível?
11. Não há promessa de vendas, renda ou comissão?
12. Não há automação de publicação sem revisão humana?
13. PipClip aparece como ferramenta opcional, sem integração automática inventada?
14. ComfyUI aparece apenas como opção avançada para quem tem GPU?
15. A execução crítica exige aprovação humana?
```

## 18.10. Aplicar proposta depois da revisão

```text
/opsx:apply
```

## 18.11. Verificar implementação

```text
/opsx:verify
```

Se a versão/perfil do OpenSpec não tiver `/opsx:verify`, use o fluxo básico e peça ao agente uma revisão manual comparando a implementação com a proposta.

## 18.12. Arquivar quando concluir

```text
/opsx:archive
```

## 18.13. Observação importante

```text
O OpenSpec não substitui a criação visual dos agentes no Hermes Workspace.

Use o Workspace para criar os agentes.
Use o OpenSpec para organizar a missão, o plano, as etapas e os critérios antes da execução.

Ordem recomendada:
1. Criar projeto
2. Inicializar OpenSpec
3. Criar proposta
4. Revisar proposta
5. Criar agentes no Workspace
6. Mandar o CEO / Orquestrador ler o OpenSpec
7. Executar por fases
```

---

# 19. Exemplo de agentes para o Hermes TikTok Commerce Lab

Crie os agentes no Hermes Workspace depois de inicializar e revisar o OpenSpec.

Use como referência o arquivo atualizado de agentes:

```text
configuracao_agentes_hermes_tiktok_commerce_lab_navegador.md
```

Agentes previstos:

```text
CEO / Orquestrador
Pesquisador de Produtos Afiliados
Pesquisador de Tendências TikTok
Estrategista de Conteúdo Afiliado
Copywriter de Vídeos Curtos
Social Media TikTok
Designer de Campanha
Revisor de Promessas
Documentador Técnico
Kanban Manager
```

## Prompt inicial para o CEO / Orquestrador

```text
Você é o CEO / Orquestrador do projeto Hermes TikTok Commerce Lab.

Antes de delegar qualquer tarefa, leia o projeto OpenSpec em:

~/projetos/hermes-tiktok-commerce-lab

Sua função é coordenar os agentes, dividir tarefas, controlar escopo, pedir aprovação humana quando necessário e garantir que toda execução siga a proposta aprovada no OpenSpec.

O objetivo do projeto é demonstrar como usar Hermes Agent, Hermes Workspace, OpenSpec e agentes de IA para organizar uma operação de afiliados no TikTok.

A operação envolve pesquisa de produtos afiliados, tendências de TikTok, roteiros curtos, calendário de conteúdo, direção visual, revisão de promessas, Kanban e documentação.

Ferramentas opcionais de criação visual podem incluir Canva, CapCut, PipClip e ComfyUI.

Essas ferramentas não são obrigatórias e não devem ser tratadas como integração automática.

O projeto também pode usar navegador controlado para pesquisa assistida em páginas públicas ou páginas abertas pela pessoa humana, respeitando as regras da plataforma.

Não prometa vendas, renda ou comissão garantida.
Não prometa renda.
Não publique nada sem revisão humana.
Não improvise fora do escopo aprovado.

Antes de executar qualquer ação:
1. apresente seu entendimento do projeto
2. liste os agentes disponíveis
3. proponha a divisão de tarefas
4. indique a primeira tarefa segura
5. indique riscos
6. peça aprovação humana antes de executar

Não execute comandos ainda.
```

---

# 20. Ferramentas opcionais de criação visual

O projeto pode usar ferramentas visuais depois que os agentes entregarem briefing, roteiro, direção visual e revisão.

Essas ferramentas são opcionais.

```text
Canva / CapCut
Uso manual para edição, cortes, legendas, montagem e acabamento.

PipClip
Ferramenta opcional para criação rápida de criativos com IA, vídeos de produto, avatares, animações, variações visuais e conteúdos curtos para TikTok, Reels e Shorts.

ComfyUI
Alternativa avançada para usuários com máquina local e GPU adequada.
Não é obrigatório.
Não será demonstrado como instalação completa neste momento.
```

Regra:

```text
O Hermes não substitui essas ferramentas.
O Hermes organiza planejamento, pesquisa, roteiro, calendário, tarefas, revisão e documentação.
A produção visual é feita depois, em fluxo manual revisado por humano.
Nenhum criativo deve ser publicado sem revisão humana.
```

---

# 21. Navegador controlado

O navegador controlado pode apoiar pesquisa assistida em páginas públicas ou páginas abertas pela pessoa humana.

Uso permitido no projeto:

```text
TikTok Creative Center
TikTok Creative Center - Top Products
TikTok Creative Center - Trends
TikTok Search
TikTok Shop / Seller Center Brasil, quando disponível
SearXNG local como validação externa
```

Limites:

```text
Não burlar login.
Não contornar captcha.
Não fazer scraping agressivo.
Não publicar automaticamente.
Não enviar mensagem automática.
Não seguir pessoas automaticamente.
Não coletar dados privados.
Não violar regras da plataforma.
```

Os links oficiais e fontes permitidas devem ficar principalmente no OpenSpec.

---

# 22. Notas de atualização desta versão

```text
SearXNG
O link antigo searxng/searxng-docker foi removido.
Agora o compose vem de searxng/searxng/master/container/docker-compose.yml.

Hermes Agent
O comando npm install -g @nousresearch/hermes-agent foi removido.
Agora a instalação usa o script oficial:
curl -fsSL https://raw.githubusercontent.com/NousResearch/hermes-agent/main/scripts/install.sh | bash

Hermes Workspace
A documentação foi ajustada para copiar .env.example, configurar HERMES_API_URL e HERMES_DASHBOARD_URL, e usar o IP do Tailscale.

OpenSpec
A seção foi ajustada para o projeto Hermes TikTok Commerce Lab e para o fluxo /opsx:propose, /opsx:apply, /opsx:verify e /opsx:archive.

afiliados no TikTok
O TikTok é o caso de uso final.
O projeto não promete vendas, renda ou comissão garantida, não ensina spam e não automatiza publicação sem revisão humana.

Ferramentas visuais
Canva, CapCut, PipClip e ComfyUI aparecem como opções manuais ou avançadas para produção visual depois da revisão dos agentes.
```
---

# Observação importante sobre VPS fora do Brasil

Esta instalação usa uma VPS Hetzner fora do Brasil.

Durante o teste real do Hermes TikTok Commerce Lab, foi identificado que alguns sites de marketplace, redes sociais e páginas de produtos podem bloquear ou limitar acessos vindos de IPs de datacenter ou IPs estrangeiros.

Isso pode afetar principalmente:

```text
Shopee Brasil
TikTok
TikTok Creative Center
TikTok Shop / Seller Center Brasil
páginas públicas de produtos com proteção antifraude
```

## O que funcionou bem na VPS

```text
Hermes Agent
Hermes Gateway
Hermes Dashboard
Hermes Workspace
Kanban
OpenSpec
SearXNG
workers via CLI
organização do fluxo operacional
documentação do projeto
```

## O que pode falhar na VPS

```text
busca direta de produtos em sites brasileiros
abertura de páginas com proteção regional
acesso a páginas que exigem login
acesso bloqueado por captcha
validação de rankings em páginas que rejeitam IP de datacenter
navegação remota como se fosse usuário local brasileiro
```

## Decisão adotada no projeto

O projeto passa a considerar a VPS como ambiente principal para:

```text
infraestrutura
orquestração
Kanban
execução dos agentes
controle operacional
documentação
```

E passa a considerar a pesquisa de produtos como fluxo:

```text
humano assistido
```

Nesse fluxo, a pessoa humana pode enviar manualmente:

```text
prints
imagens locais
nomes de produtos
links
preços observados
categorias
evidências visuais
observações sobre demanda
```

Os agentes devem analisar o material recebido, organizar a informação, registrar riscos e manter o Kanban atualizado.

## Regra de segurança

```text
Não burlar bloqueio.
Não contornar captcha.
Não fazer scraping agressivo.
Não violar regras da plataforma.
Não prometer automação total quando a plataforma bloqueia acesso.
```

## Encaminhamento para o próximo teste

Como melhoria complementar, pode ser feita uma instalação local usando nuvem para o modelo, com foco em:

```text
melhorar o acesso às páginas brasileiras
usar navegador local
melhorar os SOUL.md dos workers
verificar por que alguns agentes falharam durante o teste
ajustar instruções dos workers para o fluxo humano assistido
```

