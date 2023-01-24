print('-=' * 10 + '-')
print('    Gerador de PA')
print('-=' * 10 + '-')

ti = int(input('\nDigite a o termo inicial da P.A.: '))
raz = int(input('Digite a razão da P.A.: '))
pool = 0

while pool != 10:
    print(ti, end=' -> ')

    pool += 1
    ti += raz
print('FIM')
