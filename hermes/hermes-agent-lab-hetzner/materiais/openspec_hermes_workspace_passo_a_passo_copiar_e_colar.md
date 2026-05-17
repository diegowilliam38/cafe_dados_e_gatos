# OpenSpec com Hermes Workspace

## Projeto

Hermes Agent Lab na Hetzner

## Título explicativo

Como instalar e organizar Hermes Agent na Hetzner

## Objetivo

Usar o OpenSpec como camada de planejamento antes da execução dos agentes no Hermes Workspace.

O projeto mostra como usar Hermes Agent, Hermes Workspace, OpenSpec e agentes de IA para organizar um teste prático com pesquisa, validação, roteiro, prompt visual e revisão humana.

TikTok/Shopee aparecem como teste experimental no final do vídeo.

A infraestrutura principal é Hermes na Hetzner.

```text
OpenSpec
Define plano, escopo, regras e critérios.

Codex
Trabalha com os arquivos do OpenSpec e ajuda a aplicar mudanças no projeto.

Hermes Workspace
Cria e organiza os agentes.

Hermes Agent
Executa tarefas com base na especificação aprovada.
```

---

# 1. Ordem correta de uso

```text
1. Criar a pasta do projeto
2. Inicializar o OpenSpec dentro da pasta usando Codex
3. Criar a especificação/proposta do projeto
4. Revisar a proposta
5. Criar os agentes no Hermes Workspace com missão clara
6. Mandar o CEO / Orquestrador ler o OpenSpec
7. Acessar Hermes Gateway, Dashboard e Workspace via Tailscale
8. Delegar tarefas somente depois da revisão
9. Pesquisar tendências com SearXNG e navegador controlado quando disponível
10. Produzir criativos visualmente apenas depois de briefing, roteiro e revisão humana
```

---

# 2. Regra principal

```text
Não crie agentes vazios.

Primeiro crie o OpenSpec do projeto.

Depois crie os agentes no Hermes Workspace já com missão clara.
```

O OpenSpec define o contrato do projeto.

Os agentes executam papéis dentro desse contrato.

---

# 3. Criar pasta do projeto

## Rodar na VPS

```bash
mkdir -p ~/projetos/hermes-tiktok-commerce-lab
cd ~/projetos/hermes-tiktok-commerce-lab
```

Se estiver reaproveitando uma pasta já criada para o vídeo, mantenha a pasta atual e atualize apenas o nome e o escopo dentro da especificação.

---

# 4. Conferir Node.js

## Rodar na VPS

```bash
node --version
```

O OpenSpec precisa de Node.js moderno.

Se o Node.js 22 já foi instalado na instalação do Hermes, pode seguir.

---

# 5. Instalar ou atualizar OpenSpec

## Rodar na VPS

```bash
npm install -g @fission-ai/openspec@latest
```

---

# 6. Conferir instalação do OpenSpec

## Rodar na VPS

```bash
openspec --version
```

---

# 7. Inicializar OpenSpec no projeto

## Rodar na VPS, dentro da pasta do projeto

```bash
cd ~/projetos/hermes-tiktok-commerce-lab
openspec init
```

Durante o assistente, escolha:

```text
Codex
```

Use Codex porque o OpenSpec oferece suporte direto a ele.

O Hermes será usado depois, pelo Hermes Workspace, lendo a especificação e os arquivos do OpenSpec.

O Hermes não precisa aparecer na lista do OpenSpec para este fluxo funcionar.

---

# 8. Conferir arquivos criados

## Rodar na VPS

```bash
cd ~/projetos/hermes-tiktok-commerce-lab
ls -la
```

```bash
find . -maxdepth 3 -type f | sort
```

A estrutura pode variar conforme a versão, mas normalmente o OpenSpec cria arquivos de instrução e uma pasta de especificações.

---

# 9. Atualizar instruções do OpenSpec

## Rodar na VPS, dentro da pasta do projeto

```bash
cd ~/projetos/hermes-tiktok-commerce-lab
openspec update
```

Use este comando quando quiser regenerar ou atualizar instruções do OpenSpec dentro do projeto.

---

# 10. VS Code Remote SSH

Esta etapa é necessária para quem usa o Codex no VS Code da máquina local, mas inicializou o OpenSpec dentro da VPS.

O Codex precisa enxergar os arquivos do projeto.

Como o projeto está na Hetzner, o VS Code deve abrir a pasta remota da VPS.

## 10.1. Conferir acesso via Tailscale

## Rodar no computador local

```bash
ssh root@IP_TAILSCALE_DA_VPS
```

Se conectar corretamente, saia da VPS:

```bash
exit
```

## 10.2. Configurar conexão SSH no VS Code

## Rodar no computador local

No VS Code, pressione:

```text
CTRL + SHIFT + P
```

Procure por:

```text
Remote-SSH: Open SSH Configuration File
```

Adicione:

```sshconfig
Host hermes-hetzner
    HostName IP_TAILSCALE_DA_VPS
    User root
    Port 22
```

Se usar chave SSH específica, adicione também:

```sshconfig
Host hermes-hetzner
    HostName IP_TAILSCALE_DA_VPS
    User root
    Port 22
    IdentityFile ~/.ssh/NOME_DA_CHAVE
```

## 10.3. Abrir a pasta remota

Abra a pasta:

```text
/root/projetos/hermes-tiktok-commerce-lab
```

Ou, se estiver reaproveitando a pasta antiga:

```text
/root/projetos/hermes-agent-lab-hetzner
```

Regra:

```text
Não abra uma cópia local se o OpenSpec foi inicializado na VPS.

Abra a pasta remota da VPS pelo VS Code Remote SSH.
```

---

# 11. Criar proposta inicial

## Usar no Codex / assistente configurado com OpenSpec dentro do projeto

```text
/opsx:propose Criar a estrutura profissional do projeto Hermes Agent Lab na Hetzner, com documentação organizada, exemplos de configuração, scripts auxiliares, segurança, operação, agentes do Hermes Workspace, fluxo de trabalho com OpenSpec e caso de uso final em afiliados no TikTok.
```

---

# 12. Especificação base para colar no OpenSpec

Use este conteúdo como base da especificação do projeto.

````md
# Especificação OpenSpec - Hermes Agent Lab na Hetzner

## 1. Objetivo do projeto

Criar um laboratório técnico e prático para demonstrar como Hermes Agent, Hermes Workspace, OpenSpec e agentes de IA podem ajudar a organizar uma rodada experimental de pesquisa e conteúdo para TikTok/Shopee.

O projeto deve mostrar pesquisa de produtos afiliados, pesquisa de tendências, criação de roteiros, calendário de conteúdo, revisão de promessas, organização em Kanban, documentação para GitHub e apoio à produção de vídeos curtos.

TikTok/Shopee aparecem como teste experimental no final do vídeo.

A infraestrutura principal é Hermes na Hetzner.

## 2. Resultado final esperado

Ao final, o projeto deve entregar:

- VPS Ubuntu preparada
- Tailscale instalado e funcionando
- Firewall configurado
- Ollama ou Ollama Cloud configurado
- SearXNG rodando em Docker
- Hermes Agent instalado sem Docker
- Hermes Gateway/API funcionando
- Hermes Dashboard funcionando
- Hermes Workspace funcionando
- OpenSpec inicializado no projeto
- Agentes criados no Hermes Workspace
- Kanban organizado
- Documentação separada por temas
- Exemplos de arquivos ".env"
- Material organizado para GitHub
- Base para vídeo no YouTube
- Fluxo manual para criação visual com revisão humana
- Fluxo de pesquisa com SearXNG e navegador controlado

## 3. Escopo incluído

Este projeto inclui:

- Instalação em VPS Ubuntu Hetzner
- Uso de Tailscale para acesso privado
- Uso de firewall
- Uso de Ollama/Ollama Cloud como provedor de modelo
- Uso de Docker apenas para SearXNG
- Instalação do Hermes Agent sem Docker
- Configuração do Hermes Gateway/API
- Configuração do Hermes Dashboard
- Configuração do Hermes Workspace
- Criação de agentes pelo Hermes Workspace
- Uso do OpenSpec como camada de planejamento antes da execução
- teste experimental com TikTok/Shopee como caso de uso do vídeo
- pesquisa de produtos afiliados para gatos, gadgets, acessórios de computador e tecnologia
- Pesquisa assistida em fontes públicas do TikTok com navegador controlado
- Roteiros curtos para TikTok, Reels e Shorts
- Calendário de conteúdo
- Revisão de promessas comerciais
- Organização em Kanban
- Apoio a Shorts de IA para o canal Café com Dados & Gatos
- Ferramentas opcionais de criação visual

## 4. Escopo excluído

Este projeto não inclui:

- Garantia de vendas, renda ou comissão
- Promessa de renda
- Enriquecimento rápido
- Ensino de spam
- Burla de regras do TikTok
- Automação de publicação sem revisão humana
- Integração automática com TikTok não implementada
- Integração automática com PipClip não implementada
- Instalação completa do ComfyUI neste momento
- Burla de login, captcha, paywall ou restrições de plataforma
- Scraping agressivo
- Coleta de dados privados
- Hospedagem pública aberta sem proteção
- Exposição pública direta das portas internas
- Instalação do Hermes Agent, Dashboard ou Workspace via Docker
- Kubernetes
- CI/CD complexo
- Alta disponibilidade
- Balanceamento de carga
- Automação irreversível sem revisão humana

## 5. Arquitetura desejada

```text
VPS Ubuntu Hetzner
|-- Tailscale
|-- Firewall
|-- Ollama / Ollama Cloud
|-- Docker
|   `-- SearXNG
|-- Hermes Agent
|-- Hermes Gateway/API
|-- Hermes Dashboard
|-- Hermes Workspace
|-- OpenSpec
|-- Navegador controlado
`-- Agentes criados no Workspace
```

## 6. Portas previstas

```text
22      SSH
8080    SearXNG
8642    Hermes Gateway/API
9119    Hermes Dashboard
3000    Hermes Workspace
11434   Ollama
```

Regra geral:

```text
As portas devem ficar acessíveis preferencialmente pela rede privada Tailscale.
Não abrir portas públicas sem necessidade.
```

## 7. Caso de uso final

O caso de uso final do projeto é organizar um teste experimental de conteúdo com TikTok/Shopee com apoio de agentes de IA.

Frentes do caso de uso:

- pesquisa de produtos afiliados para TikTok
- produtos afiliados para gatos
- gadgets
- acessórios de computador
- tecnologia
- criação de conteúdo afiliado curto
- roteiros para TikTok, Reels e Shorts
- calendário de publicação
- revisão de promessas comerciais
- organização de tarefas em Kanban
- documentação para GitHub
- apoio a Shorts de IA para o canal Café com Dados & Gatos

O TikTok deve ser usado para sinais de tendência.

O SearXNG deve ser usado para validação externa.

## 8. Fontes permitidas

Fontes iniciais para pesquisa assistida:

- TikTok Creative Center
- TikTok Creative Center - Top Products
- TikTok Creative Center - Trends
- TikTok Search
- TikTok Shop / Seller Center Brasil, quando disponível
- SearXNG local para validação externa
- sites externos de reviews
- sites externos de reclamações
- sites externos de comparação de preços
- marketplaces e lojas, quando acessíveis e usados apenas para validação

Links iniciais:

```text
TikTok Creative Center
https://ads.tiktok.com/business/creativecenter/pc/pt

TikTok Creative Center - Top Products
https://ads.tiktok.com/business/creativecenter/top-products/pc/pt

TikTok Creative Center - Trends
https://ads.tiktok.com/business/creativecenter/trends/hub/pc/pt

TikTok Shop / Seller Center Brasil
https://seller-br.tiktok.com/

TikTok Search
https://www.tiktok.com/search

SearXNG local
http://IP_TAILSCALE_DA_VPS:8080
```

Esses links podem mudar com o tempo.

Se algum link mudar, atualizar primeiro o OpenSpec e depois os documentos de agentes, se necessário.

## 9. Regras de pesquisa

- O TikTok deve ser usado para sinais de tendência.
- O SearXNG deve ser usado para validação externa.
- O Hermes não deve afirmar que um produto é mais vendido sem fonte clara.
- O Hermes não deve afirmar que um produto vende muito sem evidência observável.
- O Hermes não deve burlar login, captcha, paywall ou restrição de plataforma.
- O Hermes não deve fazer scraping agressivo.
- O Hermes não deve coletar dados privados.
- O Hermes deve separar fato, hipótese, recomendação e opinião.
- O Hermes deve registrar fonte e data da observação quando usar navegador controlado.
- Toda publicação precisa de revisão humana.

## 10. Regras comerciais e editoriais

- Não garantir vendas, renda ou comissão.
- Não prometer renda.
- Não usar linguagem de enriquecimento rápido.
- Não ensinar spam.
- Não ensinar burla de regras do TikTok.
- Não automatizar publicação sem revisão humana.
- Não criar criativos enganosos.
- Não inventar benefícios técnicos de produtos.
- Não usar imagem, marca ou pessoa sem autorização.
- Não usar antes/depois sem base.
- Diferenciar fato, hipótese, recomendação e opinião.
- Não burlar login, captcha ou restrições da plataforma.
- Não fazer scraping agressivo.
- Não coletar dados privados.

## 11. Regras de segurança

- Não expor senhas reais na documentação pública.
- Não commitar arquivos ".env" reais.
- Criar arquivos ".env.example" com valores fictícios.
- Usar placeholders em documentação pública.
- Preferir acesso via Tailscale.
- Manter portas internas bloqueadas publicamente quando possível.
- Separar senha de login do Workspace da chave técnica da API.
- Não publicar IP público, token, senha ou chave real.
- Toda ação destrutiva deve pedir confirmação humana.
- Todo conteúdo público deve passar por revisão humana.

## 12. Regras de revisão humana

Toda publicação pública precisa de revisão humana.

A revisão humana é obrigatória antes de:

- publicar vídeo, post, comentário, resposta ou anúncio
- usar roteiro em canal público
- usar criativo gerado por IA
- usar imagem de produto, marca ou pessoa
- afirmar tendência, ranking ou desempenho de produto
- alterar firewall, Nginx, senhas, tokens ou exposição pública
- executar ação externa, destrutiva ou irreversível

O Revisor de Promessas pode bloquear materiais com risco comercial, promessa exagerada, claim sem base, criativo enganoso ou aparência de spam.

## 13. Regras de execução dos agentes

Os agentes não devem executar ações críticas sem aprovação humana.

Ações que exigem aprovação:

- apagar arquivos
- sobrescrever configuração
- reiniciar serviços importantes
- alterar firewall
- alterar Nginx
- publicar conteúdo
- enviar mensagem
- enviar dados para terceiros
- expor portas publicamente
- trocar senhas ou tokens
- remover volumes Docker
- limpar dados persistentes
- automatizar publicação
- tomar decisão comercial sensível
- fazer pesquisa automatizada fora dos limites aprovados

Formato obrigatório antes de ação crítica:

```text
ACTION_PROPOSED:
RISK:
FILES_AFFECTED:
COMMANDS_TO_RUN:
ROLLBACK:
NEEDS_APPROVAL:
```

Checkpoint padrão dos agentes:

```text
STATE:
RESULT:
FILES_CHANGED:
RISKS:
NEXT_ACTION:
NEEDS_REVIEW:
```

## 14. Agentes previstos no Hermes Workspace

Criar os seguintes agentes:

```text
CEO / Orquestrador
Pesquisador de Produtos Afiliados
Pesquisador de Tendências TikTok
Estrategista de Conteúdo Afiliado
Copywriter de Vídeos Curtos
Social Media TikTok
Designer de Campanha
Revisor de Promessas
Documentador Técnico
Kanban Manager
```

Use como referência:

```text
configuracao_agentes_hermes_tiktok_commerce_lab_navegador.md
```

## 15. Responsabilidades dos agentes

### CEO / Orquestrador

Coordena o projeto, lê a especificação OpenSpec, divide tarefas, controla escopo, pede aprovação humana e organiza a execução.

### Pesquisador de Produtos Afiliados

Pesquisa nichos, produtos afiliados para gatos, gadgets, acessórios de computador, tecnologia, demanda, diferenciais, riscos, oportunidades e ângulos de conteúdo.

Pode usar SearXNG para validação externa e navegador controlado para observar páginas públicas ou páginas abertas pela pessoa humana.

### Pesquisador de Tendências TikTok

Pesquisa formatos de vídeo, ganchos, linguagem, hashtags, estilos de conteúdo, referências, tendências e formatos de afiliados.

O caminho preferencial para sinais internos do TikTok é o navegador controlado, quando disponível.

### Estrategista de Conteúdo Afiliado

Define público-alvo, posicionamento, linha editorial, proposta de valor, tipos de conteúdo, lógica de venda e abordagem sem exageros.

### Copywriter de Vídeos Curtos

Cria hooks, roteiros curtos, CTAs, legendas, variações de texto e chamadas para TikTok, Reels, Shorts e comunidade.

### Social Media TikTok

Transforma a estratégia em calendário de publicação, sequência de posts, ideias de testes, formatos, organização de conteúdo e planejamento de rotina.

### Designer de Campanha

Cria direção visual, prompts de imagem, ideias de thumbnail, cenas, elementos visuais, prompts para PipClip, prompts para Canva, prompts para CapCut e sugestões para ComfyUI quando aplicável.

### Revisor de Promessas

Revisa textos, roteiros, criativos e campanhas para evitar promessas exageradas, enganosas, apelativas, sem base ou com risco comercial.

### Documentador Técnico

Documenta instalação, configuração, erros, correções, agentes, prompts, exemplos, comandos copy-paste e fluxo do projeto para GitHub.

### Kanban Manager

Organiza tarefas em Entrada / Pedidos, Aguardando, Na Fila, Executando, Testando, Concluído e Problemas / Bugs.

## 16. Ferramentas opcionais de criação visual

### Canva / CapCut

Uso manual para edição, montagem, legendas, cortes e acabamento.

### PipClip

Link de afiliada do PipClip: [https://pipclip.ai/?afid=2Z2MW26](https://pipclip.ai/?afid=2Z2MW26)

Ferramenta opcional para criação rápida de criativos com IA, vídeos de produto, avatares, animações, variações visuais e conteúdos curtos para TikTok, Reels e Shorts.

O Hermes não substitui o PipClip.

O PipClip pode ser usado depois que os agentes entregarem briefing, roteiro e direção visual.

Não afirmar que existe integração automática entre Hermes e PipClip se ela não estiver implementada.

### Regras para prompts de vídeo no PipClip

O projeto pode usar PipClip como ferramenta opcional de criação visual para vídeos curtos, cenas, variações criativas e imagens em movimento.

Formato obrigatório para prompts de vídeo:

```text
Estilo:
Cena:
Câmera:
Iluminação:
Ação por segundos:
Texto na tela:
Som ambiente:
Negativas:
```

Regras:

- prompts devem pedir vídeo vertical 9:16 quando o destino for TikTok, Reels ou Shorts
- para vídeos de 10 a 15 segundos, usar poucos momentos e cenas simples
- para vídeos de 30 segundos, permitir mais etapas, sem excesso de informação
- texto na tela deve ser curto e simples
- não usar frases longas
- para vídeos de produto, priorizar imagem, demonstração e contexto de uso
- para vídeos de produto, evitar texto atrapalhando a cena ou cobrindo o produto
- para vídeos educativos ou divulgação de canal, usar textos curtos e simples
- todo criativo precisa passar pelo Revisor de Promessas
- todo criativo precisa de aprovação humana antes de publicação

Negativas recomendadas:

- sem logotipos reais
- sem rostos reais
- sem marcas reais sem autorização
- sem promessa de dinheiro
- sem promessa de venda garantida
- sem linguagem apelativa
- sem criativo enganoso
- sem afirmar que a IA faz tudo sozinha
- sem automação sem controle
- sem excesso de texto
- sem texto pequeno
- sem texto ilegível
- sem muitas frases na tela
- sem texto atrapalhando produto ou cena

### ComfyUI

Alternativa avançada para usuários com máquina local e GPU adequada.

Não documentar instalação completa do ComfyUI neste momento.

Não prometer que todos conseguirão rodar localmente.

A demonstração principal deve usar caminhos mais acessíveis.

## 17. Navegador controlado e fontes de pesquisa

Este projeto usa pesquisa em dois níveis.

```text
Nível 1 - Hermes + SearXNG
Pesquisa aberta na web para validação externa, reviews, reclamações, preços, concorrentes e riscos.

Nível 2 - Hermes + navegador controlado
Pesquisa assistida em páginas do TikTok, TikTok Creative Center, TikTok Shop / Seller Center e outras páginas abertas no navegador.
```

O Nível 2 é o caminho preferencial para pesquisar sinais de tendência dentro do TikTok.

O navegador controlado deve ser tratado como ferramenta operacional.

Ele pode acessar páginas, observar informações públicas, organizar achados e devolver tabelas para revisão humana.

Ele não deve:

```text
- burlar login
- contornar captcha
- fazer scraping agressivo
- publicar automaticamente
- enviar mensagem automática
- seguir pessoas automaticamente
- coletar dados privados
- violar regras da plataforma
```

Fontes iniciais permitidas:

```text
TikTok Creative Center
https://ads.tiktok.com/business/creativecenter/pc/pt

TikTok Creative Center - Top Products
https://ads.tiktok.com/business/creativecenter/top-products/pc/pt

TikTok Creative Center - Trends
https://ads.tiktok.com/business/creativecenter/trends/hub/pc/pt

TikTok Shop / Seller Center Brasil
https://seller-br.tiktok.com/

TikTok Search
https://www.tiktok.com/search

SearXNG local
http://IP_TAILSCALE_DA_VPS:8080

Sites externos de reviews, reclamações e comparação de preços
Usar para validação externa.
```

Esses links podem mudar com o tempo.

Se algum link mudar, atualizar primeiro o OpenSpec e depois o arquivo de agentes, se necessário.

## 18. Fluxo visual básico

```text
1. Hermes organiza a ideia.
2. Pesquisador levanta produto e ângulo.
3. Copywriter cria roteiro.
4. Designer cria direção visual.
5. Revisor de Promessas valida riscos.
6. Humano escolhe ferramenta visual.
7. Criativo é produzido no Canva, CapCut, PipClip ou ComfyUI.
8. Humano revisa antes de publicar.
```

## 19. Critérios de aceite

O projeto só deve ser considerado pronto quando:

- o Tailscale estiver funcionando
- o IP privado da VPS estiver identificado
- o firewall estiver configurado
- o Ollama responder localmente ou via configuração definida
- o SearXNG responder localmente em Docker
- o Hermes Agent estiver instalado
- o Hermes Gateway/API responder em "/health"
- o Hermes Dashboard abrir
- o Hermes Workspace abrir
- o Workspace conseguir se conectar ao Gateway
- os agentes forem criados no Workspace
- o OpenSpec estiver inicializado no projeto
- os arquivos de documentação estiverem organizados
- os riscos comerciais estiverem documentados
- o fluxo de revisão humana estiver claro
- não houver promessa de vendas, renda ou comissão
- as ferramentas visuais forem tratadas como opcionais
- o navegador controlado estiver documentado com limites claros
- as fontes de pesquisa forem revisadas antes de uso público
- o OpenSpec definir claramente fontes permitidas
- o Hermes não afirmar ranking ou produto mais vendido sem fonte clara
- toda publicação tiver revisão humana prevista

## 20. Formato de documentação

A documentação deve seguir este padrão:

- Markdown simples
- títulos curtos
- comandos em blocos separados
- sem conversa pessoal
- sem linguagem de guru
- sem promessa exagerada
- foco em copiar e colar
- explicar apenas o necessário
- avisar quando algo for arriscado
- avisar quando algo for opcional
- separar instalação, operação, segurança, agentes e erros
````

---

# 13. Depois da proposta, revisar antes de aplicar

Não aplique direto.

Primeiro leia o que o OpenSpec propôs.

Confira:

```text
1. O escopo está correto?
2. Ele entendeu que Hermes não será instalado com Docker?
3. Ele entendeu que Docker será usado só para SearXNG?
4. Ele entendeu que Tailscale vem no começo?
5. Ele separou segurança, instalação, operação, agentes e documentação?
6. Ele não inventou portas?
7. Ele não colocou senhas reais?
8. Ele não sugeriu expor tudo publicamente?
9. Ele incluiu criação dos agentes no Workspace?
10. Ele incluiu revisão humana antes de ações críticas?
11. Ele entendeu que TikTok é caso de uso final?
12. Ele evitou promessa de vendas e renda?
13. Ele tratou navegador controlado como pesquisa assistida, sem scraping agressivo?
14. Ele tratou PipClip como opcional?
15. Ele tratou ComfyUI como opção avançada para quem tem GPU?
```

---

# 14. Aplicar a proposta depois da revisão

## Usar no Codex / assistente configurado com OpenSpec dentro do projeto

```text
/opsx:apply
```

Use apenas depois de revisar e aprovar a proposta.

---

# 15. Verificar se a implementação segue a especificação

## Usar no Codex / assistente configurado com OpenSpec dentro do projeto

```text
/opsx:verify
```

Se a versão/perfil do OpenSpec não tiver `/opsx:verify`, use o fluxo básico e peça ao agente uma revisão manual comparando a implementação com a proposta.

---

# 16. Arquivar quando concluir

## Usar no Codex / assistente configurado com OpenSpec dentro do projeto

```text
/opsx:archive
```

Use quando a mudança estiver concluída e validada.

---

# 17. Criar agentes no Hermes Workspace

Depois que o OpenSpec estiver criado e revisado, crie os agentes no Hermes Workspace.

Não crie agentes vazios.

Cada agente deve ter missão clara e apontar para o OpenSpec.

Use como referência:

```text
configuracao_agentes_hermes_tiktok_commerce_lab_navegador.md
```

---

# 18. Prompt inicial para o CEO / Orquestrador

Depois que os agentes estiverem criados, use este prompt no CEO.

```text
Estamos no projeto:

~/projetos/hermes-tiktok-commerce-lab

Este projeto usa OpenSpec inicializado com Codex.

O Codex foi escolhido porque o Hermes pode não aparecer como ferramenta nativa no OpenSpec.

Sua função como CEO / Orquestrador é ler os arquivos do OpenSpec dentro da pasta do projeto e seguir a especificação aprovada.

O acesso ao Hermes Gateway, Dashboard e Workspace será feito pela rede privada Tailscale.

O objetivo do projeto é demonstrar como usar Hermes Agent, Hermes Workspace, OpenSpec e agentes de IA para organizar um teste experimental de conteúdo com TikTok/Shopee.

A operação envolve pesquisa de produtos afiliados, tendências de TikTok, roteiros curtos, calendário de conteúdo, direção visual, revisão de promessas, Kanban e documentação.

Ferramentas opcionais de criação visual podem incluir Canva, CapCut, PipClip e ComfyUI.

O projeto pode usar navegador controlado para pesquisa assistida em páginas públicas ou páginas abertas pela pessoa humana.

Essas ferramentas não são obrigatórias e não devem ser tratadas como integração automática.

Antes de executar qualquer ação:
1. leia a especificação OpenSpec
2. apresente seu entendimento do projeto
3. liste os agentes disponíveis
4. proponha a divisão de tarefas
5. indique riscos
6. peça aprovação humana antes de executar qualquer ação crítica

Não execute comandos ainda.
```

---

# 19. Prompt para organizar a primeira rodada

```text
Com base na especificação OpenSpec do projeto Hermes Agent Lab na Hetzner, organize a primeira rodada de trabalho.

Quero que você entregue:

1. resumo do objetivo do projeto
2. lista dos agentes envolvidos
3. tarefas por agente
4. ordem sugerida de execução
5. riscos principais
6. o que precisa de aprovação humana
7. próxima ação segura

Não execute comandos ainda.
```

---

# 20. Prompt para pedir documentação

Use este prompt quando quiser que o Documentador Técnico trabalhe.

```text
Com base na especificação OpenSpec do projeto Hermes Agent Lab na Hetzner, crie ou atualize a documentação técnica do projeto.

Regras:
- usar Markdown simples
- usar comandos copy-paste quando houver comandos
- não incluir conversa pessoal
- não incluir senhas reais
- não incluir tokens reais
- não incluir IPs reais
- não inventar comandos
- não inventar integração automática com TikTok
- não inventar integração automática com PipClip
- não criar guia completo de ComfyUI se não estiver no escopo
- não documentar navegador controlado como scraping agressivo
- não sugerir burla de login, captcha ou regra de plataforma
- separar por tema
- avisar quando algo for opcional
- avisar quando algo for perigoso
- indicar onde cada comando deve ser rodado

Antes de alterar qualquer arquivo, apresente o plano de arquivos que serão criados ou editados.
```

---

# 21. Prompt para revisão de promessas

Use este prompt quando quiser que o Revisor de Promessas analise conteúdo, roteiro ou criativo.

```text
Revise o material criado para o projeto Hermes Agent Lab na Hetzner.

Verifique:
- promessa de venda, renda ou comissão garantida
- promessa de renda
- exagero comercial
- claim sem comprovação
- linguagem apelativa
- conteúdo com aparência de spam
- uso indevido de imagem, marca ou pessoa
- criativo enganoso
- antes/depois sem base
- necessidade de aprovação humana

Entregue o parecer final como:

APPROVED
CHANGES_REQUESTED
BLOCKED

Explique os motivos.
```

---

# 22. Prompt para pesquisa com navegador controlado

Use este prompt quando quiser pesquisar fontes públicas do TikTok com navegador controlado.

```text
Com base na especificação OpenSpec do projeto Hermes Agent Lab na Hetzner, use o navegador controlado para pesquisar sinais públicos de tendência e produto.

Fontes permitidas:
- TikTok Creative Center
- TikTok Creative Center - Top Products
- TikTok Creative Center - Trends
- TikTok Search
- TikTok Shop / Seller Center Brasil, quando disponível

Regras:
- não burlar login
- não contornar captcha
- não fazer scraping agressivo
- não coletar dados privados
- não publicar nada
- não enviar mensagem
- não seguir pessoas
- registrar fonte e data da observação
- separar fato, hipótese e recomendação
- pedir revisão humana antes de usar achados em roteiro ou criativo

Entregue uma tabela com:
1. fonte
2. item observado
3. categoria
4. evidência visível
5. oportunidade de conteúdo
6. risco
7. validação humana necessária
```

---

# 23. Prompt para organizar Kanban

Use este prompt para o Kanban Manager.

```text
Com base na especificação OpenSpec do projeto Hermes Agent Lab na Hetzner, organize o projeto em tarefas de Kanban.

Use estes status:

Entrada / Pedidos
Aguardando
Na Fila
Executando
Testando
Concluído
Problemas / Bugs

Para cada tarefa, informe:
- título
- descrição
- agente responsável
- prioridade
- status inicial
- critério de conclusão
- dependências
- riscos

Considere as frentes:
- infraestrutura Hermes na Hetzner
- OpenSpec
- agentes no Hermes Workspace
- afiliados no TikTok
- produtos afiliados para gatos
- gadgets
- acessórios de computador
- vídeos curtos
- navegador controlado para pesquisa assistida
- PipClip opcional
- ComfyUI opcional para GPU
- documentação para GitHub
- material para YouTube
```

---

# 24. Fluxo prático completo

```text
1. Criar pasta do projeto na VPS
2. Instalar OpenSpec na VPS
3. Rodar openspec init dentro da pasta do projeto
4. Escolher Codex durante o assistente
5. Rodar openspec update, se necessário
6. Conectar o VS Code na VPS via Tailscale
7. Abrir a pasta remota do projeto no VS Code
8. Conferir se o Codex está trabalhando na pasta remota
9. Pedir /opsx:propose no Codex ou assistente configurado com OpenSpec
10. Revisar a proposta
11. Aplicar com /opsx:apply
12. Criar agentes no Hermes Workspace
13. Configurar missão dos agentes
14. Acessar Hermes via Tailscale
15. Mandar o CEO ler o OpenSpec
16. CEO divide tarefas
17. Agentes executam por fase
18. Revisor de Promessas valida conteúdo e criativos
19. Documentador registra
20. Kanban Manager organiza status
21. Verificar a implementação comparando com a especificação
22. Arquivar com /opsx:archive quando finalizar
```

---

# 25. Regra final

```text
OpenSpec primeiro.
Codex para trabalhar com o OpenSpec.
Agentes depois no Hermes Workspace.
CEO lê o OpenSpec.
Hermes acessado via Tailscale.
TikTok é o caso de uso final.
Navegador controlado pode apoiar pesquisa assistida.
PipClip, Canva, CapCut e ComfyUI são ferramentas opcionais.
Execução só depois de revisão.
Ação crítica só com aprovação humana.
Conteúdo público só com revisão humana.
```



