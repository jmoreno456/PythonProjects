## Python Modules and Importing
## A module is just a file containing python code that can define,
## functions, variables, and classes.
## many built-in modules you can use like math and random
## why use modules?
## reuse code across multiple files
## keep your programs
## use built-in tools and libraries


## 1. Import the math module
# import math
## 2. use math.sqrt() to find the square root of 144
# sqrt1 = math.sqrt(144)
# print(round(sqrt1))
## 3. use math.pi to print the value of pi
# pie1 = math.pi
# print(pie1)
## 4. use math.pow(2, 3) to raise 2 to the power of 3
# pow1 = math.pow(2, 3)
# print(round(pow1))
## try importing random and printing a random number between 1 and 10
# import random
# num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(random.choice(num))
## from math import sqrt
## can use sqrt function without importing math


## Bonus
## write a program that
## 1. asks the user to input a number
## 2. uses math.sqrt() to compute the square root
## 3. uses maith.ceil() to round the result up to the nearest whole number
## 4. prints both the original square root and the rounded-up version
# import math

# number = int(input("Pick any number to be squared: "))
# sqrt1 = math.sqrt(number)
# sqrt2 = math.ceil(sqrt1)
# print(f"Original number: {sqrt1}")
# print(f"Rounded up version: {sqrt2}")


## working with dates and times in Python
## using datetime module
## Python's built-in datetime module helps you handle dates,
## times, and timestamps
# import datetime
# get the current date and time
# now = datetime.datetime.now()
# print(now)
# get just the date
# today = datetime.date.today()
# print(today)
# create a specific date
# birthday = datetime.date(1999, 12, 25)
# print(birthday)
# format a date
# print(birthday.strftime("%B %d, %Y")) # December 25, 1999
## common strftime() format codes
## %Y - year (e.g., 2025)
## %m - month (01-12)
## %d - day (01-31)
## %B - full month name
## %A - weekday name


## practice
## 1. prints today's date
## 2. prints the current time (hours and minutes)
## 3. creates your next birthday (use any date)
## 4. Prints how many days are left until your next birthday
# import datetime

# today = datetime.date.today()
# current_time = datetime.datetime.now().time()
# fcurrent_time = current_time.strftime("%H:%M:%S")
# nbirthday = datetime.date(2025, 7, 31)

# days_left = (nbirthday - today).days

# print(f"Today's date is: {today}, The current time is: {fcurrent_time}, Your next birthday is: {nbirthday}")
# print(f"Days left until your next birthday: {days_left}")


## example
# import random

# num = random.randint(1, 100)
# print("Random number:", num)


## quiz
# import math

# print(math.floor(3.8))


## practice
# import math

# num = int(input("Enter a number: "))

# print("The square root is:", math.sqrt(num))
# print("The result after ceil is:", math.ceil(num))
# print("The factorial is:", math.factorial(num))


## bonus: simple number guessing game
# import random

# user_guess = int(input("Guess the random number (1-10): "))
# rand_num = random.randint(1, 10)

# if user_guess == rand_num:
# print("You guessed correctly!!")
# else:
# print("Try again")


## practice
# import math

# try:
# num = float(input("Enter a positive number: "))

# if num < 0:
# print("Factorial and square root are not definded for negative numbers")
# else:
# print(f"Square Root: {math.sqrt(num):.2f}")
# print(f"Ceiling: {math.ceil(num)}")
# print(f"Floor: {math.floor(num)}")
# if num.is_integer():
# print(f"Factorial: {math.factorial(int(num))}")
# else:
# print("Factorial is not definded by non-integers")
# except ValueError:
# print("Enter a valid number")


## bonus
import random


def guessing_game():
    rand_num = random.randint(1, 10)
    attempts = 0

    while True:
        try:
            guess = int(input("Guess the number (1-10): "))
            attempts += 1

            if guess < 1 or guess > 10:
                print("Stay within the range 1-10 please")
            elif guess < rand_num:
                print("Too Low. Try again")
            elif guess > rand_num:
                print("Too High. Try again")
            else:
                print(f"Correct! you guessed it in {attempts} tries :)!")
                break
        except ValueError:
            print("Enter a valid number")


while True:
    guessing_game()
    again = input("Play again? (y/n): ").strip().lower()
    if again != "y":
        print("Thanks for playing")
        break
