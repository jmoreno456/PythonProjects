# 9-1 restaurant: make a class called restaurant. the __init__() method
# for restaurant should store two attributes: a restaurant_name and a
# cuisine_type. make a method called describe_restaurant() that prints
# these two pieces of information, and a method called open_restaurant()
# that prints a message indicated that the restaurant is open
class Restaurant:
    """Describe a restaurant and the food they serve."""

    def __init__(self, restaurant_name, cuisine_type):
        """Initialize attributes."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """Print two pieces of information."""
        print(f"\nThe restaurant is called {self.restaurant_name},")
        print(f"They are a {self.cuisine_type} restaurant.")

    def open_restaurant(self):
        """Print that the restaurant is open."""
        print(f"\n{self.restaurant_name} is now open.")


my_restaurant = Restaurant("Mr.Tequila", "Mexican")
my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()


# 9-2 three restaurants: create three different instances from the class
# and call describe_restaurant() for each instance
your_restaurant = Restaurant("A1", "Barbecue")
your_restaurant.describe_restaurant()
your_restaurant.open_restaurant()

his_restaurant = Restaurant("Different", "American")
his_restaurant.describe_restaurant()
his_restaurant.open_restaurant()

her_restaurant = Restaurant("Keto", "Healthy")
her_restaurant.describe_restaurant()
her_restaurant.open_restaurant()


# 9-3 users: make a class called user. create two attributes called
# first_name and last_name, and then create several other attributes
# that are typically stored in a user profile. make a method called
# describe_user() that prints a summary of the user's information. make
# another method called greet_user() that prints a personalized greeting
# to the user. create several instances representing different users,
# and call both methods for each user.
class User:
    """Create 5 attributes."""

    def __init__(self, first_name, last_name, age, hobby, height):
        """Initialize attributes."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.hobby = hobby
        self.height = height

    def describe_user(self):
        """Prints a summary of the user's information"""
        print(f"\n{self.first_name} {self.last_name} is {self.age} years old.")
        print(f"Their favorite hobby is: {self.hobby}.")
        print(f"Their height in inches is: {self.height}")

    def greet_user(self):
        """Personalized greeting to the user."""
        print(f"Hello {self.first_name} {self.last_name}, welcome!")


# create instances
my_user = User("Mark", "Hernandez", 20, "Video games", 67)
my_user.describe_user()
my_user.greet_user()

your_user = User("Caty", "Hurtz", 32, "Reading", 62)
your_user.describe_user()
your_user.greet_user()

first_user = User("Jesse", "Perez", 45, "Soccer", 70)
first_user.describe_user()
first_user.greet_user()


# working with classes and instances
# once you write a class, you'll spend most of your time working with
# instances created from that class. one of the first tasks you'll want
# to do is modify the attributes of an instance directly or write methods
# that update attributes in specific ways


# the car class
# our class will store information about the kind of car we're working
# with, and it will have a method that summarizes this information:
class Car:
    """A simple attempt to represent a car"""

    def __init__(self, make, model, year):  # attribute
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year

    def get_descriptive_name(self):  # method
        """Return a neatly formatted descriptive name."""
        long_name = f"\n{self.year} {self.make} {self.model}"
        return long_name.title()


my_new_car = Car("audi", "a4", 2024)  # instance
print(my_new_car.get_descriptive_name())
