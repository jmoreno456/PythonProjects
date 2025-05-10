## Composition: "Has-A" Relationships
## In python, composition means one class contains another class
## this lets you build more complex, realistic models


## example: A car has an engine
class Engine:
    def __init__(self, horsepower):
        self.horsepower = horsepower

    def start(self):
        print(f"Engine with {self.horsepower} HP started.")


class Car:
    def __init__(self, brand, horsepower):
        self.brand = brand
        self.engine = Engine(horsepower)  # Car *has an* Engine

    def drive(self):
        self.engine.start()
        print(f"The {self.brand} is now driving.")


my_car = Car("Toyota", 200)
my_car.drive()
## Car uses Engine as part of its structure
## self.engine = Engine(horsepower) creates a composition
## This promotes modularity and code reuse


## practice: build a computer that has a processor
## 1. create a processor class with:
## an attribute: speed (in GHz)
## a method: specs() that prints the speed
## 2. create a computer class with:
## an attribute: brand
## a processor objects as a member (e.g. self.processor = Processor(speed))
## a method: show_details() that prints the brand and calls the specs()
## method of the processor
## 3. create a computer object and call show_details()


class Processor:
    def __init__(self, speed):
        self.speed = speed

    def specs(self):
        print(f"The speed of your processor is {self.speed}GHz")


class Computer:
    def __init__(self, brand, speed):
        self.brand = brand
        self.processor = Processor(speed)

    def show_details(self):
        self.processor.specs()
        print(f"You bought an {self.brand} computer processor")


computer1 = Computer("Intel", 4.0)
computer1.show_details()


## extended computer class with RAM and Storage
class Processor:
    def __init__(self, speed):
        self.speed = speed


def specs(self):
    print(f"The speed of your processor is {self.speed}GHz")


class RAM:
    def __init__(self, size):
        self.size = size


def specs(self):
    print(f"RAM size: {self.size}GB")


class Storage:
    def __init__(self, capacity):
        self.capacity = capacity


def specs(self):
    print(f"Storage capacity: {self.capacity}TB")


class Computer:
    def __init__(self, brand, speed, ram_size, storage_capacity):
        self.brand = brand
        self.processor = Processor(speed)
        self.ram = RAM(ram_size)
        self.storage = Storage(storage_capacity)


def show_details(self):
    self.processor.specs()
    self.ram.specs()
    self.storage.specs()
    print(f"You bought an {self.brand} computer processor")


computer1 = Computer("Intel", 4.0, 16, 2)
computer1.show_details()


## extended code with user input
class Processor:
    def __init__(self, speed):
        self.speed = speed


def specs(self):
    print(f"The speed of your processor is {self.speed}GHz")


class RAM:
    def __init__(self, size):
        self.size = size


def specs(self):
    print(f"RAM size: {self.size}GB")


class Storage:
    def __init__(self, capacity):
        self.capacity = capacity


def specs(self):
    print(f"Storage capacity: {self.capacity}TB")


class Computer:
    def __init__(self, brand, speed, ram_size, storage_capacity):
        self.brand = brand
        self.processor = Processor(speed)
        self.ram = RAM(ram_size)
        self.storage = Storage(storage_capacity)


def show_details(self):
    self.processor.specs()
    self.ram.specs()
    self.storage.specs()
    print(f"You bought an {self.brand} computer processor")


brand = input("Enter the brand of your computer: ")
speed = float(input("Enter processor speed in GHz: "))
ram_size = int(input("Enter RAM size in GB: "))
storage_capacity = float(input("Enter storage capacity in TB: "))

computer1 = Computer(brand, speed, ram_size, storage_capacity)
computer1.show_details()


## bonus computer inventory system
## create a program that lets the user enter details for multiple
## computers, stores them in a list, and then displays all
## computers' details at the end
## 1. use a loop to collect details for each computer
## 2. after each entry, ask the user if they want to add another computer
## 3. store each computer as an object in a list
## 4. at the end, loop through the list and call show_details() for each one


class Processor:
    def __init__(self, speed):
        self.speed = speed


def specs(self):
    print(f"Processor speed: {self.speed}GHz")


class RAM:
    def __init__(self, size):
        self.size = size


def specs(self):
    print(f"RAM size: {self.size}GB")


class Storage:
    def __init__(self, capacity):
        self.capacity = capacity


def specs(self):
    print(f"Storage capacity: {self.capacity}TB")


class Computer:
    def __init__(self, brand, speed, ram_size, storage_capacity):
        self.brand = brand
        self.processor = Processor(speed)
        self.ram = RAM(ram_size)
        self.storage = Storage(storage_capacity)


def show_details(self):
    print(f"\nComputer Details:")
    print(f"Brand: {self.brand}")
    self.processor.specs()
    self.ram.specs()
    self.storage.specs()


# create empty list
computers = []

# create loop for list
while True:
    brand = input("Enter the brand of your computer (type done for exit): ")
    speed = float(input("Enter processor speed (GHz): (type done for exit) "))
    ram = int(input("Enter RAM size (GB) (type done for exit): "))
    storage = int(input("Enter storage size (type done for exit): "))

    # create object
    computer = Computer(brand, speed, ram, storage)
    computers.append(computer)

    another = input("Add another computer? (yes/no): ").lower()
    if another != "yes":
        break

print("\nComputer Inventory:")
for comp in computers:
    comp.show_details()