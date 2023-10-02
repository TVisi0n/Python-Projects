

class Vehicle:
    def __init__(self):
        self._vehicleColor = "Blue"
        self.__vehicleYear = 2013

    def setYear(self, private):
        self.__vehicleYear = private
    
obj = Vehicle()
obj.vehicleColor = "Red"
print(obj.vehicleColor)
obj.setYear = 2018
print(obj.setYear)

