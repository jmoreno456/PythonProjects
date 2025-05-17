## Python has built-in functions to work with files, using the open() function
## basic file operations
## open a file for writing (creates the file if it does not exist)
file = open("example.txt", "w")
file.write("Hello, file!")
file.close()
## open a file for reading
file = open("example.txt", "r")
content = file.read()
print(content)
file.close()


## Important Modes in open()
## "r": Read (default)
## "w": Write (overwrites)
## "a": Append
## "x": Create (fails if file exist)
## call file.close() to free system resources, ensure all data
## is actually written to disk, prevent accidental data coruption
## file.read() returns the entire content of the file as a single
## string
## opening a file in "w" while it already exists will overwrite the
## file completely


## 1. Write "this is my first file!" to a file called my_file.txt
file = open("my_file.txt", "w")
file.write("This is my first file!")
file.close()
## 2. Open my_file.txt and read its contents
file = open("my_file.txt", "r")
## 3. Print the content to the screen
content = file.read()
print(content)
file.close()


## Bonus
## Modify your code so that it writes two lines to the file using \n
## then reads and prints them line by line using a for loop
## This is line 1
## This is line 2
file = open("bonus.txt", "w")
file.writelines(
    ["This is line 1.\n", "This is line 2."]
)  # writelines to write multiple lines
file.close()

file = open("bonus.txt", "r")
content = file.read()
print(content)
file.close()


## a for loop gives more control and is often clearer
## if you want to format or modify each line before writing
## working with data that dynamically generated (user input or calculations)
## you want to insert line breaks manually after each item
lines = ["This is line 1.", "This is line 2."]
with open("bonus2.txt", "w") as file:
    for line in lines:
        file.write(line + "\n")

## bonus
## 1. create a list of five motivational quotes (as strings)
## 2. use a for loop to write each quote to a file called quotes.txt
## with each quote on a new line
## 3. then open the file, read all the quotes, and print them out one by one
quotes = [
    "Try harder and be great",
    "nothing is unachievable",
    "trust the process",
    "hard work pays off",
    "the universe will reward you",
]
## write a file with the quotes
with open("quotes.txt", "w") as file:
    for quote in quotes:
        file.write(quote + "\n")
## read quotes.txt file
with open("quotes.txt", "r") as file:
    for line in file:
        print(line.strip())  # .strip() removes the newline character