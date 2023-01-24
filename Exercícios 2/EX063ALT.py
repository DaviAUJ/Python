n = int(input('\nQuantos termos você quer ver? '))

pool = 3
t0 = 0
t1 = 1

print(f'{t0} -> {t1}', end=' -> ')

while pool <= n:
    t2 = t1 + t0
    print(f'{t2}', end=' -> ')

    pool += 1
    t0 = t1
    t1 = t2
print('FIM')
