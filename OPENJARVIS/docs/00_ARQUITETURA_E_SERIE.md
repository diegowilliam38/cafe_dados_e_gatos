# Como entender a arquitetura do OpenJarvis

## Objetivo

Entender a proposta do OpenJarvis antes da instalação e dos testes práticos.

Este documento serve como referência para a série de vídeos e para orientar a avaliação do projeto durante os testes.

## O que é OpenJarvis

OpenJarvis é um projeto open source associado ao Stanford Scaling Intelligence Lab.

A proposta é construir uma arquitetura para IA pessoal capaz de integrar modelos, agentes, ferramentas, memória, execução e aprendizado dentro de uma estrutura única.

O projeto não se apresenta apenas como um chatbot ou interface para modelos locais.

A proposta é fornecer uma fundação para sistemas pessoais de IA.

## Projeto e origem

Organização:

- Stanford Scaling Intelligence Lab

Links principais:

- https://scalingintelligence.stanford.edu/blogs/openjarvis/
- https://open-jarvis.github.io/OpenJarvis/
- https://github.com/open-jarvis/OpenJarvis

## Os 5 pilares

### Intelligence

Camada responsável por modelos, descoberta, catálogo e seleção de modelos.

### Agent

Camada responsável pelo comportamento dos agentes, coordenação de tarefas e execução.

### Tools

Camada responsável pelo uso de ferramentas externas e integração com recursos adicionais.

### Engine

Camada responsável pela execução dos modelos.

Exemplos citados pelo projeto:

- Ollama
- llama.cpp
- vLLM
- SGLang

### Learning

Camada responsável por aprendizado, observabilidade, rastreamento e otimização baseada no uso.

## Como vamos testar

A avaliação será feita em etapas.

Primeiro será validada a base do projeto através da CLI.

Depois serão testadas as interfaces Browser App e Desktop App.

Ordem dos testes:

```text
CLI no Linux
Browser App
Desktop App
```

## O que será avaliado

- facilidade de instalação;
- clareza da documentação;
- funcionamento em hardware modesto;
- suporte a modelos locais;
- experiência de uso;
- arquitetura proposta;
- integração entre componentes;
- estabilidade durante os testes.

## Critérios de conclusão

Ao final da série, o objetivo é responder:

- o projeto entrega o que promete;
- a arquitetura faz sentido na prática;
- funciona em ambiente comum;
- vale a pena estudar mais profundamente;
- faz sentido integrar ao Projeto Frankenstein de IAs.
