# Como instalar e testar o Traycer Desktop no Windows

## Objetivo

Este documento reúne os links oficiais, o escopo do teste e o prompt utilizado para avaliar o **Traycer Desktop no Windows**.

> O teste principal será realizado no Windows, por ser o sistema operacional utilizado pela maior parte do público consultado.

---

## Links oficiais

Site oficial

https://traycer.ai/

Download oficial

https://traycer.ai/download

Documentação oficial

https://docs.traycer.ai/

GitHub oficial

https://github.com/traycerai/traycer

Releases oficiais

https://github.com/traycerai/traycer/releases/latest

OpenCode Providers

https://opencode.ai/docs/providers

---

## Download para Windows

Na página oficial de download, selecione a versão para **Windows x64**.

Link direto para o instalador oficial:

https://github.com/traycerai/traycer/releases/latest/download/traycer-desktop-windows-x64.exe

---

## Proposta da ferramenta

O Traycer é uma aplicação gratuita e de código aberto voltada para orquestração de agentes de inteligência artificial.

A proposta é permitir que diferentes agentes trabalhem no mesmo projeto, compartilhem contexto e mantenham tarefas, arquivos e artefatos organizados em um único workspace.

---

## Ambiente testado no vídeo

- Sistema operacional: Windows
- Arquitetura: x64
- Traycer Desktop
- Claude Code local
- OpenCode local
- Mesmo modelo MiniMax nos dois harnesses
- Data do teste: Julho/2026

---

## O que será testado

- Instalação no Windows
- Configuração inicial
- Interface
- Integração com Claude Code
- Integração com OpenCode
- Uso do mesmo modelo MiniMax nos dois harnesses
- Regular Mode
- Epic Mode
- Compartilhamento de contexto
- Trabalho com múltiplos agentes
- Git, arquivos e artefatos
- Consumo de memória e desempenho
- Experiência geral

---

## Prompt usado no teste

```text
Você é um agente autônomo sênior de desenvolvimento de software.

Seu objetivo atual é criar um site moderno chamado Portal IA, com catálogo de modelos, ferramentas de IA, comparações, busca, filtros e design responsivo.

Critérios de sucesso (Quality Gates):
1. O site deve funcionar sem erros.
2. O layout deve ser responsivo.
3. O código deve ser organizado e documentado.
4. Não deve haver erros no console.
5. Todas as funcionalidades implementadas devem ser testadas.

Como operar em ciclo contínuo (Loop):
PASSO 1: Analise o projeto atual.
PASSO 2: Elabore um plano para a próxima etapa.
PASSO 3: Implemente apenas essa etapa.
PASSO 4: Teste e valide o resultado.
PASSO 5: Se encontrar problemas, corrija e repita o ciclo.
PASSO 6: Em caso de erro, tentar apenas 2 vezes, não solucionado o erro, parar imediatamente e comunicar o erro ao usuário.

Continue até que todos os critérios de sucesso sejam atendidos.
```

---

## Matriz de compatibilidade

| Ferramenta | Detectou | Funcionou | Observações |
|---|:---:|:---:|---|
| Claude Code | ⬜ | ⬜ | |
| OpenCode | ⬜ | ⬜ | |
| MiniMax via Claude Code | ⬜ | ⬜ | |
| MiniMax via OpenCode | ⬜ | ⬜ | |

---

## Erros encontrados e ajustes necessários

> Esta seção será atualizada conforme os testes reais forem realizados.

---

## O que ficou pendente

- Executar o primeiro projeto
- Testar os dois harnesses com o mesmo modelo
- Validar compartilhamento de contexto
- Testar agentes trabalhando em paralelo
- Verificar limitações no Windows
- Registrar o veredito final
