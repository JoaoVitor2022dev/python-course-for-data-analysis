# Importa as bibliotecas necessárias para análise de dados
import numpy as np  # Biblioteca para operações numéricas (não usada diretamente neste código, mas comum em análises)
import pandas as pd  # Biblioteca para manipulação de dados em formato de tabela (DataFrame)

# Leitura do arquivo CSV com os dados da COVID-19 do estado de SP
# Atenção: usamos uma raw string (prefixo r antes das aspas) para evitar problemas com as barras invertidas (\)
# O separador (sep=';') é usado porque os dados estão no formato CSV separado por ponto e vírgula
# encoding='utf-8' define o padrão de codificação dos caracteres para evitar erros com acentuação e outros símbolos
covid_sp = pd.read_csv(
    r'C:\HD\ESTUDOS EM GERAL GRADE 1 SEMENTRES 2025\Curso de Python Analise de Dados\1 . Fundamentos em Python\Code Python\Python\Import\Covid_19\database\dados_covid_sp.csv',
    sep=';', 
    encoding='utf-8'
)

# Exibe as 20 primeiras linhas do DataFrame para visualização inicial dos dados
# Isso ajuda a entender como os dados estão organizados (colunas, tipos de valores, etc.)
print(covid_sp.head(20))

# Exibe a "forma" (shape) do DataFrame
# Resultado: (linhas, colunas) — muito útil para saber o tamanho do conjunto de dados
print(covid_sp.shape)

# OBS: Se houver erro de codificação ao abrir o arquivo, troque o encoding para 'latin-1' ou 'iso-8859-1' como alternativa:
# covid_sp = pd.read_csv('caminho', sep=';', encoding='latin-1')
