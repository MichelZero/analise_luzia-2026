import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm
from statsmodels.formula.api import ols
import scikit_posthocs as sp
import numpy as np
import random

# ==========================================================
# 1. CARREGAR OS DADOS BRUTOS (OU SUAS MÉDIAS)
# SE FOR USAR O CSV QUE VOCÊ GEROU ANTERIORMENTE, DESCOMENTE A LINHA ABAIXO:
# df = pd.read_csv('medias_graficos_prontas.csv')

# COMO ESTOU USANDO UM EXEMPLO, VOU RECRIAR OS DADOS BASEADOS NO QUE VOCÊ ENVIOU
# (NA PRÁTICA, VOCÊ PODE USAR O SEU DATAFRAME DE MÉDIAS)
dados_exemplo = []
graficos = ['CIM', '2XCIM', '4XCIM']
condicoes = ['Controle de Crescimento', 'Controle do Veículo', 'EAO', 'Nistatina']
tempos = [0, 2, 4, 8, 24]

# Simulando as médias que você passou
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

# Criando triplicatas simuladas com pequena variação (substitua pelo seu CSV real)
for g in graficos:
    for c in condicoes:
        for t in tempos:
            media = medias_reais.get((g, c), {}).get(t, 0)
            if media == 45000: 
                reps = [44800, 45000, 45200] # Simulação de "Incontáveis" no topo
            else:
                reps = [media * (1 + random.uniform(-0.1, 0.1)) for _ in range(3)]
            for i, r in enumerate(reps):
                dados_exemplo.append({'Grafico': g, 'Condicao': c, 'Tempo_h': t, 'UFC': r})

df = pd.DataFrame(dados_exemplo)

# ==========================================================
# 2. REALIZAR A ANOVA E PÓS-TESTE (Função auxiliar)
# ==========================================================
def analisar_estatisticas(df_sub):
    df_sub['Tempo_h_cat'] = df_sub['Tempo_h'].astype('category')
    model = ols('UFC ~ C(Tempo_h_cat) + C(Condicao) + C(Tempo_h_cat):C(Condicao)', data=df_sub).fit()
    
    resultados_tukey = {}
    for tempo in [0, 2, 4, 8, 24]:
        df_tempo = df_sub[df_sub['Tempo_h'] == tempo]
        if not df_tempo.empty and len(df_tempo['Condicao'].unique()) > 1:
            resultados_tukey[tempo] = sp.posthoc_tukey(df_tempo, val_col='UFC', group_col='Condicao')
    return resultados_tukey

# ==========================================================
# 3. PLOTAR CADA GRÁFICO SEPARADAMENTE
# ==========================================================
cores = {
    'Controle de Crescimento': '#FFC000', # Amarelo
    'Controle do Veículo': '#A9A9A9',     # Cinza
    'EAO': '#4472C4',                     # Azul (Trocado de Limoneno para EAO)
    'Nistatina': '#ED7D31'                # Laranja
}

# Laço para gerar cada gráfico como uma janela independente
tipos_graficos = ['CIM', '2XCIM', '4XCIM']

for tipo in tipos_graficos:
    print(f"Gerando gráfico {tipo}...")
    df_sub = df[df['Grafico'] == tipo]
    
    # ANOVA e Tukey para este gráfico
    tukey_resultados = analisar_estatisticas(df_sub)
    
    # Cria uma NOVA figura (tela) independente
    plt.figure(figsize=(8, 6)) 
    
    plt.title(f"C. albicans ATCC 10231 - {tipo}", fontsize=14, fontweight='bold')
    plt.ylim(0, 48000)
    plt.xlim(-1, 25)
    plt.xlabel("Tempo (h)", fontsize=12)
    plt.ylabel("UFC/mL", fontsize=12)
    plt.xticks([0, 2, 4, 8, 24]) # Marcações apenas nos seus tempos de coleta
    plt.grid(True, linestyle='--', alpha=0.5)

    # Plotar linhas e pontos
    for condicao, cor in cores.items():
        dados = df_sub[df_sub['Condicao'] == condicao].sort_values('Tempo_h')
        if not dados.empty:
            # Calculando a média para desenhar a linha central
            media_por_tempo = dados.groupby('Tempo_h')['UFC'].mean().reset_index()
            plt.plot(media_por_tempo['Tempo_h'], media_por_tempo['UFC'], 
                    marker='o', linestyle='-', color=cor, label=condicao, linewidth=2)

    # Inserir asteriscos e sustenidos (anotações)
    for tempo in [0, 2, 4, 8, 24]:
        if tempo not in tukey_resultados: continue
        tukey_table = tukey_resultados[tempo]
        
        for condicao in cores.keys():
            if condicao in ['Controle de Crescimento', 'Controle do Veículo']:
                continue # Não anotamos os controles
            
            media_tempo = df_sub[(df_sub['Condicao'] == condicao) & (df_sub['Tempo_h'] == tempo)]['UFC'].mean()
            if np.isnan(media_tempo): continue
            
            # Pega p-valores
            p_vs_cresc = tukey_table.loc[condicao, 'Controle de Crescimento'] if 'Controle de Crescimento' in tukey_table.columns else 1.0
            p_vs_veic = tukey_table.loc[condicao, 'Controle do Veículo'] if 'Controle do Veículo' in tukey_table.columns else 1.0
            
            texto_marcador = ""
            if p_vs_cresc < 0.05: texto_marcador += "#"
            if p_vs_veic < 0.05: texto_marcador += "*"
            
            if texto_marcador:
                plt.text(tempo, media_tempo + 2000, texto_marcador, 
                        ha='center', va='bottom', fontsize=12, fontweight='bold', color='black')

    plt.legend(loc='upper left', fontsize=10)
    plt.tight_layout()

    # Salvar o gráfico em disco como imagem PNG (opcional)
    # plt.savefig(f'{tipo}_grafico.png', dpi=300)
    
    # Exibir o gráfico na tela
    plt.show()
    plt.close() # Fecha a figura em memória após exibir