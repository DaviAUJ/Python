import random

class Char:
    def __init__(self, name: str, maximum_hp: int, damage: int, speed: int, type: str):
        self.name = name
        self.maxhp = maximum_hp
        self.hp = maximum_hp
        self.dmg = damage
        self.speed = speed
        self.type = type

    weaknesses = {
        "Rock": "Paper",
        "Paper": "Scissors",
        "Scissors": "Rock"
    }
        
    def show_stats(self):
        print(f"""Name: {self.name}
              \rHP: {self.hp}/{self.maxhp}
              \rDamage: {self.dmg}
              \rElemental Type: {self.type}
              """)

    def attack(self, target: 'Char'):
        attack_coeficient = 1
        
        if self.type == Char.weaknesses[target.type]:  
            attack_coeficient = 2
            
        target.hp -= self.dmg * attack_coeficient

    
def call_battle(char1: Char, char2: Char):
    print(f"You've encountered a foe!\n{char1.name} Vs. {char2.name}")
    
    if char1.speed > char2.speed:
        order = (char1, char2)
        
    elif char1.speed < char2.speed:
        order = (char2, char1)
        
    else:
        order = tuple(random.sample([char1, char2], 2))
        
    turn_count = 0
    winner = str()
    
    while char1.hp > 0 and char2.hp > 0:
        turn_count += 1
        
        print(f"\nNumber of Turns: {turn_count}")
        print(f"{char1.name} HP: {char1.hp}/{char1.maxhp}\n{char2.name} HP: {char2.hp}/{char2.maxhp}")
        
        input('Continuar...')
        # Fastest one's turn
        order[0].attack(order[1])
        
        print(f"\n{char1.name} HP: {char1.hp}/{char1.maxhp}\n{char2.name} HP: {char2.hp}/{char2.maxhp}")
        if order[1].hp <= 0:
            winner = order[0]
            break
        
        input('Continuar...')
        # Slowest one's turn
        order[1].attack(order[0])
        
    if winner == '':
        winner = order[1]
        
    print(f"The winner is {winner.name}")
