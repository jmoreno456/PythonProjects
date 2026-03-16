## Sets are useful for storing unique, unordered elements and performing operations like union, intersection, and difference

## what is a set?
## A collection of unordered, unchangeable (but you can add/remove items), and unique elements

## creating a set
# my_set = {1, 2, 3, 4}
## adding and removing elements
# my_set.add(5) # adds 5 to the set
# my_set.remove(2) # removes 2 from the set
# my_set.discard(100) # discards 100, does nothing if not present
# print(my_set)

## set operations
# a = {1, 2, 3}
# b = {3, 4, 5}

# print(a.union(b))  # {1, 2, 3, 4, 5}
# print(a.intersection(b))  # {3}
# print(a.difference(b))  # {1, 2}

## check membership
# if 3 in a:
# print("3 is in the set")


## practice
# favorite_fruit = input("Enter 5 of your favorite fruit, separated by commas: ")
# my_set = set(favorite_fruits.strip().split(","))
# print(my_set)
## .split(",") splits that into a list by comma
## set() removes duplicates automatically
## you can also strip extra spaces:
## my_set = {fruit.strip() for fruit in favorite_fruits.split(",")}


## bonus1:
# set1 = {"apple", "banana", "cherry"}
# set2 = {"banana", "kiwi", "grape"}

# print(set1.intersection(set2))
# print(set1.difference(set2))
# print(set1.union(set2))


## bonus2: find common letter between two words using sets
word1 = set("apple")
word2 = set("grape")

print("Common letters:", word1 & word2) # output: {'a', 'e', 's'}


## fruits that start with certain letters
fruits = {"apples", "grapes", "bananas", "strawberries", "blueberries"}
letters = {"a", "e", "s"}
result = [fruit for fruit in fruits if fruit[0].lower() in letters]
print(result) # output ['apples', 'strawberries']
## wrap fruit[0].lower() to make it case-insensitive


## print all unique words in that sentence (as a set)
sentence = input("Enter a sentence: ")
words = set(sentence.lower().split())
print("Unique words:", words)