ti = int(input('\nDigite a o termo inicial da P.A.: '))
raz = int(input('Digite a razão da P.A.: '))

pool = 0
mais = 10
contagem = 0

while mais != 0:
    while pool != mais:
        print(ti, end=' -> ')

        pool += 1
        ti += raz
    print('PAUSA')
    mais = int(input('\n\nQuantos termos quer mostrar a mais: '))
    contagem += pool
    pool = 0
print(f'\nO programa terminou com {contagem} termos')
