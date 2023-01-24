mtz = [[], [], []]
sumpar = sum3c = 0
 
for i in range(0, 3):
    for c in range(0, 3):
        ins = int(input(f"Valor para [{i}, {c}]: "))
        mtz[i].append(ins)

        if ins % 2 == 0:
            sumpar += ins

for i in mtz:
    sum3c += i[2]

print()  # Print para formatação
for i in range(0, 3):
    print(f"[{mtz[i][0]:^5}][{mtz[i][1]:^5}][{mtz[i][2]:^5}]")

print(f"""\nSoma de todos os valores pares: {sumpar}
Soma dos valores da terceira coluna: {sum3c}
Maior valor da segunda linha: {max(mtz[1])}""")
