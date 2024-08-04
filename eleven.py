# Write a class ‘Complex’ to represent complex numbers, along with overloaded operators ‘+’ and ‘*’ which adds and multiplies them.

class Complex:
    def __init__(self, r, img) -> None:
        self.r = r
        self.img = img
    def __str__(self) -> str:
        return f"{self.r} + {self.img}i"
    def __add__(self, other):
        return Complex(self.r + other.r, self.img + other.img)
    def __mul__(self, other):
        return Complex(self.r*other.r - self.img*other.img, self.r*other.img + self.img*other.r)
a = Complex(1,2)
b = Complex(2,3)
print(a+b)
print(a*b)
