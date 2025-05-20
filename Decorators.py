## A decorator is a special function that takes another function as
## input and extends or modifies its behavior, without changing its code
## python functions are first-class citizens
## closures remember the original function


## example: logging decorator
def log_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with arguments {args} {kwargs}")
        result = func(*args, **kwargs)
        print(f"{func.__name__} returned {result}")
        return result

    return wrapper


@log_decorator
def add(x, y):
    return x + y


add(3, 5)
## @log_decorator automatically wraps the add() function
## the original add() remains unchanged
## this pattern is heavily used in logging, timing, authentication


## practice
## create a decorator called shout_decorator that turns the return
## value of a function into uppercase and add "!!!" at the end
def shout_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result.upper() + "!!!"

    return wrapper


@shout_decorator
def greet(name):
    return f"hello {name}"


print(greet("kai"))


## what will this print
def my_decorator(func):
    def wrapper():
        print("Before")
        func()
        print("After")

    return wrapper


@my_decorator
def say_hello():
    print("Hello")


say_hello()
## Before
## Hello
## After
## decorators wrap functions to add or modify behavior
## function = decorator_name(functioon)


## bonus timing decorator
## write a decorator called timing_decorator that measures and prints
## the time it takes for a function to run
import time


def timing_decorator(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        duration = end - start
        print(f"Function {func.__name__} took {duration:.2f} seconds")
        return result

    return wrapper


@timing_decorator
def slow_add(a, b):
    time.sleep(1)
    return a + b


# print(slow_add(3, 5))


## bonus: count calls decorator
## write a decorator called count_calls that counts and prints
## how many times a function has been called
## use a variable to track how many times the function is called
## print the call count and the function name each time it runs
## still run the original function and return its result if needed
def count_calls(func):
    def wrapper(*args, **kwargs):
        wrapper.count += 1
        print(f"Call {wrapper.count} to {func.__name__}")
        return func(*args, **kwargs)

    wrapper.count = 0
    return wrapper


@count_calls
def greet(name):
    print(f"Hello, {name}!")


greet("Zara")
greet("Kai")
greet("Luna")
