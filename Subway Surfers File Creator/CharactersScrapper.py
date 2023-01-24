from bs4 import BeautifulSoup as bs
import requests

Page = requests.get("https://subwaysurf.fandom.com/wiki/Characters")
PageCode = bs(Page.content, features="html.parser")

Characters = [i.text for i in PageCode.find_all('a')]
Characters = Characters[Characters.index("his dog") + 2:Characters.index("Super Runner Fresh") + 1] # First filter, takes all the unecessary items outside

# Second Filter, takes all the empty items
# And for some reason this list have to pass to the same process three times to have the results that I want
for i in range(0, 3):
    for index, item in enumerate(Characters):
        if item == "":
            Characters.pop(index)

# Third Filter, takes these two wrong names
for item in (("HALLOWEEN", "HOLIDAY")):
    Characters.remove(item)
    