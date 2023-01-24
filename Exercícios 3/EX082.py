geral = list()
par = list()
impar = list()

while True:
    ins = int(input("\nDigite um valor: "))

    geral.append(ins)

    if ins % 2 == 0:
        par.append(ins)

    else:
        impar.append(ins)

    prog = str(input("Quer continuar[Y/N]? ")).lower()

    if prog == 'n':
        break

print(f"""\nLista geral: {geral}
Lista par: {par}
Lista ímpares: {impar}""")
