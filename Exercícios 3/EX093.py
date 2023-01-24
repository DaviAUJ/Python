dados = dict()
gols = list()

dados['nome'] = str(input("\nNome do jogador: "))
npart = int(input(f"Número de partidas que {dados['nome']} jogou: "))

dados['total de gols'] = 0
print()  # Print para formatação
for c in range(0, npart):
    gols.append(int(input(f"Quantos gols na {c + 1}ª partida? ")))

dados['gols'] = gols.copy()
dados['total de gols'] = sum(gols)

print(f'\n{dados}')

print()  # Print para formatação
for k, v in dados.items():
    print(f"O campo {k} tem o valor {v}")

print(f"\nO jogador {dados['nome']} jogou {npart} partidas:")
for c in range(0, npart):
    print(f"Na {c + 1}ª partida, fez {dados['gols'][c]} gols")
print(f"Foi um total de {dados['total de gols']} gols")
