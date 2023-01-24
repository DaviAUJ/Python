dado = list()
temp = list()
mpes = mlev = 0

while True:
    temp.append(str(input("\nNome: ")))
    temp.append(float(input("Peso: ")))

    if len(dado) == 0:
        mpes = mlev = temp[1]

    else:
        if temp[1] > mpes:
            mpes = temp[1]

        elif temp[1] < mlev:
            mlev = temp[1]

    dado.append(temp[:])
    temp.clear()

    while True:
        prog = str(input("Quer continuar[Y/N]? ")).lower()[0]

        if prog in 'syn':
            break

        else:
            print("\n\033[31mCredencial inválida\033[m")

    if prog == 'n':
        break

print(f"\nNúmero de pessoas cadastradas: {len(dado)}")
if mpes == mlev:
    print(f"Todos possuem o mesmo peso de {mpes}kg. São eles:", end=' ')
    for i in dado:
        print(i[0], end='... ')
        
else:
    print(f"Os mais pesados possuem: {mpes}kg. São eles:", end=' ')
    for i in dado:
        if i[1] == mpes:
            print(i[0], end='... ') 
            
    print(f"\nOs mais leves possuem: {mlev}kg. São eles:", end=' ')
    for i in dado:
        if i[1] == mlev:
            print(i[0], end='... ')
