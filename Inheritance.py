## Inheritance is a key feature of object oriented programming
## it lets one class (child) inherit the properties and
## behaviors of another (parent)
## reduces code repetition
## allows child class to use methods and attributes from a
## parent class


## example
class Animal:
    def __init__(self, name):
        self.name = name


def speak(self):
    print(f"{self.name} makes a sound.")


class Dog(Animal):  # Dog inherits from Animal
    def speak(self):
        print(f"{self.name} says woof!")


## you can override parent methods like speak()


## practice
## 1. create a person class with name and age
## 2. add a method introduce() that prints:
## "Hi, I'm [name] and I'm [age] years old"
## 3. create student class that inherits from person
## 4. add a new attribute school to student
## 5. override introduce() to include the school:
## "Hi, I'm [name], I'm [age] years old, and I go to [school]"


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


def introduce(self):
    print(f"Hi, I'm {self.name} and I'm {self.age} years old")


class Student(Person):
    def __init__(self, name, age, school):
        super().__init__(
            name, age
        )  # use super to access and add attribute to parent class
        self.school = school


def introduce(self):
    print(
        f"Hi, I'm {self.name} and I'm {self.age} years old, and I go to {self.school}"
    )


# create an object
person1 = Student("Jesse", 24, "University of Florida")
person1.introduce()


## Bonus: Library System
## create two classes
## 1. Book - the parent class
## 2. Ebook - a child class that inherits from Book
## Book should have:
## a title and author
## a method describe() that prints:
## "Book: [title] by [author]"
## Ebook should have
## an additional attribute: file_size (in MB)
## override describe() to also include the file size, like:
## "Ebook: [title] by [author], file size: [file_size]MB"


class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author


def describe(self):
    print(f"Book: {self.title} by {self.author}")


class Ebook(Book):
    def __init__(self, title, author, file_size):
        super().__init__(title, author)  # constructor chaining
        self.file_size = file_size


def describe(self):
    print(f"EBook: {self.title} by {self.author}, file size: {self.file_size}MB")


my_book = Ebook("Normal People", "Sally Rooney", 3)
my_book.describe()