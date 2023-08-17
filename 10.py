from math import pi

class Shape:
    def __init__(self, name):
        self.name = name

    def area(self):
        pass

    def fact(self):
        return "Двухмерная фигура"

    def __str__(self):
        return self.name


class Square(Shape):
    def __init__(self, length):
        super().__init__("Квадрат")
        self.length = length

    def area(self):
        return self.length**2

    def fact(self):
        return "Каждый угол равен 90 градусам"

class Circle(Shape):
    def __init__(self, radius):
        super().__init__("Круг")
        self.radius = radius

    def area(self):
        return pi*self.radius**2

shape = Shape("фигура")
print(shape)
print(shape.area())
print(shape.fact())
print()

square = Square(4)
print(square)
print(square.area())
print(square.fact())
print()

circle = Circle(9)
print(circle)
print(circle.area())
print(circle.fact())
print()
