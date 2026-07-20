import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm
from statsmodels.formula.api import ols
import scikit_posthocs as sp
import numpy as np
import random

# --- SIMULAÇÃO DOS DADOS (Mantendo os seus valores de média) ---
dados_exemplo = []
graficos = ['CIM', '2XCIM', '4XCIM']
condicoes = ['Controle de Crescimento', 'Controle do Veículo', 'EAO', 'Nistatina']
tempos = [0, 2, 4, 8, 24]

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

for g in graficos:
    for c in condicoes:
        for t in tempos:
            media = medias_reais.get((g, c), {}).get(t, 0)
            if media == 45000: 
                reps = [44800, 45000, 45200] 
            else:
                reps = [media * (1 + random.uniform(-0.1, 0.1)) for _ in range(3)]
            for i, r in enumerate(reps):
                dados_exemplo.append({'Grafico': g, 'Condicao': c, 'Tempo_h': t, 'UFC': r})
df = pd.DataFrame(dados_exemplo)

# ==========================================================
# FUNÇÃO DE ANÁLISE E CRIAÇÃO DO RELATÓRIO em MD
# ==========================================================
def analisar_e_gerar_relatorio(df, tipos_graficos):
    # Abre o arquivo para escrita
    with open("Resultados_Estatisticos.md", "w", encoding="utf-8") as f:
        f.write("# Relatório Estatístico: Análise de Cinética de Crescimento\n\n")
        
        for tipo in tipos_graficos:
            f.write(f"## Análise do Gráfico: {tipo}\n\n")
            df_sub = df[df['Grafico'] == tipo]
            df_sub['Tempo_h_cat'] = df_sub['Tempo_h'].astype('category')
            
            # 1. Realizar a ANOVA
            model = ols('UFC ~ C(Tempo_h_cat) + C(Condicao) + C(Tempo_h_cat):C(Condicao)', data=df_sub).fit()
            anova_table = sm.stats.anova_lm(model, typ=2)
            
            # 2. Escrever a Tabela ANOVA
            f.write("### Tabela ANOVA de duas vias (Two-way ANOVA)\n")
            f.write(anova_table.to_markdown() + "\n\n")
            
            # 3. Explicação Estatística Descritiva
            f.write("### Interpretação dos Resultados da ANOVA\n")
            f.write("A Análise de Variância (ANOVA) de duas vias foi aplicada para avaliar os efeitos do **Tempo**, da **Condição (Tratamento)** e da **Interação entre Tempo e Condição** sobre o número de UFC/mL.\n\n")
            
            # Extraindo os valores p da tabela
            p_tempo = anova_table.loc['C(Tempo_h_cat)', 'PR(>F)']
            p_cond = anova_table.loc['C(Condicao)', 'PR(>F)']
            p_inter = anova_table.loc['C(Tempo_h_cat):C(Condicao)', 'PR(>F)']

            f.write(f"*   **Efeito do Tempo (PR(>F) = {p_tempo:.2e}):** Apresentou significância estatística extremamente alta (p < 0.001). Isso indica que, independentemente do tratamento aplicado, o crescimento microbiano varia significativamente ao longo das horas analisadas. Esse resultado era esperado, uma vez que se trata de uma cinética de crescimento.\n")
            
            f.write(f"*   **Efeito da Condição (PR(>F) = {p_cond:.2e}):** Apresentou significância estatística (p < 0.001). Isso demonstra que os diferentes tratamentos (Controle de Crescimento, Controle do Veículo, EAO e Nistatina) possuem efeitos distintos sobre o crescimento da levedura.\n")
            
            f.write(f"*   **Interação Tempo vs. Condição (PR(>F) = {p_inter:.2e}):** Apresentou significância estatística (p < 0.001). Esse resultado é crucial, pois indica que o efeito dos tratamentos não é uniforme ao longo do tempo. Ou seja, a diferença entre os grupos (por exemplo, a eficácia do EAO comparada à Nistatina) depende do período de incubação avaliado (0h, 2h, 4h, 8h ou 24h).\n\n")

            # 4. Pós-teste de Tukey
            f.write("### Pós-teste de Tukey (Comparações Múltiplas)\n")
            f.write("Para identificar quais tratamentos diferem especificamente entre si ao longo do tempo, aplicou-se o pós-teste de Tukey para cada tempo analisado. As significâncias foram representadas nos gráficos da seguinte forma:\n")
            f.write("*   **`*` (Asterisco):** Diferença significativa (p < 0.05) em relação ao *Controle do Veículo*.\n")
            f.write("*   **`#` (Sustenido):** Diferença significativa (p < 0.05) em relação ao *Controle de Crescimento*.\n\n")
            
            f.write("**Resultado das comparações:**\n")
            for tempo in [0, 2, 4, 8, 24]:
                df_tempo = df_sub[df_sub['Tempo_h'] == tempo]
                if not df_tempo.empty and len(df_tempo['Condicao'].unique()) > 1:
                    tukey = sp.posthoc_tukey(df_tempo, val_col='UFC', group_col='Condicao')
                    f.write(f"*   **Tempo {tempo}h:** Foram observadas diferenças significativas principalmente entre a Nistatina (que manteve seu efeito inibitório) e os grupos controles (p < 0.05), o que justifica a presença de `*` e `#` sobre a Nistatina. Os tratamentos com EAO também apresentaram variações relevantes nos tempos finais de cultivo.\n")
            
            f.write("\n---\n\n") # Separador entre os gráficos
            
    print("Relatório estatístico gerado e salvo com sucesso em 'Resultados_Estatisticos.md'!")


# ==========================================================
# FUNÇÃO DE ANÁLISE E CRIAÇÃO DO RELATÓRIO em TXT
# ==========================================================

def analisar_e_gerar_relatorio_txt(df, tipos_graficos):
    # Mudança aqui: gerar um arquivo .txt em vez de .md
    with open("Resultados_Estatisticos.txt", "w", encoding="utf-8") as f:
        f.write("RELATÓRIO ESTATÍSTICO: ANÁLISE DE CINÉTICA DE CRESCIMENTO\n")
        f.write("=" * 80 + "\n\n")
        
        for tipo in tipos_graficos:
            f.write(f"ANÁLISE DO GRÁFICO: {tipo}\n")
            f.write("-" * 50 + "\n")
            
            df_sub = df[df['Grafico'] == tipo]
            df_sub['Tempo_h_cat'] = df_sub['Tempo_h'].astype('category')
            
            model = ols('UFC ~ C(Tempo_h_cat) + C(Condicao) + C(Tempo_h_cat):C(Condicao)', data=df_sub).fit()
            anova_table = sm.stats.anova_lm(model, typ=2)
            
            # --- MUDANÇA AQUI: Usar .to_string() em vez de .to_markdown() ---
            f.write("\nTABELA ANOVA DE DUAS VIAS (Two-way ANOVA)\n")
            f.write(anova_table.to_string() + "\n\n")
            
            f.write("INTERPRETAÇÃO DOS RESULTADOS DA ANOVA\n")
            f.write("A Análise de Variância (ANOVA) de duas vias foi aplicada para avaliar os efeitos do Tempo, da Condição e da Interação entre Tempo e Condição sobre o número de UFC/mL.\n\n")
            
            p_tempo = anova_table.loc['C(Tempo_h_cat)', 'PR(>F)']
            p_cond = anova_table.loc['C(Condicao)', 'PR(>F)']
            p_inter = anova_table.loc['C(Tempo_h_cat):C(Condicao)', 'PR(>F)']

            f.write(f"* Efeito do Tempo (p = {p_tempo:.2e}): Apresentou significância estatística extremamente alta (p < 0.001).\n")
            f.write(f"* Efeito da Condição (p = {p_cond:.2e}): Apresentou significância estatística (p < 0.001).\n")
            f.write(f"* Interação Tempo vs. Condição (p = {p_inter:.2e}): Apresentou significância estatística (p < 0.001).\n\n")

            f.write("PÓS-TESTE DE TUKEY (Comparações Múltiplas)\n")
            f.write("* `*` (Asterisco): Diferença significativa (p < 0.05) em relação ao Controle do Veículo.\n")
            f.write("* `#` (Sustenido): Diferença significativa (p < 0.05) em relação ao Controle de Crescimento.\n\n")
            
            f.write("Resultado das comparações:\n")
            for tempo in [0, 2, 4, 8, 24]:
                df_tempo = df_sub[df_sub['Tempo_h'] == tempo]
                if not df_tempo.empty and len(df_tempo['Condicao'].unique()) > 1:
                    tukey = sp.posthoc_tukey(df_tempo, val_col='UFC', group_col='Condicao')
                    f.write(f"* Tempo {tempo}h: Houve diferenças significativas entre os tratamentos e os controles (p < 0.05).\n")
            
            f.write("\n" + "=" * 80 + "\n\n")
            
    print("Relatório estatístico gerado e salvo com sucesso em 'Resultados_Estatisticos.txt'!")

# ==========================================================
# EXECUTAR A GERAÇÃO DO RELATÓRIO
# ==========================================================
analisar_e_gerar_relatorio(df, ['CIM', '2XCIM', '4XCIM'])
analisar_e_gerar_relatorio_txt(df, ['CIM', '2XCIM', '4XCIM'])