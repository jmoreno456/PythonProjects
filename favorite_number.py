# 10-11 favorite number: write a program that prompts for the user's
# favorite number. use json.dumps() to store this number in a file.
# write a separate program that reads in this value and prints the
# message " i know your favorite number! it's ___."

from pathlib import Path
import json
# prompt user for favorite number
favorite_number = int(input("Enter your favorite number: "))
# create path
path = Path('favorite_number.json')
# use json dump to store favorite number in a file
contents = json.dumps(favorite_number)
# write the number to the file
path.write_text(contents)