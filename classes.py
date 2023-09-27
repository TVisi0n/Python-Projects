
#Created a Vehicle class
class Vehicles:
    Make = "Hyundai"
    Model = "Elantra"
    Year = "2013"
    Color = "Blue"

    def enterVehicle(self):
        enter_make = input("Enter the Make of Vehicle: ")
        enter_model = input("Enter the Model: ")
        enter_year = input("Enter the Year: ")
        enter_color = input("Enter the Color: ")
        if (enter_make == self.Make and enter_model == self.Model and enter_year == self.Year and enter_color == self.Color):
            print("This {} {} is in stock!".format(enter_make, enter_model))
        else:
            print("This vehicle is not in stock! \nWe are sorry :(")

#Here are the specs/info on the said vehicle
class info(Vehicles):
    Class = "Sedan"
    Doors = "4 Doors"
    Engine = "4.1 liter"

    def enterVehicle(self):
        enter_make = input("Enter the Make of Vehicle: ")
        enter_model = input("Enter the Model: ")
        enter_year = input("Enter the Year: ")
        enter_engine = input("Enter the Engine Type: ")
        if (enter_make == self.Make and enter_model == self.Model and enter_year == self.Year and enter_engine == self.Engine):
            print("This {} {} is in stock!".format(enter_make, enter_model))
        else:
            print("This vehicle is not in stock! \nWe are sorry :(")
        
#This is the location of where to purchase the car
class Dealership(Vehicles):
    Name = "Ron Tonkin"
    Location = "Hillsboro"


sales = Vehicles()
sales.enterVehicle()

dealership = info()
dealership.enterVehicle()
