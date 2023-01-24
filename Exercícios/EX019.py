from random import choice

alu1 = str(input('\n\033[33mNome do primeiro aluno: '))
alu2 = str(input('\033[34mNome do segundo aluno: '))
alu3 = str(input('\033[35mNome do terceiro aluno: '))
alu4 = str(input('\033[36mNome do quarto aluno: '))
print('\033[m', end='')

lista = choice([alu1, alu2, alu3, alu4])
msgpadrao = '\nO aluno escolhido para apagar o quadro será'

if lista == alu1:
    print(f'{msgpadrao} \033[1;33m{lista}')
elif lista == alu2:
    print(f'{msgpadrao} \033[1;34m{lista}')
elif lista == alu3:
    print(f'{msgpadrao} \033[1;35m{lista}')
else:
    print(f'{msgpadrao} \033[1;36m{lista}')
