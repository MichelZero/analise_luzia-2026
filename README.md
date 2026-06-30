# Luzia Coura - 2026

Este projeto contém uma análise de dados para geração de gráficos sobre a cinética de crescimento de microrganismos em diferentes tratamentos.

## Estrutura do projeto

- `grafico.py`: script principal que lê os dados de `dados/dados_03.csv` e gera um gráfico de linha usando `seaborn` e `matplotlib`.
- `dados/`: pasta com arquivos CSV de entrada utilizados na análise.
  - `dados_01.csv`
  - `dados_02.csv`
  - `dados_03.csv`
- `graficos/`: diretório para salvar ou organizar gráficos gerados manualmente.
- `rascunho/`: exemplos e rascunhos de scripts de análise (`ex01.py`, `ex02.py`, `ex03.py`).

## Como executar

1. Instale as dependências:

```bash
pip install -r requirements.txt
```

2. Execute o script principal:

```bash
python grafico.py
```

O script lê o arquivo `dados/dados_03.csv`, trata a coluna de tempo e plota a contagem de microrganismos por tratamento.

## Dependências

- `pandas`
- `matplotlib`
- `seaborn`
- `statsmodels`
- `scipy`
- `openpyxl`

## Observações

- O gráfico adiciona uma linha de limite em `Y = 240` com o rótulo "Limite de Contagem (Incontáveis)".
- Se desejar trabalhar com outros arquivos de dados, adapte o caminho no script ou crie novos scripts em `rascunho/`.

