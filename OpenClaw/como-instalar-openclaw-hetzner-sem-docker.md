# Como instalar o OpenClaw na Hetzner sem Docker

## 1. Acessar a VPS

```bash
ssh "root@IP_DA_VPS"
```

## 2. Atualizar o servidor

```bash
apt update
apt upgrade -y
```

## 3. Instalar dependências básicas

```bash
apt install -y git curl ca-certificates nano
```

## 4. Instalar Node.js

```bash
curl -fsSL "https://deb.nodesource.com/setup_22.x" | bash -
apt install -y nodejs
```

## 5. Conferir versões

```bash
node -v
npm -v
git --version
```

## 6. Clonar o OpenClaw

```bash
cd "/opt"
git clone "https://github.com/openclaw/openclaw.git"
cd "/opt/openclaw"
```

## 7. Instalar dependências do projeto

```bash
npm install
```

## 8. Criar arquivo de ambiente

```bash
cp ".env.example" ".env"
nano ".env"
```

## 9. Editar variáveis principais

```env
OPENCLAW_GATEWAY_PORT="18789"
OPENCLAW_GATEWAY_BIND="127.0.0.1"
OPENCLAW_CONFIG_DIR="/var/lib/openclaw"
OPENCLAW_WORKSPACE_DIR="/var/lib/openclaw/workspace"
OPENCLAW_GATEWAY_TOKEN="SEU_TOKEN_AQUI"
```

## 10. Criar pastas persistentes

```bash
mkdir -p "/var/lib/openclaw/workspace"
```

## 11. Testar execução manual

```bash
npm run dev
```

## 12. Criar serviço systemd

```bash
nano "/etc/systemd/system/openclaw.service"
```

```ini
[Unit]
Description=OpenClaw
After=network.target

[Service]
Type=simple
WorkingDirectory=/opt/openclaw
EnvironmentFile=/opt/openclaw/.env
ExecStart=/usr/bin/npm run dev
Restart=always
RestartSec=5
User=root

[Install]
WantedBy=multi-user.target
```

## 13. Ativar serviço

```bash
systemctl daemon-reload
systemctl enable openclaw
systemctl start openclaw
```

## 14. Ver status

```bash
systemctl status openclaw
```

## 15. Ver logs

```bash
journalctl -u openclaw -f
```

## 16. Acessar com túnel SSH

No computador local:

```bash
ssh -N -L "18789:127.0.0.1:18789" "root@IP_DA_VPS"
```

No navegador:

```text
http://127.0.0.1:18789
```

## 17. Comandos úteis

Reiniciar:

```bash
systemctl restart openclaw
```

Parar:

```bash
systemctl stop openclaw
```

Iniciar:

```bash
systemctl start openclaw
```

Ver logs recentes:

```bash
journalctl -u openclaw -n 100
```

## Observação importante

Não abrir a porta `"18789"` direto para a internet.

Usar túnel SSH, Tailscale ou Nginx com autenticação quando for expor acesso externo.
