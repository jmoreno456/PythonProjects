# using get() to access values
# using keys in square brackets to retrieve the value from a certain
# dictionary might cause one potential problem,
# if the key you ask for doesn't exist, you will get a KeyError
# for dictionaries, you can use the get() method to set a default value
# that will be returned if the requested key does not exist
alien_0 = {"color": "green", "speed": "slow"}

point_value = alien_0.get("points", "No point value assigned.")
print(point_value)


# 6-1 person: use a dictionary to store information about a person
# store their first name, last name, age, and city
# print each piece of information stored in your dictionary
person = {"first_name": "jesse", "last_name": "moreno", "age": 22, "city": "tampa"}

print(person)
print(
    f"Hello, I am {person['first_name'].title()} {person['last_name'].title()}, I am {person['age']} years old, and I live in {person['city'].title()}, FL."
)


# 6-2 favorite numbers: use a dictionary to store people's favorite numbers
# think of five names, think of a favorite number, print each person'name
# and their favorite number.
favorite_numbers = {"karen": 6, "ryan": 7, "kasey": 10, "jenny": 2, "tyler": 4}

number = favorite_numbers["jenny"]
print(f"Jenny's favorite number is {number}")


# 6-3 glossary: think of five programming words you've learned about
# in the previous chapters. use these words as the keys in your glossary
# and store their meanings as values
# print each word and its meanings as neatly formatted output
glossary = {
    "lists": "a list uses square brackets and is mutable",
    "tuples": "a tuple is immutable",
    "dictionary": "a dictionary uses key-value pairs",
    "strings": "are characters",
    "if statements": "are conditional tests",
}

print(f"Lists: {glossary['lists'].title()}")
print(f"Tuples: {glossary['tuples'].title()}")
print(f"Dictionaries: {glossary['dictionary'].title()}")
print(f"Strings: {glossary['strings'].title()}")
print(f"If Statements: {glossary['if statements'].title()}")


# looping through a dictionary
# you can loop through all of a dictionary's key-value pairs
# through its keys
# or through its values


# looping through all key-value pairs
# use a dictionary to store one person's username, first name, and last name
user_0 = {"username": "efermi", "first": "enrico", "last": "fermi"}


# to see everything stored in this user's dictionary
# loop through the dictionary using a for loop
for key, value in user_0.items():
    print(f"\nKey: {key}")
    print(f"Value: {value}")


# the method items() returns a sequence of key-value pairs


favorite_languages = {"jen": "python", "sarah": "c", "edward": "rust", "phil": "python"}

for name, language in favorite_languages.items():
    print(f"{name.title()}'s favorite language is {language.title()}.")


# looping through all keys in a dictionary
# the keys() method is useful when you don't need all values in a dictionary
favorite_languages = {"jen": "python", "sarah": "c", "edward": "rust", "phil": "python"}

for name in favorite_languages.keys():
    print(name.title())


# example: when name matches one of our friends display a message
favorite_languages = {"jen": "python", "sarah": "c", "edward": "rust", "phil": "python"}

friends = ["phil", "sarah"]
for name in favorite_languages.keys():
    print(f"Hi {name.title()}")

    if name in friends:
        language = favorite_languages[name].title()
        print(f"\t{name.title()}, I see you love {language}!")


# you can use the keys() method to find a particular person
favorite_languages = {"jen": "python", "sarah": "c", "edward": "rust", "phil": "python"}

if "erin" not in favorite_languages.keys():
    print("Erin, please take our poll!")