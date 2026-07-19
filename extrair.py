import pdfplumber
import re
import pandas as pd
import numpy as np

def extrair_dados_pdf(caminho_pdf):
    # Dicionário para armazenar os dados estruturados
    dados = []
    condicao_atual = None
    concentracao_atual = None
    experimento_atual = None

    with pdfplumber.open(caminho_pdf) as pdf:
        for pagina in pdf.pages:
            texto = pagina.extract_text()
            linhas = texto.split('\n')

            for linha in linhas:
                linha = linha.strip()
                
                # Identifica o experimento (1, 2, 3)
                if "Experimento" in linha:
                    match = re.search(r"Experimento\s*(\d+)", linha)
                    if match:
                        experimento_atual = f"Exp {match.group(1)}"

                # Identifica a condição (Controle, EAO, Nistatina) e Concentração
                elif "Controle de crescimento" in linha:
                    condicao_atual = "Controle Crescimento"
                    concentracao_atual = "Controle"
                elif "Controle de veículo" in linha:
                    condicao_atual = "Controle Veículo"
                    concentracao_atual = "Controle"
                elif "EAO" in linha:
                    match = re.search(r"EAO\s+(\d+)\s*µg/mL\s*\(?([^)]*)\)?", linha)
                    if match:
                        condicao_atual = "EAO"
                        concentracao_atual = f"{match.group(1)} µg/mL ({match.group(2)})"
                elif "Nistatina" in linha:
                    match = re.search(r"Nistatina\s+(\d+)\s*µg/mL\s*\(?([^)]*)\)?", linha)
                    if match:
                        condicao_atual = "Nistatina"
                        concentracao_atual = f"{match.group(1)} µg/mL ({match.group(2)})"

                # Extrai os tempos e valores (ex: "0h: 2000, 2050, 1900")
                elif "h:" in linha and experimento_atual and condicao_atual:
                    match = re.search(r"(\d+)h:\s*([\d,\s]+)", linha)
                    if match:
                        tempo = int(match.group(1))
                        valores_str = match.group(2).replace(",", " ").split()
                        # Converte para float, trata "Incontaveis" ou variações como NaN
                        valores = []
                        for v in valores_str:
                            if "incont" in v.lower():
                                valores.append(np.nan) # ou substitua por 45000 se quiser forçar um limite
                            else:
                                valores.append(float(v))
                        
                        # Adiciona ao banco de dados
                        for valor in valores:
                            dados.append({
                                "Experimento": experimento_atual,
                                "Condicao": condicao_atual,
                                "Concentracao": concentracao_atual,
                                "Tempo_h": tempo,
                                "UFC_bruto": valor
                            })
    return pd.DataFrame(dados)

# Use o caminho do seu arquivo PDF
# df_bruto = extrair_dados_pdf("Dados brutos gráficos.pdf")
df_bruto = extrair_dados_pdf("./dados_brutos/Dados brutos gráficos.pdf")