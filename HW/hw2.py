class Heroes:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp

    def action(self):
        print(f"{self.name} will destroy you!!!")

    def attack(self):
        print(f"{self.name} will kill youuu!!!")

class Archer(Heroes):
    def __init__(self, name, hp, arrows, precision):
        super().__init__(name, hp)
        self.arrows = arrows
        self.precision = precision

    def attack(self):
        self.arrows -= 1
        if(self.arrows//2 >= self.precision):
            print(f"{self.name} gonna destroy you with {self.arrows} arrows!")
        else:
            print(f"It's your lucky day!")

    def rest(self):
        self.arrows += 5
        print("You have replenished with 5 arrows")

    def status(self):
        print(f"{self.name}, {self.hp}, you have {self.arrows} arrows and you precision is {self.precision}")

hero = Archer("Peter", 100, 51, 25)
hero.attack()
hero.rest()
hero.status()