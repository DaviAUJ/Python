kmult = int(input('\nVocê estava dirigindo a quantos Km/h? '))

valmul = (kmult - 80) * 7

if kmult > 80:
    print(f'\nVocê será multado!\nO valor da sua multa será: R${valmul}')

else:
    print('\nQue ótimo! Você não foi multado!')
