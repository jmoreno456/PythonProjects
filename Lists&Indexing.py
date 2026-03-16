## core building block in python and data science
## a list is a collection of items in a specific order
## you can store numbers, strings, booleans
## you can even store other lists
# my_list = [10, 20, 30, 40]
# you can also mix other types
# mixed = ["Jesse", 28, True, 3.8]


## indexing
## Python uses zero-based indexing
# fruits = ["apple", "banana", "cherry"]
# print(fruits[0]) # apple
# print(fruits[2]) # cherry
# you can also use negative indexing
# print(fruits[-1]) # cherry
## modifying lists
# fruits[1] = "blueberry" # changes banana to blueberry
## looping through lists
# for fruit in fruits:
# print(fruit)


## slicing
## use slicing to get parts of a list
# numbers = [0, 1, 2, 3, 4]
# print(numbers[1:4]) # [1, 2, 3]
# numbers[start:end] returns from start to end-1


## list methods
## here are common ways to work with lists
# nums = [1, 2, 3]


# nums.append(4) # [1, 2, 3, 4]
# nums.remove(2) # [1, 3, 4]
# nums.pop() # removes last element
# nums.insert(1, 100) # [1, 100, 3]


## 1. create a list of 4 of your favorite foods
# my_fav = ["Tacos", "Chinese", "Pizza", "Wings"]
## 2. print the second item in the list
# print(my_fav[1])
## 3. change the last item to "avocado"
# my_fav[3] = "avocado"
# print(my_fav)
## 4. add a new food to the end of the list
# my_fav.append("brownies")
# print(my_fav)
## 5. use a loop to print every food in the list
# for food in my_fav:
# print(food)


## bonus
## list filtering
## python snippet that
## has a list of numbers from to 10
## creates a new list with only the even numbers from
## that list using a loop
## prints the new list
# my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# even_numbers = [] # create empty list to move numbers into new list

# for i in my_list:
# if i % 2 == 0:
# even_numbers.append(i) # moving even numbers from my_list

# print(even_numbers)


## list transformation
## you have a list of numbers
## double each number and store the results in a new list
## print the new list
# numbers = [1, 3, 5, 7]
# numbers_doubled = []

# for i in numbers:
# i *= 2
# numbers_doubled.append(i)

# print(numbers_doubled)


## practice: shooping list manager
shopping_list = []

for i in range(3):
    item = input("Enter items {i+1}: ")
    shopping_list.append(item)

print("Shopping List:", shopping_list)
shopping_list.pop(1)
print("Updated Shopping List", shopping_list)


## bonus: list stats
numbers_list = []

for i in range(5):
    num = int(input("Enter 5 numbers {i+1}: "))
    numbers_list.append(num)

print("Your numbers list:", numbers_list)
print("Sum:", sum(numbers_list))
print("Max:", max(numbers_list))
print("Min:", min(numbers_list))
print("Avg:", sum(numbers_list) / len(numbers_list))
