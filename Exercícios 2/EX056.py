poolida = 0
poolmmv = 0
poolhom = 0
listano = []
listaid = [0]

for x in range(0, 4):
    print(f'\n\033[1m<<<<< {x + 1}° pessoa >>>>>')
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo[M/F]: ')).strip().upper()
    print('\033[m', end='')

    poolida += idade
    if sexo == 'M':
        listano.append(nome)
        listaid.append(idade)
        poolhom += 1
    if sexo == 'F' and idade < 20:
        poolmmv += 1

if poolhom > 0:
    posmida = listaid.index(max(listaid))
else:
    posmida = 0
    listano.append('\033[1;31mnão há homens nas credenciais inseridas')

print(f'Média de idade: {poolida / 4}')
print(f'A número de mulheres com menos de 20 anos é {poolmmv}')
print(f'O nome do homem mais velho tem {max(listaid)} anos e se chama {listano[posmida]}')
