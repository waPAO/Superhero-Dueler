import random
from ability import Ability

class Weapon(Ability):
    def attack(self) -> int:
        half_damage = self.max_damage // 2
        return random.randint(half_damage, self.max_damage)