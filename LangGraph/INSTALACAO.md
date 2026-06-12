# Como instalar e configurar LangGraph Studio no Ubuntu/WSL

## 1. Atualizar o sistema

```bash
sudo apt update
```

```bash
sudo apt install -y curl git python3 python3-pip
```

## 2. Instalar o uv

```bash
curl -LsSf "https://astral.sh/uv/install.sh" | sh
```

```bash
source "$HOME/.bashrc"
```

```bash
uv --version
```

## 3. Criar a pasta de projetos

```bash
mkdir -p "$HOME/projetos"
```

```bash
cd "$HOME/projetos"
```

## 4. Criar o projeto LangGraph

```bash
uvx --from "langgraph-cli@latest" langgraph new "social-media-agent" --template "new-langgraph-project-python"
```

```bash
cd "social-media-agent"
```

## 5. Instalar dependências

```bash
uv sync --dev -U
```

## 6. Conferir arquivos do projeto

```bash
ls
```

```bash
cat "langgraph.json"
```

## 7. Criar arquivo de ambiente

```bash
cp ".env.example" ".env" 2>/dev/null || touch ".env"
```

```bash
nano ".env"
```

Exemplo:

```env
OPENAI_API_KEY="SEU_TOKEN_AQUI"
LANGSMITH_API_KEY="SEU_TOKEN_LANGSMITH_AQUI"
LANGSMITH_TRACING="true"
LANGSMITH_PROJECT="social-media-agent"
```

## 8. Criar grafo simples de mídias sociais

```bash
nano "src/agent/graph.py"
```

Conteúdo:

```python
from typing import TypedDict
from langgraph.graph import StateGraph, START, END


class SocialState(TypedDict):
    tema: str
    publico: str
    plataforma: str
    objetivo: str
    gancho: str
    roteiro: str
    legenda: str
    hashtags: str


def criar_gancho(state: SocialState):
    return {
        "gancho": f"Você está tentando entender {state['tema']}, mas ninguém explica isso de forma prática para {state['publico']}. Hoje eu vou mostrar isso em formato direto para {state['plataforma']}."
    }


def criar_roteiro(state: SocialState):
    return {
        "roteiro": f"""{state['gancho']}

1. Mostre o problema em uma frase.
2. Explique {state['tema']} com uma analogia simples.
3. Dê um exemplo prático.
4. Feche com uma chamada para ação ligada a: {state['objetivo']}."""
    }


def criar_legenda(state: SocialState):
    return {
        "legenda": f"Conteúdo rápido sobre {state['tema']} para quem quer aprender de forma prática no {state['plataforma']}. Salve para revisar depois.",
        "hashtags": "#IA #DataScience #Python #Automacao #LangGraph"
    }


builder = StateGraph(SocialState)

builder.add_node("criar_gancho", criar_gancho)
builder.add_node("criar_roteiro", criar_roteiro)
builder.add_node("criar_legenda", criar_legenda)

builder.add_edge(START, "criar_gancho")
builder.add_edge("criar_gancho", "criar_roteiro")
builder.add_edge("criar_roteiro", "criar_legenda")
builder.add_edge("criar_legenda", END)

graph = builder.compile()
```

## 9. Rodar o LangGraph Studio

```bash
uv run langgraph dev
```

Resultado esperado:

```text
Ready!
API: http://localhost:2024
Docs: http://localhost:2024/docs
Studio Web UI: https://smith.langchain.com/studio/?baseUrl=http://127.0.0.1:2024
```

## 10. Abrir o Studio

Abra no navegador:

```text
https://smith.langchain.com/studio/?baseUrl=http://127.0.0.1:2024
```

## 11. Testar pela API

Abra outro terminal no Ubuntu/WSL:

```bash
curl -s --request POST \
  --url "http://localhost:2024/runs/stream" \
  --header "Content-Type: application/json" \
  --data '{
    "assistant_id": "agent",
    "input": {
      "tema": "LangGraph para criar conteúdo",
      "publico": "criadores iniciantes de conteúdo técnico",
      "plataforma": "YouTube Shorts",
      "objetivo": "levar a pessoa para o vídeo completo"
    },
    "stream_mode": "values"
  }'
```

## 12. Rodar em outra porta se der conflito

```bash
uv run langgraph dev --port 2025
```

Abra:

```text
https://smith.langchain.com/studio/?baseUrl=http://127.0.0.1:2025
```

## 13. Parar o servidor

No terminal onde o servidor está rodando:

```text
CTRL+C
```
