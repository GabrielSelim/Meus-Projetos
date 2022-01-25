from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pandas as pd
navegador = webdriver.Chrome()


# 1 passo - Pegar a cotação dolar
navegador.get("https://www.google.com.br/")
navegador.find_element(By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys("cotação do dolar")
navegador.find_element(By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys(Keys.ENTER)
cotacao_dolar = navegador.find_element(By.XPATH, '//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]').get_attribute('data-value')
print(cotacao_dolar)

# 2 passo - Pegar a cotação euro
navegador.get("https://www.google.com.br/")
navegador.find_element(By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys("cotação do euro")
navegador.find_element(By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys(Keys.ENTER)
cotacao_euro = navegador.find_element(By.XPATH, '//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]').get_attribute('data-value')
print(cotacao_euro)

# 3 passo - Pegar a cotação ouro
navegador.get("https://www.melhorcambio.com/ouro-hoje")
cotacao_ouro = navegador.find_element(By.XPATH, '//*[@id="comercial"]').get_attribute('value')
cotacao_ouro = cotacao_ouro.replace(',', '.')
print(cotacao_ouro)
navegador.quit()
# 4 passo - Importar a base e Atualizar as cotações na minha base
tabela = pd.read_excel('padrao.xlsx')

# 5 passo - Calcular os novos preços e salvar/exportar a base de dados
tabela.loc[tabela['Moeda'] == 'Dólar', 'Cotação'] = float(cotacao_dolar) #Altera a linha da Cotação que tiver Dólar
tabela.loc[tabela['Moeda'] == 'Euro', 'Cotação'] = float(cotacao_euro) #Altera a linha da Cotação que tiver Euro
tabela.loc[tabela['Moeda'] == 'Ouro', 'Cotação'] = float(cotacao_ouro) #Altera a linha da Cotação que tiver Ouro

#Atualizar as colunas

# Preço de compra = Preço Original * Cotação
tabela['Preço de Compra'] = tabela['Preço Original'] * tabela['Cotação']

# Preço de Venda = Preço de Compra * Margem
tabela['Preço de Venda'] = tabela['Preço de Compra'] * tabela['Margem']

#Exportando o arquivo
tabela.to_excel('Produtos Novos.xlsx', index=False)

