extenso = ("Zero", "Um", "Dois", "Três", "Quatro", "Cinco", "Seis", "Sete", 
"Oito", "Nove", "Dez", "Onze", "Doze", "Treze", "Cartoze", "Quinze", 
"Dezesseis", "Dezessete", "Dezoito", "Dezenove", "vinte")

while True: 
    while True:
        ins = int(input("\nDigite um número entre 0 e 20 para saber seu extenso: "))

        if ins in range(0, len(extenso)):
            break

        print('\nInválido')

    print(f"{ins} por extenso é {extenso[ins]}")

    while True:
        prog = str(input("\nVocê quer continuar[Y/N]? ")).lower().strip()[0]

        if prog in 'ysn':
            break

        print("\nInválido")

    if prog in 'n':
        break

print("\nObrigado por escolher a Pigas Company, a sua impresa de tecnologia")
