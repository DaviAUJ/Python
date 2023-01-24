from time import sleep

sup = dict()


def contador(ini, fim, pas):
    print(60 * '=')
    print(f"Contagem de {ini} até {fim} em {pas if pas > 0 else -pas} passo(s)")

    if ini > fim:
        pas = -abs(pas)

    elif ini < fim:
        pas = abs(pas)

    if pas > 0:
        fim += 1

    elif pas < 0:
        fim -= 1

    else:
        if fim > ini:
            pas = 1
            fim += 1

        elif fim < ini:
            pas = -1
            fim -= 1

    for c in range(ini, fim, pas):
        print(c, end=' -> ')
        sleep(0.3)

    print("Fim")


# Programa principal
contador(1, 10, 1)
contador(10, 0, -2)

print(60 * '=')
print("Agora é sua vez de personalizar a contagem!")
sup['inicio'] = int(input("Início: "))
sup['fim'] = int(input("Fim: "))
sup['passo'] = int(input("Passo: "))

contador(sup['inicio'], sup['fim'], sup['passo'])
