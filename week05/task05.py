# Base class
class Shape:
    def area(self):
        return 0
    
    def perimeter(self):
        return 0

# Derived class: Circle
import math
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius * self.radius

    def perimeter(self):
        return 2 * math.pi * self.radius

# Derived class: Rectangle
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)

# Derived class: Triangle
class Triangle(Shape):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def area(self):
        # Heron's formula
        s = (self.a + self.b + self.c) / 2
        return (s * (s - self.a) * (s - self.b) * (s - self.c)) ** 0.5

    def perimeter(self):
        return self.a + self.b + self.c


# ✅ Demonstrating polymorphism
shapes = [
    Circle(5),
    Rectangle(4, 6),
    Triangle(3, 4, 5)
]

for shape in shapes:
    print(f"{shape.__class__.__name__}: Area = {shape.area():.2f}, Perimeter = {shape.perimeter():.2f}")
