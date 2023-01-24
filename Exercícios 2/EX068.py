from random import randint
from time import sleep

contvic = 0

# While usado para pedir ao player se é par ou ímpar e verificar se o input é válido
while True:
    print('\nVamos jogar par ou ímpar!')
    sleep(1)
    print('Escolha qual você quer ser:')
    print('[ 1 ] Par')
    print('[ 2 ] Ímpar')

    esc = int(input('\nQual você escolheu? '))

    if esc == 1:
        print('Você escolheu ser par')
        break
    
    elif esc == 2:
        print('Você escolheu ser ímpar')
        break

    print('\nMACACO DE ANGOLA DIGITE UMA CREDENCIAL CORRETA! >:(')

# Esse while é o par ou ímpar
while True:
    # While usado para decidir a jogada do PC e pedir a do player e verificar se o input é válido
    while True:
        sleep(1)
        rand = randint(1, 10)
        escnum = int(input('\nEscolha um número de 1 a 10: '))

        if escnum in range(1, 11):
            break
            
        else:
             print('Tente de novo! Você não escolheu um número de 1 a 10')

    print('Vamos lá')
    sleep(1)
    print('\nPAR')
    sleep(0.5)
    print('OU')
    sleep(0.5)
    print('ÍMPAR')
    sleep(0.5)

    det = rand + escnum
    print(f'\nVocê escolheu o número {escnum} e o PC escolheu {rand} que juntos somam {det}')

    # verifica quem ganhou e quem perdeu
    if esc == 1:
        if det % 2 == 0:
            print('\nBoaaa, você ganhou!')
            print('Vamos de novo!')
            contvic += 1

        elif det % 2 == 1:
            break

    elif esc == 2:  
        if det % 2 == 1:
            print('\nBoaaa, você ganhou!')
            print('Vamos de novo!')
            contvic += 1
            
        elif det % 2 == 0:
            break

if contvic > 1:
    print(f'\nDessa vez você perdeu, mas ganhou {contvic} vezes')

elif contvic == 1:
    print(f'\nDessa vez você perdeu, mas ganhou 1 vez')

elif contvic == 0:
    print(f'\nVocê perdeu sem ganhar nenhuma vez. Hoje não é seu dia de sorte!')   
    