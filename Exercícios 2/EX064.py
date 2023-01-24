print('''\n\033[1mSomátoria de Python\033[m
\nAdicione os números para no final soma-los todos 
lembrando que ao digitar 999 o programa fecha''')

num = int(input('\nInsira aqui o número: '))
pool = soma = num = 0

while num != 999:
    soma += num
    pool += 1
    num = int(input('\nInsira aqui o número: '))
print(f'''\nNúmero de valores inseridos: {pool}
Resultado da soma: {soma}''')
