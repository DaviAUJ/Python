from random import randint
from time import sleep

cor = {'cle': '\033[m',  # Dicionário de cores
       'neg': '\033[1m',
       'verm': '\033[31m',
       'verd': '\033[32m',
       'ama': '\033[33m',
       }

print(f'{cor["neg"]}', end='')  # Põe o título em negrito e o end='' junta os prints
print(f'-=' * 25 + '-')
print(f'  Bem-vindo ao pedra, papel e tesoura do Python!')
print('-=' * 25 + '-')
print(f'{cor["cle"]}', end='')  # Esse print serve como barreira para o cor['neg']

sleep(1.5)  # tempo entre a mensagem de introdução e seleção da jogada(isso se aplica aos outros)

print('''\nOpções disponíveis
[ 1 ] Pedra
[ 2 ] Papel
[ 3 ] Tesoura''')

player = int(input('\nEscolha qual tipo você vai ser: ')) - 1  # -1 serve para igualar os números do ai e jogador
ai = randint(0, 2)  # a maquina escolhe a jogada dela
jgds = ('Pedra', 'Papel', 'Tesoura')  # seta a "lista" dos itens

sleep(0.35)

print('\nVamos ver se você ganhou...')

sleep(1.5)

print(f'\nO AI escolheu {cor["neg"]}{jgds[ai]}{cor["cle"]} e você {cor["neg"]}{jgds[player]}{cor["cle"]}')
# Informa ao player as escolhas

msgder = 'Você perdeu! Mais sorte na próxima vez!'  # mensagem de derrota padrão
msgvit = 'Lessss gooooo! Você venceu!'  # mensagem de vitória padrão

if player == ai:  # checa se foi empate e relata ao player
    print(f'{cor["ama"]}Parece que foi um empate :/')
elif player == 0 and ai == 1:  # todos os elif's fazem o match up da AI e player
    print(f'{cor["verm"]}{msgder}')  # Substiuí todas as mensagens por variáveis
elif player == 0 and ai == 2:
    print(f'{cor["verd"]}{msgvit}')
elif player == 1 and ai == 2:
    print(f'{cor["verm"]}{msgder}')
elif player == 1 and ai == 0:
    print(f'{cor["verd"]}{msgvit}')
elif player == 2 and ai == 0:
    print(f'{cor["verm"]}{msgder}')
elif player == 2 and ai == 1:
    print(f'{cor["verd"]}{msgvit}')
else:  # Esse else xinga o player por ser burro e querer quebrar o jogo
    print(f'{cor["ama"]}Você é um macaco mesmo não botou as credenciais corretas')
