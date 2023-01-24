print('\033[1;35m', end='')
print('=' * 50)
print('    Descubra se é possível formar um triangulo')
print('=' * 50)
print('\033[m', end='')

a = float(input('\nDigite o tamanho do primeiro lado: '))
b = float(input('Digite o tamanho do segundo lado: '))
c = float(input('Digite o tamanho do terceiro lado: '))

det1 = int(a + b > c)  # Os três aqui verificam se a expressão é true ou false
det2 = int(a + c > b)  # e por ter um int antes de cada expressão, os valores boleanos
det3 = int(b + c > a)  # se tornam 1 e 0

if det1 + det2 + det3 == 3:  # como eu preciso que as três sejam verdadeiras eu só comparo a soma dos itens a o número 3
    print('\n\033[32mÉ possível formar o triangulo')
else:
    print('\n\033[31mNão é possível formar o triangulo')
