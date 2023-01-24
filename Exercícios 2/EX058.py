from random import randint
from time import sleep

pool = 1

print('Bem-vindo ao jogo de adivinhação do Python!!')
sleep(0.5)

print('\nUm número entre 0 e 10 está sendo sorteado...')
sleep(2)
numale = randint(0, 10)
print('O número foi sorteado!')

chute = int(input('\ntente chutar qual é o número: '))
sleep(0.75)

while chute != numale:
    pool += 1

    if chute < numale:
        print('\nMaior...')

    elif chute > numale:
        print('\nMenor...')
    print('Putz! Número errado! :(')
    chute = int(input('Tente chutar novamente: '))
    sleep(0.75)

print('\nO jogo acabou!')
if pool == 1:
    print('Uau!!1! Você acertou de primeira! Parabéns!')
else:
    print('Parabéns! Você conseguiu acertar o número aleatório!')
    print(f'Foram necessários {pool} chutes para você vencer.')
