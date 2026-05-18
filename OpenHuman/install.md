# OpenHuman Linux Ubuntu - Instalação e Correções

## Contexto

Instalação do OpenHuman em Linux/Ubuntu, incluindo correções comuns para AppImage, FUSE, sandbox, AppArmor, GTK/WebView e VirtualBox.

Projeto ainda está em beta. Em VM, principalmente VirtualBox, podem aparecer erros gráficos que não necessariamente indicam erro do OpenHuman.

---

# 1. Atualizar o sistema

```bash
sudo apt update
```

```bash
sudo apt install -y curl tar python3 ca-certificates
```

---

# 2. Instalar dependências comuns

```bash
sudo apt install -y libwebkit2gtk-4.1-0 libayatana-appindicator3-1 libgtk-3-0 libxdo3 libssl3
```

---

# 3. Instalar FUSE para AppImage

No Ubuntu mais novo:

```bash
sudo apt install -y libfuse2t64
```

Se não existir:

```bash
sudo apt install -y libfuse2
```

---

# 4. Testar instalador sem instalar

```bash
curl -fsSL https://raw.githubusercontent.com/tinyhumansai/openhuman/main/scripts/install.sh | bash -s -- --dry-run
```

---

# 5. Instalar OpenHuman

```bash
curl -fsSL https://raw.githubusercontent.com/tinyhumansai/openhuman/main/scripts/install.sh | bash
```

---

# 6. Atualizar o terminal

```bash
source ~/.bashrc
```

---

# 7. Abrir OpenHuman

```bash
openhuman
```

Se não abrir:

```bash
~/.local/bin/openhuman
```

---

# 8. Se aparecer aviso de unprivileged user namespaces

Durante a abertura, pode aparecer uma janela dizendo:

```text
unprivileged user-namespaces are disabled
```

Isso acontece porque algumas versões/distribuições Linux bloqueiam recursos usados por apps Electron/Tauri/AppImage para sandbox.

O botão "Sim" tenta liberar automaticamente.

Também é possível tentar manualmente:

```bash
sudo sysctl -w kernel.apparmor_restrict_unprivileged_userns=0
```

Se funcionar e quiser deixar permanente:

```bash
echo "kernel.apparmor_restrict_unprivileged_userns=0" | sudo tee /etc/sysctl.d/20-openhuman.conf
```

```bash
sudo sysctl --system
```

Para desfazer:

```bash
sudo rm -f /etc/sysctl.d/20-openhuman.conf
```

```bash
sudo sysctl -w kernel.apparmor_restrict_unprivileged_userns=1
```

Observação: em alguns Ubuntu/Kernel, principalmente VM, esse parâmetro pode não existir. Se aparecer erro dizendo que o arquivo ou diretório não existe, siga para as correções de execução com "--no-sandbox" e WebKit.

---

# 9. Abrir com no-sandbox

Se o OpenHuman não abrir ou fechar sozinho:

```bash
~/.local/bin/openhuman --no-sandbox
```

---

# 10. Correção para erro gráfico em VM/VirtualBox

Se aparecer erro parecido com:

```text
BadWindow (invalid Window parameter)
```

ou:

```text
shared_memory_switch
```

tente abrir com WebKit sem compositing:

```bash
WEBKIT_DISABLE_COMPOSITING_MODE=1 ~/.local/bin/openhuman --no-sandbox
```

Esse erro costuma estar relacionado a ambiente gráfico, GTK/WebView, AppImage/Tauri e VirtualBox.

---

# 11. Remover OpenHuman completamente

Fechar processos:

```bash
pkill -f openhuman || true
```

Remover binário e atalho:

```bash
rm -f ~/.local/bin/openhuman
```

```bash
rm -f ~/.local/share/applications/openhuman.desktop
```

Remover configurações, dados e cache:

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

# 12. Reinstalar do zero

Depois da limpeza:

```bash
sudo apt update
```

```bash
sudo apt install -y curl tar python3 ca-certificates libwebkit2gtk-4.1-0 libayatana-appindicator3-1 libgtk-3-0 libxdo3 libssl3
```

```bash
sudo apt install -y libfuse2t64
```

Se o pacote acima não existir:

```bash
sudo apt install -y libfuse2
```

Reinstalar:

```bash
curl -fsSL https://raw.githubusercontent.com/tinyhumansai/openhuman/main/scripts/install.sh | bash
```

Abrir:

```bash
~/.local/bin/openhuman
```

Se estiver em VM e não abrir:

```bash
WEBKIT_DISABLE_COMPOSITING_MODE=1 ~/.local/bin/openhuman --no-sandbox
```

---

# 13. Comandos úteis para diagnóstico

Ver caminho do OpenHuman:

```bash
which openhuman
```

Ver se o arquivo existe:

```bash
ls -lh ~/.local/bin/openhuman
```

Ver arquitetura da máquina:

```bash
uname -m
```

Ver versão do Ubuntu:

```bash
lsb_release -a
```

---

# 14. Observações para vídeo

- O OpenHuman ainda está em beta.
- A instalação Linux usa AppImage.
- O instalador baixa o AppImage mais recente automaticamente.
- Em Ubuntu 24.04 ou derivados, pode aparecer aviso de "unprivileged user namespaces".
- Em VirtualBox, pode aparecer erro gráfico mesmo com a instalação correta.
- O erro "BadWindow" normalmente aponta para problema gráfico/VM, não necessariamente problema do projeto.
- Para teste real, vale mostrar que nem tudo funciona de primeira.
- Para uso mais estável, testar também em Linux instalado direto na máquina pode ser melhor que VM.

---

# 15. Documentação oficial

```bash
https://github.com/tinyhumansai/openhuman
```
