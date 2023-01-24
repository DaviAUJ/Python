from math import hypot
cat1 = float(input('\nMedida do primeiro cateto: '))
cat2 = float(input('Medida do segundo cateto: '))
# print(f'A hipotenusa possui {sqrt(pow(cat1, 2) + pow(cat2, 2)) :.2f} de medida')
# Esse metodo é pior
print(f'\nA hipotenusa possui {hypot(cat1, cat2) :.2f} de medida')
