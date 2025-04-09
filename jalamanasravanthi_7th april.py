# 1
# Identify  error  (Home work)
class   c1:
	def  m1(self):
		pass
class   c2:
        pass
#class   c3:# pass is missing here

# 2
# Find  outputs  (Home  work)
class   c1:
	pass
# End  of  the  class
a = c1()
print(id(a)) #id address
print(type(a)) # <class '_main_.c1'>
print(a . _dict_) #{} cz there is no 
print(a) # <_main_.c1 object at 0x000001EB0AD86A50>
del  a
#print(a) # error due to 'a' is not defined

'''
Output:
2109010897488
<class '_main_.c1'>
{}
<_main_.c1 object at 0x000001EB0AD86A50>
'''

# 3
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
a = c1()
a . m1()
m1()

Output:
3rd method
function

# 4
#  Find  outputs  (Home  work)
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
#a . m1(30) # missing 1 required positional argument: 'y'
# a . m1() #  missing 2 required positional arguments: 'x' and 'y'

Output:
Two  argument  method :  10 20

# 5
#  Find  outputs  (Home  work)
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

Output:
Two  argument  method :  10 20
Two  argument  method :  30 2
Two  argument  method :  1 2

# 6
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
a = c1()
a . m1()

Output:
Method  of  third  c1  class

# 7
# Find  outputs  (Home  work)
class   c1:
	def   m1(self):
		print('Method  of  first  c1  class')
class   c1:
	def   m1(self):
		print('Method  of  second  c1  class')
class   c1:
	pass
a = c1()
# a . m1() #'c1' object has no attribute 'm1'

# 8
#  Find  outputs (Home  work)
class  c1:
        pass
# End  of  class
a = c1()
print(a . _dict_)
a . x = 10
print(a . _dict_)
a . y = 20
print(a . _dict_)
a . x = 30
print(a . _dict_)
a . y = 40
print(a . _dict_)
del  a . x
print(a . _dict_)
del  a . y
print(a . _dict_)
del   a
#print(a . _dict_) #name 'a' is not defined

Output:
{}
{'x': 10}
{'x': 10, 'y': 20}
{'x': 30, 'y': 20}
{'x': 30, 'y': 40}
{'y': 40}
{}

# 9
'''  (Home  work)
Write  a  program  to  determine  area  and  perimeter  of  triangle  and  represent  triangle  by  an  object

1) What  is  the  area  of  triangle ?  --->  sqrt(s * (s - a) * (s - b) * (s - c))

2) What  is  the  formula  for  's' ?  --->  (a + b + c) / 2

3) What  is  the  perimeter  of  triangle ?  --->  a + b + c
'''
import  math
class  triangle:
	def  get(self):
		How  to  read  three  sides  into  object  self
	def  test(self):
		if  sum  of  every  2  sides  >=  3rd  side:
				Do  nothing
		 else:
				print('Not  a  triangle')
				How  to  stop  execution
	def  area(self):
			return   area  of  triangle
	def  peri(self):
			return  perimeter  of  triangle
# End of the class
How  to  create  triangle  class  object
How  to  read  inputs  into  object
How  to  test  whether  inputs  are  valid
print('Area : ',   ???)
print('Perimeter : ',  ???)

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
t = triangle()        # create triangle object
t.get()               # read inputs
t.test()              # check if it's a valid triangle

print('Area :', t.area())
print('Perimeter :', t.peri())

Output:
Enter side a: 5
Enter side b: 6
Enter side c: 7
Area : 14.696938456699069
Perimeter : 18.0


# 10
#  Find  outputs  (Home  work)
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
a . m2()
print(a . x)
#print(self . x)
#print(x)

# 11
'''  (Home  work)
Write  a  program  to  add  two  objects  where  each  object  contains  three  values  and
store  results  in   third  object

1st  object   --->  x = 10 , y = 20 , z = 30

2nd  object --->  x = 40 , y = 50 , z = 60

3rd  object  ---> x = 10 + 40 = 50 , y = 20 + 50 = 70 , z = 30 + 60 = 90
'''
class  Test:
	def   get(self):
		 How  to  read  inputs  into  variables  x , y  and  z  of  object  self
	def   add(self , m , n):
		 How  to  add  objects  m  and  n  and  store  results  in  object  self
	def  disp(self):
		 How  to  print  object  self
# End  of  the  class
How  to  create  three  Test  class  objects  a , b  and  c
print('First  Object')
How  to  read  inputs  into  object  'a'
print('Second  Object')
How  to  read  inputs  into  object  'b'
How  to  add  objects  a  and  b  and  store  results in  object  'c'
print('Addition  results')
How  to  print  object  'c'


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
a.disp()
print("Addition Results:")
c.disp()

Output:
First Object:
Enter x: 10
Enter y: 20
Enter z: 30
Second Object:
Enter x: 40
Enter y: 50
Enter z: 60
Addition Results:
x = 50, y = 70, z = 90

# 12
#  Find  outputs (Home  work)
class  Date:
	pass
# End of the class
a =  Date()
a . dd = 15
a . mm = 8
a . yy = 1947
print(a)


output:
<_main_.Date object at 0x000001A940B56A50>


# 13
#  Find  outputs (Home  work)
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
#print(b) #type error
#print(c)
#print(d)#  missing 1 required positional argument: 'x'
print(b . _str_())
print(c . _str_())
print(d . _str_(50))

Output:
25
35
Hyd
None
50
