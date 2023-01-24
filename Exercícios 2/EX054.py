from datetime import date

anoatu = date.today().year
soma = 0

print('')  # Serve só pra formatação do programa
for c in range(0, 7):
    anonas = int(input('Em qual ano você nasceu? '))
    idade = anoatu - anonas

    if idade >= 21:
        soma += 1

print(f'''\n{soma} é número de pessoas do grupo seleto que são maiores de idade
{7 - soma} é número de pessoas que ainda são menores de idade''')
