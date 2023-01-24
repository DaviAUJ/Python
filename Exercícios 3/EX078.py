nums = list()

print()
for i in range(0, 5):
    nums.append(int(input("Insira um valor aqui: ")))

print(f"""\nO maior valor digitado: {max(nums)}
sua(s) posição(ões):""", end=' ')

for i, j in enumerate(nums):
    if j == max(nums):
        print(i, end='... ' )

print(f"""\n\nO menor valor digitado: {min(nums)}
sua(s) posição(ões):""", end=' ')

for i, j in enumerate(nums):
    if j == min(nums):
        print(i, end='... ')
