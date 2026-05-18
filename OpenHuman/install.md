# OpenHuman Linux Ubuntu - Instalação

## 1. Atualizar sistema

```bash
sudo apt update
sudo apt install -y curl tar python3 ca-certificates
```

---

## 2. Testar instalador sem instalar

```bash
curl -fsSL https://raw.githubusercontent.com/tinyhumansai/openhuman/main/scripts/install.sh | bash -s -- --dry-run
```

---

## 3. Instalar OpenHuman

```bash
curl -fsSL https://raw.githubusercontent.com/tinyhumansai/openhuman/main/scripts/install.sh | bash
```

---

## 4. Atualizar terminal

```bash
source ~/.bashrc
```

---

## 5. Abrir OpenHuman

```bash
openhuman
```

---

## 6. Se não abrir

```bash
~/.local/bin/openhuman
```

---

# Correção AppImage/FUSE Ubuntu

Se aparecer erro relacionado ao AppImage:

```bash
sudo apt install -y libfuse2t64
```

Se não existir:

```bash
sudo apt install -y libfuse2
```

---

# Remover OpenHuman

```bash
rm -f ~/.local/bin/openhuman
rm -f ~/.local/share/applications/openhuman.desktop
```

---

# Observações

- Projeto ainda está em beta.
- Instalação Linux atualmente focada em x86_64/amd64.
- O instalador baixa automaticamente o AppImage mais recente.

## Caminho do binário

```bash
~/.local/bin/openhuman
```

## Documentação oficial

```bash
https://github.com/tinyhumansai/openhuman
```
