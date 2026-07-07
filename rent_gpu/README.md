# Rent GPU - Pesquisa de aluguel de GPU por hora

Este repositório reúne uma pesquisa do canal **Café com Dados & Gatos** sobre serviços de aluguel de GPU por hora para IA generativa, com foco em uso prático para ferramentas como **ComfyUI**, **Stable Diffusion**, **Flux**, geração de imagens, geração de vídeos e experimentos com modelos de IA.

A ideia deste material não é apontar uma única empresa como "a melhor", mas ajudar a comparar perfis de provedores, tipos de cobrança, disponibilidade de GPUs e cuidados antes de contratar uma instância em nuvem.

## Arquivos da pasta

- [`precos_por_empresa_gpu_cafe_com_dados_e_gatos.pdf`](./precos_por_empresa_gpu_cafe_com_dados_e_gatos.pdf)  
  Base de pesquisa organizada por empresa, com observações sobre tipo de cobrança, perfil do serviço, modelos de GPU encontrados e pontos de atenção.

- [`melhores_precos_por_gpu_cafe_com_dados_e_gatos.pdf`](./melhores_precos_por_gpu_cafe_com_dados_e_gatos.pdf)  
  Ranking consolidado por tipo de GPU, selecionando o menor preço encontrado dentro do recorte pesquisado e trazendo uma leitura prática para cada categoria.

## Data da consulta

A pesquisa foi realizada em **07-07-2026**.

Preços de GPU em nuvem mudam com frequência. Eles podem variar conforme:

- disponibilidade da GPU;
- região do datacenter;
- tipo de instância;
- modelo de cobrança;
- prioridade da máquina;
- marketplace ou provedor fixo;
- armazenamento incluído ou cobrado à parte;
- tráfego de rede;
- CPU, RAM e snapshots;
- compromisso mínimo ou reserva.

Por isso, este material deve ser usado como um **guia de comparação**, não como uma tabela definitiva de preços.

## Como ler a pesquisa

O arquivo de preços por empresa mostra a base da coleta. Ele é útil para entender o perfil de cada provedor: se é cloud tradicional, marketplace, bare metal, container, Kubernetes, cluster enterprise ou serviço mais amigável para experimentos.

O arquivo de melhores preços por GPU consolida a pesquisa por modelo de placa. Ele ajuda a responder perguntas como:

- Onde apareceu a RTX 4090 mais barata?
- Qual provedor teve melhor valor para RTX 5090?
- Quais opções fazem sentido para 48GB de VRAM?
- Quando vale olhar A100, H100 ou H200?
- Quais opções são mais enterprise e quais são mais acessíveis?

## Observação importante

Menor preço não significa necessariamente melhor escolha.

Para uso com ComfyUI, Flux, Stable Diffusion e workflows de vídeo, também é importante avaliar:

- quantidade de VRAM;
- estabilidade da máquina;
- facilidade de configuração;
- reputação do host, quando for marketplace;
- velocidade de disco;
- velocidade de download/upload;
- se a instância pode ser interrompida;
- se há cobrança mínima;
- se storage e tráfego são cobrados separadamente;
- se é fácil desligar ou remover tudo ao final.

Em cloud, um dos maiores riscos não é apenas escolher uma GPU cara. É esquecer recurso ligado e continuar pagando.

## Empresas citadas na pesquisa

A pesquisa inclui provedores como Salad, Vast.ai, Massed Compute, ThunderCompute, VERDA, Radiant / Ori, DigitalOcean, Paperspace, Scaleway, LeaderGPU, Lambda Labs e Vultr.

Cada empresa tem um perfil diferente. Algumas são mais simples para testes rápidos, outras são mais técnicas, e outras fazem mais sentido para times, clusters, inferência em produção ou workloads enterprise.

## Links oficiais das empresas

| Empresa | Link |
|---|---|
| VERDA | https://verda.com/pricing |
| Ori / Radiant | https://docs.ori.co/kubernetes/billing/ |
| Vultr | https://www.vultr.com/pricing/#cloud-gpu |
| Scaleway | https://www.scaleway.com/en/pricing/gpu/ |
| Massed Compute | https://vm.massedcompute.com/pricing |
| LeaderGPU | https://www.leadergpu.com/lead/new?operating_system%5B%5D=Ubuntu+22.04+Server&operating_system%5B%5D=Windows%C2%AE+Server+2019&operating_system%5B%5D=Windows%C2%AE+Server+2022&product_ids%5B%5D=961&product_ids%5B%5D=962&product_ids%5B%5D=963&product_ids%5B%5D=964&server_conf_id=106 |
| ThunderCompute | https://www.thundercompute.com/pricing |
| Lambda | https://lambda.ai/pricing |
| DigitalOcean GPU Droplets | https://www.digitalocean.com/pricing/gpu-droplets#reserved-plans |
| Paperspace | https://www.paperspace.com/pricing |
| Vast.ai | https://vast.ai/pricing |
| Salad | https://salad.com/pricing |

## Aviso

Confira sempre a página oficial do provedor antes de contratar qualquer serviço. Preço, disponibilidade, região, GPU, condições de uso e modelo de cobrança podem mudar a qualquer momento.

## Créditos

Pesquisa organizada por **Café com Dados & Gatos**.

Conteúdo voltado para quem estuda IA, dados, automação e ferramentas de forma prática, sem hype e sem enrolação.
