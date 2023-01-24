sex = str(input('\nQual é o seu secho(M/F)? ')).strip().lower()[0]

while sex not in 'mf':
    print('\nCredencial inválida')
    sex = str(input('Qual é o seu secho novamente? ')).strip().lower()[0]

if sex == 'm':
    print('\nVocê é do século masculino!1!!')
else:
    print('\nVocê e mulher kkkkk')
