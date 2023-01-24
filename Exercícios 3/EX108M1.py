# Módulo do desafio 108, quando importa-lo chame-o de moeda

def metade(n=0):
    return n / 2


def dobro(n=0):
    return n * 2


def aumentar(n=0, prcntgm=50):
    return n + (n * (prcntgm / 100))


def diminuir(n=0, prcntgm=50):
    return n - (n * (prcntgm / 100))


def moeda(n=0, moeda='R$'):
    return f"{moeda}{n:.2f}".replace('.', ',')
    # Não sei por as virgulas que o prof pôs no arquivo dele