'''
PROGRAM_1:
'''
# Identify  error  (Home work)
'''
class c1:
	def m1(self):
		pass
class c2:
	pass
class c3:
'''
# Find  outputs  (Home  work)
class   c1:
	pass
a = c1()
print(id(a))
print(type(a))
print(a.__dict__) 
print(a)
del a
#print(a) -->after object deletion,these is no name defined as a
'''
OUTPUT:
2568541336112
<class '__main__.c1'>
{}
<__main__.c1 object at 0x0000025608FE7230>
'''
#  Find  outputs  (Home  work)
def   m1():
		print('Function')
class   c1:
	def   m1(self):
		print('1st  method')
	def   m1(self):
		print('2nd  method')
	#def   m1(self): method should contain program for operation
a=c1()
a.m1()
m1()
'''
OUTPUT:
2nd method
Function
'''
#  Find  outputs  (Home  work)
class   c1:
	def   m1(self):
		print('No  argument  method')
	def   m1(self , x):
		print('Single  argument  method : ' , x)
	def   m1(self , x , y):
		print('Two  argument  method : ' , x , y)
a = c1()
a . m1(10 , 20)
#a.m1(30) --> c1.m1() missing 1 required positional argument: 'y'
#a.m1() -->c1.m1() missing 2 required positional arguments: 'x' and 'y'
'''
OUTPUT:
Two  argument  method :  10  20
'''
#  Find  outputs  (Home  work)
class   c1:
	def   m1(self):
		print('No  argument  method')
	def   m1(self , x):
		print('Single  argument  method : ' , x)
	def   m1(self , x = 1  , y = 2):
		print('Two  argument  method : ' , x , y)
a = c1()
a.m1(10 , 20)
a.m1(30)
a.m1()
'''
OUTPUT:
Two  argument  method :  10 20
Two  argument  method :  30 2
Two  argument  method :  1 2
'''
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
a=c1()
a.m1()
'''
OUTPUT:
Method  of  third  c1  class
'''
# Find  outputs  (Home  work)
class   c1:
	def   m1(self):
		print('Method  of  first  c1  class')
class   c1:
	def   m1(self):
		print('Method  of  second  c1  class')
class   c1:
	pass
a=c1()
#a.m1() -->c1 object has no method named m1
'''
OUTPUT:
c1 object has no method named m1
'''
#  Find  outputs (Home  work)
class  c1:
        pass
a = c1()
print(a . __dict__)
a . x = 10
print(a . __dict__)
a . y = 20
print(a . __dict__)
a . x = 30
print(a . __dict__)
a . y = 40
print(a . __dict__)
del  a . x
print(a . __dict__)
del  a . y
print(a . __dict__)
del   a
#print(a.__dict__)-->object a is deleted.therefore no dictionary typecasting is possible
'''
OUTPUT:
{}
{'x':10}
{'x':10,y:20}
{'x':30,y:20}
{'x':30,y:40}
{'y':40}
{}
'''
'''  (Home  work)
Write  a  program  to  determine  area  and  perimeter  of  triangle  and  represent  triangle  by  an  object

1) What  is  the  area  of  triangle ?  --->  sqrt(s * (s - a) * (s - b) * (s - c))

2) What  is  the  formula  for  's' ?  --->  (a + b + c) / 2

3) What  is  the  perimeter  of  triangle ?  --->  a + b + c
'''
import  math
class  triangle:
	def  get(self):
		self.a=int(input("Enter side a : "))
		self.b=int(input("Enter side b : "))
		self.c=int(input("Enter side c : "))
	def  test(self):
		if  self.a+self.b>self.c or self.b+self.c>self.a or self.c+self.a>self.b:
			pass
		else:
				print('Not  a  triangle')
				exit()
	def  area(self):
		s=(self.a+self.b+self.c)/2
		return math.sqrt(s*(s-self.a)*(s-self.b)*(s-self.c))
	def  peri(self):
			return self.a+self.b+self.c
obj=triangle()
obj.get()
obj.test()
print('Area : ',obj.area())
print('Perimeter : ',obj.peri())
'''
OUTPUT:
Enter 1st side of the triangle : 3
Enter 2nd side of the triangle : 4
Enter 3rd side of the triangle : 5
Area :  6.0
Perimeter :  12
'''
#  Find  outputs  (Home  work)
class   c1:
	def  m1(self):
		x = 10
		self . x = 20
		print(x)
		print(self . x)
		x += 5
		self.x += 7
	def   m2(self):
		#print(x) -->name x is not defined
		print(self.x)
		self . x += 6
a = c1()
a . m1()
a . m2()
print(a.x)
#print(self.x) -->no self is defined
#print(x) -->no global variable x defined 
'''
OUTPUT:
10
20
27
33
'''
#  Find  outputs (Home  work)
class  Date:
	pass
a=Date()
a.dd=15
a.mm=8
a.yy=1947
print(a)
'''
OUTPUT:
<__main__.Date object at 0x000001867B857230>
'''
'''  (Home  work)
Write  a  program  to  add  two  objects  where  each  object  contains  three  values  and
store  results  in   third  object

1st  object   --->  x = 10 , y = 20 , z = 30

2nd  object --->  x = 40 , y = 50 , z = 60

3rd  object  ---> x = 10 + 40 = 50 , y = 20 + 50 = 70 , z = 30 + 60 = 90
'''
class  Test:
	def   get(self):
		 self.x=int(input("Enter x value : "))
		 self.y=int(input("Enter y value : "))
		 self.z=int(input("Enter z value : "))
	def   add(self,m,n):
		self.x=m.x+n.x
		self.y=m.y+n.y
		self.z=m.z+n.z
	def  disp(self):
		 print('x: ',self.x)
		 print('y: ',self.y)
		 print('z: ',self.z)
a=Test()
b=Test()
c=Test()
print('First  Object')
a.get()
print('Second  Object')
b.get()
c.add(a,b)
print('Addition  results')
c.disp()
'''
OUTPUT:
First  Object
Enter x value : 10
Enter y value : 20
Enter z value : 30
Second  Object
Enter x value : 40
Enter y value : 50
Enter z value : 60
Addition  results
x:  50
y:  70
z:  90
'''
#  Find  outputs (Home  work)
class   c1:
	def  __str__(self):
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
a = c1()
b = c2()
c = c3()
d = c4()
print(a)
#print(b)
#print(c) -->__str__ returned non-string (type NoneType)
#print(d) -->c4.__str__() missing 1 required positional argument: 'x'
print(b.__str__())
print(c.__str__())
print(d.__str__(50))
'''
OUTPUT:
<__main__.Date object at 0x0000025C18D37230>
25
35
Hyd
None
50
'''


