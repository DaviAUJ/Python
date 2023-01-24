soma = 0
cont = 0

for c in range(0, 6):
    num = int(input('Digite um número: '))
    if num % 2 == 0:
        soma += num
        cont += 1
print(f'Você informou {cont} número(s) e a soma foi {soma}')
