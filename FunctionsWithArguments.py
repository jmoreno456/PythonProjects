## functions let you reuse code
## accept multiple arguements
## perform logic inside
## return a result to be used elsewhere


## 1. write a function called multiply that takes two numbers
## and returns their product
## 2. call the function with the numbers 6 and 7, and print the result

# def multiply(x, y):
# return x * y # ends the function and sends the result back to where the function waa called

# mul_result = multiply(6, 7)
# print(mul_result)


## returning multiple values from a function
## write a function get_full_name that takes in two arguments
## first_name and last_name, and returns both the full name (as a string)
## and the length of the full name (as an integer)

# def get_full_name(first_name, last_name):
# concatenate first and last names to create full name
# full_name = first_name + " " + last_name
# return the full name and its length
# return full_name, len(full_name)

# first_name = input("What is your first name: ")
# last_name = input("What is your last name: ")
# full_name, name_length = get_full_name(first_name, last_name)
# print(f"Full Name: {full_name}")
# print(f"Length: {name_length}")


## write a function check_temperature(temp)
## takes a temperature in fahrenheit as input
## prints: "It's cold!" if below 50, "It's moderate." if between
## 50 and 85, "It's hot!" if above 85
# def check_temperature(temp):
# if temp < 50:
# print("It's cold!")
# elif 50 <= temp <= 85:
# print("It's moderate.")
# else:
# print("It's hot!")
# return temp

# temp = int(input("What is your temp? "))
# check_temperature(temp)


## bonus: write a function student_feedback(name, subject, score)
## three arguments: name (string), subject (string), score(integer)
## prints feedback in the format
## "Alice's grade in Math: A - Excellent!" for 90+
## "Bob's grade in History: B - Good job." for 80–89
## "Carla's grade in Science: C - You passed." for 70–79
## "David's grade in English: D - Needs improvement." for 60–69
## "Eli's grade in Art: F - Failed." for below 60


# def student_feedback(name, subject, score):
# if score >= 90:
# print(f"{name}'s grade in {subject}: A - Excellent!")
# elif 80 <= score <= 89:
# print(f"{name}'s grade in {subject}: B - Good Job.")
# elif 70 <= score <= 79:
# print(f"{name}'s grade in {subject}: C -  You passed.")
# elif 60 <= score <= 69:
# print(f"{name}'s grade in {subject}: D - Needs improvement.")
# else:
# print(f"{name}'s grade in {subject}: F - Failed.")
# return name, subject, score


# name = input("What is your name: ")
# subject = input("What is your subject: ")
# score = int(input("What is your score: "))
# student_feedback(name, subject, score)


## practice
# def greet_user(name):
# return f"Welcome {name} !"


# message = greet_user("Jesse")
# print(message)


## bonus
# def average_score(scores):
# return sum(scores) / len(scores)

# scores = [80, 90, 70]
# result = average_score(scores)
# print(f"Result: {result:.0f}")


## bonus2
# def bmi_category(weight, height):
# bmi = weight / (height ** 2)
# if bmi < 18.5:
# print("Underweight")
# elif 18.5 <= bmi <= 24.9:
# print("Normal")
# elif 25 <= bmi <= 29.9:
# print("Overweight")
# else:
# print("Obese")
# return bmi

# bmi_category(58, 1.6)
