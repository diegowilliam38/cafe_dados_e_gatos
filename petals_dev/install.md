# Instalação do Petals no Linux com Llama

## Versão do Python

O Petals atualmente funciona melhor com:

- Python 3.10
- Python 3.11

Evite usar Python 3.12 neste projeto, porque algumas dependências ainda podem falhar durante a instalação.

Verificar versão atual:

```bash
python3 --version
```

---

# Instalar Python 3.11

```bash
sudo apt update
sudo apt install -y python3.11 python3.11-venv python3.11-dev
```

Verificar instalação:

```bash
python3.11 --version
```

---

# Instalar dependências gerais

```bash
sudo apt install -y git python3-pip python3-venv
```

---

# Criar pasta do projeto

```bash
mkdir -p ~/petals-teste
cd ~/petals-teste
```

---

# Criar ambiente virtual com Python 3.11

```bash
python3.11 -m venv .venv
```

---

# Ativar ambiente virtual

```bash
source .venv/bin/activate
```

---

# Confirmar versão ativa

```bash
python --version
```

Deve aparecer algo parecido com:

```text
Python 3.11.x
```

---

# Atualizar ferramentas do pip

```bash
pip install --upgrade pip setuptools wheel
```

---

# Instalar Petals

```bash
pip install git+https://github.com/bigscience-workshop/petals
```

---

# Instalar Hugging Face CLI

```bash
pip install huggingface_hub
```

---

# Login na Hugging Face

```bash
huggingface-cli login
```

Cole o token da Hugging Face quando pedir.

Antes disso:

1. Crie uma conta na Hugging Face
2. Acesse a página do modelo Llama
3. Aceite a licença da Meta

Sem isso, o modelo pode retornar erro de permissão.

---

# Modelo usado neste exemplo

```text
meta-llama/Meta-Llama-3.1-405B-Instruct
```

---

# Como fazer perguntas ao modelo

O Petals não funciona exatamente como o Ollama.

No Ollama usamos:

```bash
ollama run modelo
```

No Petals, normalmente usamos Python com:

- transformers
- petals
- AutoTokenizer
- AutoDistributedModelForCausalLM

Abaixo estão dois modos simples de teste.

---

# Modo 1 — Pergunta fixa

## Criar arquivo de teste

```bash
nano teste_llama_petals.py
```

Cole:

```python
from transformers import AutoTokenizer
from petals import AutoDistributedModelForCausalLM

model_name = "meta-llama/Meta-Llama-3.1-405B-Instruct"

tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoDistributedModelForCausalLM.from_pretrained(model_name)

prompt = "Explique em português, de forma simples, o que é uma rede peer-to-peer em inteligência artificial."

inputs = tokenizer(prompt, return_tensors="pt")["input_ids"]

outputs = model.generate(
    inputs,
    max_new_tokens=120,
    do_sample=True,
    temperature=0.7
)

print(tokenizer.decode(outputs[0], skip_special_tokens=True))
```

Salvar:

```text
CTRL + O
ENTER
CTRL + X
```

Rodar:

```bash
python3 teste_llama_petals.py
```

---

# Modo 2 — Chat simples pelo terminal

## Criar arquivo de chat

```bash
nano chat.py
```

Cole:

```python
from transformers import AutoTokenizer
from petals import AutoDistributedModelForCausalLM

model_name = "meta-llama/Meta-Llama-3.1-405B-Instruct"

tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoDistributedModelForCausalLM.from_pretrained(model_name)

print("Chat Petals + Llama iniciado.")
print("Digite 'sair' para encerrar.\n")

while True:
    prompt = input("Você: ")

    if prompt.lower().strip() in ["sair", "exit", "quit"]:
        break

    inputs = tokenizer(prompt, return_tensors="pt")["input_ids"]

    outputs = model.generate(
        inputs,
        max_new_tokens=200,
        do_sample=True,
        temperature=0.7
    )

    resposta = tokenizer.decode(outputs[0], skip_special_tokens=True)

    print("\nLlama:")
    print(resposta)
    print()
```

Salvar:

```text
CTRL + O
ENTER
CTRL + X
```

Rodar:

```bash
python3 chat.py
```

Para sair:

```text
sair
```

---

# CLI do Petals

A CLI do Petals existe, mas ela é usada principalmente para rodar um servidor/peer e colaborar com a rede.

Exemplo:

```bash
python3 -m petals.cli.run_server meta-llama/Meta-Llama-3.1-405B-Instruct
```

Esse comando é para participar da rede como peer.

Para fazer perguntas como cliente, usamos os scripts Python acima.

---

# Aviso importante

O Petals usa uma rede pública peer-to-peer.

Isso significa que partes do processamento podem passar por máquinas de outras pessoas.

Teste com responsabilidade.

Nunca envie:

- senhas
- dados bancários
- documentos pessoais
- chaves de API
- informações privadas
- informações empresariais sensíveis

Para dados sensíveis, prefira:

- modelos locais
- infraestrutura privada
- ambientes controlados

---

# Monitor público do Petals

Consultar modelos e saúde da rede:

https://health.petals.dev
