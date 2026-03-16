from random import randint


class Die:
    """create an attribute with a default value."""

    def __init__(self, sides=6):
        """Initialize attribute sides."""
        self.sides = sides

    def roll_dice(self):
        """prints a random number between 1 and the number of sides
        each dice has."""
        return randint(1, self.sides)


# create instance
# six_sided_die = Die()
# for _ in range(10): # rolling ten times
#   print(six_sided_die.roll_dice())

# ten_sided_die = Die(10)
# for _ in range(10):
#   print(ten_sided_die.roll_dice())

twenty_sided_die = Die(20)
for _ in range(10):
    print(twenty_sided_die.roll_dice())