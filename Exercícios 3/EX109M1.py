# Módulo do desafio 109, quando importa-lo chame-o de moeda
def moeda(n=0, moeda='R$'):
    return f"{moeda}{n:.2f}".replace('.', ',')


def metade(n=0, formatar=False):
    n /= 2
    
    if formatar:
        return moeda(n)
    
    else:
        return n


def dobro(n=0, formatar=False):
    n *= 2
    
    if formatar:
        return moeda(n)
    
    else:
        return n


def aumentar(n=0, prcntgm=50, formatar=False):
    novo_valor = n + (n * (prcntgm / 100))
    
    if formatar:
        return moeda(novo_valor)
    
    else:
        return novo_valor


def diminuir(n=0, prcntgm=50, formatar=False):
    novo_valor = n - (n * (prcntgm / 100))
    
    if formatar:
        return moeda(novo_valor)
    
    else:
        return novo_valor
