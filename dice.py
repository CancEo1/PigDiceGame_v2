# Dice program that I retrieved from a different code. Worked all the same
# and was an excellent use of GitHub and using old code with new codes.
import random

class Die:
    ## Attributes not variables. ATTRIBUTES
    __value:int = 1 # If you want this to be private add double underscore to the prefix.

    # If the value is between 1 and 6 continue. If not closes the program.
    # With the @ symbol you can also set value to a getter or setter
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value):
        if value < 1 or value > 6:
            raise ValueError("Die value must be from 1 to 6.")
        else:
            self.__value = value

    def roll(self):
        self.value = random.randrange(1, 7)

# Object composition is a way to combine simple objects into more complex ones.
# e.x. one Dice object can store multiple Die objects.
class Dice():
    # Explicit constructor
    def __init__(self):
        self.__list = []

    @property       # read-only
    def list(self):
        return tuple(self.__list)

    def addDie(self, die):
        self.__list.append(die)

    def rollAll(self):
        for die in self.__list:
            die.roll()
