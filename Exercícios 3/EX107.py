import EX107M1 as moeda

p = float(input("Digite o preço: R$"))

print(f"""\nA metade de R${p:.2f} é R${moeda.metade(p):.2f}
O dobro de R${p:.2f} é R${moeda.dobro(p):.2f}
Aumentando em 10%, temos R${moeda.aumentar(p, 10):.2f}
Reduzindo 13%, temos R${moeda.diminuir(p, 13):.2f}""")
