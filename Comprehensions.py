## List & Dictionary Comprehensions
## How to use conditions inside comprehensions
## when and why to use them over loops


## A list comprehension is a shorter, cleaner way to create lists


## traditional way (using a loop):
squares = []
for x in range(5):
    squares.append(x**2)
print(squares)


## with list comprehensions
squares = [x**2 for x in range(5)]
print(squares)


## basic format:
## [expression for item in iterable]


## example with condition
evens = [x for x in range(10) if x % 2 == 0]
print(evens)


## practice
## write a list comprehension
## 1. create a list of the cubes of numbers from 1 to 10
## 2. include only the cubes of even numbers
cube_even = [x**3 for x in range(1, 11) if x % 2 == 0]
print(cube_even)


## dictionary comprehensions
## traditional way:
squares = {}
for x in range(5):
    squares[x] = x ** 2
print(squares)


## dictionary comprehensions:
squares = {x: x**2 for x in range(5)}
print(squares)


## practice
## create a dictionary that maps numbers 1-5 to their cubes
## but only includes numbers that are odd
cube_odd = {x: x**3 for x in range(1, 6) if x % 2 != 0}
print(cube_odd)


quiz1 = {x: x % 2 == 0 for x in range(4)}
print(quiz1) # {0: True, 1: False, 2: True, 3: False}


## Bonus: comprehension combo
## create a dictionary where:
## the keys are numbers from 1 to 10
## the values are: "even" if the number is even and "odd" if the 
## number is odd
dict1 = range(1, 11)
dict1 = {x: "even" if x % 2 == 0 else "odd" for x in dict1}
print(dict1)