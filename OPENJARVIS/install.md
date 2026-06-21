# Como instalar e testar OpenJarvis Desktop no Linux

## Verificação oficial

```text
Data da verificação: 21/06/2026

Documentação oficial:
https://open-jarvis.github.io/OpenJarvis/

Repositório oficial:
https://github.com/open-jarvis/OpenJarvis

Status do projeto:
Ativo

Interface principal do teste:
OpenJarvis Desktop (AppImage)

Sistema operacional:
Linux
```

## Ambiente testado

```text
Sistema: Linux

Interface principal:
OpenJarvis Desktop

Backend:
OpenJarvis local

Inferência:
Ollama

Modelo inicial:
qwen3:0.6b
```

## Baixar OpenJarvis Desktop

Baixar o AppImage na página oficial de releases.

```text
https://github.com/open-jarvis/OpenJarvis/releases
```

## Preparar OpenJarvis Desktop

```bash
cd "$HOME/Downloads"
ls | grep -i "openjarvis"
```

```bash
cd "$HOME/Downloads"
APPIMAGE="$(find "$HOME/Downloads" -maxdepth 1 -type f -iname "*OpenJarvis*.AppImage" | head -n 1)"
echo "$APPIMAGE"
mv "$APPIMAGE" "$HOME/Downloads/OpenJarvis.AppImage"
chmod +x "$HOME/Downloads/OpenJarvis.AppImage"
```

## Abrir Desktop sem backend

```bash
cd "$HOME/Downloads"
./OpenJarvis.AppImage
```

## Instalar OpenJarvis Backend

```bash
cd "$HOME"
git clone "https://github.com/open-jarvis/OpenJarvis.git"
cd "OpenJarvis"
./scripts/quickstart.sh
```

## Conferir interface web

```text
http://localhost:5173
```

## Abrir Desktop com backend ligado

```bash
cd "$HOME/Downloads"
./OpenJarvis.AppImage
```

## Conferir backend

```text
http://localhost:8000
```

## Testar CLI

```bash
jarvis --version
```

```bash
jarvis doctor
```

```bash
jarvis model list
```

```bash
jarvis ask "Explique em uma frase o que é o OpenJarvis."
```

## Instalação manual

```bash
cd "$HOME/OpenJarvis"
uv sync --extra desktop
uv run maturin develop -m "rust/crates/openjarvis-python/Cargo.toml"
cd "frontend"
npm install
cd ..
```

## Iniciar Ollama

```bash
ollama serve
```

## Baixar modelo inicial

```bash
ollama pull "qwen3:0.6b"
```

## Subir backend manualmente

```bash
cd "$HOME/OpenJarvis"
uv run jarvis serve --port 8000
```

## Subir frontend manualmente

```bash
cd "$HOME/OpenJarvis/frontend"
npm run dev
```

## Testes no Desktop

```text
Explique em linguagem simples o que é o OpenJarvis e o que está rodando localmente neste teste.
```

```text
Você consegue acessar meus arquivos automaticamente? Responda apenas com o que está disponível neste ambiente agora.
```

```text
Monte um plano de organização semanal para uma pessoa que estuda IA e grava vídeos técnicos. Separe em manhã, tarde e noite.
```

## Comandos úteis

```bash
jarvis doctor
```

```bash
jarvis model list
```

```bash
jarvis chat
```

```bash
jarvis serve --port 8000
```

## Erros encontrados

```text
Ao tentar executar:

chmod +x "OpenJarvis.AppImage"

o terminal retornou:

chmod: cannot access 'OpenJarvis.AppImage': No such file or directory
```

## Ajustes necessários

```text
O arquivo AppImage baixado pela página de releases veio com nome versionado, e não como OpenJarvis.AppImage.

Por isso, antes de executar o chmod, foi necessário localizar o arquivo real dentro da pasta Downloads e renomear para OpenJarvis.AppImage.

Esse ajuste foi incluído diretamente na seção "Preparar OpenJarvis Desktop" para manter o fluxo copy-paste funcionando.
```

## Observações sobre a documentação oficial

```text
Se durante o teste algum comando intermediário for necessário, adicionar o comando diretamente na seção correspondente da instalação.

Não criar seção extra para o comando.

Registrar a observação somente em "Ajustes necessários".

Manter sempre o fluxo copy-paste funcionando.
```

## Resultado do teste

```text
Preencher após a gravação.
```
