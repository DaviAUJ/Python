def area(largura, comprimento):
    resultado = largura * comprimento
    print(f"\nUm terreno de {largura}m por {comprimento}m tem {resultado}m²")


# Programa principal
lar = float(input("\nLargura(Em Metros): "))
com = float(input("Comprimento(Em Metros): "))

area(lar, com)
