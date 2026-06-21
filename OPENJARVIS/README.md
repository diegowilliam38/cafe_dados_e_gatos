# Como estudar e testar OpenJarvis

Documentação e testes práticos do projeto OpenJarvis, do Stanford Scaling Intelligence Lab, para o canal Café com Dados & Gatos.

## Objetivo da série

Estudar o OpenJarvis como projeto de arquitetura para IA pessoal, começando pela base técnica e avançando por camadas de uso.

A série será organizada em três frentes:

- CLI no Linux
- Browser App
- Desktop App

A ideia é entender primeiro a estrutura do projeto, depois testar a instalação e, por fim, avaliar a experiência de uso em interfaces mais completas.

## O que é OpenJarvis

OpenJarvis é um projeto open source associado ao Stanford Scaling Intelligence Lab.

A proposta é criar uma arquitetura para agentes pessoais de IA, combinando modelos, agentes, ferramentas, engine de execução, memória e aprendizado.

Neste repositório, o foco será testar o projeto na prática, com atenção especial a modelos locais, hardware modesto e uso real em ambiente de laboratório.

## Por que começar pela CLI

A CLI será o primeiro teste porque ela mostra a base do projeto com menos camadas de interface.

Pela CLI, é mais fácil observar:

- backend de inferência;
- modelo usado;
- configuração local;
- comportamento dos agentes;
- erros reais de instalação;
- limites de desempenho no hardware.

Depois que a base estiver funcionando, os testes avançam para Browser App e Desktop App.

## Ordem dos testes

```text
CLI no Linux
Browser App
Desktop App
```

## Ambiente usado

- Sistema operacional principal: Windows 11
- Ambiente de teste: Linux / WSL Ubuntu
- Hardware: i7 2018 + GTX 960 2GB
- Prioridade: instalação simples para testes
- Preferência: modelos locais quando possível
- Backend inicial: Ollama

## Documentos da série

```text
OPENJARVIS/
├── README.md
└── docs/
    ├── 00_ARQUITETURA_E_SERIE.md
    ├── 01_OPENJARVIS_CLI_LINUX.md
    ├── 02_OPENJARVIS_BROWSER_APP.md
    └── 03_OPENJARVIS_DESKTOP_APP.md
```

## Status dos testes

```text
00_ARQUITETURA_E_SERIE.md      iniciado
01_OPENJARVIS_CLI_LINUX.md     pendente
02_OPENJARVIS_BROWSER_APP.md   pendente
03_OPENJARVIS_DESKTOP_APP.md   pendente
```

## Links oficiais

- Site oficial: https://open-jarvis.github.io/OpenJarvis/
- Blog do Stanford Scaling Intelligence Lab: https://scalingintelligence.stanford.edu/blogs/openjarvis/
- Repositório oficial: https://github.com/open-jarvis/OpenJarvis
