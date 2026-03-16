from pathlib import Path

path = Path("alice.txt")
try:
    contents = path.read_text(encoding="utf-8")
except FileNotFoundError:
    print(f"Sorry, the file {path} does not exist.")


# analyzing text
# you can analyze text files containing entire books.
from pathlib import Path

path = Path("alice.txt")
try:
    contents = path.read_text(encoding="utf-8")
except FileNotFoundError:
    print(f"The file {path} does not exist.")
else:
    # count the number of words in the file
    words = contents.split()
    num_words = len(words)
    print(f"The file {path} has about {num_words} words.")


# working with multiple files
# let's move hte bulk of this program to a function to make it easier
# to run the analysis for multiple books
from pathlib import Path


def count_words(path):
    """Count the approximate number of words in a file."""
    try:
        contents = path.read_text(encoding="utf-8")
    except FileNotFoundError:
        print(f"The file {path} does not exist.")
    else:
        words = contents.split()
        num_words = len(words)
        print(f"The file {path} has about {num_words} words.")


path = Path("alice.txt")
count_words(path)


# example 2
# python has a pass statement that tells it to do nothing in a block
# the pass statement is a reminder that you're choosing to do nothing
# at a specific point in your programs' execution and that you might
# want to do something there later.
from pathlib import Path


def count_words(filename):
    """Count the approximate number of words in a file."""
    try:
        contents = path.read_text(encoding="utf-8")
    except FileNotFoundError:
        pass
    else:
        words = contents.split()
        num_words = len(words)
        print(f"The file {path} has about {num_words} words.")


filenames = ["alice.txt", "siddhartha.txt", "moby_dick.txt", "little_women.txt"]

for filename in filenames:
    path = Path(filename)
    count_words(path)
