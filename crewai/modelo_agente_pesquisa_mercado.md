# COMO CRIAR UM AGENTE DE PESQUISA DE MERCADO NO CREWAI STUDIO

## Objetivo

Criar um agente simples no **CrewAI Studio**, rodando localmente no Linux, usando **Ollama** como provedor de modelo.

Este modelo serve para testes iniciais e para demonstrar, em vídeo, como criar um agente multiagente de forma visual.

---

# 1. Instalação do CrewAI Studio sem Docker

## Onde rodar

No terminal do Linux.

## Baixar o projeto

```bash
cd "$HOME"
git clone "https://github.com/strnad/CrewAI-Studio.git"
cd "$HOME/CrewAI-Studio"
```

## Instalar com ambiente virtual

```bash
./install_venv.sh
```

## Rodar o CrewAI Studio

```bash
./run_venv.sh
```

## Acessar no navegador

```text
http://localhost:8501
```

---

# 2. Preparar o Ollama

## Verificar se o Ollama está instalado

```bash
ollama --version
```

## Subir o Ollama

```bash
ollama serve
```

Se aparecer que a porta já está em uso, provavelmente o Ollama já está rodando.

## Baixar um modelo para teste

```bash
ollama pull llama3.2
```

Ou, para máquina mais simples:

```bash
ollama pull phi3.5
```

---

# 3. Configurar conexão com Ollama no CrewAI Studio

Na tela de conexão ou configuração de modelo, usar:

```text
Provider: Custom OpenAI Compatible
Connection name: Ollama
API key: valor ficticio para teste local
Base URL: http://localhost:11434/v1
```

## Modelo

Usar um modelo disponível no Ollama.

Exemplo:

```text
llama3.2
```

Ou:

```text
phi3.5
```

Observação: se a interface pedir o nome no formato com prefixo, testar:

```text
ollama/llama3.2
```

ou:

```text
ollama/phi3.5
```

---

# 4. Criar o agente

## Tela

Abrir a tela de criação de agente no CrewAI Studio.

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

---

# 5. Versão em português para explicar no vídeo

```text
Aqui eu estou criando um agente com o papel de analista de pesquisa de mercado.

A função dele é buscar, organizar e resumir informações confiáveis para apoiar decisões.

Na prática, esse tipo de agente pode ajudar a analisar tendências, concorrentes, comportamento do público e oportunidades de conteúdo ou negócio.
```

---

# 6. Capabilities

Para o primeiro teste, manter simples.

```text
Reasoning: ligado
Memory: desligado
```

## Explicação para o vídeo

```text
Neste primeiro teste, eu vou deixar o raciocínio ligado para o agente conseguir organizar melhor a análise.

A memória eu vou deixar desligada, porque a ideia agora é testar um fluxo simples, sem persistência entre execuções.
```

---

# 7. Tools

Para o primeiro teste, não selecionar ferramentas extras.

```text
Tools: nenhuma
Integration apps: nenhuma
MCP servers: nenhum
```

## Explicação para o vídeo

```text
Neste primeiro momento, eu não vou adicionar ferramentas externas.

A ideia é começar simples: criar o agente, conectar ao modelo local e testar se ele consegue gerar uma análise estruturada.

Depois, em testes mais avançados, esse agente pode receber ferramentas de busca, leitura de arquivos, APIs ou integrações externas.
```

---

# 8. Criar uma tarefa para o agente

## Task name

```text
Market Research Report
```

## Description

```text
Analyze the current market opportunities for educational content about local AI agents, Ollama, and multi-agent systems. Identify audience interests, possible content angles, risks, and practical recommendations.
```

## Expected output

```text
A structured markdown report with:

1. Market overview
2. Target audience
3. Main interests and pain points
4. Content opportunities
5. Risks or limitations
6. Practical recommendations
```

---

# 9. Versão em português da tarefa para explicar no vídeo

```text
Agora eu vou criar uma tarefa para esse agente.

A tarefa será analisar oportunidades de conteúdo educacional sobre agentes de IA locais, Ollama e sistemas multiagentes.

A saída esperada é um relatório em Markdown, com visão de mercado, público-alvo, interesses, dores, oportunidades de conteúdo, riscos e recomendações práticas.
```

---

# 10. Criar a Crew

## Nome da Crew

```text
Market Research Crew
```

## Agente

```text
Market Research Analyst
```

## Tarefa

```text
Market Research Report
```

## Explicação para o vídeo

```text
Depois de criar o agente e a tarefa, eu monto a crew.

A crew é a equipe de trabalho.

Neste exemplo inicial, a equipe tem apenas um agente, mas a lógica pode crescer.

Depois eu posso adicionar um agente redator, um agente revisor e um agente estrategista, criando um fluxo multiagente mais completo.
```

---

# 11. Teste inicial

Prompt de teste:

```text
Analyze the market opportunity for a YouTube channel that teaches local AI agents, Ollama, and multi-agent workflows to beginners and intermediate users.
```

Resultado esperado:

```text
Um relatório estruturado em Markdown com análise de mercado, público-alvo, oportunidades, riscos e recomendações.
```

---

# 12. Observação importante

```text
Este modelo é apenas o primeiro teste.

A proposta não é criar uma automação complexa logo de início.

A ideia é validar o fluxo básico:

1. instalar o CrewAI Studio;
2. conectar com Ollama;
3. criar um agente;
4. criar uma tarefa;
5. montar uma crew;
6. executar o fluxo;
7. analisar o resultado.
```

---

# 13. Possíveis evoluções

Depois do primeiro teste, o agente pode ser adaptado para:

```text
Automação de conteúdo
Pesquisa para vídeos
Análise de concorrentes
Relatórios semanais
Triagem de informações
Planejamento editorial
Pesquisa de mercado para produtos digitais
Análise de tendências em IA
```

---

# 14. Diferença prática para explicar no vídeo

```text
O CrewAI Studio é interessante porque ele permite criar equipes de agentes de forma mais direta e visual.

Ele não tenta ser um grande centro de comando como outras ferramentas.

O foco aqui é mais objetivo:

criar agentes,
definir tarefas,
montar uma equipe
e executar um fluxo multiagente.

Para muitos casos, isso já é exatamente o que a pessoa precisa.
```
