## recursion is a powerful programming technique where a function
## calls itself to solve a problem


## a recursive function calls itself, and has a base case to stop the
## recursion
## example: factorial
def factorial(n):
    if n == 1:  # base case
        return 1
    else:
        return n * factorial(n - 1)  # recursive call


print(factorial(5))  # 120
## to calculate factorial(5):
## 5 * factorial(4)
## 4 * factorial(3)
## 3 * factorial(2)
## 2 * factorial(1)
## returns 1 (base case)
## 2 * 1 = 2
## 3 * 2 = 6
## 4 * 6 = 24
## 5 * 24 = 120


## practice
## write a function called sum_range(n) that recursively returns
## the sum of numbers from 1 to n
def sum_range(n):
    if n == 1:
        return 1
    else:
        return n + sum_range(n - 1)


print(sum_range(5))
## sum_range(5)
## 5 + sum_range(4)
## 5 + 4 + sum_range(3)
## 5 + 4 + 3 + sum_range(2)
## 5 + 4 + 3 + 2 + sum_range(1)
## 5 + 4 + 3 + 2 + 1 → 15


def mystery(n):
    if n == 0:
        return 0
    return n + mystery(n - 1)


print(mystery(3))
## 3 + mystery(2)
## 2 + mystery(1)
## 1 + mystery(0)
## 1 + 0 = 1
## 2 + 1 = 3
## 3 + 3 = 6


def reverse_string(s):
    if s == "":
        return s
    return reverse_string(s[1:]) + s[0]


print(reverse_string("abc"))
## reverse_string("bc") + "a"
## reverse_string("c") + "b" + "a"
##  reverse_string("") + "c" + "b" + "a"
## "" + "cba" = "cba"


## bonus: recursive palindrome checker
## write a recursive function called is_palindrome that checks
## whether a given string is a palindrome (reads the same foward and backward)
## rules: ignore case sensitivity
## you can assume the input is a single word(no spaces/punctuation)
def is_palindrome(s):
    s = s.lower()

    if len(s) <= 1:  # base case
        return True

    if s[0] != s[-1]:
        return False

    return is_palindrome(s[1:-1])


print(is_palindrome("Racecar"))
print(is_palindrome("hello"))
## "racecar"
## r == r
## "aceca"
## a == a
## "cec"
## c == c
## e base case


## bonus: recursive flattening of nested lists
## write a function flatten that takes a nested list
## and returns a flat list with all the values
## check each element
## if it is a list, recurse into it
## it it is not a list, add it to the result
def flatten(nested_list):
    flat_list = []

    for item in nested_list:
        if isinstance(item, list):
            flat_list += flatten(item)
        else:
            flat_list.append(item)
    return flat_list


print(flatten([1, [2, [3, 4], 5], 6]))
# ➜ [1, 2, 3, 4, 5, 6]


## bonus: recursive binary search
## write a recursive function binary_search(arr, target) that returns
## the index of the target in a sorted list, or -1 if it's not found
## you must use recursion
## the array is sorted in ascending order
## return the index
## handle the case where the target is not found


def binary_search(arr, target):
    def search(low, high):
        if (
            low > high
        ):  # if the low index goes above the high index, the item does not exist in the list
            return -1
        mid = (low + high) // 2  # finds the middle index of the current range
        if (
            arr[mid] == target
        ):  # if the middle value matches the target, return the index
            return mid
        elif (
            arr[mid] < target
        ):  # if the target is greater, search the right half of the array
            return search(mid + 1, high)  # (low, high) - low = mid + 1
        else:
            return search(
                low, mid - 1
            )  # if the target is less, search the left half of the array

    return search(
        0, len(arr) - 1
    )  # this line starts the recursion by searching the full array, from index 0 to len(arr) - 1


print(binary_search([1, 3, 5, 7, 9, 11], 7))  # ➜ 3
print(binary_search([1, 3, 5, 7, 9, 11], 2))  # ➜ -1

## binary search works on sorted lists and cuts the list in half
## every time, checking:
## 1. is the middle element equal to the target
## 2. if not, should we look left or right
## 3. repeat the process recursively
## think recursively
## how can i reduce the size of the problem each time
## keep reducing until base case


## write a recursive function
## power(base, exponent)
def power(base, exponent):

    if exponent == 0:
        return 1
    else:
        return base * power(base, exponent - 1)


print(power(2, 3))  # 8 (2 * 2 * 2)
print(power(5, 0))  # 1 (base case: anything^0 = 1)
print(power(3, 2))  # 9 (3 * 3)


## factorial function should return the factorial of a number n
## where: n! = n * (n-1) * (n-2) * ... * 1
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


print(factorial(5))  # 120 → (5 * 4 * 3 * 2 * 1)
print(factorial(3))  # 6   → (3 * 2 * 1)
print(factorial(0))  # 1   → base case (0! = 1)