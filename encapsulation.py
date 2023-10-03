

class Vehicle:
    def __init__(self):
        self._vehicleColor = "Blue"
        self.__vehicleYear = 2013

    def getYear(self):
        print(self.__vehicleYear)
    
    def setYear(self, private):
        self.__vehicleYear = private
    
obj = Vehicle()
obj.getYear()
obj.setYear(2018)
obj.getYear()

