# def outer():
# def inner():
# print("I'm inside the outer function!")
# inner()

# outer()


## example
# def greet():
# name = "Jesse"

# def say_hello():
# print(f"Hello, {name}!")  # uses outer variable

# say_hello()  # enclosing scope


# greet()


## quiz
# def outer():
# message = "Hi"

# def inner():
# print(message)

# inner()

# outer()


## practice
# def outer_function():
# language = "Python"

# def inner_function():
# print(f"I love programming in {language}!")

# inner_function()


# outer_function()


## Bonus
# Define a global variable
# count = 10


# def change_count():
# global count # use global count to change the global variable inside the function or python will create a new local variable
# count += 10
# print("Inside the function:", count / 2)


# change_count()
# print("Outside the function:", count)


## bonus2
# def make_multiplier(n):
# def inner(x):
# return n * x
# return inner

# double = make_multiplier(5)
# print(double(5))


## bonus3
def make_greeter(name):
    def inner():
        print(f"Hello {name}, have a great day !")

    return inner


hello_jesse = make_greeter("Jesse")
hello_jesse()
