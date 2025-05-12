## exception handling with custom classes
## a useful skill for building robust programs


## concept
## you can define your own error types by creating a class that
## inherits from exception


class TooColdError(Exception):
    pass


def check_temperature(temp):
    if temp < 0:
        raise TooColdError("Temperature is below freezing!")
    else:
        print("Temperature is fine.")


try:
    check_temperature(0)
except TooColdError as e:
    print("Custom Error:", e)


## practice
## 1. write a function register_user(age) that raises this error if
## age < 13
## 2. catch and print a friendly message if the error is raised


class TooYoungError(Exception):
    pass


def register_user(age):
    if age < 13:
        raise TooYoungError("You are too young to participate!!!")
    else:
        print("You are old enough to participate.")


try:
    register_user(8)
except TooYoungError as e:
    print("Custom Error:", e)


## bonus
## add a loop so that the user can try again until they enter a valid
## age (13 or older), and only then exit
## while True:
## a try/except inside the loop
## a break when the input is valid


class TooYoungError(Exception):
    pass


def register_user(age):
    if age < 13:
        raise TooYoungError("You are too young to participate!!!")
    else:
        print("You are old enough to participate.")


while True:
    try:
        age = int(input("Enter your age: "))
        register_user(age)
        break
    except TooYoungError as e:
        print("Custom Error:", e)
    except ValueError:
        print("Please enter a valid number.")


## bonus: custom login exception
## 1. defines a custom exception called LoginError
## 2. prompts the user to enter a username
## 3. if the username is not "admin", raise the LoginError with the
## message "Invalid username!"
## 4. if it correct, print "Access granted"
## use a try/except block to handle the error and display the
## custom message


class LoginError(Exception):
    pass


def user_name(user):
    if user != "admin":
        raise LoginError("Invalid Username!")
    else:
        print("Access granted!")


while True:
    try:
        user = input("Enter your username: ")
        user_name(user)
        break
    except LoginError as e:
        print("Custom Error: ", e)
