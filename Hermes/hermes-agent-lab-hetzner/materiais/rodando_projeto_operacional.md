# Rodando o Projeto - Hermes Agent Lab na Hetzner

# Objetivo

Este documento mostra como iniciar operacionalmente o projeto depois que:

```text
- Hermes Agent estiver funcionando
- gateway estiver funcionando
- workers estiverem criados
- SOUL.md dos workers estiver configurado
- Kanban estiver habilitado
- OpenSpec estiver dentro do projeto
```

---

# Estrutura operacional

O projeto usa:

```text
default = CEO / Orquestrador
```

Workers:

```text
hermes-pesquisador-tiktok
hermes-validador-searxng
hermes-organizador-produtos
hermes-criador-conteudo
hermes-designer-pipclip
hermes-revisor-final
```

Projeto:

```text
/root/projetos/hermes-tiktok-commerce-lab
```

Workspace usado nos cards:

```text
dir:/root/projetos/hermes-tiktok-commerce-lab
```

---

# Fluxo operacional oficial

```text
default/orquestrador
→ hermes-pesquisador-tiktok
   KANBAN_STATUS: Produto encontrado

→ hermes-validador-searxng
   KANBAN_STATUS: Validando com SearXNG

→ hermes-organizador-produtos
   KANBAN_STATUS: Aguardando escolha humana

→ pausa obrigatória
   humano escolhe produto

→ hermes-criador-conteudo
   KANBAN_STATUS: Criando roteiro

→ pausa obrigatória
   humano aprova roteiro

→ hermes-designer-pipclip
   KANBAN_STATUS: Criando prompt PipClip

→ hermes-revisor-final
   KANBAN_STATUS: Revisado

→ pausa obrigatória
   publicação manual, fora da automação
```

---

# 1. Entrar na VPS

No Windows PowerShell:

```powershell
ssh root@SEU_IP
```

---

# 2. Entrar na pasta do projeto

```bash
cd /root/projetos/hermes-tiktok-commerce-lab
```

Conferir:

```bash
pwd
ls -la
```

---

# 3. Garantir que o gateway está funcionando

```bash
hermes gateway start
```

Conferir:

```bash
hermes gateway status
```

---

# 4. Conferir os profiles

```bash
hermes profile list
```

Resultado esperado:

```text
default
hermes-pesquisador-tiktok
hermes-validador-searxng
hermes-organizador-produtos
hermes-criador-conteudo
hermes-designer-pipclip
hermes-revisor-final
```

---

# 5. Abrir o Hermes Workspace

Abrir no navegador:

```text
http://IP_DA_VPS:3000
```

ou via Tailscale:

```text
http://IP_TAILSCALE:3000
```

---

# 6. Abrir chat do default/orquestrador

Usar o profile:

```text
default
```

---

# 7. Primeiro prompt do projeto

Enviar:

```text
Estamos no projeto:

/root/projetos/hermes-tiktok-commerce-lab

Antes de responder, leia:
- AGENTS.md
- arquivos OpenSpec do projeto

Depois:

1. explique o objetivo do projeto
2. liste os workers disponíveis
3. explique o fluxo operacional atual
4. proponha a primeira rodada operacional
5. diga quais cards devem ser criados primeiro
6. diga qual worker deve executar cada card
7. use somente os KANBAN_STATUS definidos no projeto:
   - Produto encontrado
   - Validando com SearXNG
   - Aguardando escolha humana
   - Criando roteiro
   - Criando prompt PipClip
   - Revisado
8. use como fonte inicial de produtos:
   https://shopee.com.br/search?keyword=mais%20vendidos%20da%20shopee
9. não crie roteiro
10. não crie prompt PipClip
11. não publique nada
12. não execute nada ainda
13. aguarde aprovação humana antes de criar cards reais

Responda no formato:

OBJETIVO:
WORKERS:
FLUXO OPERACIONAL:
PRIMEIRA RODADA PROPOSTA:
CARDS SUGERIDOS:
WORKER POR CARD:
KANBAN_STATUS:
PONTOS QUE EXIGEM APROVAÇÃO HUMANA:
PRÓXIMA AÇÃO:
```

---

# 8. Revisar resposta do orquestrador

Verificar se:

```text
- você leu AGENTS.md
- ele leu OpenSpec
- você entendeu os workers
- ele respeitou o fluxo
- ele respeitou as pausas humanas
- ele NÃO avançou automaticamente para conteúdo
```

---

# 9. Iniciar primeira rodada operacional

Depois da aprovação humana, enviar:

```text
Agora execute a primeira rodada operacional.

Use a ferramenta real do Kanban.
Não simule.
Não apenas descreva.
Crie os cards reais necessários para a primeira rodada.

Workers que devem ser usados:
- hermes-pesquisador-tiktok
- hermes-validador-searxng
- hermes-organizador-produtos

Workspace obrigatório:
dir:/root/projetos/hermes-tiktok-commerce-lab

Fonte inicial de produtos:
https://shopee.com.br/search?keyword=mais%20vendidos%20da%20shopee

Fluxo obrigatório da rodada:

1. Pesquisar produtos candidatos
   Worker: hermes-pesquisador-tiktok
   KANBAN_STATUS:
   Produto encontrado

2. Validar produtos encontrados com SearXNG
   Worker: hermes-validador-searxng
   KANBAN_STATUS:
   Validando com SearXNG

3. Organizar lista para decisão humana
   Worker: hermes-organizador-produtos
   KANBAN_STATUS:
   Aguardando escolha humana

Regras:
- Não avance para criação de conteúdo.
- Não crie roteiro.
- Não crie prompt PipClip.
- Não publique nada.
- Não use KANBAN_STATUS fora dos definidos no projeto.
- Pare obrigatoriamente em:
  KANBAN_STATUS:
  Aguardando escolha humana

Ao terminar, responda apenas com:
- cards criados
- assignee de cada card
- workspace usado
- KANBAN_STATUS esperado de cada card
- próximo ponto de aprovação humana
```

---

# 10. Verificar cards do Kanban

No terminal:

```bash
hermes kanban list
```

Acompanhar:

```bash
hermes kanban watch
```

---

# 11. Fluxo esperado da primeira rodada

```text
default/orquestrador
→ cria cards reais

hermes-pesquisador-tiktok
→ pesquisa produtos
→ KANBAN_STATUS: Produto encontrado

hermes-validador-searxng
→ valida externamente
→ KANBAN_STATUS: Validando com SearXNG

hermes-organizador-produtos
→ organiza lista
→ KANBAN_STATUS: Aguardando escolha humana
```

---

# 12. Primeira pausa obrigatória

Neste ponto:

```text
o sistema deve parar
```

A pessoa humana escolhe:

```text
- quais produtos continuar
- quais rejeitar
- quais precisam de mais pesquisa
```

O sistema NÃO deve continuar sozinho.

---

# 13. Continuar para criação de conteúdo

Depois da escolha humana:

```text
Agora continue apenas com os produtos aprovados.

Use:
hermes-criador-conteudo

KANBAN_STATUS:
Criando roteiro

Não avance para prompt PipClip sem aprovação humana do roteiro.
```

---

# 14. Segunda pausa obrigatória

Depois do roteiro:

```text
o sistema deve parar
```

A pessoa humana aprova ou rejeita o roteiro.

---

# 15. Continuar para PipClip

Depois da aprovação humana do roteiro:

```text
Agora continue para criação do prompt visual.

Use:
hermes-designer-pipclip

KANBAN_STATUS:
Criando prompt PipClip

Use o padrão obrigatório:

Estilo:
Cena:
Câmera:
Iluminação:
Ação por segundos:
Texto na tela:
Som ambiente:
Negativas:
```

---

# 16. Revisão final

Depois do prompt:

```text
Use:
hermes-revisor-final

KANBAN_STATUS:
Revisado
```

O revisor deve:

```text
- verificar exageros
- verificar claims sem prova
- verificar spam
- verificar texto ilegível
- verificar problemas visuais
- verificar riscos comerciais
```

---

# 17. Última pausa obrigatória

Depois da revisão:

```text
o sistema deve parar
```

A publicação:

```text
é manual
fica fora da automação
```

---

# 18. Ver logs se travar

```bash
journalctl --user -u hermes-gateway -n 100 --no-pager
```

---

# 19. Reiniciar gateway

```bash
hermes gateway stop
hermes gateway start
```

---

# 20. Regra final

```text
OpenSpec primeiro.
default coordena.
Workers executam.
Kanban controla estado operacional.
Pausas humanas são obrigatórias.
Não publicar automaticamente.
Shopee/TikTok geram pesquisa inicial.
SearXNG valida externamente.
Conteúdo só depois da aprovação humana.
Prompt PipClip só depois do roteiro aprovado.
Publicação continua manual.
```
---

# 21. Observação pós-teste em VPS fora do Brasil

Durante a gravação e execução real do laboratório na VPS Hetzner, foi identificado um limite importante:

```text
Alguns sites de marketplace e descoberta de produtos, como Shopee, TikTok e páginas relacionadas, podem bloquear ou limitar acessos vindos de VPS fora do Brasil.
```

Esse bloqueio pode acontecer por:

```text
- IP de datacenter
- IP europeu acessando páginas brasileiras
- proteção antifraude
- exigência de login
- captcha
- bloqueio regional
- limitação de navegação automatizada
- comportamento considerado suspeito pela plataforma
```

## Impacto no fluxo operacional

Na prática, isso significa que a VPS pode continuar funcionando bem para:

```text
- Hermes Agent
- Gateway
- Kanban
- OpenSpec
- workers
- organização das tarefas
- roteiros
- revisão
- documentação
```

Mas pode falhar ou ser limitada para:

```text
- buscar produtos diretamente na Shopee
- acessar páginas do TikTok Creative Center
- abrir páginas de produtos brasileiras
- validar rankings ou páginas públicas bloqueadas por IP
- navegar como se fosse um usuário brasileiro comum
```

## Ajuste oficial do fluxo

A partir deste teste, o fluxo passa a ser tratado como:

```text
modo humano assistido
```

Neste modo:

```text
1. A pessoa humana acessa os sites pelo próprio navegador local.
2. A pessoa humana copia links, prints, imagens ou dados básicos dos produtos.
3. Os dados são enviados para os workers analisarem.
4. O Hermes organiza, valida, cria cards e controla o Kanban.
5. Os agentes trabalham sobre o material fornecido ou sobre fontes acessíveis.
6. A decisão humana continua obrigatória antes de conteúdo, prompt visual e publicação.
```

## Uso de imagens locais de produtos

Quando a busca direta pela VPS falhar, é permitido usar imagens locais e dados enviados manualmente.

Exemplos de entrada humana:

```text
- print da página do produto
- imagem do produto
- nome do produto
- preço observado
- link do produto
- categoria
- comentários observados
- indícios de tendência
- observação manual sobre demanda
```

Os workers devem tratar esse material como evidência fornecida pela pessoa humana, não como prova automática de venda ou tendência.

## Regra importante

```text
Não burlar bloqueio.
Não contornar captcha.
Não mascarar IP para violar regra de plataforma.
Não fazer scraping agressivo.
Não afirmar que o produto vende muito sem evidência clara.
Não transformar limitação técnica em promessa falsa de automação.
```

## Estado do teste gravado

Na gravação desta etapa:

```text
- a infraestrutura Hermes funcionou
- o Gateway funcionou
- o Kanban funcionou
- o OpenSpec ficou dentro do projeto
- os workers foram criados
- os SOUL.md foram separados por worker
- o CLI funcionou melhor que o Workspace para execução real
- alguns agentes falharam durante a execução operacional
- o bloqueio por IP da VPS apareceu como limitação real para pesquisa de produtos
```

## Melhorias recomendadas

Como melhoria complementar, o laboratório pode ser testado em instalação local usando nuvem para o modelo.

Objetivos recomendados:

```text
- reduzir bloqueios por IP estrangeiro
- usar o navegador local da máquina
- melhorar os SOUL.md dos agentes
- revisar por que alguns workers falharam
- deixar instruções mais objetivas para cada agente
- melhorar a passagem de tarefa entre orquestrador e workers
- reforçar o modo humano assistido
```

## Conclusão operacional

```text
VPS fora do Brasil é boa para infraestrutura e orquestração.

Para pesquisa real em plataformas brasileiras de marketplace e redes sociais, o caminho mais confiável é usar modo humano assistido ou execução local com navegador do próprio usuário.
```

