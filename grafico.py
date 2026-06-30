import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# 1. Lendo os dados
df = pd.read_csv('dados/dados_03.csv', sep=',')
df['Contagem'] = df['Contagem'].fillna(250)

# ==========================================
# 2. A CORREÇÃO DEFINITIVA DO EIXO X (TT0):
df['Tempo_h'] = df['Tempo_h'].astype(str).str.replace('T', '')
df['Tempo_h'] = 'T' + df['Tempo_h']
# ==========================================

# 3. Estilo
sns.set_theme(style="white")
plt.figure(figsize=(10, 6))

# 4. Gerando o gráfico
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

# 5. O truque dos Incontáveis
plt.axhline(y=240, color='red', linestyle='--', linewidth=1.5, alpha=0.5)
plt.text(x=3.5, y=245, s='Limite de Contagem (Incontáveis)', 
         color='red', fontsize=10, fontstyle='italic', ha='center')

# =========================================================================
# 5.1 ADIÇÃO DOS SÍMBOLOS ESTATÍSTICOS (# e *)
# Mapeamento do Eixo X: T0=0, T2=1, T4=2, T8=3, T24=4
# =========================================================================

# --- EXEMPLOS PARA O TEMPO T8 (Posição X = 3) ---
# Ajuste o valor de Y (segundo parâmetro) para flutuar logo acima do ponto da curva
ax.text(3, 80, '#', ha='center', va='bottom', fontsize=13, fontweight='bold', color='black')
ax.text(3, 122, '#', ha='center', va='bottom', fontsize=13, fontweight='bold', color='black')

# --- EXEMPLOS PARA O TEMPO T24 (Posição X = 4) ---
# Se um ponto estiver colado no teto (250) e for significativamente diferente:
ax.text(4, 256, '#', ha='center', va='bottom', fontsize=13, fontweight='bold', color='black')

# Se a maior dose barrou o crescimento e ficou no chão (Y = 0):
ax.text(4, 6, '*#', ha='center', va='bottom', fontsize=13, fontweight='bold', color='purple')

# =========================================================================

# 6. Estética 
ax.grid(axis='y', color='lightgray', linestyle='-')
sns.despine()

plt.title('Efeito dos tratamentos sobre a cinética de crescimento', fontsize=14, pad=15)
plt.xlabel('Tempos (h)', fontsize=12)
plt.ylabel('Número de microrganismos viáveis\n(UFC/mL)', fontsize=12)

# Ajustado para 270 para dar folga aos símbolos que ficarem no topo (Y=250)
plt.ylim(-15, 270) 

# 7. Legenda 
plt.legend(
    title=None,                   
    loc='upper center',           
    bbox_to_anchor=(0.5, -0.15),  
    ncol=4,                       
    frameon=False                 
)

plt.tight_layout()
plt.show()