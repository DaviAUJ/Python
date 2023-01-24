import datetime

func = dict()
anoatu = datetime.datetime.now().year

func['nome'] = str(input("\nNome: "))
func['ano de nsc'] = int(input("Ano de nascimento: "))
func['idade'] = anoatu - func['ano de nsc']
func['ctr de tblh'] = int(input("CTPS[0 para não]: Nº"))
if func['ctr de tblh'] != 0:
    func['ano de ctc'] = int(input("Ano de contratação: "))
    func['slr'] = int(input("Salário: R$"))
    func['ano de apstdr'] = func['ano de ctc'] + 35
    func['idd de apstdr'] = func['ano de apstdr'] - func['ano de nsc']

print(f"""\nNome: {func['nome']}
Idade: {func['idade']}""")
if func['ctr de tblh'] != 0:
    print(f"Carteira de trabalho: N°{func['ctr de tblh']}")
    print(f"Ano de contratação: {func['ano de ctc']}")
    print(f"Salário: R${func['slr']}")
    print(f"Ano de aposentadoria: {func['ano de apstdr']}")
    print(f"Idade da aposentadoria: {func['idd de apstdr']}")

else: 
    print("Carteira de trabalho: Não possui")
