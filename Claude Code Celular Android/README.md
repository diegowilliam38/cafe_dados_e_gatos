# Claude Code no celular Android com MiniMax M3

Este guia mostra como preparar um celular Android para tentar rodar o Claude Code pelo Termux e configurar o MiniMax M3 como modelo.

> Observação importante: no Android, o Claude Code não roda como aplicativo comum. Ele roda dentro de um terminal Linux no celular, normalmente pelo Termux. A instalação no Termux pode exigir ajustes porque o Claude Code depende de binário nativo.

## Lógica da instalação

Antes de instalar o Claude Code, precisamos primeiro instalar e atualizar o Termux.

Sem Termux, não existe terminal Linux no Android. E sem terminal, não existe onde rodar os comandos do Claude Code.

Por isso a ordem correta é:

1. Instalar o Termux
2. Atualizar o Termux
3. Instalar os pacotes básicos
4. Criar o arquivo de configuração do Termux
5. Instalar o Claude Code via npm
6. Testar o comando `claude`
7. Corrigir possíveis erros de instalação
8. Configurar o MiniMax M3
9. Testar com o modelo

## Onde rodar

Os comandos só começam depois que o Termux estiver instalado no celular Android.

Dentro do Termux, os comandos funcionam como em um pequeno Linux no Android.

## 1. Instalar o Termux

Use a versão do Termux pelo F-Droid:

```text
https://f-droid.org/packages/com.termux/
```

Evite a versão antiga da Play Store, porque ela costuma ficar desatualizada.

Depois de instalar, abra o Termux uma vez para ele criar o ambiente inicial.

## 2. Atualizar o Termux

Com o Termux aberto, rode:

```bash
pkg update && pkg upgrade -y
```

Esse passo vem antes de instalar o Claude Code porque atualiza os repositórios e pacotes do ambiente Linux do Android.

## 3. Instalar pacotes básicos

Agora instale as ferramentas que o Claude Code vai precisar:

```bash
pkg install -y nodejs git curl nano
```

Depois confira se o Node.js e o npm foram instalados:

```bash
node -v
npm -v
```

Exemplo de saída que funcionou nos testes:

```text
node v26.3.1
npm 11.18.0
```

## 4. Preparar o arquivo de configuração do Termux

No Termux, o arquivo `~/.bashrc` pode não existir por padrão.

Antes de usar `source ~/.bashrc`, crie o arquivo:

```bash
touch ~/.bashrc
```

Agora confira se ele existe:

```bash
ls -la ~/.bashrc
```

Resultado esperado:

```text
/data/data/com.termux/files/home/.bashrc
```

Se aparecer o arquivo, pode continuar.

## 5. Instalar o Claude Code no Termux

No Android/Termux, use a instalação via npm:

```bash
npm install -g @anthropic-ai/claude-code
```

Depois teste:

```bash
claude --version
```

## 6. Se aparecer `npm warn allow-scripts`

Em algumas instalações no Termux, o npm adiciona o pacote, mas bloqueia o script de instalação do Claude Code.

O aviso aparece parecido com isto:

```text
npm warn allow-scripts 1 package has install scripts not yet covered by allowScripts
npm warn allow-scripts @anthropic-ai/claude-code@2.1.205 (postinstall: node install.cjs)
npm warn allow-scripts Run `npm install -g --allow-scripts=@anthropic-ai/claude-code` to allow these scripts once
```

Primeiro tente o comando completo:

```bash
npm install -g @anthropic-ai/claude-code --allow-scripts=@anthropic-ai/claude-code
```

Depois teste:

```bash
claude --version
```

Se continuar dando erro, tente o método de configuração do npm:

```bash
npm uninstall -g @anthropic-ai/claude-code
npm config set allow-scripts=@anthropic-ai/claude-code --location=user
npm install -g @anthropic-ai/claude-code
claude --version
```

> Importante: não rode apenas `npm install -g --allow-scripts=@anthropic-ai/claude-code`, porque aí o npm pode tentar procurar um `package.json` na pasta atual e retornar erro `ENOENT`.

## 7. Se aparecer erro `ENOENT package.json`

Se você rodou o comando incompleto e apareceu algo assim:

```text
npm error code ENOENT
npm error path /data/data/com.termux/files/home/package.json
npm error enoent Could not read package.json
```

Não precisa criar `package.json`.

Esse erro apareceu porque o comando foi executado sem informar o pacote que deveria ser instalado.

Rode o comando correto:

```bash
npm install -g @anthropic-ai/claude-code --allow-scripts=@anthropic-ai/claude-code
```

Se continuar com problema, use o método de configuração:

```bash
npm uninstall -g @anthropic-ai/claude-code
npm config set allow-scripts=@anthropic-ai/claude-code --location=user
npm install -g @anthropic-ai/claude-code
```

Depois teste:

```bash
claude --version
```

## 8. Se aparecer `claude native binary not installed`

Se o comando `claude --version` retornar:

```text
Error: claude native binary not installed.
```

Tente rodar o pós-instalação manualmente.

Primeiro veja onde ficam os pacotes globais do npm:

```bash
npm root -g
```

Depois rode:

```bash
node $(npm root -g)/@anthropic-ai/claude-code/install.cjs
```

Agora teste novamente:

```bash
claude --version
```

Se continuar dando erro, a instalação do Claude Code no Termux ainda pode não estar funcionando por causa do binário nativo usado pelo Claude Code. Nesse caso, o caminho mais seguro é usar o celular para acessar uma máquina Linux, VPS ou PC por SSH e rodar o Claude Code lá.

## 9. Atenção: instalador oficial via curl no Termux

No PC Linux, macOS ou WSL, o instalador oficial pode funcionar assim:

```bash
curl -fsSL https://claude.ai/install.sh | bash
```

Mas no Android/Termux esse caminho pode baixar um binário `linux-arm64` que não executa corretamente no Android.

O erro costuma aparecer assim:

```text
cannot execute: required file not found
```

Se isso acontecer, não continue insistindo no instalador `curl`. Use o npm e os passos de correção acima.

## 10. Configurar MiniMax M3 no Claude Code

A MiniMax disponibiliza o M3 por API. Para usar com o Claude Code, a configuração normalmente é feita apontando o Claude Code para o endpoint compatível indicado pela MiniMax e passando a chave de API.

Edite o arquivo de configuração do shell:

```bash
nano ~/.bashrc
```

Adicione no final do arquivo:

```bash
export ANTHROPIC_AUTH_TOKEN="COLE_SUA_CHAVE_DA_MINIMAX_AQUI"
export ANTHROPIC_BASE_URL="COLE_A_URL_OFICIAL_DA_MINIMAX_AQUI"
export ANTHROPIC_MODEL="MiniMax-M3"
```

Salve com:

```text
CTRL + O
ENTER
CTRL + X
```

Recarregue o terminal:

```bash
source ~/.bashrc
```

Confira se as variáveis foram carregadas:

```bash
echo $ANTHROPIC_BASE_URL
echo $ANTHROPIC_MODEL
```

A chave não deve ser exibida no terminal. Para conferir apenas se ela existe:

```bash
[ -n "$ANTHROPIC_AUTH_TOKEN" ] && echo "Token configurado" || echo "Token ausente"
```

## 11. Testar o Claude Code com MiniMax M3

Entre em uma pasta de teste:

```bash
mkdir -p ~/teste-claude-minimax
cd ~/teste-claude-minimax
```

Abra o Claude Code:

```bash
claude
```

Faça um teste simples:

```text
Crie um README.md simples explicando que este projeto é um teste do Claude Code no Android usando MiniMax M3.
```

## 12. Se quiser manter a configuração separada

Em vez de colocar tudo direto no `~/.bashrc`, você pode criar um arquivo separado:

```bash
nano ~/.minimax-m3.env
```

Conteúdo:

```bash
export ANTHROPIC_AUTH_TOKEN="COLE_SUA_CHAVE_DA_MINIMAX_AQUI"
export ANTHROPIC_BASE_URL="COLE_A_URL_OFICIAL_DA_MINIMAX_AQUI"
export ANTHROPIC_MODEL="MiniMax-M3"
```

Depois adicione ao `~/.bashrc`:

```bash
echo 'source ~/.minimax-m3.env' >> ~/.bashrc
```

Recarregue:

```bash
source ~/.bashrc
```

## 13. Limpar tentativa quebrada e recomeçar

Se quiser remover uma tentativa anterior do Claude Code e começar de novo a partir do Termux já instalado:

```bash
rm -rf ~/.claude
npm uninstall -g @anthropic-ai/claude-code
clear
```

Depois volte para o passo de atualização:

```bash
pkg update && pkg upgrade -y
```

## 14. Comandos rápidos

```bash
pkg update && pkg upgrade -y
pkg install -y nodejs git curl nano
touch ~/.bashrc
npm install -g @anthropic-ai/claude-code
npm install -g @anthropic-ai/claude-code --allow-scripts=@anthropic-ai/claude-code
node $(npm root -g)/@anthropic-ai/claude-code/install.cjs
claude --version
```

## 15. Nota para revisão

Este guia deixa os campos da URL oficial e da chave como placeholders para evitar publicar informação sensível. Antes de gravar o vídeo ou seguir em produção, confira a página oficial da MiniMax usada no seu PC e substitua `COLE_A_URL_OFICIAL_DA_MINIMAX_AQUI` pelo endpoint correto informado por eles.
