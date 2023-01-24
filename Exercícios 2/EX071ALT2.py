print('\033[1m' + '-' * 30)
print('Banco do Pigas'.center(30, ' '))
print('-' * 30 + '\033[m')

valor = int(input('\nQuantos reais você quer sacar? R$'))
n50 = n20 = n10 = 0

n50 = valor // 50
valor -= n50 * 50
n20 = valor // 20
valor -= n20 * 20
n10 = valor // 10
valor -= n10 * 10

if n50 > 0:
    print(f'Você sacou {n50} nota(s) de R$50')

if n20 > 0:
    print(f'Você sacou {n20} nota(s) de R$20')

if n10 > 0:
    print(f'Você sacou {n10} nota(s) de R$10')

if valor > 0:
    print(f'Você sacou {valor} nota(s) de R$1')
