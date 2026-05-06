# Hermes Agent + Browser Harness no Ubuntu VM

## Objetivo

Instalar Hermes Agent e Browser Harness em uma VM Ubuntu de forma simples para testes e gravação de vídeo.

Sem:
- ambientes isolados
- múltiplos perfis
- configurações avançadas
- pastas extras de projeto

Navegador utilizado:
- Brave Browser

---

# 1. Instalar dependências básicas

```bash
sudo apt update
sudo apt install -y curl git python3 python3-pip pipx
```

---

# 2. Instalar uv

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
source ~/.bashrc
```

Verificar:

```bash
uv --version
```

---

# 3. Instalar Hermes Agent

Instalação oficial:

```bash
curl -fsSL https://raw.githubusercontent.com/NousResearch/hermes-agent/main/scripts/install.sh | bash
```

Atualizar terminal:

```bash
source ~/.bashrc
```

Verificar instalação:

```bash
hermes --version
```

Abrir Hermes:

```bash
hermes
```

Diagnóstico:

```bash
hermes doctor
```

Selecionar modelo:

```bash
hermes model
```

---

# 4. Instalar Browser Harness

Clonar repositório oficial:

```bash
cd ~
git clone https://github.com/browser-use/browser-harness
```

Entrar na pasta:

```bash
cd ~/browser-harness
```

Instalar Browser Harness:

```bash
uv tool install -e .
```

Verificar instalação:

```bash
command -v browser-harness
```

Diagnóstico:

```bash
browser-harness --doctor
```

---

# 5. Testar Browser Harness

Abrir Brave Browser normalmente.

Depois testar:

```bash
browser-harness -c 'print(page_info())'
```

---

# 6. Caso o Browser Harness não conecte

Executar:

```bash
browser-harness --doctor
```

Se aparecer solicitação no navegador:
- clicar em "Allow"
- permitir acesso de debug remoto

---

# 7. Verificações finais

Hermes funcionando:

```bash
hermes
```

Browser Harness funcionando:

```bash
browser-harness -c 'print(page_info())'
```

Somente depois integrar Hermes + Browser Harness.
