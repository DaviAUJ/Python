val = int(input('\nQual é o valor da casa que quer comprar? R$'))
sal = int(input('Quanto vale o seu salário? R$'))
tem = int(input('Em quantos anos você irá pagar a casa: '))

mes = tem * 12  # calcula quantos meses tem em x de anos
pre = val / mes  # calcula o valor da prestação

if pre > 0.3 * sal:  # checa se a prestação tem um valor maior do que 30% do 'sal'
    print(f'\nInfelizmente você não poderá comprar essa casa, a prestação excede 30% do seu salário')
else:
    print('Que ótimo, a compra será realizada com sucesso!')
