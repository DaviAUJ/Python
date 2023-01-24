from time import sleep

cor = {'clear': '\033[m',  # Dicionário de cores
       'verm': '\033[31m',
       'ver': '\033[32m',
       'mag': '\033[36m',
       }

num = int(input('\nDigite um número: '))  # pede o número a ser convertido
print('\nEscolha uma base para conversão: ')

sleep(0.25)

print(f'{cor["ver"]}1{cor["clear"]} para {cor["ver"]}binário{cor["clear"]}')  # essas três linhas mostram
print(f'{cor["verm"]}2{cor["clear"]} para {cor["verm"]}octal{cor["clear"]}')  # as opções
print(f'{cor["mag"]}3{cor["clear"]} para {cor["mag"]}hexdecimal{cor["clear"]}')

base = int(input('\ndigite aqui a base: '))  # pede o número correspondente ao método

if base == 1:
    print(f'Seu número {num} em {cor["ver"]}binário{cor["clear"]} é: {cor["ver"]}{bin(num)[2:]}{cor["clear"]}')
elif base == 2:
    print(f'Seu número {num} em {cor["verm"]}octal{cor["clear"]} é: {cor["verm"]}{oct(num)[2:]}{cor["clear"]}')
elif base == 3:
    print(f'Seu número {num} em {cor["mag"]}hexadecimal{cor["clear"]} é: {cor["mag"]}{hex(num)[2:]}{cor["clear"]}')
else:
    print('Você não pôs uma credencial válida')
