import EX109M1 as moeda

p = float(input("Digite o preço: R$"))

print(f"""\nA metade de {moeda.moeda(p)} é {moeda.metade(p, True)}
O dobro de {moeda.moeda(p)} é {moeda.dobro(p, True)}
Aumentando em 10%, temos {moeda.aumentar(p, 10, True)}
Reduzindo 13%, temos {moeda.diminuir(p, 13, True)}""")
