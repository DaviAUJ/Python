fra = str(input('\nDigite uma frase: ')).strip().lower()
letra = str(input('Digite uma letra: ')).strip().lower()

numA = fra.count(letra)
findA = fra.find(letra)
findLA = fra.rfind(letra)

print(f'\nNa sua frase a letra {letra} aparece {numA} vez(es)')
print(f'Na sua frase o primeiro {letra} aparece na {findA + 1}° posição')
print(f'Na sua frase o último {letra} aparece na {findLA + 1}° posição')
