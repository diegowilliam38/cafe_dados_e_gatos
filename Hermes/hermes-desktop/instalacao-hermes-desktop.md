# Como instalar o Hermes Desktop

## O que vamos fazer

Instalar o Hermes Desktop no Linux.

O Hermes Desktop é a interface visual do Hermes Agent.

Ele serve para usar o Hermes por uma tela gráfica, sem depender apenas do terminal.

Neste guia, o Hermes Agent já existe no ambiente.

Por isso, não vamos apagar nem alterar os dados persistentes do Hermes Agent.

## Repositórios

Hermes Desktop:

    https://github.com/fathah/hermes-desktop

Hermes Agent principal:

    https://github.com/NousResearch/hermes-agent

## Atenção importante

O Hermes Agent guarda dados em:

    ~/.hermes

Essa pasta pode conter:

    ~/.hermes/.env
    ~/.hermes/config.yaml
    ~/.hermes/hermes-agent
    ~/.hermes/profiles/
    ~/.hermes/state.db
    ~/.hermes/cron/jobs.json

Neste guia, não vamos apagar:

    ~/.hermes

A remoção segura deste documento remove apenas o aplicativo Hermes Desktop e dados locais do app desktop, quando existirem.

---

# 1. Verificar se o Hermes Agent já existe

    ls -la ~/.hermes

    which hermes || true

    hermes --help

Se o comando `hermes --help` responder, o Hermes Agent já está disponível no ambiente.

---

# 2. Criar pasta para baixar o Hermes Desktop

    mkdir -p ~/Downloads/hermes-desktop
    cd ~/Downloads/hermes-desktop

---

# 3. Abrir a página de releases

    xdg-open https://github.com/fathah/hermes-desktop/releases

Na página de releases, baixar uma das opções:

    Linux AppImage: arquivo .AppImage
    Linux Ubuntu/Debian: arquivo .deb
    Linux Fedora: arquivo .rpm
    Windows: arquivo .exe
    macOS: arquivo .dmg

Para Ubuntu, existem duas opções boas:

    .AppImage
    .deb

---

# 4. Instalação usando AppImage

Use esta opção se quiser testar sem instalar pacote no sistema.

Depois de baixar o arquivo `.AppImage`, entre na pasta onde ele foi salvo:

    cd ~/Downloads/hermes-desktop

Dar permissão de execução:

    chmod +x *.AppImage

Executar:

    ./*.AppImage

Se o sistema pedir integração com o menu, aceitar se quiser.

---

# 5. Instalação usando DEB

Use esta opção se quiser instalar como aplicativo do sistema no Ubuntu/Debian.

Depois de baixar o arquivo `.deb`, entre na pasta onde ele foi salvo:

    cd ~/Downloads/hermes-desktop

Instalar:

    sudo apt install ./hermes-desktop*.deb

Se o nome do arquivo baixado estiver diferente, listar os arquivos:

    ls -lh

E instalar apontando para o nome correto:

    sudo apt install ./NOME_DO_ARQUIVO.deb

---

# 6. Abrir o Hermes Desktop

Depois de instalar via `.deb`, procurar no menu de aplicativos por:

    Hermes Agent

Ou tentar abrir pelo terminal:

    hermes-agent

Se o comando não existir, abrir pelo menu gráfico.

---

# 7. Primeiro uso

Na primeira abertura, o Hermes Desktop pode perguntar se você quer:

    Run Hermes locally

ou:

    Connect to remote Hermes API server

Para teste local, escolher:

    Run Hermes locally

O app deve procurar a instalação local do Hermes em:

    ~/.hermes

Como o Hermes Agent já existe no ambiente, o ideal é que o app reconheça a instalação existente.

---

# 8. Endereço local usado pelo app

No modo local, o Hermes Desktop usa o Hermes Agent em:

    http://127.0.0.1:8642

Se o app não conseguir conectar, verificar se o Hermes está funcionando pelo terminal:

    hermes --help

    hermes

---

# 9. Funções principais para testar

## 1. Chat

Testar se o app consegue conversar com o Hermes Agent pela interface visual.

O que observar:

    abre corretamente
    envia mensagem
    recebe resposta
    mostra streaming
    renderiza markdown
    mostra progresso de ferramentas, se houver

## 2. Sessions

Testar se o app mostra sessões ou conversas anteriores.

O que observar:

    lista histórico
    permite buscar conversas
    permite retomar sessão
    organiza por data

## 3. Memory

Testar se o app mostra ou permite editar a memória.

O que observar:

    mostra entradas de memória
    mostra perfil do usuário
    mostra capacidade ou estado da memória
    permite editar sem quebrar o Hermes

---

# 10. Principais áreas do Hermes Desktop

O app pode ter telas como:

    Chat
    Sessions
    Agents / Profiles
    Skills
    Models
    Memory
    Soul / Persona
    Tools
    Schedules
    Gateway
    Office
    Settings
    Logs
    Backup
    Import
    Debug dump

Algumas telas podem mudar conforme a versão.

O projeto ainda está em desenvolvimento ativo.

---

# 11. Principais comandos úteis do Hermes Agent

Mesmo usando o Desktop App, estes comandos ajudam no diagnóstico.

Ver se o Hermes existe:

    which hermes || true

Ver ajuda:

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

---

# 12. Remover Hermes Desktop instalado via DEB

Primeiro, descobrir o nome do pacote instalado:

    dpkg -l | grep -i hermes

Se aparecer `hermes-desktop`, remover:

    sudo apt remove hermes-desktop -y

Remover dependências que não são mais usadas:

    sudo apt autoremove -y

Se o nome do pacote for outro, remover usando o nome exibido pelo comando:

    sudo apt remove NOME_DO_PACOTE -y

---

# 13. Remover Hermes Desktop usado como AppImage

Se usou AppImage, basta apagar o arquivo baixado.

    rm -f ~/Downloads/hermes-desktop/*.AppImage

Se criou outro local para o AppImage, apagar o arquivo nesse local.

Exemplo:

    rm -f ~/Aplicativos/*Hermes*.AppImage

---

# 14. Remover atalho do AppImage, se existir

Alguns AppImages criam atalhos em `~/.local/share/applications`.

Verificar:

    find ~/.local/share/applications -iname '*hermes*' -print

Remover apenas atalhos do Hermes Desktop:

    find ~/.local/share/applications -iname '*hermes*' -delete

---

# 15. Ver dados locais do app desktop

Não vamos apagar `~/.hermes`.

Antes de remover qualquer dado persistente do app desktop, verificar possíveis pastas do aplicativo:

    find ~/.config ~/.cache ~/.local/share -maxdepth 2 -iname '*hermes*' -print 2>/dev/null

Atenção:

    ~/.hermes

não deve ser removido neste guia.

---

# 16. Remover dados persistentes do Hermes Desktop

O app é um aplicativo Electron.

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

# 17. Garantir que os dados do Hermes Agent continuam intactos

Verificar se `~/.hermes` ainda existe:

    ls -la ~/.hermes

Testar o Hermes Agent:

    hermes --help

---

# 18. Remoção completa apenas do Desktop App

Fluxo seguro:

    dpkg -l | grep -i hermes || true

    sudo apt remove hermes-desktop -y || true
    sudo apt autoremove -y

    rm -f ~/Downloads/hermes-desktop/*.AppImage

    find ~/.local/share/applications -iname '*hermes*' -print

    rm -rf "$HOME/.config/Hermes Agent"
    rm -rf "$HOME/.cache/Hermes Agent"
    rm -rf "$HOME/.local/share/Hermes Agent"

    ls -la ~/.hermes
    hermes --help

---

# 19. O que não apagar

Não apagar:

    ~/.hermes

Não rodar:

    rm -rf ~/.hermes

Não rodar:

    rm -rf ~/.hermes/hermes-agent

Não rodar:

    rm -rf ~/.hermes/profiles

Esses dados pertencem ao Hermes Agent, não apenas ao Desktop App.

---

# 20. Resumo rápido

Para instalar:

    mkdir -p ~/Downloads/hermes-desktop
    cd ~/Downloads/hermes-desktop
    xdg-open https://github.com/fathah/hermes-desktop/releases

Baixar `.AppImage` ou `.deb`.

AppImage:

    chmod +x *.AppImage
    ./*.AppImage

DEB:

    sudo apt install ./hermes-desktop*.deb

Para remover o Desktop App sem apagar o Hermes Agent:

    sudo apt remove hermes-desktop -y || true
    sudo apt autoremove -y
    rm -rf "$HOME/.config/Hermes Agent"
    rm -rf "$HOME/.cache/Hermes Agent"
    rm -rf "$HOME/.local/share/Hermes Agent"
    ls -la ~/.hermes
