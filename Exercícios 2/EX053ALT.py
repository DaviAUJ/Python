frase = str(input('Digite uma frase: ')).strip().lower().replace(' ', '')
inverso = ''

for letra in range(len(frase) - 1, -1, -1):
    inverso += frase[letra]

print(f'O inverso de {frase} é {inverso}')
if inverso == frase:
    print('Temos um palindromo')
else:
    print('A frase digitada não é um palindromo')
