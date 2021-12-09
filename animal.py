class Animal:
    def __init__(self, name: str) -> None:
        self.name = name
    
    def eat(self):
        print(f'{self.name} is eating')
    
    def drink(self):
        print(f'{self.name} is drinking')
    
class Frog(Animal):
    def jump(self):
        print(f'{self.name} is jumping')


if __name__ == '__main__':
    tiger = Animal('Tony')
    tiger.eat()
    tiger.drink()

    frog = Frog('Kirby')
    frog.eat()
    frog.drink()
    frog.jump()