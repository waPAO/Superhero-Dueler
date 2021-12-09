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
    

        
    

