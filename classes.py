# object oriented programming (OOP) is one of the most effective approaches
# to writing software. IN OOP you write classes that represent real-world
# things and situtations, and you create objects based on these classes
# when you write a class, you define the general behavior that a whole
# category of objects can have. when you create individual objects from
# the class, each object is automatically equipped with the general
# behavior; you can then give each object whatever unique traits you
# desire.


# making an object from a class is called instantiation, and you work
# with instances of a class. you'll write classes and create instances
# of those classes. you'll specify the kind of information that can be
# stored in instances, and you'll define actions that can be taken with
# these instances. you'll also write classes that extend the functionality
# of existing classes, so similar classes can share common functionality
# you'll store your classes in modules and import classes written by
# other programmers into your own program files.


# learning about OOP will help you see the world as a programmer does
# it will help you understand your code--not just what's happening
# line by line, but also the bigger concepts behind it. knowing the
# logic behind classes will train you to think logically, so you can
# write programs that effectively address almost any problem you encounter


# creating and using a class
# you can model almost anything using classes. let's write a simple class
# Dog, that represents a dog, any dog. what do we know about most pet
# dogs? they all have a name and an age. we also know that most dogs
# sit and roll over. those two pieces of information (name and age) and
# those two behaviors (sit and roll over) will go in our dog class


# creating the dog class
# we first define a class called Dog
# a function that's part of a class is a method. the __init__() method
# the __init__() method is a sepcial method that python runs automatically
# whenever we create a new instance based on the Dog class.
# the self parameter must be included in the definition because when
# python calls this method later (to create an instance of Dog), the method
# call will automatically pass the self argument.
class Dog:
    """A simple attempt to model a dog."""

    def __init__(self, name, age):
        """Initialize name and age attributes."""
        self.name = name  # attributes
        self.age = age  # attributes

    def sit(self):  # method
        """Simulate a dog sitting in response to a command."""
        print(f"{self.name} is now sitting.")

    def roll_over(self):  # method
        """Simulate rolling over in response to a command."""
        print(f"{self.name} rolled over!")


# variables that are accessible through instances like this are called
# attributes
# these methods don't need additional information to run, we just define
# them to have one parameter, self. the instances we create later will
# have access to these methods.


# making an instance from a class
# think of a class as a set of instructions for how to make an instance
# let's make an instance representing a specific dog:
my_dog = Dog("Willie", 6)  # calls __init__() method in Dog

print(
    f"My dog's name is {my_dog.name}"
)  # use dot notation to access attribute of an instance
print(
    f"My dog is {my_dog.age} years old."
)  # use dot notation to access attribute of an instance


# calling methods
# after we create an instance from the class Dog, we can use dot notation
# to call any method defined in Dog
my_dog.sit()  # my_dog is the instance
my_dog.roll_over()


# creating multiple instances
# you can create as many instances from a class as you need
your_dog = Dog("Lucy", 3)

print(f"\nMy dog's name is {my_dog.name}")
print(f"My dog is {my_dog.age} years old.")
my_dog.sit()

print(
    f"\nYour dog's name is {your_dog.name}"
)  # use dot notation to access attribute of an instance
print(f"Your dog is {your_dog.age} years old.")
your_dog.sit()
