from datetime import date
ano = int(input('\nQue ano é esse ano? '))

if ano == 0:
    ano = date.today().year

det = ano % 4
det1 = ano % 100
det2 = ano % 400

if det == 0 and det1 != 0 or det2 == 0:
    print(f'O ano de {ano} é bissexto')
else:
    print(f'O ano de {ano} não é bissexto')
