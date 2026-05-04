# Como instalar o PaperClip limpo no Ubuntu para o Projeto Robô Frank

## Objetivo

Este guia mostra como instalar o PaperClip do zero em um ambiente local Ubuntu, sem Docker, para organizar o fluxo operacional do Projeto Robô Frank / Frankenstein de IAs.

A proposta é usar o PaperClip como camada de organização do trabalho, enquanto o Robô Frank atua como CEO/orquestrador principal e o Hermes executa por baixo.

## Arquitetura usada neste guia

```text
Usuário
-> PaperClip
-> Robô Frank CEO
-> especialistas funcionais
-> Hermes
-> ferramentas e integrações
-> Obsidian / ByteRover
```

## Papéis no projeto

```text
PaperClip = organiza empresa, tarefas e fluxo operacional
Robô Frank = agente principal, CEO e orquestrador
Especialistas funcionais = apoiam o Robô Frank por função
Hermes = executor por baixo
Obsidian = documentação humana
ByteRover = memória operacional curta
Codex/OpenCode = apoio técnico para scripts, código e documentação
Gemini API / ComfyUI = ferramentas de imagem
Trello = opcional, apenas sob pedido direto
CCGram = futuro/opcional
```

## O que este guia não faz

Este guia não instala PaperClip com Docker.

Este guia não expõe o PaperClip na internet.

Este guia não configura VPS.

Este guia não configura Trello automaticamente.

Este guia não cria agente chamado Clipper.

Este guia não mexe no Hermes real, exceto quando for necessário documentar a relação entre PaperClip e Hermes.

## Portas locais usadas neste ambiente

No ambiente usado como referência:

```text
SearXNG:
http://localhost:8080

Open WebUI:
http://localhost:8081

PaperClip:
http://localhost:3100
```

A porta `8080` não deve ser assumida como Open WebUI neste ambiente, porque já está sendo usada pelo SearXNG.

A porta padrão esperada para o PaperClip local é `3100`.

## Antes de começar

Abra um terminal no Ubuntu.

Este guia assume que o projeto principal está em:

```text
~/frankenstein-ias
```

Se a pasta ainda não existir, crie:

```bash
mkdir -p ~/frankenstein-ias
```

Entre na pasta:

```bash
cd ~/frankenstein-ias
```

## Etapa 1 - Conferir Node, npm e npx

Rode:

```bash
node -v
```

Depois:

```bash
npm -v
```

Depois:

```bash
npx --version
```

O PaperClip usa Node.js. A documentação atual do projeto indica Node.js 20+ como requisito para uso/desenvolvimento local.

Se `node`, `npm` ou `npx` não existirem, instale o Node.js antes de continuar.

## Etapa 2 - Conferir portas locais

Antes de instalar, confira as portas importantes:

```bash
ss -ltnp | grep -E "3100|8080|8081|11434"
```

Interpretação esperada:

```text
8080 = SearXNG, se estiver rodando
8081 = Open WebUI, se estiver rodando
11434 = Ollama, se estiver rodando
3100 = PaperClip, se já estiver rodando
```

Se a porta `3100` não aparecer, ela provavelmente está livre para o PaperClip.

## Etapa 3 - Instalar e fazer onboard do PaperClip

Dentro da pasta do projeto:

```bash
cd ~/frankenstein-ias
```

Rode:

```bash
npx paperclipai onboard --yes
```

Esse é o comando de onboarding rápido do PaperClip.

Ele prepara a instalação local e inicia o fluxo inicial de configuração.

## Etapa 4 - Abrir o PaperClip

Depois que o comando terminar, abra no navegador:

```text
http://localhost:3100
```

Ou use o terminal:

```bash
xdg-open http://localhost:3100
```

Se não abrir, confira se a porta `3100` está ativa:

```bash
ss -ltnp | grep 3100
```

Também é possível testar com:

```bash
curl -I http://127.0.0.1:3100
```

## Etapa 5 - Se o PaperClip não ficar rodando

Se o onboarding terminar, mas o servidor não estiver ativo, rode:

```bash
cd ~/frankenstein-ias
```

Depois:

```bash
npx paperclipai run
```

Em seguida, abra novamente:

```text
http://localhost:3100
```

Resumo didático:

```text
onboard = prepara/configura
run = inicia o servidor
```

## Etapa 6 - Verificar arquivos de configuração

Depois da instalação, verifique se existe configuração local:

```bash
ls -la ~/.paperclip
```

Para listar alguns arquivos:

```bash
find ~/.paperclip -maxdepth 4 -type f | sort | head -80
```

Atenção: antes de mostrar qualquer arquivo em vídeo, verifique se há tokens, secrets, chaves de API, JWT secrets ou credenciais.

Não mostre arquivos sensíveis em gravação.

## Etapa 7 - Criar a empresa/projeto no PaperClip

Na interface do PaperClip, crie uma empresa/projeto com um nome coerente.

Exemplo:

```text
Frankenstein de IAs
```

Missão sugerida:

```text
Organizar o ecossistema do Projeto Robô Frank para produção de conteúdo, documentação, automação local, memória operacional e integração segura entre ferramentas de IA.
```

## Etapa 8 - Criar o agente principal

Crie apenas um agente principal com nome próprio:

```text
Robô Frank
```

Papel sugerido:

```text
CEO / Orquestrador principal
```

Descrição sugerida:

```text
Robô Frank é o agente principal do Projeto Frankenstein de IAs. Ele interpreta pedidos, organiza prioridades, chama especialistas funcionais quando necessário, consolida resultados e mantém Denise no controle das decisões importantes.
```

Regra importante:

```text
Não criar Clipper.
Não criar outro agente principal concorrente.
```

## Etapa 9 - Especialistas funcionais

Os especialistas de conteúdo devem ser tratados como funções subordinadas ao Robô Frank.

Núcleo ativo sugerido:

```text
strategist
script_writer
hook_specialist
thumbnail_agent
publisher
community_manager
persona_guardian
```

Esses especialistas não precisam ser todos criados imediatamente na interface.

A recomendação inicial é começar com o Robô Frank e só adicionar especialistas conforme o fluxo ficar estável.

## Etapa 10 - Relação com Hermes

O Hermes deve ser tratado como executor por baixo.

Regra conceitual:

```text
PaperClip organiza.
Robô Frank decide.
Hermes executa.
```

O Hermes não é a entrada principal do fluxo.

O Hermes não substitui o Robô Frank.

O Hermes só deve executar comandos, scripts e integrações quando isso for necessário e autorizado.

## Etapa 11 - Relação com imagem

Codex/OpenCode não geram imagens diretamente.

Eles podem criar ou corrigir scripts.

Quem gera imagem é uma ferramenta visual, como:

```text
Gemini API
ComfyUI
```

Fluxo correto de imagem:

```text
Pedido visual
-> PaperClip organiza
-> Robô Frank interpreta
-> thumbnail_agent cria briefing visual
-> Hermes executa ferramenta
-> Gemini API ou ComfyUI gera imagem
-> usuário aprova
```

## Etapa 12 - Relação com Trello

Trello é opcional.

Não criar cartões automaticamente.

Não mover cartões automaticamente.

Não consultar Trello automaticamente.

Usar Trello apenas quando houver pedido direto, por exemplo:

```text
Coloque isso no Trello.
Crie um cartão no Trello.
Atualize essa tarefa no Trello.
```

## Etapa 13 - Relação com CCGram

CCGram é futuro/opcional.

Não tratar CCGram como parte obrigatória do núcleo atual.

Se for usado depois, deve ter regras próprias de segurança, permissão e limite de uso.

## Etapa 14 - Regras de segurança

Antes de qualquer ação sensível, explicar o risco e pedir confirmação.

Ações sensíveis incluem:

```text
apagar arquivos
sobrescrever documentos importantes
alterar .env
manipular tokens
chamar API paga
publicar conteúdo
enviar mensagens externas
criar ou mover cartões no Trello
reinstalar ferramentas
alterar configurações principais
alterar memória permanente
```

## Etapa 15 - Teste inicial simples

Depois de configurar o PaperClip, faça um teste simples.

Prompt sugerido:

```text
Robô Frank, confirme se você entendeu a arquitetura atual do projeto. Explique em poucas linhas o papel do PaperClip, do Robô Frank, dos especialistas funcionais, do Hermes, do Obsidian e do ByteRover. Não execute nenhuma ação. Apenas explique.
```

Resposta esperada:

```text
PaperClip organiza.
Robô Frank decide.
Especialistas apoiam.
Hermes executa.
Obsidian documenta.
ByteRover lembra o curto prazo.
Usuário aprova.
```

## Etapa 16 - Teste com tarefa de conteúdo

Prompt sugerido:

```text
Robô Frank, crie uma ideia de vídeo curto explicando por que o PaperClip organiza o trabalho, mas o Robô Frank continua sendo o agente principal do projeto. Não publique nada. Apenas entregue a ideia, o gancho e um roteiro curto.
```

Resultado esperado:

```text
ideia
gancho
roteiro curto
sem publicação automática
sem Trello automático
sem comandos
```

## Etapa 17 - Teste com imagem

Prompt sugerido:

```text
Robô Frank, crie um briefing de thumbnail para um vídeo sobre a instalação limpa do PaperClip no Projeto Robô Frank. Não gere imagem ainda. Apenas crie o briefing visual.
```

Resultado esperado:

```text
briefing visual
elementos principais
texto sugerido
estilo
observação de que a geração real depende de Gemini API ou ComfyUI
```

## Etapa 18 - Comandos úteis

Verificar se PaperClip está rodando:

```bash
ss -ltnp | grep 3100
```

Abrir PaperClip:

```bash
xdg-open http://localhost:3100
```

Rodar PaperClip:

```bash
cd ~/frankenstein-ias
npx paperclipai run
```

Repetir onboarding, se necessário:

```bash
cd ~/frankenstein-ias
npx paperclipai onboard --yes
```

Atenção: repetir onboarding pode sobrescrever ou reconstruir partes da configuração. Use com cuidado depois que o ambiente estiver configurado.

## Etapa 19 - Diagnóstico rápido

Se `localhost:3100` não abrir:

```bash
ss -ltnp | grep 3100
```

Se não houver nada na porta `3100`, tente iniciar:

```bash
cd ~/frankenstein-ias
npx paperclipai run
```

Se aparecer erro de Node:

```bash
node -v
npm -v
npx --version
```

Se aparecer erro de porta ocupada:

```bash
ss -ltnp | grep 3100
```

Se aparecer erro de permissão, copie a mensagem exata antes de tentar comandos destrutivos.

## Etapa 20 - O que documentar depois da instalação

Registrar no vault ou documentação do projeto:

```text
data da instalação
versão do Node
comando usado
porta do PaperClip
nome da empresa criada
nome do agente principal
regras de segurança definidas
problemas encontrados
correções aplicadas
```

## Modelo de registro

```md
# Registro de Instalação do PaperClip

Data:

Sistema:

Node:

npm:

npx:

Comando usado:

Porta:

URL local:

Empresa criada:

Agente principal:

Observações:

Problemas encontrados:

Correções aplicadas:
```

## Frase para explicar no vídeo

```text
Neste fluxo, o PaperClip não substitui o Robô Frank. O PaperClip organiza a empresa e as tarefas. O Robô Frank é o CEO com quem eu interajo. Os especialistas ajudam por função. O Hermes executa por baixo. E as decisões importantes continuam passando por revisão humana.
```

## Referências

PaperClip - site oficial:

https://paperclip.ing/

PaperClip - repositório oficial:

https://github.com/paperclipai/paperclip
