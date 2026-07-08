# Claude Code no celular Android com MiniMax M3

Este guia é para rodar o **Claude Code direto no celular Android**, usando o **Termux** como terminal Linux.

O app Claude da Play Store não é o Claude Code CLI. Para usar Claude Code no celular, precisamos de terminal.

## 1. Instalar o Termux

Instale o Termux pelo F-Droid ou pelo GitHub oficial.

F-Droid:

```text
https://f-droid.org/packages/com.termux/
```

GitHub:

```text
https://github.com/termux/termux-app/releases
```

Para a maioria dos celulares atuais, use o APK universal mais recente.

Depois de instalar, abra o Termux uma vez.

## 2. Atualizar o Termux

```bash
pkg update && pkg upgrade -y
```

Se aparecer pergunta com `[Y/n]`, digite `Y` e pressione Enter.

## 3. Instalar Node.js

```bash
pkg install nodejs
```

Confira:

```bash
node -v
npm -v
```

## 4. Instalar o Claude Code

```bash
npm install -g @anthropic-ai/claude-code
```

## 5. Corrigir o caminho do Claude Code no Termux

No Termux, o comando `claude` pode precisar apontar explicitamente para o Node.js do Termux.

Rode:

```bash
sed -i '1s|.*|#!/data/data/com.termux/files/usr/bin/node|' /data/data/com.termux/files/usr/bin/claude
chmod +x /data/data/com.termux/files/usr/bin/claude
```

Teste:

```bash
claude --version
```

## 6. Rodar o Claude Code

```bash
claude
```

Ele deve abrir o assistente de configuração.

Você poderá escolher assinatura, chave de API ou conexão third-party, dependendo da sua conta e do provedor que vai usar.

## 7. Configurar MiniMax M3

Crie e edite o `.bashrc`:

```bash
touch ~/.bashrc
nano ~/.bashrc
```

Adicione no final:

```bash
export ANTHROPIC_AUTH_TOKEN="COLE_SUA_CHAVE_DA_MINIMAX_AQUI"
export ANTHROPIC_BASE_URL="COLE_A_URL_OFICIAL_DA_MINIMAX_AQUI"
export ANTHROPIC_MODEL="MiniMax-M3"
```

Salve no nano com:

```text
CTRL + O
ENTER
CTRL + X
```

Recarregue:

```bash
source ~/.bashrc
```

Confira sem mostrar a chave:

```bash
echo $ANTHROPIC_BASE_URL
echo $ANTHROPIC_MODEL
[ -n "$ANTHROPIC_AUTH_TOKEN" ] && echo "Token configurado" || echo "Token ausente"
```

Depois rode:

```bash
claude
```

## 8. Opção grátis com Ollama

Este caminho é opcional e experimental.

Instale o Ollama:

```bash
pkg install -y ollama
```

Inicie o servidor em uma sessão do Termux:

```bash
ollama serve
```

Deixe essa sessão aberta. Depois abra uma nova sessão no Termux.

Configure as variáveis:

```bash
export ANTHROPIC_AUTH_TOKEN=ollama
export ANTHROPIC_API_KEY=""
export ANTHROPIC_BASE_URL=http://localhost:11434
```

Rode com um modelo leve:

```bash
ollama launch claude --model qwen3:0.6b
```

Esse modo pode ficar lento no celular. É melhor para estudo e teste.

## 9. Teste com Python

```bash
pkg install -y python
mkdir -p ~/teste-claude-code
cd ~/teste-claude-code
claude
```

Peça ao Claude Code:

```text
Crie um arquivo hello.py com um Hello World em Python e me diga como executar.
```

Depois rode:

```bash
python hello.py
```

## 10. Teste com HTML no navegador do celular

Peça ao Claude Code:

```text
Crie um site simples em HTML com um título Hello World e um botão.
```

Depois sirva a pasta com Python:

```bash
python -m http.server 8080
```

No navegador do celular, abra:

```text
http://localhost:8080
```

## 11. Se aparecer `npm warn allow-scripts`

Se o npm bloquear o script de instalação, rode:

```bash
npm install -g @anthropic-ai/claude-code --allow-scripts=@anthropic-ai/claude-code
```

Depois repita a correção do Termux:

```bash
sed -i '1s|.*|#!/data/data/com.termux/files/usr/bin/node|' /data/data/com.termux/files/usr/bin/claude
chmod +x /data/data/com.termux/files/usr/bin/claude
```

E teste:

```bash
claude --version
```

## 12. Se aparecer erro `ENOENT package.json`

Se aparecer algo como:

```text
npm error code ENOENT
npm error path /data/data/com.termux/files/home/package.json
```

Não crie `package.json`.

Rode o comando completo:

```bash
npm install -g @anthropic-ai/claude-code --allow-scripts=@anthropic-ai/claude-code
```

## 13. Comandos rápidos

Instalação básica:

```bash
pkg update && pkg upgrade -y
pkg install nodejs
npm install -g @anthropic-ai/claude-code
sed -i '1s|.*|#!/data/data/com.termux/files/usr/bin/node|' /data/data/com.termux/files/usr/bin/claude
chmod +x /data/data/com.termux/files/usr/bin/claude
claude --version
```

Rodar:

```bash
claude
```

Ollama opcional:

```bash
pkg install -y ollama
ollama serve
```

Em outra sessão:

```bash
export ANTHROPIC_AUTH_TOKEN=ollama
export ANTHROPIC_API_KEY=""
export ANTHROPIC_BASE_URL=http://localhost:11434
ollama launch claude --model qwen3:0.6b
```

## Aviso final

Nunca publique sua chave da MiniMax no GitHub, em prints ou em vídeos.

O caminho com assinatura/API tende a funcionar melhor. O caminho local com Ollama é possível, mas pode ficar lento dependendo do celular.
