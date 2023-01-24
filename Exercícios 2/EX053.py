palin = str(input('\nDigite uma frase para ver se é um palindromo: '))

palin = palin.replace(' ', '').replace(',', '').strip().strip('.').strip('!').strip('?').lower()

if palin == palin[::-1]:
    print('É palindromo')
else:
    print('Não é palindromo')
