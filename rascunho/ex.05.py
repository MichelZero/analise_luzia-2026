import pdfplumber
import re
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def extrair_e_processar_dados(caminho_pdf):
    # Estrutura para armazenar todos os dados brutos
    dados_brutos = []
    
    grafico_atual = None
    experimento_atual = None
    condicao_atual = None

    with pdfplumber.open(caminho_pdf) as pdf:
        for pagina in pdf.pages:
            texto = pagina.extract_text()
            if not texto:
                continue
            linhas = texto.split('\n')
            
            # Resetar o experimento e condição a cada página, mas manter o gráfico da página atual
            experimento_atual = None
            condicao_atual = None
            
            for linha in linhas:
                linha = linha.strip()

                # 1. IDENTIFICAR O GRÁFICO DA PÁGINA (CIM, 2XCIM, 4XCIM)
                if "GRÁFICO" in linha and "CIM" in linha:
                    if "1 - CIM" in linha or "GRÁFICO 1" in linha:
                        grafico_atual = "CIM"
                    elif "2x CIM" in linha or "GRÁFICO 2" in linha:
                        grafico_atual = "2XCIM"
                    elif "4x CIM" in linha or "GRÁFICO 3" in linha:
                        grafico_atual = "4XCIM"

                # 2. IDENTIFICAR O EXPERIMENTO (Exp 1, 2 ou 3)
                match_exp = re.search(r"Experimento\s*(\d+)", linha)
                if match_exp:
                    experimento_atual = f"Exp {match_exp.group(1)}"

                # 3. IDENTIFICAR A CONDIÇÃO E CONCENTRAÇÃO
                if "Controle de crescimento" in linha:
                    condicao_atual = "Controle de Crescimento"
                elif "Controle de veículo" in linha:
                    condicao_atual = "Controle do Veículo"
                elif "EAO" in linha:
                    match_eao = re.search(r"EAO\s+(\d+)\s*µg/mL", linha)
                    if match_eao:
                        condicao_atual = "EAO" # Será renomeado para Limoneno no gráfico
                elif "Nistatina" in linha:
                    match_nis = re.search(r"Nistatina\s+(\d+)\s*µg/mL", linha)
                    if match_nis:
                        condicao_atual = "Nistatina"

                # 4. EXTRAIR OS DADOS DE TEMPO E VALORES (ex: "0h: 2000, 2050, 1900")
                match_tempo = re.search(r"(\d+)h:\s*(.+)", linha)
                if match_tempo and grafico_atual and experimento_atual and condicao_atual:
                    tempo = int(match_tempo.group(1))
                    valores_str = match_tempo.group(2).strip()
                    
                    # Substitui vírgulas por espaço e separa
                    partes = valores_str.replace(",", " ").split()
                    valores = []
                    for p in partes:
                        # Trata "Incontáveis" como NaN (Não é Número)
                        if "incont" in p.lower():
                            valores.append(np.nan)
                        else:
                            valores.append(float(p))
                    
                    # Adiciona cada uma das 3 réplicas ao banco de dados
                    for v in valores:
                        dados_brutos.append({
                            "Grafico": grafico_atual,
                            "Experimento": experimento_atual,
                            "Condicao": condicao_atual,
                            "Tempo_h": tempo,
                            "UFC_bruto": v
                        })

    # Transformar a lista em DataFrame
    df_bruto = pd.DataFrame(dados_brutos)
    
    # --- CALCULAR AS MÉDIAS POR GRÁFICO, CONDIÇÃO E TEMPO ---
    df_medias = df_bruto.groupby(['Grafico', 'Condicao', 'Tempo_h'], as_index=False)['UFC_bruto'].mean()

    # Renomear "EAO" para "Limoneno" para ficar igual ao gráfico desejado
    df_medias['Condicao'] = df_medias['Condicao'].replace('EAO', 'Limoneno')
    
    return df_medias

# ==========================================================
# EXECUTAR A EXTRAÇÃO E CÁLCULO DE MÉDIAS
# ==========================================================
# Substitua 'Dados brutos gráficos.pdf' pelo caminho correto do arquivo
df_final = extrair_e_processar_dados('./dados_brutos/Dados brutos gráficos.pdf')

# Salvar em CSV
df_final.to_csv('medias_para_grafico.csv', index=False)
print("Dados processados com sucesso! Médias salvas em 'medias_para_grafico.csv'.")

# ==========================================================
# PLOTAGEM DOS 3 GRÁFICOS (COM EIXO X: 0, 2, 4, 8, 24)
# ==========================================================
cores = {
    'Controle de Crescimento': '#FFC000', # Amarelo
    'Controle do Veículo': '#A9A9A9',     # Cinza
    'Limoneno': '#4472C4',                # Azul (correspondente ao EAO)
    'Nistatina': '#ED7D31'                # Laranja
}

fig, axes = plt.subplots(1, 3, figsize=(18, 5))
graficos = ['CIM', '2XCIM', '4XCIM']

for i, tipo_grafico in enumerate(graficos):
    ax = axes[i]
    ax.set_title(f"C. Albicans A2 {tipo_grafico}", fontsize=12, fontweight='bold')
    ax.set_ylim(0, 45000)
    ax.set_xlim(0, 24)
    ax.set_xlabel("Tempo (h)")
    ax.set_ylabel("UFC/mL")
    
    # DEFINIR OS TICKS DO EIXO X APENAS NOS TEMPOS REAIS
    ax.set_xticks([0, 2, 4, 8, 24])

    # Filtrar os dados pelo gráfico atual
    df_sub = df_final[df_final['Grafico'] == tipo_grafico]

    # Plotar cada condição
    for condicao, cor in cores.items():
        dados = df_sub[df_sub['Condicao'] == condicao]
        if not dados.empty:
            # DICA: Para fazer a linha subir até 45.000 nos pontos "Incontáveis", 
            # descomente a linha abaixo (substitui NaN por 45000 antes de plotar)
            # dados['UFC_bruto'] = dados['UFC_bruto'].fillna(45000)
            
            ax.plot(dados['Tempo_h'], dados['UFC_bruto'], 
                    marker='o', linestyle='-', color=cor, 
                    label=condicao, linewidth=2)
            
            # Caso queira forçar os pontos "Incontáveis" a não aparecerem (linha cortada),
            # o código acima já irá ignorar os NaN e desenhar uma linha quebrada.

    ax.legend(loc='upper left', fontsize=9)
    ax.grid(True, linestyle='--', alpha=0.5)

plt.tight_layout()
plt.show()