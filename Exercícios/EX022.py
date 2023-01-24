nome = str(input('\nEscreva o seu nome completo: ')).strip()

nomeLMa = nome.upper()
nomeLMi = nome.lower()
numL = (len(nome) - nome.count(' '))
nomeS = nome.split()
numLPN = len(nomeS[0])

print(f'\nAqui está seu nome com apenas letras maiúsculas: {nomeLMa}')
print(f'Aqui está seu nome com apenas letras minúsculas: {nomeLMi}')
print(f'Aqui está o número de letras no seu nome: {numL}')
print(f'Aqui está o número de letras no seu primeiro nome: {numLPN}')
