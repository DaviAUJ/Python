import pyautogui as pag
from time import sleep

com = ['m', 'ha', 'wa', 'dk', 'daily', 'rolls']

print('''\nEscolha um desses:
[ 1 ] para $m
[ 2 ] para $ha
[ 3 ] para $wa''')

escolha = int(input('\nQual você escolheu? ')) - 1
exe = str(input('Executar os comandos diários?(Y/N) '))
rolls = str(input('Executar $rolls?(Y/N) '))
print('\nO programa agora iniciará em 10 segundos')

sleep(10)

if exe in 'Yy':
    for x in range(0, 2):
        pag.typewrite(f'${com[x + 3]}')
        pag.press('enter')
        sleep(1)

for x in range(0, 19):
    pag.typewrite('$' + com[escolha])
    pag.press('enter')
    sleep(1)

if rolls in 'Yy':
    pag.typewrite(f'${com[5]}')
    pag.press('enter')
    sleep(1)

    for x in range(0, 19):
        pag.typewrite('$' + com[escolha])
        pag.press('enter')
        sleep(1)

pag.typewrite('.')
pag.press('enter')
