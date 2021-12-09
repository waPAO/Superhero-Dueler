import random

class Armor:
    def __init__(self, name: str, max_block: int) -> None:
        self.name = name
        self.max_block = max_block

    def block(self) -> int:
        return random.randint(0, self.max_block)
    
if __name__ == "__main__":
  armor = Armor("Debugging Shield", 10)
  print(armor.name)
  print(armor.block())