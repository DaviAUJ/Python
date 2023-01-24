import string, keyboard, random
import pyperclip as pyc

def gerarlink():
    sublink = str()
    for c in range(0, 6):
        sublink += random.choice(string.digits + string.ascii_lowercase)
            
    link = f"https://prnt.sc/{sublink}"
    
    return link

pyc.copy(gerarlink())

while True:
    keyboard.wait('ctrl+v')
    pyc.copy(gerarlink())
 