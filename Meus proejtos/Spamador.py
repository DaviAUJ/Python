import pyautogui, time, random, keyboard 

cont = 0
cores = ['Pinto', 'Bosta', 'Mijo', 'Cu', 'Rola', 'Pinto', 'Rola', 'Cacete', 'Piroca', 'Buceta', 'Caralho', 'Puta', 'Penis', 'Gonorreia', 'Suspeito', 'Jirimum', 'Sucrilhos', 'Guidao',
         'Conspiracionista', 'Chines']

while True:
    tempomsg = float(input('Quanto tempo você quer entre cada mensagem[1 a 60000 ms]: '))
    temposleep = int(input('Quanto tempo até o programa iniciar[sec]: '))

    if tempomsg in range(1, 60001) and temposleep >= 0:
        break

    print('Inválido')

print('O programa vai começar em 5 segundos')

print("começando em: ")
for x in range(temposleep, 0, -1):
    print(x)
    time.sleep(1)
print("começou!")

while not keyboard.is_pressed('alt'):
    esccor = random.choice(cores)
    pyautogui.typewrite("Melk" + esccor)
    pyautogui.press("enter")
    time.sleep(tempomsg / 1000)
    cont += 1
    print(f"Total de mensagens enviadas: {cont}")
