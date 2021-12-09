import random

class Ability:
    def __init__(self, name: str, max_damage: int) -> None:
        self.name = name 
        self.max_damage = max_damage
    
    def attack(self) -> int:
        return random.randint(0, self.max_damage)
    

if __name__ == "__main__":
  ability = Ability("Debugging Ability", 20)
  print(ability.name)
  print(ability.attack())