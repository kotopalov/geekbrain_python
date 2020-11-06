class Complex:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        return f'{self.a}{"+" if self.b>=0 else "-"}{abs(self.b)}i'

    def __add__(self, other):
        return Complex(self.a + other.a, self.b + other.b)

    def __mul__(self, other):
        return Complex(self.a*other.a - self.b*other.b, self.a*other.b + self.b*other.a)


print(Complex(1, 1))
print(Complex(1, -1))
print(Complex(-1, -1))

print(Complex(-1, -1) + Complex(2, -2))
print(Complex(3, 2) * Complex(1, -4))
