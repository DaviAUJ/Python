def leiaDinheiro(msg):
    valido = False
    
    while not valido:
        valor = str(input(msg)).strip().replace(',', '.')
        
        if valor.isalpha() or valor == '':
            print(f"ERRO - Credencial \"{valor}\" inválida")
            
        else:
            valido = True
            return float(valor)
