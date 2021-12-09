import random

class Team:
    def __init__(self, name: str) -> None:
        self.name = name
        self.heroes = []
    
    def view_all_heroes(self) -> None:
        for hero in self.heroes:
            print(hero.name)

    def add_hero(self, hero) -> None:
        self.heroes.append(hero)
        
    def remove_hero(self, name: str) -> None:
        foundHero = False
        for hero in self.heroes:
            if hero.name == name:
                self.heroes.remove(hero)
                foundHero = True
            
        if not foundHero:
            return 0
    
    def stats(self) -> None:
        for hero in self.heroes:
            kd = hero.kills / hero.deaths
            print(f"{hero.name} Kill/Deaths:{kd}")
    
    def revive_heroes(self) -> None:
        for hero in self.heroes:
            hero.current_health = hero.starting_health
    
    def attack(self, other_team) -> None:
        living_heroes = []
        living_opponents = []

        for hero in self.heroes:
            living_heroes.append(hero)
        
        for hero in other_team.heroes:
            living_opponents.append(hero)
        
        while len(living_heroes) > 0 and len(living_opponents) > 0:
            random_hero = random.choice(living_heroes)
            random_opponent = random.choice(living_opponents)

            random_hero.fight(random_opponent)

            if random_hero.is_alive():
                living_opponents.remove(random_opponent)
            else:
                living_heroes.remove(random_hero)


    

        
    

