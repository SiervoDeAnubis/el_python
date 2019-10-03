# A class is like a blueprint for creating objects. An object has properties and methods(functions) associated with it. Almost everything in Python is an object

# Create class user


class User:
    # Constructor
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age

    def greeting(self):
        return f'My name es {self.name} and I am {self.age}'

    def has_birthday(self):
        self.age += 1

# Customer class


class Customer(User):
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age
        self.balance = 0

    def set_balance(self, balance):
        self.balance = balance

    def greeting(self):
        return f'My name is {self.name} and I owe a balance of {self.balance}'

# Init user obejct


cesar = User('Cesarin', 'omnislahs@hotmail.com', 35)
yesenia = User('yesenia', 'omnislahs@hotmail.com', 35)

# Edit property
cesar.age = 36

print(cesar.name)

yesenia.has_birthday()

# Call method

print(yesenia.greeting())

# Init customer


john = Customer('john', 'el_email@some.com', 40)

john.set_balance(500)

print(john.greeting())
