import sqlite3

connect = sqlite3.connect("Clothes.db")
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


create_table()

def add_user(fio, age):
    cursor.execute('INSERT INTO users(fio, age) VALUES (?, ?)', (fio, age))
    connect.commit()
    print(f"User {fio} is added!")


add_user("John Doe", 25)
add_user("Peter Parker", 19)
add_user("Ivan Zolo", 23)

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
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Clothes(
        brand VARHCAR (100) NOT NULL,
        size TEXT,
        quantity INTEGER NOT NULL
    )
''')
connect.commit()

def add_cloth(brand, size, quantity):
    cursor.execute(
        'INSERT INTO Clothes(brand, size, quantity) VALUES (?, ?, ?)',
        (brand, size, quantity)
    )
    print("Added!")
    connect.commit()

add_cloth("ArmaniExchange", "L", 25)

def get_all_clothes():
    cursor.execute('SELECT * FROM Clothes')
    Clothes = cursor.fetchall()
    print(f"All clothes: {Clothes}")
    for i in Clothes:
        print(f"Brand: {i[0]}, Size: {i[1]}, Quantity: {i[2]}")

get_all_clothes()

def update_cloth(brand, rowid):
    cursor.execute(
        'UPDATE Clothes SET brand = ? WHERE rowid = ?',
        (brand, rowid)
    )
    print("Updated!")
    connect.commit()

update_cloth("Puma", 2)

def delete_cloth(rowid):
    cursor.execute('DELETE FROM Clothes WHERE rowid = ?', (rowid,))
    print("Cloth is deleted!")
    connect.commit()

delete_cloth(5)
"""
"""
nums = list(map(int, input().split()))
target = int(input())
for i in range(len(nums)):
    for j in range(i+1, len(nums)):
        if(nums[i] + nums[j] == target):
            print([i, j])
            exit()
"""
"""
def square_result(func):
    def wrapper(a, b):
        cur = func(a, b)
        return cur ** 2
    return wrapper

@square_result
def add(a, b):
    return a+b

print(add(2, 3))

def check_user(username):
    def decorator(func):
        def wrapper():
            if(username == 'admin'):
                func()
            else:
                print("Access denied. Only for admin")
        return wrapper
    return decorator

@check_user("admin")
def delete_database():
    print("Database deleted!")

@check_user("guest")
def delete_logs():
    print("Logs deleted!")

delete_database()
delete_logs()
"""
"""
from itertools import product

class Products:
    def __init__(self, name, price, stock):
        self.__name = name
        self.__price = price
        self.__stock = stock

    def get_info(self):
        return(print(f"Product: {self.__name}, Price: {self.__price}, In stock: {self.__stock}"))

    def buy(self, quantity):
        if(self.__stock < quantity):
            return False
        else:
            self.__stock -= quantity
            return True
    def get_name(self):
        return self.__name

    def get_price(self):
        return self.__price

class Cart:
    def __init__(self):
        self.products = []

    def add_product(self, name, quantity):
        if name.buy(quantity):
            self.products.append((name, quantity))
        else:
            print("Not enough products in the stock!")

    def checkout(self):
        total = 0
        for name, quantity in self.products:
            price = name.get_price()
            curname = name.get_name()
            cur = price * quantity
            total += cur
            print(f"Product: {curname}, {quantity} pcs. at {price} = {cur}")
        print(f"Total: {total}")

p1 = Products("Laptop", 50000, 10)
p2 = Products("Mouse", 1000, 50)
cart = Cart()
cart.add_product(p1, 2)
cart.add_product(p2, 5)
cart.checkout()
"""
"""
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
"""