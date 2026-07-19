# Exemplo com os dados extraídos (simulado)
from extrair import df_bruto

df_bruto = df_bruto.copy()  # Supondo que df_bruto seja o DataFrame resultante da função extrair_dados_pdf

# Calcular a média de UFC para cada condição e tempo
df_media = df_bruto.groupby(['Condicao', 'Concentracao', 'Tempo_h'], as_index=False)['UFC_bruto'].mean()

# Criar uma coluna para identificar os gráficos (CIM, 2xCIM, 4xCIM)
def categorizar_grafico(conc):
    if "(CIM)" in conc and "2X" not in conc and "4X" not in conc: return "CIM"
    elif "2X" in conc: return "2XCIM"
    elif "4X" in conc: return "4XCIM"
    else: return "Controle"

df_media['Grafico'] = df_media['Concentracao'].apply(categorizar_grafico)
df_media['Concentracao_Label'] = df_media['Concentracao']

# Exportar para CSV
df_media.to_csv('dados_plotagem.csv', index=False)
print(df_media.head())