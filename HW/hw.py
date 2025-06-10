class Person:
    def __init__(self, name, age, city):
        self.name = name
        self.age = age
        self.city = city

    def introduce(self):
        print(f"Hello, my name is {self.name}, my age is {self.age}, my city"
              f" is {self.city}")

    def is_adult(self):
        return (self.age >= 18)

human = Person("Bob", 19, "London")
human_1 = Person("Jake", 16, "Bermingham")
human_2 = Person("Micheal", 11, "Chicago")
print(human.is_adult(), human_1.is_adult(), human_2.is_adult(), sep='\n')