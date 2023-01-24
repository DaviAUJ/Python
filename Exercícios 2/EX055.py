maior = 0
menor = 0

print('')
for x in range(0, 5):
    peso = float(input(f'Qual é o peso(Kg) da {x + 1}° pessoa? '))
    if x == 0:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        elif peso < menor:
            menor = peso
print(f'\nO maior peso foi {maior}Kg e o menor foi {menor}Kg')
