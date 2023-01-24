from bs4 import BeautifulSoup as bs
import CharactersScrapper as cs
import requests

Page = requests.get("https://subwaysurf.fandom.com/wiki/Outfits")
PageCode = bs(Page.content, features = "html.parser")

Outfits = [i.text for i in PageCode.find_all('th')]

print(Outfits)