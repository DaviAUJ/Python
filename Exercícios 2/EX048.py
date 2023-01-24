ini = int(input('\nNúmero inicial: '))
fin = int(input('Número final: '))
pool = 0
cont = 0

if ini % 2 == 0:
    ini += 1

for c in range(ini, (fin + 1), 2):
    if c % 3 == 0:
        pool += c
        cont += 1
print(f'\nA soma de {cont} valor(es) entre {ini} e {fin} é: {pool}')
