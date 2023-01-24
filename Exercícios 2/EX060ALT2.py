num = int(input('\nDigite um número para a sua fatorial ser calculada: '))
fator = 1

print(f'\n{num}! = ', end='')
for x in range(num, 0, -1):
    fator *= x

    print(x, end='')
    print(' x ' if x > 1 else ' = ', end='')

print(fator)
