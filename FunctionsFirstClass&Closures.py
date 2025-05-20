## functions are first-class objects
## you can assign them to variables
## pass them as arguments
## return them from other functions


## assigning a function to a variable
def greet(name):
    return f"Hello, {name}!"


say_hello = greet  # assigning the function to a new name
print(say_hello("Kai"))


## passing a function as an argument
def shout(text):
    return text.upper()


def whisper(text):
    return text.lower()


def speak(func, message):
    return func(message)


print(speak(shout, "hi there"))
print(speak(whisper, "HI THERE"))


## returning a function (Closure)
def multiplier(factor):
    def multiply(x):
        return x * factor

    return multiply  # returns a function


double = multiplier(2)
triple = multiplier(3)

print(double(5))
print(triple(4))
## a closure
## the returned function multiply remembers the value of
## factor from when it was created


## practice
## define a function greet_maker(greeting) that returns a function
## which adds the name to the greeting
def greet_maker(greeting):
    def greeter(name):
        return f"{greeting}, {name}"

    return greeter


hello = greet_maker("Hello")
print(hello("Zara"))


## write a function apply_twice(func, x) that applies a function
## func to x, twice
def apply_twice(func, x):
    return func((func(x)))


def square(n):
    return n * n


print(apply_twice(square, 2))
## call the function two times
## python's functional flexibility
## functions can be passed, returned, assigned


## bonus: custom filter function with closure
## write a function make_filter(min_value) that returns a function
## which takes a list of numbers and returns only the values greater
## than or equal to min_value
def make_filter(min_value):
    def numbers(nums):
        return list(filter(lambda x: x >= min_value, nums))

    return numbers


filter10 = make_filter(10)
print(filter10([4, 10, 12, 8, 20]))

filter5 = make_filter(5)
print(filter5([1, 3, 5, 7, 9]))