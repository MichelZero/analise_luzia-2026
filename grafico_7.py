import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm
from statsmodels.formula.api import ols
from statsmodels.stats.multicomp import pairwise_tukeyhsd
import scikit_posthocs as sp

# ==========================================================
# PASSO 1: CARREGAR OS DADOS BRUTOS (COM AS RÉPLICAS)
# Substitua pelo caminho do seu CSV montado com as triplicatas!
# ==========================================================
# Exemplo de carregamento:
# df = pd.read_csv('dados_triplicatas.csv')

# Para testarmos aqui, vou criar um DATAFRAME SIMULADO baseado nas suas médias.
# OBS: Na vida real, você DEVE usar os dados brutos.
# Aqui eu crio um desvio padrão artificial só para o código rodar como exemplo.
dados_exemplo = []
graficos = ['CIM', '2XCIM', '4XCIM']
condicoes = ['Controle de Crescimento', 'Controle do Veículo', 'EAO', 'Nistatina']
tempos = [0, 2, 4, 8, 24]

# Preciso das médias originais para simular triplicatas
medias_reais = {
    ('CIM', 'Controle de Crescimento'): {0:1917, 2:2000, 4:4000, 8:6667, 24:45000},
    ('CIM', 'Controle do Veículo'): {0:1712, 2:1734, 4:3000, 8:5200, 24:45000},
    ('CIM', 'EAO'): {0:1617, 2:1062, 4:2056, 8:4800, 24:45000},
    ('CIM', 'Nistatina'): {0:578, 2:245, 4:0, 8:217, 24:34},
    ('2XCIM', 'Controle de Crescimento'): {0:1917, 2:2000, 4:4000, 8:6667, 24:45000},
    ('2XCIM', 'Controle do Veículo'): {0:1712, 2:1734, 4:3000, 8:5200, 24:45000},
    ('2XCIM', 'EAO'): {0:878, 2:723, 4:1134, 8:3039, 24:45000},
    ('2XCIM', 'Nistatina'): {0:495, 2:62, 4:0, 8:106, 24:12},
    ('4XCIM', 'Controle de Crescimento'): {0:1917, 2:2000, 4:4000, 8:6667, 24:45000},
    ('4XCIM', 'Controle do Veículo'): {0:1712, 2:1734, 4:3000, 8:5200, 24:45000},
    ('4XCIM', 'EAO'): {0:634, 2:523, 4:690, 8:1050, 24:45000},
    ('4XCIM', 'Nistatina'): {0:318, 2:0, 4:0, 8:0, 24:6},
}

# Criar 3 réplicas com pequenas variações (simulação)
import random
for g in graficos:
    for c in condicoes:
        for t in tempos:
            media = medias_reais.get((g, c), {}).get(t, 0)
            if media == 45000: # Se for incontável, mantenha variabilidade alta
                reps = [44800, 45000, 45200] 
            else:
                reps = [media * (1 + random.uniform(-0.1, 0.1)) for _ in range(3)]
            for i, r in enumerate(reps):
                dados_exemplo.append({'Grafico': g, 'Condicao': c, 'Tempo_h': t, 'Replica': i+1, 'UFC': r})

df = pd.DataFrame(dados_exemplo)

# ==========================================================
# PASSO 2: REALIZAR A ANOVA DE DUAS VIAS E PÓS-TESTE DE TUKEY
# ==========================================================
def analisar_estatisticas(df_sub):
    # 1. ANOVA de duas vias (Fatores: Tempo e Condição)
    # Nota: Convertemos Tempo_h para categoria
    df_sub['Tempo_h_cat'] = df_sub['Tempo_h'].astype('category')
    model = ols('UFC ~ C(Tempo_h_cat) + C(Condicao) + C(Tempo_h_cat):C(Condicao)', data=df_sub).fit()
    anova_table = sm.stats.anova_lm(model, typ=2)
    print("\n--- Tabela ANOVA ---")
    print(anova_table)
    
    # 2. Pós-teste de Tukey para cada tempo, comparando todas as Condições
    # O objetivo é encontrar onde estão as diferenças.
    resultados_tukey = {}
    for tempo in [0, 2, 4, 8, 24]:
        df_tempo = df_sub[df_sub['Tempo_h'] == tempo]
        if not df_tempo.empty and len(df_tempo['Condicao'].unique()) > 1:
            tukey = sp.posthoc_tukey(df_tempo, val_col='UFC', group_col='Condicao')
            resultados_tukey[tempo] = tukey
    return resultados_tukey

# ==========================================================
# PASSO 3: PLOTAR COM ANOTAÇÕES (# e *)
# ==========================================================
def plotar_com_anotacoes(df, resultados_tukey, tipo_grafico, ax):
    # Cores e estilos
    cores = {
        'Controle de Crescimento': '#FFC000',
        'Controle do Veículo': '#A9A9A9',
        'EAO': '#4472C4',
        'Nistatina': '#ED7D31'
    }
    
    # Filtrar o gráfico específico
    df_sub = df[df['Grafico'] == tipo_grafico]
    
    # Plotar linhas
    for condicao, cor in cores.items():
        dados = df_sub[df_sub['Condicao'] == condicao].sort_values('Tempo_h')
        if not dados.empty:
            # Precisamos calcular a média para plotar os pontos
            media_por_tempo = dados.groupby('Tempo_h')['UFC'].mean().reset_index()
            ax.plot(media_por_tempo['Tempo_h'], media_por_tempo['UFC'], 
                    marker='o', linestyle='-', color=cor, label=condicao, linewidth=2)

    # Adicionar as marcas de significância (com base na tabela Tukey)
    # Definição de marcas padrão:
    # * = Significativo (p < 0.05) em relação ao Controle do Veículo
    # # = Significativo (p < 0.05) em relação ao Controle de Crescimento
    
    for tempo in [0, 2, 4, 8, 24]:
        if tempo not in resultados_tukey:
            continue
        tukey_table = resultados_tukey[tempo]
        
        # Para cada condição, verificar o p-valor em relação ao Veículo e Crescimento
        for condicao in cores.keys():
            if condicao in ['Controle de Crescimento', 'Controle do Veículo']:
                continue # Pula os controles, só anotamos os tratamentos
            
            # Verifica se existe dados para este tempo
            media_tempo = df_sub[(df_sub['Condicao'] == condicao) & (df_sub['Tempo_h'] == tempo)]['UFC'].mean()
            if np.isnan(media_tempo):
                continue

            # Pega o p-valor contra os dois controles
            p_vs_cresc = tukey_table.loc[condicao, 'Controle de Crescimento'] if 'Controle de Crescimento' in tukey_table.columns else 1.0
            p_vs_veic = tukey_table.loc[condicao, 'Controle do Veículo'] if 'Controle do Veículo' in tukey_table.columns else 1.0
            
            texto_marcador = ""
            if p_vs_cresc < 0.05:
                texto_marcador += "#" # Significativo vs Crescimento
            if p_vs_veic < 0.05:
                texto_marcador += "*" # Significativo vs Veículo
            
            # Posicionar o texto acima do ponto
            if texto_marcador:
                ax.text(tempo, media_tempo + 2000, texto_marcador, 
                        ha='center', va='bottom', fontsize=12, fontweight='bold', color='black')

# ==========================================================
# PASSO 4: RODAR A ANÁLISE E GERAR OS 3 GRÁFICOS
# ==========================================================
fig, axes = plt.subplots(1, 3, figsize=(20, 6))
tipos_graficos = ['CIM', '2XCIM', '4XCIM']

for i, tipo in enumerate(tipos_graficos):
    print(f"\nAnalisando Gráfico {tipo}...")
    df_sub = df[df['Grafico'] == tipo]
    
    # Realiza a ANOVA e Tukey para este gráfico específico
    tukey_resultados = analisar_estatisticas(df_sub)
    
    # Plota no subplot
    ax = axes[i]
    ax.set_title(f"C. albicans ATCC 10231 - {tipo}", fontsize=14, fontweight='bold')
    ax.set_ylim(0, 48000)
    ax.set_xlim(-1, 25)
    ax.set_xlabel("Tempo (h)", fontsize=12)
    ax.set_ylabel("UFC/mL", fontsize=12)
    ax.set_xticks([0, 2, 4, 8, 24])
    ax.grid(True, linestyle='--', alpha=0.5)
    
    plotar_com_anotacoes(df, tukey_resultados, tipo, ax)
    
    if i == 0:
        ax.legend(loc='upper left', fontsize=10)

plt.tight_layout()
plt.show()