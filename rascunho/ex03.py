import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# 1. Lendo os dados
df = pd.read_csv('dados/dados_01.csv', sep=',')
df['Tempo_h'] = 'T' + df['Tempo_h'].astype(str)

# 2. Estilo
sns.set_theme(style="white")
plt.figure(figsize=(10, 6))

# 3. Gerando o gráfico
ax = sns.lineplot(
    data=df, 
    x='Tempo_h', 
    y='Contagem', 
    hue='Tratamento', 
    marker='o',       
    linewidth=3,       
    markersize=10,     
    errorbar=None
)

# ==========================================================
# O TRUQUE DE MESTRE PARA OS INCONTÁVEIS:
# Adiciona uma linha pontilhada vermelha no teto (Y = 240)
plt.axhline(y=240, color='red', linestyle='--', linewidth=1.5, alpha=0.5)

# Escreve "Placas Incontáveis" bem em cima dessa linha
plt.text(x=3.5, y=245, s='Limite de Contagem (Incontáveis)', 
         color='red', fontsize=10, fontstyle='italic', ha='center')
# ==========================================================

# 4. Estética
ax.grid(axis='y', color='lightgray', linestyle='-')
sns.despine()

plt.title('Efeito dos tratamentos sobre a cinética de crescimento', fontsize=14, pad=15)
plt.xlabel('Tempos (h)', fontsize=12)
plt.ylabel('Número de microrganismos viáveis\n(UFC/mL)', fontsize=12)

# Força o gráfico a ir um pouco mais alto (até 260) para caber o texto
plt.ylim(-10, 260) 

# 5. Legenda
plt.legend(
    title=None,                   
    loc='upper center',           
    bbox_to_anchor=(0.5, -0.15),  
    ncol=4,                       
    frameon=False                 
)

plt.tight_layout()
plt.show()