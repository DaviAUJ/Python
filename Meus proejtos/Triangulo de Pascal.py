def pascal(num_linhas, mostrar_linhas: bool=False):
    quant_linhas = int()
    linha = [1, 1]
    linha_apoio = list()
    
    while quant_linhas < num_linhas - 1:
        if mostrar_linhas:
            if quant_linhas == 0:
                print("0 - 1")

            print(f"{linha[1]} -", end=' ')
            
            for index, item in enumerate(linha):
                print(f"{item} ", end='\n' if index == len(linha) - 1 else '')

        for index_n0 in range(0, len(linha) - 1):
            index_n1 = index_n0 + 1
            soma = linha[index_n0] + linha[index_n1]
            
            linha_apoio.append(soma)
            
        linha = linha_apoio[:]
        linha_apoio.clear()
        quant_linhas += 1
        
        linha.insert(0, 1)
        linha.append(1)

    print(f"{linha[1]} -", end=' ')
        
    for index, item in enumerate(linha):       
        print(f"{item} ", end='\n' if index == len(linha) - 1 else '')
    
# Programa Principal
pascal(20, False)
