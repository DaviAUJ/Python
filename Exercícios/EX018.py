from math import radians, sin, cos, tan

ang = int(input('\nInsira um angulo para saber seu seno, cosseno e tangente: '))
rad = radians(ang)
print(f'O seno de {ang}° é: {sin(rad) :.3f}')
print(f'O cosseno de {ang}° é: {cos(rad) :.3f}')
print(f'A tangente de {ang}° é: {tan(rad) :.3f}')
