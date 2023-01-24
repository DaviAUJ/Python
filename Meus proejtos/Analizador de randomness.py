txt = open('vairos impostores.txt', 'r')
words = txt.read().split()
listnum = []
listpro = []
totcores = len(words) - words.count('Impostor')
media = 0

cores = ['Vermelho', 'Rosa', 'Ciano', 'Azul', 'Laranja',
         'Roxo', 'Lima', 'Verde', 'Amarelo', 'Branco',
         'Marrom', 'Preto']

for cor in cores:
    listnum.append(words.count(cor))

for x in range(0, 12):
    listpro.append((listnum[x] / totcores) * 100)
    print('\n', cores[x], f'teve {listpro[x]:.5f}% de chance de aparecer')
    media += listpro[x]

print(f'\n Ou seja com uma média de: {media / 12}% cada')
