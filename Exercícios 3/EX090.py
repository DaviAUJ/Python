boletim = dict()

boletim['nome'] = str(input("\nNome: "))
boletim['media'] = float(input(f"Média de {boletim['nome']}: "))

if boletim['media'] >= 7:
    boletim['situacao'] = '\033[32mAprovado\033[m'

elif 5 <= boletim['media'] < 7:
    boletim['situacao'] = '\033[33mRecuperação\033[m'

else:
    boletim['situacao'] = '\033[31mReprovado\033[m'

print(
    f"""\nNome: {boletim['nome']}
    \rMédia: {boletim['media']}
    \rSituação: {boletim['situacao']}"""
)
