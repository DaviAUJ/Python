listagem = ("lápis", 1.75, "Borracha", 2, "Caderno", 15.9, "Estojo", 25, "Transferidor", 4.2, 
"Compasso", 9.99, "Mochila", 120.32, "Canetas", 22.3, "Livro", 34.9, "Cacete de Agulha", 666,
"Sussy", 4.2, "Baka", 6.9, "Cock", 23.67, "Casa", 74945.99)

print('-' * 32 + '\n' + "LISTAGEM DE PREÇOS".center(32) + '\n' + '-' * 32)

for i in range(0, len(listagem), 2):
    print(listagem[i].ljust(22, '.') + 'R$' + f"{listagem[i + 1]:.2f}".rjust(8))

print('-' * 32)
