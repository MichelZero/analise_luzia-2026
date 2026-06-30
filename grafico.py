import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# 1. Lendo os dados
df = pd.read_csv('dados/dados_01.csv', sep=',')

# TRUQUE MÁGICO: Transforma os números 0, 2, 24 em textos "T0", "T2", "T24"
# Isso força o Eixo X a ter distâncias iguais (como no artigo original)
df['Tempo_h'] = 'T' + df['Tempo_h'].astype(str)

# 2. Configurando o estilo geral (fundo branco, sem grade automática)
sns.set_theme(style="white")
plt.figure(figsize=(10, 6))

# 3. Gerando o gráfico
ax = sns.lineplot(
    data=df, 
    x='Tempo_h', 
    y='Contagem', 
    hue='Tratamento', 
    marker='o',       
    linewidth=3,       # Deixou a linha mais grossa
    markersize=10,     # Deixou a bolinha maior
    errorbar=None
)

# 4. Ajustes finos de estética idênticos ao PDF original
# Colocando linha de grade apenas na horizontal, de cor cinza clara
ax.grid(axis='y', color='lightgray', linestyle='-')

# Removendo a borda de cima e da direita (estilo Excel clássico)
sns.despine()

# Ajustando Títulos e Eixos
plt.title('Efeito dos tratamentos sobre a cinética de crescimento', fontsize=14, pad=15)
plt.xlabel('Tempos (h)', fontsize=12)
plt.ylabel('Número de microrganismos viáveis\n(UFC/mL)', fontsize=12)

# 5. Configurando a Legenda para ficar na parte de baixo, deitada
plt.legend(
    title=None,                   # Tira o título da legenda
    loc='upper center',           # Ponto de âncora
    bbox_to_anchor=(0.5, -0.15),  # Joga a legenda para baixo do gráfico
    ncol=4,                       # Divide os nomes em 4 colunas (fica deitada)
    frameon=False                 # Tira o quadrado ao redor da legenda
)

plt.tight_layout()

# 6. Mostra o gráfico na tela
plt.show()