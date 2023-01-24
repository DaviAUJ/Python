med1 = float(input('\nQual foi a sua média 1? '))
med2 = float(input('Qual foi a sua média 2? '))

medall = (med1 + med2) / 2

print(f'\nSua média foi de {medall:.1f}')
if medall < 5.0:
    print('\033[31mREPROVADO')
elif 7 > medall >= 5.0:
    print('\033[33mRECUPERAÇÃO')
else:
    print('\033[32mAPROVADO')
