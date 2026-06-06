# 🐱 Prompt: Pawtrack — Diário Digital de Pets com Dados

---

Você é uma engenheira sênior de apps mobile premium, especializada em produtos Apple-like e Android nativo. Quero que você crie um **APK Android completo, vendável e tecnicamente excelente**, chamado **"Pawtrack"** — um diário digital de pets com forte camada de dados.

## Contexto

Este app será demonstrado no canal **"Café com Dados e Gatos"** no YouTube (canal de analytics + gatos, público BR). Precisa ser:

- **Visualmente POLIDO** (Apple-like, dark-mode first, animações sutis)
- **Tecnicamente impressionante** (mostra várias features em sequência)
- **Realmente utilizável** (não é protótipo, é produto pronto pra Play Store)
- **100% offline** (dados ficam no celular, privacidade total)

**Paleta de cores:** tons de café com leite + azul céu + amarelo mostarda + creme (referência: café passado com chantilly num dia ensolarado).

**Modelo de venda:** Freemium ético.

- Grátis até 3 pets
- Premium **R$ 12,90 one-time** (pets ilimitados + insights + export)
- ZERO anúncio. ZERO assinatura recorrente. Zero pegadinha.

## Stack técnica (obrigatória)

- React 18 + TypeScript + Vite
- Tailwind CSS + Framer Motion
- Recharts (gráficos)
- Zustand (state)
- date-fns (datas em PT-BR)
- Capacitor + Android (gerar APK nativo)
- @capacitor/local-notifications (alarmes)
- @capacitor/camera (foto do cartão de vacina)
- @capacitor/preferences (storage leve)
- SQLite local via plugin ou capacitor-sqlite

## Funcionalidades core (todas precisam estar funcionando)

### 1) 🐱 Cadastro de pets (ilimitado no premium)

- Foto grande (galeria ou câmera)
- Nome, sexo, cor, raça (autocomplete)
- Data de nascimento (calcula idade humana automaticamente)
- Peso atual + histórico com gráfico
- Número do microchip
- Registro nacional/municipal do pet
- Castrado? (sim/não + data)
- Nome do veterinário + telefone
- Observações livres
- Cor tema do gato (6–8 cores pastéis pra escolher)

### 2) ⏰ Alarmes de alimentação

- 2 horários por dia configuráveis (padrão: 8h e 18h)
- Alarme **NATIVO** do Android (dispara mesmo com app fechado)
- Usuário **CANCELA** manualmente o alarme (UX simples)
- Toggle pra pausar todos os alarmes (viagem)
- Histórico simples: "ração dada em 12/06 às 8:02"

### 3) 💉 Controle de vacinas

- Tipos pré-cadastrados: V3, V4, V5, V8, V10, antirrábica, giárdia, FIV/FeLV, leucemia
- Data, veterinário, lote, foto do cartão
- Próxima dose: padrão +1 ano (customizável: 6m, 1, 2, 3 anos)
- Notificações em 3 estágios: 30 dias antes / 7 dias antes / no dia
- Carteira de vacinação digital por gato (timeline visual)

### 4) 💊 Vermifugação

- Marca do vermífugo (Drontal, Milbemax, etc — lista)
- Data, peso do gato no momento, próxima dose
- Frequência customizável: 3, 6 ou 12 meses
- Notificações em 3 estágios (30/7/0 dias)
- Histórico por gato

### 5) 💡 Dica de saúde do dia

- Banco com **60+ dicas** em português (nutrição, comportamento, sinais de alerta, enriquecimento ambiental, vermifugação, vacinação, hidratação, pelos, dentes, brincadeiras)
- 1 dica rotativa por dia na Home
- Botão "favoritar" + "não mostrar mais"
- Categorias filtráveis

### 6) 📊 Dashboard "Café com Dados"

- Cards de KPI: pets cadastrados, próximas vacinas, gasto do mês
- Gráfico de peso por gato (linha temporal, Recharts)
- Heatmap de cuidados cumpridos (estilo GitHub contribution)
- Lista "próximos eventos da semana"
- Insights automáticos:
  - "Luna está com a V10 atrasada há 12 dias"
  - "Você gastou R$ 240 com ração este mês"
  - "Simba atrasou 47min na ração 4x este mês"

### 7) 🏥 Consultas no vet

- Data, motivo, diagnóstico, tratamento, exames anexados
- Próxima consulta agendada + lembrete

### 8) 🎂 Datas especiais

- Aniversário do gato (com notificação + confete na home)
- Aniversário de "adoção" (data que chegou na família)

### 9) 📸 Galeria de fotos

- Upload múltiplo, organizado por mês
- Timeline visual cronológica

### 10) 📤 Exportação

- PDF da carteira de vacinação completa (por gato)
- CSV de todos os dados
- JSON pra backup

### 11) ⚙️ Configurações

- Modo escuro/claro/auto
- Notificações on/off por categoria
- Gerenciar assinatura premium (fake pra demo)
- Exportar tudo
- Sobre o app

## Critérios de qualidade (não negocie)

- ✓ Sem bugs
- ✓ Animações suaves em **toda** transição (Framer Motion)
- ✓ Design system consistente (componentes reutilizáveis)
- ✓ Performance boa no celular (60fps)
- ✓ APK final < 30MB
- ✓ Carrega em < 3 segundos
- ✓ Funciona 100% offline
- ✓ Acessível (textos grandes, contraste)
- ✓ TypeScript strict, sem `any` desnecessário
- ✓ Responsivo: celular portrait (principal) + tablet

## Entregáveis (nessa ordem)

1. Estrutura completa do projeto Capacitor
2. Schema do banco SQLite
3. Banco de 60+ dicas de saúde em JSON
4. Telas funcionais
5. APK Android pronto pra sideload (instalável)
6. PWA pra teste rápido no navegador
7. README com instruções de uso

## Como trabalhar

- Vá em **ondas pequenas**, com build/teste no fim de cada uma
- Comece pelo **esqueleto** (estrutura + navegação)
- Depois **banco de dados**
- Depois **features core** (cadastro, vacinas, alarme)
- Depois **dashboard e polish**
- Por último, **build do APK**
- A cada feature importante, me mostre com screenshot/GIF
- Se aparecer bug, corrija antes de seguir

---

