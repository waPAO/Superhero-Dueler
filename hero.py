import random
from ability import Ability
from armor import Armor
from weapon import Weapon

class Hero:
    def __init__(self, name: str, starting_health: int = 100) -> None:
        self.name = name
        self.starting_health = starting_health
        self.current_health = starting_health
        self.deaths = 0
        self.kills = 0
        self.abilities = []
        self.armors = []
        
    
    def add_ability(self, ability) -> None:
        self.abilities.append(ability)
    
    def add_armor(self, armor) -> None:
        self.armors.append(armor)
    
    def add_weapon(self, weapon) -> None:
        self.abilities.append(weapon)

    def add_kill(self, num_kills: int) -> None:
        self.kills += num_kills
    
    def add_death(self, num_deaths: int) -> None:
        self.deaths += num_deaths

    def attack(self) -> int:
        total_damage = 0
        for ability in self.abilities:
            total_damage += ability.attack()
        return total_damage
   
    def defend(self) -> int:
        total_block = 0
        for armor in self.armors:
            total_block += armor.block()
        return total_block
    
    def take_damage(self, damage) -> None:
        damage_taken = damage - self.defend()
        if damage_taken > 0:
            self.current_health -= damage_taken
    
    def is_alive(self) -> bool:
        if self.current_health <= 0:
            return False
        return True
    
    def fight(self, opponent) -> None:
        if len(self.abilities) == 0 and len(opponent.abilities) == 0:
            print('Draw!')
        else:
            while True:
                my_damage = self.attack()
                opponent_damage = opponent.attack()

                self.take_damage(opponent_damage)
                opponent.take_damage(my_damage)

                if self.is_alive() == False and opponent.is_alive() == False:
                    print('Draw!')
                    break
                elif self.is_alive() == False:
                    print(f'{opponent.name} won!')
                    self.add_kill(1)
                    opponent.add_death(1)
                    break
                elif opponent.is_alive() == False:
                    print(f'{self.name} won!')
                    opponent.add_kill(1)
                    self.add_death(1)
                    break
                else:
                    pass
    


if __name__ == "__main__":
    hero = Hero("Wonder Woman")
    weapon = Weapon("Lasso of Truth", 90)
    hero.add_weapon(weapon)
    print(hero.attack())