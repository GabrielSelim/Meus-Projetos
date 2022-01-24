# Passo 1 - Importabase de dados

import pandas as pd
import plotly.express as px

tabela = pd.read_csv(r'telecom_users.csv')

# Passo 2 - Tratamento de dados(corrigir os problemas da base de dados)

tabela = tabela.drop('Unnamed: 0', axis=1) #removendo as colunas nao utilizavel
tabela = tabela.drop('IDCliente', axis=1)
tabela['TotalGasto'] = pd.to_numeric(tabela['TotalGasto'], errors='coerce')    #Arrumando os Valores reconhecidos de forma errada
tabela = tabela.dropna(how='all', axis=1)     #tratar valores vazios colunas
tabela = tabela.dropna(how='any', axis=0)    #tratar valores vazios linhas
print(tabela.info())

# Passo 3 - Analise Inicial

print(tabela['Churn'].value_counts())
print(tabela['Churn'].value_counts(normalize=True).map('{:.2%}'.format))

# Passo 4 - Analise detalhada dos clientes

for coluna in tabela.columns:
    grafico = px.histogram(tabela, x=coluna, color='Churn')
    grafico.show()
