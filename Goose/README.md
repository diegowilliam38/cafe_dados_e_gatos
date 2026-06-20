# 🧾 Goose Recipes

Coleção de **recipes YAML** para o [Goose](https://github.com/block/goose). Cada `.yaml` é uma tarefa reutilizável que pode ser executada via CLI ou UI.

> 📚 Para o **guia completo do formato YAML** (campos, parâmetros, extensions, settings), veja [`../goose-recipes.md`](../goose-recipes.md).

---

## 📦 Recipes Disponíveis

| Recipe                 | Arquivo                                          | Descrição                                                                                            |
| ---------------------- | ------------------------------------------------ | ---------------------------------------------------------------------------------------------------- |
| ⭐ **File Summarizer** | [`file-summarizer.yaml`](./file-summarizer.yaml) | **🌟 MODELO PÚBLICO** — gera resumo estruturado em `.md` a partir de qualquer arquivo de texto (código, docs, logs, configs, CSVs) |

---

## 🚀 Como Usar

### 1. Importar uma recipe

```bash
# 1. Validar a sintaxe antes de importar
goose recipe validate ./file-summarizer.yaml

# 2. Copiar para a pasta padrão do Goose
#    Linux / macOS / WSL:
cp ./file-summarizer.yaml ~/.config/goose/recipes/

#    Windows (PowerShell):
Copy-Item .\file-summarizer.yaml $env:USERPROFILE\.config\goose\recipes\
```

### 2. Executar via CLI

```bash
# Sintaxe básica
goose run --recipe <nome-da-recipe> --parametro1 "valor" --parametro2 "valor"

# Exemplo:
goose run --recipe file-summarizer --caminho_arquivo "./README.md" --caminho_saida "./resumo-readme.md"

# Com idioma e formato customizados:
goose run --recipe file-summarizer --caminho_arquivo "./src/api/auth.py" --caminho_saida "./docs/auth-summary.md" --idioma "en-US" --formato "detalhado" --publico_alvo "tecnico"
```

### 3. Listar recipes instaladas

```bash
goose recipe list
```

---

## ⚙️ Configuração de Ambiente

Algumas recipes precisam de **variáveis de ambiente** (API keys, tokens). Configure-as antes de usar:

```powershell
# Windows (PowerShell)
setx OPENAI_API_KEY "sk-xxxxxxxxxxxxx"
```

| Variável | Usada por | Obter em |
|----------|-----------|----------|
| `OPENAI_API_KEY` | `file-summarizer` | <https://platform.openai.com/api-keys> |

---

## 🛠️ Criando Sua Própria Recipe

Use qualquer recipe desta pasta como ponto de partida. Estrutura mínima:

```yaml
version: "1.0.0"
title: "Minha Recipe"
description: "Descrição de uma linha"

prompt: |
  Tarefa para o agente...
  Entrada: {{ meu_parametro }}

parameters:
  - key: meu_parametro
    input_type: string
    requirement: required
    description: "Descrição do input"

extensions:
  - type: builtin
    name: developer

settings:
  provider: openai
  model: gpt-4o
  temperature: 0.7

retry:                   # obrigatório: bloco retry com 'checks:'
  max_retries: 1
  timeout_seconds: 120
  on_failure: continue
  checks: []             # pode ser [] se não houver validação extra
```

Para detalhes completos (todos os campos, tipos de parâmetros, tipos de extensions, retry, response JSON schema), consulte o **[guia completo](../goose-recipes.md)**.

---

## 🤝 Contribuindo

1. Crie sua recipe seguindo o template mínimo acima
2. Documente todos os parâmetros no campo `description`
3. Teste localmente com `goose recipe validate`
4. Adicione uma entrada na tabela acima (ordem alfabética)
5. Abra um PR 🎉

---

## 📜 Licença

MIT — use, modifique e compartilhe livremente.