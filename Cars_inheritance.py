#!/usr/bin/python3
"""Class Carro that Define a Car
Attribute:
cars -- defining those types of cars is
actions -- defining whether it is in motion or not... True or False"""


class Carro():
    def __init__(self, cars, actions):
        self.cars = cars
        self.actions = actions

    def __str__(self):
        return "Cars: {}, Action: {},".format(self.cars, self.actions)

    """Class Cars which defines the characteristics of the car
    Attribute:
    cars -- defining those types of cars is
    actions -- defining whether it is in motion or not... True or False
    brand -- Car Brand
    year -- Car Year
    Color -- Car Color"""


class Cars(Carro):
    def __init__(self, cars, actions, brand, year, color):
        Carro.__init__(self, cars, actions)
        self.brand = brand
        self.year = year
        self.color = color

        """
        returns a printable string representing the object
        """
    def __str__(self):
        return (Carro.__str__(self) +
                "Brand: {}, Year: {}, Color: {}"
                .format(self.brand, self.year, self.color))

Car1 = Cars("vehicle", True, "Ford", "2019", "Red")
Car2 = Cars("vehicle", False, "Toyota", "1955", "GreenViche")
print(Car1)
print(Car2)
