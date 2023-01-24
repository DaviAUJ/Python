r1 = float(input('\nQual é o tamanho da reta a? '))
r2 = float(input('Qual é o tamanho da reta b? '))
r3 = float(input('Qual é o tamanho da reta c? '))

if r1 + r2 > r3 and r2 + r3 > r1 and r1 + r3 > r2:
    print('\nÉ possivel criar o triangulo')
    print('Aliás, seu triangulo é', end=' ')
    if r1 == r2 == r3:
        print('equilatero')
    elif r1 != r2 != r3 != r1:
        print('escaleno')
    else:
        print('isósceles')
else:
    print('\nNão é possivel formar um triangulo')
