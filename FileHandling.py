## Python has built-in functions to work with files, using the open() function
## basic file operations
## open a file for writing (creates the file if it does not exist)
# file = open("example.txt", "w")
# file.write("Hello, file!")
# file.close()
## open a file for reading
# file = open("example.txt", "r")
# content = file.read()
# print(content)
# file.close()


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
# file = open("my_file.txt", "w")
# file.write("This is my first file!")
# file.close()
## 2. Open my_file.txt and read its contents
# file = open("my_file.txt", "r")
## 3. Print the content to the screen
# content = file.read()
# print(content)
# file.close()


## Bonus
## Modify your code so that it writes two lines to the file using \n
## then reads and prints them line by line using a for loop
## This is line 1
## This is line 2
# file = open("bonus.txt", "w")
# file.writelines(
# ["This is line 1.\n", "This is line 2."]
# )  # writelines to write multiple lines
# file.close()

# file = open("bonus.txt", "r")
# content = file.read()
# print(content)
# file.close()


## a for loop gives more control and is often clearer
## if you want to format or modify each line before writing
## working with data that dynamically generated (user input or calculations)
## you want to insert line breaks manually after each item
# lines = ["This is line 1.", "This is line 2."]
# with open("bonus2.txt", "w") as file:
# for line in lines:
# file.write(line + "\n")


## bonus
## 1. create a list of five motivational quotes (as strings)
## 2. use a for loop to write each quote to a file called quotes.txt
## with each quote on a new line
## 3. then open the file, read all the quotes, and print them out one by one
# quotes = [
# "Try harder and be great",
# "nothing is unachievable",
# "trust the process",
# "hard work pays off",
# "the universe will reward you",
# ]
## write a file with the quotes
# with open("quotes.txt", "w") as file:
# for quote in quotes:
# file.write(quote + "\n")
## read quotes.txt file
# with open("quotes.txt", "r") as file:
# for line in file:
# print(line.strip())  # .strip() removes the newline character


## quiz
# with open("data.txt", "a") as file:
# file.write("Data Science!\n")


## example
# with open("notes.txt", "w") as f:
# f.write("Python is awesome.\nLet's master it!")

# with open("notes.txt", "r") as f:
# print(f.read())


## practice
# with open("Journal.txt", "a") as file_input:
# file_input.write("\n")
# file_input.write(input("Enter journal entry: "))
# print("Entry saved")


## bonus
# with open("Journal.txt", "r") as file_input:
# for i, line in enumerate(file_input, start=1):
# print(f"{i}. {line}", end="")


## when should you use file handling
## 1. saving user data, like logs or results
## 2. reading configuration files
## 3. exporting reports, logs, or processed data
## 4. loading static input files for scripts


## time complexity:
## Operation: read() | Complexity: O(n) - reads whole file
## Operation: write() | Complexity: O(n) - writes all content
## Operation: readline() | Complexity: O(k) - k is line length


## Quiz
## what does with open("file.txt", "r") as f: do?
## opens the file, reads contents, automatically closes it after the block ends


## Practice
## write a program that:
# 1. prompts the user to enter a filename
# 2. reads and prints the content of that file
# 3. handle the case where the file doesn't exist gracefully

# file_name = input("Enter the name of the file: ")

# try:
# with open(file_name, "r") as file:
# content = file.read()
# print(f"File content: {content}")
# except FileNotFoundError:
# print("Error: File not found.")


## Big O: O(n) where n is the number of characters in the file (due to .read())


## Bonus1:
## write a program that:
# 1. takes 3 lines of user input
# 2. writes them to a file called output.txt
# 3. confirms that writing is done

# with open("output.txt", "a") as file:
# while True:
# user_input = input("Enter a line of text(press 1 to exit): ").lower()
# if user_input == "exit":
# break
# file.write(user_input + "\n")


## Bonus2: create a mini log system:
# 1. ask the user for a message
# 2. append it to a file called log.txt with the current time using datetime

from datetime import datetime

user_input = input("Enter a message: ").lower()
timestamp = datetime.now().strftime("[%Y-%m-%d %H:%M:%S]")

with open("log.txt", "a") as file:
    file.write(f"{timestamp} {user_input}\n")

print("Message logged successfully.")


## datetime.now() gets the current time
## .strftime("[%Y-%m-%d %H:%M:%S]") formats it like [YYYY-MM-DD HH:MM:SS]
## file.write[...] logs both timestamp and message to the file
## the file is opened in "a" (append) mode so previous logs aren't overwritten