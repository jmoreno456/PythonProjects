## learning:
## the syntax and structure of list comprehensions
## how to replace basic for loops with list comprehensions
## how to use conditionals in comprehensions


## what is a list comprehension?
## a list comprehension is a more concise way to create lists


## instead of this:
# squares = []
# for i in range(5):
# squares.append(i * i)
# print(squares)

## you can write this:
# squares = [i * i for i in range(5)]
# print(squares)


## syntax:
## [expression for item in iterable if condition]


## examples:
## 1. simple list
# nums = [x for x in range(10)]
# print(nums)
## 2. with a condition:
# evens = [x for x in range(10) if x % 2 == 0]
# print(evens)
## 3. transforming data:
# words = ["apple", "banana", "strawberry"]
# uppercase = [w.upper() for w in words]
# print(uppercase)


## quiz:
# squares = [x**2 for x in range(5) if x % 2 == 0]
# print(squares)


## practice: write a list comprehension that creates a list of the first 10 multiples of 3, starting from 3
# multiples = [x for x in range(3, 31) if x % 3 == 0]
# print(multiples)


## bonus1: write a list comprehension that replaces all negative numbers with 0 in the following list
# nums = [5, -3, 7, -1, 0, 9, -8]
# zeros = [0 if x < 0 else x for x in nums]
# print(zeros)
## the if before the for is for filtering
## the if-else before the for is for transformation (like replacing)


## bonus2: from a given list of words, return a new list containing the length of each word only if the words starts with a vowel
# words = ["apple", "banana", "orange", "grape", "umbrella"]
# vowels = "aeiou"
# result = [len(word) for word in words if word[0].lower() in vowels]
# print(result)


## bonus3: you are given a list of words. create a dictionary where each word is the key, and its length is the value
words = ["data", "science", "python", "ai"]

length_dict = {word: len(word) for word in words}

print(length_dict)
