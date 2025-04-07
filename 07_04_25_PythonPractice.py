# Identify  error  (Home work)
class   c1:
	def  m1(self):
		pass
class   c2:
        pass
#class   c3: # Error becoz in class atleast one stmt or method or pass stmt should be there
# Find  outputs  (Home  work)
class   c1:
	pass
# End  of  the  class
a = c1() # creates c1 class objt
print(id(a)) # id of a
print(type(a)) # <classname '__main__.c1'>
print(a .__dict__) # objct a is converted to dictionary i.e {}
print(a) # Type and Address of objt a
del  a # Deletes the object a
print(a) # Error: name 'a' is not defined
#  Find  outputs  (Home  work)
def   m1():
		print('Function')
class   c1:
	def   m1(self):
		print('1st  method')
	def   m1(self):
		print('2nd  method')
	def   m1(self):
		print('3rd  method')
# End  of  class  c1
a = c1() # objct created c1 and ref a
a . m1() # 3rd method becoz of same method name in class c1
m1() # Function (outter method function)
#  Find  outputs  (Home  work)
class   c1:
	def   m1(self):
		print('No  argument  method')
	def   m1(self , x):
		print('Single  argument  method : ' , x)
	def   m1(self , x , y):
		print('Two  argument  method : ' , x , y)
# End  of  class  c1
a = c1() # cteates c1 objct with ref a
a . m1(10 , 20) # Two  argument  method : 10 20
#a . m1(30) # Error: c1.m1() missing 1 required positional argument: 'y'
#a . m1() # Error: c1.m1() missing 2 required positional arguments: 'x' and 'y'
#  Find  outputs  (Home  work)
class   c1:
	def   m1(self):
		print('No  argument  method')
	def   m1(self , x):
		print('Single  argument  method : ' , x)
	def   m1(self , x = 1  , y = 2):
		print('Two  argument  method : ' , x , y)
# End  of  class  c1
a = c1() # creates c1 objct with ref a
a . m1(10 , 20) # Two  argument  method : 10 20
a . m1(30) # Two  argument  method : 30 2
a . m1() # Two  argument  method : 1 2
# Find  outputs  (Home  work)
class   c1:
	def   m1(self):
		print('Method  of  first  c1  class')
class   c1:
	def   m1(self):
		print('Method  of  second  c1  class')
class   c1:
	def   m1(self):
		print('Method  of  third  c1  class')
a = c1() # creates c1 objct with ref a
a . m1() # Method  of  third  c1  class
# Find  outputs  (Home  work)
class   c1:
	def   m1(self):
		print('Method  of  first  c1  class')
class   c1:
	def   m1(self):
		print('Method  of  second  c1  class')
class   c1:
	pass
a = c1() # creates c1 objct with ref a
a . m1() # Error: 'c1' object has no attribute 'm1'
#  Find  outputs (Home  work)
class  c1:
        pass
# End  of  class
a = c1()
print(a . __dict__) # {}
a . x = 10
print(a . __dict__) # {'x' : 10}
a . y = 20
print(a . __dict__) # {'x' : 10 , 'y' : 20}
a . x = 30
print(a . __dict__) # {'x' : 30 , 'y' : 20}
a . y = 40
print(a .__dict__) # {'x' : 30 , 'y' : 40}
del  a . x
print(a . __dict__) # {'y' : 40}
del  a . y
print(a . __dict__) # {}
del   a
print(a . __dict__) #Error: name 'a' is not defined
'''  (Home  work)
Write  a  program  to  determine  area  and  perimeter  of  triangle  and  represent  triangle  by  an  object

1) What  is  the  area  of  triangle ?  --->  sqrt(s * (s - a) * (s - b) * (s - c))

2) What  is  the  formula  for  's' ?  --->  (a + b + c) / 2

3) What  is  the  perimeter  of  triangle ?  --->  a + b + c
'''
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
        # Removed 'print(x)' because x is not in scope
        print(self.x)
        self.x += 6

a = c1()
a.m1()
a.m2()
print(a.x)  # 33

'''  (Home  work)
Write  a  program  to  add  two  objects  where  each  object  contains  three  values  and
store  results  in   third  object

1st  object   --->  x = 10 , y = 20 , z = 30

2nd  object --->  x = 40 , y = 50 , z = 60

3rd  object  ---> x = 10 + 40 = 50 , y = 20 + 50 = 70 , z = 30 + 60 = 90
'''
class Test:
    def get(self):
        # Read inputs into object self
        self.x = int(input("Enter x: "))
        self.y = int(input("Enter y: "))
        self.z = int(input("Enter z: "))

    def add(self, m, n):
        # Add corresponding values of objects m and n, store in self
        self.x = m.x + n.x
        self.y = m.y + n.y
        self.z = m.z + n.z

    def disp(self):
        # Display the values of object self
        print(f"x = {self.x}, y = {self.y}, z = {self.z}")

# Create three Test class objects
a = Test()
b = Test()
c = Test()

# Read inputs into object 'a'
print("First Object")
a.get()

# Read inputs into object 'b'
print("Second Object")
b.get()

# Add objects a and b, store result in object 'c'
c.add(a, b)

# Display result
print("Addition results")
c.disp()


#  Find  outputs (Home  work)
class  Date:
	pass
# End of the class
a =  Date()
a . dd = 15
a . mm = 8
a . yy = 1947
print(a)
#  Find  outputs (Home  work)
class   c1:
	def __str__(self):
			return  '25'
class   c2:
	def  __str__(self):
			return   35
class   c3:
	def  __str__(self):
			print('Hyd')
class   c4:
	def  __str__(self , x):
			return   F'{x}'
#end of the class
a = c1() # creates objt with ref a
b = c2() # creates objt with ref b
c = c3() # creates objt with ref c
d = c4() # creates objt with ref d
print(a) # 25
#print(b) # Error becoz of 35 is int it takes only string in return
#print(c) # Error: __str__ returned non-string (type NoneType)
#print(d) # Error becoz of there is a variable x in self
print(b . __str__()) # Explicitly calling so it returns 35
print(c . __str__()) # Hyd <next line> None
print(d . __str__(50)) # 50


