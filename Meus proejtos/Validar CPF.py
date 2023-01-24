cpf = str()
numero_verificador = list()

while not cpf.isnumeric() or len(cpf) != 11:
    cpf = str(input("\nDigite aqui seu CPF: ")).replace('.', '').replace('-', '').replace(',', '')
    
    if not cpf.isnumeric():
        print("ERRO - Caractere(s) inválido(s)")
        
    elif len(cpf) < 11:
        print("ERRO - Número de caractares insuficiente")
        
    elif len(cpf) > 11:
        print("ERRO - Número excessivo de caracteres")

for i in range(1, -1, -1):  
    suporte = int()
    
    for c in range(1, 10):
        suporte += int(cpf[c - i]) * c

    suporte %= 11
    if suporte == 10:
        suporte = 0
        
    numero_verificador.append(str(suporte))

numero_verificador = ''.join(numero_verificador)

if cpf[-2:] == numero_verificador:
    print("\nCPF Válido")
    
else:
    print("\nCPF Inválido")
