# looping through a dictionary's keys in a particular order
# one way to do this is to sort the keys as they have returned in the for loop
favorite_languages = {"jen": "python", "sarah": "c", "edward": "rust", "phil": "python"}

for name in sorted(favorite_languages.keys()):
    print(f"{name.title()}, thank you for taking the poll.")


# looping through all values in a dictionary
favorite_languages = {"jen": "python", "sarah": "c", "edward": "rust", "phil": "python"}

print("The following languages have been mentioned:")
for language in favorite_languages.values():
    print(language.title())


# to see a list without repetition use a set
# when you see braces but no key-value pairs, it is a set
# sets do not retain items in any specific order
favorite_languages = {"jen": "python", "sarah": "c", "edward": "rust", "phil": "python"}

print("The following languages have been mentioned:")
for language in set(favorite_languages.values()):
    print(language.title())


# 6-4 glossary 2: clean up the code from exercise 6-3 by replacing
# your series of print() statements with a loop.
# add five more terms to your glossary
glossary = {
    "lists": "a list uses square brackets and is mutable",
    "tuples": "a tuple is immutable",
    "dictionary": "a dictionary uses key-value pairs",
    "strings": "are characters",
    "if statements": "are conditional tests",
    "sets": "when you see braces without key-value pairs",
    "for loop": "iterates through a list, dictionary",
    "oop": "uses classes to deswcribe a person, place, or thing",
    "while loop": "loops until a condition is no longer met",
    "functions": "perform specific tasks",
}

print("\nHere are ten terms and their definitions:")
for key, value in glossary.items():
    print(f"{key.title()}: {value}")


# 6-5 rivers: make a dictionary containing three major rivers and the
# country each river runs through.
# use a loop to print a sentence about each river
# use a loop to print the name of each river included in the dictionary
# use a loop to print the name of each country included in the dictionary
rivers = {"nile": "egypt", "amazon": "brazil", "mississippi": "america"}

print("\n")
for river, country in rivers.items():
    print(f"The {river.title()} river runs through {country.title()}")

for river in rivers.keys():
    print(f"{river.title()}")

for country in rivers.values():
    print(f"{country.title()}")


# 6-6 polling: make a list of people who should take the favorite languages
# poll. include some names that are already in the dictionary and some
# that are not
# loop through the list of people who should take the poll. if they
# have, print a message thanking them for responding
# if they have not invite them to take the poll
favorite_languages = {"jen": "python", "sarah": "c", "edward": "rust", "phil": "python"}

people = ["jen", "sarah", "ariana", "ashlynn"]

for name in people:
    if name in favorite_languages:
        print(f"Hello {name.title()}, thanks for taking the poll.")
    else:
        print(f"Hello {name.title()}, please take my poll.")


# nesting: sometimes you will want to store multiple dictionaries in
# a list
# or a list of items as a value in a dictionary
# you can nest dictionaries inside a list, a list of items inside a dictionary,
# or even a dictionary inside another dictionary


# a list of dictionaries
alien_0 = {"color": "green", "points": 5}
alien_1 = {"color": "yellow", "points": 10}
alien_2 = {"color": "red", "points": 15}

aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
    print(alien)


# a more realistic example
# make an empty list for storing aliens
aliens = []

# make 30 green aliens
for alien_number in range(30):
    new_alien = {"color": "green", "points": 5, "speed": "slow"}
    aliens.append(new_alien)

# when it's time to change colors, we can use a for loop and an if
# statement to change the color of the aliens
for alien in aliens[:3]:
    if alien["color"] == "green":
        alien["color"] = "yellow"
        alien["speed"] = "medium"
        alien["points"] = 10

# show the first 5 aliens
for alien in aliens[:5]:
    print(alien)
print("...")

# show how many aliens have been created
print(f"Total number of aliens: {len(aliens)}")
