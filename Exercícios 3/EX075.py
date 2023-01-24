nums = (int(input("\nDigite um número de 0 a 10: ")),
        int(input("Digite mais um número de 0 a 10: ")),
        int(input("Digite mais um número de 0 a 10: ")),
        int(input("Digite mais um número de 0 a 10: ")))

print("\nLista dos números inseridos: ", end='')
for i in range(0, len(nums)):
    print(nums[i], end='' if i == 3 else ', ')

print(f"\n\nO número 9 apareceu {nums.count(9)} vez(es)")

if 3 in nums:
    print(f"O número 3 aparece pela primeira vez na {nums.index(3) + 1}ª posição")

else:
    print("O número 3 não existe na tupla")

print("Os números pares foram:")
for i in nums:
    if i % 2 == 0:
       print(f"- {i}")
