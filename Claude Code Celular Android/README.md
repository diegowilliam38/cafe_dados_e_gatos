# Claude Code no celular Android com MiniMax M3

Este guia mostra como preparar um celular Android para rodar o Claude Code pelo Termux e configurar o MiniMax M3 como modelo, usando o mesmo conceito de configuração por variáveis de ambiente que você já usa no computador.

> Observação importante: no Android, o Claude Code não roda como aplicativo comum. Ele roda dentro de um terminal Linux no celular, normalmente pelo Termux.

## Lógica da instalação

Antes de instalar o Claude Code, precisamos primeiro instalar e atualizar o Termux.

Sem Termux, não existe terminal Linux no Android. E sem terminal, não existe onde rodar os comandos do Claude Code.

Por isso a ordem correta é:

1. Instalar o Termux
2. Atualizar o Termux
3. Instalar os pacotes básicos
4. Instalar o Claude Code
5. Configurar o MiniMax M3
6. Testar

## O que vamos fazer

- Instalar o Termux pelo F-Droid
- Atualizar o ambiente Linux do Android
- Instalar Node.js, Git e ferramentas básicas
- Instalar o Claude Code
- Criar o arquivo `~/.bashrc`, caso ele não exista
- Configurar a chave da MiniMax
- Configurar o endpoint/modelo MiniMax M3
- Testar se o Claude Code abre usando o M3

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

Depois confira se o Node.js foi instalado:

```bash
node -v
npm -v
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

## 5. Instalar o Claude Code

Agora sim, com o Termux instalado, atualizado, com Node.js disponível e com o `~/.bashrc` criado, instale o Claude Code.

Tente primeiro pelo instalador oficial:

```bash
curl -fsSL https://claude.ai/install.sh | bash
```

Feche e abra o Termux novamente, ou rode:

```bash
source ~/.bashrc
```

Teste:

```bash
claude --version
```

Se o instalador oficial não funcionar no Termux, tente pelo npm:

```bash
npm install -g @anthropic-ai/claude-code
```

E teste novamente:

```bash
claude --version
```

## 6. Configurar MiniMax M3 no Claude Code

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

## 7. Testar o Claude Code com MiniMax M3

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

## 8. Se quiser manter a configuração separada

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

## 9. Cuidados importantes

Nunca publique sua chave da MiniMax no GitHub.

Não coloque sua chave em prints de vídeo.

No celular, o desempenho pode ser mais limitado que no PC, principalmente para projetos grandes.

Se o Claude Code abrir, mas não responder, verifique:

- se a chave está correta;
- se a URL do endpoint está exatamente igual à documentação da MiniMax;
- se o nome do modelo está correto;
- se o celular está com internet;
- se o Termux está com Node.js atualizado;
- se o arquivo `~/.bashrc` existe.

## 10. Comandos rápidos

A ordem resumida também respeita a lógica: primeiro Termux atualizado, depois dependências, depois `~/.bashrc`, depois Claude Code.

```bash
pkg update && pkg upgrade -y
pkg install -y nodejs git curl nano
touch ~/.bashrc
npm install -g @anthropic-ai/claude-code
source ~/.bashrc
claude --version
```

Configuração:

```bash
nano ~/.bashrc
```

Depois adicione:

```bash
export ANTHROPIC_AUTH_TOKEN="COLE_SUA_CHAVE_DA_MINIMAX_AQUI"
export ANTHROPIC_BASE_URL="COLE_A_URL_OFICIAL_DA_MINIMAX_AQUI"
export ANTHROPIC_MODEL="MiniMax-M3"
```

Recarregue:

```bash
source ~/.bashrc
```

Teste:

```bash
mkdir -p ~/teste-claude-minimax
cd ~/teste-claude-minimax
claude
```

## 11. Nota para revisão

Este guia deixa os campos da URL oficial e da chave como placeholders para evitar publicar informação sensível. Antes de gravar o vídeo ou seguir em produção, confira a página oficial da MiniMax usada no seu PC e substitua `COLE_A_URL_OFICIAL_DA_MINIMAX_AQUI` pelo endpoint correto informado por eles.
