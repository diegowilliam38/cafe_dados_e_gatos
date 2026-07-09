# Claude Code no celular Android com MiniMax M3

Este guia é para rodar o **Claude Code direto no celular Android**, usando o **Termux** como terminal Linux.

O app Claude da Play Store não é o Claude Code CLI. Para usar Claude Code no celular, precisamos de terminal.

## Importante sobre versões

Nos testes com a versão atual `2.1.205`, o Claude Code falhou no Termux/Android com o erro de binário nativo ausente.

O motivo é que versões a partir da `2.1.113` passaram a depender de um binário nativo Linux com glibc. O Termux roda sobre Android, que usa Bionic libc, então esse binário não funciona corretamente ali.

### Issue de referência

A issue abaixo documenta o problema no GitHub da Anthropic:

```text
https://github.com/anthropics/claude-code/issues/50270
```

Resumo da issue:

- a partir da versão `2.1.113`, o Claude Code passou a usar binário nativo Linux com glibc;
- o Termux/Android não usa glibc, ele usa Bionic libc;
- por isso, versões novas podem falhar com erro de binário nativo ausente;
- a versão indicada como última funcional no Termux é a `2.1.112`.

A versão indicada no issue do GitHub como última versão funcional no Termux é:

```text
2.1.112
```

Por isso, neste guia, vamos instalar fixando a versão e desativando o auto update:

```bash
export DISABLE_AUTOUPDATER=1
npm install -g @anthropic-ai/claude-code@2.1.112
```

---

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

---

## 2. Atualizar o Termux

```bash
pkg update && pkg upgrade -y
```

Se aparecer pergunta com `[Y/n]`, digite `Y` e pressione Enter.

---

## 3. Instalar Node.js

```bash
pkg install nodejs
```

Confira:

```bash
node -v
npm -v
```

---

## 4. Desativar o auto update do Claude Code

Antes de instalar o Claude Code, desative o auto update para evitar que ele atualize sozinho para a versão `2.1.113+`, que não funciona corretamente no Termux/Android.

Teste temporário:

```bash
export DISABLE_AUTOUPDATER=1
```

Para deixar definitivo, salve no `.bashrc`:

```bash
touch ~/.bashrc
nano ~/.bashrc
```

Adicione no final:

```bash
export DISABLE_AUTOUPDATER=1
```

Salve e recarregue:

```bash
source ~/.bashrc
```

---

## 5. Instalar o Claude Code no Termux

Não instale o `latest` no Termux, porque as versões novas podem falhar no Android.

Instale a versão `2.1.112`:

```bash
npm install -g @anthropic-ai/claude-code@2.1.112
```

Teste:

```bash
claude --version
```

Se aparecer a versão, a instalação funcionou.

---

## 6. Rodar o Claude Code

```bash
claude
```

Ele deve abrir o assistente de configuração.

Você poderá escolher assinatura, chave de API ou conexão third-party, dependendo da sua conta e do provedor que vai usar.

---

## 7. Configurar MiniMax M3

Primeiro, teste a configuração de forma temporária no próprio Termux:

```bash
export DISABLE_AUTOUPDATER=1
export ANTHROPIC_AUTH_TOKEN="COLE_SUA_CHAVE_DA_MINIMAX_AQUI"
export ANTHROPIC_BASE_URL="https://api.minimax.io/anthropic"
export ANTHROPIC_MODEL="MiniMax-M3"

claude
```

Se funcionar e você quiser deixar definitivo, salve no `.bashrc`:

```bash
touch ~/.bashrc
nano ~/.bashrc
```

Adicione no final:

```bash
export DISABLE_AUTOUPDATER=1
export ANTHROPIC_AUTH_TOKEN="COLE_SUA_CHAVE_DA_MINIMAX_AQUI"
export ANTHROPIC_BASE_URL="https://api.minimax.io/anthropic"
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
echo $DISABLE_AUTOUPDATER
echo $ANTHROPIC_BASE_URL
echo $ANTHROPIC_MODEL
[ -n "$ANTHROPIC_AUTH_TOKEN" ] && echo "Token configurado" || echo "Token ausente"
```

Depois rode:

```bash
claude
```

---

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
export DISABLE_AUTOUPDATER=1
export ANTHROPIC_AUTH_TOKEN=ollama
export ANTHROPIC_API_KEY=""
export ANTHROPIC_BASE_URL=http://localhost:11434
```

Rode com um modelo leve:

```bash
ollama launch claude --model qwen3:0.6b
```

Esse modo pode ficar lento no celular. É melhor para estudo e teste.

---

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

---

## 10. Teste com HTML no navegador do celular

Peça ao Claude Code:

```text
Crie um site simples em HTML sobre saúde felina. O site deve ter título, uma seção sobre sinais de alerta em gatos, uma seção sobre hidratação, uma seção sobre alimentação e um aviso dizendo que o conteúdo não substitui consulta veterinária.
```

Depois sirva a pasta com Python:

```bash
python -m http.server 8080
```

No navegador do celular, abra:

```text
http://localhost:8080
```

---

## 11. Não use estes comandos com versões novas

Com versões novas do Claude Code, pode aparecer erro como:

```text
Error: claude native binary not installed.
```

Também pode aparecer mensagem dizendo que não existe binário para:

```text
linux-arm64-android
```

Nesse caso, não adianta corrigir com `sed` nem forçar `install.cjs`.

A solução no Termux é usar a versão funcional e manter o auto update desativado:

```bash
export DISABLE_AUTOUPDATER=1
npm install -g @anthropic-ai/claude-code@2.1.112
```

---

## 12. Comandos rápidos

```bash
pkg update && pkg upgrade -y
pkg install nodejs
touch ~/.bashrc
echo 'export DISABLE_AUTOUPDATER=1' >> ~/.bashrc
source ~/.bashrc
npm install -g @anthropic-ai/claude-code@2.1.112
claude --version
claude
```

## Aviso final

Nunca publique sua chave da MiniMax no GitHub, em prints ou em vídeos.

O caminho com assinatura/API tende a funcionar melhor. O caminho local com Ollama é possível, mas pode ficar lento dependendo do celular.
