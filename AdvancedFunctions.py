## Advanced functions in python
## default arguments
## *args and **kwargs
## lambda functions
## higher-order functions (map, filter, reduce)


## default arguments
## you can assign default values to function parameters
def greet(name="Stranger"):
    print(f"Hello, {name}!")


greet()  # Hello, Stranger!
greet("Alice")  # Hello, Alice!


## *args and **kwargs
## *args: allows variable number of positional arguments
## *kwargs: allows variable number of keyword arguments
def print_args(*args):
    for arg in args:
        print(arg)


print_args(1, 2, 6, 7)


def print_kwargs(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")


print_kwargs(name="Alice", age=30)


## you can combine all three
def demo(a, b=2, *args, **kwargs):
    print(a, b, args, kwargs)


demo(1, 3, 4, 5, x=10, y=20)


## lambda functions
## anonymous one-line functions, useful for short operations
square = lambda x: x * x
print(square(5))


## higher-order functions
## these take other functions as arguments
## map()
nums = [1, 2, 3]
squares = list(map(lambda x: x * x, nums))
print(squares)


## filter ()
nums = [1, 2, 3, 4, 5]
even = list(filter(lambda x: x % 2 == 0, nums))
print(even)  # [2, 4]


## reduce() from functools
from functools import reduce

total = reduce(lambda x, y: x + y, [1, 2, 3, 4])
print(total)


## practice
## 1. write a function that takes any number of numbers using *args
## and returns their average
def numbers(*args):
    return sum(args) / len(args)


## if args else 0
## avoid division by zero if no arguments passed

print(numbers(1, 2, 3, 6, 7))


## 2. write a lambda function to check if a number is divisible by 3
is_div_by_3 = lambda x: x % 3 == 0
print(is_div_by_3(15))


## which built-in function applies a function cumulatively to the
## items of a sequence
## reduce() pplies a function cumulatively, like: (((1+2)+3)+4)


## output of this code
def demo(a, b=2, *args, **kwargs):
    print(a, b, args, kwargs)


demo(5, 7, 1, 2, x=10, y=20)
## a=5, b=7, args=(1,2), kwargs={'x': 10, 'y':20}


## what does this return
total = list(map(lambda x: x + 2, [1, 2, 3]))
print(total)
## each element gets 2 added
## [1+2, 2+2, 3+2] = [3, 4, 5]


## bonus challenge: flexible calculator
## write a function called flex_calc that takes:
## any number of values using *args
## a keyword argument operation with a default value of "add"
## it should return the result of performing the operation
## ("add", "mul", or "sub") across all numbers
def flex_calc(*args, **kwargs):
    operation = kwargs.get("operation", "add")

    if operation == "add":
        return sum(args)

    elif operation == "mul":
        result = 1
        for num in args:
            result *= num
        return result

    elif operation == "sub":
        if not args:
            return 0
        result = args[0]
        for num in args[1:]:
            result -= num
        return result

    else:
        return "Invalid operation"


print(flex_calc(1, 2, 3, 4, operation="mul"))
print(flex_calc(10, 5, operation="sub"))
print(flex_calc(1, 2, 3))


## bonus: multi mode stats calculator
## write a function called stats_calc that takes any number
## of numeric arguments using *args and accepts a keyword argument
## mode (default is "mean")
## mean, max, min, range
def stats_calc(*args, **kwargs):
    mode = kwargs.get("mode", "mean")

    if mode == "mean":
        if not args:
            return 0
        return sum(args) / len(args)
    elif mode == "max":
        return max(args)
    elif mode == "min":
        if not args:
            return 0
        return min(args)
    elif mode == "range":
        return max(args) - min(args)


print(stats_calc(2, 5, 7, 1))  # ➞ 3.75 (default is mean)
print(stats_calc(2, 5, 7, 1, mode="max"))  # ➞ 7
print(stats_calc(2, 5, 7, 1, mode="min"))  # ➞ 1
print(stats_calc(2, 5, 7, 1, mode="range"))  # ➞ 6 (7 - 1)
print(stats_calc(mode="min"))  # ➞ 0 or "No data"
