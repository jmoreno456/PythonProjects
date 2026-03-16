# importing classes
# as you add more functionality to your classes, your files can get long
# even when you use inheritance and composition properly. python lets
# you store classes in modules and then import the classes you need
# into your main program.


# the import statement tells python to pen the car module and import
# the class Car. now we can use the car class as if it were defined
# in this file. importing classes is an effective way to program.
# picture how long this program file would be if the entire car class
# were included. when you instead move the class to a module and import
# the module, you still get all the same functionality, but you keep your
# main program file clean and easy to read. you also store most of the
# logic in separate files


# storing multiple classes in a module
# you can store as many classes as you need in a single module, although
# each class in a module should be related somehow. the classes battery
# and electricCar both help represent cars, so let's add them to the
# module car.py, now we can make a new file called my_electric_car.py
# import the electricCar class, and make an electric car


# importing multiple classes from a module
# you can import as many classes as you need into a program file. if
# we want to make a regular car and an electric car in the same file,
# we need to import both classes car, and electriccar


# importing an entire module
# you can also import an entire module and then access the classes you
# need using dot notation. this approach is simple and results in code
# that is easy to read. because every call that creates an instance of
# a class includes the module name, you won't have naming conflicts
# with any names used in the current file.


# importing a module into a module
# sometimes you'll want to spread out your classes over several
# modules to keep any one file from growing too large and avoid
# storing unrelated classes in the same module. when you store your
# classes in several modules, you may find that a class in one module
# depends on a class in another module. when this happens, you can
# import the required class into the first module.
# for example, let's store the car class in one module and the electricCar
# and battery classes in a separate module. we'll make a new module called
# electric_car.py and copy the battery and electriccar classes into this module


# using aliases
# aliases can be quite helpful when using modules to organize your
# projects' code. you can use aliases when importing classes as well
# as an example, consider a program where you want to make a bunch of
# electric cars. it might get tedious to type (and read) ElectricCar
# over and over again. you can give ElectricCar an alias in the import
# statement: from electric_car import ElectricCar as EC
# my_leaf = EC('nissan', 'leaf', 2024)


# 9-10 imported restaurant: using your latest restaurant class, store
# it in a module. maqke a separate file that imports restaurant. make
# a restaurant instance, and call one of restaurant's methods to show
# that the import statement is working properly.


# 9-11 imported admin: start with your work from exercise 9-8. store
# the classes user, privileges, and admin in one module. create a
# separate file, make an admin instance, and call show_privileges()
# to show that everything is working correctly


# 9-12 multiple modules: store the user class in one module, and store
# the privileges and admin classes in a separate module. in a separate
# file, create an admin instance and call show_privileges() to show
# that everything is still working correctly


# the python standard library
# the python standard library is a set of modules included with every
# python installation. you can start to use modules like these that
# other programmers have written. let's look at one module, random,
# which can be useful in modeling many real-world situations. One
# interesting function from the random module is randint(). This function
# takes two integer arguments and returns a randomly selected integer
# between ( and including ) those numbers. here's how to generate a
# random number between 1 and 6:
from random import randint

print(randint(1, 6))


# another useful function is choice(). this function takes in a list or
# tuple and returns a randomly chosen element:
from random import choice

players = ["charles", "martina", "michael", "florence", "eli"]
first_up = choice(players)
print(first_up)


# the random module should not be used when building security-related
# applications, but it works well for many fun and interesting projects
# you can also download modules from external sources. you'll see a
# number of these examples in Part 2. where we'll need external modules
# to complete each project


# 9-13 dice: make a class die with one attribute called sides, which
# has a default value of 6. write a method called roll_dice() that prints
# a random number between 1 and the number of sides the die has. make
# a 6-sided dice and roll it 10 times. make a 10-sided die and a 20-sided
# die. roll each die 10 times.


# 9-14 lottery: make a list or a tuple containing a series of 10 numbers
# and 5 letters. randomly select 4 numbers or letters from the list and
# print a message saying that any ticket matching these 4 numbers or
# letters wins a prize.
from random import choice

# make a list random numbers and letters
numbers = [2, 5, 9, 10, 6, 3, 12, 24, 56, 30, "a", "c", "d", "f", "h"]

# make an empty list to hold winning ticket
winning_ticket = []
print("The winning ticket is...")

# create while loop to match winning ticket
while len(winning_ticket) < 4:
    random_item = choice(numbers)

    # only add one random item to the list, no repeats
    if random_item not in winning_ticket:
        print(f" we pulled a: {random_item}")
        winning_ticket.append(random_item)

# make a final print statement
print(f"The final winning ticket is: {winning_ticket}")


# 9-15 lottery analysis: you can use a loop to see how hard it might
# be to win the kind of lottery you just modeled. make a list or tuple
# called my_ticket. write a loop that keeps pulling numbers until your
# ticket wins. print a message reporting how many times the loop had
# to run to give you a winning ticket

# list of posibilities
random_list = [2, 5, 9, 10, 6, 3, 12, 24, 56, 30, "a", "c", "d", "f", "h"]

# my ticket
my_ticket = [5, 8, "a", 10]


# create function
def generate_ticket():
    """compare my ticket to the random choice from  random list"""
    ticket = []
    while len(ticket) < 4:
        chosen_element = choice(random_list)
        if chosen_element not in ticket:
            ticket.append(chosen_element)
    return ticket


# count the number of tries
tries = 0

while True:
    tries += 1
    winning_ticket = generate_ticket()
    if winning_ticket == my_ticket:
        break
    if tries > 10000:
        print("You did not win sorry")
        break

print(f"Tries: {tries} tries")
print(f"Winning ticket: {winning_ticket}")
