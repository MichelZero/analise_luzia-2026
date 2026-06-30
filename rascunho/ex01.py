import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# 1. Lendo os dados de dentro da pasta 'dados'
df = pd.read_csv('dados/dados_01.csv', sep=',')

# 2. Configurando o estilo do gráfico para ficar parecido com artigo científico
sns.set_theme(style="whitegrid")
plt.figure(figsize=(10, 6))

# 3. Gerando o gráfico (O Seaborn já calcula a média caso haja replicatas)
grafico = sns.lineplot(
    data=df, 
    x='Tempo_h', 
    y='Contagem', 
    hue='Tratamento', # Uma cor/linha para cada tratamento
    marker='o',       # Bolinhas marcando os pontos
    linewidth=2,
    errorbar=None     # Sem barras de erro por enquanto para ver as linhas limpas
)

# 4. Ajustes estéticos (Títulos e eixos)
plt.title('Cinética de Crescimento (Time Kill)', fontsize=14, pad=15)
plt.xlabel('Tempos (horas)', fontsize=12)
plt.ylabel('Contagem de UFC', fontsize=12)
plt.xticks([0, 2, 4, 8, 24]) # Força o eixo X a mostrar exatamente os seus tempos

# Ajusta a legenda para fora do gráfico para não tampar as linhas
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()

# 5. Mostra o gráfico na tela
plt.show()