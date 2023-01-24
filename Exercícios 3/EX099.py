from time import sleep


def maior(* num):
    print(40 * '=')
    print("Analisando os valores inseridos...")
    maiornum = 0
    for numero in num:
        print(numero, end=' ' if numero != num[-1] else '\n')
        sleep(0.3)
        if maiornum == 0 or numero > maiornum:
            maiornum = numero

    print(f"Foram informadoas {len(num)} ao todo")
    print(f"O maior valor foi {maiornum}")


# Programa principal
maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()
