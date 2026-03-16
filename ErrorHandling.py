## Try, Except, and Handling Errors
## sometimes, your code might encounter unexpected issues
## like dividng by zero or trying to read a missing file
## python lets you handle those errors gracefully using
## try and except


## example
# try:
# num = int(input("Enter a number: "))
# result = 10 / num
# print("Result: ", result)
# except ZeroDivisionError:
# print("You can't divide by zero!")
# except ValueError:
# print("Please enter a valid number.")


## practice
## 1. ask the user to enter two numbers
## 2. divide the first number by the second
## 3. use try and except to catch: ZeroDivisionError and ValueError
## 4. if no error, print the result
# try:
# num1 = int(input("Enter your first number: "))
# num2 = int(input("Enter your second number: "))
# result = round(num1 / num2)
# print("Result: ", result)
# except ZeroDivisionError:
# print("You cannot divide by zero!!!")
# except ValueError:
# print("Enter a valid number!!!")