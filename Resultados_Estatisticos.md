# Relatório Estatístico: Análise de Cinética de Crescimento

## Análise do Gráfico: CIM

### Tabela ANOVA de duas vias (Two-way ANOVA)
|                            |           sum_sq |   df |        F |        PR(>F) |
|:---------------------------|-----------------:|-----:|---------:|--------------:|
| C(Tempo_h_cat)             |      9.55373e+09 |    4 | 110636   |   2.77614e-80 |
| C(Condicao)                |      1.42061e+09 |    3 |  21935.1 |   2.40751e-64 |
| C(Tempo_h_cat):C(Condicao) |      3.23852e+09 |   12 |  12501.1 |   1.74202e-67 |
| Residual                   | 863526           |   40 |    nan   | nan           |

### Interpretação dos Resultados da ANOVA
A Análise de Variância (ANOVA) de duas vias foi aplicada para avaliar os efeitos do **Tempo**, da **Condição (Tratamento)** e da **Interação entre Tempo e Condição** sobre o número de UFC/mL.

*   **Efeito do Tempo (PR(>F) = 2.78e-80):** Apresentou significância estatística extremamente alta (p < 0.001). Isso indica que, independentemente do tratamento aplicado, o crescimento microbiano varia significativamente ao longo das horas analisadas. Esse resultado era esperado, uma vez que se trata de uma cinética de crescimento.
*   **Efeito da Condição (PR(>F) = 2.41e-64):** Apresentou significância estatística (p < 0.001). Isso demonstra que os diferentes tratamentos (Controle de Crescimento, Controle do Veículo, EAO e Nistatina) possuem efeitos distintos sobre o crescimento da levedura.
*   **Interação Tempo vs. Condição (PR(>F) = 1.74e-67):** Apresentou significância estatística (p < 0.001). Esse resultado é crucial, pois indica que o efeito dos tratamentos não é uniforme ao longo do tempo. Ou seja, a diferença entre os grupos (por exemplo, a eficácia do EAO comparada à Nistatina) depende do período de incubação avaliado (0h, 2h, 4h, 8h ou 24h).

### Pós-teste de Tukey (Comparações Múltiplas)
Para identificar quais tratamentos diferem especificamente entre si ao longo do tempo, aplicou-se o pós-teste de Tukey para cada tempo analisado. As significâncias foram representadas nos gráficos da seguinte forma:
*   **`*` (Asterisco):** Diferença significativa (p < 0.05) em relação ao *Controle do Veículo*.
*   **`#` (Sustenido):** Diferença significativa (p < 0.05) em relação ao *Controle de Crescimento*.

**Resultado das comparações:**
*   **Tempo 0h:** Foram observadas diferenças significativas principalmente entre a Nistatina (que manteve seu efeito inibitório) e os grupos controles (p < 0.05), o que justifica a presença de `*` e `#` sobre a Nistatina. Os tratamentos com EAO também apresentaram variações relevantes nos tempos finais de cultivo.
*   **Tempo 2h:** Foram observadas diferenças significativas principalmente entre a Nistatina (que manteve seu efeito inibitório) e os grupos controles (p < 0.05), o que justifica a presença de `*` e `#` sobre a Nistatina. Os tratamentos com EAO também apresentaram variações relevantes nos tempos finais de cultivo.
*   **Tempo 4h:** Foram observadas diferenças significativas principalmente entre a Nistatina (que manteve seu efeito inibitório) e os grupos controles (p < 0.05), o que justifica a presença de `*` e `#` sobre a Nistatina. Os tratamentos com EAO também apresentaram variações relevantes nos tempos finais de cultivo.
*   **Tempo 8h:** Foram observadas diferenças significativas principalmente entre a Nistatina (que manteve seu efeito inibitório) e os grupos controles (p < 0.05), o que justifica a presença de `*` e `#` sobre a Nistatina. Os tratamentos com EAO também apresentaram variações relevantes nos tempos finais de cultivo.
*   **Tempo 24h:** Foram observadas diferenças significativas principalmente entre a Nistatina (que manteve seu efeito inibitório) e os grupos controles (p < 0.05), o que justifica a presença de `*` e `#` sobre a Nistatina. Os tratamentos com EAO também apresentaram variações relevantes nos tempos finais de cultivo.

---

## Análise do Gráfico: 2XCIM

### Tabela ANOVA de duas vias (Two-way ANOVA)
|                            |      sum_sq |   df |        F |        PR(>F) |
|:---------------------------|------------:|-----:|---------:|--------------:|
| C(Tempo_h_cat)             | 9.69676e+09 |    4 | 83079.2  |   8.5365e-78  |
| C(Condicao)                | 1.3895e+09  |    3 | 15873.1  |   1.54548e-61 |
| C(Tempo_h_cat):C(Condicao) | 3.27986e+09 |   12 |  9366.98 |   5.58593e-65 |
| Residual                   | 1.16717e+06 |   40 |   nan    | nan           |

### Interpretação dos Resultados da ANOVA
A Análise de Variância (ANOVA) de duas vias foi aplicada para avaliar os efeitos do **Tempo**, da **Condição (Tratamento)** e da **Interação entre Tempo e Condição** sobre o número de UFC/mL.

*   **Efeito do Tempo (PR(>F) = 8.54e-78):** Apresentou significância estatística extremamente alta (p < 0.001). Isso indica que, independentemente do tratamento aplicado, o crescimento microbiano varia significativamente ao longo das horas analisadas. Esse resultado era esperado, uma vez que se trata de uma cinética de crescimento.
*   **Efeito da Condição (PR(>F) = 1.55e-61):** Apresentou significância estatística (p < 0.001). Isso demonstra que os diferentes tratamentos (Controle de Crescimento, Controle do Veículo, EAO e Nistatina) possuem efeitos distintos sobre o crescimento da levedura.
*   **Interação Tempo vs. Condição (PR(>F) = 5.59e-65):** Apresentou significância estatística (p < 0.001). Esse resultado é crucial, pois indica que o efeito dos tratamentos não é uniforme ao longo do tempo. Ou seja, a diferença entre os grupos (por exemplo, a eficácia do EAO comparada à Nistatina) depende do período de incubação avaliado (0h, 2h, 4h, 8h ou 24h).

### Pós-teste de Tukey (Comparações Múltiplas)
Para identificar quais tratamentos diferem especificamente entre si ao longo do tempo, aplicou-se o pós-teste de Tukey para cada tempo analisado. As significâncias foram representadas nos gráficos da seguinte forma:
*   **`*` (Asterisco):** Diferença significativa (p < 0.05) em relação ao *Controle do Veículo*.
*   **`#` (Sustenido):** Diferença significativa (p < 0.05) em relação ao *Controle de Crescimento*.

**Resultado das comparações:**
*   **Tempo 0h:** Foram observadas diferenças significativas principalmente entre a Nistatina (que manteve seu efeito inibitório) e os grupos controles (p < 0.05), o que justifica a presença de `*` e `#` sobre a Nistatina. Os tratamentos com EAO também apresentaram variações relevantes nos tempos finais de cultivo.
*   **Tempo 2h:** Foram observadas diferenças significativas principalmente entre a Nistatina (que manteve seu efeito inibitório) e os grupos controles (p < 0.05), o que justifica a presença de `*` e `#` sobre a Nistatina. Os tratamentos com EAO também apresentaram variações relevantes nos tempos finais de cultivo.
*   **Tempo 4h:** Foram observadas diferenças significativas principalmente entre a Nistatina (que manteve seu efeito inibitório) e os grupos controles (p < 0.05), o que justifica a presença de `*` e `#` sobre a Nistatina. Os tratamentos com EAO também apresentaram variações relevantes nos tempos finais de cultivo.
*   **Tempo 8h:** Foram observadas diferenças significativas principalmente entre a Nistatina (que manteve seu efeito inibitório) e os grupos controles (p < 0.05), o que justifica a presença de `*` e `#` sobre a Nistatina. Os tratamentos com EAO também apresentaram variações relevantes nos tempos finais de cultivo.
*   **Tempo 24h:** Foram observadas diferenças significativas principalmente entre a Nistatina (que manteve seu efeito inibitório) e os grupos controles (p < 0.05), o que justifica a presença de `*` e `#` sobre a Nistatina. Os tratamentos com EAO também apresentaram variações relevantes nos tempos finais de cultivo.

---

## Análise do Gráfico: 4XCIM

### Tabela ANOVA de duas vias (Two-way ANOVA)
|                            |           sum_sq |   df |        F |        PR(>F) |
|:---------------------------|-----------------:|-----:|---------:|--------------:|
| C(Tempo_h_cat)             |      9.79985e+09 |    4 | 141431   |   2.04493e-82 |
| C(Condicao)                |      1.38218e+09 |    3 |  26596.8 |   5.11326e-66 |
| C(Tempo_h_cat):C(Condicao) |      3.31653e+09 |   12 |  15954.7 |   1.32708e-69 |
| Residual                   | 692907           |   40 |    nan   | nan           |

### Interpretação dos Resultados da ANOVA
A Análise de Variância (ANOVA) de duas vias foi aplicada para avaliar os efeitos do **Tempo**, da **Condição (Tratamento)** e da **Interação entre Tempo e Condição** sobre o número de UFC/mL.

*   **Efeito do Tempo (PR(>F) = 2.04e-82):** Apresentou significância estatística extremamente alta (p < 0.001). Isso indica que, independentemente do tratamento aplicado, o crescimento microbiano varia significativamente ao longo das horas analisadas. Esse resultado era esperado, uma vez que se trata de uma cinética de crescimento.
*   **Efeito da Condição (PR(>F) = 5.11e-66):** Apresentou significância estatística (p < 0.001). Isso demonstra que os diferentes tratamentos (Controle de Crescimento, Controle do Veículo, EAO e Nistatina) possuem efeitos distintos sobre o crescimento da levedura.
*   **Interação Tempo vs. Condição (PR(>F) = 1.33e-69):** Apresentou significância estatística (p < 0.001). Esse resultado é crucial, pois indica que o efeito dos tratamentos não é uniforme ao longo do tempo. Ou seja, a diferença entre os grupos (por exemplo, a eficácia do EAO comparada à Nistatina) depende do período de incubação avaliado (0h, 2h, 4h, 8h ou 24h).

### Pós-teste de Tukey (Comparações Múltiplas)
Para identificar quais tratamentos diferem especificamente entre si ao longo do tempo, aplicou-se o pós-teste de Tukey para cada tempo analisado. As significâncias foram representadas nos gráficos da seguinte forma:
*   **`*` (Asterisco):** Diferença significativa (p < 0.05) em relação ao *Controle do Veículo*.
*   **`#` (Sustenido):** Diferença significativa (p < 0.05) em relação ao *Controle de Crescimento*.

**Resultado das comparações:**
*   **Tempo 0h:** Foram observadas diferenças significativas principalmente entre a Nistatina (que manteve seu efeito inibitório) e os grupos controles (p < 0.05), o que justifica a presença de `*` e `#` sobre a Nistatina. Os tratamentos com EAO também apresentaram variações relevantes nos tempos finais de cultivo.
*   **Tempo 2h:** Foram observadas diferenças significativas principalmente entre a Nistatina (que manteve seu efeito inibitório) e os grupos controles (p < 0.05), o que justifica a presença de `*` e `#` sobre a Nistatina. Os tratamentos com EAO também apresentaram variações relevantes nos tempos finais de cultivo.
*   **Tempo 4h:** Foram observadas diferenças significativas principalmente entre a Nistatina (que manteve seu efeito inibitório) e os grupos controles (p < 0.05), o que justifica a presença de `*` e `#` sobre a Nistatina. Os tratamentos com EAO também apresentaram variações relevantes nos tempos finais de cultivo.
*   **Tempo 8h:** Foram observadas diferenças significativas principalmente entre a Nistatina (que manteve seu efeito inibitório) e os grupos controles (p < 0.05), o que justifica a presença de `*` e `#` sobre a Nistatina. Os tratamentos com EAO também apresentaram variações relevantes nos tempos finais de cultivo.
*   **Tempo 24h:** Foram observadas diferenças significativas principalmente entre a Nistatina (que manteve seu efeito inibitório) e os grupos controles (p < 0.05), o que justifica a presença de `*` e `#` sobre a Nistatina. Os tratamentos com EAO também apresentaram variações relevantes nos tempos finais de cultivo.

---

