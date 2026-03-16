# inheritance
# you don't always have to start from scratch when writing a class. if
# the class you're writing is a specialized version of another class
# you wrote, you can use inheritance. when one class inherits from another
# it takes on the attributes and methods of the first class. the original
# class is called the parent class, and the new class is the child class
# it can also define new attributes and methods of its own


# the __init__ method for a child class
# when you're writing a new class based on an existing class. you'll
# often want to call the __init__() method from the parent class. this
# will initialize any attributes that were defined in the parent __init__()
# method and make them available in the child class.
# let's model ElectricCar class on the car class
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


class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""

    def __init__(self, make, model, year):  # gets attributes from parent class
        """Initialize attributes of the parent class."""
        super().__init__(make, model, year)


my_leaf = ElectricCar("nissan", "leaf", 2024)
print(my_leaf.get_descriptive_name())


# the super() function is a special function that allows you to call a
# method from the parent class. the name super comes from a convention
# of calling the parent class a superclass and the child class a subclass


# defining attributes and methods for the child class
# you can attributes and methods necessary to differentiate the child
# class from the parent class.
class ElectricCar(Car):
    """Represents aspects of an electric vehicle"""

    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery_size = 40

    def describe_battery(self):
        """Print a statement describing the battery size."""
        print(f"This car has a {self.battery_size}-kWh battery.")


my_leaf = ElectricCar("nissan", "leaf", 2024)
my_leaf.describe_battery()


# overriding methods from the parent class
# you can ovveride any method from the parent class that doesn't fit
# what you're trying to model with the child class. to do this, you
# define a method in the child class with the same name as the method
# you want to ovveride in the parent class. python will disregard the
# parent class method and only pay attention to the method you define
# in the child class.


# instances as attributes
# you can break your large class into smaller classes that work together
# this approach is called composition.
# for example, if we continue adding detail to the ElectricCar class,
# we might notice that we're adding many attributes and methods specific
# to the car's battery. when we see this happening, we can stop and move
# those attributes and methods to a separate class called battery. then
# we can use a battery instance as an attribute in the ElectricCar class
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


my_leaf = ElectricCar("nissan", "leaf", 2024)
print(my_leaf.get_descriptive_name())
my_leaf.battery.describe_battery()
my_leaf.battery.get_range()
