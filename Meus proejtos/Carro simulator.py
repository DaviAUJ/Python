class Carro:
    def __init__(self, Marca="Nulo", Nome="Nulo", Ano="Nulo", Cavalos="Nulo", Tipo_de_combustivel="Nulo", velocidade_max=120):
        self.marca = Marca
        self.nome = Nome
        self.ano = Ano
        self.cavalos = Cavalos
        self.combustivel = Tipo_de_combustivel
        self.max_velocidade = velocidade_max
        self.velocidade_atual = 0
        self.esta_ligado = False
        
    def ligar(self):
        if not self.esta_ligado:
            self.esta_ligado = True
            print("\nVruum Vruum")
            
        else:
            print("\nVocê pode ligar o carro no momento")
        
    def acelerar(self, Vezes=1):
        Vezes = abs(Vezes)
        
        if self.esta_ligado and self.velocidade_atual <= self.max_velocidade:
            if (Vezes * 10) + self.velocidade_atual > self.max_velocidade:
                self.velocidade_atual = self.max_velocidade
                print("\nVelocidade máxima atingida")
            
            else:
                self.velocidade_atual += (Vezes * 10)
                print(f"\nAcelerando... \nVelocidade atual: {self.velocidade_atual}" )
        else:
            print("\nVocê não pode acelerar no momento")
        
    def desacelerar(self, Vezes=1):
        Vezes = abs(Vezes)   
            
        if self.esta_ligado and self.velocidade_atual > 0:
            if (Vezes * 10) + self.velocidade_atual < 0:
                self.velocidade_atual = 0
                print("\nVelocidade mínima atingida")
            
            else:
                self.velocidade_atual -= (Vezes * 10)
                print(f"\nDesacelerando... \nVelocidade atual: {self.velocidade_atual}")
        else:
            print("\nVocê não pode desacelerar no momento")
            
    def freiar(self):
        if not self.esta_ligado:
            print("\nO Carro está desligado")
            
        elif self.velocidade_atual == 0:
            print("\nO carro já está parado")
             
        else:
            self.velocidade_atual = 0
            print("\nCarro freiado")
        
    def desligar(self):
        if self.esta_ligado and self.velocidade_atual == 0:
               self.esta_ligado = False
               print("\nCarro desligado")
               
        else:
            print("\nO carro não pode ser desligado no momento")
            
    def info(self):
        print(f"""\n\rEstá ligado?: {self.esta_ligado}
              \rVelocidade atual: {self.velocidade_atual}
            
              \rMarca: {self.marca}
              \rNome: {self.nome}
              \rAno: {self.ano}
              \rCavalos: {self.cavalos}
              \rCombustível: {self.combustivel}
              \rPotência: {self.max_velocidade}""")
              
              
# Programa principal
carro1 = Carro("Ford", "Fusion", 2020, 143, "Híbrido", 100)
carro2 = Carro("Fiat", "Uno", 1999, 67, "Gasolina", 80)

carro1.ligar()
carro1.info()