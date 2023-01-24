nums = list()

while True:
    nums.append(int(input("\nDigite um valor: ")))

    if nums[-1] in nums[:(len(nums) - 1)]:
        nums.pop()
        print("O valor adicionado já existe na lista")

    else:
        print("O valor foi adicionado com sucesso!")

    prog = str(input("Quer continuar[Y/N]: ")).lower()

    if prog in "n":
        break

nums.sort()

print("\nLista dos valores inseridos em ordem crescente: ")
for i in nums:
    print(i, end=' -> ' if i != nums[-1] else '\n')
