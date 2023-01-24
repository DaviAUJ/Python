def ficha(nome="[NULL]", gols=0):
    print(f"O jogador {nome} marcou {gols} gol(s) ")


namen = str(input("Nome do jogador: "))
tore = str(input("Número de gols: "))

if tore.isnumeric():
    tore = int(tore)
else:
    tore = 0
    
if namen.strip() == '':
    ficha(gols=tore)
else:
    ficha(namen, tore)
