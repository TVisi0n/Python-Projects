
from abc import ABC, abstractmethod

# Represents a singular dice
class die(ABC):
    @abstractmethod
    def sideno(self):
        pass

# Possible rolls
class front(die):
    def sideno(self):
        print("My side number is 1")

class back(die):
    def sideno(self):
        print("My side number is 6")

class left(die):
    def sideno(self):
        print("My side number is 2")

class right(die):
    def sideno(self):
        print("My side number is 5")

class top(die):
    def sideno(self):
        print("My side number is 4")

class bottom(die):
    def sideno(self):
        print("My side number is 3")


# User's first roll
Roll1 = front()
Roll1.sideno()

# User's second roll
Roll2 = right()
Roll2.sideno()

# User's third roll
Roll3 = back()
Roll3.sideno()
