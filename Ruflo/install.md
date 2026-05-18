# Teste Ruflo + Codex

## 1. Criar pasta de teste

```bash
mkdir -p ~/testes-ruflo
cd ~/testes-ruflo
```

## 2. Conferir Node e NPM

```bash
node --version
npm --version
```

## 3. Inicializar Ruflo na pasta de teste

```bash
npx ruflo@latest init wizard
```

## 4. Ver ajuda do Ruflo

```bash
npx ruflo@latest --help
```

## 5. Testar MCP do Ruflo

```bash
npx ruflo@latest mcp start
```

## 6. Abrir Codex apontando para a pasta do Ruflo

```bash
codex --cd ~/testes-ruflo
```

## 7. Prompt para colar no Codex

```text
Leia a pasta atual, identifique os arquivos criados pelo Ruflo e me explique como este projeto foi inicializado.
```

## 8. Segundo prompt para colar no Codex

```text
Crie um mini projeto Python nesta pasta com README.md, requirements.txt, app.py e um teste simples. Use a estrutura do Ruflo se ela estiver disponível.
```

## 9. Prompt para testar organização

```text
Organize este projeto usando planejamento, implementação, revisão e testes. Mostre o que foi criado e o que foi alterado.
```

## 10. Instalar Ruflo globalmente

```bash
npm install -g ruflo@latest
```

## 11. Conferir instalação global

```bash
ruflo --version
```

## 12. Iniciar Ruflo instalado globalmente

```bash
ruflo init wizard
```

## 13. Abrir Codex novamente na mesma pasta

```bash
codex --cd ~/testes-ruflo
```

## 14. Remover instalação global

```bash
npm uninstall -g ruflo
```

## 15. Verificar se removeu

```bash
ruflo --version
```

```bash
which ruflo
```

## 16. Limpar pastas de teste

```bash
cd ~
rm -rf ~/testes-ruflo
rm -rf ~/testes-ruflo-codex
```

## 17. Limpar cache do NPM

```bash
npm cache clean --force
```
