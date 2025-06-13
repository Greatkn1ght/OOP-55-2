from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        # ...
        pass

    @abstractmethod
    def move(self):
        pass

class Dog(Animal):
    def make_sound(self):
        print("gaf gaf")

    def move(self):
        print("step")

gufi = Dog()
"""
# Encapsulation
import random
class BankAccount:

    def __init__(self, user_name, balance, password):
        self.user_name = user_name
        # protected
        self._balance = balance
        # private
        self.__password = password

    def get_balance(self):
        return self._balance

    def reset_password(self, new_one):
        self.__password = self.__generate_code()
        return self.__password

jack = BankAccount("Jack", 1000, 321123)
print(jack.user_name)
"""
"""
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
class Warrior(Hero, Power):
    def __init__(self, name, lvl, hp, st):
        super().__init__(name, lvl, hp)
        self.st = st
    def action(self):
        print(f"Warrior method!!!")

soldier = Warrior("solder 1", 5, 100, 50)
soldier.action()

# CamelCase
# snake_case
"""
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