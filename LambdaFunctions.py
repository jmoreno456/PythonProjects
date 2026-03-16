## lambda functions & map(), filter(), reduce()
## lambda - quick, anonymous functions
## map() - apply a function to every item in a list
## filter() - keep items that meet a condition
## reduce() - combine items using a function (needs functools)


## lambda function example:
# square = lambda x: x * x
# print(square(5))


## map() example:
# nums = [1, 2, 3, 4]
# squares = list(map(lambda x: x * x, nums))
# print(squares)


## filter() example:
# nums = [1, 2, 3, 4, 5, 6]
# evens = list(filter(lambda x: x % 2 == 0, nums))
# print(evens)


## reduce() example:
# from functools import reduce

# nums = [1, 2, 3, 4]
# product = reduce(lambda x, y: x * y, nums)
# print(product)


## practice: use lambda and map to square each number in a list
# numbers = [2, 4, 6, 8]
# square = list(map(lambda x: x**2, numbers))
# print(square)


## bonus1: use filter with lambda to get only words longer than 5 characters
# words = ["apple", "banana", "kiwi", "strawberry", "fig", "blueberry"]
# result = list(filter(lambda x: len(x) > 5, words))
# print(result)


## bonus2: use reduce() with a lambda to calculate the product of all numbers in the list
# from functools import reduce

# nums = [1, 3, 5, 7]

# product = reduce(lambda x, y: x * y, nums)
# print(product)
