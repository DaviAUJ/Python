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

print('''\nprecauções antes de usar:
Certifique-se que a primeira aba do google não é nada importante e pode ser fechado
Ou certifique-se que o google chrome está fechado''')

escolha = str(input('\nPra qual professor você quer enviar a atividade? ')).lower()
dia = str(input('Dia em que a atividade foi requisitada: '))
mes = str(input('Mês em que a atividade foi requisitada: '))
posprof = listprof.index(escolha)

confobs = str(input('Adicionar observação?(Y/N) '))
if confobs in 'Yy':
    obs = str(input('Escreva sua observação: '))

# agora a automação vai começar

print('\nA automação vai começar em 3 segundos')
sleep(3)

gui.click(x=467, y=1060)  # clica no icone do google chrome
sleep(2)
gui.click(x=20, y=12)  # clica na primeira aba aberta do google
sleep(0.5)
gui.click(x=245, y=84)  # clica no shortcut do email
sleep(5)
gui.click(x=74, y=207)  # clica no botão "escrever"
sleep(0.5)
gui.click(x=1382, y=500)  # clica na caixa onde se escreve o endereço de email
gui.typewrite(listemail[posprof], interval=0.05)  # escreve o email do professor escolhido
sleep(0.5)
gui.click(x=1288, y=526)  # clica na caixa do assunto
gui.typewrite('Entrega de atividade', interval=0.05)
sleep(0.5)
gui.click(x=1339, y=690)  # clica na caixa de texto do email
copy('Davi Araújo do Nascimento - 2° Ano B')
gui.hotkey('ctrl', 'v')  # essa macacada só acontece pq o pyatuogui nn reconhece acento
sleep(0.5)
gui.press(['enter', 'enter'])  # formatação do texto
sleep(0.2)
gui.typewrite(f'Atividade requisitada no dia: {dia}/{mes}', interval=0.05)
sleep(0.5)
gui.press(['enter', 'enter'])  # formatação do texto
sleep(0.2)
gui.typewrite('Segue em anexo um arquivo do bloco de notas com as minhas respostas da atividade', interval=0.05)
sleep(0.5)

if confobs in 'Yy':
    gui.press(['enter', 'enter'])
    sleep(0.5)
    copy(obs)
    sleep(0.5)
    gui.hotkey('ctrl', 'v')
    sleep(1)

gui.click(x=1428, y=1006)  # clica no botão de anexar
sleep(1.5)
gui.click(x=376, y=443, clicks=2)  # abre o arquivo
sleep(3)
gui.hotkey('Ctrl', 'enter')  # hotkey de enviar email
