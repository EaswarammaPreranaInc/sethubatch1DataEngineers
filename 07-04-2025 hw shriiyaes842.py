# Identify  error  (Home work)
class c1:
    def m1(self):
        pass


class c2:
    pass


class c3:  # Indensation error


# ============================================
#  Find  outputs  (Home  work)
class c1:
    def m1(self):
        x = 10
        self.x = 20
        print(x)
        print(self.x)
        x += 5
        self.x += 7

    def m2(self):
        # print(x)
        print(self.x)
        self.x += 6


# End  of  the  class
a = c1()
a.m1()
a.m2()
print(a.x)


# print(self . x)
# print(x)

# =================================================
# Find  outputs  (Home  work)
class c1:
    pass


# End  of  the  class
a = c1()
print(id(a))  # address of an object
print(type(a))  # class type class '__main__'.c1
print(a.__dict__)  # {}
print(a)  # type and address
del a


# print(a)
# =====================================================

#  Find  outputs  (Home  work)
def m1():
    print('Function')  # Function 2nd


class c1:
    def m1(self):
        print('1st  method')

    def m1(self):
        print('2nd  method')

    def m1(self):
        print('3rd  method')  # 3rd method 1st


# End  of  class  c1
a = c1()
a.m1()
m1()


# ============================================================

#  Find  outputs  (Home  work)
class c1:
    def m1(self):
        print('No  argument  method')

    def m1(self, x):
        print('Single  argument  method : ', x)

    def m1(self, x, y):
        print('Two  argument  method : ', x, y)  # Two  argument  method : 10 20


# End  of  class  c1
a = c1()
a.m1(10, 20)


# a .m1(30)
# a.m1()

# ===================================================================================================
#  Find  outputs  (Home  work)
class c1:
    def m1(self):
        print('No  argument  method')

    def m1(self, x):
        print('Single  argument  method : ', x)

    def m1(self, x=1, y=2):
        print('Two  argument  method : ', x, y)


# End  of  class  c1
a = c1()
a.m1(10, 20)  # Two  argument  method : 10 20
a.m1(30)  # Two  argument  method : 30 2
a.m1()  # Two  argument  method : 1 2


# ==================================================================

# Find  outputs  (Home  work)
class c1:
    def m1(self):
        print('Method  of  first  c1  class')


class c1:
    def m1(self):
        print('Method  of  second  c1  class')


class c1:
    def m1(self):
        print('Method  of  third  c1  class')  # Method  of  third  c1  class


a = c1()
a.m1()


# ==================================================================================

# Find  outputs  (Home  work)
class c1:
    def m1(self):
        print('Method  of  first  c1  class')


class c1:
    def m1(self):
        print('Method  of  second  c1  class')


class c1:
    pass


a = c1()


# a.m1()#error
# ========================================================================
#  Find  outputs (Home  work)
class c1:
    pass


# End  of  class
a = c1()
print(a.__dict__)  # {}
a.x = 10
print(a.__dict__)  # {'x':10}
a.y = 20
print(a.__dict__)  # {'x':10,'y':20}
a.x = 30
print(a.__dict__)  # {'x':10,'y':20,'x':30}
a.y = 40
print(a.__dict__)  # {'x':10,'y':20,'x':30,'y':40}
del a.x
print(a.__dict__)  # {'y':40}
del a.x
del a.y
print(a.__dict__)  # {}
del a
# print(a.__dict__)
# ===================================================================

import math


class triangle:
    def get(self):
        self.a = float(input("Enter side a: "))
        self.b = float(input("Enter side b: "))
        self.c = float(input("Enter side c: "))

    def test(self):
        # Triangle inequality test
        if (self.a + self.b > self.c) and (self.a + self.c > self.b) and (self.b + self.c > self.a):
            pass  # valid triangle
        else:
            print("Not a triangle")
            exit()  # stop execution

    def area(self):
        s = (self.a + self.b + self.c) / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))

    def peri(self):
        return self.a + self.b + self.c


# --- Usage ---
t = triangle()  # create triangle object
t.get()  # read inputs
t.test()  # check if it's a valid triangle

print('Area :', t.area())
print('Perimeter :', t.peri())


# ==================================================================================

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


# End of the class

# Creating three objects
a = Test()
b = Test()
c = Test()

print("First Object:")
a.get()

print("Second Object:")
b.get()

# Adding a and b, store result in c
c.add(a, b)

print("Addition Results:")
c.disp()


# =============================================================================
#  Find  outputs (Home  work)
class Date:
    pass


# End of the class
a = Date()
a.dd = 15
a.mm = 8
a.yy = 1947
print(a)  # type and address


# ==================================================

#  Find  outputs (Home  work)
class c1:
    def __str__(self):
        return '25'


class c2:
    def __str__(self):
        return 35


class c3:
    def __str__(self):
        print('Hyd')


class c4:
    def __str__(self, x):
        return F'{x}'


# end of the class
a = c1()
b = c2()
c = c3()
d = c4()
print(a)
# print(b)#error due to non string
# print(c)#error
# print(d)
print(b.__str__())
print(c.__str__())
print(d.__str__(50))
# =======================================================
'''