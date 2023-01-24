from random import choice

numque = int(input('\nQuantas questões tem a atividade? '))

opc = ['A', 'B', 'C', 'D', 'E']

print('\nChuta aí essas alternativas: ')
for x in range(0, numque):
    print(f'\n{x + 1}) Alternativa {choice(opc)}')
