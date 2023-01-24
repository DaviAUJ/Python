def leiaInt(msg, limite=False, max=1, min=0):
    valido = False

    while not valido:
        try:
            num = int(input(msg))
        except:
            print("ERRO - Credencial inválida")
        else:
            if limite:
                if num in range(min, max + 1):
                    valido = True
                else:
                    print("ERRO - Credencial inválida")
            else:
                valido = True
    return num

def leiaStr(msg, min=0, limite=False, max=1):
    valido = False

    while not valido:
        num = str(input(msg))

        if limite:
            if len(num) > max:
                print("Limite máximo de letras atingidos!")
                continue
            
        if len(num) < min:
            print("Número de insuficiente de letras!")
            continue

        for letter in num:
            if letter == ':':
                print("ERRO - O nome não pode conter \":\"!")
                break   
            elif letter == num[-1]:
                valido = True                
    num = num.strip()  # Retira espaços inúteis fora da string
    num = ' '.join(num.split())  # Retira espaços inúteis dentro da string

    return num

def linha():
    print('-' * 60)


# Programa principal 
import os
import time

continuar = True
arquivo = 'Exercícios 3\\EX115.txt'

while continuar:
    linha()
    print("MENU PRINCIPAL".center(60))
    linha()

    print("""1 - Ver pessoas cadastradas
          \r2 - Cadastrar nova pessoa
          \r3 - Deletar cadastro
          \r4 - Criar novo arquivo
          \r5 - Deletar arquivo atual
          \r6 - sair do programa""")
    linha()

    opcao = leiaInt("Sua opção: ", True, 6, 1)
    linha()

    # Mostra a lista de pessoas
    if opcao == 1:
        if os.path.exists(arquivo):
            if os.stat(arquivo).st_size != 0:
                with open(arquivo, 'r') as txt:
                    for line in txt:
                        dado = line.split(':')
                        
                        print(dado[0].ljust(50) + dado[1].strip('\n').rjust(3), 'anos')
            else:
                print("O Arquivo está vazio!")
        else:
            print("O arquivo não existe!")

        linha()
        input("pressione Enter para continuar...")

    # Cria caixas possibilitando a entrada de dados                               
    elif opcao == 2:
        if os.path.exists(arquivo):
            with open(arquivo, 'a') as txt:
                txt.write(leiaStr("Nome: ", 1, True, 48) + ':')
                txt.write(str(leiaInt("Idade: ", True, 999, 1)) + '\n')
                txt.close()

            print("Pessoa cadastrada com sucesso!")

        else:
            print("O arquivo não existe!")

        linha()
        input("pressione Enter para continuar...")
        
    elif opcao == 3:
        if os.path.exists(arquivo):
            if os.stat(arquivo).st_size != 0:
                with open(arquivo, 'r') as txt:
                    lines = txt.readlines()
                    apagar = leiaInt("Número de quem você quer apagar[0 para sair]: ", True, len(lines), 0)
                
                if apagar != 0:
                    with open(arquivo, 'w') as txt:
                        for number, line in enumerate(lines):
                            if number != (apagar - 1):
                                txt.write(line)
                            else:
                                dado = line.split(':')
                                deletado = dado[0]

                    print(f"\"{deletado}\" foi deletado com sucesso")   
                    
                else:
                    print("Nada foi deletado da lista")
            else:
                print("O arquivo está vazio!")
        else:
            print("O arquivo não existe!")
                
        linha()
        input("pressione Enter para continuar...")

    # Cria um novo arquivo se ele não já existe        
    elif opcao == 4:
        if not os.path.exists(arquivo):
            txt = open(arquivo, 'x')
            print("Arquivo criado com sucesso!")
        else:
            print("O arquivo já existe!")

        linha()
        input("pressione Enter para continuar...")

    # Deleta o arquivo se ele existe    
    elif opcao == 5:
        confirmacao = bool(leiaInt("Tem certeza que quer apagar o arquivo[0 para não/1 para sim]? ", True, 1, 0))

        if confirmacao:
            if os.path.exists(arquivo):
                os.remove(arquivo)
                print("Arquivo deletado com sucesso!")
            else:
                print("O arquivo não existe!")

        else:
            print("Seu arquivo não foi deletado")

        linha()
        input("pressione Enter para continuar...")

    elif opcao == 6:
        continuar = False

        time.sleep(0.25)
print("programa finalizado. Obrigado por usar os produtas da Pigas LTDA")
