from random import randint
from time import sleep

numeros = list()


def sorteio(lista):
    print("Sorteando 5 números:", end=' ')
    for c in range(0, 5):
        lista.append(randint(1, 10))
        print(numeros[c], flush=True, end='; ' if c != 4 else ';\n')
        sleep(0.5)


def soma_par(lista):
    soma = 0
    for num in lista:
        if num % 2 == 0:
            soma += num
    print(f"Somando os valores pares de: {numeros} - total: {soma}")


sorteio(numeros)
soma_par(numeros)
