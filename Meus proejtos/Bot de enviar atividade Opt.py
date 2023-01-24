import pyautogui as gui
from time import sleep
from pyperclip import copy

listprof = ['teste', 'herculis', 'iltemberg', 'joselma', 'deniel', 'suellen', 'hilario', 'elton', 'erica',
            'cida', 'rodrigo', 'neyllan', 'emanoell', 'joao', 'rosana', 'ana']
listemail = ['im.a.powerless.lord@gmail.com', 'profhr2021@gmail.com', 'prof.iltemberg.2b@gmail.com',
             'joselmabiologia2021@gmail.com', 'atividadesprofdeniel@gmail.com', 'literaturafreitas@hotmail.com',
             'hilariomontessori@gmail.com', 'eltondoria.montessori@gmail.com',
             'ericabiomontessori@gmail.com', 'Cida.1sara@hotmail.com', 'professor.georodrigo@gmail.com',
             'neyllan45@outlook.com', 'sandesemanoell@yahoo.com.br', 'atividadesprojoao@gmail.com',
             'rosanabmedeiros27@hotmail.com', 'institucionalsegundoano@gmail.com']

listx = [467, 20, 245, 74, 1382, 1288, 1339, 1428, 376]
listy = [1060, 12, 84, 207, 500, 526, 690, 1006, 443]
listsleep = [2, 0.5, 5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 1, 1.5]

print('''\nprecauções antes de usar:
Certifique-se que a primeira aba do google não é nada importante e pode ser fechado
Ou certifique-se que o google chrome está fechado''')

escolha = str(input('\nPra qual professor você quer enviar a atividade? ')).lower()
dia = str(input('Dia em que a atividade foi requisitada: '))
mes = str(input('Mês em que a atividade foi requisitada: '))
posprof = listprof.index(escolha)

listfrases = [listemail[posprof], 'Entrega de atividade', 'Davi Araújo do Nascimento - 2° Ano B',
              f'Atividade requisitada no dia: {dia}/{mes}',
              'Segue em anexo um arquivo do bloco de notas com as minhas respostas da atividade']

confobs = str(input('Adicionar observação?(Y/N) '))
if confobs in 'Yy':
    obs = str(input('Escreva sua observação: '))

# agora a automação vai começar

print('\nA automação vai começar em 3 segundos')
sleep(3)

for c in range(0, 11):
    if c < 7:
        gui.click(x=listx[c], y=listy[c])
    if c == 4:
        gui.typewrite(listemail[posprof], interval=0.05)  # escreve o email do professor escolhido
    if c == 5:
        gui.typewrite('Entrega de atividade', interval=0.05)
    if c == 6:
        copy(listfrases[2])
        gui.hotkey('ctrl', 'v')  # essa macacada só acontece pq o pyatuogui nn reconhece acento
    if 6 < c < 9:
        gui.press(['enter', 'enter'])  # formatação do texto
        sleep(0.2)
        gui.typewrite(listfrases[c - 4], interval=0.05)
    if c == 9:
        if confobs in 'Yy':
            gui.press(['enter', 'enter'])
            sleep(0.5)
            copy(obs)
            sleep(0.5)
            gui.hotkey('ctrl', 'v')
    if c == 10:
        gui.click(x=listx[c - 3], y=listy[c - 3])
    sleep(listsleep[c])

gui.click(x=listx[8], y=listy[8], clicks=2)
sleep(3)
gui.hotkey('Ctrl', 'enter')  # hotkey de enviar email
