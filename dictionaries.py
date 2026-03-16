# consider a game featuring aliens that can have different colors
# and point values
# this simple dictionary stores information about a particular alien
# the dictionary alien_0 stores the alien's color and points value
# the last two lines access and display that information
alien_0 = {"color": "green", "points": 5}

print(alien_0["color"])  # green
print(alien_0["points"])  # 5


# a dictionary in python is a collection of key-value pairs
# each key is connected to a value
# and you can use a key to access the value associated with that key
# a key's value can be a number, string, a list, or another dictionary
# you can use any object that you can create in python as a value
# in a dictionary


# to get the value associated with a key, give the name of the
# dictionary and then place the key inside square brackets


# if a player shoots down this alien, you can look up how many points
# they should earn using code like this:
alien_0 = {"color": "green", "points": 5}

new_points = alien_0["points"]
print(f"You just earned {new_points} points!")


# adding new key-value pairs
# dictionaries are dynamic structures and you can add new key-value
# pairs to a dictionary at any time
# to add a new key-value pair, give the name of the dictionary
# followed by the new key in square brackets, along with the new value
alien_0 = {"color": "green", "points": 5}
print(alien_0)

alien_0["x_position"] = 0
alien_0["y-position"] = 25
print(alien_0)


# starting with an empty dictionary
# define a dictionary with an empty set of braces and then add each
# key-value pair on its own line
# you will use empty dictionaries when storing user-supplied data
# or when writing code that generates a large number of key-value
# pairs automatically
alien_0 = {}

alien_0["color"] = "red"
alien_0["points"] = 4

print(alien_0)


# modifying values in a dictionary
# to modify a value in a dictionary, give the name of the dictionary
# with the key in square brackets and then the new value
alien_0 = {"color": "yellow"}
print(f"The alien is {alien_0['color']}")

alien_0["color"] = "green"
print(f"The alien is now {alien_0['color']}")


# track the position of an alien that can move at different speeds
alien_0 = {"x-position": 0, "y-postion": 25, "speed": "medium"}
print(f"Original position: {alien_0['x-position']}")

# move the alien to the right
# determine how far to move the alien based on its current speed
if alien_0["speed"] == "slow":
    x_increment = 1
elif alien_0["speed"] == "medium":
    x_increment = 2
else:  # this must be a fast alien
    x_increment = 3

# the new position is the old position plus the increment
alien_0["x-position"] = alien_0["x-position"] + x_increment

print(f"New position: {alien_0['x-position']}")


# removing key-value pairs
# use the del statement to completely remove a key-value pair
# all del needs is the name of the dictionary and the key that you
# want to remove
# the deleted key-value pair is deleted permanently
alien_0 = {"color": "purple", "points": 6}
print(alien_0)

del alien_0["points"]
print(alien_0)


# a dictionary of similar objects
favorite_languages = {"jen": "python", "sarah": "c", "edward": "rust", "phil": "python"}

language = favorite_languages["sarah"].title()
print(f"Sarah's favorite language is {language}")