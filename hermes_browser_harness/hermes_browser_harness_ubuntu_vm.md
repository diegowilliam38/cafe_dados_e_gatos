# Hermes Agent + Browser Harness no Ubuntu VM

## Instalar dependências

```bash
sudo apt update
sudo apt install -y curl git python3 python3-pip pipx
```

---

## Instalar uv

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
source ~/.bashrc
```

---

## Verificar uv

```bash
uv --version
```

---

## Instalar Hermes Agent

```bash
curl -fsSL https://hermes-agent.nousresearch.com/install.sh | bash
```

---

## Atualizar terminal

```bash
source ~/.bashrc
```

---

## Verificar Hermes

```bash
hermes --version
```

---

## Abrir Hermes

```bash
hermes
```

---

## Configurar Hermes

```bash
hermes setup
```

---

## Diagnóstico Hermes

```bash
hermes doctor
```

---

## Escolher modelo

```bash
hermes model
```

---

## Clonar Browser Harness

```bash
cd ~
git clone https://github.com/browser-use/browser-harness
```

---

## Entrar na pasta

```bash
cd ~/browser-harness
```

---

## Instalar Browser Harness

```bash
uv tool install -e .
```

---

## Verificar Browser Harness

```bash
command -v browser-harness
```

---

## Diagnóstico Browser Harness

```bash
browser-harness --doctor
```

---

## Abrir Brave Browser

```bash
brave-browser
```

---

## Testar Browser Harness

```bash
browser-harness -c 'print(page_info())'
```

---

## Testar Hermes

```bash
hermes
```

---

## Testar Browser Harness novamente

```bash
browser-harness -c 'print(page_info())'
```
