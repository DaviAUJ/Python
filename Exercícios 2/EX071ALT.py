print('\033[1m' + '-' * 30)
print('Banco do Pigas'.center(30, ' '))
print('-' * 30 + '\033[m')

while True:
    valor = int(input('\nQual o valor a ser sacado[R$500 a R$1500]? R$'))

    if valor in range(500, 1501):
        break

n50 = n20 = n10 = n1 = 0

while valor >= 50:
    valor -= 50
    n50 += 1

while valor >= 20:
    valor -= 20
    n20 += 1

while valor >= 10:
    valor -= 10
    n10 += 1

while valor >= 1:
    valor -= 1
    n1 += 1

print(f'''Você sacou {n50:>2} nota(s) de R$50
Você sacou {n20:>2} nota(s) de R$20
Você sacou {n10:>2} nota(s) de R$10
Você sacou {n1:>2} nota(s) de R$1''')
