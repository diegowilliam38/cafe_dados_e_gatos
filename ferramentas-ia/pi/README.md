# Como instalar e testar o Pi no Windows

## Objetivo

Instalar e testar o Pi, um harness mínimo para agentes de programação no terminal, diretamente no Windows.

O Pi pode ler, criar e editar arquivos, além de executar comandos. Neste teste, ele será usado dentro de uma pasta separada e versionada com Git, facilitando a revisão e a reversão das alterações.

## Fontes oficiais consultadas

- Site oficial: https://pi.dev/
- Repositório oficial: https://github.com/earendil-works/pi
- Documentação oficial: https://github.com/earendil-works/pi/tree/main/packages/coding-agent/docs
- Instalação rápida: https://github.com/earendil-works/pi/blob/main/packages/coding-agent/docs/quickstart.md
- Configuração no Windows: https://github.com/earendil-works/pi/blob/main/packages/coding-agent/docs/windows.md
- Pacote npm: https://www.npmjs.com/package/@earendil-works/pi-coding-agent

Documentação consultada em 22 de julho de 2026.

## Ambiente testado no vídeo

- Sistema operacional: Windows
- Terminal: PowerShell ou Windows Terminal
- Instalação: Windows nativo
- Isolamento: pasta separada e versionada com Git
- Autenticação: ChatGPT Plus ou Pro por meio do Codex
- Data do teste: preencher após a gravação
- Modelo usado: preencher após o teste

## Pré-requisitos

O Pi é distribuído como pacote npm e requer:

- Node.js 22.19.0 ou superior;
- npm, instalado junto com o Node.js;
- um shell Bash no Windows;
- Git for Windows, recomendado pela documentação oficial do Pi.

No Windows, o Pi procura um shell Bash em locais como:

- caminho personalizado definido nas configurações;
- `C:\Program Files\Git\bin\bash.exe`;
- `bash.exe` disponível no PATH.

Para a maioria das pessoas, instalar o Git for Windows é suficiente.

## Instalar o Node.js e o npm

Abra o PowerShell ou o Windows Terminal. Primeiro, verifique se o WinGet está disponível:

```powershell
winget --version
```

Instale a versão LTS do Node.js:

```powershell
winget install --id OpenJS.NodeJS.LTS -e --source winget
```

O npm é instalado junto com o Node.js. Depois da instalação, feche e abra novamente o PowerShell ou o Windows Terminal.

Verifique:

```powershell
node --version
npm --version
```

O Node.js deve estar na versão `22.19.0` ou superior. Para maior estabilidade, use uma versão LTS.

Se o WinGet não estiver disponível, instale o aplicativo **Instalador de Aplicativo** pela Microsoft Store e tente novamente. Também é possível baixar o instalador LTS diretamente pelo site oficial do Node.js.

## Instalar o Git for Windows e o Git Bash

No PowerShell ou no Windows Terminal:

```powershell
winget install --id Git.Git -e --source winget
```

O Git Bash é instalado junto com o Git for Windows. Depois da instalação, feche e abra novamente o terminal.

Verifique o Git:

```powershell
git --version
```

Verifique se o Bash foi instalado no caminho padrão:

```powershell
Test-Path "C:\Program Files\Git\bin\bash.exe"
```

Resultado esperado:

```text
True
```

Também é possível abrir o menu Iniciar e procurar por:

```text
Git Bash
```

## Instalar o Pi

```powershell
npm install -g --ignore-scripts @earendil-works/pi-coding-agent
```

A opção `--ignore-scripts` desativa scripts de ciclo de vida das dependências durante a instalação. Segundo a documentação oficial, o Pi não precisa desses scripts em uma instalação normal pelo npm.

## Verificar a instalação

```powershell
pi --version
```

## Criar uma pasta isolada para o teste

```powershell
New-Item -ItemType Directory -Force "$HOME\Documents\pi-teste"
Set-Location "$HOME\Documents\pi-teste"
git init
```

O Pi trabalha na pasta atual e pode modificar os arquivos existentes nela. Usar uma pasta separada e inicializar o Git facilita revisar e desfazer alterações.

## Iniciar o Pi

```powershell
pi
```

## Autenticar com o ChatGPT

Dentro do Pi:

```text
/login
```

Selecione a opção de autenticação do ChatGPT Plus ou Pro por meio do Codex e conclua o login no navegador.

Outros logins de assinatura documentados pelo projeto podem aparecer, como Claude Pro ou Max e GitHub Copilot.

## Escolher o modelo

Dentro do Pi:

```text
/model
```

Selecione o modelo disponível para sua autenticação.

## Criar um arquivo para o teste

No PowerShell, dentro da pasta `pi-teste`:

```powershell
@'
# Projeto de teste

Este projeto existe apenas para testar o Pi.
'@ | Set-Content -Encoding UTF8 README.md
```

## Teste rápido de leitura e escrita

Inicie o Pi:

```powershell
pi
```

Use este prompt:

```text
Leia o arquivo README.md, explique o objetivo desta pasta e crie um arquivo chamado teste.txt com uma frase informando que o Pi conseguiu escrever dentro do projeto. Não altere nenhum outro arquivo.
```

Depois encerre ou suspenda a interação e verifique:

```powershell
Get-Content .\teste.txt
git status
```

## Teste em modo somente leitura

Para pedir uma análise sem liberar escrita e execução de comandos:

```powershell
pi --tools read,grep,find,ls -p "Analise os arquivos desta pasta e não faça alterações."
```

## Revisar as alterações

```powershell
git status
git diff
```

## Desfazer alterações não desejadas

Para desfazer alterações em arquivos já rastreados pelo Git:

```powershell
git restore .
```

Para apagar arquivos novos não rastreados, revise primeiro:

```powershell
git clean -n
```

Depois, somente se tiver certeza:

```powershell
git clean -f
```

`git clean -f` remove arquivos não rastreados. Confira a prévia com `git clean -n` antes de executar.

## Atualizar o Pi

```powershell
pi update --self
```

Também é possível reinstalar a versão atual do pacote:

```powershell
npm install -g --ignore-scripts @earendil-works/pi-coding-agent
```

## Encerrar o Pi

Na interface interativa, encerre a sessão normalmente ou pressione:

```text
Ctrl+C
```

## Remover o Pi

```powershell
npm uninstall -g @earendil-works/pi-coding-agent
```

A remoção do pacote não apaga automaticamente configurações, credenciais, sessões e outros dados armazenados pelo Pi.

## Segurança durante o teste

O Pi trabalha com as permissões do processo que o iniciou. Durante o vídeo e os testes:

- use somente uma pasta separada;
- inicialize o Git antes de permitir alterações;
- não execute o Pi como administrador;
- não teste dentro de pastas pessoais ou projetos importantes;
- revise os comandos antes de autorizar ações sensíveis;
- não publique tokens, chaves de API ou arquivos de autenticação;
- revise extensões, skills e pacotes de terceiros antes de instalar.

## Erros encontrados e ajustes necessários

Esta seção será preenchida durante a gravação.

### Bash não encontrado no Windows

**O que aconteceu:**

O Pi foi instalado, mas não encontrou um shell Bash para executar comandos.

**Verificação:**

```powershell
Test-Path "C:\Program Files\Git\bin\bash.exe"
```

**Correção:**

Instale o Git for Windows ou configure manualmente o caminho do Bash nas configurações do Pi.

Exemplo documentado pelo projeto:

```json
{
  "shellPath": "C:\\cygwin64\\bin\\bash.exe"
}
```

### Comando `pi` não encontrado

Feche e abra novamente o PowerShell depois da instalação global pelo npm.

Verifique também:

```powershell
npm config get prefix
Get-Command pi
```

## O que ficou pendente

- Registrar o modelo usado no vídeo.
- Registrar os erros reais encontrados durante a instalação.
- Confirmar o comportamento do login no navegador durante a gravação.
- Registrar quais recursos do Pi foram testados na prática.
