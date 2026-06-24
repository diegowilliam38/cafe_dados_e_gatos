# OpenJarvis no Windows: caminho recomendado

Guia pratico para instalar o **OpenJarvis** no Windows seguindo apenas o caminho **recomendado pela documentacao oficial do projeto**.

Neste guia:

- o **WSL2 + Ubuntu** instala o **backend**
- a interface pode ser pelo **navegador** ou pelo **app desktop do Windows**

## Recomendacao

A documentacao oficial do OpenJarvis recomenda, no Windows:

- **Windows + WSL2 + Ubuntu**

Este guia mostra somente esse caminho.

## Antes de comecar

Tenha em mente estes pontos:

- Windows 10 ou Windows 11
- internet funcionando
- acesso de administrador para instalar o WSL2
- pelo menos **8 GB a 10 GB livres no `C:`** para instalar com folga

> Observacao:
> Mesmo usando WSL2, parte da instalacao continua consumindo espaco no `C:`. Se o disco estiver muito cheio, limpe antes de instalar.

## Se voce ja tem Ollama no Windows

Tudo bem. Ter o **Ollama** instalado ajuda, mas **nao instala o OpenJarvis sozinho**.

Voce ainda precisa instalar o OpenJarvis separadamente.

## Instalacao recomendada no Windows

### 1. Instale o WSL2

Abra o **PowerShell como Administrador** e rode:

```powershell
wsl --install
```

Se o Windows pedir, reinicie a maquina.

### 2. Abra o Ubuntu

Depois da instalacao, abra o **Ubuntu** no menu iniciar e finalize a criacao do usuario e senha.

### 3. Instale o OpenJarvis dentro do Ubuntu

No terminal do Ubuntu, rode:

```bash
curl -fsSL https://open-jarvis.github.io/OpenJarvis/install.sh | bash
```

Quando terminar, teste:

```bash
jarvis
```

## Como abrir o OpenJarvis depois da instalacao

Depois que o OpenJarvis estiver instalado no Ubuntu/WSL2, voce pode usar de duas formas:

- **browser**
- **app desktop do Windows**

Em ambos os casos, o que roda no WSL2 e o **backend**.

### Opcao 1. Usar no navegador

Inicie o backend dentro do Ubuntu/WSL:

```bash
jarvis serve
```

Depois abra no Windows:

```text
http://localhost:8000
```

### Opcao 2. Usar com o app desktop do Windows

Se voce quiser usar o app desktop do OpenJarvis no Windows:

1. Inicie o backend dentro do Ubuntu/WSL
2. Baixe e instale o app desktop do Windows
3. Depois abra o app desktop no Windows

Para subir o backend:

```bash
jarvis serve
```

O app desktop do Windows deve se conectar em:

```text
http://localhost:8000
```

Baixe o app desktop pela pagina oficial de releases:

```text
https://github.com/open-jarvis/OpenJarvis/releases
```

## Erros comuns

### 1. `./scripts/quickstart.sh` abriu uma janela pedindo aplicativo para `.sh`

Isso acontece quando o comando foi rodado no **PowerShell do Windows**.

O arquivo `.sh` e um script de shell Linux/macOS e **nao deve ser executado assim no PowerShell**.

Use o Ubuntu/WSL2 e rode os comandos por la.

### 2. `Subsistema do Windows para Linux nao tem distribuicoes instaladas`

Isso significa que o WSL foi chamado, mas o Ubuntu ainda nao foi instalado.

Rode:

```powershell
wsl --install
```

Se quiser listar as distribuicoes disponiveis:

```powershell
wsl --list --online
```

## Resumo rapido

Se voce quer instalar o OpenJarvis no Windows do jeito recomendado pelo projeto:

1. libere espaco no `C:`
2. instale o `WSL2`
3. abra o `Ubuntu`
4. rode:

```bash
curl -fsSL https://open-jarvis.github.io/OpenJarvis/install.sh | bash
```

Esse e o caminho mais indicado para quem quer reproduzir a instalacao em casa com menos chance de erro.
