# Instalação do PicoClaw em VPS Hetzner sem Docker

## Objetivo

Instalar o PicoClaw diretamente na VPS Ubuntu da Hetzner, sem Docker.

Este documento usa o caminho de instalação puro:

```bash
GitHub -> build local -> binário -> configuração -> systemd
```

---

## 1. Acessar a VPS

No seu computador local, acesse a VPS por SSH:

```bash
ssh root@IP_DA_SUA_VPS
```

Atualize o sistema:

```bash
apt update && apt upgrade -y
```

Instale ferramentas básicas:

```bash
apt install -y git curl wget nano build-essential make
```

---

## 2. Instalar Go

O PicoClaw é feito em Go. Para compilar direto na VPS, instale o Go.

Verifique se já existe Go instalado:

```bash
go version
```

Se não existir ou estiver muito antigo, instale pelos pacotes do Ubuntu:

```bash
apt install -y golang-go
```

Confira novamente:

```bash
go version
```

---

## 3. Baixar o PicoClaw

Entre na pasta onde você costuma instalar projetos:

```bash
cd /opt
```

Clone o repositório oficial:

```bash
git clone https://github.com/sipeed/picoclaw.git
```

Entre na pasta:

```bash
cd /opt/picoclaw
```

Veja os arquivos:

```bash
ls
```

---

## 4. Instalar dependências do projeto

Dentro da pasta do PicoClaw:

```bash
make deps
```

---

## 5. Compilar o PicoClaw

Compile para a plataforma atual:

```bash
make build
```

Verifique se o binário foi criado:

```bash
ls build
```

---

## 6. Instalar o binário no PATH

Use o alvo oficial de instalação:

```bash
make install
```

Verifique se o comando ficou disponível:

```bash
which picoclaw
```

Confira a versão:

```bash
picoclaw --version
```

Se o comando não for encontrado, teste procurar o binário:

```bash
find /opt/picoclaw -type f -name "picoclaw*" 2>/dev/null
```

---

## 7. Criar a configuração inicial

Rode o onboarding:

```bash
picoclaw onboard
```

Depois verifique se a pasta de configuração foi criada:

```bash
ls ~/.picoclaw
```

Veja o arquivo de configuração:

```bash
ls ~/.picoclaw/config.json
```

Abra para editar:

```bash
nano ~/.picoclaw/config.json
```

Configure pelo menos um provedor de modelo.

Exemplo de pontos para revisar dentro do arquivo:

```text
providers
api_key
model
tools
telegram
discord
web
```

Salve no nano:

```text
CTRL + O
ENTER
CTRL + X
```

---

## 8. Testar o PicoClaw no terminal

Teste uma pergunta simples:

```bash
picoclaw agent -m "Responda apenas: PicoClaw funcionando."
```

Se responder corretamente, o binário e a configuração básica estão funcionando.

---

## 9. Rodar o gateway manualmente

Para iniciar o gateway em primeiro plano:

```bash
picoclaw gateway
```

Se estiver usando Telegram, Discord ou outro canal, este comando mantém o PicoClaw ouvindo as mensagens.

Para parar:

```text
CTRL + C
```

---

## 10. Criar serviço systemd

Para deixar o PicoClaw rodando mesmo depois de fechar o terminal, crie um serviço.

Crie o arquivo:

```bash
nano /etc/systemd/system/picoclaw.service
```

Cole:

```ini
[Unit]
Description=PicoClaw Gateway
After=network.target

[Service]
Type=simple
User=root
WorkingDirectory=/root
ExecStart=/usr/local/bin/picoclaw gateway
Restart=always
RestartSec=5
Environment=HOME=/root

[Install]
WantedBy=multi-user.target
```

Salve:

```text
CTRL + O
ENTER
CTRL + X
```

Recarregue o systemd:

```bash
systemctl daemon-reload
```

Ative o serviço:

```bash
systemctl enable picoclaw
```

Inicie:

```bash
systemctl start picoclaw
```

Veja o status:

```bash
systemctl status picoclaw
```

---

## 11. Ver logs

Ver logs em tempo real:

```bash
journalctl -u picoclaw -f
```

Ver últimos logs:

```bash
journalctl -u picoclaw -n 100 --no-pager
```

---

## 12. Reiniciar o PicoClaw

```bash
systemctl restart picoclaw
```

---

## 13. Parar o PicoClaw

```bash
systemctl stop picoclaw
```

---

## 14. Desativar da inicialização

```bash
systemctl disable picoclaw
```

---

## 15. Atualizar o PicoClaw

Entre na pasta do projeto:

```bash
cd /opt/picoclaw
```

Atualize o código:

```bash
git pull
```

Recompile:

```bash
make deps
make build
make install
```

Reinicie o serviço:

```bash
systemctl restart picoclaw
```

Confira o status:

```bash
systemctl status picoclaw
```

---

## 16. Checar portas abertas

Se o PicoClaw estiver rodando como gateway ou API, confira portas abertas:

```bash
ss -tulpn
```

Se usar firewall UFW, veja o status:

```bash
ufw status
```

---

## 17. Comandos úteis

Ver versão:

```bash
picoclaw --version
```

Rodar onboarding:

```bash
picoclaw onboard
```

Testar agente:

```bash
picoclaw agent -m "Teste rápido."
```

Rodar gateway:

```bash
picoclaw gateway
```

Ver serviço:

```bash
systemctl status picoclaw
```

Ver logs:

```bash
journalctl -u picoclaw -f
```

---

## 18. Remover PicoClaw

Parar serviço:

```bash
systemctl stop picoclaw
```

Desativar serviço:

```bash
systemctl disable picoclaw
```

Remover arquivo systemd:

```bash
rm /etc/systemd/system/picoclaw.service
```

Recarregar systemd:

```bash
systemctl daemon-reload
```

Remover binário:

```bash
rm -f /usr/local/bin/picoclaw
```

Remover projeto:

```bash
rm -rf /opt/picoclaw
```

Opcional: remover configuração do usuário root:

```bash
rm -rf /root/.picoclaw
```

---

## Observação

Este guia evita Docker de propósito.

A ideia é manter a VPS Hetzner no padrão de instalação pura:

```text
binário + config + systemd
```
