# passing an arbitrary number of arguments
# sometimes you won't know ahead of time how many arguments a function
# needs to accept. python allows a function to collect an arbitrary
# number of arguments from the calling statements.
# for example, consider a function that build a pizza. it needs to
# accept a number of toppings, but you cannot know ahead of time how
# much toppings a customer will want. the function in the following
# example has one parameter, *toppings, but this parameter collects
# as many arguments as the calling line provdes:
def make_pizza(*toppings):
    """Print the list of toppings that have been requested."""
    print(toppings)


make_pizza("pepperoni")
make_pizza("mushrooms", "green peppers", "extra cheese")


# the asterisk in the parameter name *toppings tells python to make a
# tuple called toppings, containing all values this function recieves


# now we can replace the print() call with a loop that runs through
# the list of toppings
def make_pizza(*toppings):
    """Summarize the pizza we are about to make."""
    print("\nMaking a pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")


make_pizza("pepperoni")
make_pizza("mushrooms", "green peppers", "extra cheese")


# mixing positional and arbitrary arguments
# if you want a function to accept several different kinds of arguments
# the parameter that accepts an arbitrary number of arguments must be
# placed last in the function definition. python matches positional
# and keyword arguments first and then collects any remaining arguments
# in the final parameter
# you'll often see the generic parameter name *args, which collects
# arbitrary positional arguments like this
def make_pizza(size, *toppings):
    """Summarize that we are about to make a pizza"""
    print(f"\nMaking a {size}-inch pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")


make_pizza(16, "pepperoni")
make_pizza(12, "mushrooms", "green peppers", "extra cheese")


# using arbitrary keyword arguments
# sometimes you'll want to accept an arbitrary number of arguments,
# but you won't know ahead of time what kind of information will be passed
# to the function. in this case, you can write functions that accept as
# many key-value pairs as the calling statement provides. one example
# involves building user profiles: you know you'll get information about
# a user, but you're not sure what kind of information you'll recieve.
# the following the example always takes in a first and last name, but
# it accepts an arbitrary number of keyword arguments as well:
def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    user_info["first_name"] = first
    user_info["last_name"] = last
    return user_info


user_profile = build_profile(
    "albert", "einstein", location="princeton", field="physics"
)
print(user_profile)


# the definition of build_profile() expects a first and last name, and
# then it allows the user to pass in as many name-value pairs as they want
# the double asterisks before the parameter **user_info cause python to
# create a dictionary called user_info containing all the extra name-value
# pairs the function recieves.
# you'll often see the parameter name **kwargs used to collect nonspecific
# keyword arguments


# 8-12 sandwiches: write a function that accepts a list of items a
# person wants on a sandwich. the function should have one parameter
# that collects as many items as the function call provides, and it
# should print a summary of the sandwich that's being ordered. call
# the function three times, using a different number of arguments
# each time.
def make_sandwich(*toppings):
    """print summary of the sandwich"""
    print(toppings)


make_sandwich("lettuce")
make_sandwich("tomatoes", "mayo", "cheese")
make_sandwich("ham", "peppers")


# 8-13 user profile: build a profile of yourself by calling build_profile()
# using your first and last names and thrre other key-value pairs that
# describe you
def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    user_info["first_name"] = first
    user_info["last_name"] = last
    return user_info


user_profile = build_profile(
    "jesse",
    "rodriguez",
    location="new york",
    field="data science",
    hobby="playing soccer",
)
print(user_profile)


# 8-14 cars: write a function that stores information about a car in a
# dictionary. the function should always recieve a manufacturer and
# a model name. it should then accept an arbitrary number of keyword
# arguments. call the function with the required information and two
# other name-value pairs, such as a color or an optional feature. your
# function should work for a call like this one:
# car = make_car('subaru', 'outback', color='blue', tow_package=True)
# print the dictionary that's returned to make sure all the information
# was stored correctly
def make_car(make_name, model_name, **car_info):
    """build your car"""
    car_info["make"] = make_name
    car_info["model"] = model_name

    return car_info


car = make_car("subaru", "outback", color="blue", tow_package=True)
print(car)
