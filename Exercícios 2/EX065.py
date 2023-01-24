conf = 's'  # Variavel para saber se o usuario quer continuar ou não
pool = soma = 0  # pool para contar quantos número foram inseridos e somátoria dos número inseridos
lista = []  # lista para agregar os números inserido e depois dizer qual é o maior ou menor

while conf in 'Ss':
    numins = int(input('\nInsira um número: '))
    lista.append(numins)
    soma += numins
    pool += 1

    conf = str(input('Quer continuar(S/N)? '))[0]

print(f'''\nMédia Aritmética: {soma / pool:.2f}
O maior número inserido foi {max(lista)}
O menor número inserido foi {min(lista)}''')
