import keyboard
import pyautogui as pag
import time

c = 0

while c < 102 and not keyboard.is_pressed('alt'):
    # Digitar mensagem
    pag.leftClick(x=496, y=986)
    pag.typewrite(f"{c}")
    pag.press('enter')

    # Apagar mensagem
    pag.moveTo(1864, 940)
    pag.moveTo(1862, 901, 0.5)
    pag.leftClick(1862, 901)
    time.sleep(0.3)
    pag.leftClick(1598, 977)
    time.sleep(0.3)
    pag.leftClick(1157, 636)
    time.sleep(0.3)

    c += 1
