# Nota pós-gravação - Hermes TikTok Commerce Lab

## Contexto

Durante a gravação do laboratório Hermes TikTok Commerce Lab em VPS Hetzner Ubuntu, a infraestrutura principal funcionou.

Funcionaram:

```text
Hermes Agent
Gateway
Kanban
OpenSpec
workers criados via CLI
SOUL.md separado por worker
execução operacional pelo terminal/CLI
```

## Limitação encontrada

No contexto de usar uma VPS fora do Brasil, alguns sites usados para busca de produtos podem bloquear o acesso.

Exemplos:

```text
Shopee Brasil
TikTok
TikTok Creative Center
TikTok Shop / Seller Center Brasil
páginas públicas de produtos com proteção antifraude
```

Motivos prováveis:

```text
IP europeu
IP de datacenter
proteção antifraude
bloqueio regional
captcha
exigência de login
limitação contra navegação automatizada
```

## Decisão operacional

O projeto deve seguir em modo humano assistido.

Nesse modo:

```text
1. A pessoa humana acessa os sites pelo navegador local.
2. A pessoa humana coleta prints, links, imagens ou dados básicos.
3. O material é enviado para os workers.
4. Os workers analisam, organizam, validam e registram riscos.
5. O Kanban continua sendo usado como controle operacional real.
6. A decisão humana continua obrigatória antes de conteúdo, prompt visual e publicação.
```

## Regra

```text
Não burlar bloqueio.
Não contornar captcha.
Não fazer scraping agressivo.
Não coletar dados privados.
Não prometer automação total quando a plataforma bloqueia acesso.
Não afirmar venda, ranking ou tendência sem evidência clara.
```

## Melhorias recomendadas

Em uma etapa complementar, recomenda-se revisar:

```text
SOUL.md dos workers
falhas dos agentes durante o teste
uso de imagens locais de produtos
entrada manual de links e prints
passagem de tarefa entre orquestrador e workers
comportamento dos workers quando a fonte bloquear acesso
```

## Conclusão

```text
A VPS fora do Brasil é boa para infraestrutura, orquestração, Kanban e documentação.
```
