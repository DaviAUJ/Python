conesq = 0
condir = 0
exp = str(input("Sua expressão: "))

for let in exp:
    if let == '(':
        conesq += 1

    if let == ')':
        condir += 1

if conesq == condir:
    print("Expressão válida")

elif conesq > condir:
    print("Expressão inválida - Parenteses faltando")

else: 
    print("Expressão inválida - Parenteses de mais")
