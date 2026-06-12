# Como instalar e remover CrewAI

## 1. Verificar Python

```bash
python3 --version
```

Resultado esperado:

```text
Python 3.10.x até Python 3.13.x
```

## 2. Instalar dependências básicas

```bash
sudo apt update
```

```bash
sudo apt install -y curl python3 python3-pip python3-venv
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

## 5. Corrigir PATH se necessário

```bash
uv tool update-shell
```

```bash
source "$HOME/.bashrc"
```

## 6. Testar instalação

```bash
crewai --version
```

```bash
uv tool list
```

## 7. Atualizar CrewAI

```bash
uv tool install crewai --upgrade
```

## 8. Remover CrewAI

```bash
uv tool uninstall crewai
```

## 9. Conferir remoção

```bash
crewai --version
```

Resultado esperado:

```text
comando não encontrado
```

```bash
uv tool list
```

## 10. Remover uv

Usar somente se quiser remover também o gerenciador `uv`.

```bash
rm -rf "$HOME/.local/bin/uv"
```

```bash
rm -rf "$HOME/.local/bin/uvx"
```

```bash
rm -rf "$HOME/.cache/uv"
```

## 11. Conferir remoção do uv

```bash
uv --version
```

Resultado esperado:

```text
comando não encontrado
```
