# Google Image Bridge — geração de imagens com Gemini API em projeto local

## Visão geral

O Google Image Bridge é uma ponte local simples para gerar imagens via Gemini API usando um script Python.

A ideia é permitir que uma pessoa, agente local, orquestrador ou automação consiga:

- receber um prompt visual;
- chamar a Gemini API por script;
- salvar a imagem em uma pasta local;
- retornar no terminal o caminho do arquivo gerado;
- manter a chave de API fora do código;
- usar um ambiente Python isolado para evitar conflito de bibliotecas.

Este guia foi pensado para Linux/Ubuntu, mas a lógica pode ser adaptada para outros sistemas.

## Para que serve

Este bridge é útil quando o objetivo é integrar geração de imagens em fluxos locais, por exemplo:

- agentes de IA que criam prompts visuais;
- automações que precisam gerar imagens por API;
- projetos de conteúdo;
- mascotes, thumbnails, avatares e imagens de apoio;
- pipelines locais que precisam salvar arquivos em uma pasta previsível;
- testes com Gemini API sem depender de uma interface manual.

## O que este guia cria

Ao final, a estrutura será parecida com esta:

```text
~/frankenstein-ias/apps/imagem/
├── config/
│   ├── .env
│   └── .env.example
├── input/
├── output/
├── scripts/
│   └── google_image_bridge.py
├── requirements.txt
├── .gitignore
└── .venv/
```

## Requisitos

Antes de começar, é necessário ter:

```text
Linux/Ubuntu ou sistema compatível
Python 3
python3-venv
pip
chave de API da Google Gemini
acesso à internet
```

## Instalar dependências do sistema

No Ubuntu, rode:

```bash
sudo apt update
sudo apt install -y python3 python3-venv python3-pip
```

## Criar a estrutura de pastas

Neste exemplo, o app ficará em:

```text
~/frankenstein-ias/apps/imagem
```

Crie a estrutura:

```bash
mkdir -p ~/frankenstein-ias/apps/imagem/{config,input,output,scripts}
cd ~/frankenstein-ias/apps/imagem
```

## Criar ambiente virtual

Crie a venv:

```bash
python3 -m venv .venv
```

Ative:

```bash
source .venv/bin/activate
```

Atualize o pip:

```bash
python -m pip install --upgrade pip
```

## Criar requirements.txt

Crie o arquivo:

```bash
nano requirements.txt
```

Conteúdo:

```txt
google-genai
python-dotenv
pillow
```

Salve com:

```text
CTRL + O
ENTER
CTRL + X
```

Instale as dependências:

```bash
python -m pip install -r requirements.txt
```

## Por que usar venv

É recomendado usar uma venv isolada porque pacotes do namespace `google` podem entrar em conflito.

Um erro comum é:

```text
ImportError: cannot import name 'genai' from 'google'
```

Esse erro normalmente acontece quando:

- o pacote `google-genai` não está instalado no ambiente usado;
- o script foi executado com Python global;
- existe conflito com pacotes antigos da Google;
- o agente/orquestrador chamou `python` errado.

Por isso, o comando recomendado sempre usa:

```bash
.venv/bin/python
```

em vez de depender do Python global.

## Criar arquivo .env.example

Crie o arquivo:

```bash
nano config/.env.example
```

Conteúdo:

```env
GEMINI_API_KEY=COLE_SUA_CHAVE_AQUI
GOOGLE_IMAGE_MODEL=gemini-3.1-flash-image-preview
GOOGLE_IMAGE_OUTPUT_DIR=~/frankenstein-ias/apps/imagem/output
```

Salve.

## Criar arquivo .env

Copie o exemplo:

```bash
cp config/.env.example config/.env
```

Abra para editar:

```bash
nano config/.env
```

Troque:

```text
COLE_SUA_CHAVE_AQUI
```

pela sua chave real da Gemini API.

Atenção: não publique esse arquivo.

Proteja o arquivo:

```bash
chmod 600 config/.env
```

## Criar .gitignore

Crie o arquivo:

```bash
nano .gitignore
```

Conteúdo:

```gitignore
# ambiente virtual
.venv/

# segredos
config/.env

# imagens geradas
output/

# cache Python
__pycache__/
*.pyc

# arquivos temporários
*.log
.DS_Store
```

Salve.

## Criar o script google_image_bridge.py

Crie o arquivo:

```bash
nano scripts/google_image_bridge.py
```

Cole o conteúdo abaixo:

```python
#!/usr/bin/env python3
import argparse
import datetime as dt
import os
import re
import sys
from pathlib import Path

from dotenv import load_dotenv
from google import genai


DEFAULT_APP_DIR = Path.home() / "frankenstein-ias" / "apps" / "imagem"


def get_app_dir() -> Path:
    raw = os.getenv("GOOGLE_IMAGE_APP_DIR", "").strip()
    if raw:
        return Path(raw).expanduser().resolve()
    return DEFAULT_APP_DIR


APP_DIR = get_app_dir()
ENV_PATH = APP_DIR / "config" / ".env"


def load_config():
    if not ENV_PATH.exists():
        print(f"ERRO_ENV_NAO_ENCONTRADO: {ENV_PATH}", file=sys.stderr)
        sys.exit(2)

    load_dotenv(ENV_PATH)

    api_key = os.getenv("GEMINI_API_KEY", "").strip()
    model = os.getenv("GOOGLE_IMAGE_MODEL", "gemini-3.1-flash-image-preview").strip()
    output_dir = Path(
        os.getenv("GOOGLE_IMAGE_OUTPUT_DIR", str(APP_DIR / "output")).strip()
    ).expanduser()

    if not api_key or api_key == "COLE_SUA_CHAVE_AQUI":
        print("ERRO_GEMINI_API_KEY_AUSENTE", file=sys.stderr)
        sys.exit(2)

    output_dir.mkdir(parents=True, exist_ok=True)

    return {
        "api_key": api_key,
        "model": model,
        "output_dir": output_dir,
    }


def slugify(text, max_len=60):
    text = text.lower().strip()
    text = re.sub(r"[^a-z0-9áàâãéèêíïóôõöúçñ\s_-]", "", text, flags=re.IGNORECASE)
    text = re.sub(r"\s+", "-", text)
    text = re.sub(r"-+", "-", text)
    text = text.strip("-_")

    if not text:
        text = "imagem-gerada"

    return text[:max_len]


def cmd_status(args):
    config = load_config()

    print("GOOGLE_IMAGE_BRIDGE_OK")
    print(f"APP_DIR={APP_DIR}")
    print(f"ENV_PATH={ENV_PATH}")
    print(f"MODEL={config['model']}")
    print(f"OUTPUT_DIR={config['output_dir']}")
    print("GEMINI_API_KEY=CONFIGURADA")
    print("OBS=O comando status nao gera imagem.")


def extract_parts(response):
    if hasattr(response, "parts") and response.parts:
        return response.parts

    parts = []
    candidates = getattr(response, "candidates", None) or []

    for candidate in candidates:
        content = getattr(candidate, "content", None)
        if content and getattr(content, "parts", None):
            parts.extend(content.parts)

    return parts


def cmd_generate(args):
    config = load_config()

    prompt = args.prompt.strip()
    if not prompt:
        print("ERRO_PROMPT_VAZIO", file=sys.stderr)
        sys.exit(2)

    client = genai.Client(api_key=config["api_key"])

    response = client.models.generate_content(
        model=config["model"],
        contents=[prompt],
    )

    parts = extract_parts(response)

    saved_files = []
    text_notes = []

    timestamp = dt.datetime.now().strftime("%Y%m%d-%H%M%S")
    base_name = slugify(args.name or prompt)

    for idx, part in enumerate(parts, start=1):
        text = getattr(part, "text", None)
        inline_data = getattr(part, "inline_data", None)

        if text:
            text_notes.append(text)

        if inline_data is not None:
            try:
                image = part.as_image()
                filename = f"{timestamp}-{base_name}-{idx}.png"
                output_path = config["output_dir"] / filename
                image.save(output_path)
                saved_files.append(output_path)
            except Exception as exc:
                print(f"ERRO_AO_SALVAR_IMAGEM: {exc}", file=sys.stderr)

    if text_notes:
        print("TEXTO_MODELO_INICIO")
        for note in text_notes:
            print(note)
        print("TEXTO_MODELO_FIM")

    if not saved_files:
        print("ERRO_NENHUMA_IMAGEM_GERADA", file=sys.stderr)
        sys.exit(1)

    for path in saved_files:
        print(f"IMAGEM_GERADA={path}")

    print("GOOGLE_IMAGE_BRIDGE_DONE")


def main():
    parser = argparse.ArgumentParser(
        description="Google Image Bridge para geracao de imagens via Gemini API"
    )

    subparsers = parser.add_subparsers(dest="command", required=True)

    status_parser = subparsers.add_parser("status")
    status_parser.set_defaults(func=cmd_status)

    generate_parser = subparsers.add_parser("generate")
    generate_parser.add_argument(
        "--prompt",
        required=True,
        help="Prompt visual da imagem a ser gerada.",
    )
    generate_parser.add_argument(
        "--name",
        required=False,
        help="Nome base do arquivo de saida.",
    )
    generate_parser.set_defaults(func=cmd_generate)

    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
```

Salve.

Dê permissão de execução:

```bash
chmod +x scripts/google_image_bridge.py
```

## Testar se o pacote google-genai está correto

Dentro da pasta do app:

```bash
cd ~/frankenstein-ias/apps/imagem
```

Rode:

```bash
.venv/bin/python -c "from google import genai; print('google-genai OK')"
```

Saída esperada:

```text
google-genai OK
```

Se falhar, reinstale dentro da venv:

```bash
.venv/bin/python -m pip install --upgrade google-genai python-dotenv pillow
```

## Testar status

Rode:

```bash
cd ~/frankenstein-ias/apps/imagem
.venv/bin/python scripts/google_image_bridge.py status
```

Saída esperada:

```text
GOOGLE_IMAGE_BRIDGE_OK
APP_DIR=/home/usuario/frankenstein-ias/apps/imagem
ENV_PATH=/home/usuario/frankenstein-ias/apps/imagem/config/.env
MODEL=gemini-3.1-flash-image-preview
OUTPUT_DIR=/home/usuario/frankenstein-ias/apps/imagem/output
GEMINI_API_KEY=CONFIGURADA
OBS=O comando status nao gera imagem.
```

## Gerar uma imagem de teste

Rode:

```bash
cd ~/frankenstein-ias/apps/imagem

.venv/bin/python scripts/google_image_bridge.py generate \
  --name "teste-maine-coon" \
  --prompt "A studio portrait of a luxurious Maine Coon cat sitting elegantly on a velvet cushion. Soft, warm studio lighting highlighting the silver and tabby patterns of the fur. Clean, minimalist background. Ultra-detailed, focus on the soulful expression and the sheer size of the breed."
```

Saída esperada:

```text
IMAGEM_GERADA=/home/usuario/frankenstein-ias/apps/imagem/output/20260504-123456-teste-maine-coon-1.png
GOOGLE_IMAGE_BRIDGE_DONE
```

## Abrir a pasta de saída

Rode:

```bash
xdg-open ~/frankenstein-ias/apps/imagem/output
```

Ou liste os arquivos:

```bash
ls -lah ~/frankenstein-ias/apps/imagem/output
```

## Comando padrão para agentes/orquestradores

Quando um agente local, orquestrador ou sistema externo precisar gerar imagem, o comando recomendado é:

```bash
cd ~/frankenstein-ias/apps/imagem
.venv/bin/python scripts/google_image_bridge.py generate --name "NOME_CURTO" --prompt "PROMPT_VISUAL_COMPLETO"
```

## Regras operacionais para agentes

Se um agente for usar essa ferramenta, ele deve seguir estas regras:

- usar sempre `.venv/bin/python`;
- nunca usar Python global;
- nunca instalar bibliotecas globalmente;
- nunca pedir a chave da Gemini no chat;
- nunca exibir o conteúdo de `config/.env`;
- considerar sucesso apenas se aparecer `GOOGLE_IMAGE_BRIDGE_DONE`;
- informar arquivo gerado apenas se aparecer `IMAGEM_GERADA=...`;
- não inventar caminhos;
- não prometer execução em segundo plano;
- retornar a saída real do comando;
- pedir confirmação antes de gerar muitas imagens ou consumir API paga.

## Fluxo conceitual

```text
Pedido do usuário
-> agente ou app cria/refina o prompt visual
-> Google Image Bridge chama a Gemini API
-> imagem é salva em output/
-> terminal retorna IMAGEM_GERADA=...
-> sistema informa o caminho do arquivo gerado
```

## Exemplo de prompt para avatar

```bash
cd ~/frankenstein-ias/apps/imagem

.venv/bin/python scripts/google_image_bridge.py generate \
  --name "avatar-robo-amigavel" \
  --prompt "Create a premium character avatar of a friendly intelligent robot assistant, expressive face, kind eyes, slightly futuristic but warm design, polished 3D render, cinematic studio lighting, centered composition, clean neutral background, suitable for an AI project mascot, no text, no letters, no logo."
```

## Exemplo de prompt para thumbnail

```bash
cd ~/frankenstein-ias/apps/imagem

.venv/bin/python scripts/google_image_bridge.py generate \
  --name "thumbnail-ia-local" \
  --prompt "Create a dramatic YouTube thumbnail style image about local AI automation, a glowing computer screen, futuristic assistant interface, dark background with warm highlights, cinematic lighting, high contrast, clean composition, no readable text."
```

## Como usar outro caminho de instalação

Por padrão, o script usa:

```text
~/frankenstein-ias/apps/imagem
```

Se quiser usar outro caminho sem editar o código, defina a variável:

```bash
export GOOGLE_IMAGE_APP_DIR="/caminho/para/apps/imagem"
```

Depois rode:

```bash
.venv/bin/python scripts/google_image_bridge.py status
```

Também é possível usar na mesma linha:

```bash
GOOGLE_IMAGE_APP_DIR="/caminho/para/apps/imagem" .venv/bin/python scripts/google_image_bridge.py status
```

## Segurança

Boas práticas recomendadas:

- manter `config/.env` fora do repositório;
- usar `chmod 600 config/.env`;
- não mostrar chave de API em vídeo, print ou live;
- não registrar tokens em logs;
- não publicar imagens de teste se contiverem dados privados;
- revisar prompts antes de enviar para a API;
- lembrar que chamadas de API podem consumir créditos ou limites.

## Troubleshooting

### Erro: ERRO_ENV_NAO_ENCONTRADO

Causa provável:

```text
O arquivo config/.env não existe no caminho esperado.
```

Solução:

```bash
cd ~/frankenstein-ias/apps/imagem
cp config/.env.example config/.env
nano config/.env
chmod 600 config/.env
```

### Erro: ERRO_GEMINI_API_KEY_AUSENTE

Causas possíveis:

```text
GEMINI_API_KEY não foi preenchida
GEMINI_API_KEY ainda está como COLE_SUA_CHAVE_AQUI
nome da variável está incorreto
.env está no caminho errado
```

Solução:

```bash
nano ~/frankenstein-ias/apps/imagem/config/.env
```

Verifique se existe a linha:

```env
GEMINI_API_KEY=SUA_CHAVE_REAL
```

### Erro: ImportError: cannot import name 'genai' from 'google'

Causa provável:

```text
O script foi executado com Python global ou ambiente errado.
```

Solução:

```bash
cd ~/frankenstein-ias/apps/imagem
.venv/bin/python -m pip install --upgrade google-genai python-dotenv pillow
.venv/bin/python -c "from google import genai; print('google-genai OK')"
```

Depois rode novamente usando:

```bash
.venv/bin/python scripts/google_image_bridge.py status
```

### Erro: ERRO_NENHUMA_IMAGEM_GERADA

Causas possíveis:

```text
a API retornou apenas texto
modelo configurado não retornou imagem
prompt não gerou saída visual
limites, billing ou permissão da API impediram a geração
```

Ações recomendadas:

```text
verificar modelo no .env
testar prompt mais simples
verificar conta/projeto na Google
verificar limites ou billing
verificar se a API retornou mensagens entre TEXTO_MODELO_INICIO e TEXTO_MODELO_FIM
```

### Status funciona, mas geração falha

Verificar:

```text
chave de API válida
modelo configurado
conectividade com internet
billing/limites na Google
prompt
saída textual do modelo
```

## Checklist final

Antes de considerar a instalação pronta, confira:

```text
[ ] pasta apps/imagem criada
[ ] venv criada
[ ] requirements.txt criado
[ ] dependências instaladas na venv
[ ] config/.env.example criado
[ ] config/.env criado e preenchido
[ ] config/.env protegido com chmod 600
[ ] .gitignore criado
[ ] script google_image_bridge.py criado
[ ] import google-genai testado
[ ] status retornou GOOGLE_IMAGE_BRIDGE_OK
[ ] geração retornou GOOGLE_IMAGE_BRIDGE_DONE
[ ] imagem apareceu na pasta output/
```

## Resumo

O Google Image Bridge cria uma ponte simples entre um projeto local e a Gemini API para geração de imagens.

A abordagem recomendada é:

```text
script local
-> venv isolada
-> .env protegido
-> Gemini API
-> imagem salva em output/
-> saída verificável no terminal
```

O ponto mais importante é sempre executar com:

```bash
.venv/bin/python
```

Isso evita o erro de conflito entre bibliotecas do Google e garante que o script use as dependências corretas.
