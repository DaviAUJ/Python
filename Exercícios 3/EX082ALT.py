geral = list()
par = list()
impar = list()

while True:
    geral.append(int(input("\nDigite um valor: ")))

    prog = str(input("Quer continuar[Y/N]? ")).lower()
    
    if prog == 'n':
        break

for num in geral:
    if num % 2 == 0:
        par.append(num)

    else:
        impar.append(num)

print(f"""\nLista geral: {geral}
Lista par: {par}
Lista ímpar: {impar}""")
