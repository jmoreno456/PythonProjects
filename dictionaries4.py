# a list in a dictionary
# it's sometimes useful to put a list inside a dictionary


# store information about a pizza being ordered
pizza = {"crust": "thick", "toppings": ["mushrooms", "extra cheese"]}

# summarize the order
print(f"You ordered a {pizza['crust']}-crust pizza " "with the following toppings:")

for topping in pizza["toppings"]:
    print(f"\t{topping}")


# favorite languages using lists within a dictionary
favorite_languages = {
    "jen": ["python", "rust"],
    "sarah": ["c"],
    "edward": ["rust", "go"],
    "phil": ["python", "haskell"],
}

for name, languages in favorite_languages.items():
    if len(languages) < 2:
        print(f"\n{name.title()}'s favorite language is:")
        for language in languages:
            print(f"\t{language.title()}")
    else:
        print(f"\n{name.title()}'s favorite languages are:")
        for language in languages:
            print(f"\t{language.title()}")


# a dictionary in a dictionary
users = {
    "aeinstein": {"first": "albert", "last": "einstein", "location": "princeton"},
    "mcurie": {"first": "marie", "last": "curie", "location": "paris"},
}

for username, user_info in users.items():
    print(f"\nUsername: {username}")
    full_name = f"{user_info['first']} {user_info['last']}"
    location = user_info["location"]

    print(f"\tFull name: {full_name.title()}")
    print(f"\tLocation: {location.title()}")


# 6-7 people: start with the program from 6-1, make two new dictionaries
# representing different people, and store all three dictionaries
# in a list called people. loop through your list of people, as you loop
# through the list, print everything you know about each person
person1 = {"first": "jesse", "last": "moreno", "age": 21, "city": "tampa"}
person2 = {"first": "sarah", "last": "moore", "age": 18, "city": "new york city"}
person3 = {"first": "amy", "last": "sanchez", "age": 34, "city": "miami"}

people = [person1, person2, person3]

for person in people:
    print(person)


# 6-8 pets: make several dictionaries, where each dictionary represents
# a different pet. in each dictionary, include the kind of animal and
# the owner's name. store these dictionaries in a list called pets.
# next, loop through your list and as you do, print everything you
# know about each pet
pet1 = {"animal": "dog", "owner": "marco"}
pet2 = {"animal": "cat", "owner": "katie"}
pet3 = {"animal": "hamster", "owner": "ariana"}

pets = [pet1, pet2, pet3]

for pet in pets:
    print(f"\n{pet['owner'].title()} owns a {pet['animal'].title()}")


# 6-9 favorite places: make a dictionary called favorite_places. think
# of three names to use as keys in the dictionary, and store one to three
# favorite places for each person. loop through the dictionary, and print
# each person's name and their favorite places
favorite_places = {
    "jesse": ["gym", "universal studios", "new york city"],
    "sarah": ["mall", "starbucks"],
    "ariana": ["target", "sephora", "waterparks"],
}

for name, places in favorite_places.items():
    print(f"\nHi my name is {name.title()} and my favorite places to visit are:")
    for place in places:
        print(f"\t{place.title()}")


# 6-10 favorite numbers: each person can have more than one favorite number
# then print each person's name along with their favorite numbers
favorite_numbers = {
    "karen": [4, 5, 8],
    "ryan": [2, 1, 3],
    "kasey": [10, 8, 9],
    "jenny": [5, 6],
    "tyler": [4, 8],
}

for name, numbers in favorite_numbers.items():
    print(f"{name.title()}'s favorite numbers are:")
    for number in numbers:
        print(f"\t{number}")


# 6-11 cities: use the names of three cities as keys in your dictionary
# create a dictionary of information about each city and include the
# country that the city is in, its approximate population, and one fact
# about that city. the keys for each city's dictionary should be something
# like country, population, and fact. print the name of each city and
# all of the information you have stored about it
cities = {
    "new york city": {
        "country": "united states of america",
        "population": "eight million",
        "fact": "over 800 spoken languages",
    },
    "miami": {
        "country": "united states of america",
        "population": "five hundred thousand",
        "fact": "known as gateway to latin america",
    },
    "austin": {
        "country": "united states of america",
        "population": "nine hundred thousand",
        "fact": "live music capital of the world",
    },
}

for city, city_info in cities.items():
    print(f"City: {city.title()}")
    print(f"\tCountry: {city_info['country'].title()}")
    print(f"\tPopulation: {city_info['population']}")
    print(f"\tFact: {city_info['fact']}")
