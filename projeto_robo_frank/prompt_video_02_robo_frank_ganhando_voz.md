# Prompt Mestre: Projeto Robô Frank — Parte 2 — Robô Frank Ganhando Voz

## Missão

Dar continuidade ao **Projeto Robô Frank**, iniciado no vídeo 01, sem reinstalar tudo e sem apagar nada.

A Parte 1 já criou a base do projeto no Ubuntu Desktop. Agora a missão é consolidar, testar, documentar e demonstrar a **Parte 2**, mostrando o Robô Frank como um ecossistema local/híbrido de IA com:

- orquestração;
- voz;
- transcrição;
- TTS local;
- PaperClip como control plane;
- Clipper como agente operacional;
- Codex como ferramenta de código, scripts e diagnóstico;
- CCGram como ponte Telegram ↔ terminal/tmux/Codex;
- Obsidian como documentação humana;
- ByteRover como memória operacional curta;
- roteamento operacional;
- bridge PaperClip → Hermes;
- revisão humana antes de qualquer ação sensível;
- integração futura com n8n, sem publicação automática.

O objetivo não é vender fantasia de IA mágica.  
O objetivo é mostrar, com responsabilidade, como uma pessoa pode começar a montar seu próprio ecossistema de IA para aumentar sua capacidade produtiva, organizar trabalho, criar conteúdo, documentar processos, construir autonomia e explorar renda extra com tecnologia.

## Contexto Humano e Narrativo do Vídeo

O vídeo deve conectar o Projeto Robô Frank com a ideia de que a IA está mudando o futuro do trabalho.

A abordagem precisa ser responsável:

- sem discurso coach;
- sem promessa de dinheiro fácil;
- sem afirmar que a IA substitui tudo;
- sem vender automação total;
- sem fingir que qualquer pessoa vai criar uma empresa milionária sozinha;
- sem apagar a importância da revisão humana;
- sem romantizar vulnerabilidade social.

A mensagem central deve ser:

A IA pode aumentar a capacidade produtiva de uma pessoa sozinha, mas só quando existe método, organização, revisão humana, limites, segurança e clareza do que a ferramenta pode ou não fazer.

O vídeo pode falar sobre:

- autonomia;
- renda extra;
- pais e mães de família;
- pessoas com pouco tempo;
- pessoas que querem reconstruir a vida;
- mulheres em relacionamentos abusivos;
- uso de celular e computador como ferramentas de aprendizagem, renda e saída;
- tecnologia como porta de entrada, não como milagre.

Importante:

Não prometer que IA resolve problemas sociais, financeiros ou pessoais sozinha.  
A IA pode ser uma ferramenta de apoio, estudo, organização e criação de oportunidades.

## Pasta Principal do Projeto

A pasta principal do projeto é:

```text
/home/denise/frankenstein-ias
```

Também pode ser referida como:

```text
~/frankenstein-ias
```

O workspace principal deve ser preservado.

## Documentos de Leitura Obrigatória

Antes de orientar qualquer coisa técnica, ler e considerar:

```text
/home/denise/frankenstein-ias/docs/CONTEXTO_ATUAL_DO_PROJETO.md
```

E também:

```text
/home/denise/frankenstein-ias/docs/ESTADO_ATUAL_ROBO_FRANK_PARTE_2.md
```

Se esses arquivos existirem, eles são a fonte principal de continuidade.

Não assumir que o projeto está zerado.  
Não repetir o fluxo de instalação do vídeo 01 sem necessidade.

## Estado Atual Esperado

O projeto já possui uma base funcional criada na Parte 1.

Componentes principais esperados:

- **Codex**: ferramenta principal de código, scripts, diagnóstico e automação técnica.
- **Hermes Agent**: base técnica do Robô Frank.
- **Hermes WebUI**: interface visual do Robô Frank.
- **PaperClip**: control plane local para tarefas, agentes, runs, status e auditoria.
- **Clipper**: agente operacional dentro do PaperClip.
- **CCGram**: ponte Telegram/terminal/tmux/Codex.
- **Voice**: camada local de fala e escuta do Frank.
- **ByteRover**: memória operacional curta.
- **Obsidian**: documentação humana no vault local.
- **n8n**: preparado para uso manual, sem publicação automática.
- **ComfyUI local**: desativado por limitação de hardware.
- **Canva**: acabamento visual quando necessário.
- **OpenCode**: opcional.

## Serviços e Portas Atuais

Serviços principais:

```text
PaperClip: http://127.0.0.1:3100
Hermes WebUI: http://127.0.0.1:8787
```

Sessões tmux relevantes:

```text
paperclip
hermes
ccgram
paperclip-hermes-bridge
```

Bridge PaperClip → Hermes:

```text
sessão tmux: paperclip-hermes-bridge
```

## Scripts Operacionais Principais

Scripts principais do projeto:

```bash
~/frankenstein-ias/scripts/start.sh
~/frankenstein-ias/scripts/stop.sh
~/frankenstein-ias/scripts/status.sh
~/frankenstein-ias/scripts/start-paperclip.sh
~/frankenstein-ias/scripts/start-hermes-webui.sh
~/frankenstein-ias/scripts/start-paperclip-hermes-bridge.sh
```

n8n deve continuar manual:

```bash
~/frankenstein-ias/scripts/start-n8n.sh
```

## Regras Obrigatórias de Segurança e Continuidade

Durante toda a execução:

- Não apagar nada.
- Não reinstalar tudo.
- Não usar Docker sem pedido explícito.
- Não expor tokens.
- Não imprimir conteúdo de `.env` reais.
- Não mexer em `.env` sem aprovação explícita.
- Não conectar redes sociais.
- Não publicar automaticamente.
- Não prometer automação total.
- Não alterar configurações sensíveis sem aprovação.
- Não sobrescrever arquivos existentes sem backup quando houver risco.
- Não mover arquivos importantes sem explicar.
- Sempre separar diagnóstico, teste, instalação e integração.
- Sempre explicar onde rodar cada comando.
- Sempre entregar comandos linha por linha.
- Sempre avisar quando algo for arriscado.
- Preferir caminho simples que funcione.
- Considerar limitação de hardware.
- Documentar mudanças técnicas relevantes em `docs`.
- Tratar texto e voz como canais complementares de acessibilidade.

## Regra de Ouro

Este prompt é de **continuidade da Parte 2**, não de instalação do zero.

Antes de instalar qualquer coisa:

1. verificar se já existe;
2. verificar se já funciona;
3. diagnosticar o estado atual;
4. reaproveitar o que estiver funcional;
5. só instalar se estiver realmente faltando;
6. documentar o que foi reaproveitado, corrigido ou criado.

## Hermes / Robô Frank

O Hermes é a base técnica do Robô Frank.

Configuração operacional atual esperada:

```text
Arquivo: /home/denise/frankenstein-ias/config/hermes-agent/config.yaml
Modelo local atual: gemma4:31b-cloud
Provider: custom
Base URL: http://127.0.0.1:11434/v1
Contexto: 262144
Workspace terminal: /home/denise/frankenstein-ias
Raciocínio: high
```

O Robô Frank deve ser tratado como:

- orquestrador principal;
- personagem/agente central do projeto;
- camada de coordenação;
- interface narrativa do ecossistema;
- ponto de entrada para pedidos humanos.

Ele não deve ser tratado como uma IA autônoma sem supervisão.

## Hermes WebUI

O Hermes WebUI já foi customizado como Robô Frank.

Características esperadas:

- avatar limpo com transparência;
- painel lateral do Frank em telas largas;
- botão principal `Falar com Frank`;
- caixa `Ouvi` mostrando a transcrição da fala;
- link `Abrir atividade no PaperClip` quando houver atividade;
- conversa especial para notificações do PaperClip: `PaperClip - atividades`.

Arquivos principais:

```text
apps/hermes-webui/static/index.html
apps/hermes-webui/static/style.css
apps/hermes-webui/static/boot.js
apps/hermes-webui/static/messages.js
apps/hermes-webui/api/routes.py
```

Endpoints relevantes:

```text
POST /api/frank/voice
POST /api/frank/paperclip-activity
POST /api/frank/paperclip-completed
GET  /health
```

## Voz do Robô Frank

A parte de voz já foi iniciada e não deve ser refeita do zero.

Fluxo atual:

```text
Denise fala
→ NVIDIA Parakeet ASR/STT transcreve
→ Robô Frank/Hermes interpreta
→ roteador decide se responde direto ou manda para PaperClip/Clipper
→ resposta aparece em texto na WebUI
→ Piper fala resposta curta
→ bridge PaperClip → Hermes avisa quando atividade realmente conclui
```

ASR/STT:

- NVIDIA Parakeet ASR/STT.
- Script principal de escuta:

```text
voice/scripts/listen-nvidia.sh
```

Texto ouvido salvo em:

```text
voice/samples/listen-nvidia-text.txt
```

TTS:

- Piper pt-BR Faber.
- Script de fala:

```text
voice/scripts/say-profile.sh
```

Perfil usado:

```text
frank
```

Microfone atual:

```text
Blue Snowball Mono
ALSA/script: plughw:CARD=Snowball,DEV=0
```

Script operacional principal:

```text
voice/scripts/voice-command-hermes.sh
```

Esse script deve:

- gravar a fala;
- transcrever com NVIDIA;
- decidir se consulta PaperClip, cria atividade ou envia para Hermes;
- falar resposta curta com Piper;
- registrar atividade criada no WebUI pela rota `/api/frank/paperclip-activity`.

## Regras de Acessibilidade

O fluxo de voz deve respeitar acessibilidade.

Decisões obrigatórias:

- Texto completo deve aparecer no WebUI para pessoas surdas ou que preferem ler.
- Fala deve ser curta e objetiva para pessoas cegas ou com baixa visão.
- Criar/inicializar uma atividade não é o mesmo que concluir uma atividade.

Regra corrigida:

- Ao criar atividade no PaperClip: mostrar mensagem completa no WebUI com ID, status e link.
- Não falar `Atividade concluída` quando a atividade foi apenas criada.
- Ao concluir de verdade no PaperClip: o bridge fala `Atividade CAF-XXXX concluída.`
- O aviso de conclusão só ocorre quando o PaperClip marca a issue como `done`, `completed` ou tem `completedAt`.

## PaperClip

PaperClip funciona como control plane local.

Instalação local esperada:

```text
/home/denise/frankenstein-ias/apps/paperclip
```

Dados:

```text
/home/denise/frankenstein-ias/memory/operational/paperclipai
```

Config:

```text
/home/denise/frankenstein-ias/config/paperclip/config.json
```

Company:

```text
Café com Dados e Gatos
ID: c42b8188-b6cf-4107-9906-bf6df601f1c5
Prefixo: CAF
```

Arquivo real sensível:

```text
/home/denise/frankenstein-ias/config/paperclip/.env
```

Não expor nem alterar esse arquivo sem autorização.

## Clipper

Clipper é o agente operacional do PaperClip.

ID atual:

```text
2d426cb4-dc47-44a1-be7a-26deb6b4fcc9
```

Adapter:

```text
hermes_local
```

Configuração efetiva relevante:

```json
{
  "cwd": "/home/denise/frankenstein-ias",
  "model": "",
  "command": "hermes",
  "timeoutSec": 300,
  "persistSession": true
}
```

Correção já aplicada:

- `adapterConfig.cwd` do Clipper foi ajustado para `/home/denise/frankenstein-ias`.
- Não alterar `.env`, tokens, modelo, provider, heartbeat ou runtimeConfig sem aprovação.
- O Clipper deve usar o workspace principal por padrão.

Motivo:

O Clipper precisa enxergar:

```text
docs
scripts
voice
config
memory
skills
vault
```

## Bridge PaperClip → Hermes

Bridge criado:

```text
scripts/paperclip-to-hermes-bridge.py
```

Scripts relacionados:

```text
scripts/start-paperclip-hermes-bridge.sh
scripts/stop-paperclip-hermes-bridge.sh
scripts/status-paperclip-hermes-bridge.sh
```

Função da bridge:

- consultar PaperClip local;
- detectar issues concluídas;
- enviar notificação para Hermes WebUI;
- falar `Atividade CAF-XXXX concluída.` via Piper;
- registrar a conclusão no ByteRover.

Endpoint usado:

```text
POST http://127.0.0.1:8787/api/frank/paperclip-completed
```

Estado:

```text
memory/operational/paperclip-hermes-bridge.json
```

Para silenciar fala automática:

```bash
PAPERCLIP_HERMES_SPEAK=0 ~/frankenstein-ias/scripts/start-paperclip-hermes-bridge.sh
```

## Roteamento Operacional

Política criada:

```text
docs/politica-roteamento-robo-frank.md
```

Regra central:

- Pedido simples, seguro e Frank livre: Frank executa direto.
- Frank ocupado: encaminhar para PaperClip/Clipper.
- Pedido com várias etapas, continuidade, agentes, imagem, automação, publicação ou acompanhamento: PaperClip/Clipper.
- Pedido sensível: pedir aprovação antes.

Roteador local:

```text
scripts/frank-operational-router.py
```

O roteador consulta:

- Hermes WebUI `/health`, para ver streams ativos;
- PaperClip issues, para ver atividades com `activeRun`;
- ByteRover, para registrar pedido e decisão.

## ByteRover

ByteRover registra memória operacional curta.

Script:

```text
scripts/byterover-memory.py
```

Arquivos:

```text
memory/byterover/operational-state.json
memory/byterover/events.jsonl
```

Uso atual:

- roteador registra último pedido e decisão de roteamento;
- bridge registra última atividade concluída;
- ByteRover não substitui documentação humana em `docs`.

## Obsidian

Vault:

```text
/home/denise/frankenstein-ias/vault
```

Estrutura do vault:

```text
00-inbox
01-projeto
02-agentes
03-runs
04-documentacao
05-videos
```

Notas já criadas ou esperadas no Obsidian:

```text
Cafe com Dados & Gatos - Identidade.md
Robo Frank - Visao Geral.md
Robo Frank - Arquitetura Operacional.md
Projeto Frankenstein de IAs.md
Hermes Agent.md
Clipper - Agente Operacional.md
Robo Frank - Politica de Roteamento.md
Skills do Robo Frank.md
Diario de Bordo.md
Runs importantes.md
Problemas e Correcoes.md
Voz do Robo Frank - ASR e TTS.md
PaperClip e Fluxos.md
ByteRover.md
CCGram.md
Codex.md
Obsidian.md
Regras de Seguranca.md
Comandos Operacionais.md
Video 01 - Instalacao Base.md
Video 02 - Robo Frank Ganhando Voz.md
Ideias Futuras.md
```

Uso do Obsidian:

- decisões humanas;
- mapa do projeto;
- diário de bordo;
- campanhas e ideias;
- explicações narrativas;
- material dos vídeos;
- documentação que Denise pode ler e reaproveitar depois.

## ComfyUI

ComfyUI local foi desativado por limitação de hardware.

Não tentar reativar, reinstalar ou forçar geração pesada local sem pedido explícito.

Direção atual:

- ComfyUI Cloud;
- RunComfy;
- RunPod;
- outro serviço em nuvem;
- outra máquina com GPU melhor;
- Canva como acabamento visual.

Mensagem importante:

A limitação de hardware deve ser tratada com honestidade no vídeo.  
Não vender a ideia de que qualquer máquina fraca vai gerar imagem pesada localmente sem dificuldade.

## n8n

n8n fica como automação futura.

Regras:

- n8n pode ser preparado e iniciado manualmente;
- não conectar redes sociais nesta etapa;
- não publicar automaticamente;
- não criar workflow de postagem sem aprovação;
- não salvar credenciais em documentação;
- não prometer automação total.

Script manual:

```bash
~/frankenstein-ias/scripts/start-n8n.sh
```

## Site Público do Projeto

A página pública atual do projeto apresenta o Robô Frank como um ecossistema local/híbrido de IAs para:

- agentes;
- memória;
- automação;
- documentação;
- produção visual;
- controle remoto;
- integração futura.

Ela já mostra a Parte 1 publicada no YouTube:

```text
Instalações e primeiros testes do Robô Frank
```

Link atual da Parte 1:

```text
https://www.youtube.com/watch?v=elEJ9blUxV4
```

A página também apresenta:

- visão geral do projeto;
- objetivo;
- componentes principais;
- fluxo de funcionamento;
- exemplo de fluxo de produção;
- limites do laboratório;
- próximos passos;
- chamada para baixar o prompt no GitHub.

## Atualização Necessária Para o Site — Parte 2

Preparar uma atualização da página pública do Projeto Robô Frank para incluir a Parte 2.

A nova seção deve apresentar a Parte 2 com foco em:

```text
Robô Frank ganhando voz
```

Pontos que devem aparecer no texto público:

- Parte 2 mostra o que já foi construído depois da instalação/base.
- Robô Frank já tem uma WebUI customizada.
- O projeto já possui fluxo de voz iniciado.
- NVIDIA Parakeet faz a transcrição da fala.
- Piper faz a fala local do Frank.
- PaperClip organiza atividades.
- Clipper funciona como agente operacional.
- Bridge PaperClip → Hermes avisa quando uma atividade realmente conclui.
- Obsidian registra documentação humana.
- ByteRover registra memória operacional curta.
- O projeto ainda depende de revisão humana.
- Não há publicação automática.
- n8n fica para automação futura.
- ComfyUI local foi desativado por limitação de hardware, com imagem pesada ficando para cloud/futuro.

Texto sugerido para card da Parte 2:

```text
Na Parte 2, o Projeto Robô Frank começa a ganhar voz. O vídeo mostra a WebUI customizada, o fluxo com NVIDIA Parakeet para transcrição, Piper para fala local, PaperClip como painel de controle, Clipper como agente operacional, ByteRover como memória curta e Obsidian como documentação humana. A proposta é mostrar um ecossistema de IA sendo construído por partes, com revisão humana, segurança e pé no chão.
```

Título sugerido:

```text
Robô Frank ganhando voz: agentes, memória e controle humano
```

Subtítulo sugerido:

```text
A segunda parte mostra o ecossistema funcionando além da instalação: voz, WebUI, PaperClip, Clipper, bridge, ByteRover, Obsidian e os primeiros fluxos práticos.
```

Botão sugerido enquanto o vídeo ainda não estiver publicado:

```text
Parte 2 em produção
```

Botão sugerido depois da publicação:

```text
Assistir Parte 2 no YouTube
```

Não inventar link.  
Só inserir link real quando Denise fornecer.

## Tarefas Técnicas da Parte 2

Executar apenas o que for necessário para consolidar e validar o estado atual.

### Tarefa 1 — Diagnóstico Inicial

Rodar dentro do projeto:

```bash
cd ~/frankenstein-ias
```

Verificar estrutura:

```bash
pwd
ls
ls docs
ls scripts
ls voice
ls apps
ls config
```

Verificar sessões tmux:

```bash
tmux ls
```

Verificar scripts disponíveis:

```bash
ls scripts
```

Verificar saúde dos serviços:

```bash
curl -sS http://127.0.0.1:8787/health
curl -sS http://127.0.0.1:3100/api/health
```

Não corrigir nada ainda.  
Primeiro relatar o estado.

### Tarefa 2 — Verificar WebUI do Robô Frank

Confirmar se a WebUI está acessível em:

```text
http://127.0.0.1:8787
```

Verificar se os endpoints existem:

```bash
curl -sS http://127.0.0.1:8787/health
```

Não alterar layout sem pedido.

### Tarefa 3 — Verificar PaperClip

Confirmar se o PaperClip está acessível em:

```text
http://127.0.0.1:3100
```

Verificar health:

```bash
curl -sS http://127.0.0.1:3100/api/health
```

Verificar se o Clipper continua com workspace correto:

```text
/home/denise/frankenstein-ias
```

Não alterar `.env`.

### Tarefa 4 — Verificar Voz

Verificar scripts de voz:

```bash
ls voice/scripts
```

Validar sintaxe do script principal:

```bash
bash -n voice/scripts/voice-command-hermes.sh
```

Validar script de busca de issue:

```bash
bash -n voice/scripts/find-paperclip-issue.sh
```

Não reinstalar Piper.  
Não reinstalar NVIDIA Parakeet.  
Não refazer a camada de voz do zero.

### Tarefa 5 — Testar Fluxo de Voz

Fazer um teste simples e seguro.

Exemplo de comando de voz:

```text
Frank, crie uma atividade simples de teste no PaperClip dizendo: validar fluxo da Parte 2.
```

Resultado esperado:

- fala é gravada;
- Parakeet transcreve;
- Robô Frank interpreta;
- roteador decide;
- PaperClip cria atividade se fizer sentido;
- WebUI mostra atividade criada;
- Piper fala resposta curta;
- não falar “atividade concluída” antes da hora.

### Tarefa 6 — Testar Bridge de Conclusão

Testar se a bridge só fala quando a atividade realmente estiver concluída.

Resultado esperado:

```text
Atividade CAF-XXXX concluída.
```

Somente quando PaperClip marcar a issue como:

```text
done
completed
completedAt
```

Não confundir atividade criada com atividade concluída.

### Tarefa 7 — Validar ByteRover

Verificar arquivos:

```bash
ls memory/byterover
```

Verificar se existem:

```text
memory/byterover/operational-state.json
memory/byterover/events.jsonl
```

Não substituir documentação humana pelo ByteRover.

### Tarefa 8 — Validar Obsidian

Verificar vault:

```bash
ls ~/frankenstein-ias/vault
```

Verificar estrutura:

```bash
ls ~/frankenstein-ias/vault/00-inbox
ls ~/frankenstein-ias/vault/01-projeto
ls ~/frankenstein-ias/vault/02-agentes
ls ~/frankenstein-ias/vault/03-runs
ls ~/frankenstein-ias/vault/04-documentacao
ls ~/frankenstein-ias/vault/05-videos
```

Confirmar se a nota da Parte 2 existe:

```text
Video 02 - Robo Frank Ganhando Voz.md
```

Se não existir, criar com conteúdo resumindo:

- objetivo do vídeo;
- peças mostradas;
- fluxo de voz;
- limites;
- revisão humana;
- próximos passos.

### Tarefa 9 — Atualizar Documentação Técnica

Se necessário, atualizar ou criar documentos em `docs`, sem apagar conteúdo anterior.

Documentos importantes:

```text
docs/CONTEXTO_ATUAL_DO_PROJETO.md
docs/ESTADO_ATUAL_ROBO_FRANK_PARTE_2.md
docs/politica-roteamento-robo-frank.md
docs/paperclip.md
docs/byterover.md
docs/obsidian.md
```

Regra:

- fazer backup antes se houver risco;
- não reduzir conteúdo;
- acrescentar seções novas;
- registrar data da alteração;
- não expor tokens.

### Tarefa 10 — Preparar Material Para o Vídeo 02

Criar ou atualizar no vault:

```text
vault/05-videos/Video 02 - Robo Frank Ganhando Voz.md
```

Conteúdo obrigatório:

```text
# Video 02 - Robo Frank Ganhando Voz

## Objetivo do vídeo

Mostrar o Projeto Robô Frank depois da instalação base, com WebUI customizada, voz, transcrição, TTS local, PaperClip, Clipper, bridge, ByteRover, Obsidian e revisão humana.

## Mensagem central

A IA pode aumentar a capacidade produtiva de uma pessoa sozinha, mas precisa de organização, documentação, segurança e controle humano.

## Demonstração

1. Abrir pasta do projeto.
2. Mostrar documentação no Obsidian.
3. Mostrar WebUI do Robô Frank.
4. Mostrar PaperClip e Clipper.
5. Mostrar fluxo de voz.
6. Mostrar atividade criada no WebUI.
7. Mostrar bridge avisando conclusão real.
8. Explicar limites e próximos passos.

## Limites

- Não há publicação automática.
- n8n é futuro/manual.
- ComfyUI local foi desativado por hardware.
- Tokens não são mostrados.
- Toda ação sensível precisa de aprovação.

## Frase de transição

Agora eu vou mostrar por que isso aqui não é só um chat bonitinho. É o começo de uma infraestrutura pessoal de IA.
```

## Tarefa 11 — Preparar Atualização do Site

Preparar texto ou patch para atualizar a página pública do projeto.

A página atual já tem uma seção de vídeos da série com a Parte 1.

Adicionar a Parte 2 como novo card.

Enquanto não houver link do YouTube, usar estado “em produção”.

Estrutura sugerida:

```html
<article class="series-video-card">
  <div class="series-video-card__content">
    <p class="eyebrow">Parte 2 em produção</p>
    <h3>Robô Frank ganhando voz: agentes, memória e controle humano</h3>
    <p>
      A segunda parte mostra o Robô Frank além da instalação base: WebUI customizada,
      fluxo de voz com NVIDIA Parakeet, fala local com Piper, PaperClip como painel
      de controle, Clipper como agente operacional, ByteRover como memória curta,
      Obsidian como documentação humana e bridge avisando quando uma atividade
      realmente é concluída.
    </p>
  </div>
</article>
```

Se o vídeo já estiver publicado, trocar para:

```text
Parte 2 publicada
```

E incluir botão:

```text
Assistir Parte 2 no YouTube
```

Não inventar link.  
Só inserir link real quando Denise fornecer.

## Validações Técnicas Recomendadas

Rodar somente se os arquivos existirem:

```bash
cd ~/frankenstein-ias
```

```bash
python3 -m py_compile apps/hermes-webui/api/routes.py
```

```bash
python3 -m py_compile scripts/paperclip-to-hermes-bridge.py
```

```bash
python3 -m py_compile scripts/frank-operational-router.py
```

```bash
python3 -m py_compile scripts/byterover-memory.py
```

```bash
bash -n voice/scripts/voice-command-hermes.sh
```

```bash
bash -n voice/scripts/find-paperclip-issue.sh
```

```bash
node --check apps/hermes-webui/static/boot.js
```

```bash
node --check apps/hermes-webui/static/messages.js
```

```bash
curl -sS http://127.0.0.1:8787/health
```

```bash
curl -sS http://127.0.0.1:3100/api/health
```

## Resultado Esperado da Parte 2

Ao final, entregar um relatório claro com:

1. estado atual do projeto;
2. serviços ativos;
3. scripts testados;
4. fluxo de voz validado;
5. PaperClip/Clipper verificados;
6. bridge verificada;
7. ByteRover verificado;
8. Obsidian verificado;
9. documentação atualizada;
10. texto pronto para o site;
11. pendências;
12. próximos passos recomendados.

## Próximos Passos Recomendados

Prioridade:

1. testar atividade simples por voz;
2. confirmar que aparece no WebUI como criada/inicializada;
3. testar conclusão real no PaperClip;
4. confirmar que a bridge fala apenas quando a issue estiver concluída;
5. testar nova run do Clipper;
6. confirmar que não aparece mais fallback workspace;
7. atualizar nota do Obsidian da Parte 2;
8. preparar card da Parte 2 para o site;
9. manter n8n como futuro/manual;
10. deixar ComfyUI local como desativado por limitação de hardware.

## Instrução Final ao Executor

Trabalhe como assistente técnico do Projeto Robô Frank.

Seja cuidadoso, objetivo e conservador.

Não tente “melhorar” apagando ou reinstalando.

Não transforme o projeto em automação sem supervisão.

O foco da Parte 2 é demonstrar o que já foi construído:

- o Frank com voz;
- a WebUI customizada;
- a transcrição com Parakeet;
- a fala com Piper;
- o PaperClip como control plane;
- o Clipper como agente operacional;
- o Codex como apoio técnico;
- o CCGram como ponte remota;
- o ByteRover como memória operacional;
- o Obsidian como documentação humana;
- e a revisão humana como parte central da arquitetura.

No final, explicar tudo de forma que possa virar vídeo, documentação e atualização pública do site.
