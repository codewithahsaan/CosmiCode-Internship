class ComplexNumber:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    # Overload + operator
    def __add__(self, other):
        return ComplexNumber(self.real + other.real, self.imag + other.imag)

    # Overload - operator
    def __sub__(self, other):
        return ComplexNumber(self.real - other.real, self.imag - other.imag)

    # Overload * operator
    def __mul__(self, other):
        real_part = (self.real * other.real) - (self.imag * other.imag)
        imag_part = (self.real * other.imag) + (self.imag * other.real)
        return ComplexNumber(real_part, imag_part)

    # Overload string representation for printing
    def __str__(self):
        return f"{self.real} + {self.imag}i" if self.imag >= 0 else f"{self.real} - {-self.imag}i"


# ✅ Testing the program
c1 = ComplexNumber(3, 4)   # 3 + 4i
c2 = ComplexNumber(1, -2)  # 1 - 2i

print("First Complex Number:", c1)
print("Second Complex Number:", c2)

print("\nAddition:", c1 + c2)
print("Subtraction:", c1 - c2)
print("Multiplication:", c1 * c2)
