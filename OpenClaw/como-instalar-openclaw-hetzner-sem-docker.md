# Como instalar o OpenClaw na Hetzner sem Docker usando o modo Linux full

Instalação do OpenClaw em uma VPS Linux Ubuntu, sem Docker, usando o fluxo oficial atual do OpenClaw: instalador Linux, `openclaw onboard`, modo `Advanced` e daemon gerenciado pelo próprio OpenClaw.

## Base oficial usada

- Instalação Linux/macOS/WSL2: `https://docs.openclaw.ai/install`
- Onboarding CLI: `https://docs.openclaw.ai/start/wizard`
- Atualização: `https://docs.openclaw.ai/install/updating`
- Releases: `https://github.com/openclaw/openclaw/releases/latest`

## O que este guia faz

- Atualiza a VPS Ubuntu.
- Instala dependências básicas.
- Instala o OpenClaw pelo instalador oficial.
- Roda o `openclaw onboard` em modo completo.
- Instala o daemon pelo próprio OpenClaw.
- Testa Gateway, dashboard, health check e versão.
- Inclui comandos de atualização e manutenção.

## O que este guia não faz

- Não usa Docker.
- Não clona o repositório manualmente.
- Não cria serviço `systemd` manual.
- Não roda `npm run dev` em produção.
- Não abre a porta do Gateway direto para a internet.

## 1. Acessar a VPS

No seu computador local:

```bash
ssh "root@IP_DA_VPS"
```

## 2. Atualizar o Ubuntu

Na VPS:

```bash
apt update
apt upgrade -y
```

## 3. Instalar dependências básicas

```bash
apt install -y curl git ca-certificates nano unzip build-essential
```

## 4. Instalar o OpenClaw pelo instalador oficial

```bash
curl -fsSL "https://openclaw.ai/install.sh" | bash
```

O instalador oficial detecta o sistema, instala Node quando necessário, instala o OpenClaw e inicia o onboarding.

## 5. Recarregar o terminal se o comando não aparecer

Se o comando `openclaw` não for encontrado depois da instalação:

```bash
source "$HOME/.bashrc"
```

Teste novamente:

```bash
openclaw --version
```

Se ainda não aparecer, confira o caminho do npm global:

```bash
node -v
npm prefix -g
echo "$PATH"
```

## 6. Conferir a versão instalada

```bash
openclaw --version
```

Ver a versão mais recente publicada no npm:

```bash
npm view openclaw version
```

Ver a release mais recente no GitHub:

```bash
openclaw update status --json
```

## 7. Rodar o onboard completo

Use o onboard interativo:

```bash
openclaw onboard
```

Quando aparecer a escolha entre `QuickStart` e `Advanced`, escolha:

```text
Advanced
```

## 8. Configuração recomendada no modo Advanced

Durante o `openclaw onboard`, configure com foco em instalação completa:

```text
Mode: Local Gateway
Workspace: ~/.openclaw/workspace
Gateway port: 18789
Gateway bind: 127.0.0.1
Gateway auth: Token
Tailscale exposure: Off
Daemon: Install
Skills: Install recommended skills
Health check: Yes
```

## 9. Instalar daemon pelo OpenClaw

Se o onboard não instalar o daemon durante o fluxo interativo, rode:

```bash
openclaw onboard --install-daemon
```

Também é possível instalar/reinstalar o Gateway gerenciado:

```bash
openclaw gateway install
```

## 10. Testar o OpenClaw

```bash
openclaw doctor
```

```bash
openclaw gateway status
```

```bash
openclaw health
```

Resultado esperado:

```text
OpenClaw instalado, Gateway configurado e health check sem erro crítico.
```

## 11. Abrir o dashboard

Na VPS:

```bash
openclaw dashboard
```

Se estiver acessando de fora da VPS, use túnel SSH no seu computador local:

```bash
ssh -N -L "18789:127.0.0.1:18789" "root@IP_DA_VPS"
```

Depois abra no navegador local:

```text
http://127.0.0.1:18789
```

## 12. Configurar depois do onboard

Reabrir configuração geral:

```bash
openclaw configure
```

Configurar ferramentas de busca web:

```bash
openclaw configure --section web
```

Adicionar outro agente:

```bash
openclaw agents add "NOME_DO_AGENTE"
```

## 13. Reiniciar o Gateway

```bash
openclaw gateway restart
```

## 14. Parar o Gateway

```bash
openclaw gateway stop
```

## 15. Iniciar o Gateway

```bash
openclaw gateway start
```

## 16. Ver status profundo

```bash
openclaw gateway status --deep --json
```

## 17. Atualizar o OpenClaw

O comando recomendado pela documentação oficial é:

```bash
openclaw update
```

Depois rode:

```bash
openclaw doctor
openclaw gateway restart
openclaw health
```

## 18. Testar atualização antes de aplicar

```bash
openclaw update --dry-run
```

## 19. Voltar para canal estável

```bash
openclaw update --channel stable
```

## 20. Usar canal de desenvolvimento

Use somente se quiser acompanhar o `main` do GitHub:

```bash
openclaw update --channel dev
```

Antes de trocar, simule:

```bash
openclaw update --channel dev --dry-run
```

## 21. Recuperar instalação com npm se necessário

Use apenas se o instalador ou o updater falhar.

```bash
openclaw gateway stop
npm install -g "openclaw@latest"
openclaw gateway install --force
openclaw gateway restart
openclaw doctor
openclaw health
```

## 22. Reinstalar pelo instalador oficial sem refazer onboard

```bash
curl -fsSL "https://openclaw.ai/install.sh" | bash -s -- --no-onboard
```

## 23. Forçar instalação via npm pelo instalador oficial

```bash
curl -fsSL "https://openclaw.ai/install.sh" | bash -s -- --install-method npm
```

## 24. Instalar versão específica

Troque `VERSAO_AQUI` pela versão desejada.

```bash
curl -fsSL "https://openclaw.ai/install.sh" | bash -s -- --install-method npm --version "VERSAO_AQUI"
```

## 25. Conferência final

```bash
openclaw --version
openclaw doctor
openclaw gateway status
openclaw health
```

## 26. Segurança mínima na VPS

Não exponha a porta `18789` diretamente para a internet.

Use uma destas opções:

```text
Túnel SSH
Tailscale
Nginx com autenticação
VPN
```

Para uso simples e seguro, prefira túnel SSH:

```bash
ssh -N -L "18789:127.0.0.1:18789" "root@IP_DA_VPS"
```

## 27. Comandos principais

```bash
openclaw --version
openclaw onboard
openclaw onboard --install-daemon
openclaw dashboard
openclaw configure
openclaw configure --section web
openclaw agents add "NOME_DO_AGENTE"
openclaw doctor
openclaw health
openclaw gateway status
openclaw gateway status --deep --json
openclaw gateway start
openclaw gateway stop
openclaw gateway restart
openclaw update
openclaw update --dry-run
openclaw update status --json
```

## Resultado esperado

Ao final, a VPS deve ter:

```text
OpenClaw instalado sem Docker.
CLI openclaw funcionando.
Onboarding completo em modo Advanced.
Gateway local na porta 18789.
Daemon instalado pelo próprio OpenClaw.
Dashboard acessível via túnel SSH.
Doctor e health check funcionando.
```
