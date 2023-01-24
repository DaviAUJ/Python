from time import sleep
from random import randint

print('\033[1m', end='')
print('\033[30m-\033[31m=' * 21)
print('         Grupo \033[30mdo \033[31mZap \033[30mdo \033[31mFlamengo')
print('\033[31m-\033[30m=' * 21)
print('\033[m', end='')

msg = str(input('\nDigite uma mensagem para o grupo do flamengo e seus participantes: ')).lower().strip()

if 'bom dia' in msg or 'boa tarde' in msg or 'boa noite' in msg:

    num = randint(0, 9999)
    num1 = randint(0, 9999)

    sleep(1)
    print(f'\033[1m21 9{num:04d}-{num1:04d} está gravando áudio...')  # esse "04d" dentro do {} serve para botar numero
    print('\033[m', end='')                                           # em milhar mesmo q ele seja menor que mil
    sleep(3.2)

    print('\nMermão bom dia é o caralho parcero, isso aqui é o grupo da torcida jovem, entendeu? Tu quer dar bom dia ')
    print('tu cria um grupo de viado, de GLS, e fica "bom dia", "boa tarde", "boa noite", ou então tu cria um grupo')
    print('pra tua família, aí tu fica dando bom dia.')
    print('Aqui é psicopata, ladrão, bandido, cheirador, vendedor de droga, polícia maluco, polícia assaltante, aqui')
    print('tem a porra toda mermão, isso aqui é a Torcida Jovem do Flamengo! Bom dia é o caralho, rapá! Toma no cu!!!')
else:
    print('\n*ninguém responde*')
