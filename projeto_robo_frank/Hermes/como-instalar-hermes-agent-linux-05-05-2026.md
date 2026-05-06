# Como instalar o Hermes Agent no Linux sem Docker — versão simples

Este guia mostra apenas o caminho prático para instalar o Hermes Agent no Linux, configurar o modelo, habilitar a API local e fazer o gateway iniciar junto com o sistema.

> Observação importante: se o Hermes já criar um serviço `hermes-gateway.service` durante a instalação, mantenha o serviço criado por ele. Não misture esse serviço com outro modelo manual.

---

## 1. Atualizar o sistema

```bash
sudo apt update
sudo apt upgrade -y
sudo apt install -y curl git build-essential ca-certificates openssl
```

---

## 2. Instalar o Hermes Agent

```bash
curl -fsSL https://raw.githubusercontent.com/NousResearch/hermes-agent/main/scripts/install.sh | bash
```

Recarregue o terminal:

```bash
source ~/.bashrc
```

Teste:

```bash
hermes --version
```

Se não funcionar, feche e abra o terminal novamente.

---

## 3. Configurar o modelo

Rode:

```bash
hermes model
```

Escolha o provedor e preencha os dados pedidos.

Para Ollama local, normalmente use:

```text
API base URL: http://localhost:11434/v1
API key: ollama
Model: nome-do-modelo-instalado-no-ollama
```

Para ver os modelos do Ollama:

```bash
ollama list
```

Depois teste:

```bash
hermes
```

Digite uma mensagem simples, por exemplo:

```text
Olá, confirme que está funcionando.
```

---

## 4. Habilitar a API local do Hermes

Abra o arquivo:

```bash
nano ~/.hermes/.env
```

Gere uma chave forte em outro terminal:

```bash
openssl rand -hex 32
```

No arquivo `~/.hermes/.env`, adicione ou ajuste estas linhas:

```env
API_SERVER_ENABLED=true
API_SERVER_KEY=cole_a_chave_gerada_aqui
API_SERVER_HOST=127.0.0.1
API_SERVER_PORT=8642
```

Salve no nano:

```text
Ctrl+O
Enter
Ctrl+X
```

Mantenha `API_SERVER_HOST=127.0.0.1` para uso local. Isso evita expor o Hermes na rede.

---

## 5. Testar o gateway manualmente

Rode:

```bash
hermes gateway
```

Em outro terminal, teste:

```bash
curl http://127.0.0.1:8642/health
```

Resposta esperada:

```json
{"status":"ok"}
```

Teste também os modelos:

```bash
curl http://127.0.0.1:8642/v1/models \
  -H "Authorization: Bearer SUA_CHAVE_FORTE"
```

Troque `SUA_CHAVE_FORTE` pela chave configurada em `API_SERVER_KEY`.

---

## 6. Fazer o gateway iniciar com o Linux

Primeiro, veja se o instalador já criou um serviço:

```bash
ls ~/.config/systemd/user | grep hermes
```

Se aparecer `hermes-gateway.service`, abra para conferir:

```bash
nano ~/.config/systemd/user/hermes-gateway.service
```

Se o arquivo já tiver um `ExecStart` parecido com este, mantenha como está:

```ini
ExecStart=/home/SEU_USUARIO/.hermes/hermes-agent/venv/bin/python -m hermes_cli.main gateway run --replace
```

Esse é o serviço criado pelo próprio Hermes. Não troque por outro caminho.

Confira apenas se no final existe:

```ini
[Install]
WantedBy=default.target
```

Salve e saia:

```text
Ctrl+O
Enter
Ctrl+X
```

Ative o serviço:

```bash
systemctl --user daemon-reload
systemctl --user enable --now hermes-gateway.service
systemctl --user status hermes-gateway.service
```

O esperado é aparecer:

```text
active (running)
```

---

## 7. Se o serviço não existir

Use este passo apenas se o comando abaixo não encontrou nenhum serviço do Hermes:

```bash
ls ~/.config/systemd/user | grep hermes
```

Crie a pasta:

```bash
mkdir -p ~/.config/systemd/user
```

Descubra o caminho do Hermes:

```bash
which hermes
```

Crie o serviço:

```bash
nano ~/.config/systemd/user/hermes-gateway.service
```

Se `which hermes` retornou `/home/seu_usuario/.local/bin/hermes`, cole:

```ini
[Unit]
Description=Hermes Agent Gateway
After=network-online.target
Wants=network-online.target

[Service]
Type=simple
ExecStart=%h/.local/bin/hermes gateway
Restart=always
RestartSec=5
WorkingDirectory=%h
Environment=PATH=%h/.local/bin:/usr/local/bin:/usr/bin:/bin

[Install]
WantedBy=default.target
```

Salve:

```text
Ctrl+O
Enter
Ctrl+X
```

Ative:

```bash
systemctl --user daemon-reload
systemctl --user enable --now hermes-gateway.service
systemctl --user status hermes-gateway.service
```

---

## 8. Permitir iniciar mesmo sem abrir terminal

```bash
sudo loginctl enable-linger "$USER"
```

Verifique:

```bash
loginctl show-user "$USER" | grep Linger
```

Esperado:

```text
Linger=yes
```

---

## 9. Testar depois de reiniciar

Reinicie:

```bash
sudo reboot
```

Depois verifique:

```bash
systemctl --user status hermes-gateway.service
curl http://127.0.0.1:8642/health
```

Se aparecer `active (running)` e `{"status":"ok"}`, o Hermes está instalado, com API local habilitada e iniciando com o Linux.

---

## 10. Comandos úteis

Parar:

```bash
systemctl --user stop hermes-gateway.service
```

Reiniciar:

```bash
systemctl --user restart hermes-gateway.service
```

Ver status:

```bash
systemctl --user status hermes-gateway.service
```

Ver logs:

```bash
journalctl --user -u hermes-gateway.service -f
```

Desativar inicialização automática:

```bash
systemctl --user disable hermes-gateway.service
```

---

## Checklist final

```bash
hermes --version
hermes doctor
hermes
curl http://127.0.0.1:8642/health
systemctl --user status hermes-gateway.service
```

Está pronto quando:

- `hermes --version` funciona.
- `hermes` responde no terminal.
- `/health` retorna `{"status":"ok"}`.
- `systemctl --user status hermes-gateway.service` mostra `active (running)`.
