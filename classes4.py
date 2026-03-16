# 9-4 number served: start with your program from 9-1. add an attribute
# called number_served with a default value of 0. create an instance
# called restaurant from this class. print the number of customers the
# restaurant has served, and then change this value and print it again
class Restaurant:
    """Describe a restaurant and the food they serve."""

    def __init__(self, restaurant_name, cuisine_type):
        """Initialize attributes."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        """Print two pieces of information."""
        print(f"\nThe restaurant is called {self.restaurant_name.title()},")
        print(f"They are a {self.cuisine_type.title()} restaurant.")

    def open_restaurant(self):
        """Print that the restaurant is open."""
        print(f"\n{self.restaurant_name.title()} is now open.")

    def customers_served(self):
        """Print the number of customers served"""
        print(f"the restaurant has served {self.number_served} customers tonight.")


my_restaurant = Restaurant("aurelios", "mexican")
my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()
my_restaurant.customers_served()

my_restaurant = Restaurant("aurelios", "mexican")
my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()
my_restaurant.number_served = 80
my_restaurant.customers_served()


# add a method called set_number_served() that lets you set the
# number of customers that have been served. call this method with a new
# number and print the value again.
class Restaurant:
    """Describe a restaurant and the food they serve."""

    def __init__(self, restaurant_name, cuisine_type):
        """Initialize attributes."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        """Print two pieces of information."""
        print(f"\nThe restaurant is called {self.restaurant_name.title()},")
        print(f"They are a {self.cuisine_type.title()} restaurant.")

    def open_restaurant(self):
        """Print that the restaurant is open."""
        print(f"\n{self.restaurant_name.title()} is now open.")

    def set_number_served(self, people_served):
        """set the number of customers served"""
        if people_served > self.number_served:
            self.number_served = people_served
        else:
            print("The restaurant served at least one person!")

    def customers_served(self):
        """Print the number of customers served"""
        print(f"the restaurant has served {self.number_served} customers tonight.")


my_restaurant = Restaurant("aurelio", "mexican")
my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()
my_restaurant.set_number_served(45)
my_restaurant.customers_served()


# add a method called increment_number_served() that lets you increment
# the number of customers who've been served. call this method with any
# number you like that could represent how many customers were served
# say, in a day of business
class Restaurant:
    """Describe a restaurant and the food they serve."""

    def __init__(self, restaurant_name, cuisine_type):
        """Initialize attributes."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        """Print two pieces of information."""
        print(f"\nThe restaurant is called {self.restaurant_name.title()},")
        print(f"They are a {self.cuisine_type.title()} restaurant.")

    def open_restaurant(self):
        """Print that the restaurant is open."""
        print(f"\n{self.restaurant_name.title()} is now open.")

    def set_number_served(self, people_served):
        """set the number of customers served"""
        if people_served > self.number_served:
            self.number_served = people_served
        else:
            print("The restaurant served at least one person!")

    def increment_number_served(self, people):
        """add customers as they are served"""
        self.number_served += people

    def customers_served(self):
        """Print the number of customers served"""
        print(f"the restaurant has served {self.number_served} customers tonight.")


my_restaurant = Restaurant("aurelio", "mexican")
my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()
my_restaurant.set_number_served(45)
my_restaurant.increment_number_served(10)
my_restaurant.customers_served()


# 9-5 login attempts: add an attribute called login_attempts to your
# user class from 9-3. write a method called increment_login_attempts()
# that increments the value of login_attempts by 1. write another method
# called reset_login_attempts() that resets the value of login_attempts
# to 0. make an instance of the user class and call it increment_login_attempts()
# several times. print the value of login_attempts to make sure it was
# incremented properly, and then call reset_login_attempts(). print
# login_attempts again to make sure it was reset to 0
class User:
    """Create 5 attributes."""

    def __init__(self, first_name, last_name, age, hobby, height):
        """Initialize attributes."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.hobby = hobby
        self.height = height
        self.login_attempts = 0

    def describe_user(self):
        """Prints a summary of the user's information"""
        print(f"\n{self.first_name} {self.last_name} is {self.age} years old.")
        print(f"Their favorite hobby is: {self.hobby}.")
        print(f"Their height in inches is: {self.height}")

    def greet_user(self):
        """Personalized greeting to the user."""
        print(f"Hello {self.first_name} {self.last_name}, welcome!")

    def increment_login_attempts(self):
        """increment the value by 1."""
        self.login_attempts += 1

    def reset_login_attempts(self):
        """resets login attempts back to 0"""
        self.login_attempts = 0


# create instances
my_user = User("Jesse", "hernandez", 20, "soccer", 65)
my_user.describe_user()

# call increment_login_attempts() several times
my_user.increment_login_attempts()
my_user.increment_login_attempts()
my_user.increment_login_attempts()

# print the number of attempts
print(f"Login attempts: {my_user.login_attempts}")

# reset login attempts
my_user.reset_login_attempts()

# print login attempts again to make sure it was reset to 0
print(f"Login attempts: {my_user.login_attempts}")
