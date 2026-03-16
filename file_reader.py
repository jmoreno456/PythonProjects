from pathlib import Path

# path = Path("pi_digits.txt")
# contents = path.read_text().rstrip()
# contents = contents.rstrip()  # remove the extra blank line by using rstrip()
# print(contents)


# using splitlines
# path = Path('pi_digits.txt')
# contents = path.read_text()

# lines = contents.splitlines()
# for line in lines:
  #  print(line)


# explore the digits of pi
path = Path('pi_digits.txt')
contents = path.read_text()

pi_string = ''
for line in contents.splitlines():
    pi_string += line.lstrip()

print(pi_string)
print(len(pi_string))