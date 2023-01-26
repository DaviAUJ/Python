from time import sleep

estilo = {
    'normal': 0,
    'negrito': 1,
    'sublinhado': 4,
    'inverso': 7,
}

cores_letra = {
    'normal': 0,
    'preto': 30,
    'vermelho': 31,
    'verde': 32,
    'amarelo': 33,
    'azul': 34,
    'roxo': 35,
    'ciano': 36,
    'cinza': 37
}

cores_fundo = {
    'normal': 0,
    'preto': 40,
    'vermelho': 41,
    'verde': 42,
    'amarelo': 43,
    'azul': 44,
    'roxo': 45,
    'ciano': 46,
    'cinza': 47
}


def linha(msg):
    tamanho = len(msg) + 4

    return f"""{tamanho * '~'}
    \r{msg.center(tamanho)}
    \r{tamanho * '~'}"""


def colorir(msg, fonte='normal', cor_letra='normal', cor_fundo='normal'):
    fonte = fonte.lower()
    cor_letra = cor_letra.lower()
    cor_fundo = cor_fundo.lower()

    return f"\033[{estilo[fonte]};{cores_letra[cor_letra]};{cores_fundo[cor_fundo]}m{msg}"


# Programa principal

while True:
    print(colorir(linha("SISTEMA DE AJUDA PyHelp"), 'negrito', 'normal', 'verde'))
    resp = str(input("\033[mFunção ou Biblioteca > ")).lower()

    if resp == 'fim':
        break

    sleep(1)
    print(colorir(linha(f"Acessando o manual do comando '{resp}'"), 'negrito', 'normal', 'azul'))
    print(colorir(f"{help(resp)}", 'negrito', 'preto', 'vermelho'))
    sleep(2)

print(colorir("\nDesligando", cor_letra='verde'), end='')
for c in range(0, 3):  # For para animação
    sleep(0.5)
    print('.', end='')


print(colorir("\nPrograma encerrado", 'negrito', 'verde', 'normal'))
