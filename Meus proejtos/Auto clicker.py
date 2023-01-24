import pyautogui as gui
from time import sleep
import keyboard as kb

sleep(3)

while not kb.is_pressed('alt'):
    gui.typewrite('VAII DJ')
    gui.press('enter')
    
