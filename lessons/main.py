# Inheritance
# Polymorphism

class Power:
    def __init__(self, power1, power2):
        self.power1 = power1
        self.power2 = power2
# Parent class / Super class
class Hero:

    def __init__(self, name, lvl, hp):
        self.name = name
        self.lvl = lvl
        self.hp = hp

    def action(self):
        print(f"{self.name} action")

# Child class / Inherited class
class warrior(Hero, Power):
    def __init__(self, name, lvl, hp, st):
        super().__init__(name, lvl, hp)
        self.st = st
    def action(self):
        print(f"Warrior method!!!")

soldier = warrior("solder 1", 5, 100, 50)
soldier.action()
"""
class hero:
    # class constructor
    def __init__(self, name: str = 'dawg', lvl: int = "1", hp: int = 0):
        # class attributes
        self.name = name
        self.lvl = lvl
        self.hp = hp
    # class methods
    def base_action(self):
        return f'{self.name} base action, {self.hp}'

# class objects \\ class instances
spiderman =hero(lvl = 100, name='Peter')
print(spiderman.base_action())
"""