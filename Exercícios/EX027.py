nome = str(input('\nDigite o seu nome completo: ')).strip()

n = nome.split()

print(f'O seu primeiro nome é: {n[0]}')
print(f'O seu último nome é: {n[-1]}')
