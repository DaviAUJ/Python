valor = float(input('\nQuanto vale o seu produto: R$'))

print('''\nEscolha o método de pagamento: 
[ 1 ] á vista no dinheiro: 10% de desconto
[ 2 ] á vista no cartão: 5% de desconto
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão: 20% de juros''')

meto = int(input('\nQual método você escolheu? '))

print(f'\nO valor do produto é de R${valor}')
if meto == 1:
    print(f'O valor final será R${valor * 0.9:.2f}')
elif meto == 2:
    print(f'O valor final será R${valor * 0.95:.2f}')
elif meto == 3:
    print(f'O valor final será R${valor}')
    print(f'As parcelas serão de R${valor / 2:.2f}')  # informa o valor das parcelas
elif meto == 4:
    print(f'O valor final será R${valor * 1.2:.2f}')  # informa o valor total com os juros

    numpar = int(input('\nQual é o número de parcelas? '))  # pede o número de parcelas

    print(f'As parcelas serão de R${(valor * 1.2) / numpar:.2f}')  # calcula o valor das parcelas conforme os juros
else:
    print(f'\n\033[31mCredencial inválida')
