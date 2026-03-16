# making an argument optional
# soemtimes it makes sense to make an argument optional, so that people
# using the function can choose to provide extra information only if
# they want to
# you can use default values to make an argument optional
# to make the middle name optional, we can give the middle name argument
# an empty default value and ignore the argument unless the user provides
# a value
# to get this function to work without a middle name, we set the default
# value of middle name to an empty string and move it to the end
def get_formatted_name(first_name, last_name, middle_name=""):
    """Return a full name, neatly formatted."""
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"

    return full_name.title()


musician = get_formatted_name("john", "hooker", "lee")
print(musician)

musician = get_formatted_name("john", "hooker")
print(musician)


# since there is always a first and last name, these parameters are
# listed first. the middle name is optional so it is listed last in
# the definition and its default value is an empty string
# if using a middle name, it must line up with the calling line, so
# python will match up the positional arguments correctly


# returning a dictionary
# a function can return any kind of value you need it to, including
# more complicated data structures like lists and dictionaries
def build_person(first_name, last_name):
    """Return a dictionary of information about a person"""
    person = {"first": first_name, "last": last_name}
    return person


musician = build_person("jimi", "hendrix")
print(musician)


# you can easily extend this function to accept optional values like
# middle name, an age, an occupation, or any other information you
# want to store about a person
# the following example, allows you to store a person's age as well:
def build_person(first_name, last_name, age=None):
    """Return a dictionary of information about a person."""
    person = {"first": first_name, "last": last_name}
    if age:
        person["age"] = age
    return person


musician = build_person("jimi", "hendrix", age=27)
print(musician)


# the special value None is used when a variable has no specific value
# assigned to it. None is a placeholder value. in conditional tests
# none evaluates to false.


# using a function with a while loop
## def get_formatted_name(first_name, last_name):
## """Return a full name, neatly formatted."""
## full_name = f"{first_name} {last_name}"
## return full_name.title()

## while True:
## print("\nPlease tell me your name:")
## print("(enter 'q' at any time to quit)")

## f_name = input("First name: ")
## if f_name == 'q':
## break

## l_name = input("Last name: ")
## if l_name == 'q':
## break

## formatted_name = get_formatted_name(f_name, l_name)
## print(f"\nHello, {formatted_name}")


# 8-6 city names: write a function called city_country() that takes in
# the name of a city and its country. the function should return a string
# formatted like this: "santiago, chile"
# call your function with at least three city-country pairs, and print
# the values that are returned
def city_country(city_name, country_name):
    """list the name of a city and its country"""
    city_country = f"{city_name}, {country_name}"
    return city_country.title()


get_city_country = city_country("madrid", "spain")
print(get_city_country)

get_city_country = city_country("santiago", "chile")
print(get_city_country)

get_city_country = city_country("tampa", "usa")
print(get_city_country)


# 8-7 album: write a function called make_album() that builds a dictionary
# describing a music album. the function should take in an artist name
# and an album title, and it should return a dictionary containing
# these two pieces of information. use the function to make three
# dictionaries representing different albums. print each return value
# to show that the dictionaries are storing the information correctly
# use none to add an optional parameter thay allows you to store the
# number of songs on an album. if the calling line includes a value for
# the number of songs, add that value to the album's dictionary. make
# at least one new function call that includes the number of songs
def make_album(artist_name, album_title, num_songs=None):
    """Detail description of an album"""
    album = {"artist": artist_name, "album": album_title}

    if num_songs:
        album["songs"] = num_songs
    return album


album_description = make_album("drake", "take care")
print(album_description)

album_description = make_album("travis scott", "utopia")
print(album_description)

album_description = make_album("pop smoke", "meet the woo")
print(album_description)

album_description = make_album("drake", "take care", num_songs=18)
print(album_description)


# 8-8 user albums: write a while loop that allows users to enter an
# album's artist and title. once you have that information, call the
# function with the user's input and print the dictionary that's
# created. be sure to include a quit value in the while loop
def make_album(artist_name, album_title):
    """Detail description of an album"""
    album = {"artist": artist_name, "album": album_title}

    return album


while True:
    print(
        "\nEnter the name of an artist, "
        "along with the name of their album(your favorite):"
    )
    print("Enter 'quit' when done:")

    a_name = input("What is the name of the artist: ")
    if a_name == "quit":
        break

    a_title = input("What is the name of their album: ")
    if a_title == "quit":
        break

    album_final = make_album(a_name, a_title)
    print(album_final)
