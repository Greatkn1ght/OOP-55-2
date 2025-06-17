"""
def class_decorator(cls):
    class NewClass(cls):
        def new_method(self):
            return "New method!"

    return NewClass

@class_decorator
class MyClass:
    def old_method(self):
        return "Old method"

obj = MyClass()
print(obj.old_method())
print(obj.new_method())
print(obj)
"""
"""
# Decorators with parameters
def repeat(n):
    def decorator(func):
        def wrapper():
            for i in range(n):
                func()
        return wrapper
    return decorator

@repeat(5)
def hello():
    print("Sup, bro!")
hello()
"""
"""
def my_decorator(func):
    def wrapper():
        print("Before using function")
        func()
        print("After using function")

    return wrapper

@my_decorator
def hello():
    print("Hi, man")

hello()
"""
"""
import logging
class Circle:
    n = logging.info("!!!")
    def __init__(self, radius):
        self.__radius = radius

    @property
    def get_radius(self):
        return self.__radius

    @property
    def area(self):
        return 3.14 * self.__radius

circle = Circle(5)
# print(circle._Circle__radius)
print(circle.get_radius)
print(circle.area)
"""
"""
class Math:
    # class attribute
    sum = 122
    
    def __init__(self, num):
        # instance class attribute
        self.num = num
    @staticmethod
    def add(a, b):
        return a+b

    @classmethod
    def get_sum(cls):
        # cls = super()
        return cls.sum

print(Math.sum)
"""
"""
class A:
    def test_method(self):
        return "Class A"

class B(A):
    def test_method(self):
        return super().test_method()
        # return "Class B"

class C(A):
    def test_method(self):
        return super().test_method()

class D(B, C):
    pass
    # def test_method(self):
    #     return "Class D"

a = B()
print(B.__mro__)
"""
"""
class Animal:
    def make_sound(self):
        return "sound"

class Flyable:
    def move(self):
        return "flies"

class Swimable:
    def move(self):
        return "swims"

class Duck(Animal, Flyable, Swimable):
    pass

don = Duck()
print(Duck.__mro__)
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