program1:
# End  of  class  c1
a = c1()
a . m1()
m1()
output:
3rd  method
Function

program2:
class   c1:
	def   m1(self):
		print('No  argument  method')
	def   m1(self , x):
		print('Single  argument  method : ' , x)
	def   m1(self , x , y):
		print('Two  argument  method : ' , x , y)
# End  of  class  c1
a = c1()
a . m1(10 , 20)
#a . m1(30)
#a . m1()
output:
Two  argument  method :  10 20

program3:
class   c1:
	def   m1(self):
		print('No  argument  method')
	def   m1(self , x):
		print('Single  argument  method : ' , x)
	def   m1(self , x = 1  , y = 2):
		print('Two  argument  method : ' , x , y)
# End  of  class  c1
a = c1()
a . m1(10 , 20)
a . m1(30)
a . m1()
output:
Two  argument  method :  10 20
Two  argument  method :  30 2
Two  argument  method :  1 2

program4:
class   c1:
	def   m1(self):
		print('Method  of  first  c1  class')
class   c1:
	def   m1(self):
		print('Method  of  second  c1  class')
class   c1:
	def   m1(self):
		print('Method  of  third  c1  class')
a = c1()
a . m1()
output:
Method  of  third  c1  class

program5:

Write  a  program  to  determine  area  and  perimeter  of  triangle  and  represent  triangle  by  an  object

import math

class Triangle:
    def get(self):
        self.a = eval(input("Enter side a: "))
        self.b = eval(input("Enter side b: "))
        self.c = eval(input("Enter side c: "))

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
if--name--=='--main--'
triangle = Triangle()
triangle.get()
if triangle.test():
    print("Area: ", triangle.area())
    print("Perimeter: ", triangle.peri())
output:
Enter side a: 6
Enter side b: 8
Enter side c: 9
Area:  23.525252389719434
Perimeter:  23.0

program6:
class   c1:
	def  m1(self):
		x = 10
		self . x = 20
		print(x)
		print(self . x)
		x += 5
		self . x += 7
	def   m2(self):
		#print(x)
		print(self . x)
		self . x += 6
# End  of  the  class
a = c1()
a . m1()
#a . m2()
print(a . x)
#print(self . x)
#print(x)
output:
10
20
27

program7:
Write  a  program  to  add  two  objects  where  each  object  contains  three  values  and
store  results  in   third  object

class Test:
    def get(self):
        self.x = eval(input("Enter the value of x: "))
        self.y = eval(input("Enter the value of y: "))
        self.z = eval(input("Enter the value of z: "))

    def add(self, m, n):
        self.x = m.x + n.x
        self.y = m.y + n.y
        self.z = m.z + n.z

    def disp(self):
        print(f"x: {self.x}, y: {self.y}, z: {self.z}")
a = Test()
b = Test()
c = Test()
print("First Object")
a.get()
a.disp()
print("Second Object")
b.get()
b.disp()
c.add(a, b)
print("Addition results")
c.disp()
'''output:
First Object
Enter x: 8
Enter y: 9
Enter z: 6
x: 8, y: 9, z: 6
Second Object
Enter x: 5
Enter y: 4
Enter z: 7
x: 5, y: 4, z: 7
Addition results
x: 13, y: 13, z: 13

program8:
class  Date:
	pass
# End of the class
a =  Date()
a . dd = 15
a . mm = 8
a . yy = 1947
print(a)
output:
<__main__.Date object at 0x0000026165956A50>

program9:
class   c1:
	def  _str_(self):
			return  '25'
class   c2:
	def  _str_(self):
			return   35
class   c3:
	def  _str_(self):
			print('Hyd')
class   c4:
	def  _str_(self , x):
			return   F'{x}'
#end of the class
a = c1()
b = c2()
c = c3()
d = c4()
print(a)
print(b)
print(c)
print(d)
print(b . _str_())
print(c . _str_())
print(d . _str_(50))
output:
<__main__.c1 object at 0x0000028F7C046A50>
<__main__.c2 object at 0x0000028F7C046BA0>
<__main__.c3 object at 0x0000028F7C046CF0>
<__main__.c4 object at 0x0000028F7C046E40>
35
Hyd
None
50
