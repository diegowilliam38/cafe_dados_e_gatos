# Como instalar o PaperClip limpo no Ubuntu

## Objetivo

Este guia mostra como instalar o PaperClip do zero em um ambiente local Ubuntu, sem Docker.

O foco é fazer uma instalação simples, local e reproduzível, usando o comando de onboarding rápido do PaperClip.

## O que é o PaperClip

PaperClip é uma ferramenta open source para orquestrar equipes de agentes de IA a partir de uma interface local.

Ele permite criar uma organização, definir objetivos, configurar agentes e acompanhar atividades em um painel.

## O que este guia cobre

Este guia cobre:

- verificação de Node.js, npm e npx;
- instalação/onboarding local;
- abertura da interface web;
- comandos básicos para iniciar novamente;
- diagnóstico de porta;
- cuidados com arquivos sensíveis.

## O que este guia não cobre

Este guia não cobre:

- instalação com Docker;
- deploy em VPS;
- exposição pública na internet;
- configuração avançada de rede;
- integração com ferramentas externas;
- criação avançada de agentes;
- automações de produção.

## Requisitos

Antes de começar, é necessário ter:

```text
Ubuntu ou distribuição Linux compatível
Node.js 20 ou superior
npm / npx disponíveis no terminal
acesso ao terminal
navegador web
```

A documentação atual do PaperClip indica Node.js 20+ e pnpm 9.15+ como requisitos para uso/desenvolvimento local.

## Porta padrão

A interface local do PaperClip costuma ficar disponível em:

```text
http://localhost:3100
```

ou:

```text
http://127.0.0.1:3100
```

## Etapa 1 - Abrir o terminal

Abra um terminal no Ubuntu.

Escolha uma pasta de trabalho.

Exemplo:

```bash
cd ~
```

Opcionalmente, crie uma pasta própria para testes:

```bash
mkdir -p ~/paperclip-teste
```

Entre na pasta:

```bash
cd ~/paperclip-teste
```

## Etapa 2 - Conferir Node.js

Rode:

```bash
node -v
```

Exemplo de saída esperada:

```text
v20.x.x
```

ou superior.

Se o comando não existir ou a versão for antiga, instale ou atualize o Node.js antes de continuar.

## Etapa 3 - Conferir npm

Rode:

```bash
npm -v
```

Se aparecer uma versão, o npm está disponível.

## Etapa 4 - Conferir npx

Rode:

```bash
npx --version
```

Se aparecer uma versão, o `npx` está disponível.

## Etapa 5 - Conferir se a porta 3100 está livre

Antes de iniciar, confira se já existe algo usando a porta `3100`:

```bash
ss -ltnp | grep 3100
```

Se não aparecer nada, a porta provavelmente está livre.

Se aparecer algum processo, a porta já está ocupada e será necessário identificar o serviço antes de continuar.

## Etapa 6 - Rodar o onboarding do PaperClip

Na pasta escolhida, rode:

```bash
npx paperclipai onboard --yes
```

Esse comando baixa/executa a CLI via `npx`, prepara a instalação local e inicia o processo de onboarding.

Segundo a documentação oficial, esse quickstart usa modo local em loopback por padrão para a primeira execução.

## Etapa 7 - Abrir a interface

Depois que o onboarding terminar, abra no navegador:

```text
http://localhost:3100
```

ou:

```text
http://127.0.0.1:3100
```

Também é possível abrir pelo terminal:

```bash
xdg-open http://localhost:3100
```

## Etapa 8 - Confirmar se o servidor está rodando

Se a página não abrir, confira a porta:

```bash
ss -ltnp | grep 3100
```

Também é possível testar com:

```bash
curl -I http://127.0.0.1:3100
```

Se houver resposta HTTP, o servidor está ativo.

## Etapa 9 - Iniciar o PaperClip novamente depois

Se o onboarding já foi feito e o PaperClip não estiver rodando, tente iniciar com:

```bash
npx paperclipai run
```

Depois abra:

```text
http://localhost:3100
```

Resumo:

```text
onboard = prepara/configura a instalação local
run = inicia o servidor depois da configuração
```

## Etapa 10 - Verificar configurações locais

Depois da instalação, confira se existe pasta de configuração:

```bash
ls -la ~/.paperclip
```

Para listar arquivos principais:

```bash
find ~/.paperclip -maxdepth 4 -type f | sort | head -80
```

Atenção: antes de mostrar arquivos de configuração em vídeo, aula, print ou tutorial, verifique se há dados sensíveis.

Não exponha:

```text
tokens
API keys
JWT secrets
master keys
credenciais
arquivos .env
segredos de configuração
```

## Etapa 11 - Criar primeira empresa ou organização

Na interface web, crie a primeira empresa/organização.

Exemplo genérico:

```text
Minha Empresa de IA
```

Defina um objetivo claro.

Exemplo:

```text
Organizar tarefas, objetivos e agentes de IA para apoiar projetos de conteúdo, pesquisa, automação e documentação.
```

## Etapa 12 - Criar primeiro agente

Crie um agente principal para testar o fluxo.

Exemplo genérico:

```text
CEO Agent
```

Papel sugerido:

```text
Coordenar objetivos, organizar tarefas e acompanhar o trabalho dos demais agentes.
```

Para um primeiro teste, evite criar muitos agentes de uma vez.

Comece simples.

## Etapa 13 - Fazer um teste simples

Na interface, envie um pedido simples.

Exemplo:

```text
Explique em poucas linhas qual é o objetivo desta empresa e quais seriam os próximos passos para organizar o trabalho.
```

O objetivo do primeiro teste é verificar se:

```text
a interface abre
o agente responde
o servidor está funcionando
as tarefas aparecem no painel
não há erro de porta
não há erro de configuração
```

## Etapa 14 - Diagnóstico rápido

### Se localhost:3100 não abrir

Verifique se a porta está ativa:

```bash
ss -ltnp | grep 3100
```

### Se nada estiver rodando na porta 3100

Tente iniciar:

```bash
npx paperclipai run
```

### Se aparecer erro de Node

Confira:

```bash
node -v
npm -v
npx --version
```

### Se aparecer erro de permissão

Copie a mensagem exata.

Não rode comandos destrutivos sem entender o erro.

### Se aparecer erro de porta ocupada

Veja qual processo está usando a porta:

```bash
ss -ltnp | grep 3100
```

## Etapa 15 - Comandos úteis

### Conferir versão do Node

```bash
node -v
```

### Conferir npm

```bash
npm -v
```

### Conferir npx

```bash
npx --version
```

### Rodar onboarding

```bash
npx paperclipai onboard --yes
```

### Iniciar PaperClip

```bash
npx paperclipai run
```

### Conferir porta 3100

```bash
ss -ltnp | grep 3100
```

### Abrir no navegador

```bash
xdg-open http://localhost:3100
```

### Conferir pasta local de configuração

```bash
ls -la ~/.paperclip
```

## Etapa 16 - Registro da instalação

É recomendado registrar:

```text
data da instalação
sistema operacional
versão do Node.js
versão do npm
versão do npx
comando usado
porta usada
URL local
problemas encontrados
correções aplicadas
observações importantes
```

Modelo:

```md
# Registro de Instalação do PaperClip

Data:

Sistema operacional:

Node.js:

npm:

npx:

Comando usado:

Porta:

URL local:

Problemas encontrados:

Correções aplicadas:

Observações:
```

## Cuidados importantes

Não exponha a interface do PaperClip diretamente na internet sem entender autenticação, bind de rede, firewall e riscos de segurança.

Para o primeiro uso, prefira rodar localmente em:

```text
localhost
127.0.0.1
```

Evite publicar prints ou gravações mostrando arquivos de configuração sensíveis.

## Fluxo mínimo recomendado

```bash
cd ~
mkdir -p ~/paperclip-teste
cd ~/paperclip-teste
node -v
npm -v
npx --version
ss -ltnp | grep 3100
npx paperclipai onboard --yes
xdg-open http://localhost:3100
```

Se precisar iniciar depois:

```bash
cd ~/paperclip-teste
npx paperclipai run
```

## Referências

Site oficial:

https://paperclip.ing/

Repositório oficial:

https://github.com/paperclipai/paperclip
