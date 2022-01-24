from time import sleep
import pyautogui
import pyperclip
import pandas as pd
pyautogui.PAUSE = 1

# Os point click estão todos adequados para os meus monitores, para rodar em outro computador é necessário adequar para o seu

#Passo 1 - Abrir o Chrome
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")
pyautogui.click(x=570, y=863)

#Passo 2 - Acessar o link do OneDrive
pyperclip.copy("https://onedrive.live.com/?authkey=%21AHKoHP8FUkhNuT8&id=8D8F7DD925BC6E7D%211536&cid=8D8F7DD925BC6E7D")
pyautogui.hotkey('ctrl', 'v')
pyautogui.press('enter')
sleep(5)

#Passo 3 - Navegar no OneDrive até o arquivo
pyautogui.click(x=2033, y=324)
sleep(5)

#Passo 4 - Fazer o Download da base de dados de vendas no OneDrive
pyautogui.click(x=2666, y=272)
pyautogui.click(x=2155, y=136)
sleep(5)

#Passo 5 - Importar a base de vendas pro Python
tabela = pd.read_excel(r'C:\Users\Gabriel\Downloads\Vendas - Dez.xlsx')
print(tabela)

#Passo 6 - Calcular o Faturamento e quantidade de produtos vendiso (os indicadores)
faturamento = tabela['Valor Final'].sum()
quantidade_produto = tabela['Quantidade'].sum()

#Passo 7 - abrir o gmail
pyautogui.hotkey('ctrl','t')
pyperclip.copy('https://gmail.com/')
pyautogui.hotkey('ctrl','v')
pyautogui.press('enter')
sleep(5)

#Passo 9 - Fazer login no gmail
pyperclip.copy('gabrielsanz@email.com')
pyautogui.hotkey('ctrl','v')
pyautogui.click(x=3009, y=705)
sleep(4)
pyperclip.copy('123456789!@dzD')
pyautogui.hotkey('ctrl','v')
pyautogui.click(x=2726, y=539)
pyautogui.click(x=3007, y=659)
sleep(4)

#Passo 10 - Clicar no botão de escrever email
pyautogui.click(x=2010, y=170)
sleep(2)

#Passo 11 - Escreve o email de destino
pyperclip.copy('gabrieltestepython@gmail.com')
pyautogui.hotkey('ctrl','v')
pyautogui.hotkey('tab') #seleciona o email
sleep(2)

#Passo 12 - Escreve o Assunto
pyperclip.copy('Relatório de Vendas - Teste')
pyautogui.hotkey('ctrl','v')
pyautogui.hotkey('tab') #muda o campo para a mensagem

#Passo 12 - Escreve o Corpo do email
corpo_email = f'''
Olá Chefia,
O faturamento de ontem das Empresas foram de R$ {faturamento:,.2f}.
A quantidade de produtos vendidos foram de {quantidade_produto:,}.
Att,
Gabriel Sanz
Engenheiro Sanitário e Ambiental
Engenheiro de Segurança do Trabalho
Engenheiro de Software
Celular: (67) 9 xxxx-xxxx
'''
pyperclip.copy(corpo_email)
pyautogui.hotkey('ctrl', 'v')

#Passo 8 - Clicar em Enviar
pyautogui.hotkey('ctrl', 'enter')
