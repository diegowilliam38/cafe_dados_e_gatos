# Como criar um agente de pesquisa de mercado no CrewAI Studio em modo híbrido

## Objetivo

Criar um agente simples no **CrewAI Studio**, rodando no Linux, usando uma configuração híbrida:

```text
CrewAI Studio + Ollama + MiniMax
```

Neste modelo:

```text
Ollama = modelo local para testes, economia e tarefas leves
MiniMax = modelo cloud para tarefas mais pesadas, análise melhor e respostas mais refinadas
```

---

## 1. Instalar o CrewAI Studio sem Docker

### Onde rodar

No terminal do Linux.

### Baixar o projeto

```bash
cd "$HOME"
git clone "https://github.com/strnad/CrewAI-Studio.git"
cd "$HOME/CrewAI-Studio"
```

### Instalar com ambiente virtual

```bash
./install_venv.sh
```

### Rodar o CrewAI Studio

```bash
./run_venv.sh
```

### Acessar no navegador

```text
http://localhost:8501
```

---

## 2. Preparar o Ollama

### Verificar se o Ollama está instalado

```bash
ollama --version
```

### Subir o Ollama

```bash
ollama serve
```

Se aparecer que a porta já está em uso, provavelmente o Ollama já está rodando.

### Baixar um modelo para teste

```bash
ollama pull llama3.2
```

Ou, para máquina mais simples:

```bash
ollama pull phi3.5
```

---

## 3. Configurar conexão com Ollama no CrewAI Studio

Na tela de conexão ou configuração de modelo, usar:

```text
Provider: Custom OpenAI Compatible
Connection name: Ollama
API key: valor ficticio para teste local
Base URL: http://localhost:11434/v1
```

### Modelo

Usar um modelo disponível no Ollama.

Exemplo:

```text
llama3.2
```

Ou:

```text
phi3.5
```

Se a interface pedir o nome no formato com prefixo, testar:

```text
ollama/llama3.2
```

ou:

```text
ollama/phi3.5
```

---

## 4. Configurar conexão com MiniMax

### Observação

O MiniMax deve ser configurado como provedor compatível com OpenAI, caso sua conta/API disponibilize endpoint nesse formato.

Na tela de conexão ou configuração de modelo, usar:

```text
Provider: Custom OpenAI Compatible
Connection name: MiniMax
API key: SUA_CHAVE_MINIMAX
Base URL: URL_BASE_COMPATIVEL_COM_OPENAI_DA_MINIMAX
```

### Modelo

Usar o nome do modelo MiniMax disponível na sua conta/API.

Exemplo genérico:

```text
NOME_DO_MODELO_MINIMAX
```

### Importante

```text
Não expor a chave MiniMax no vídeo.
Não colocar a chave real no GitHub.
Usar sempre placeholder em documentação pública.
```

---

## 5. Estratégia híbrida

A ideia é usar cada modelo onde ele faz mais sentido.

```text
Ollama:
testes locais
tarefas simples
economia de API
execuções rápidas
fluxos de baixo risco

MiniMax:
análise mais elaborada
respostas mais refinadas
tarefas com maior exigência de qualidade
relatórios finais
síntese estratégica
```

### Explicação para o vídeo

```text
Neste teste, eu vou usar o CrewAI Studio em modo híbrido.

A ideia não é escolher apenas local ou apenas nuvem.

Para tarefas mais simples, eu posso usar o Ollama rodando na minha máquina.

Para tarefas que precisam de uma resposta mais forte, eu posso usar um modelo cloud como o MiniMax.

Assim, eu monto uma equipe de agentes mais flexível, escolhendo o modelo mais adequado para cada parte do fluxo.
```

---

## 6. Criar o agente

### Tela

Abrir a tela de criação de agente no CrewAI Studio.

### Agent Configuration

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

## 7. Modelo recomendado para este agente

Para o primeiro teste, usar:

```text
MiniMax
```

Motivo:

```text
Este agente vai fazer análise, síntese e organização de ideias.
Para esse tipo de tarefa, um modelo cloud mais forte pode entregar uma resposta mais estruturada.
```

Alternativa econômica:

```text
Ollama
```

Motivo:

```text
Usar Ollama quando o objetivo for testar a estrutura do fluxo sem gastar API.
```

---

## 8. Versão em português para explicar no vídeo

```text
Aqui eu estou criando um agente com o papel de analista de pesquisa de mercado.

A função dele é buscar, organizar e resumir informações confiáveis para apoiar decisões.

Neste exemplo, eu posso usar um modelo local com Ollama ou um modelo cloud como MiniMax.

O ponto principal é que o CrewAI Studio permite montar o fluxo de agentes e escolher o modelo mais adequado para cada etapa.
```

---

## 9. Capabilities

Para o primeiro teste, manter simples.

```text
Reasoning: ligado
Memory: desligado
```

### Explicação para o vídeo

```text
Neste primeiro teste, eu vou deixar o raciocínio ligado para o agente conseguir organizar melhor a análise.

A memória eu vou deixar desligada, porque a ideia agora é testar um fluxo simples, sem persistência entre execuções.
```

---

## 10. Tools

Para o primeiro teste, não selecionar ferramentas extras.

```text
Tools: nenhuma
Integration apps: nenhuma
MCP servers: nenhum
```

### Explicação para o vídeo

```text
Neste primeiro momento, eu não vou adicionar ferramentas externas.

A ideia é começar simples: criar o agente, conectar os modelos e testar se ele consegue gerar uma análise estruturada.

Depois, em testes mais avançados, esse agente pode receber ferramentas de busca, leitura de arquivos, APIs ou integrações externas.
```

---

## 11. Criar uma tarefa para o agente

### Task name

```text
Market Research Report
```

### Description

```text
Analyze the current market opportunities for educational content about local AI agents, Ollama, cloud models, and multi-agent systems. Identify audience interests, possible content angles, risks, and practical recommendations.
```

### Expected output

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

## 12. Versão em português da tarefa para explicar no vídeo

```text
Agora eu vou criar uma tarefa para esse agente.

A tarefa será analisar oportunidades de conteúdo educacional sobre agentes de IA, Ollama, modelos cloud e sistemas multiagentes.

A saída esperada é um relatório em Markdown, com visão de mercado, público-alvo, interesses, dores, oportunidades de conteúdo, riscos e recomendações práticas.
```

---

## 13. Criar a Crew

### Nome da Crew

```text
Market Research Crew
```

### Agente

```text
Market Research Analyst
```

### Tarefa

```text
Market Research Report
```

### Modelo sugerido

```text
MiniMax
```

### Alternativa para teste econômico

```text
Ollama
```

### Explicação para o vídeo

```text
Depois de criar o agente e a tarefa, eu monto a crew.

A crew é a equipe de trabalho.

Neste exemplo inicial, a equipe tem apenas um agente, mas a lógica pode crescer.

Depois eu posso adicionar um agente redator, um agente revisor e um agente estrategista.

Também posso escolher modelos diferentes para diferentes etapas do fluxo.
```

---

## 14. Teste inicial

Prompt de teste:

```text
Analyze the market opportunity for a YouTube channel that teaches local AI agents, Ollama, cloud models, and multi-agent workflows to beginners and intermediate users.
```

Resultado esperado:

```text
Um relatório estruturado em Markdown com análise de mercado, público-alvo, oportunidades, riscos e recomendações.
```

---

## 15. Possível evolução com mais agentes

Depois do primeiro teste, criar uma equipe com mais agentes.

### Agente 1

```text
Market Research Analyst
Modelo: MiniMax
Função: analisar mercado, público e oportunidades
```

### Agente 2

```text
Content Strategist
Modelo: MiniMax ou Ollama
Função: transformar a análise em ideias de conteúdo
```

### Agente 3

```text
Technical Reviewer
Modelo: Ollama ou MiniMax
Função: revisar clareza, consistência e limitações técnicas
```

---

## 16. Observação importante

```text
Este modelo é apenas o primeiro teste.

A proposta não é criar uma automação complexa logo de início.

A ideia é validar o fluxo básico:

1. instalar o CrewAI Studio;
2. conectar com Ollama;
3. conectar com MiniMax;
4. criar um agente;
5. criar uma tarefa;
6. montar uma crew;
7. executar o fluxo;
8. analisar o resultado.
```

---

## 17. Possíveis evoluções

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
Comparação entre modelos locais e cloud
Fluxos híbridos com economia de custo
```

---

## 18. Diferença prática para explicar no vídeo

```text
O CrewAI Studio é interessante porque permite criar equipes de agentes de forma direta e visual.

Ele não obriga a usar apenas modelo local, nem apenas modelo cloud.

Eu posso usar Ollama para tarefas locais e econômicas.

Também posso usar MiniMax para tarefas que exigem respostas mais fortes.

O foco aqui é montar uma equipe de agentes flexível:

criar agentes,
definir tarefas,
escolher modelos,
montar uma equipe
e executar um fluxo multiagente.

Para muitos casos, isso já é exatamente o que a pessoa precisa.
```
