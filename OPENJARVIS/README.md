# Como estudar e testar OpenJarvis

Este material reúne estudos, documentação técnica e testes práticos sobre o OpenJarvis, elaborados com base em pesquisa realizada no paper oficial, na documentação oficial, no repositório oficial e nos materiais públicos disponibilizados pelo Stanford Scaling Intelligence Lab.

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

- Sistema operacional de teste: Ubuntu 24.04.4 LTS x86_64
- Kernel: 6.17.0-35-generic
- Sessão gráfica: X11, ubuntu:GNOME
- CPU: Intel Core i7-6700K, 4 núcleos / 8 threads
- RAM: 46 GiB
- GPU: Intel HD Graphics 530 + NVIDIA GeForce GTX 960
- Prioridade: instalação simples para testes
- Preferência: modelos locais quando possível
- Backend inicial: Ollama

## Como registrar as informações da máquina

```bash
cat /etc/os-release
uname -a
lscpu
free -h
lsblk
glxinfo -B 2>/dev/null || true
nvidia-smi 2>/dev/null || true
```

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
