class Carro:
    def __init__(self):
        pass
    def cars(self, brand, year, color):
        self.brand = brand
        self.year = year
        self.color = color
    def actions(self, drive, brake, park):
        self.drive = drive
        self.brake = brake
        self.park = park    
Car1 = Carro()
Car1.cars("Ford", 2019, "Red")
print(Car1.brand)
Car1.actions(True, True, False)
print(Car1.__dict__)

Car2 = Carro()
Car2.cars("Toyota", 1955, "Rusty")
Car2.actions(False, False, False) 
