nums = [[], []]
msg = ("Números pares:", "Números ímpares:")

for i in range(0, 7):
    ins = int(input("Valor: "))
    
    if ins % 2 == 0:
        nums[0].append(ins)

    else:
        nums[1].append(ins)

nums[0].sort()
nums[1].sort()

for i in range(0, 2):
    print(msg[i], end=' ')
    for c in nums[i]:
        print(c, end=' -> ' if c != nums[i][-1] else '\n')
