'''Desafio:
O programa de fidelidade de uma determinada livraria premia seus clientes de acordo com o número de livros comprados a cada semestre.
Os pontos são atribuídos da seguinte forma:
•Se um cliente comprar 0 livros, ele ganhará 0 pontos.
•Se um cliente comprar 1 livro, ele ganhará 5 pontos.
•Se um cliente comprar 2 livros, ele ganhará 15 pontos.
•Se um cliente comprar 3 livros, ele ganhará 30 pontos.
•Se um cliente comprar 4 ou mais livros, ele ganhará 60 pontos.
Lista de brindes:
De 20 à 30 pontos o cliente poderá escolher entre: Uma Eco Bag OU Caneta personalizada
De 35-60 pontos o cliente poderá escolher entre: Um livro (com valor máximo de R$30,00) OU Luminária de cabeceira.
Acima de 65 o cliente poderá escolher entre: 2 livros (com valor máximo de R$100,00) OU Powerbank
Obs: Os pontos são acumulativos, e contado a cada compra realizada pelo cliente.
Ex: Se o cliente na semana 1 comprar 2 livros de uma única vez ele receberá 15 pontos, se na semana 2 ele comprar 1 único livro receberá 5 pontos totalizando 20 pontos em duas semanas.
Crie um programa que leia o número de livros comprado por um usuário e exiba o número de pontos correspondentes e qual brinde ele poderá escolher.'''

cont = 1
total = 0
while cont <= 6:
    bimestre = int(input("Digite o bimestre da compra: "))
    livros = int(input("Digite a quantidade de livros comprados no %d º bimestre: " % bimestre))
    cont = cont+1
    if (livros == 0):
        total = total+0
    elif (livros == 1):
        total = total+5
    elif (livros == 2):
        total = total+15
    elif (livros == 3):
        total = total+30
    elif (livros >= 4):
        total = total+60

print("<<<< Você possuí %d pontos. >>>>" % total)
if (total >= 20):
    brinde = int(input(
        " 1 - Você pode escolher uma Ecobag por 20 pontos.\n 2 - Caneta Personalizada por 30 pontos.\n 3 - Um livro (com valor máximo de R$ 30,00) por 35 pontos.\n 4 - Uma Luminária de cabeceira por 60 pontos.\n 5 - 2 livros (com valor máximo de R$100,00) por 150 pontos.\n 6 - Powerbank por 120 pontos.\n 7 - Digite para sair.\n"))
    if (brinde == 1 and total >= 20):
        print(
            "Parabéns você adquiriu uma Ecobag e poderá retirar diretamente na livraria. Seu saldo atual é de: %d pontos. " % (
                        total-20))
    if (brinde == 2 and total >= 30):
        print(
            "Parabéns você adquiriu uma Caneta Personalizada e poderá retirar diretamente na livraria. Seu saldo atual é de: %d pontos. " % (
                        total-30))
    if (brinde == 3 and total >= 35):
        print(
            "Parabéns você adquiriu um livro (com valor máximo de R$ 30,00) e poderá retirar diretamente na livraria. Seu saldo atual é de: %d pontos. " % (
                        total-35))
    if (brinde == 4 and total >= 60):
        print(
            "Parabéns você adquiriu uma Luminária de Cabeceira e poderá retirar diretamente na livraria. Seu saldo atual é de: %d pontos. " % (
                        total-60))
    if (brinde == 5 and total >= 150):
        print(
            "Parabéns você adquiriu 2 livros (com valor máximo de R$100,00) e poderá retirar diretamente na livraria. Seu saldo atual é de: %d pontos. " % (
                        total-150))
    if (brinde == 6 and total >= 120):
        print(
            "Parabéns você adquiriu um Powerbank e poderá retirar diretamente na livraria. Seu saldo atual é de: %d pontos. " % (
                        total-120))
    if (brinde == 7):
        print("Até Logo!!")
    if (brinde == 2 and total <= 30):
        print("Você não possui pontos para adquirir uma Caneta Personalizada")
    if (brinde == 3 and total <= 35):
        print("Você não possui pontos para adquirir o livro (com valor máximo de R$ 30,00).")
    if (brinde == 4 and total <= 60):
        print("Você não possui pontos para adquirir a Luminária de Cabeceira.")
    if (brinde == 5 and total <= 150):
        print("Você não possui pontos suficientes para adquirir os 2 livros (com valor máximo de R$100,00).")
    if (brinde == 6 and total <= 120):
        print("Você não possui pontos suficientes para adquirir o Powerbank.")
else:
    print("Você não possui pontos suficientes.")
