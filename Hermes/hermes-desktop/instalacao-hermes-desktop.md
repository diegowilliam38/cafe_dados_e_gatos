# Como instalar o Hermes Desktop no Ubuntu usando DEB

## O que vamos fazer

Instalar o Hermes Desktop no Ubuntu usando o pacote `.deb`.

Este guia usa apenas um caminho de instalação para evitar confusão.

O Hermes Desktop é a interface visual do Hermes Agent.

Neste teste, o Hermes Agent já existe no ambiente.

Por isso, este guia não instala o Hermes Agent do zero e não apaga os dados persistentes do Hermes Agent.

## Repositórios

Hermes Desktop:

    https://github.com/fathah/hermes-desktop

Hermes Agent principal:

    https://github.com/NousResearch/hermes-agent

## Atenção importante

O Hermes Agent guarda dados em:

    ~/.hermes

Neste guia, não vamos apagar:

    ~/.hermes

Essa pasta pertence ao Hermes Agent, não apenas ao Hermes Desktop.

---

# 1. Verificar se o Hermes Agent já existe

    ls -la ~/.hermes

    which hermes || true

    hermes --help

Se o comando `hermes --help` responder, o Hermes Agent já está disponível no ambiente.

---

# 2. Criar a pasta de download

    mkdir -p ~/Downloads/hermes-desktop

    cd ~/Downloads/hermes-desktop

---

# 3. Abrir a página de releases

    xdg-open https://github.com/fathah/hermes-desktop/releases

Na página de releases, baixar o arquivo Linux `.deb`.

Exemplo de nome do arquivo:

    hermes-desktop_0.3.5_amd64.deb

A versão pode mudar.

O importante é baixar o arquivo que termina com:

    .deb

---

# 4. Confirmar que o arquivo foi baixado

Dentro da pasta `~/Downloads/hermes-desktop`, rodar:

    ls -lh

Você deve ver um arquivo parecido com:

    hermes-desktop_0.3.5_amd64.deb

Se não aparecer nenhum arquivo `.deb`, o download foi salvo em outra pasta ou ainda não foi feito.

---

# 5. Instalar o Hermes Desktop

Dentro da pasta `~/Downloads/hermes-desktop`, rodar:

    sudo apt install ./*.deb

Se pedir senha, digitar a senha do Ubuntu.

---

# 6. Abrir o Hermes Desktop

Depois da instalação, procurar no menu de aplicativos por:

    Hermes

ou:

    Hermes Agent

Se quiser tentar abrir pelo terminal, testar:

    hermes-desktop

Se esse comando não funcionar, testar:

    hermes-agent

Se nenhum dos dois comandos abrir, procurar pelo aplicativo no menu gráfico do Ubuntu.

---

# 7. Primeiro uso

Na primeira abertura, o Hermes Desktop pode perguntar se você quer rodar localmente ou conectar em um servidor remoto.

Para este teste, escolher o modo local.

O app deve procurar a instalação local do Hermes em:

    ~/.hermes

Como o Hermes Agent já existe no ambiente, o ideal é que o app reconheça a instalação existente.

---

# 8. Endereço local usado pelo app

No modo local, o Hermes Desktop pode usar o Hermes Agent em:

    http://127.0.0.1:8642

Se o app não conseguir conectar, verificar se o Hermes está funcionando pelo terminal:

    hermes --help

    hermes

---

# 9. Funções principais para testar no vídeo

## 1. Chat

Testar se o app consegue conversar com o Hermes Agent pela interface visual.

Observar:

    abre corretamente
    envia mensagem
    recebe resposta
    mostra streaming
    renderiza markdown

## 2. Sessions

Testar se o app mostra sessões ou conversas anteriores.

Observar:

    lista histórico
    permite buscar conversas
    permite retomar sessão
    organiza por data

## 3. Memory

Testar se o app mostra ou permite acessar a memória.

Observar:

    mostra entradas de memória
    mostra perfil do usuário
    mostra estado da memória
    permite visualizar sem quebrar o Hermes

---

# 10. Comandos úteis para diagnóstico

Ver se o Hermes Agent existe:

    which hermes || true

Ver ajuda do Hermes:

    hermes --help

Abrir Hermes pelo terminal:

    hermes

Escolher modelo:

    hermes model

Configurar Hermes:

    hermes setup

Diagnóstico:

    hermes doctor

Ver versão:

    hermes --version

Ver pacote instalado do Desktop:

    dpkg -l | grep -i hermes

---

# 11. Remover o Hermes Desktop instalado via DEB

Primeiro, descobrir o nome do pacote instalado:

    dpkg -l | grep -i hermes

Se aparecer `hermes-desktop`, remover com:

    sudo apt remove hermes-desktop -y

Remover dependências que não são mais usadas:

    sudo apt autoremove -y

Se o nome do pacote for outro, remover usando o nome exibido pelo comando `dpkg -l | grep -i hermes`.

Exemplo:

    sudo apt remove NOME_DO_PACOTE -y

---

# 12. Ver dados locais do app desktop

Não apagar `~/.hermes`.

Antes de remover qualquer dado persistente do app desktop, verificar possíveis pastas do aplicativo:

    find ~/.config ~/.cache ~/.local/share -maxdepth 2 -iname '*hermes*' -print 2>/dev/null

A pasta abaixo não deve ser removida neste guia:

    ~/.hermes

---

# 13. Remover dados persistentes do Hermes Desktop

O Hermes Desktop é um aplicativo Electron.

Dependendo da versão e do empacotamento, os dados do app desktop podem aparecer em locais como:

    ~/.config/Hermes Agent
    ~/.cache/Hermes Agent
    ~/.local/share/Hermes Agent

Verificar antes:

    ls -la ~/.config | grep -i hermes || true
    ls -la ~/.cache | grep -i hermes || true
    ls -la ~/.local/share | grep -i hermes || true

Remover apenas dados do app desktop:

    rm -rf "$HOME/.config/Hermes Agent"
    rm -rf "$HOME/.cache/Hermes Agent"
    rm -rf "$HOME/.local/share/Hermes Agent"

---

# 14. Garantir que os dados do Hermes Agent continuam intactos

Verificar se `~/.hermes` ainda existe:

    ls -la ~/.hermes

Testar o Hermes Agent:

    hermes --help

---

# 15. Remoção completa apenas do Desktop App

Fluxo seguro:

    dpkg -l | grep -i hermes || true

    sudo apt remove hermes-desktop -y || true

    sudo apt autoremove -y

    rm -rf "$HOME/.config/Hermes Agent"
    rm -rf "$HOME/.cache/Hermes Agent"
    rm -rf "$HOME/.local/share/Hermes Agent"

    ls -la ~/.hermes

    hermes --help

---

# 16. O que não apagar

Não apagar:

    ~/.hermes

Não rodar:

    rm -rf ~/.hermes

Não rodar:

    rm -rf ~/.hermes/hermes-agent

Não rodar:

    rm -rf ~/.hermes/profiles

Esses dados pertencem ao Hermes Agent, não apenas ao Hermes Desktop.

---

# 17. Resumo rápido

Criar pasta:

    mkdir -p ~/Downloads/hermes-desktop

    cd ~/Downloads/hermes-desktop

Abrir releases:

    xdg-open https://github.com/fathah/hermes-desktop/releases

Baixar o arquivo `.deb`.

Conferir:

    ls -lh

Instalar:

    sudo apt install ./*.deb

Remover apenas o Desktop App:

    sudo apt remove hermes-desktop -y || true

    sudo apt autoremove -y

    rm -rf "$HOME/.config/Hermes Agent"
    rm -rf "$HOME/.cache/Hermes Agent"
    rm -rf "$HOME/.local/share/Hermes Agent"

Conferir que o Hermes Agent continua intacto:

    ls -la ~/.hermes

    hermes --help
