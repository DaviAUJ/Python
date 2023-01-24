def escreva(frase):
    tam = len(frase) + 4
    print()  # print() para formatação
    print(tam * '~')
    print(frase.center(tam))
    print(tam * '~')


# Programa principal
escreva("Gustavo Guanabara")
escreva("Curso de Python no YouTube")
escreva("CeV")
