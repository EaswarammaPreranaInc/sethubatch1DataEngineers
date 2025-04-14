#Python program that determines the area and perimeter of a triangle and represents the triangle as an object:

"""
import math

class Triangle:
    def get(self):
        self.a = float(input("Enter side a: "))
        self.b = float(input("Enter side b: "))
        self.c = float(input("Enter side c: "))

    def test(self):
        if (self.a + self.b > self.c) and (self.a + self.c > self.b) and (self.b + self.c > self.a):
            return True
        else:
            print("Not a triangle")
            return False

    def area(self):
        s = (self.a + self.b + self.c) / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))

    def peri(self):
        return self.a + self.b + self.c


t = Triangle()
t.get()


if t.test():
    print("Area: ", t.area())
    print("Perimeter: ", t.peri())


class Test:
    def get(self):
        self.x = int(input("Enter x: "))
        self.y = int(input("Enter y: "))
        self.z = int(input("Enter z: "))

    def add(self, m, n):
        self.x = m.x + n.x
        self.y = m.y + n.y
        self.z = m.z + n.z

    def disp(self):
        print(f"x = {self.x}, y = {self.y}, z = {self.z}")

a = Test()
b = Test()
c = Test()

print("First Object")
a.get()
print("Second Object")
b.get()

c.add(a, b)

print("First Object")
a.disp()
print("Second Object")
b.disp()
print("Addition results")
c.disp()

"""