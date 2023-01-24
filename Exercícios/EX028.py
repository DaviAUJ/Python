from random import randint
from time import sleep

print('\nBem-vindo ao jogo de adivinhação! \nAdivinhe o número que a máquina escolheu')

numale = randint(1, 5)

sleep(1.5)
print('\nO número entre 1 e 5 foi sorteado')
numchute = int(input('Sua aposta: '))

print('\nVamos ver se você ganhou...')
sleep(2)

if numale == numchute:
    print('\nParabéns seu sortudo! Você acertou!')
else:
    print(f'\nDessa vez não foi! :(\nAliás, o número sorteado foi: {numale}')
