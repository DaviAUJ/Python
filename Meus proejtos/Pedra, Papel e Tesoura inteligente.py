import random
import time


def limitarOpcao(item=''):
    lista = ['Pedra', 'Papel', 'Tesoura']   
    
    if item != '':
        lista.remove(item)
    
    return lista


# Opções e suas fraquezas
opcoes = {
    'Pedra': {'nome': 'Pedra', 'Fraqueza': 'Papel'},
    'Papel': {'nome': 'Papel', 'Fraqueza': 'Tesoura'},
    'Tesoura': {'nome': 'Tesoura', 'Fraqueza': 'Pedra'}
}

# Estatísticas da partida
estatisticas = {  
    'NumeroDeRodadas': 0,
    'Player': 0,
    'Empate': 0,
    'PC': 0
}

# Looping do jogo em si
while estatisticas['NumeroDeRodadas'] < 7:
    estatisticas['NumeroDeRodadas'] += 1
    
    print('-' * 40)
    print(f"Número desta rodada: {estatisticas['NumeroDeRodadas'] - estatisticas['Empate']}")
    
    # Verifica se o input está correto
    while True:
        player = str(input("\nSua jogada: ")).strip().capitalize()
        
        if player in opcoes:
            break
        
        print("ERRO - Credencial inválida")

    # Se a rodada for a primeira o script gera uma jogada aleatória baseda em estatisticas
    if estatisticas['NumeroDeRodadas'] == 1:
        decidir = random.randint(1, 1000)
        
        if decidir in range(1, 355):
            pc = opcoes['Pedra']['Fraqueza']
            
        elif decidir in range(355, 706):
            pc = opcoes['Papel']['Fraqueza']
            
        elif decidir in range(706, 1001):
            pc = opcoes['Tesoura']['Fraqueza']
            
    else:
        # Se o resultado da rodada anterior for um empate o bot escolherá igualmente as opções
        if resultado == 'Empate':
            pc = random.choice(limitarOpcao())
        
        # Se o resultado da rodada anterior for uma derrota o bot terá 75% de chance de escolher a fraqueza do que o player jogou
        # e 25% divido em 50/50 de escolher as outras opções
        elif resultado == 'Derrota':
            decidir == random.randint(1, 1000)
            
            if decidir in range(1, 801):
                pc = opcoes[jogadaPassadaPlayer]['Fraqueza']
                
            elif decidir in range(801, 1001):
                pc = random.choice(limitarOpcao(opcoes[jogadaPassadaPlayer]['Fraqueza']))
        
        # Se o resultado da rodada anterior for uma vitória o bot terá 75% de chance de escolher a mesma jogada que o player jogou na rodada anterior
        # e 25% divido em 50/50 de escolher as outras opções        
        elif resultado == 'Vitoria':
            decidir == random.randint(1, 1000)
                
            if decidir in range(1, 801):
                pc = jogadaPassadaPlayer
                
            elif decidir in range(801, 1001):
                pc = random.choice(limitarOpcao(jogadaPassadaPlayer))
                
    # Mostra as jogadas de cada lado
    time.sleep(0.5)
    print(f"""\nPlayer: {player}
        \rBot: {pc}""")
    time.sleep(1)
    
    # Verifica se foi empate
    if player == pc:
        print("\nEmpate")
        estatisticas['Empate'] += 1
        estatisticas['NumeroDeRodadas'] -= 1
        resultado = 'Empate'

    # Verifica se o player ganhou
    elif player == opcoes[pc]['Fraqueza']:
        print("\nO player ganhou")
        estatisticas['Player'] += 1
        resultado = 'Derrota'

    # Verifica se o PC ganhou   
    elif pc == opcoes[player]['Fraqueza']:
        print("\nO bot ganhou")
        estatisticas['PC'] += 1
        resultado = 'Vitoria'
    
    jogadaPassadaPlayer = player
    
    # Como o jogo é melhor de 7, quando qualquer um dos dois lados chegarem a 4 o jogo termina
    if estatisticas['PC'] == 4 or estatisticas['Player'] == 4:
        if estatisticas['PC'] == 4:
            ganhador = 'Bot'
            
        if estatisticas['Player'] == 4:
            ganhador = 'Player'
            
        break

print('-' * 40)    
print(f"""O jogo terminou!
O vencedor foi o {ganhador}""")
