# Importa as bibliotecas necessárias para análise de dados
import numpy as np  # Biblioteca para operações numéricas (não usada diretamente neste código, mas comum em análises)
import pandas as pd  # Biblioteca para manipulação de dados em formato de tabela (DataFrame)

## Importanto os dados com xlsx excel 

covid_excel_sp = pd.read_excel(r'C:\HD\ESTUDOS EM GERAL GRADE 1 SEMENTRES 2025\Curso de Python Analise de Dados\1 . Fundamentos em Python\Code Python\Python\Python\Import\Covid_19\database\dados_covid_sp_excel.xlsx')

print(covid_excel_sp.head())

print(covid_excel_sp.head(20))

# A melhor opção de são arquivos .csc, pois eles tem um melhor desempenho na leitura. 