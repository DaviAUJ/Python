num = int(input('\nDigite um número para saber se ele é primo: '))
soma = 0

print('')  # formatação
for c in range(1, (num + 1)):
    if num % c == 0:
        print('\033[32m', end='')
        soma += 1
    else:
        print('\033[31m', end='')
    print(f'{c}', '\033[m', end=' ')

print(f'\n\nO número {num} foi divido {soma} vezes')
if soma == 2:
    print('E por isso ele é primo')
else:
    print('E por isso ele não é primo')
