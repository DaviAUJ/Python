lista = []

print('')
for x in range(0, 5):
    peso = float(input('Qual é o seu peso(Kg)? '))
    lista.append(peso)

print(f'\nO maior peso é {max(lista)}Kg e o menor é {min(lista)}Kg')
