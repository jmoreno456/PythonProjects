# use json loads for this program

from pathlib import Path
import json

# create path to created file
path = Path("favorite_number.json")
# read the contents of the file
contents = path.read_text()
# use json loads to retrieve the contents of the file
favorite_number = json.loads(contents)
# use print statment to output the contents of the file
print(f"I know your favorite number! it's {favorite_number}")
