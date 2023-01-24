while True:
    num = int(input('\nDigite um número(número negativo para parar): '))

    if num < 0:
        break

    print('-' * 20)
    print(f'A tabuada de {num} é:')
    for x in range(1, 11):
        print(f'{num} x {x:>2} = {num * x}')
    print('-' * 20)

print('\nPrograma encerrado. Volte sempre!')        
