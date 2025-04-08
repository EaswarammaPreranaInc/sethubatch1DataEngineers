import math

class Triangle:
    def get(self):
        # Read three sides and assign to self
        self.a = float(input("Enter side a: "))
        self.b = float(input("Enter side b: "))
        self.c = float(input("Enter side c: "))

    def test(self):
        # Check if the three sides can form a triangle
        if (self.a + self.b > self.c) and (self.a + self.c > self.b) and (self.b + self.c > self.a):
            pass  # Valid triangle, do nothing
        else:
            print('Not a triangle')
            exit()  # Stop execution if not a valid triangle

    def area(self):
        # Calculate semi-perimeter
        s = (self.a + self.b + self.c) / 2
        # Heron's formula
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))

    def peri(self):
        # Calculate perimeter
        return self.a + self.b + self.c

# Create object
t = Triangle()

# Read inputs into object
t.get()

# Validate the triangle
t.test()

# Print results
print('Area :', t.area())
print('Perimeter :', t.peri())

import math

class Rat:
    def get(self):
        self.num = int(input("Enter numerator: "))
        self.den = int(input("Enter denominator (non-zero): "))
        self.test()

    def test(self):
        while self.den == 0:
            print("Denominator cannot be zero.")
            self.den = int(input("Re-enter denominator: "))

    def __str__(self):
        return f"{self.num} / {self.den}"

    def add(self, a, b):
        self.num = a.num * b.den + b.num * a.den
        self.den = a.den * b.den
        self.simplify()

    def sub(self, a, b):
        self.num = a.num * b.den - b.num * a.den
        self.den = a.den * b.den
        self.simplify()

    def mul(self, a, b):
        self.num = a.num * b.num
        self.den = a.den * b.den
        self.simplify()

    def div(self, a, b):
        if b.num == 0:
            self.num = None  # invalid
            self.den = None
        else:
            self.num = a.num * b.den
            self.den = a.den * b.num
            self.simplify()

    def simplify(self):
        if self.num != 0:
            g = math.gcd(self.num, self.den)
            self.num //= g
            self.den //= g

# --- Main Program ---
a = Rat()
b = Rat()
c = Rat()
d = Rat()
e = Rat()
f = Rat()

print("\nEnter first rational number:")
a.get()
print("Enter second rational number:")
b.get()

c.add(a, b)
d.sub(a, b)
e.mul(a, b)
f.div(a, b)

print("\nSum        :", c)
print("Difference :", d)
print("Product    :", e)

if f.num is not None:
    print("Division   :", f)
else:
    print("Division is not permitted (division by zero).")