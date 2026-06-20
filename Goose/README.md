# 🧾 Goose Recipes

Coleção de **recipes YAML** para o [Goose](https://github.com/block/goose). Cada `.yaml` é uma tarefa reutilizável que pode ser executada via CLI ou UI.

> 📚 Para o **guia completo do formato YAML** (campos, parâmetros, extensions, settings, 10 regras de validação), veja [`../../goose-recipes.md`](../../goose-recipes.md).

---

## 📦 Recipes Disponíveis

| Recipe | Arquivo | Descrição |
| ------ | ------- | --------- |
| ⭐ **Summarizer** | [`summarizer.yaml`](./summarizer.yaml) | **🌟 MODELO PÚBLICO** — resume qualquer conteúdo textual (texto colado, arquivo local ou URL) em Markdown estruturado |
| **File Summarizer** | [`file-summarizer.yaml`](./file-summarizer.yaml) | Versão específica para arquivos locais (código, docs, logs, configs, CSVs) |

> 💡 A **`summarizer.yaml`** é o template **genérico e didático**. Use-a como ponto de partida para criar novas recipes de sumarização. A **`file-summarizer.yaml`** é a versão especializada apenas em arquivos.

---

## 🚀 Como Usar

### 1. Importar uma recipe

```bash
# 1. Validar a sintaxe antes de importar
goose recipe validate ./summarizer.yaml

# 2. Copiar para a pasta padrão do Goose
#    Linux / macOS / WSL:
cp ./summarizer.yaml ~/.config/goose/recipes/

#    Windows (PowerShell):
Copy-Item .\summarizer.yaml $env:USERPROFILE\.config\goose\recipes\
```

### 2. Executar via CLI

```bash
# Sintaxe básica
goose run --recipe <nome-da-recipe> --parametro1 "valor" --parametro2 "valor"

# ─── Summarizer (genérico) ─────────────────────────────────────────────

# Resumir texto colado
goose run --recipe summarizer --conteudo "Cole seu texto aqui..."

# Resumir arquivo local
goose run --recipe summarizer --arquivo "./README.md" --arquivo_saida "./resumo-readme.md"

# Resumir página web
goose run --recipe summarizer --url "https://exemplo.com/artigo" --idioma en-US

# ─── File Summarizer (específico para arquivo) ────────────────────────

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

```bash
# Linux / macOS / WSL
export OPENAI_API_KEY="sk-xxxxxxxxxxxxx"
```

| Variável | Usada por | Obter em |
|----------|-----------|----------|
| `OPENAI_API_KEY` | todas (default provider) | <https://platform.openai.com/api-keys> |
| `TAVILY_API_KEY` (opcional) | extension `tavily` para busca web | <https://tavily.com/> |

---

## 🛠️ Criando Sua Própria Recipe

Use a **`summarizer.yaml`** como ponto de partida — ela é o template didático.

### Estrutura mínima (4 blocos obrigatórios)

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

retry:                   # bloco retry com 'checks:' (pode ser [])
  max_retries: 1
  timeout_seconds: 120
  on_failure: continue
  checks: []
```

### 10 Regras de Ouro (validadas em produção)

1. ❌ `input_type: file` **NÃO** pode ter `default` (erro: `File parameters cannot have default values`)
2. ✅ Toda `{{ var }}` em prompt/instructions DEVE ter parameter; todo parameter DEVE ser usado
3. ❌ `input_type: date` com `default` é rejeitado (mesma restrição que `file`) — use `string` + default ISO
4. ✅ Settings: use **apenas** `provider`, `model`, `temperature` (outros campos bloqueiam o Start button)
5. ❌ Bloco `retry:` sem `checks:` causa erro — sempre inclua (mesmo `checks: []`)
6. ✅ `extensions[].type` válidos: `stdio | builtin | platform | streamable_http | frontend | inline_python` (NÃO `http`)
7. ❌ Comentários trailing após último bloco YAML quebram parsers
8. ❌ `{{ variavel }}` em comentários YAML SÃO detectados (não use em comentários!)
9. ✅ Provider field name = `provider` (NÃO `goose_provider` / `llm_provider`)
10. ❌ `requirement: user_prompt` + `input_type: file` BLOQUEIA o Start button

> 📖 Para detalhes completos e exemplos, consulte o **[guia completo](../../goose-recipes.md)**.

---

## 🤝 Contribuindo

1. Crie sua recipe seguindo o template mínimo acima
2. Use a `summarizer.yaml` como base se for uma recipe de sumarização
3. Documente todos os parâmetros no campo `description`
4. Teste localmente com `goose recipe validate`
5. Adicione uma entrada na tabela acima (ordem: starred primeiro, depois alfabética)
6. Abra um PR 🎉

---

## 📜 Licença

MIT — use, modifique e compartilhe livremente.
