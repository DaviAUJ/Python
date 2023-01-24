import EX108M1 as moeda

p = float(input("Digite o preço: R$"))

print(f"""\nA metade de {moeda.moeda(p)} é {moeda.moeda(moeda.metade(p))}
O dobro de {moeda.moeda(p)} é {moeda.moeda(moeda.dobro(p))}
Aumentando em 10%, temos {moeda.moeda(moeda.aumentar(p, 10))}
Reduzindo 13%, temos {moeda.moeda(moeda.diminuir(p, 13))}""")
