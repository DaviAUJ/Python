def leia_int(msg):
    while True:
        count = 0
        num = input(msg)

        for c in num:
            if c in '1234567890':
                count += 1

        if count == len(num) and num != '':
            return int(num)

        else:
            print("\033[31mCredencial inválida!\033[m")


# Programa principal
n = leia_int("Digite um número: ")
print(f"Você acabou de digitar o número {n}")
