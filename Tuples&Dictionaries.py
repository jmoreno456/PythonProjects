## two essential data structures
## Tuples
## A tuple is like a list, but its immutable
## you can't change it once its created
# my_tuple = ("apple", "banana", "cherry")
# print(my_tuple[1]) # Output: banana
## why use tuples?
## tuples are faster than lists
## they're used when data should not be changed
## for example: coordinates, RGB colors


## Dictionaries
## a dictionary stores data in key-value pairs.
## think of it like a mini-database
# my_dict = {"name": "Jesse", "age": 28, "is_student": True}

# print(my_dict["name"])  # Output: Jesse
## why use dictionaries?
## extremely useful for structured data
## keys are unique identifiers; values hold the actual data


## 1. create a tuple with 3 of your favorite colors and
## print the second color
# new_tuple = ("green", "blue", "red")
# print(new_tuple[1])
## 2. try to change one of the items in the tuple and see what happens
# new_tuple[1] = "purple"  # tuple does not support item assignment


## 3. create a dictionary with keys: name, age, and language.
## fill in your own values
# new_dict = {"name": "Jesse", "age": 24, "language": "English"}
## print the value of the language key
# print(new_dict["language"])
## add a new key-value pair to your dictionary: "hobby": "coding"
# new_dict["hobby"] = "coding"
# print(new_dict)


## dictionary keys can be numbers
# scores = {1: "Beginner", 2: "Intermediate"}
# print(scores[1])  # Outputs: Beginner


## get() does not add the key - it tries to retrieve it
## if the key does not exist, it returns the default value you provide
# user = {"name": "Ana", "city": "Boston"}
# print(user.get("age", "Not found"))  # Output: Not found
# the dictionary stays unchanged


## Bonus
## write a dictionary called movie with keys:
## title, year, rating and then print a sentence like
## I watched inception (2010) and rated it 9/10
# movie = {"title": "Inception", "year": 2010, "rating": "9/10"}
## use single quotes in f string when accessing dictionary
## use parenthesis around curly brackets to get value
## inside of parenthesis
# print(f'I watched {movie["title"]} ({movie["year"]}) and rated it {movie["rating"]}')


## Bonus
## nested dicitonary and loop
## you are given a dictionary where each key is a username
## and the value is another dictionary
## with their age and favorite language
# users = {
# "jesse24": {"age": 24, "language": "Python"},
# "sara_code": {"age": 27, "language": "JavaScript"},
# "dev_lee": {"age": 30, "language": "Go"},
# }
## 1. loop through each user in the users dictionary
## 2. print a sentence like:
## "User jesse24 is 24 years old and loves Python"
# for username, info in users.items():  # loops through both keys and values
# age = info["age"]
# language = info["language"]
# print(f"User {username} is {age} years old and loves {language}.")

## get only the first username and their details
# first_username, first_info = next(iter(users.items()))  # not a loop
# print(
# f"User {first_username} is {first_info['age']} years old and loves {first_info['language']}."
# )


## Bonus
## create a dictionary called students with 3 students.
## each student should have a name(key), and a nested dictionary
## with grade and major
## then use a loop to print
## NAME has a grade of GRADE and is studying MAJOR
# students = {
# "Adam": {"grade": "A", "major": "Biology"},
# "Sara": {"grade": "A+", "major": "Nursing"},
# "Jesse": {"grade": "A", "major": "Data Science"},
# }

# for student_name, info in students.items():
# print(
# f"{student_name} has a grade of {info['grade']} and is studying {info['major']}"
# )


# person = {"name": "Jesse", "age": 28, "job_hunting": True}

# person["weight"] = 127.8
# person["age"] = 29
# person.pop("job_hunting")
# print(person)

# if "age" in person:
# print("Age is known")

# for key, value in person.items():
# print(key, value)


## example
# car = {"brand": "Toyota", "model": "Camry", "year": 2020}

# car["color"] = "black"
# car.pop("model")

# print(car)


## practice: contact book
# contacts = {}
# n = int(input("Enter the number of entries: "))

# for _ in range(n):
# key = input("Enter a name: ")
# value = input("Enter a phone number: ")
# contacts.update({key: value})

# print(contacts)


## bonus: dictionary analyzer
student_major = {
    "Jesse": "Data Science",
    "Tyler": "Computer science",
    "Mary": "Biology",
    "Teresa": "Biomedical Engineering",
    "Tom": "Sports Medicine",
}

print(len(student_major))
print(list(student_major.keys()))
print(list(student_major.values()))

if "Mary" in student_major:
    print("Exists")
