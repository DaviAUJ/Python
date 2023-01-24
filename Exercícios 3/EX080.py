nums = list()

for i in range(0, 5):
    ins = int(input("\nDigite um valor: "))
    if i == 0 or max(nums) < ins:
        nums.append(ins)
        print("O valor foi inserido na última posição")

    else:
        for pos in range(0, i):
            if nums[pos] >= ins:
                nums.insert(pos, ins)
                print(f"O valor foi inserido na posição {pos}")
                break

print("\nOs valores inseridos em ordem crescente foram:")
for i in nums:
    print(i, end=' -> ' if i != nums[-1] else '')
