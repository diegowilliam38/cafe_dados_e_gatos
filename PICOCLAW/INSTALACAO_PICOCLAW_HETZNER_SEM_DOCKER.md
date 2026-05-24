# Como instalar PicoClaw em VPS Hetzner sem Docker

## Objetivo

Instalar o PicoClaw diretamente em uma VPS Ubuntu da Hetzner, sem Docker.

Fluxo usado:

```text
VPS Ubuntu -> Go 1.25.10 -> build local -> onboard -> config.json -> Ollama -> WebUI Launcher -> Gateway
```

---

## 1. Acessar a VPS

```bash
ssh root@"IP_DA_SUA_VPS"
```

```bash
apt update && apt upgrade -y
```

```bash
apt install -y git curl wget nano build-essential make
```

---

## 2. Instalar Go 1.25.10

```bash
rm -rf "/usr/local/go"
```

```bash
cd "/tmp"

wget "https://go.dev/dl/go1.25.10.linux-amd64.tar.gz"
```

```bash
tar -C "/usr/local" -xzf "go1.25.10.linux-amd64.tar.gz"
```

```bash
echo 'export PATH=/usr/local/go/bin:$PATH' >> "~/.bashrc"

source "~/.bashrc"
```

```bash
go version
which go
```

Resultado esperado:

```text
go version go1.25.10 linux/amd64
/usr/local/go/bin/go
```

Se ainda aparecer Go antigo:

```bash
export PATH="/usr/local/go/bin:$PATH"

go version
which go
```

---

## 3. Baixar o PicoClaw

Se já existir uma instalação anterior e quiser começar limpo:

```bash
rm -rf "/opt/picoclaw"
```

```bash
cd "/opt"

git clone "https://github.com/sipeed/picoclaw.git"

cd "/opt/picoclaw"

ls
```

---

## 4. Instalar dependências

```bash
cd "/opt/picoclaw"

make deps
```

---

## 5. Compilar o PicoClaw

```bash
cd "/opt/picoclaw"

make build
```

```bash
find "/opt/picoclaw/build" -type f -name "picoclaw*" 2>/dev/null
```

No teste, o binário principal foi gerado como:

```text
/opt/picoclaw/build/picoclaw-linux-amd64
```

---

## 6. Instalar o binário no PATH

```bash
cp "/opt/picoclaw/build/picoclaw-linux-amd64" "/usr/local/bin/picoclaw"

chmod +x "/usr/local/bin/picoclaw"

which picoclaw

picoclaw --help
```

Observação: nesta build, este comando não existe:

```bash
picoclaw --version
```

Use:

```bash
picoclaw --help
```

---

## 7. Gerar a configuração inicial

O arquivo de configuração é gerado pelo próprio PicoClaw.

```bash
picoclaw onboard
```

Confira:

```bash
ls "/root/.picoclaw"

ls "/root/.picoclaw/config.json"
```

Abra:

```bash
nano "/root/.picoclaw/config.json"
```

---

## 8. Configurar Ollama no config.json

Confirme se o Ollama responde:

```bash
curl "http://127.0.0.1:11434/api/tags"
```

Veja os modelos disponíveis no Ollama:

```bash
ollama list
```

Abra a configuração:

```bash
nano "/root/.picoclaw/config.json"
```

Procure por `model_list`:

```text
CTRL + W
model_list
ENTER
```

No começo do arquivo, em:

```json
"agents": {
  "defaults": {
```

configure o provider e o modelo padrão.

Exemplo usado no teste:

```json
"provider": "ollama",
"model_name": "gemma4:31b-cloud"
```

Depois, em `model_list`, cadastre o mesmo `model_name`:

```json
{
  "model_name": "gemma4:31b-cloud",
  "provider": "ollama",
  "model": "ollama/gemma4:31b-cloud",
  "api_base": "http://127.0.0.1:11434/v1"
}
```

Pontos importantes:

```text
agents.defaults.model_name precisa bater exatamente com model_list[].model_name.
Para Ollama local, use http://127.0.0.1:11434/v1.
Não use https no Ollama local.
O campo model precisa ter o prefixo ollama/.
```

Salvar no nano:

```text
CTRL + O
ENTER
CTRL + X
```

Teste:

```bash
picoclaw agent -m "Oi, diga olá para meus amigos do Café com Dados e Gatos."
```

---

## 9. Usar o modo interativo

```bash
picoclaw agent
```

Para sair:

```text
CTRL + C
```

---

## 10. Compilar o WebUI Launcher

O WebUI Launcher precisa ser compilado separadamente.

```bash
cd "/opt/picoclaw"

make build-launcher
```

Verifique se foi gerado:

```bash
find "/opt/picoclaw" -type f -name "*launcher*" 2>/dev/null
```

No teste, o launcher foi gerado como:

```text
/opt/picoclaw/build/picoclaw-launcher
```

Instale no PATH:

```bash
cp "/opt/picoclaw/build/picoclaw-launcher" "/usr/local/bin/picoclaw-launcher"

chmod +x "/usr/local/bin/picoclaw-launcher"

which picoclaw-launcher
```

---

## 11. Subir a interface WebUI

Para VPS, VM ou Tailscale:

```bash
picoclaw-launcher -public
```

Abra no navegador:

```text
http://IP_DA_VPS:18800
```

Ou via Tailscale:

```text
http://IP_TAILSCALE:18800
```

Conferir porta:

```bash
ss -tulpn | grep "18800"
```

---

## 12. Subir o Gateway

```bash
picoclaw gateway
```

Para deixar rodando em segundo plano:

```bash
nohup picoclaw gateway > "/root/picoclaw-gateway.log" 2>&1 &
```

Ver logs:

```bash
tail -f "/root/picoclaw-gateway.log"
```

Ver processo:

```bash
ps aux | grep "picoclaw"
```

---

## 13. Atualizar PicoClaw depois

```bash
cd "/opt/picoclaw"

git pull

make deps

make build

make build-launcher

cp "/opt/picoclaw/build/picoclaw-linux-amd64" "/usr/local/bin/picoclaw"

chmod +x "/usr/local/bin/picoclaw"

cp "/opt/picoclaw/build/picoclaw-launcher" "/usr/local/bin/picoclaw-launcher"

chmod +x "/usr/local/bin/picoclaw-launcher"
```

---

# Como corrigir erros comuns

## Erro: Go antigo

```text
go.mod requires go >= 1.25.10
running go 1.22.2
```

Correção:

```bash
rm -rf "/usr/local/go"

cd "/tmp"

wget "https://go.dev/dl/go1.25.10.linux-amd64.tar.gz"

tar -C "/usr/local" -xzf "go1.25.10.linux-amd64.tar.gz"

export PATH="/usr/local/go/bin:$PATH"

go version
which go
```

---

## Erro: pasta já existe

```text
fatal: destination path 'picoclaw' already exists and is not an empty directory.
```

Correção:

```bash
rm -rf "/opt/picoclaw"

cd "/opt"

git clone "https://github.com/sipeed/picoclaw.git"

cd "/opt/picoclaw"
```

---

## Erro: picoclaw --version não existe

```text
unknown flag: --version
```

Use:

```bash
picoclaw --help
```

---

## Erro: model não encontrado

```text
model "NOME_DO_MODELO" not found in model_list
```

Causa:

```text
agents.defaults.model_name não existe dentro de model_list.
```

Correção:

```json
"model_name": "gemma4:31b-cloud"
```

E dentro de `model_list`:

```json
{
  "model_name": "gemma4:31b-cloud",
  "provider": "ollama",
  "model": "ollama/gemma4:31b-cloud",
  "api_base": "http://127.0.0.1:11434/v1"
}
```

---

## Erro: HTTPS no Ollama local

```text
server gave HTTP response to HTTPS client
```

Causa:

```text
Ollama local usa HTTP, não HTTPS.
```

Correção:

```json
"api_base": "http://127.0.0.1:11434/v1"
```

Não use:

```json
"api_base": "https://127.0.0.1:11434/v1"
```

---

## Erro: mensagem digitada direto no terminal

```text
command not found
```

Use:

```bash
picoclaw agent -m "Sua mensagem aqui"
```

Ou:

```bash
picoclaw agent
```

---

## Erro: launcher não encontrado

```text
picoclaw-launcher: command not found
```

Correção:

```bash
cd "/opt/picoclaw"

make build-launcher

cp "/opt/picoclaw/build/picoclaw-launcher" "/usr/local/bin/picoclaw-launcher"

chmod +x "/usr/local/bin/picoclaw-launcher"

picoclaw-launcher -public
```

---

# Comandos úteis

```bash
picoclaw --help
```

```bash
picoclaw onboard
```

```bash
nano "/root/.picoclaw/config.json"
```

```bash
picoclaw agent -m "Teste rápido."
```

```bash
picoclaw agent
```

```bash
picoclaw gateway
```

```bash
picoclaw-launcher -public
```

```bash
ss -tulpn
```

---

# Remover PicoClaw

```bash
rm -f "/usr/local/bin/picoclaw"

rm -f "/usr/local/bin/picoclaw-launcher"

rm -rf "/opt/picoclaw"
```

Opcional: remover configuração:

```bash
rm -rf "/root/.picoclaw"
```

---

# Observações

Este guia evita Docker de propósito.

O PicoClaw ainda está em evolução rápida. Comandos, nomes de binários, launcher e formato de configuração podem mudar entre versões.

Pontos confirmados no teste:

```text
Go precisa estar atualizado.
O config.json é criado pelo picoclaw onboard.
O binário principal foi gerado como build/picoclaw-linux-amd64.
O launcher precisou ser compilado com make build-launcher.
picoclaw --version não existia nesta build.
Ollama local precisa usar HTTP, não HTTPS.
agents.defaults.model_name precisa existir em model_list[].model_name.
```