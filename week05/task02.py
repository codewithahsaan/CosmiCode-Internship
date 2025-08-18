import math

# Base Class
class Shape:
    def area(self):
        raise NotImplementedError("Subclasses must implement area method.")

    def perimeter(self):
        raise NotImplementedError("Subclasses must implement perimeter method.")


# Circle Class
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        return 2 * math.pi * self.radius


# Rectangle Class
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)


# Triangle Class
class Triangle(Shape):
    def __init__(self, a, b, c):
        self.a = a  # side 1
        self.b = b  # side 2
        self.c = c  # side 3

    def area(self):
        # Heron's formula
        s = (self.a + self.b + self.c) / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))

    def perimeter(self):
        return self.a + self.b + self.c


# Example Usage
shapes = [
    Circle(5),
    Rectangle(4, 6),
    Triangle(3, 4, 5)
]

for shape in shapes:
    print(f"{shape.__class__.__name__} → Area: {shape.area():.2f}, Perimeter: {shape.perimeter():.2f}")
