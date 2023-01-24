sal = float(input('\nQual é o seu salário? R$'))

if sal > 1250:
    print(f'\nSeu salário de R${sal:.2f} passará a ser R${sal * 1.1:.2f}')
else:
    print(f'\nSeu salário de R${sal:.2f} passará a ser R${sal * 1.15:.2f}')
