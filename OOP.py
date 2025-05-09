## Object-Oriented Programming
## an essential concept for building structured and reusable code
## OOP is a programming paradigm based on objects
## which combines data (attributes) and
## functions(methods) into a single unit


## class: a blueprint for creating objects
## object: an instance of a class
## attributes: variables that hold data related to the object
## methods: functions that belong to a class


## example
class Dog:
    def __init__(self, name, age):  # Constructor method
        self.name = name  # Attribute
        self.age = age  # Attribute


def bark(self):
    print(f"{self.name} says woof!")


# creating an object
my_dog = Dog("Buddy", 3)
# accessing attributes and methods
print(my_dog.name)  # Output: Buddy
my_dog.bark()  # Output: Buddy says woof!


## practice
## 1. create a car class with brand and year attributes
## 2. add a method start() that prints "Brand is starting!"
## 3. create an object of Car and call the method


class Car:
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year


def start(self):
    print(f"{self.brand} ({self.year}) is starting!")


my_car = Car("BMW", 2022)
my_car.start()


## __init__ is the constructor used to initialize object attributes
## self refers to the current instance of the class, not the main method
## self gives acces to instance variables and methods
## A class is a blueprint; an object is an instance of that blueprint


## bonus
## 1. create a class Dog
## 2. attributes: name, age
## 3. method: speak() that prints:
## "Woof! My name is <name> and I am <age> years old."
## create an instance of Dog and call the speak() method
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age


def speak(self):
    print(f"Woof! My name is {self.name} and I am {self.age} years old")


my_dog = Dog("Gohan", 3)
my_dog.speak()
