geral = list()
par = list()
impar = list()

while True:
    geral.append(int(input("\nDigite um valor: ")))

    prog = str(input("Quer continuar[Y/N]? "))

    if prog == 'n':
        break
    
for i in range(0, len(geral)):
    if geral[i] % 2 == 0:
        par.append(geral[i])

    else:
        impar.append(geral[i])

print(f"""\nLista geral: {geral}
Lista par: {par}
Lista ímpar: {impar}""")
