## Functions let you reuse code, organize logic, and write
## cleaner programs
## every real-world app is built with lots of them


## defining a function
# def greet():
# print("Hello there!")
## def means your're defining a function
## greet() is the function name
## () is where arguments would go (if needed)


## calling a function
# greet() # this will print "Hello there!"


## functions with parameters
# def greet_person(name):
# print(f"Hello, {name}!")
## now you can pass a name
# greet_person("Jesse")


## returning values
# def add(x, y):
# return x + y
## this function gives back a result
# sum_result = add(3, 5)
# print(sum_result)


## write a function called favorite_food() that
## 1. takes one argument (the food)
## 2. prints: "My favorite food is ___"
# def favorite_food(food):
# print(f"My favorite food is {food}")
# favorite_food("Pizza")


## even without a print statement
## the function still stores and gives back a value
## it will be stored in the variable


## Bonus
## write a function called convert_temp() that:
## takes one argument: temp_f (a temperature in fahrenheit)
## converts it to celsius using this formula (temp - 32) * 5/9
## returns the celsius value
## then call the function with a value and print the result

# def convert_temp(temp_f):
# return (temp_f - 32) * 5/9
# temp_result = convert_temp(71)
# print(temp_result)


## Bonus
## create a function is_even() that:
## takes one argument, a number
## returns True if the number is even, and False if it's odd


## implicit return
def is_even(number):
    return number % 2 == 0  # evaluates to True or False


result = is_even(4)
print(result)