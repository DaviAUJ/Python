num = int(input('\nDigite um número para saber sua fatorial: '))

if num > 1:
    outro = num - 1
    fatorial = num * outro

    while outro != 1:
        outro -= 1
        fatorial *= outro

    print(f'A fatorial de {num}! = ', end='')
    for x in range(num, 0, -1):
        print(f'{x}', end='')
        print(' x ' if x > 1 else ' = ', end='')
    print(fatorial)

elif num == 1:
    print(f'A fatorial de {num} é igual a {num}')

else:
    print('\nA fatorial não existe')
