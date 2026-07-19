import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Carregar os dados processados (gerado pelo código de extração anterior)
df = pd.read_csv('dados_plotagem.csv')

# Dicionário de cores baseado NOVA imagem (C. Albicans A2)
# Azul -> EAO/Limoneno | Laranja -> Nistatina | Cinza -> Veículo | Amarelo -> Crescimento
cores = {
    'Controle de Crescimento': '#FFC000',  # Amarelo
    'Controle do Veículo': '#A9A9A9',      # Cinza
    'EAO': '#4472C4',                      # Azul (usaremos os dados do EAO como "Limoneno")
    'Nistatina': '#ED7D31'                 # Laranja
}

# Dicionário para renomear as legendas no gráfico (EAO vira Limoneno)
legendas_map = {
    'Controle de Crescimento': 'Controle de Crescimento',
    'Controle do Veículo': 'Controle do Veículo',
    'EAO': 'Limoneno',
    'Nistatina': 'Nistatina'
}

# Criar a figura com 3 subplots
fig, axes = plt.subplots(1, 3, figsize=(18, 5))

# Ordem dos gráficos
graficos = ['CIM', '2XCIM', '4XCIM']

for i, tipo_grafico in enumerate(graficos):
    ax = axes[i]
    # Título da imagem de referência
    ax.set_title(f"C. Albicans A2 {tipo_grafico}", fontsize=12, fontweight='bold')
    
    # Definir limites e rótulos
    ax.set_ylim(0, 45000)
    ax.set_xlim(0, 24)
    ax.set_xlabel("Tempo (h)")
    ax.set_ylabel("UFC/mL")
    
    # --- PONTO CRÍTICO: Definir os ticks do X apenas nos dados reais (0, 2, 4, 8, 24) ---
    ax.set_xticks([0, 2, 4, 8, 24])

    # Filtrar os dados para este gráfico específico
    df_sub = df[df['Grafico'] == tipo_grafico]

    # Plotar cada condição com as novas cores e legendas
    for condicao in cores.keys():
        dados_cond = df_sub[df_sub['Condicao'] == condicao]
        if not dados_cond.empty:
            ax.plot(dados_cond['Tempo_h'], dados_cond['UFC_bruto'], 
                    marker='o', linestyle='-', color=cores[condicao], 
                    label=legendas_map[condicao], linewidth=2)

    # Inserir a legenda, grade e ajustar
    ax.legend(loc='upper left', fontsize=9)
    ax.grid(True, linestyle='--', alpha=0.5)

plt.tight_layout()
plt.show()