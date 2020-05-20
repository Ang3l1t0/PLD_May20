#!/usr/bin/python3

class Carro():
    def __init__(self, cars, actions):
        self.cars = cars
        self.actions = actions
    def __str__(self):
        return "Cars: {}, Action: {},".format(self.cars, self.actions)

class Cars(Carro):
    def __init__(self, cars, actions, brand, year, color):
        Carro.__init__(self, cars, actions)
        self.brand = brand
        self.year = year
        self.color = color
    def __str__(self):
        return Carro.__str__(self) + " Brand: {}, Year: {}, Color: {}".format(self.brand, self.year, self.color)

Car1 = Cars("vehicle", True, "Ford", "2019", "Red")
Car2 = Cars("vehicle", False, "Toyota", "1955", "GreenViche")
print(Car1)
print(Car2)
