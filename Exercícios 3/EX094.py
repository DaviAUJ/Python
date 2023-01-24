dados = list()
temp = dict()

while True:
    temp['nome'] = str(input("\nNome: ")).strip().capitalize()

    while True:
        temp['sexo'] = str(input("Sexo: ")).strip().upper()[0]

        if temp['sexo'] in 'MF':
            break

        print(f"\033[31mCredencial inválida\033[m")
    
    temp['idade'] = int(input("Idade: "))

    dados.append(temp.copy())
    temp.clear()
        
    while True:
        prog = str(input("\nContinuar? ")).upper()[0]

        if prog in 'YSN':
            break

        print("\033[31mCredencial inválida\033[m")

    if prog == 'N':
        break

media_de_idade = 0
for c in range(0, len(dados)):
    media_de_idade += dados[c]['idade']
media_de_idade /= len(dados)

print(f"""\nNúmero de pessoas cadastradas: {len(dados)}
A média de idade é: {media_de_idade} anos
Todas as mulheres cadastradas:""", end=' ')
for persona in dados:
    if persona['sexo'] == 'F':
        print(persona['nome'], end='; ')

print(f"\nLista de pessoas que são mais velhos que média: \n")
for persona in dados:
    if persona['idade'] > media_de_idade:
        for k, v in persona.items():
            print(f"{k} == {v}", end='; ')
        print('\n')  # Print(\n) para formatação

print("Programa finalizado")
