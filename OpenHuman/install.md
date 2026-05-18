# OpenHuman no Linux - Instalação e Remoção

## Contexto

Este guia é para instalar o OpenHuman diretamente no Linux.

A instalação usa o instalador oficial do projeto, que baixa o AppImage mais recente e cria o comando "openhuman".

---

# 1. Atualizar o sistema

```bash
sudo apt update
```

---

# 2. Instalar dependências básicas

```bash
sudo apt install -y curl tar python3 ca-certificates
```

---

# 3. Instalar dependência para AppImage

No Ubuntu mais novo:

```bash
sudo apt install -y libfuse2t64
```

Se o pacote acima não existir:

```bash
sudo apt install -y libfuse2
```

---

# 4. Testar o instalador sem instalar

```bash
curl -fsSL https://raw.githubusercontent.com/tinyhumansai/openhuman/main/scripts/install.sh | bash -s -- --dry-run
```

---

# 5. Instalar o OpenHuman

```bash
curl -fsSL https://raw.githubusercontent.com/tinyhumansai/openhuman/main/scripts/install.sh | bash
```

---

# 6. Atualizar o terminal

```bash
source ~/.bashrc
```

---

# 7. Abrir o OpenHuman

```bash
openhuman
```

Se o comando acima não abrir:

```bash
~/.local/bin/openhuman
```

---

# 8. Remover o OpenHuman

Fechar processos abertos:

```bash
pkill -f openhuman || true
```

Remover o binário:

```bash
rm -f ~/.local/bin/openhuman
```

Remover o atalho do sistema:

```bash
rm -f ~/.local/share/applications/openhuman.desktop
```

Remover configurações e dados locais:

```bash
rm -rf ~/.config/openhuman
```

```bash
rm -rf ~/.local/share/openhuman
```

```bash
rm -rf ~/.cache/openhuman
```

---

# 9. Documentação oficial

```bash
https://github.com/tinyhumansai/openhuman
```
