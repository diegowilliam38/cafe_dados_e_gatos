# Instalação OpenClaw via Docker — Versão 2026.02.27

PT-BR
Este repositório contém a documentação **passo a passo** para instalar o **OpenClaw via Docker**, em um ambiente **local** com:

- Windows 10/11  
- WSL2 (Ubuntu)  
- Docker Desktop  
- Ollama (rodando no Windows/host)

**Testado em:** 28/02/2026

---

## 📁 Estrutura do repositório

- **PT_BR/** → documentação em português (PDF)
- **EN_US/** → documentation in English (PDF)


---

## 📘 Documentação (PT-BR)

A documentação completa em português está na pasta:

- `PT_BR/`

Inclui:
- Pré-check do ambiente
- Setup Docker/Compose
- Integração com Ollama (OpenAI-compatible)
- Acesso ao Control UI e uso do token
- Solução do erro **pairing required (1008)**
- Comandos de verificação e diagnóstico (sanidade)

---

## 🧠 Visão geral da arquitetura

- OpenClaw roda dentro do Docker (WSL Ubuntu)
- Ollama roda no Windows (host)


---

## ⚠️ Observações importantes

- Em versões mais recentes, o **onboarding** pode iniciar automaticamente (e essa etapa pode não ser necessária).
- Se aparecer o erro **pairing required (1008)**, consulte a seção de troubleshooting no PDF.
- Sempre confirme que o Docker Desktop está rodando antes de iniciar.

---

## 📌 Referência de versão

Guia aplicável à instalação via Docker validada na versão:

**OpenClaw — 2026.02.27**

---

## 👤 Autoria

Mantido por **Denise Marti**  
Canal no YouTube: **Café com Dados & Gatos -  @CafecomDadoseGatos** 
## ⭐ Apoie o Projeto

Se isso fez sentido para você, **inscreva-se no canal**, deixe seu apoio e **compartilhe com quem está aprendendo também** — juntos fazemos o Café com Dados & Gatos crescer 💛🐱☕


---
EN-US

# OpenClaw Installation via Docker — Version 2026.02.27

This repository contains **step-by-step documentation** to install **OpenClaw via Docker** in a fully **local** environment using:

- Windows 10/11  
- WSL2 (Ubuntu)  
- Docker Desktop  
- Ollama (running on Windows/host)

**Tested on:** 02/28/2026

---

## 📁 Repository Structure

- **PT_BR/** → documentação em português (PDF)
- **EN_US/** → documentation in English (PDF)

---

## 📘 Documentation (EN-US)

The full English documentation is available in:

- `EN_US/`

It includes:
- Environment pre-check
- Docker/Compose setup
- Ollama integration (OpenAI-compatible)
- Control UI access and token usage
- Fix for the **pairing required (1008)** error
- Sanity check and troubleshooting commands

---

## 🧠 Architecture Overview

- OpenClaw runs inside Docker (WSL Ubuntu)
- Ollama runs on Windows (host)

---

## ⚠️ Important Notes

- In newer versions, the **onboarding** process may start automatically (and this step may not be required).
- If you encounter **pairing required (1008)**, check the troubleshooting section in the PDF.
- Always make sure Docker Desktop is running before you start.

---

## 📌 Version Reference

This guide applies to the Docker installation validated for:

**OpenClaw — 2026.02.27**

---

## 👤 Maintainer

Maintained by **Denise Marti**  
YouTube Channel: **Café com Dados & Gatos - @CafecomDadoseGatos**

---

## ⭐ Support the Project

If this helped you, please **subscribe to the channel** and **share it with someone who needs it** — it really helps the project grow 💛🐱☕