def leia_int(msg):
    while True:
        num = str(input(f"\n{msg}"))
        if num.isnumeric():
            return num

        print("\033[31mCredencial inválida!\033[m")


# Programa principal
n = leia_int("Digite um número: ")
print(f"Você acabou de digitar o número {n}")
