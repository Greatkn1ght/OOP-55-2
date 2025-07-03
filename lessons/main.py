import sqlite3

connect = sqlite3.connect("users.db")
cursor = connect.cursor()

def create_table():
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users(
            userid INTEGER PRIMARY KEY AUTOINCREMENT,
            fio VARCHAR (100) NOT NULL,
            age INTEGER NOT NULL
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS grades(
            gradeid INTEGER PRIMARY KEY AUTOINCREMENT,
            userid INTEGER, 
            subject VARCHAR (100) NOT NULL,
            grade INTEGER NOT NULL,
            FOREIGN KEY (userid) REFERENCES users(userid)
        )
    ''')
    connect.commit()

# create_table()

def add_user(fio, age):
    cursor.execute('INSERT INTO users(fio, age) VALUES (?, ?)', (fio, age))
    connect.commit()
    print(f"User {fio} is added!")

# add_user("John Doe", 25)
# add_user("Peter Parker", 19)
# add_user("Ivan Zolo", 23)

def add_grade(userid, subject, grade):
    cursor.execute(
        'INSERT INTO grades(userid, subject, grade) VALUES (?, ?, ?)',
        (userid, subject, grade)
    )
    print(f"Grade is added for user with ID {userid}")
    connect.commit()


def get_users_with_grades():
    cursor.execute('''
        SELECT users.fio, grades.subject, grades.grade
        FROM users INNER JOIN grades ON users.userid = grades.userid
    ''')
    rows = cursor.fetchall()
    for i in rows:
        print(f"FIO: {i[0]}, SUBJECT: {i[1]}, GRADE: {i[2]}")

# get_users_with_grades()

# AVG() - Average
# MAX() - Maximum
# MIN() - Minimum COUNT() SUM()
"""
def get_avg_age():
    cursor.execute('SELECT AVG(age) FROM users')
    avg_age = cursor.fetchall()
    print(avg_age)

get_avg_age()
"""
# def create_view_young_users():
#     cursor.execute('''
#         CREATE VIEW IF NOT EXISTS young_users AS
#         SELECT fio, age
#         FROM users
#         WHERE age <= 30
#     ''')
#     connect.commit()
#     print("View young_users is created!")

# create_view_young_users()

def create_view_Daniel():
    cursor.execute('''
            CREATE VIEW IF NOT EXISTS elder_users AS
            SELECT fio, age
            FROM users
            WHERE age >= 20
        ''')
    connect.commit()
    print("View elder_users is created!")

create_view_Daniel()

def get_from_view_Daniel():
    cursor.execute('SELECT * FROM elder_users')
    print(cursor.fetchall())

"""
import sqlite3

#A4 paper
connect = sqlite3.connect("users.db")
# Hand with pencil
cursor = connect.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS users(
        fio VARCHAR (100) NOT NULL,
        age INTEGER NOT NULL,
        hobby TEXT
    )
''')
connect.commit()

# CRUD = Create - Read - Update - Delete
def add_user(fio, age, hobby):
    cursor.execute(
        'INSERT INTO users(fio, age, hobby) VALUES (?, ?, ?)',
        (fio, age, hobby)
    )
    connect.commit()

add_user('peter parker', 23, "Rescue")

def get_all_users():
    cursor.execute('SELECT * FROM users')
    users = cursor.fetchall()
    print(f"ALL users: {users}")
    for i in users:
        print(f"FIO: {i[0]}, AGE: {i[1]}, HOBBY: {i[2]}")

get_all_users()

# Update

def update_user(fio, rowid):
    cursor.execute(
        'UPDATE users SET fio = ? WHERE rowid = ?',
        (fio, rowid)
    )
    connect.commit()

update_user("Ivan Zolo", 2)

# Delete
def delete_user(rowid):
    cursor.execute('DELETE FROM users WHERE rowid = ?', (rowid,))
    connect.commit()
"""
"""
# requests - for working with HTTP requests
import requests
response = requests.get("https://api.github.com")
print(response.json())

#pandas - for working with tables and data
import pandas as pd
data = {
    "Name": ["Arzybek", "Adilet", "Aziza"],
    "Age": [25, 30, 22]
}
df = pd.DataFrame(data)
print(df)

#matplotlib - for plotting graphs
import matplotlib.pyplot as plt
x = [1, 2, 3, 4, 5]
y = [2, 5, 7, 10, 12]

plt.plot(x, y, label="Growth", marker='o')
plt.title("Example Plot")
plt.xlabel("Time")
plt.ylabel("Value")
plt.legend()
plt.grid(True)
plt.show()

#beautifulsoup4 = for HTML parsing
import requests
from bs4 import BeautifulSoup

response = requests.get("https://example.com")
soup = BeautifulSoup(response.text, "html.parser")

title = soup.title.text
print("Page title: ", title)

for p in soup.find_all("p"):
    print("Paragraph:", p.text)
# Big o notation - way of describing comlexity of algorithm.

# O(1) - constant
# O(n) - linear
# O(n^2) - squared
"""
"""
def find_element(arr, elem):
    for i in arr:
        if(i == elem):
            return(print(f"{i}"))
    return(print("There is no such a number"))
my_list = [1, 23, 4, 54, 5, 67, 658]
find_element(my_list, 4)

# O(log n)
def binary_search(arr, target):
    l, r = 0, len(arr) - 1
    while(l <= r):
        mid = (l+r) >> 1
        print(mid)
        if(arr[mid] == target):
            return print(mid)
        elif arr[mid] < target:
            l = mid+1
        else:
            r = mid-1
    return print("There no such a number")
my_array = [1, 3, 5, 7, 9, 11, 13]
binary_search(my_array, 7)
# Modul - main.py all files with extension .py
# from HW/hw import square_result
# @square_result
# def ok(a, b):
#     return a+b
# print(ok)
# Packets = file which contains many moduls
"""
"""
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __eq__(self, other):
        return "Not equal"

    def __gt__(self, other):
        return "Correct"

    def __lt__(self, other):
        return "Correct ls"

a = Vector(10, 20)
b = Vector(5, 1)
c = a < b

class Customlist:
    def __init__(self, items):
        self.items = items

    def __setitem__(self, key, value):
        return print("Our text")

    def __delitem__(self, key):
        print("Not going to delete!")
        
    # def __call__(self, *args, **kwargs):
    # def __exit__(self, exc_type, exc_val, exc_tb):   
    
    
my_list = Customlist([1, 23, 15, 8, 0])
my_list[1] = 25
del my_list[2]
# Magic methods
# (or dunder-methods, from "underscore")
"""
"""
class Hero:
    def __init__(self, name, hp, lvl=None):
        self.name = name
        self.lvl = lvl

    def __str__(self):
        return "Our text"

hero = Hero("Bob", 100, 10)
print(hero)
"""
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