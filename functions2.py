# default values
# when writing a function, you can define a default value for each parameter
# if an argument for a parameter is provided in the function call, python
# uses the argument value. if not, it uses the parameter's default value
# when you use default values, any parameter with a default value needs
# to be listed after all the parameters that don't have default values
def describe_pet(pet_name, animal_type="dog"):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}")


# equivalent function calls
# because positional arguments, keyword arguments, and default values
# can all be used together, you'll often have several equivalent ways
# to call a function. consider the following definition for describe_pet()
# with one default value provided


# a dog named willie.
describe_pet("willie")
describe_pet(pet_name="willie")

# a hamster named harry
describe_pet("harry", "hamster")
describe_pet(pet_name="harry", animal_type="hamster")
describe_pet(animal_type="hamster", pet_name="harry")


# avoiding argument errors
# when you start to use functions, don't be surprised if you encounter
# errors about unmatched arguments.
# unmatched arguments happen when you provide fewer or more arguments
# than a function needs to do its work
# typeError appears


# 8-3 t-shirt: write a function called make_shirt() that accepts a size
# and the text of a message that should be printed on the shirt. the
# function should print a sentence summarizing the size of the shirt and
# the message printed on it. call the function once using positional
# arguments to make a shirt. call the function a second time using
# keyword arguments
def make_shirt(shirt_size, shirt_text):
    """Display the shirt size and text"""
    print(f"\nThe size of the shirt is a: {shirt_size.title()}")
    print(f"The message on the shirt: {shirt_text.title()}")


make_shirt("large", "rock on")  # positional arguments
make_shirt(shirt_size="medium", shirt_text="never give up")  # keyword argument


# 8-4 large shirts: modify the make_shirt() function so that shirts
# are large by default with a message that reads i love python. make
# a large shirt and a medium shirt with the default message, and a
# shirt of any size with a different message
def make_shirt(shirt_size="large", shirt_text="i love python"):
    """Display the shirt size and text"""
    print(f"\nThe size of the shirt is a: {shirt_size.title()}")
    print(f"The text on the shirt: {shirt_text.title()}")


make_shirt()  # default size and message
make_shirt("medium")  # changing default shirt size parameter
make_shirt("small", "this is a small shirt")  # changing both default parameters


# 8-5 cities: write a function called describe_city() that accepts the
# name of a city and its country. the function should print a sentence
# such as reykjavik is in iceland. give the parameter for the country
# a default value. call your function for three different cities, at
# least one of which is not in the default country
def describe_city(city_name, city_country="united states"):
    """Display the city and country in a sentence"""
    print(f"\n{city_name.title()} is in {city_country.title()}")


describe_city("miami")
describe_city(city_name="madrid", city_country="spain")
describe_city(city_name="new york city")


# return values
# a function doesn't always have to display its output directly
# it can process some data and then return a value or set of values
# the value the function returns is called a return value
# the return statement takes a value from inside a function and sends it
# back to the line that called the function
# return values allow you to move much of your program's grunt work
# into functions, which can simplify the body of your program


# returning a simple value
# when you call a function that returns a value, you need to provide
# a variable that the return value can be assigned to
def get_formatted_name(first_name, last_name):
    """Return a full name, neatly formatted"""
    full_name = f"{first_name} {last_name}"
    return full_name.title()


musician = get_formatted_name("jimi", "hendrix")
print(musician)
