## map(), filter(), zip(), enumerate()
## these are built-in functions that take other functions as arguments


## map(function, iterable)
## applies a function to each element of an iterable and returns a
## map object (which can be turned into a list)
## convert it with list() to access the values
nums = [1, 2, 3, 4]
squares = list(map(lambda x: x**2, nums))
print(squares)  # [1, 4, 9, 16]


## filter(function, iterable)
## filters elements based on a condition, keeps only the elements
## for which the function returns True
nums = [1, 2, 3, 4, 5]
evens = list(filter(lambda x: x % 2 == 0, nums))
print(evens)  # [2, 4]


## zip(iter1, iter2, ...)
## combines multiple iterables into pairs(or tuples of N elements)
## stops at the shortest iterable
## zip() pairs items by index from multiple iterables
names = ["Alice", "Bob", "Charlie"]
scores = [85, 92, 78]
zipped = list(zip(names, scores))
print(zipped)  # [('Alice', 85), ('Bob', 92), ('Charlie', 78)]


## enumerate(iterable, start=0)
## returns index + value pairs (like a numbered list)
fruits = ["apple", "banana", "cherry"]
for index, fruit in enumerate(fruits, start=1):
    print(index, fruit)
# output:
# 1 apple
# 2 banana
# 3 cherry


## practice
## use map() and filter() together to:
## 1. square all numbers from 1 to 10
## 2. keep only the squares that are greater than 30
squares1 = range(1, 11)
squares1 = list(filter(lambda x: x > 30, map(lambda x: x**2, squares1)))
print(squares1)
## filter() and map() both take an iterable as the second argument
## nest them properly


## practice
## you are given two lists:
## use zip() to combines these into a list of tuples
## use enumerate() to print them out in a numbered format
students = ["Alex", "Brian", "Cathy"]
grades = [90, 82, 78]

for i, (student, grade) in enumerate(zip(students, grades), start=1):
    print(f"{i}. {student} - {grade}")
## tuple unpacking for i, (student, grade)
## i for the index from enumerate
## student, grade the inner tuple from zip
## for each student and grade pair, also keep track of the index


## bonus
## write a program that takes 3 lists of names, scores1, and scores2
## use zip() to pair each student with both scores
## use map() to calculate each student's average score
## print output
names = ["Luna", "Kai", "Zara"]
scores1 = [90, 80, 70]
scores2 = [85, 75, 95]

average_score = list(map(lambda x, y: (x + y) / 2, scores1, scores2))

for name, avg in zip(names, average_score):
    print(f"{name} - Average: {average_score}")