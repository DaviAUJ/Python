from random import shuffle

cor = {'verm': '\033[31m',
       'verd': '\033[32m',
       'rox': '\033[35m',
       'cia': '\033[36m',
       'bold': '\033[1m',
       'clear': '\033[m'}

alu0 = str(input(f'\n{cor["verm"]}Nome do primeiro aluno: '))
alu1 = str(input(f'{cor["verd"]}Nome do segundo aluno: '))
alu2 = str(input(f'{cor["rox"]}Nome do terceiro aluno: '))
alu3 = (str(input(f'{cor["cia"]}Nome do quarto aluno: ')))
print(f'{cor["clear"]}', end='')

deck = [alu0, alu1, alu2, alu3]  # faz a lista
shuffle(deck)  # embaralha a lista e não pode estar dentro do f{}

print(f'\nA ordem da apresentação do trabalho será a seguinte: {deck}')
