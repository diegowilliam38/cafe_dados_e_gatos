# Segurança

## Objetivo

Definir cuidados simples para publicar e operar o **Hermes Agent Lab na Hetzner** sem expor dados sensíveis, sem abrir serviços sem necessidade e sem criar riscos comerciais.

## Regra rápida

Antes de publicar documentação, print, vídeo, log ou arquivo no GitHub, remova dados reais e mantenha apenas exemplos.

```text
Pode publicar:
.env.example
tokens fictícios
IPs fictícios
comandos genéricos
prints sem dados sensíveis

Não publique:
.env real
token real
senha real
chave de API real
IP sensível
log com segredo
print com painel, token, email privado ou credencial
```

## Checklist antes de publicar

- [ ] O arquivo `.env` real não foi enviado.
- [ ] Tokens, senhas e chaves foram removidos.
- [ ] IPs sensíveis da VPS ou do Tailscale foram ocultados quando necessário.
- [ ] Prints e logs foram revisados.
- [ ] Links afiliados foram conferidos.
- [ ] Claims de produto têm fonte ou foram removidos.
- [ ] Não há promessa de venda, renda ou comissão garantida.
- [ ] Não há uso indevido de marca, imagem, logo ou pessoa.
- [ ] O conteúdo público passou por revisão humana.

## Portas e acesso

Use Tailscale como caminho preferencial para acessar serviços internos.

Evite expor diretamente:

```text
3000  Hermes Workspace
8080  SearXNG
8642  Hermes Gateway/API
9119  Hermes Dashboard
11434 Ollama
```

Só exponha porta pública quando houver necessidade clara, regra de firewall revisada e aprovação humana.

## Pesquisa e navegador controlado

O navegador controlado pode apoiar pesquisa assistida, mas não deve contornar regras de plataforma.

Não usar para:

- burlar login
- contornar captcha
- furar paywall
- fazer scraping agressivo
- coletar dados privados
- publicar automaticamente
- enviar mensagens automáticas
- seguir pessoas automaticamente

Quando uma plataforma bloquear acesso por região, datacenter, login, captcha ou antifraude, use o modo humano assistido: a pessoa coleta link, print ou dado básico e o agente analisa o material recebido.

## Conteúdo, afiliados e criativos

- Não prometer vendas, renda ou comissão garantida.
- Não usar linguagem de enriquecimento rápido.
- Não afirmar que um produto é o mais vendido sem fonte clara.
- Validar claims de produto antes de transformar em roteiro ou criativo.
- Informar conteúdo afiliado, patrocinado ou comissionado quando necessário.
- Não usar imagem, marca, logo ou pessoa sem autorização.
- Não criar antes/depois sem base.
- Não criar representação falsa ou enganosa de produto com ferramenta visual.
- Publicar manualmente, depois de revisão humana.

## Aprovação humana obrigatória

Peça aprovação humana antes de:

- publicar conteúdo
- enviar mensagem
- alterar firewall
- expor porta pública
- trocar senha, token ou chave
- apagar ou sobrescrever arquivo
- executar ação externa ou irreversível
- usar criativo visual em público

## Critério final

Se houver dúvida sobre segurança, privacidade, promessa comercial, uso de marca ou exposição pública, pare e peça revisão humana.

