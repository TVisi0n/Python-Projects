
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

obj = roll()
obj.yourRoll("1")
obj.rollAmount("1")
