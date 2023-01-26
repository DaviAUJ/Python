from datetime import date

anonas = int(input('\nEm que ano você nasceu? '))
sexo = str(input('Qual é o seu sexo(F para mulher, M para homem)? ')).strip().lower()

if sexo == 'm':

    anoatu = date.today().year
    idade = anoatu - anonas
    anoali = anonas + 18

    print(f'\nQuem nasceu em {anonas} tem {idade} em {anoatu}')
    if idade == 17:
        print('Você ainda não está na idade para se alistar, falta 1 ano')
        print(f'Seu alistamento será em {anoali}')
    elif idade < 17:
        print(f'Você ainda não está na idade para se alistar, faltam {18 - idade} anos')
        print(f'Seu alistamento será em {anoali}')
    elif idade == 18:
        print('Já está na hora de se alistar')
    elif idade == 19:
        print('Você está atrasado para o seu alistamento por 1 ano')
        print(f'Seu alistamento foi em {anoali}')
    elif 60 > idade > 19:
        print(f'Você está atrasado para o seu alistamento por {idade - 18} anos ')
        print(f'Seu alistamento foi em {anoali}')
    else:
        print(f'Já passou da idade de se alistar')
elif sexo == 'f':
    print('Mulher não precisa se alistar')
else:
    print('Incorreto')
