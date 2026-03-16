# setting a default value for an attribute
# when an instance is created, attributes can be defined without being
# passed in as parameters. these attributes can be defined in the __init__ method()
# where they are assigned a default value
# let's add an attribute called odometer_reading that always starts with
# a value of 0. we'll also add a method read_odometer() that helps us
# read each car's odometer
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


my_new_car = Car("audi", "a4", 2024)  # instance
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()


# modifying attribute values
# you can change an attribute's value in three ways: you can change the
# value directly through an instance, set the value through a method, or
# increment the value (add a certain amount to it) through a method.


# modifying an attribute's value directly
# the simplest way to modify the value of an attribute is to access
# the attribute directly through an instance. here we set the odometer
# reading to 23 directly:
# sometimes you'll want to access attributes directly like this, but
# other times you'll want to write a method that updates the value for you
my_new_car.odometer_reading = 23
my_new_car.read_odometer()


# modifying an attribute's value through a method
# it can be helpful to have methods that update certain attributes for
# you. instead of accessing the attribute directly, you pass the new
# value to a method that handles the updating internally.
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

    # let's add a little logic to make sure no one tries to roll back
    # the odometer reading:
    def update_odometer(self, mileage):
        """Set the odometer reading to the given value.
        Reject the change if it attempts to roll the odometer back."""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def read_odometer(self):
        """Print a statement showing the car's mileage."""
        print(f"This car has {self.odometer_reading} miles on it")


my_new_car = Car("audi", "a4", 2024)  # instance
print(my_new_car.get_descriptive_name())

my_new_car.update_odometer(18)
my_new_car.read_odometer()


# incrementing an attribute's value through a method
# sometimes you'll want to increment an attribute's value by a certain
# amount, rather than set an entirely new value. say we buy a used car
# and put 100 miles on it between the time we buy it and the time we
# register it. here's a method that allows us to pass this incremental
# amount and add that value to the odometer reading:
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

    def read_odometer(self):
        """Print a statement showing the car's mileage."""
        print(f"This car has {self.odometer_reading} miles on it")


my_used_car = Car("subaru", "outback", 2019)
print(my_used_car.get_descriptive_name())

my_used_car.update_odometer(23_500)
my_used_car.read_odometer()

my_used_car.increment_odometer(100)
my_used_car.read_odometer()


# you can use methods like this to control how users of your program
# update values such as an odometer reading, but anyone with access to
# the program can set the odometer reading to any value by accessing the
# attribute directly. effective security takes extreme attention to detail
# in addition to basic checks like those shown here.
