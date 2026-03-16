# 10-8 cats and dogs: make two files, cat.txt and dogs.txt. store at
# least three names of cats in the first file and three names of dogs
# in the second file. write a program that tries to read these files
# and print the contents of the file to the screen. wrap your code in
# try-except block to catch the filenotfound error, and print a friendly
# message if a file is missing. move one of the files to a different
# location on your system, and make sure the code in the except block
# executes properly
from pathlib import Path


def multi_files(path):
    """Try to read the cats an dogs text file"""
    try:
        contents = path.read_text(encoding="utf-8")
    except FileNotFoundError:
        pass
    else:
        print(contents)


filenames = ["cats.txt", "dogs.txt"]
for file in filenames:
    path = Path(file)
    multi_files(path)