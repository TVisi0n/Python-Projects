
from abc import ABC, abstractmethod
class die(ABC):
    def yourRoll(self, amount):
        print("Your roll amount is: ",amount)

    @abstractmethod
    def rollAmount(self, amount):
        pass

class roll(die):
    def rollAmount(self, amount):
        print('You rolled a {}! Roll again!'.format(amount))

# User's first roll
#Roll1 = front()
#Roll1.sideno()

# User's second roll
#Roll2 = right()
#Roll2.sideno()

# User's third roll
#Roll3 = back()
#Roll3.sideno()

obj = roll()
obj.yourRoll("1")
obj.rollAmount("1")
