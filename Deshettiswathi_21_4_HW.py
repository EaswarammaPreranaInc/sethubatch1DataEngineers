Q1 #Find  outputs (Home  work)
class c1:
    x = 10
    def __init__(self):
	    self . y = 20
a = c1()
b = c1()
a . x += 1
b . y += 1
print(a . x) #11
print(a . y) #20
print(b . x) #10
print(b . y) #21
print(c1 . x) #10
print(a . __dict__) #{'y': 20, 'x': 11}
print(b . __dict__) #{'y' : 21}
print(c1 . __dict__) #{'__module__': '__main__', 'x': 10, '__init__': <function c1.__init__ at 0x000001D081C4FA30>, '__dict__': <attribute '__dict__' of 'c1' objects>, '__weakref__': <attribute '__weakref__' of 'c1' objects>, '__doc__': None}
#---------------------------------------------------------------------------
Q2 #Find  outputs (Home  work)
class  c1:
	x = 10
	def  m1(self):
		self . x = 20
a = c1()
a . m1()
print(c1 . x) #10
print(a . x)  #20
#--------------------------------------------------------
Q3 #Find  outputs  (Home  work)
class   c1:
	x = 10
	def  __init__(self):
		self . y = 20
	@classmethod
	def   m1(cls):
		cls . x = 30  #class varaible x is modified from 10 to 30
		cls . y = 40  
# End  of  the  class
a = c1()  #a.y=20
b = c1()  #b.y=20
c1 . m1() 
print(a . x) #30
print(a . y) #20
print(b . x) #30
print(b . y) #20
print(c1 . x , c1 . y) #30 40
print(cls . x , cls . y) #error - cls is not defined outside the class
print(self . x , self . y) #error - self is not defined outside the class
#------------------------------------------------------------------------
Q4 #Find  outputs
class   c1:
	@staticmethod
	def   m1(self):
		print(self)
#  End  of  the   class
c1 . m1(25)  #25 
a = c1()
a . m1(35)   #35
#------------------------------------------------------
Q5 #Find  outputs
class   c1:
	def   m1(self):
		print(self)
#  End  of  the   class
c1 . m1(25) #25
a = c1()
a . m1()   #<__main__.c1 object at 0x0000013938757D60>
#a . m1(35) #error - 2 arguments are given -> self and 35
#-----------------------------------------------------------
Q6 #Find  outputs
class   c1:
	@staticmethod
	def   m1(self):
		print('static  method')
		print(self)
	def   m1(self):
		print('instance  method')
		print(self)
#  End  of  the   class
c1 . m1(25) #instance method  <\n> 25
a = c1()
a . m1()    #instance method  <\n> <__main__.c1 object at 0x0000028C35CBBFD0>
#------------------------------------------------------------------------
Q7 #How  to  access  static  variable  in  different  ways  ?
class   c1:
	x = 25
	def   __init__(self):
		print(self.x)  #How  to  print  static  variable  'x'
		print(c1.x)    #How  to  print  static  variable  'x'  in  another  way
		#print(x)       #error - no local variable x 
	def   m1(self):
		print(self.x)  #How  to  print  static  variable  'x'
		print(c1.x)    #How  to  print  static  variable  'x'  in  another  way
		#print(cls . x) #error - cls is not defined
	@classmethod
	def   m2(cls):
		print(cls.x)    #How  to  print  static  variable  'x'
		print(c1.x)     #How  to  print  static  variable  'x'  in  another  way
		#print(self . x) #error - self is not defined
	@staticmethod
	def   m3():
		print(c1.x)      #How  to  print  static  variable  'x'
		#print(cls . x)   #error -  this is not classmethod
		#print(self . x)	  #error - no self argument
# End  of  the  class
print(c1.x)  #How  to  print  static  variable  'x'
m=c1()
print(m.x)  #How  to  print  static  variable  'x'  in  another  way
#print(x)       #error - there is nno global varaible x in the program
#print(self . x) #error- self is not defined
#print(cls . x)  #error - cls is not defined
m.m1() #How  to  call  method  m1()
c1.m2() #How  to  call  method  m2()
c1.m3()  #How  to  call  method  m3()
#-------------------------------------------------------------------------------------------------
Q8 #How  to  add  static  variable  to  the  class  at  different  locations  of  the  program ?
class   c1:
	a=10   #How  to  add  static  variable  'a'  with  value  10
	def    __init__(self):
		c1.b=20  #How  to  add  static  variable  'b'  with  value  20
		self.c=30  #How  to  add  instance  variable  'c'  with  value  30
		#cls . k = 25 #error- cls is not defined in __init__() method
	def   m1(self):
		c1.d=40  #How  to  add  static  variable  'd'  with  value  40
		self.e=50  #How  to  add  instance  variable  'e'  with  value  50
	@classmethod
	def   m2(cls):
		c1.f=60  #How  to  add  static  variable  'f'  with  value  60
		cls.g=70  #How  to  add  static  variable  'g'  with  value  70  in  another  way
		#self . k = 25  #error - self is not defined
	@staticmethod
	def   m3():
		c1.h=80  #How  to  add  static  variable  'h'  with  value  80
		#self . k = 25  #error - self is not defined
		#cls . k = 35    #error - cls is not defined
#End  of  the  class
print('Begin')
print(c1 . __dict__)
print()
print()
x = c1()
print('Constructor')
print(c1 . __dict__)
print()
print()
x.m1()      #How  to  call  m1()  method
print('Instance  method  m1')
print(c1 .__dict__)
print()
print()
c1.m2()      #How  to  call  m2()  method
print('class  method   m2')
print(c1 . __dict__)
print()
print()
c1.m3()         #How  to  call  m3()  method
print('static   method   m3')
print(c1 . __dict__)
print()
print()
c1.i=90   #How  to  add  static  variable  'i'  with  value  90
x.j=100   #How  to  add  instance  variable  'j'  with  value  100
print('Outside  the  class')
print(c1 . __dict__)
print()
print()
print("Object  'x' ")
print(x . __dict__)

OP-
Begin
{'__module__': '__main__', 'a': 10, '__init__': <function c1.__init__ at 0x00000243B154FB50>, 'm1': <function c1.m1 at 0x00000243B154FC70>, 'm2': <classmethod(<function c1.m2 at 0x00000243B154FD90>)>, 'm3': <staticmethod(<function c1.m3 at 0x00000243B154FE20>)>, '__dict__': <attribute '__dict__' of 'c1' objects>, '__weakref__': <attribute '__weakref__' of 'c1' objects>, '__doc__': None}


Constructor
{'__module__': '__main__', 'a': 10, '__init__': <function c1.__init__ at 0x00000243B154FB50>, 'm1': <function c1.m1 at 0x00000243B154FC70>, 'm2': <classmethod(<function c1.m2 at 0x00000243B154FD90>)>, 'm3': <staticmethod(<function c1.m3 at 0x00000243B154FE20>)>, '__dict__': <attribute '__dict__' of 'c1' objects>, '__weakref__': <attribute '__weakref__' of 'c1' objects>, '__doc__': None, 'b': 20}


Instance  method  m1
{'__module__': '__main__', 'a': 10, '__init__': <function c1.__init__ at 0x00000243B154FB50>, 'm1': <function c1.m1 at 0x00000243B154FC70>, 'm2': <classmethod(<function c1.m2 at 0x00000243B154FD90>)>, 'm3': <staticmethod(<function c1.m3 at 0x00000243B154FE20>)>, '__dict__': <attribute '__dict__' of 'c1' objects>, '__weakref__': <attribute '__weakref__' of 'c1' objects>, '__doc__': None, 'b': 20, 'd': 40}


class  method   m2
{'__module__': '__main__', 'a': 10, '__init__': <function c1.__init__ at 0x00000243B154FB50>, 'm1': <function c1.m1 at 0x00000243B154FC70>, 'm2': <classmethod(<function c1.m2 at 0x00000243B154FD90>)>, 'm3': <staticmethod(<function c1.m3 at 0x00000243B154FE20>)>, '__dict__': <attribute '__dict__' of 'c1' objects>, '__weakref__': <attribute '__weakref__' of 'c1' objects>, '__doc__': None, 'b': 20, 'd': 40, 'f': 60, 'g': 70}


static   method   m3
{'__module__': '__main__', 'a': 10, '__init__': <function c1.__init__ at 0x00000243B154FB50>, 'm1': <function c1.m1 at 0x00000243B154FC70>, 'm2': <classmethod(<function c1.m2 at 0x00000243B154FD90>)>, 'm3': <staticmethod(<function c1.m3 at 0x00000243B154FE20>)>, '__dict__': <attribute '__dict__' of 'c1' objects>, '__weakref__': <attribute '__weakref__' of 'c1' objects>, '__doc__': None, 'b': 20, 'd': 40, 'f': 60, 'g': 70, 'h': 80}


Outside  the  class
{'__module__': '__main__', 'a': 10, '__init__': <function c1.__init__ at 0x00000243B154FB50>, 'm1': <function c1.m1 at 0x00000243B154FC70>, 'm2': <classmethod(<function c1.m2 at 0x00000243B154FD90>)>, 'm3': <staticmethod(<function c1.m3 at 0x00000243B154FE20>)>, '__dict__': <attribute '__dict__' of 'c1' objects>, '__weakref__': <attribute '__weakref__' of 'c1' objects>, '__doc__': None, 'b': 20, 'd': 40, 'f': 60, 'g': 70, 'h': 80, 'i': 90}


Object  'x'
{'c': 30, 'e': 50, 'j': 100}
#__---------------------------------------------------------------
Q9 #Find  outputs  (Home  work)
class  c1:
        a , b , c  = range(1 , 4)
# End  of  the  class
print(c1.a)  #How  to  print  variable  'a'
print(c1.b)  #How  to  print  variable  'b'
print(c1.c)  #How  to  print  variable  'c'
#------------------------------------------------------------------------------------
Q10 #What  are  the  outputs  if  inputs  are  10 , 20 , 30 , 40 , 50 , 60 , 70 
class   Test:
	@classmethod
	def  get1(cls):
		cls . x = int(input('Enter  any  number    :  '))
	def  get2(self):
		self . y = int(input('Enter  any  number  :  '))
		self . z = int(input('Enter  any  number  :  '))
	def   compute(self):
		Test . x += 1
		self . y  += 1
		self . z  += 1
		self . x  += 1
	def    disp(self):
		print(Test . x , self . y , self . z ,  self . x , sep = '\t')
# End  of  the  class
Test . get1()
a = Test()
b = Test()
c = Test()
a . get2()
b . get2()
c . get2()
a . compute()
b . compute()
c . compute()
a . disp()
b . disp()
c . disp()

OP-
Enter  any  number    :  1
Enter  any  number  :  3
Enter  any  number  :  4
Enter  any  number  :  2
Enter  any  number  :  5
Enter  any  number  :  4
Enter  any  number  :  8
4       4       5       3
4       3       6       4
4       5       9       5
#--------------------------------------------------------------------------------------------
Q11 Write  a  program  to  add  two  Vector  objects

class  vector:
	@staticmethod
	def get1():
		vector.n=int(input('Enter number of elements: '))  #How  to  read  number  of  elements  into  variable  'n'
	def get2(self):
		self.d=eval(input('Enter a list: ')) #How  to  read  the  list  into  the  object
	def add(self , x , y):
		self.d=[]
		for i in range(vector.n):
			self.d.append(x.d[i]+y.d[i])     #How  add  the  lists  held  by  objects  'x'  and  'y'  and  store  the  results  in  list  held  by  owner  object
vector.get1()       #How  to  call  get1()  method
a=vector()
a.get2()       #How  to  read  the  list  into  1st  object 'a'
b=vector()
b.get2()       #How  to  read  the  list  into  2nd  object  'b'
c=vector()
c.add(a,b)      #How  to  add  the  lists  held  by  objects  'a'  and  'b'  and  store  the  results  in  list  of  3rd  object  'c'
print('Addition results: ',c.d)  #How  to  print  the  list  of  3rd   object

OP-
Enter number of elements: 4
Enter a list: [3,4,1,2]
Enter a list: [4,5,3,2]
Addition results:  [7, 9, 4, 4]
#-------------------------------------------------------------------------------------------------------------------
Q12 Write  a  program  to  print  only  static  variables  but  not  environment  variables  of   classname . __dict__

class  c1:
	x = 1
	y = 2
	z = 3
# End  of  the  class
static_vars = {}
for key, value in c1.__dict__.items():
    if not key.startswith('__'):  
        static_vars[key] = value
print("Static variables of class c1:", static_vars)

OP-
Static variables of class c1: {'x': 1, 'y': 2, 'z': 3}
#----------------------------------------------------------------------------------
Q13 # What  are  k , l ,  x , y , z , m , n , p , q , s ?  
class   c1:
	x = 10  #  What  is  variable  'x'  ---> static variable
	def    m1(self):
		self . y = 20   #  What  is  variable  'y'  ---> instance variable
		z = 30   #  What  is  variable   'z'  ---> local varaible in m1() method
		c1 . m = 40   #  What  is  variable   'm'  ---> static variable
#end of the class
def    f1():
	a = c1()
	a . p = 50   #  What  is   variable  'p'  ---> instance variable
	c1 . q = 60   #  What  is  variable   'q'  ---> static varaible
	s = 70   #  What  is  variable   's'  ---> local variable to function f1()
#end of the function
k = 80   #  What  is  variable 'k'  --->  global variable 
c1 . l = 90   #  What  is  variable  'l'  --->  static variable
b = c1()
b . n = 100   #  What  is  variable  'n' --->  instance variable
