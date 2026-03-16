## lists vs tuples vs sets
## purpose: to help decide when and why to use each


## a frozenset is an immutable version of a set(mutable)
## a frozenset also makes it hashable


## an object is considered hashable if it has a hash value or not
## if the object has a hash value then it can be used as a key
## for a dictionary or as an element in a set


## Feature: Ordered? | List([]): yes | Tuple(()): yes | Set ({}): no
## Feature: Mutable? | List([]): yes | Tuple(()): no | Set ({}): yes
## Feature: Duplicates? | List([]): allowed | Tuple(()): allowed | Set ({}): not allowed
## Feature: Indexing? | List([]): yes(list[0]) | Tuple(()): yes(tuple[0]) | Set ({}): No indexing
## Feature: Hashable? | List([]): no | Tuple(()): yes | Set ({}): No (unless frozenset)
## Feature: Speed | List([]): fast | Tuple(()): faster | Set ({}): fastest (for lookups)


## use a list when:
# 1. you need a mutable sequence
# 2. you'll be adding/removing elements
# 3. you care about order
# ex: [1, 2, 3], ["tasks", "to", "do"]


## use a Tuple when:
# 1. you want an immutable sequence
# 2. you care about performance
# ex: (latitude, longitude), ("name", "email")


## use a Set when:
# 1. you care about uniqueness
# 2. you need fast lookups or membership tests
# 3. you don't need order
# ex: {1, 2, 3}, {"apple", "banana"}


## time complexity
## Operation: Lookup | List: O(n) | Tuple: O(n) | Set: O(1)
## Operation: Insert | List: O(1) | Tuple: none | Set: O(1)
## Operation: Delete | List: O(n) | Tuple: none | Set: O(1)
## Operation: Iterate | List: O(n) | Tuple: O(n) | Set: O(n)
## Operation: Check membership | List: O(n) | Tuple: O(n) | Set: O(1)


## Quiz
## question: which data structure is best for fast membership checks (i.e., x in structure)?
## answer: Set
## a set is implemented as a hash table, so checking membership (x in my_set)
## takes O(1) time on average - much faster than a list or tuple


## hash tables are a type of data structure that allows for quick
## insertion, deletion, and retrieval of data.
## it works by using a hash function to map a key to an index in an array


## Practice
## you're managing a grocery store inventory. ask the user to input
## a few fruit names (comma-separated), then:
## 1. convert the input into a list
## 2. convert that list into a set to remove duplicates
## 3. print both the original list and the set

# fruit_names = input("Enter the names of fruits: ").split()
# my_set = set(fruit_names)
# print(fruit_names)
# print(my_set)


## converts input to list and set properly
## handles duplication with set()
## converting a list to a set: O(n) time
## split() splits by spaces by default. if you want comma-separated input, use:
## input().split(",")


## bonus1: tuple vs list memory comparison
## task: create a list and a tuple with the same elements, then:
## 1. import getsizeof from sys
## 2. compare their memory sizes

# from sys import getsizeof

# my_list = [1, 2, 3, 4, 5, 6]
# my_tuple = (1, 2, 3, 4, 5, 6)

# print(f"List size: {getsizeof(my_list)} bytes")
# print(f"Tuple size: {getsizeof(my_tuple)} bytes")


## tuples typically use less memory than lists because they are immutable
## and fixed in size


## bonus2: fast membership check with set
## you're building a basic spam filter. you have a set of banned words
## ask the user to input a message. check if any banned word exist in the message

banned_words = {"spam", "buy", "click", "offer"}
your_message = input("Enter a message: ")

words = your_message.lower().split()
found = banned_words.intersection(words)

if found:
    print(
        "Banned words detected: ", ", ".join(found)
    )  # if multiple banned words, this splits them with a comma and .join(found) joins them together on the same line
else:
    print("Message is clean")


## split() separates into words (instead of checking for substrings)
## set.intersection() is O(min(n, m)) - faster for large inputs


## recap of time complexities
## Operation: List -> Set | Time complexity: O(n)
## Operation: in check (list) | Time complexity: O(n)
## Operation: in check (set/dict) | Time complexity: O(1) avg
## Operation: Set intersection | Time complexity: O(min(len(A), len(B))
