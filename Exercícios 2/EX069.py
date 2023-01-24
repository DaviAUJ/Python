print('\033[1m\nPrograma pra cadastrar pessoas\033[m')

poolidade = poolhomens = poolfmev = cont = 0

while True:
    cont += 1
    print('\n' + '-' * 20)
    idade = int(input('Idade: '))

    while True:
        sexo = str(input('Sexo[M/F]: ')).lower().strip()[0]

        if sexo in 'mf':
            break
    print('-' * 20)

    if idade > 18:
        poolidade += 1

    if sexo == 'm':
        poolhomens += 1

    if sexo == 'f' and idade < 20:
        poolfmev += 1

    print(f'\nAté agora {cont} pessoa(s) foram cadastradas')
    while True:
        prog = str(input('Quer continuar[S/N]? ')).lower().strip()[0]

        if prog in 'sn':
            break

    if prog == 'n':
        break

print(f'''\nNúmero de pessoas registradas: {cont}
Número de pessoas com mais de 18 anos: {poolidade}
Número de pessoas que são do sexo masculino: {poolhomens}
Número de pessoas que são do sexo feminino e têm menos de 20 anos de idade: {poolfmev}''')
