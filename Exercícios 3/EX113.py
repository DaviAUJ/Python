def leiaInt(msg):
    valido = False
    
    while not valido:
        try:
            num = int(input(msg))
        except (ValueError, TypeError):
            print("ERRO - Tipo de credencial incorreto")
        else:
            valido = True
    return num

def leiaFloat(msg):
    valido = False
    
    while not valido:
        try:
            num = float(input(msg))
        except (ValueError, TypeError):
            print("ERRO - Tipo de credencial incorreto")
        else:
            valido = True
    return num


inteiro = leiaInt("\nNúmero inteiro: ")
real = leiaFloat("\nNúmero real: ")

print(f"""\nNúmero inteiro inserido: {inteiro}
      \rNúmero real inserido: {real}""")
