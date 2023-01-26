from math import pow

peso = float(input('\nInsira seu peso(em quilos): '))
alt = float(input('Insira sua altura(em metros): '))

imc = peso / pow(alt, 2)

print(f'\nSeu resultado foi: {imc:.2f}')
if imc < 18.5:
    print('Você está abaixo do peso ideal')
elif 25 > imc >= 18.5:
    print('Você está no peso ideal')
elif 30 > imc >= 25:
    print('Você está um pouco acima do peso ideal')
elif 40 > imc >= 30:
    print('Você está obeso(Obesidade nível 1)')
else:
    print('Você está gravemente obeso(obesidade nível 2)')
