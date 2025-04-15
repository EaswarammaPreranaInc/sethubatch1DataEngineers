# Identify  error  (Home work)
class   c1:
	def  m1(self):
		pass
class   c2:
        pass
class   c3:
	#pass
"""
Output:
Error is at c3 due to the no method is defined or pass
"""

# Find  outputs  (Home  work)
class   c1:
	pass
# End  of  the  class
a = c1()
print(id(a))
print(type(a))
print(a .__dict__) 
print(a)
del  a
#print(a)
"""
Output:
3068689148496
<class '__main__.c1'>
{}
<__main__.c1 object at 0x000002CA7C206A50>
"""

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
"""
Output:
3rd  method
Function
"""


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
#a . m1(30)
#a . m1()
"""
Output:
Two  argument  method :  10 , 20
"""

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
"""
Output:
Two  argument  method :10,20
Two  argument  method :30,2
Two  argument  method :1,2
"""

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

"""
Output:
Method  of  third  c1  class
"""



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
a . m1()
"""
Output:
Method  of  second  c1  class
"""

#  Find  outputs (Home  work)
class  c1:
        pass
# End  of  class
a = c1()
print(a .__dict__)
a . x = 10
print(a .__dict__)
a . y = 20
print(a .__dict__)
a . x = 30
print(a .__dict__)
a . y = 40
print(a .__dict__)
del  a . x
print(a .__dict__)
del  a . y
print(a .__dict__)
del   a
#print(a .__dict__)
"""
Output:
{}
{'x': 10}
{'x': 10, 'y': 20}
{'x': 30, 'y': 20}
{'x': 30, 'y': 40}
{'y': 40}
{}
"""


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

"""
Output:
10
20
27
33
"""

#(Home  work)
#Write  a  program  to  determine  area  and  perimeter  of  triangle  and  represent  triangle  by  an  object
#1) What  is  the  area  of  triangle ?  --->  sqrt(s * (s - a) * (s - b) * (s - c))
#2) What  is  the  formula  for  's' ?  --->  (a + b + c) / 2
#3) What  is  the  perimeter  of  triangle ?  --->  a + b + c

import  math
class  triangle:
	def  get(self,x,y,z):
		self.x=x
		self.y=y
		self.z=z                  #How  to  read  three  sides  into  object  self
	def  test(self):
		if  (self.x+self.y>z) or (self.x+self.z>y) or (self.z+self.y>x): #sum  of  every  2  sides  >=  3rd  side:
				pass        #Do  nothing
		else:
			print('Not  a  triangle')
			#break                 #How  to  stop  execution
	def  area(self):
			s=(x+y+x)/2
			return  math.sqrt(s * (s - self.x) * (s - self.y) * (s - self.z))     #return   area  of  triangle
	def  peri(self):
			return self.x+self.y+self.z      #return  perimeter  of  triangle
# End of the class
x=int(input("Enter the First side: "))
y=int(input("Enter the Second side: "))
z=int(input("Enter the Third side: "))

a=triangle()
a.get(x,y,z)
Area=a.area()
Peri=a.peri()
print(F'Area : ', Area)
print(F'Perimeter : ',  Peri)
"""
Output:
Enter the First side: 5
Enter the Second side: 5
Enter the Third side: 5
Area :  10.825317547305483
Perimeter :  15
"""

'''  (Home  work)
Write  a  program  to  add  two  objects  where  each  object  contains  three  values  and
store  results  in   third  object

1st  object   --->  x = 10 , y = 20 , z = 30

2nd  object --->  x = 40 , y = 50 , z = 60

3rd  object  ---> x = 10 + 40 = 50 , y = 20 + 50 = 70 , z = 30 + 60 = 90
'''
class  Test:
	def   get(self,x,y,z):
		 self.x=x
		 self.y=y
		 self.z=z       
	def   add(self , m , n):
		 self.x=m.x+n.x 
		 self.y=m.y+n.y
		 self.z=m.z+n.z    
	def  disp(self):
		 return f"x={self.x},y={self.y},z={self.z}"   #How  to  print  object  self
# End  of  the  class
a=Test()
b=Test()
c=Test()#How  to  create  three  Test  class  objects  a , b  and  c
print('First  Object')
a.get(10,20,30) 
print(a.disp())#How  to  read  inputs  into  object  'a'
print('Second  Object')
b.get(40,50,60)#How  to  read  inputs  into  object  'b'
print(b.disp())
#How  to  add  objects  a  and  b  and  store  results in  object  'c'
c.add(a,b)
print('Addition  results')
print(c.disp())#How  to  print  object  'c'

"""
Output:
First  Object
x=10,y=20,z=30
Second  Object
x=40,y=50,z=60
Addition  results
x=50,y=70,z=90
"""


#  Find  outputs (Home  work)
class  Date:
	pass
# End of the class
a =  Date()
a . dd = 15
a . mm = 8
a . yy = 1947
print(a)
"""
Output:
type and address of class Date
<__main__.Date object at 0x000002482D5A6A50>
"""

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
print(b)
print(c)
print(d)
print(b . _str_())
print(c . _str_())
print(d . _str_(50))
"""
Output:
Type and Address of c1
Type and Address of c2
Type and Address of c3
Type and Address of c4
35
Hyd
None
50
"""
