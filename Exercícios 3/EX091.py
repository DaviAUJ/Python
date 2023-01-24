from random import randint
from time import sleep
from operator import itemgetter

jogo = dict()
ranking = dict()

for c in range(1, 5):
    jogo[f'jogador {c}'] = randint(1, 6)

for k, v in jogo.items():
    print(f"{k} tirou o valor {v} no dado")
    sleep(0.5)

ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)

print("Ranking dos jogadores: ") 
for i, v in enumerate(ranking):
    print(f"{i + 1}º lugar: {v[0]} com {v[1]} pontos")
    sleep(0.5)