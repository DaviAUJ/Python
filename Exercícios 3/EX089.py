geral = list()
temp = list()

while True:
    temp.append(str(input("\nNome: ")))
    geral.append(temp[:])
    temp.clear()

    temp.append(float(input("Nota 1: ")))
    temp.append(float(input("Nota 2: ")))
    geral[-1].append(temp[:])
    temp.clear()

    while True:
        prog = str(input("\nContinuar[Y/N]? ")).lower()[0]
        
        if prog in 'ysn':
            break

        print("\033[31mCredencial inválida\033[m")

    if prog == 'n':
        break

print('\n' + 40 * '=' + '\n')
print("No." + "NOME".rjust(6) + "MÉDIA".rjust(19))
print(30 * '-')
for i, c in enumerate(geral):
    media = (c[1][0] + c[1][1]) / 2
    print(f"{i:<5}{c[0]:<15} {media:^9.1f}")
print(30 * '-')

while True:
    while True:
        prog = int(input("\nMostrar notas de qual aluno(999 interrompe)? "))

        if prog <= (len(geral) - 1):
            break

        print("\033[31m\nCredencial inválida\033[m")

    if prog == 999:
        break

    print(f"As notas de {geral[prog][0]} são: ")
    print(f"\nNota 1: {geral[prog][1][0]}")
    print(f"Nota 2: {geral[prog][1][1]}")

    print('\n' + 30 * '-')

print("\n\033[32mPrograma finalizado\033[m")
