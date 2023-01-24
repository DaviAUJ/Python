from bs4 import BeautifulSoup as bs
import string, keyboard, random, requests
import pyperclip as pyc

def gerarlink():
    ValidCharacters = string.digits + string.ascii_lowercase + string.ascii_uppercase + "-_"
    
    sublink = str()
    for c in range(0, 11):
        sublink += random.choice(ValidCharacters)
            
    link = f"https://www.youtube.com/watch?v={sublink}"
    print("Link Gerado")
    
    Page = requests.get(link)
    PageCode = bs(Page.content, features="html.parser")
    ProofText = PageCode.find_all("div")
    print(ProofText)
    
    return link

pyc.copy(gerarlink())

while True:
    keyboard.wait('ctrl+v')
    pyc.copy(gerarlink())
 