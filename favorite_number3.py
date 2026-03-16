# 10-12 favorite number remembered: combine the two programs you wrote
# in exercise 10-11 into one file. if the number is already stored,
# report the favorite number to the user.
# if not, prompt the user's favorite number and store it in a file.
# run th eprogram twice to see that it works.

from pathlib import Path
import json

path = Path("favorite_number.json")
if path.exists():  # use exists method from path library
    contents = path.read_text()
    favorite_number = json.loads(contents)
    print(f"I know your favorite number! It's {favorite_number}")
else:
    favorite_number = int(input("What's your favorite number? "))
    contents = json.dumps(favorite_number)
    path.write_text(contents)
