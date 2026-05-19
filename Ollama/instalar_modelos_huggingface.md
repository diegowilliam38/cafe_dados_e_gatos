# COMO RODAR MODELOS GGUF DO HUGGING FACE NO OLLAMA
# WINDOWS + LINUX
# MODO DIRETO COM "hf.co"

---

# O QUE ESTAMOS FAZENDO

Vamos rodar modelos GGUF do Hugging Face diretamente no Ollama, sem baixar manualmente o arquivo e sem criar "Modelfile".

O formato do comando é:

```text
ollama run hf.co/USUARIO/REPOSITORIO:QUANTIZACAO
```

Exemplo:

```text
ollama run hf.co/TheBloke/TinyLlama-1.1B-Chat-v1.0-GGUF:Q4_K_M
```

---

# COMO MONTAR O COMANDO

Pegue o link do modelo no Hugging Face.

Exemplo:

```text
https://huggingface.co/TheBloke/TinyLlama-1.1B-Chat-v1.0-GGUF
```

Remova esta parte:

```text
https://huggingface.co/
```

Sobra isto:

```text
TheBloke/TinyLlama-1.1B-Chat-v1.0-GGUF
```

Agora coloque "hf.co/" na frente:

```text
hf.co/TheBloke/TinyLlama-1.1B-Chat-v1.0-GGUF
```

Depois coloque ":" e a quantização desejada.

Exemplo:

```text
:Q4_K_M
```

Comando final:

```text
ollama run hf.co/TheBloke/TinyLlama-1.1B-Chat-v1.0-GGUF:Q4_K_M
```

---

# QUAL QUANTIZAÇÃO USAR

Para máquinas simples, use:

```text
Q4_K_M
```

Se estiver muito pesado, teste:

```text
Q3_K_M
```

Se quiser qualidade maior e tiver mais memória, teste:

```text
Q5_K_M
```

---

# PARTE 1 — WINDOWS

# 1. Instalar Ollama pelo aplicativo

Baixe e instale:

```text
https://ollama.com/download/windows
```

Depois de instalar, feche e abra o PowerShell.

---

# 2. Testar se o Ollama está funcionando

```powershell
ollama --version
```

---

# 3. Rodar modelo pequeno 1 — TinyLlama

```powershell
ollama run hf.co/TheBloke/TinyLlama-1.1B-Chat-v1.0-GGUF:Q4_K_M
```

---

# 4. Testar o modelo

Depois que abrir o chat no terminal, digite:

```text
Explique em português o que é um modelo de IA local.
```

Para sair:

```text
/bye
```

---

# 5. Rodar modelo pequeno 2 — Qwen

Escolha um repositório GGUF pequeno do Qwen no Hugging Face.

O formato será assim:

```powershell
ollama run hf.co/USUARIO/REPOSITORIO-QWEN-GGUF:Q4_K_M
```

Exemplo de estrutura:

```powershell
ollama run hf.co/NOME_DO_AUTOR/NOME_DO_MODELO_QWEN_GGUF:Q4_K_M
```

---

# 6. Ver modelos baixados no Ollama

```powershell
ollama list
```

---

# 7. Remover modelo do Ollama

```powershell
ollama rm hf.co/TheBloke/TinyLlama-1.1B-Chat-v1.0-GGUF:Q4_K_M
```

Se o nome aparecer diferente no "ollama list", copie exatamente o nome mostrado na lista.

---

# PARTE 2 — LINUX

# 1. Instalar Ollama

```bash
curl -fsSL https://ollama.com/install.sh | sh
```

---

# 2. Testar se o Ollama está funcionando

```bash
ollama --version
```

---

# 3. Rodar modelo pequeno 1 — TinyLlama

```bash
ollama run hf.co/TheBloke/TinyLlama-1.1B-Chat-v1.0-GGUF:Q4_K_M
```

---

# 4. Testar o modelo

Depois que abrir o chat no terminal, digite:

```text
Explique em português o que é um modelo de IA local.
```

Para sair:

```text
/bye
```

---

# 5. Rodar modelo pequeno 2 — Qwen

Escolha um repositório GGUF pequeno do Qwen no Hugging Face.

O formato será assim:

```bash
ollama run hf.co/USUARIO/REPOSITORIO-QWEN-GGUF:Q4_K_M
```

Exemplo de estrutura:

```bash
ollama run hf.co/NOME_DO_AUTOR/NOME_DO_MODELO_QWEN_GGUF:Q4_K_M
```

---

# 6. Ver modelos baixados no Ollama

```bash
ollama list
```

---

# 7. Remover modelo do Ollama

```bash
ollama rm hf.co/TheBloke/TinyLlama-1.1B-Chat-v1.0-GGUF:Q4_K_M
```

Se o nome aparecer diferente no "ollama list", copie exatamente o nome mostrado na lista.

---

# COMO SABER SE O MODELO SERVE PARA ESSE MÉTODO

No Hugging Face, o repositório precisa ter arquivos GGUF.

Procure por nomes como:

```text
GGUF
Q4_K_M
Q3_K_M
Q5_K_M
```

Exemplo de arquivo:

```text
tinyllama-1.1b-chat-v1.0.Q4_K_M.gguf
```

---

# O QUE EVITAR NESTE VÍDEO

Não use modelos em formatos como:

```text
safetensors
bin
pt
ckpt
```

Esses formatos não entram direto nesse fluxo simples com Ollama.

---

# RESUMO PARA O VÍDEO

O comando direto segue este padrão:

```text
ollama run hf.co/USUARIO/REPOSITORIO:QUANTIZACAO
```

Exemplo real:

```text
ollama run hf.co/TheBloke/TinyLlama-1.1B-Chat-v1.0-GGUF:Q4_K_M
```

Esse comando baixa o modelo GGUF do Hugging Face e já abre o chat no Ollama.
