pool = soma = 0

while True:
    num = int(input('Digite um número(999 para parar): '))
    
    if num == 999:
        break

    pool += 1
    soma += num
print(f'A soma de todos os {pool} valores inseridos foi: {soma}')
