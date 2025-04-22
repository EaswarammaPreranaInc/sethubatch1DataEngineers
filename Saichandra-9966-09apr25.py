# 1. Write a program to determine area and perimeter of triangle and represent triangle by an object.
what is the area of triangle ? ---> sqrt(s(s-a)(s-b)(s-c))
what is the formula for 's' ? ---> (a+b+c)/2
what is the perimeter of triangle ? ---> a+b+c
'''
import math

class Triangle:
    def get(self):
        self.a = eval(input("Enter first side of triangle : "))
        self.b = eval(input("Enter second side of triangle : "))
        self.c = eval(input("Enter third side of triangle : "))

    def test(self):
        if (self.a + self.b > self.c) and (self.a + self.c > self.b) and (self.b + self.c > self.a):
            pass
        else:
            print("Not a triangle")
            exit()

    def area(self):
        s = (self.a + self.b + self.c) / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))

    def peri(self):
        return self.a + self.b + self.c
# End of the class
if __name__ == '__main__':
	t = Triangle()
	t.get()
	t.test()
	print('Area:',t.area())
	print('Perimeter:',t.peri())
'''



# 2. Local Variable Vs Instance Variable
class C1:
    def m1(self):  # self is object 'a'
        x = 10      # Local variable of m1() method   
        self.x = 20     # Adds variable 'x' to object 'a' with value 20     
        print(x)        # Local variable i.e. 20
        print(self.x)     # Variable 'x' of object 'a' i.e. 20
        x += 5         # Modifies Local variable 'x' to 15 
        self.x += 7      # Modifies variable 'x' object 'a' to 15
    
    def m2(self):
        #print(x)      # Error : No local variable x in m2() method
        print(self.x)    # Variable 'x' of object 'a' i.e. 27
        self.x += 6    # Modifies variable 'x' object 'a' to 33

# End of the class
a = C1()   # Creates empty c1 class
a.m1()
a.m2()
print(a.x)  
#print(self.x)  # Error becoz there is no self outside the class
#print(x)   # Error becoz there is no global variable 'x'



# 3. (Add objects)
# Write a program to add two objects where each object contains three values and store results in third object
1st object ---> x = 10, y = 20, z = 30
2nd object ---> x = 40, y = 50, z = 60
3rd object ---> x = 10 + 40 = 50, y = 20 + 50 = 70, z = 30 + 60 = 90
'''
class Test:
    def get(self):
        self.x = eval(input('Enter value of x: '))
        self.y = eval(input('Enter value of y: '))
        self.z = eval(input('Enter value of z: '))    # How to read inputs into variables x, y and z of object self

    def add(self, m, n):
        self.x = m.x + n.x
        self.y = m.y + n.y
        self.z = m.z + n.z   # How to add objects m and n and store results in object self

    def disp(self):
        print('x:', self.x)
        print('y:', self.y)
        print('z:', self.z)   # How to print object self

# End of the class
a = Test()
b = Test()
c = Test()   # How to create three test class objects a, b and c

print('First object')
a.get()    # How to read inputs into object 'a'

print('Second object')
b.get()    # How to read inputs into object 'b'

c.add(a, b)    # How to add objects a and b and store results in object 'c'

print('Addition results')
c.disp()   # How to print object 'c'
'''



# 4. (__str__demo1)
class Date:
    def disp(self):  # self is object 'a'
        print('dd:', self.dd)
        print('mm:', self.mm)
        print('yy:', self.yy)

    def __str__(self):
        return f'{self.dd}-{self.mm}-{self.yy}'

# End of the class
a = Date()  # Creates an empty Date object

a.dd = 15
a.mm = 8
a.yy = 1947

a.disp()            
print(a)             # print(15-8-1947)
print(a.__str__())   # print('15-8-1947')
print(a.__dict__)    #  {'dd': 15, 'mm': 8, 'yy': 1947}



# 5. (__str__demo2)
class Date:
	pass
# End of the class
a = Date()
a.dd = 15
a.mm = 8
a.yy = 1947
print(a)



# 6. (__str__demo3)
# prog 8c (__str__demo3)
class c1:
	def __str__(self):
		return '25'
class c2:
	def __str__(self):
		return '35'
class c3:
	def __str__(self):
		print('Hyd')
class c4:
	def __str__(self, x):
		return f'{x}'

# End of the class
a = c1()
b = c2()
c = c3()
d = c4()
print(a)   # __str__ method of class c1 returns 25
#print(b)   # Error becoz __str__() method of class c2 returns non-string i.e 35
#print(c)   # Error becoz __str__() method of class c3 returns non-string i.e None
#print(d)   # Error : arg for __str__() methid of class c4
print(b.__str__())   # __str__() method of class c2 returns 35
print(c.__str__())   # __str__() method of class c3 prints 'Hyd' and returns NOne
print(d.__str__(50))   # __str__() method of class c4 returns '50'

