n = int(input('\nDigite um número: '))
nummul = int(input('Digite outro número: '))

print(f'\nA Tabuada de {n} é:')
for c in range(0, (nummul + 1)):
    print(f'{n} x {c} = {n * c}')
