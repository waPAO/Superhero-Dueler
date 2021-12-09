import random

class Hero:
    def __init__(self, name: str, starting_health: int = 100) -> None:
        self.name = name
        self.starting_health = starting_health
        self.current_health = starting_health
    
    def fight(self, opponent):
        print(f'{random.choice([self.name, opponent.name])} won!')



if __name__ == '__main__':
    hero1 = Hero("Wonder Woman")
    hero2 = Hero("Dumbledore")

    hero1.fight(hero2)
