# Identify  error  (Home work)
'''class   c1:
	def  m1(self):
		pass
class   c2:
        pass
class   c3:#must have some arguments indentation


# Find  outputs  (Home  work)
class   c1:
	pass
# End  of  the  class
a = c1()
print(id(a))#same adress of object a
print(type(a))#<class '__main__.a')
print(a . __dict__) #{}
print(a)#type and adress
del  a #object a is deleted
print(a)#nothing error

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
a = c1()#object is created name a
a . m1()#3rd method
m1()#Function

#  Find  outputs  (Home  work)
class   c1:
	def   m1(self):
		print('No  argument  method')
	def   m1(self , x):
		print('Single  argument  method : ' , x)
	def   m1(self , x , y):
		print('Two  argument  method : ' , x , y)
# End  of  class  c1
a = c1()#object a is created
a . m1(10 , 20)#'Two  argument  method : ' , 10,20)
a . m1(30)#error 
a . m1()#error

#  Find  outputs  (Home  work)
class   c1:
	def   m1(self):
		print('No  argument  method')
	def   m1(self , x):
		print('Single  argument  method : ' , x)
	def   m1(self , x = 1  , y = 2):
		print('Two  argument  method : ' , x , y)
# End  of  class  c1
a = c1()#object a is created
a . m1(10 , 20)#('Two  argument  method : ' , 10,20)
a . m1(30)#('Two  argument  method : ' , 30,2)
a . m1()#('Two  argument  method : ' , 1,2)

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
a = c1()#object a is created
a . m1()#('Method  of  third  c1  class')

# Find  outputs  (Home  work)
class   c1:
	def   m1(self):
		print('Method  of  first  c1  class')
class   c1:
	def   m1(self):
		print('Method  of  second  c1  class')
class   c1:
	pass
a = c1()#object a is created
a . m1()#error bcoz c1 has no method m1()

#  Find  outputs (Home  work)
class  c1:
        pass
# End  of  class
a = c1()
print(a . __dict__)#{}
a . x = 10
print(a . __dict__)#{x:10}
a . y = 20
print(a . __dict__)#{x:10,y:20}
a . x = 30
print(a . __dict__)#{x:30,y:20}
a . y = 40
print(a . __dict__)#{x:30,y:40}
del  a . x
print(a . __dict__)#{y:40}
del  a . y
print(a . __dict__)#{}
del   a
print(a . __dict__)#error

#  Find  outputs  (Home  work)
class   c1:
	def  m1(self):#self is a
		x = 10
		self . x = 20
		print(x)#10
		print(self . x)#20
		x += 5 #15
		self . x += 7 #27
	def   m2(self):
		#print(x)#15
		print(self . x)#27
		self . x += 6 #
# End  of  the  class
a = c1()#object a is created
a . m1()#
a . m2()
print(a . x)#33
#print(self . x)#error self is not defined
print(x)#error

#  Find  outputs (Home  work)
class  Date:
	pass
# End of the class
a =  Date()#object a is created
a . dd = 15
a . mm = 8
a . yy = 1947
print(a)#type and adreess

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
a = c1()#objet a is created
b = c2()#object b is created
c = c3()#object c is created
d = c4()#object d is created
print(a)#'25'
#print(b)#error due to int 35
#print(c)#error due to none type
#print(d)#error
print(b . __str__())#'35'
print(c . __str__())#'Hyd',None
print(d . __str__(50))#50

'''
'''  (Home  work)
Write  a  program  to  determine  area  and  perimeter  of  triangle  and  represent  triangle  by  an  object

1) What  is  the  area  of  triangle ?  --->  sqrt(s * (s - a) * (s - b) * (s - c))

2) What  is  the  formula  for  's' ?  --->  (a + b + c) / 2

3) What  is  the  perimeter  of  triangle ?  --->  a + b + c

import  math
s=5
class  triangle:
	def  get(self):
		self.x=int(input('enter first side:'))
		self.y=int(input('enter Second side:'))
		self.z=int(input('enter Third side:'))
	def  test(self):
		if  self.x + self.y>=self.z and self.x +self.z>=self.y and self.y+self.z>=self.x:
																pass
		else:
				print('Not  a  triangle')
				exit()
	def  area(self):
			s=(self.x+self.y+self.z)/2
			return   math.sqrt(s * (s - self.x) * (s - self.y) * (s - self.z))
	def  peri(self):
			return  (self.x + self.y + self.z)
# End of the class
a=triangle()
a.get()
a.test()
print('Area : ',a.area())
print('Perimeter : ',a.peri() )

outputs--
Area:6.0
Perimeter:12

  (Home  work)
Write  a  program  to  add  two  objects  where  each  object  contains  three  values  and
store  results  in   third  object

1st  object   --->  x = 10 , y = 20 , z = 30

2nd  object --->  x = 40 , y = 50 , z = 60

3rd  object  ---> x = 10 + 40 = 50 , y = 20 + 50 = 70 , z = 30 + 60 = 90
'''
class  c1():
	def   get(self):
		 self.x=int(input('enter first value:'))
		 self.y =int(input('enter first value:'))
		 self.z=int(input('enter first value:'))#How  to  read  inputs  into  variables  x , y  and  z  of  object  self
	def   add(self , m , n):
		 self.x=m.x+n.x
		 self.y=m.y+n.y
		 self.z=m.z+n.z #How  to  add  objects  m  and  n  and  store  results  in  object  self
	def  disp(self):
			print('x:',self.x)
			print('y:',self.y)
			print('z:',self.z)
		 
# End  of  the  class
a=c1()
b=c1()
c=c1() #How  to  create  three  Test  class  objects  a , b  and  c
print('First  Object')
a.get() #How  to  read  inputs  into  object  'a'
print('Second  Object')
b.get() #How  to  read  inputs  into  object  'b'
c.add(a,b) #How  to  add  objects  a  and  b  and  store  results in  object  'c'
print('Addition  results')
c.disp() #How  to  print  object  'c'

outputs--

First  Object
enter first value:10
enter first value:20
enter first value:30
Second  Object
enter first value:40
enter first value:50
enter first value:60
Addition  results
x: 50
y: 70
z: 90
