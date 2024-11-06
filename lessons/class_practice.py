"""Quiz 03 Practice."""

import math


class Circle:
    radius: float

    def __init__(self, r: float):
        self.radius = r

    def area(self) -> float:
        return math.pi * self.radius**2


class Rectangle:
    width: float
    height: float

    def __init__(self, w: float, h: float):
        self.width = w
        self.height = h

    def area(self) -> float:
        return self.width * self.height


circ: Circle = Circle(2.0)
rect: Rectangle = Rectangle(4.0, 5.5)
print(circ.area())
print(rect.area())
