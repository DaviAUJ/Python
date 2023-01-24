num = int(input('\nInsira um número de 0 a 9999: '))

u = num % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10

print(f'\nmilhar: {u}')
print(f'centena: {d}')
print(f'dezena: {c}')
print(f'unidade: {m}')
