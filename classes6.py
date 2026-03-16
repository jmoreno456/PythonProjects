# modeling real-world objects
# some approaches are more efficient than others, but it takes practice
# to find the most efficient representations.
# as you begin to model more complicated things like electric cars,
# you'll wrestle with interesting questions. is the range of an electric
# car a property of the battery or of the car? if we're only describing
# one car, it's probably fine to maintain the association of the method
# get_range() with the battery class. but if we're describing a
# manufacturer's entire line of cars, we probably want to move get_range()
# to the ElectricCar class. the get_range() method would still check the
# battery size before determining the range, but it would report a
# range specific to the kind of car it's associated with. alternatively,
# we could maintain the association of the get_range() method with the
# battery but pass it a parameter such as car_model. the get_range()
# method would then report a range based on the battery size and the
# car model.


# 9-6 ice cream stand: write a class called icecreamstand that inherits
# from the restaurant class. add an attribute called flavors that stores
# a list of ice cream flavors. write a method that displays these
# flavors. create an instance of incecreamstand, and call this method
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


class IceCreamStand(Restaurant):
    """add an attribute called flavors."""

    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ["chocolate", "vanilla", "strawberry"]

    def show_flavors(self):
        """Display the ice cream flavors."""
        print("The flavors of ice cream available are:")
        for flavor in self.flavors:
            print(f"{flavor.title()}")


# call the method
available_icecream = IceCreamStand("aurelios", "mexican")
available_icecream.show_flavors()


# 9-7 admin: write a class called admin that inherits from the user
# class you wrote in 9-5. add an attribute, privileges, that stores
# a list of strings like "can add post", "can delete post", "can ban user"
# write a method called show_privileges() that lists the administrator's
# set of privileges. create an instance of admin, and call your method
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


class Privileges:
    """an attribute that stores a list of strings"""

    def __init__(self, privileges):
        self.privileges = privileges

    def show_privileges(self):
        """display the privileges of an admin."""
        print("\nHere is a list of the privileges of an Admin:")
        for priv in self.privileges:
            print(f"{priv}")


class Admin(User):
    """add an attribute that stores a list of things an admin can do."""

    def __init__(self, first_name, last_name, age, hobby, height):
        super().__init__(first_name, last_name, age, hobby, height)
        privileges_list = [
            "can add post",
            "can delete post",
            "can ban user",
        ]
        self.privileges = Privileges(privileges_list)


# create instance
## my_privilege = Admin('Jesse', 'moreno', 20, 'soccer', 65)
## my_privilege.show_privileges()


# 9-8 privileges: write a separate privileges class. the class should
# have one attribute privileges, that stores a list of strings as
# described in 9-7. move the show_privilege() method to this class
# make a privileges instance as an attribute in the admin class. create
# a new instance of admin and use your method to show its privileges.
my_privileges = Admin("jesse", "moreno", 24, "video games", 66)
my_privileges.privileges.show_privileges()


# 9-9 battery upgrade: use the final version of electric car. add a
# method to the battery class called upgrade_battery(). this method
# should check the battery size and set the capacity to 65 if it isn't
# already. make an electric car with a default battery size, call get
# range once, and then call get_range() a second time after upgrading
# the battery. you should see an increase in the car's range.
class Car:
    """A simple attempt to represent a car"""

    def __init__(self, make, model, year):  # attribute
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):  # method
        """Return a neatly formatted descriptive name."""
        long_name = f"\n{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        """Print a statement showing the car's mileage."""
        print(f"This car has {self.odometer_reading} miles on it")

    # let's add a little logic to make sure no one tries to roll back
    # the odometer reading:
    def update_odometer(self, mileage):
        """Set the odometer reading to the given value.
        Reject the change if it attempts to roll the odometer back."""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading."""
        self.odometer_reading += miles


class Battery:
    """A simple attempt to model a battery for an electric car."""

    def __init__(self, battery_size=40):
        """Initialize the battery's attributes."""
        self.battery_size = battery_size

    def upgrade_battery(self):
        """Check the battery size and set the capacity to 65"""
        if self.battery_size != 65:
            print("I need to set the capacity to 65")
        else:
            self.battery_size

    def describe_battery(self):
        """Print a statement describing the battery size."""
        print(f"This car has a {self.battery_size}-kWh battery.")

    def get_range(self):
        """Print a statement about the range this battery provides."""
        if self.battery_size == 40:
            range = 150
        elif self.battery_size == 65:
            range = 225

        print(f"This car can go about {range} miles on a full charge.")


class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""

    def __init__(self, make, model, year):  # gets attributes from parent class
        """Initialize attributes of the parent class."""
        super().__init__(make, model, year)
        self.battery = Battery()  # create a new instance of battery


# instance
my_leaf = ElectricCar("nissan", "leaf", 2024)
my_leaf.battery.get_range()  # battery size is 40 - 150 miles
my_leaf.battery.battery_size = 65
my_leaf.battery.get_range()  # battery size is 65 - 225 miles
