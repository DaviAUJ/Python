print('\nQuais são os números pares entre...')
ini = int(input('esse número: '))
fin = int(input('e esse número: '))

if ini % 2 == 1:
    ini += 1
    print(f'\nOs número pares entre {ini - 1} e {fin} são:')
else:
    print(f'\nOs número pares entre {ini} e {fin} são:')
for c in range(ini, (fin + 1), 2):
    print(c, end=' ')
