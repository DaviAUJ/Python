from time import sleep
from random import randint

jogo = list()
temp = list()
njog = int(input("Número de jogos a serem sorteados: "))

print(5 * '-=' + '-' + f"Sorteando {njog} jogos".center(20) + 6 * '-=' + '-')
for i in range(0, njog):
    for c in range(0, 6):
        while True:
            rand = randint(1, 60)
            if rand not in temp:
                break

        temp.append(rand)

    temp.sort()
    jogo.append(temp[:])
    temp.clear()

    print(f"Jogo {i + 1}: {jogo[i]}")
    sleep(0)
print(5 * '-=' + '-' + f"BOA SORTE!".center(20) + 5 * '-=' + '-')
