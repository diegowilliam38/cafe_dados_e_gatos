# OpenHuman Ubuntu 24.04

## 1. Baixar o arquivo .deb

Baixar no GitHub Releases:

```text
OpenHuman_0.53.43_amd64.deb
```

---

## 2. Instalar dependências

```bash
sudo apt update
sudo apt install -y curl tar python3 ca-certificates libxdo3 libgtk-3-0 libwebkit2gtk-4.1-0 libayatana-appindicator3-1 libssl3
```

---

## 3. Instalar o OpenHuman

```bash
cd ~/Downloads
sudo apt install ./OpenHuman_0.53.43_amd64.deb
```

---

## 4. Abrir o OpenHuman

```bash
OpenHuman
```

ou:

```bash
/usr/bin/OpenHuman
```

---

## 5. Observações importantes

Durante os testes no Ubuntu 24.04, o método AppImage/script apresentou erros relacionados a:

- EGL_BAD_ATTRIBUTE
- GPU shared context
- NSS
- GLIBC
- sandbox/AppImage
- virtualização

O método ".deb" foi o que funcionou corretamente no ambiente real.

---

## 6. Problema encontrado

Erro:

```bash
libxdo.so.3: cannot open shared object file
```

Correção:

```bash
sudo apt install -y libxdo3
```

---

## 7. Fluxo utilizado no teste real

- Ubuntu 24.04.4 LTS
- GLIBC 2.39
- Instalação real em máquina física
- AppImage falhou
- ".deb" funcionou corretamente

---

## 8. Remover o OpenHuman

```bash
sudo apt remove -y open-human
sudo apt autoremove -y
```

---

## 9. Abrir depois pelo menu

Depois da instalação, também é possível procurar no menu do Ubuntu por:

```text
OpenHuman
```

---

## 10. Link oficial

```text
https://github.com/tinyhumansai/openhuman/releases
```
