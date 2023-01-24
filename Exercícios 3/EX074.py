from random import randint

numales = (randint(0, 10), randint(0, 10), randint(0, 10), 
           randint(0, 10), randint(0, 10))

print("\nLista de números")
for i in range(0, 5):
    print(f"{i + 1}. {numales[i]}")

print(f"""\nO Maior número sorteado foi {max(numales)}
O menor número sorteado foi {min(numales)}""")
