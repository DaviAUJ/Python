nums = [[], []]

for i in range(0, 7):
    ins = int(input("Valor: "))
    
    if ins % 2 == 0:
        nums[0].append(ins)

    else:
        nums[1].append(ins)

nums[0].sort()
nums[1].sort()

print("Números pares:", end=' ')
for i in nums[0]:
    print(i, end=' -> ' if i != nums[0][-1] else '\n')

print("Números ímpares", end=' ')
for i in nums[1]:
    print(i, end=' -> ' if i != nums[1][-1] else '\n')
