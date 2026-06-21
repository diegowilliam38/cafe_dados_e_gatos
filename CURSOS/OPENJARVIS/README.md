# Como estudar e testar OpenJarvis

Curso prático do canal Café com Dados & Gatos para estudar, instalar e testar o OpenJarvis com foco em documentação oficial, teste real e aprendizado progressivo.

## Objetivo do curso

Entender o OpenJarvis como projeto de IA pessoal local, começando pela arquitetura e avançando para testes práticos nas interfaces principais.

O curso não parte da ideia de que a ferramenta está pronta para todos os usos. A proposta é testar com honestidade:

- o que o OpenJarvis promete;
- o que a documentação oficial mostra;
- o que funciona na prática;
- onde aparecem limites;
- quais requisitos fazem diferença;
- quando faz sentido estudar, usar ou acompanhar o projeto.

## Estrutura inicial

```text
Aula 1 - Como entender, preparar e testar o OpenJarvis pela CLI
Aula 2 - Como testar o OpenJarvis no Browser App
Aula 3 - Como testar o OpenJarvis no Desktop App
```

## Aula 1 - Como entender, preparar e testar o OpenJarvis pela CLI

Esta é a aula-base do curso.

Conteúdo:

- o que é OpenJarvis;
- proposta do projeto;
- arquitetura geral;
- cinco pilares: Intelligence, Engine, Agents, Tools & Memory e Learning;
- modelos locais;
- Ollama;
- requisitos de hardware;
- por que máquinas com GPU RTX são mais indicadas;
- preparação do ambiente;
- primeiro teste pela CLI no Linux.

## Aula 2 - Como testar o OpenJarvis no Browser App

Conteúdo:

- instalação ou execução do Browser App;
- acesso pela interface web;
- primeiro uso;
- comportamento real;
- pontos fortes;
- limitações encontradas;
- registro dos erros e ajustes.

## Aula 3 - Como testar o OpenJarvis no Desktop App

Conteúdo:

- instalação ou execução do Desktop App;
- experiência de uso;
- dependências gráficas;
- estabilidade;
- recursos disponíveis;
- comparação com CLI e Browser App dentro do próprio OpenJarvis;
- conclusão prática.

## Estrutura de arquivos

```text
CURSOS/OPENJARVIS/
├── README.md
├── docs/
│   ├── AULA_01_FUNDAMENTOS_OLLAMA_CLI.md
│   ├── AULA_02_BROWSER_APP.md
│   └── AULA_03_DESKTOP_APP.md
├── recursos/
│   ├── comandos/
│   │   └── diagnostico_ambiente_linux.md
│   └── referencias/
│       └── links_oficiais.md
└── videos/
    ├── aula-01/
    │   └── roteiro.md
    ├── aula-02/
    │   └── roteiro.md
    └── aula-03/
        └── roteiro.md
```

## Fontes oficiais

- Paper no arXiv: https://arxiv.org/abs/2605.17172
- Site oficial: https://open-jarvis.github.io/OpenJarvis/
- Pesquisa: https://open-jarvis.github.io/OpenJarvis/#research
- Repositório oficial: https://github.com/open-jarvis/OpenJarvis
- Blog do Stanford Scaling Intelligence Lab: https://scalingintelligence.stanford.edu/blogs/openjarvis/
- Cursos no YouTube: https://support.google.com/youtube/answer/15128409?hl=pt-BR

## Observação

Este curso será ampliado conforme os testes forem avançando. A estrutura inicial tem três aulas para manter o curso enxuto, prático e fácil de publicar.
