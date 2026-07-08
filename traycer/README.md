# Como instalar e testar o Traycer Desktop no Linux

## Objetivo

Este documento mostra como instalar e executar o **Traycer Desktop** no Linux (Ubuntu/Debian), utilizando o instalador oficial disponibilizado pela equipe do projeto.

> Este documento será atualizado conforme novos testes forem sendo realizados durante a gravação do vídeo.

---

## Fontes oficiais consultadas

Site oficial

https://traycer.ai/

GitHub

https://github.com/traycerai/traycer

Releases

https://github.com/traycerai/traycer/releases

---

## Ambiente testado no vídeo

- Sistema Operacional: Ubuntu 24.04 LTS
- Arquitetura: x86_64
- Desktop: GNOME
- Terminal: Bash
- Data do teste: Julho/2026

---

## Promessa oficial da ferramenta

Segundo os desenvolvedores, o Traycer é um ambiente de desenvolvimento colaborativo para agentes de IA e programadores humanos, permitindo que múltiplos agentes trabalhem em paralelo no mesmo projeto, compartilhem contexto, revisem código entre si e colaborem em um workspace único.

Neste repositório vamos verificar, na prática, se essas funcionalidades realmente funcionam como prometido.

---

## Observação sobre os métodos de instalação

No momento desta documentação, o Traycer disponibiliza oficialmente:

- Linux (.deb)
- Linux (AppImage)
- Linux (.rpm)
- macOS

O suporte para Windows ainda aparece como **Coming Soon** no repositório oficial.

---

## Pré-requisitos

Ubuntu ou Debian baseado em arquitetura AMD64 (x86_64).

Acesso à internet.

---

## Instalação no Linux (.deb)

Baixar o instalador oficial

```bash
cd ~/Downloads

wget https://github.com/traycerai/traycer/releases/latest/download/traycer-desktop-linux-amd64.deb
```

Instalar

```bash
sudo apt install ./traycer-desktop-linux-amd64.deb
```

---

## Instalação alternativa (AppImage)

Baixar

```bash
cd ~/Downloads

wget https://github.com/traycerai/traycer/releases/latest/download/traycer-desktop-linux-x86_64.AppImage
```

Dar permissão

```bash
chmod +x traycer-desktop-linux-x86_64.AppImage
```

Executar

```bash
./traycer-desktop-linux-x86_64.AppImage
```

---

## Como iniciar

Caso o ícone apareça no menu do sistema, basta abrir o Traycer normalmente.

Ou pelo terminal:

```bash
traycer
```

---

## Como verificar se funcionou

O aplicativo deverá abrir a interface gráfica.

Na primeira execução poderão ser solicitadas autenticação e configuração dos provedores de IA.

---

## Teste rápido

Durante o vídeo serão avaliados:

- Interface
- Compatibilidade com Claude Code
- Compatibilidade com Codex
- Compatibilidade com Cursor
- Compatibilidade com modelos locais
- Comunicação entre agentes
- Workspace compartilhado
- Experiência geral

---

## Como remover

```bash
sudo apt remove traycer
```

Caso tenha utilizado AppImage, basta apagar o arquivo.

---

## Erros encontrados e ajustes necessários

> Esta seção será preenchida durante os testes reais.

---

## O que ficou pendente

- Testar integração com Claude Code
- Testar integração com Codex
- Testar múltiplos agentes trabalhando simultaneamente
- Testar compartilhamento de contexto
- Testar consumo de memória
- Testar projetos grandes

---

## Links úteis

Site oficial

https://traycer.ai/

GitHub

https://github.com/traycerai/traycer

Releases

https://github.com/traycerai/traycer/releases
