from time import sleep

n = int(input('\nDigite o primerio valor: '))
n1 = int(input('Digite o segundo valor: '))

escolha = 0

while escolha != 5:
    print('\nEscolha o que você quer fazer com os números')
    print('[ 1 ] Somar')
    print('[ 2 ] Multiplicação')
    print('[ 3 ] Maior número')
    print('[ 4 ] Novos números')
    print('[ 5 ] Sair do programa')

    escolha = int(input('\nEscolha uma opção: '))

    if escolha == 1:
        print('\nVocê escolheu soma')
        print(f'A soma entre {n} e {n1} é igual a {n + n1}')

    elif escolha == 2:
        print('\nVocê escolheu multiplicação')
        print(f'A multiplicação entre {n} e {n1} é igual a {n * n1}')

    elif escolha == 3:
        print('\nVocê escolheu o maior número')
        print(f'O maior número dos escolhidos é {max(n, n1)}')

    elif escolha == 4:
        print('\nVocê escolheu inserir novos números')
        n = float(input('Digite o primeiro valor: '))
        n1 = float(input('Digite o segundo valor: '))

    elif escolha == 5:
        print('Finalizando...')

    else:
        print('\nComando inválido. Tente novamente')

    sleep(2)

print('\nVocê escolheu sair do programa. Adeus!')
