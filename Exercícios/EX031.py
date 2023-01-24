kmvia = int(input('\nPor quantos quilômetros você viajou? '))

if kmvia <= 200:
    print(f'Você deverá pagar R${kmvia * 0.5:.2f}')
else:
    print(f'Você deverá pagar R${kmvia * 0.45:.2f}')
