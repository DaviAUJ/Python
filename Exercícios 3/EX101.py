def voto(nascimento):
    from datetime import datetime 
    
    ano_atual = datetime.now().year
    idade = ano_atual - nascimento

    if idade < 16:
        return f"Para {idade} anos: NEGADO"
    elif 16 <= idade < 18 or idade >= 65:
        return f"Para {idade} anos: VOTO OPCIONAL"
    else:
        return f"Para {idade} anos: VOTO OBRIGATÓRIO"


nasc = int(input("Ano de nascimento: "))

print(voto(nasc))
