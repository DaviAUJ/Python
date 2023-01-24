sum = pool1000 = pool = 0
name = [] 
price = []

while True:
    pool += 1
    item = str(input('\nNome do produto: '))
    name.append(item)

    item = int(input('Preço do produto: R$'))
    price.append(item)
    sum += item

    if item >= 1000:
        pool1000 += 1

    print(f'\nNúmero de produto(s) adicionado(s): {pool}')
    while True:
        prog = str(input('Quer continuar[S/N]? ')).lower().strip()[0]

        if prog in 'sn':
            break
        print('Inválido')

    if prog == 'n':
        break

cheap = name[price.index(min(price))]

print(f'''\nPreço total: R${sum:.2f}
Número de produtos que custam mais de R$1000: {pool1000}
Nome do produto mais barato: {cheap}
Preço do produto mais barato: R${min(price):.2f}''')
