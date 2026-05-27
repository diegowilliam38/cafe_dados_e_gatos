# Como instalar o AionUI no Linux

## 1. Acessar o download oficial

Baixar o AionUI para Linux em:

```text
https://aionui.com/download/
```

Ou pelo GitHub Releases:

```text
https://github.com/iOfficeAI/AionUi/releases
```

## 2. Baixar a versão Linux

Escolher o pacote compatível com a máquina:

```text
Linux x64
```

ou:

```text
Linux arm64
```

## 3. Dar permissão de execução se for AppImage

```bash
chmod +x "AionUI*.AppImage"
```

## 4. Abrir o AionUI

```bash
./AionUI*.AppImage
```

## 5. Testar Hermes no terminal

```bash
hermes --help
```

## 6. Testar OpenClaw no terminal

```bash
openclaw --help
```

## 7. Configurar no AionUI

Dentro do AionUI, adicionar os comandos locais:

```bash
hermes
```

```bash
openclaw
```

## 8. Primeiro teste

Pedir no AionUI:

```text
Crie um arquivo chamado teste-aionui.txt dizendo qual agente executou a tarefa.
```

## 9. Conferir o arquivo

```bash
ls -la
cat "teste-aionui.txt"
```
