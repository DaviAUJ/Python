from datetime import date

anonas = int(input('\nEm que ano você nasceu? '))
anoatu = date.today().year
idade = anoatu - anonas

print(f'\nO atleta tem {idade}')
if 0 < idade <= 9:
    print('Categoria: Mirim')
elif 9 < idade <= 14:
    print('Categoria: Infantil')
elif 14 < idade <= 19:
    print('Categoria: Junior')
elif 19 < idade <= 25:
    print('Categoria: Sênior')
elif 25 < idade <= 60:
    print('Categoria: Mestre')
else:
    print('Categoria: Já está muito velho para competir')
