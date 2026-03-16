## Class: A blueprint for creating objects
## Object: instance of a class
## Constructor: __init__() to intialize object
## Encapsulation: Group data + methods
## Inheritance: One class inherits from another
## Polymorphism: same methods behaves differently based on context


## example:
# class Animal:
# def __init__(self, name):
# self.name = name

# def speak(self):
# return "Some Sound"


# class Dog(Animal):
# def speak(self):
# return f"{self.name} says woof!"


# class Cat(Animal):
# def speak(self):
# return f"{self.name} says meow!"


## usage
# pets = [Dog("Buddy"), Cat("Whiskers")]

# for pet in pets:
# print(pet.speak())  # polymorphism in action


## List: ordered, mutable sequence: [1, 2, 3]
## Tuple: ordered, immutable sequence: (1, 2)
## Set: unordered, unique items: {1, 2, 3}
## Dict: key-Value store: {"name": "Alice", "age": 25}


## example: frequency counter
# def count_chars(s):
# freq = {}
# for char in s:
# freq[char] = freq.get(char, 0) + 1
# return freq

# print(count_chars("amazon"))


## bonus1: model a book library
## task: create two classes: book and library
## book has title, author, and genre
## library stores books in a list and has 3 methods:
## add_book(book)
## get_books_by_author(author)
## get_books_by_genre(genre)
# class Book:
# def __init__(self, title, author, genre):
# self.title = title
# self.author = author
# self.genre = genre

# def __str__(self):
# return f"{self.title} by {self.author} [{self.genre}]"


# class Library:
# def __init__(self):
# self.books = []

# def add_book(self, book):
# self.books.append(book)

# def get_books_by_author(self, author):
# return [book for book in self.books if book.author == author]

# def get_books_by_genre(self, genre):
# return [book for book in self.books if book.genre.lower() == genre.lower()]


# book1 = Book("1984", "George orwell", "Dystopia")
# book2 = Book("Animal Farm", "George orwell", "Satire")
# book3 = Book("The hobbit", "J.R.R Tolkien", "Fantasy")

# library = Library()
# library.add_book(book1)
# library.add_book(book2)
# library.add_book(book3)

# fantasy_books = library.get_books_by_genre("Fantasy")
# for book in fantasy_books:
# print(book)


## optimal solution for bonus1
# class Library:
# def __init__(self):
# self.books = []
# self.book_by_author = {}
# self.book_by_genre = {}

# def add_book(self, book):
# self.books.append(book)

## index by author
# if book.author not in self.book_by_author:
# self.book_by_author[book.author] = []
# self.book_by_author[book.author].append(book)

## index by genre
# genre = book.genre.lower()
# if genre not in self.book_by_genre:
# self.book_by_genre[genre] = []
# self.book_by_genre[genre].append(book)

# def get_books_by_author(self, author):
# return self.get_books_by_author.get(author, [])

# def get_books_by_genre(self, genre):
# return self.get_books_by_genre.get(genre.lower(), [])


## bonus2: design a student gradebook system
## student with name, id, and a grades list
## gradebook which stores multiple students and has methods to:
## 1. add a student
## 2. record a grade for a student
## 3. calculate the average grade for a student
## 4. find the top student (highest average)
# class Student:
# def __init__(self, name, id):
# self.name = name
# self.id = id
# self.grades = []

# def add_grade(self, grade):
# self.grades.append(grade)

# def average(self):
# return sum(self.grades) / len(self.grades) if self.grades else 0

# def __str__(self):
# return f"{self.name} (#{self.id}) - Avg: {self.average():.2f}"


# class GradeBook:
# def __init__(self):
# self.students = {}

# def add_student(self, name, id):
# self.students[id] = Student(name, id)

# def add_grade(self, id, grade):
# if id in self.students:
# self.students[id].add_grade(grade)

# def calculate_average(self, id):
# if id in self.students:
# return self.students[id].average()

# def get_top_student(self):
# if not self.students:
# return None
# return max(self.students.values(), key=lambda student: student.average())


# gradebook = GradeBook()
# gradebook.add_student("Alice", 1)
# gradebook.add_student("Bob", 2)

# gradebook.add_grade(1, 90)
# gradebook.add_grade(1, 95)
# gradebook.add_grade(2, 88)
# gradebook.add_grade(2, 92)

# top_student = gradebook.get_top_student()
# print(top_student)


## Time complexity
## Operation: add_student, Time complexity: O(1) - dictionary insert
## Operation: add_grade, Time complexity: O(1) - dictionary insert + list append
## Operation: calculate_average, Time complexity: O(n) - sum over n grades
## Operation: get_top_student, Time complexity: O(m) - where m = number of students