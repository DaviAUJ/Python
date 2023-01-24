num = int(input('\nDigite um número para saber sua fatorial: '))

if num > 1:
    cont = num
    fator = 1

    print(f'{num}! = ', end='')
    while cont > 0:
        print(cont, end='')
        print(' x ' if cont > 1 else ' = ', end='')

        fator *= cont
        cont -= 1
    print(fator)

elif num == 1:
    print(f'A fatorial de {num} é igual a {num}')

else:
    print('\nA fatorial não existe')
