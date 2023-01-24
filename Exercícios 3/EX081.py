nums = list()

while True:
    nums.append(int(input("\nInsira um valor: ")))

    prog = str(input("Quer continuar[Y/N]? ")).lower()

    if prog in 'n':
        break

numsort = sorted(nums, reverse=True)

print(f"\nNúmero de valores inseridos: {len(nums)}")

print("\nNúmeros listados em ordem decrescente:", end=' ')
for i, c in enumerate(numsort):
    print(c, end=' -> ' if i != (len(nums) - 1) else '\n')
 
if 5 in nums:
    print("\nO valor 5 está presente na lista")
    print("Ele aparece nessas posições:", end=' ')
    for i, c in enumerate(nums):
        if c == 5:
            print(i, end='... ')

else:
    print("\nO valor 5 não está presente na lista")
