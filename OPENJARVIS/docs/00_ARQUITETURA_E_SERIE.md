# Como entender a arquitetura do OpenJarvis

## Objetivo

Entender a proposta do OpenJarvis antes da instalação e dos testes práticos.

Este documento serve como referência para a série de vídeos e para orientar a avaliação do projeto durante os testes.

## Fontes de pesquisa consultadas

Este documento usa apenas informações verificadas nos links abaixo:

- Paper no arXiv: https://arxiv.org/abs/2605.17172
- Site e documentação oficial: https://open-jarvis.github.io/OpenJarvis/#research
- Repositório oficial: https://github.com/open-jarvis/OpenJarvis
- Blog do Stanford Scaling Intelligence Lab: https://scalingintelligence.stanford.edu/blogs/openjarvis/

## O que é OpenJarvis

OpenJarvis é apresentado como um framework open source para agentes pessoais de IA que rodam no dispositivo do usuário.

A proposta do projeto é construir uma base para IA pessoal local, usando modelos, agentes, ferramentas, memória, engine de execução e aprendizado dentro de uma arquitetura modular.

O projeto defende uma abordagem local-first: a IA deve rodar localmente por padrão e chamar a nuvem apenas quando necessário.

## Projeto e origem

O OpenJarvis está associado ao Stanford Scaling Intelligence Lab.

Na documentação oficial, o projeto também aparece ligado à iniciativa Intelligence Per Watt, ao Hazy Research, ao Scaling Intelligence Lab e ao Stanford SAIL.

O paper principal é:

```text
OpenJarvis: Personal AI, On Personal Devices
arXiv:2605.17172
Submetido em 16 de maio de 2026
```

Autores informados no arXiv:

```text
Jon Saad-Falcon
Avanika Narayan
Robby Manihani
Tanvir Bhathal
Herumb Shandilya
Hakki Orhun Akengin
Gabriel Bo
Andrew Park
Matthew Hart
Caia Costello
Chuan Li
Christopher Ré
Azalia Mirhoseini
```

## Motivação do projeto

Segundo o blog do Scaling Intelligence Lab, a motivação do OpenJarvis vem da ideia de que a IA está chegando a um momento parecido com a transição dos mainframes para os computadores pessoais.

A tese apresentada é que agentes pessoais de IA estão crescendo, mas muitos ainda dependem de modelos e APIs na nuvem.

O problema apontado é que, nesses casos, a parte local costuma ser apenas uma camada de orquestração, enquanto a inteligência principal roda em servidores externos.

O OpenJarvis foi criado para explorar uma alternativa: agentes pessoais que rodam localmente por padrão, com atenção a privacidade, latência, custo, energia e limites reais de hardware.

## Ideia central

A ideia central do OpenJarvis é representar um sistema de IA pessoal como uma especificação modular composta por cinco primitivas.

Essas primitivas podem ser editadas, substituídas, medidas e otimizadas separadamente ou em conjunto.

O projeto apresenta três ideias principais:

- primitivas compartilhadas para construir agentes locais;
- avaliações que consideram energia, FLOPs, latência, custo e precisão;
- um ciclo de aprendizado que melhora modelos usando dados locais de rastros de uso.

## Os 5 pilares

### Intelligence

Camada dos modelos de linguagem usados para raciocínio, geração e entendimento.

A documentação apresenta essa camada como responsável por lidar com modelos locais e catálogo de modelos, ajudando a escolher o que o hardware consegue suportar.

### Engine

Camada de execução dos modelos.

A documentação cita engines como:

- Ollama
- vLLM
- SGLang
- llama.cpp
- APIs em nuvem

Essa camada abstrai onde e como a inferência roda.

### Agents

Camada responsável por agentes e raciocínio multi-etapa com uso de ferramentas.

A documentação oficial menciona agentes integrados que vão de chat simples a fluxos orquestrados.

### Tools & Memory

Camada responsável por ferramentas, conectores, memória e busca de contexto.

Essa camada é importante porque IA pessoal não depende apenas do modelo, mas também da capacidade de acessar informações, lembrar contexto e usar recursos externos.

### Learning

Camada responsável por aprendizado, avaliação, rastreamento e otimização.

O blog descreve o uso de rastros locais para melhorar o sistema e estudar estratégias de otimização no stack local de IA.

## O que a pesquisa afirma

O resumo do paper no arXiv afirma que trocar modelos de fronteira na nuvem por modelos locais dentro de stacks existentes não resolve o problema sozinho.

Segundo o paper, essa troca pode causar queda de precisão em tarefas de IA pessoal.

A proposta do OpenJarvis é decompor o stack em primitivas para que cada parte possa ser otimizada individualmente ou em conjunto.

O paper também apresenta a ideia de LLM-guided spec search, em que modelos de fronteira podem propor edições na especificação durante a busca, mas a especificação final roda no dispositivo durante a inferência.

## Como vamos testar nesta série

A avaliação será feita em etapas.

Primeiro será validada a base do projeto através da CLI.

Depois serão testadas as interfaces Browser App e Desktop App.

Ordem dos testes:

```text
CLI no Linux
Browser App
Desktop App
```

## Por que começar pela CLI

A documentação oficial apresenta diferentes formas de uso, incluindo Browser App, Desktop App, Python SDK e CLI.

A CLI será o primeiro teste porque permite observar o projeto mais perto da base técnica:

- backend de inferência;
- modelo usado;
- configuração local;
- comandos principais;
- comportamento inicial dos agentes;
- erros reais de instalação.

Depois da CLI, os testes avançam para Browser App e Desktop App.

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
- quais partes rodam bem localmente;
- quais partes ainda dependem de ajustes;
- vale a pena estudar mais profundamente;
- faz sentido integrar ao Projeto Frankenstein de IAs.

## Observação

Este documento é uma leitura inicial baseada nas fontes oficiais e no paper.

Os documentos seguintes serão preenchidos com base nos testes práticos:

```text
01_OPENJARVIS_CLI_LINUX.md
02_OPENJARVIS_BROWSER_APP.md
03_OPENJARVIS_DESKTOP_APP.md
```
