# Como instalar e testar o Claude Code Router no Windows

## Objetivo

Instalar o Claude Code Router no Windows, abrir a interface visual, configurar provedores e iniciar o Claude Code usando o roteador.

O Claude Code Router permite encaminhar as solicitações do Claude Code para diferentes modelos e provedores compatíveis.

## Fontes oficiais consultadas

- Site do Claude Code Router: https://ccrdesk.top/
- Claude Code Router no GitHub: https://github.com/musistudio/claude-code-router
- Pacote oficial no npm: https://www.npmjs.com/package/@musistudio/claude-code-router
- Documentação oficial do Claude Code: https://docs.anthropic.com/en/docs/claude-code/getting-started

## Ambiente do guia

- Sistema operacional: Windows 10 ou Windows 11
- Terminal: PowerShell
- Node.js: versão 22 ou superior
- Gerenciador de pacotes: npm
- Data da verificação da documentação: 22 de julho de 2026

> O teste prático ainda deve registrar a versão exata do Windows, do Node.js, do Claude Code e do Claude Code Router usada na gravação.

## Pré-requisitos

O Claude Code Router distribuído pelo npm exige Node.js 22 ou superior.

O Claude Code também precisa estar instalado quando o perfil criado no Router for abrir o agente localmente.

Para executar o Claude Code diretamente no Windows, a documentação da Anthropic recomenda ter o Git for Windows instalado.

## Verificar o Node.js e o npm

Abra o PowerShell e execute:

```powershell
node --version
npm --version
```

O Node.js precisa mostrar a versão 22 ou superior, por exemplo:

```text
v22.x.x
```

Caso o comando `node` não seja reconhecido ou a versão seja inferior à 22, atualize o Node.js antes de continuar.

Download oficial:

https://nodejs.org/

Depois da instalação, feche e abra novamente o PowerShell.

## Verificar o Git for Windows

```powershell
git --version
```

Se o comando não for reconhecido, instale o Git for Windows:

https://git-scm.com/download/win

Depois, feche e abra novamente o PowerShell.

## Instalar o Claude Code

Verifique primeiro se o Claude Code já está instalado:

```powershell
claude --version
```

Caso não esteja instalado:

```powershell
npm install -g @anthropic-ai/claude-code
```

Verifique novamente:

```powershell
claude --version
claude doctor
```

Se o Claude Code não localizar o Git Bash automaticamente, configure o caminho no PowerShell:

```powershell
$env:CLAUDE_CODE_GIT_BASH_PATH="C:\Program Files\Git\bin\bash.exe"
```

Essa variável vale apenas para a sessão atual do PowerShell.

Para gravar a variável no perfil do usuário:

```powershell
[Environment]::SetEnvironmentVariable(
  "CLAUDE_CODE_GIT_BASH_PATH",
  "C:\Program Files\Git\bin\bash.exe",
  "User"
)
```

Feche e abra novamente o PowerShell depois desse comando.

## Instalar o Claude Code Router

```powershell
npm install -g @musistudio/claude-code-router
```

## Verificar a instalação

```powershell
ccr --version
ccr --help
```

O comando `ccr --help` deve mostrar os comandos disponíveis na versão instalada.

## Abrir a interface visual

```powershell
ccr ui
```

O comando inicia ou reutiliza o serviço local e abre a interface de gerenciamento no navegador.

Os endereços padrão são:

```text
Interface de gerenciamento: http://127.0.0.1:3458
Gateway local: http://127.0.0.1:3456
```

Se uma porta estiver ocupada, o Router pode usar outra. Considere sempre o endereço mostrado no PowerShell.

## Configuração inicial na interface

Na interface visual:

- adicione um provedor;
- informe a chave da API do provedor;
- adicione pelo menos um modelo;
- crie uma chave de cliente do CCR em `API Keys`;
- escolha o modelo padrão ou configure as rotas;
- confirme em `Server` que o gateway está ativo;
- crie e habilite um perfil em `Agent Config` para o Claude Code.

A chave da API do provedor e a chave de cliente criada pelo CCR são credenciais diferentes.

Não mostre nenhuma dessas chaves durante a gravação.

## Abrir um perfil do Claude Code

Na versão atual do pacote npm, crie e habilite um perfil em `Agent Config`.

Depois, abra pelo nome:

```powershell
ccr "Nome do perfil"
```

Exemplo:

```powershell
ccr "Claude - MiniMax"
```

Também é possível indicar explicitamente a interface de linha de comando:

```powershell
ccr "Claude - MiniMax" cli
```

Argumentos específicos do Claude Code devem ser colocados depois de `--`:

```powershell
ccr "Claude - MiniMax" cli -- --help
```

## Comandos de serviço

Abrir a interface:

```powershell
ccr ui
```

Iniciar o serviço em segundo plano:

```powershell
ccr start
```

Parar o serviço em segundo plano:

```powershell
ccr stop
```

Executar em primeiro plano para acompanhar os erros:

```powershell
ccr serve
```

O modo `serve` é o mais útil para diagnóstico, pois mantém os registros visíveis no terminal.

## Se a versão instalada ainda oferecer os comandos antigos

Algumas páginas e versões anteriores do projeto documentam:

```powershell
ccr model
ccr code
```

Use esses comandos apenas se eles aparecerem no resultado de:

```powershell
ccr --help
```

A versão atual do pacote npm também utiliza perfis de agente iniciados com:

```powershell
ccr "Nome do perfil"
```

## Teste rápido

Crie uma pasta separada para o teste:

```powershell
New-Item -ItemType Directory -Path "$HOME\Documents\teste-claude-code-router" -Force
Set-Location "$HOME\Documents\teste-claude-code-router"
```

Crie um arquivo simples:

```powershell
@'
def somar(a, b):
    return a + b
'@ | Set-Content -Encoding UTF8 app.py
```

Abra o perfil configurado:

```powershell
ccr "Nome do perfil"
```

No Claude Code, use um pedido semelhante a:

```text
Leia o arquivo app.py, explique o que ele faz e crie testes para a função somar. Antes de alterar qualquer arquivo, mostre o plano.
```

Durante o teste, observe:

- se o modelo lê o arquivo corretamente;
- se o Claude Code continua usando as ferramentas;
- se o provedor escolhido aparece nos registros do Router;
- se as alterações exigem confirmação;
- se há erros de compatibilidade com ferramentas ou respostas estruturadas.

## Local dos arquivos no Windows

A configuração atual do Claude Code Router fica normalmente em:

```text
%APPDATA%\claude-code-router
```

Arquivos e pastas importantes podem incluir:

```text
config.sqlite
app-data\
service.json
gateway.config.json
profiles\
bin\
```

Não edite ou copie o banco SQLite enquanto o CCR estiver em execução.

Para fazer backup, pare o serviço antes:

```powershell
ccr stop
```

## Atualizar

```powershell
npm install -g @musistudio/claude-code-router@latest
```

Depois, confira:

```powershell
ccr --version
ccr --help
```

## Remover

```powershell
ccr stop
npm uninstall -g @musistudio/claude-code-router
```

A remoção do pacote npm não apaga automaticamente as configurações e os bancos locais do CCR.

Para localizar a pasta de configuração:

```powershell
explorer "$env:APPDATA\claude-code-router"
```

Não exclua essa pasta antes de salvar qualquer configuração que deseje manter.

## Solução de problemas

### O comando `ccr` não foi encontrado

Confira:

```powershell
node --version
npm prefix -g
```

Feche e abra novamente o PowerShell depois da instalação.

Verifique se a pasta global do npm está no `PATH` do Windows.

### O comando `claude` não foi encontrado

```powershell
npm install -g @anthropic-ai/claude-code
claude --version
```

Feche e abra novamente o terminal se necessário.

### O Claude Code não encontra o Git Bash

```powershell
$env:CLAUDE_CODE_GIT_BASH_PATH="C:\Program Files\Git\bin\bash.exe"
claude doctor
```

Confirme se o arquivo existe:

```powershell
Test-Path "C:\Program Files\Git\bin\bash.exe"
```

### A interface abriu, mas o gateway não funciona

Confirme na interface se existem:

- um provedor configurado;
- pelo menos um modelo;
- uma chave de cliente do CCR;
- um modelo padrão ou rota válida;
- gateway ativo em `Server`.

Execute em primeiro plano para ver os erros:

```powershell
ccr stop
ccr serve
```

### A porta padrão está ocupada

Use o endereço exibido pelo Router ou reinicie com outra porta de gerenciamento:

```powershell
ccr stop
ccr start --host 127.0.0.1 --port 3459
```

### O serviço continua usando opções antigas

```powershell
ccr stop
ccr start --host 127.0.0.1 --port 3458
```

### O perfil não foi encontrado

Confirme se o perfil está salvo e habilitado em `Agent Config`.

Nomes são aceitos sem diferenciação entre maiúsculas e minúsculas, mas nomes ambíguos podem exigir o ID do perfil.

## Segurança

- não exponha as chaves durante a gravação;
- não publique a URL autenticada da interface de gerenciamento;
- mantenha o host em `127.0.0.1` para uso local;
- revise comandos antes de permitir sua execução;
- teste primeiro em uma pasta separada;
- faça backup antes de usar em projetos importantes;
- não envie a pasta `%APPDATA%\claude-code-router` para o GitHub.

A URL autenticada da interface pode conter um token chamado `ccr_web_token`. Trate essa URL como uma senha.

## O que registrar durante a gravação

- versão do Windows;
- versão do Node.js;
- versão do npm;
- versão do Claude Code;
- versão do Claude Code Router;
- provedor e modelo testados;
- comandos que realmente apareceram em `ccr --help`;
- erros encontrados;
- resultado de cada teste;
- custo ou consumo observado no provedor.

## O que ficou pendente

- registrar as versões exatas usadas no vídeo;
- confirmar o fluxo visual da interface na máquina de teste;
- configurar o primeiro provedor;
- verificar se `ccr model` e `ccr code` continuam disponíveis na versão instalada;
- registrar erros e ajustes específicos encontrados durante o teste real.
