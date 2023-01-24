def fatorial(valor, show=False):
    """
    -> Calcula o Fatorial de um número
    :param valor:  O valor a ser calculado
    :param show: (opcional) Mostra ou não a conta
    :return: Retorna a fatorial da variável valor
    """
    fator = 1
    for c in range(valor, 0, -1):
        fator *= c
        if show:
            print(c, end=' x ' if c != 1 else f' == {fator}')

    return fator


print(fatorial(5))
