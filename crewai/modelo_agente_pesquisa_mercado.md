# Modelo de agente CrewAI - Market Research Analyst

## Objetivo

Modelo simples para preencher a tela New Agent do CrewAI Platform durante testes iniciais.

## Connection / LLM

```text
Provider: Custom OpenAI Compatible
Connection name: Ollama
API key: valor ficticio para teste local
Base URL: http://localhost:11434/v1
```

## Agent Configuration

### Role

```text
Market Research Analyst
```

### Goal

```text
Gather and synthesize insights from trusted sources to guide strategic decisions.
```

### Backstory

```text
You are a seasoned market research analyst with strong experience in industry trends, consumer behavior, competitive analysis, and data interpretation. Your job is to transform scattered information into clear, useful, and practical insights for decision-making.
```

## Versao em portugues para explicar no video

```text
Aqui eu estou criando um agente com o papel de analista de pesquisa de mercado.

A funcao dele e buscar, organizar e resumir informacoes confiaveis para apoiar decisoes.

Na pratica, esse tipo de agente poderia ajudar a analisar tendencias, concorrentes, comportamento do publico e oportunidades de conteudo ou negocio.
```

## Capabilities

Para teste inicial, deixar simples.

```text
Reasoning: opcional
Memory: opcional
```

Sugestao para primeiro teste:

```text
Reasoning: ligado
Memory: desligado
```

## Tools

Para primeiro teste, nao selecionar ferramentas extras.

```text
Tools: nenhuma
Integration apps: nenhuma
MCP servers: nenhum
```

## Observacao

```text
Este modelo e apenas para testar a criacao de agente no CrewAI Platform.
Depois, o agente pode ser adaptado para automacao de conteudo, analise de dados, pesquisa para videos, relatorios semanais ou triagem de informacoes.
```
