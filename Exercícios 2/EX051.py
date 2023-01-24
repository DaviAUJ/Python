pt = int(input('\nDigite a o termo inicial da P.A.: '))
raz = int(input('Digite a razão da P.A.: '))

for c in range(0, 10):
    print(pt, end=' -> ')
    pt += raz
print('ACABOU')
