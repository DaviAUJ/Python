dados = dict()
geral = list()
gols = list()

while True:
    dados['nome'] = str(input("\nNome do jogador: ")).strip().capitalize()
    npart = int(input(f"Número de partidas que {dados['nome']} jogou: "))

    dados['total de gols'] = 0
    print()  # Print para formatação
    for c in range(0, npart):
        gols.append(int(input(f"Quantos gols na {c + 1}ª partida? ")))
        dados['total de gols'] += gols[c] 

    dados['gols'] = gols.copy()
    geral.append(dados.copy())
    dados.clear()
    gols.clear()

    while True:
        prog = str(input("\nContinuar? ")).strip().lower()[0]

        if prog in 'ysn':
            break

        print("\033[31mCredencial inválida\033[m")

    if prog == 'n':
        break

#  Apartir daqui é análise de dados

print("\nN°".ljust(5), "Nome".ljust(15), "total".ljust(10), "gols")
print(60 * '-')
for c in range(0, (len(geral))):
    print(f"{c:<4} {geral[c]['nome']:<15} {geral[c]['total de gols']:<10} {geral[c]['gols']}")
print(60 * '-')

while True:
    while True:
        prog = int(input("\nMostar dados de qual jogador[999 para cancelar]? "))

        if prog <= (len(geral) - 1) or prog == 999:
            break

        print("\n\033[31mNúmero de jogador inválido\033[m")

    if prog == 999:
        break

    print(f"\nLevantamento do jogador {geral[prog]['nome']}")
    for c in range(0, len(geral[prog]['gols'])):
        print(f"No {c + 1}ª jogo ele marcou {geral[prog]['gols'][c]} gols")

    print('\n' + 60 * '-')

print("\n\033[32mPrograma encerrado")
