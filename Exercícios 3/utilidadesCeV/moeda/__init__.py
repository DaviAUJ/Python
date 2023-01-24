def moeda(n=0, moeda='R$'):
    return f"{moeda}{n:.2f}".replace('.', ',')
    # Não sei por as virgulas que o prof pôs no arquivo dele
    

def resumo(p=0, prcntgm0=50, prcntgm1=50):
    dick = {
        'Preço Original': p,
        'Dobro do preço': dobro(p),
        'Metade do preço': metade(p),
        f'Aumento de {prcntgm0}%': aumentar(p, prcntgm0),
        f'Redução de {prcntgm1}%': diminuir(p, prcntgm1)
    }
    
    print(34 * '-')
    print("RESUMO DO VALOR".center(34))
    print(34 * '-')
    
    for k, v in dick.items():
        print(f"{k + ':':<20} {moeda(v):<10}")
    

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
