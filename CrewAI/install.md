# Como instalar CrewAI com MiniMax

## 1. Atualizar o Ubuntu

```bash
sudo apt update
```

```bash
sudo apt install -y curl git python3 python3-pip python3-venv
```

## 2. Verificar Python

```bash
python3 --version
```

Resultado esperado:

```text
Python 3.10.x até Python 3.13.x
```

## 3. Instalar uv

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

```bash
source "$HOME/.bashrc"
```

```bash
uv --version
```

## 4. Instalar CrewAI

```bash
uv tool install crewai
```

```bash
uv tool update-shell
```

```bash
source "$HOME/.bashrc"
```

```bash
crewai --version
```

```bash
uv tool list
```

## 5. Criar projeto

```bash
mkdir -p "$HOME/crewai-lab"
```

```bash
cd "$HOME/crewai-lab"
```

```bash
crewai create crew "cafe_dados_crew"
```

```bash
cd "$HOME/crewai-lab/cafe_dados_crew"
```

## 6. Instalar dependências do projeto

```bash
crewai install
```

## 7. Configurar MiniMax

```bash
nano ".env"
```

Cole no arquivo:

```env
MODEL="openai/MiniMax-M3"
OPENAI_API_KEY="SUA_CHAVE_MINIMAX_AQUI"
OPENAI_API_BASE="https://api.minimax.io/v1"
```

Salvar:

```text
CTRL+O
ENTER
CTRL+X
```

## 8. Testar a chave MiniMax antes do CrewAI

```bash
source ".env"
```

```bash
curl "https://api.minimax.io/v1/chat/completions" \
  -H "Authorization: Bearer $OPENAI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "MiniMax-M3",
    "messages": [
      {
        "role": "user",
        "content": "Responda apenas: MiniMax funcionando."
      }
    ]
  }'
```

Resultado esperado:

```text
MiniMax funcionando.
```

## 9. Rodar CrewAI

```bash
crewai run
```

## 10. Ver estrutura criada

```bash
tree -a -I ".venv|__pycache__|.git"
```

Se não tiver tree:

```bash
sudo apt install -y tree
```

```bash
tree -a -I ".venv|__pycache__|.git"
```

## 11. Arquivos principais

```bash
ls -la
```

```bash
ls -la "src/cafe_dados_crew"
```

```bash
ls -la "src/cafe_dados_crew/config"
```

## 12. Editar agentes

```bash
nano "src/cafe_dados_crew/config/agents.yaml"
```

## 13. Editar tarefas

```bash
nano "src/cafe_dados_crew/config/tasks.yaml"
```

## 14. Editar orquestração

```bash
nano "src/cafe_dados_crew/crew.py"
```

## 15. Editar entrada principal

```bash
nano "src/cafe_dados_crew/main.py"
```

## 16. Rodar novamente

```bash
crewai run
```

## 17. Atualizar CrewAI depois

```bash
uv tool install crewai --upgrade
```

```bash
crewai --version
```

## 18. Corrigir PATH se o comando crewai não aparecer

```bash
uv tool update-shell
```

```bash
source "$HOME/.bashrc"
```

```bash
which crewai
```

## 19. Conferir variáveis do MiniMax

```bash
grep -n "MODEL\|OPENAI_API_KEY\|OPENAI_API_BASE" ".env"
```

## 20. Abrir o projeto no VS Code

```bash
code .
```
