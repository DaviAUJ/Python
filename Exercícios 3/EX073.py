times = ("Flamengo", "Internacional", "Atlético-MG", "São Paulo", "Fluminense", "Grêmio", "Palmeiras", "Santos", "Athletico-PR", "Bragantino", 
"Ceará SC", "Corinthians", "Atlético-GO", "Bahia", "Sport Recife", "Fortaleza", "Vasco da Gama", "Goiás", "Coritiba", "Botafogo")

print("\nOs cinco primeiros colocados foram:")
for i in range(0, 5):
    print(f"{i + 1}. {times[i]}")

print("\nOs ultimos quatro colocados foram:")
for i in range(len(times), (len(times) - 4), -1):
    print(f"{i}. {times[i - 1]}")

#  Chapecoense não está na lista, trocarei por Sport Recife
print(f"""\nPosição do Sport Recife na tupla:
ele está em {times.index("Sport Recife") + 1}° lugar""")

print("\nLista dos times em ordem alfabética:")
for i in range(0, len(times)):
    print(f"{i + 1}. {sorted(times)[i]}")

