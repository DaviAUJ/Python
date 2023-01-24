nums = list()

while True:
    n = int(input("\nDigite um número: "))

    if n not in nums:
        nums.append(n)
        print("Valor adicionado com sucesso")

    else:
        print("Valor já existe na lista")

    prog = str(input("Quer continuar[Y/N]? ")).lower()

    if prog == 'n':
        break

nums.sort()

print("\nLista dos valores inseridos em ordem crescente: ")
for i in nums:
    print(i, end=' -> ' if i != nums[-1] else '\n')