# OpenSpec

## Objetivo

Este documento resume o contrato operacional do projeto **Hermes TikTok Commerce Lab**.

O OpenSpec define o fluxo de trabalho dos agentes antes da execução: pesquisa, validação, escolha humana, roteiro, prompt visual, revisão, Kanban e documentação.

O OpenSpec não valida instalação, não audita infraestrutura e não substitui a documentação técnica da VPS.

## Projeto

```text
Hermes TikTok Commerce Lab
Como usar Hermes Agent para vender no TikTok com IA
```

## Escopo incluído

- Operação de afiliados no TikTok como caso de uso.
- Pesquisa de produtos em destaque ou produtos candidatos.
- Validação externa com SearXNG.
- Organização de lista de produtos para escolha humana.
- Criação de ângulos, hooks, roteiros curtos, CTA e legenda.
- Criação de prompts visuais no padrão PipClip.
- Revisão de promessas comerciais.
- Controle operacional em Kanban.
- Modo humano assistido quando a plataforma bloquear acesso pela VPS.
- Documentação para GitHub e material de apoio para YouTube.

## Escopo técnico relacionado

A infraestrutura continua sendo documentada nos guias de instalação:

- VPS Ubuntu Hetzner
- Tailscale
- Firewall
- Ollama / Ollama Cloud
- Docker apenas para SearXNG
- Hermes Agent sem Docker
- Hermes Gateway/API
- Hermes Dashboard
- Hermes Workspace
- OpenSpec
- Navegador controlado quando disponível

## Escopo excluído

- Garantia de vendas, renda ou comissão.
- Promessa de renda.
- Enriquecimento rápido.
- Spam.
- Burla de regras do TikTok.
- Burla de login, captcha, paywall ou restrição de plataforma.
- Scraping agressivo.
- Coleta de dados privados.
- Automação de publicação sem revisão humana.
- Integração automática com TikTok não implementada.
- Integração automática com PipClip não implementada.
- Instalação completa do ComfyUI neste momento.

## Fluxo operacional

```text
produto observado ou indicado
-> validação externa
-> lista de candidatos
-> escolha humana
-> roteiro
-> prompt PipClip
-> vídeo
-> revisão
-> atualização do Kanban
```

## Modo humano assistido

Durante a gravação, a VPS fora do Brasil funcionou bem para infraestrutura, Hermes, Gateway, OpenSpec e Kanban, mas alguns sites brasileiros ou plataformas sociais podem bloquear acesso por IP de datacenter, IP europeu, captcha, login ou proteção antifraude.

Quando isso acontecer, o fluxo correto é:

```text
1. A pessoa humana acessa os sites pelo navegador local.
2. A pessoa humana coleta links, prints, imagens ou dados básicos.
3. O material é enviado para os workers.
4. Os workers analisam, organizam, validam e registram riscos.
5. O Kanban continua sendo usado como controle operacional.
6. A decisão humana continua obrigatória antes de roteiro, prompt visual e publicação.
```

## Fontes permitidas

- TikTok Creative Center
- TikTok Creative Center Top Products
- TikTok Creative Center Trends
- TikTok Search
- TikTok Shop / Seller Center, quando disponível
- SearXNG para validação externa
- sites externos de reviews
- sites externos de reclamações
- sites externos de comparação de preços
- links, prints, imagens ou dados fornecidos manualmente pela pessoa humana

## Regras de pesquisa

- O TikTok deve ser usado apenas como sinal de tendência, quando acessível.
- O SearXNG deve ser usado para validação externa.
- O Hermes não deve afirmar que um produto é mais vendido sem fonte clara.
- O Hermes não deve afirmar que um produto vende muito sem evidência observável.
- O Hermes não deve burlar login, captcha, paywall ou restrição de plataforma.
- O Hermes não deve fazer scraping agressivo.
- O Hermes não deve coletar dados privados.
- Os agentes devem separar fato, hipótese, recomendação e opinião.
- Toda publicação precisa de revisão humana.

## Workers usados na gravação

```text
default = CEO / Orquestrador

hermes-pesquisador-tiktok
hermes-validador-searxng
hermes-organizador-produtos
hermes-criador-conteudo
hermes-designer-pipclip
hermes-revisor-final
```

## Regra de pausas humanas

O sistema deve parar para aprovação humana antes de:

- escolher produto
- criar conteúdo final
- transformar roteiro em prompt visual
- usar criativo em ferramenta externa
- publicar qualquer conteúdo
- executar ação externa, destrutiva ou irreversível

## Ferramentas opcionais

- Canva
- CapCut
- PipClip ([link de afiliada do PipClip](https://pipclip.ai/?afid=2Z2MW26))
- ComfyUI como opção avançada para quem tem GPU

## Regras para prompts de vídeo no PipClip

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

- Prompts devem pedir vídeo vertical 9:16 quando o destino for TikTok, Reels ou Shorts.
- Para vídeos de 10 a 15 segundos, usar poucos momentos e cenas simples.
- Para vídeos de 30 segundos, permitir mais etapas, sem excesso de informação.
- Texto na tela deve ser curto e simples.
- Não usar frases longas.
- Para vídeos de produto, priorizar imagem, demonstração e contexto de uso.
- Para vídeos de produto, evitar texto atrapalhando a cena ou cobrindo o produto.
- Para vídeos educativos ou divulgação de canal, usar textos curtos e simples.
- Todo criativo precisa passar pelo Revisor de Promessas.
- Todo criativo precisa de aprovação humana antes de publicação.

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

## Critérios de aceite

- A infraestrutura Hermes está documentada.
- O uso de Docker está limitado ao SearXNG.
- Hermes Agent, Dashboard e Workspace aparecem sem Docker.
- O fluxo operacional da gravação está documentado.
- O modo humano assistido está documentado.
- Os workers têm papéis definidos.
- As promessas comerciais passam por revisão.
- O projeto não promete vendas, renda ou comissão garantida.
- Todo conteúdo público exige revisão humana.
