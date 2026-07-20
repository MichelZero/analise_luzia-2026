import pandas as pd
import matplotlib.pyplot as plt

# ==========================================================
# 1. INSERIR OS DADOS DAS MÉDIAS MANUALMENTE (extraídos do seu PDF)
# ==========================================================
# OBS: Substituí os valores "Incontáveis" por 45000 para que a linha vá até o topo do gráfico.
dados_medias = [
    # --- GRÁFICO 1 - CIM ---
    # Controle de Crescimento
    {'Grafico': 'CIM', 'Condicao': 'Controle de Crescimento', 'Tempo_h': 0, 'UFC': 1917},
    {'Grafico': 'CIM', 'Condicao': 'Controle de Crescimento', 'Tempo_h': 2, 'UFC': 2000},
    {'Grafico': 'CIM', 'Condicao': 'Controle de Crescimento', 'Tempo_h': 4, 'UFC': 4000},
    {'Grafico': 'CIM', 'Condicao': 'Controle de Crescimento', 'Tempo_h': 8, 'UFC': 6667},
    {'Grafico': 'CIM', 'Condicao': 'Controle de Crescimento', 'Tempo_h': 24, 'UFC': 45000}, # Incontáveis
    # Controle do Veículo
    {'Grafico': 'CIM', 'Condicao': 'Controle do Veículo', 'Tempo_h': 0, 'UFC': 1712},
    {'Grafico': 'CIM', 'Condicao': 'Controle do Veículo', 'Tempo_h': 2, 'UFC': 1734},
    {'Grafico': 'CIM', 'Condicao': 'Controle do Veículo', 'Tempo_h': 4, 'UFC': 3000},
    {'Grafico': 'CIM', 'Condicao': 'Controle do Veículo', 'Tempo_h': 8, 'UFC': 5200},
    {'Grafico': 'CIM', 'Condicao': 'Controle do Veículo', 'Tempo_h': 24, 'UFC': 45000}, # Incontáveis
    # EAO (Limoneno)
    {'Grafico': 'CIM', 'Condicao': 'EAO', 'Tempo_h': 0, 'UFC': 1617},
    {'Grafico': 'CIM', 'Condicao': 'EAO', 'Tempo_h': 2, 'UFC': 1062},
    {'Grafico': 'CIM', 'Condicao': 'EAO', 'Tempo_h': 4, 'UFC': 2056},
    {'Grafico': 'CIM', 'Condicao': 'EAO', 'Tempo_h': 8, 'UFC': 4800},
    {'Grafico': 'CIM', 'Condicao': 'EAO', 'Tempo_h': 24, 'UFC': 45000}, # Incontáveis
    # Nistatina
    {'Grafico': 'CIM', 'Condicao': 'Nistatina', 'Tempo_h': 0, 'UFC': 578},
    {'Grafico': 'CIM', 'Condicao': 'Nistatina', 'Tempo_h': 2, 'UFC': 245},
    {'Grafico': 'CIM', 'Condicao': 'Nistatina', 'Tempo_h': 4, 'UFC': 0},
    {'Grafico': 'CIM', 'Condicao': 'Nistatina', 'Tempo_h': 8, 'UFC': 217},
    {'Grafico': 'CIM', 'Condicao': 'Nistatina', 'Tempo_h': 24, 'UFC': 34},
    
    # --- GRÁFICO 2 - 2XCIM ---
    # Controle de Crescimento
    {'Grafico': '2XCIM', 'Condicao': 'Controle de Crescimento', 'Tempo_h': 0, 'UFC': 1917},
    {'Grafico': '2XCIM', 'Condicao': 'Controle de Crescimento', 'Tempo_h': 2, 'UFC': 2000},
    {'Grafico': '2XCIM', 'Condicao': 'Controle de Crescimento', 'Tempo_h': 4, 'UFC': 4000},
    {'Grafico': '2XCIM', 'Condicao': 'Controle de Crescimento', 'Tempo_h': 8, 'UFC': 6667},
    {'Grafico': '2XCIM', 'Condicao': 'Controle de Crescimento', 'Tempo_h': 24, 'UFC': 45000}, # Incontáveis
    # Controle do Veículo
    {'Grafico': '2XCIM', 'Condicao': 'Controle do Veículo', 'Tempo_h': 0, 'UFC': 1712},
    {'Grafico': '2XCIM', 'Condicao': 'Controle do Veículo', 'Tempo_h': 2, 'UFC': 1734},
    {'Grafico': '2XCIM', 'Condicao': 'Controle do Veículo', 'Tempo_h': 4, 'UFC': 3000},
    {'Grafico': '2XCIM', 'Condicao': 'Controle do Veículo', 'Tempo_h': 8, 'UFC': 5200},
    {'Grafico': '2XCIM', 'Condicao': 'Controle do Veículo', 'Tempo_h': 24, 'UFC': 45000}, # Incontáveis
    # EAO (Limoneno)
    {'Grafico': '2XCIM', 'Condicao': 'EAO', 'Tempo_h': 0, 'UFC': 878},
    {'Grafico': '2XCIM', 'Condicao': 'EAO', 'Tempo_h': 2, 'UFC': 723},
    {'Grafico': '2XCIM', 'Condicao': 'EAO', 'Tempo_h': 4, 'UFC': 1134},
    {'Grafico': '2XCIM', 'Condicao': 'EAO', 'Tempo_h': 8, 'UFC': 3039},
    {'Grafico': '2XCIM', 'Condicao': 'EAO', 'Tempo_h': 24, 'UFC': 45000}, # Incontáveis
    # Nistatina
    {'Grafico': '2XCIM', 'Condicao': 'Nistatina', 'Tempo_h': 0, 'UFC': 495},
    {'Grafico': '2XCIM', 'Condicao': 'Nistatina', 'Tempo_h': 2, 'UFC': 62},
    {'Grafico': '2XCIM', 'Condicao': 'Nistatina', 'Tempo_h': 4, 'UFC': 0},
    {'Grafico': '2XCIM', 'Condicao': 'Nistatina', 'Tempo_h': 8, 'UFC': 106},
    {'Grafico': '2XCIM', 'Condicao': 'Nistatina', 'Tempo_h': 24, 'UFC': 12},

    # --- GRÁFICO 3 - 4XCIM ---
    # Controle de Crescimento
    {'Grafico': '4XCIM', 'Condicao': 'Controle de Crescimento', 'Tempo_h': 0, 'UFC': 1917},
    {'Grafico': '4XCIM', 'Condicao': 'Controle de Crescimento', 'Tempo_h': 2, 'UFC': 2000},
    {'Grafico': '4XCIM', 'Condicao': 'Controle de Crescimento', 'Tempo_h': 4, 'UFC': 4000},
    {'Grafico': '4XCIM', 'Condicao': 'Controle de Crescimento', 'Tempo_h': 8, 'UFC': 6667},
    {'Grafico': '4XCIM', 'Condicao': 'Controle de Crescimento', 'Tempo_h': 24, 'UFC': 45000}, # Incontáveis
    # Controle do Veículo
    {'Grafico': '4XCIM', 'Condicao': 'Controle do Veículo', 'Tempo_h': 0, 'UFC': 1712},
    {'Grafico': '4XCIM', 'Condicao': 'Controle do Veículo', 'Tempo_h': 2, 'UFC': 1734},
    {'Grafico': '4XCIM', 'Condicao': 'Controle do Veículo', 'Tempo_h': 4, 'UFC': 3000},
    {'Grafico': '4XCIM', 'Condicao': 'Controle do Veículo', 'Tempo_h': 8, 'UFC': 5200},
    {'Grafico': '4XCIM', 'Condicao': 'Controle do Veículo', 'Tempo_h': 24, 'UFC': 45000}, # Incontáveis
    # EAO (Limoneno)
    {'Grafico': '4XCIM', 'Condicao': 'EAO', 'Tempo_h': 0, 'UFC': 634},
    {'Grafico': '4XCIM', 'Condicao': 'EAO', 'Tempo_h': 2, 'UFC': 523},
    {'Grafico': '4XCIM', 'Condicao': 'EAO', 'Tempo_h': 4, 'UFC': 690},
    {'Grafico': '4XCIM', 'Condicao': 'EAO', 'Tempo_h': 8, 'UFC': 1050},
    {'Grafico': '4XCIM', 'Condicao': 'EAO', 'Tempo_h': 24, 'UFC': 45000}, # Incontáveis
    # Nistatina
    {'Grafico': '4XCIM', 'Condicao': 'Nistatina', 'Tempo_h': 0, 'UFC': 318},
    {'Grafico': '4XCIM', 'Condicao': 'Nistatina', 'Tempo_h': 2, 'UFC': 0},
    {'Grafico': '4XCIM', 'Condicao': 'Nistatina', 'Tempo_h': 4, 'UFC': 0},
    {'Grafico': '4XCIM', 'Condicao': 'Nistatina', 'Tempo_h': 8, 'UFC': 0},
    {'Grafico': '4XCIM', 'Condicao': 'Nistatina', 'Tempo_h': 24, 'UFC': 6},
]

# Criar DataFrame
df = pd.DataFrame(dados_medias)

# Salvar em CSV
df.to_csv('medias_graficos_prontas.csv', index=False)
print("Arquivo 'medias_graficos_prontas.csv' salvo com sucesso!")

# ==========================================================
# 2. PLOTAGEM DOS GRÁFICOS
# ==========================================================
cores = {
    'Controle de Crescimento': '#FFC000', # Amarelo
    'Controle do Veículo': '#A9A9A9',     # Cinza
    'EAO': '#4472C4',                # Azul
    'Nistatina': '#ED7D31'                # Laranja
}

fig, axes = plt.subplots(1, 3, figsize=(18, 5))
graficos = ['CIM', '2XCIM', '4XCIM']
titulos = ['CIM', '2XCIM', '4XCIM']

for i, tipo_grafico in enumerate(graficos):
    ax = axes[i]
    ax.set_title(f"C. albicans ATCC 10231 - {titulos[i]}", fontsize=12, fontweight='bold')
    ax.set_ylim(0, 45000)
    ax.set_xlim(0, 24)
    ax.set_xlabel("Tempo (h)")
    ax.set_ylabel("UFC/mL")

    # DEFINIR OS TICKS DO EIXO X APENAS NOS TEMPOS COLETADOS (0, 2, 4, 8, 24)
    ax.set_xticks([0, 2, 4, 8, 24])

    # Filtrar os dados para este gráfico
    df_sub = df[df['Grafico'] == tipo_grafico]

    # Plotar cada condição
    for condicao, cor in cores.items():
        dados = df_sub[df_sub['Condicao'] == condicao].sort_values('Tempo_h')
        if not dados.empty:
            ax.plot(dados['Tempo_h'], dados['UFC'], 
                    marker='o', linestyle='-', color=cor, 
                    label=condicao, linewidth=2)
            
    ax.legend(loc='upper left', fontsize=9)
    ax.grid(True, linestyle='--', alpha=0.5)

plt.tight_layout()
plt.show()