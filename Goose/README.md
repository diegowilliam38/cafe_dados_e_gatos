# 🧾 Goose Recipes

Coleção de **recipes YAML** para o [Goose](https://github.com/block/goose). Cada `.yaml` é uma tarefa reutilizável que pode ser executada via CLI ou UI.

> 📚 Para o **guia completo do formato YAML** (campos, parâmetros, extensions, settings), veja [`../goose-recipes.md`](../goose-recipes.md).

---

## 📦 Recipes Disponíveis

| Recipe                 | Arquivo                                          | Descrição                                                                                      |
| ---------------------- | ------------------------------------------------ | ---------------------------------------------------------------------------------------------- |
| ⭐ **Doc Installer**    | [`doc-installer.yaml`](./doc-installer.yaml)     | Pesquisa na internet e gera `.md` copy-paste de instalação (pronto para GitHub)                |
| 🧾 **File Summarizer** | [`file-summarizer.yaml`](./file-summarizer.yaml) | **🌟 MODELO PÚBLICO** — gera resumo estruturado em `.md` a partir de qualquer arquivo de texto |

> 📄 **Documentos gerados:** [`docker-install.md`](./docker-install.md) — exemplo real (379 linhas) produzido pela recipe `doc-installer` rodando sobre o Docker.

---

## 🚀 Como Usar

### 1. Importar uma recipe

```bash
# 1. Validar a sintaxe antes de importar
goose recipe validate ./doc-installer.yaml

# 2. Copiar para a pasta padrão do Goose
#    Linux / macOS / WSL:
cp ./doc-installer.yaml ~/.config/goose/recipes/

#    Windows (PowerShell):
Copy-Item .\doc-installer.yaml $env:USERPROFILE\.config\goose\recipes\
```

### 2. Executar via CLI

```bash
# Sintaxe básica
goose run --recipe <nome-da-recipe> --parametro1 "valor" --parametro2 "valor"

# Exemplo:
goose run --recipe doc-installer --ferramenta "Docker"
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
setx TAVILY_API_KEY "tvly-xxxxxxxxxxxxx"
setx BRAVE_API_KEY "BSA-xxxxxxxxxxxxx"
```

| Variável         | Usada por                     | Obter em                        |
| ---------------- | ----------------------------- | ------------------------------- |
| `TAVILY_API_KEY` | `doc-installer`               | <https://tavily.com>            |
| `BRAVE_API_KEY`  | `doc-installer` (alternativa) | <https://brave.com/search/api/> |
| `OPENAI_API_KEY` | `file-summarizer`             | <https://platform.openai.com/api-keys> |

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