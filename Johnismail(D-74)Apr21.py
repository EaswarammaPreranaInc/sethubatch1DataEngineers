# Find  outputs (Home  work)
'''class c1:
    x = 10 #static variable due to inside the class
    def __init__(self):
	    self . y = 20 #instance variable due to self 
a = c1() #object a is created and constructor will execute
b = c1() #object b is created and constructor will execute
a . x += 1 #static varible is modified to 11
b . y += 1 #static varible is modified to 11
print(a . x)#11
print(a . y) #20
print(b . x) # 10
print(b . y) #21
print(c1 . x) #10
print(a . __dict__) #{y:20,x:11}
print(b . __dict__) #{y:21}
print(c1 . __dict__) #{x:10}

object a--> y=20,

object b-->y=20

# Find  outputs (Home  work)
class  c1:
	x = 10 #ststic variable
	def  m1(self):
		self . x = 20 #instance variable
a = c1() #object is created
a . m1() 
print(c1 . x) #10
print(a . x) #20

#object a--> x=20

# Find  outputs  (Home  work)
class   c1:
	x = 10
	def  __init__(self):
		self . y = 20
	@classmethod
	def   m1(cls):
		cls . x = 30
		cls . y = 40
# End  of  the  class
a = c1() #constructor is executed 
b = c1()
c1 . m1()
print(a . x) #30
print(a . y) #20
print(b . x)#30
print(b . y)#20
print(c1 . x , c1 . y)#(30,40)
#print(cls . x , cls . y)#error only inside classmethod it is used
#print(self . x , self . y)#self is not defined


object a-->y=20

object b-->y=20

static method-->x=30,y=40

#  Find  outputs
class   c1:
	@staticmethod
	def   m1(self):
		print(self)
#  End  of  the   class
c1 . m1(25) #25
a = c1()
a . m1(35) #35

#  Find  outputs
class   c1:
	
	def   m1(self):
		print(self)
#  End  of  the   class
c1 . m1(25) #25
a = c1()
a . m1()#type and adress
a . m1(35)#error

#  Find  outputs
class   c1:
	@staticmethod
	def   m1(self):
		print('static  method')
		print(self)
	def   m1(self):
		print('instance  method')
		print(self)
#  End  of  the   class
c1 . m1(25) #'static  method'  <next line> 25
a = c1()
a . m1() #'instance  method' <next line> type and adress

# How  to  access  static  variable  in  different  ways  ?
class   c1:
	x = 25
	def   __init__(self):
		print(self.x) #How  to  print  static  variable  'x'
		print(c1.x)#How  to  print  static  variable  'x'  in  another  way
		#print(x)
	def   m1(self):
		#print(x)#How  to  print  static  variable  'x'
		print(self.x)#How  to  print  static  variable  'x'  in  another  way
		print(c1 . x)
	@classmethod
	def   m2(cls):
		#print(x)#How  to  print  static  variable  'x'
		print(cls.x)#How  to  print  static  variable  'x'  in  another  way
		#print(self . x)
	@staticmethod
	def   m3():
		pass
		#print(x)#How  to  print  static  variable  'x'
		#print(cls . x)
		#print(self . x)
# End  of  the  class
print(c1.x)#How  to  print  static  variable  'x'
print(x)#How  to  print  static  variable  'x'  in  another  way
print(x)
print(self . x)
print(cls . x)
a=c1()
a.m1()#How  to  call  method  m1()
c1.m2()#How  to  call  method  m2()
c1.m3()#How  to  call  method  m3()

# How  to  add  static  variable  to  the  class  at  different  locations  of  the  program ?
class   c1:
	a=10 #How  to  add  static  variable  'a'  with  value  10
	def    __init__(self):
		c1.b=20 #How  to  add  static  variable  'b'  with  value  20
		self.c=30 #How  to  add  instance  variable  'c'  with  value  30
		#cls . k = 25
	def   m1(self):
		c1.d=40 #How  to  add  static  variable  'd'  with  value  40
		self.e=50 #How  to  add  instance  variable  'e'  with  value  50
	@classmethod
	def   m2(cls):
		cls.f=60 #How  to  add  static  variable  'f'  with  value  60
		c1.g=70 #How  to  add  static  variable  'g'  with  value  70  in  another  way
		#self . k = 25
	@staticmethod
	def   m3():
		c1.h=80 #How  to  add  static  variable  'h'  with  value  80
		#self . k = 25
		#cls . k = 35
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
x.m1()#How  to  call  m1()  method
print('Instance  method  m1')
print(c1 .__dict__)
print()
print()
c1.m2()#How  to  call  m2()  method
print('class  method   m2')
print(c1 . __dict__)
print()
print()
c1.m3()#How  to  call  m3()  method
print('static   method   m3')
print(c1 . __dict__)
print()
print()
c1.i=90 #How  to  add  static  variable  'i'  with  value  90
x.j=100 #How  to  add  instance  variable  'j'  with  value  100
print('Outside  the  class')
print(c1 . __dict__)
print()
print()
print("Object  'x' ")
print(x . __dict__)

outputs---
Begin
{'__module__': '__main__', 'a': 10, '__init__': <function c1.__init__ at 0x000001C40D9B2DD0>, 'm1': <function c1.m1 at 0x000001C40D9B2E60>, 'm2': <classmethod(<function c1.m2 at 0x000001C40D9B2EF0>)>, 'm3': <staticmethod(<function c1.m3 at 0x000001C40D9B2F80>)>, '__dict__': <attribute '__dict__' of 'c1' objects>, '__weakref__': <attribute '__weakref__' of 'c1' objects>, '__doc__': None}


Constructor
{'__module__': '__main__', 'a': 10, '__init__': <function c1.__init__ at 0x000001C40D9B2DD0>, 'm1': <function c1.m1 at 0x000001C40D9B2E60>, 'm2': <classmethod(<function c1.m2 at 0x000001C40D9B2EF0>)>, 'm3': <staticmethod(<function c1.m3 at 0x000001C40D9B2F80>)>, '__dict__': <attribute '__dict__' of 'c1' objects>, '__weakref__': <attribute '__weakref__' of 'c1' objects>, '__doc__': None, 'b': 20}


Instance  method  m1
{'__module__': '__main__', 'a': 10, '__init__': <function c1.__init__ at 0x000001C40D9B2DD0>, 'm1': <function c1.m1 at 0x000001C40D9B2E60>, 'm2': <classmethod(<function c1.m2 at 0x000001C40D9B2EF0>)>, 'm3': <staticmethod(<function c1.m3 at 0x000001C40D9B2F80>)>, '__dict__': <attribute '__dict__' of 'c1' objects>, '__weakref__': <attribute '__weakref__' of 'c1' objects>, '__doc__': None, 'b': 20, 'd': 40, 'e': 50}


class  method   m2
{'__module__': '__main__', 'a': 10, '__init__': <function c1.__init__ at 0x000001C40D9B2DD0>, 'm1': <function c1.m1 at 0x000001C40D9B2E60>, 'm2': <classmethod(<function c1.m2 at 0x000001C40D9B2EF0>)>, 'm3': <staticmethod(<function c1.m3 at 0x000001C40D9B2F80>)>, '__dict__': <attribute '__dict__' of 'c1' objects>, '__weakref__': <attribute '__weakref__' of 'c1' objects>, '__doc__': None, 'b': 20, 'd': 40, 'e': 50, 'f': 60, 'g': 70}


static   method   m3
{'__module__': '__main__', 'a': 10, '__init__': <function c1.__init__ at 0x000001C40D9B2DD0>, 'm1': <function c1.m1 at 0x000001C40D9B2E60>, 'm2': <classmethod(<function c1.m2 at 0x000001C40D9B2EF0>)>, 'm3': <staticmethod(<function c1.m3 at 0x000001C40D9B2F80>)>, '__dict__': <attribute '__dict__' of 'c1' objects>, '__weakref__': <attribute '__weakref__' of 'c1' objects>, '__doc__': None, 'b': 20, 'd': 40, 'e': 50, 'f': 60, 'g': 70, 'h': 80}


Outside  the  class
{'__module__': '__main__', 'a': 10, '__init__': <function c1.__init__ at 0x000001C40D9B2DD0>, 'm1': <function c1.m1 at 0x000001C40D9B2E60>, 'm2': <classmethod(<function c1.m2 at 0x000001C40D9B2EF0>)>, 'm3': <staticmethod(<function c1.m3 at 0x000001C40D9B2F80>)>, '__dict__': <attribute '__dict__' of 'c1' objects>, '__weakref__': <attribute '__weakref__' of 'c1' objects>, '__doc__': None, 'b': 20, 'd': 40, 'e': 50, 'f': 60, 'g': 70, 'h': 80, 'i': 90}


Object  'x'
{'c': 30, 'j': 100}


# Find  outputs  (Home  work)
class  c1:
        a , b , c  = range(1 , 4)
# End  of  the  class
print(c1.a) #How  to  print  variable  'a'
print(c1.b) #How  to  print  variable  'b'
print(c1.c) #How  to  print  variable  'c'

outputs--
1
2
3

# What  are  the  outputs  if  inputs  are  10 , 20 , 30 , 40 , 50 , 60 , 70 (Home  work)
class   Test:
	@classmethod
	def  get1(cls):
		cls . x = int(input('Enter  any  number    :  ')) #10
	def  get2(self):
		self . y = int(input('Enter  any  number  :  ')) #a.y=20,b.y=40,c.y=60
		self . z = int(input('Enter  any  number  :  ')) #a.z=30,b.z=50,c.z=70
	def   compute(self):
		Test . x += 1 #11
		self . y  += 1 #41
		self . z  += 1 #51
		self . x  += 1 #13
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

outputs--
1st--13 21 31 12
2nd--13 41 51 13
3rd--13 61 71 14


Write  a  program  to  add  two  Vector  objects

1) What  are  the  names  of  objects ?  ---> x , y   and  z

2) What  are  the  names  of   lists  held  by  each  object ?  --->  x .  a , y . a  , z . a

3) How  to  access  elements  of  1st  list ?  --->  x . a[i]
    How  to  access  elements  of  2nd  list ?  --->  y . a[i]

4) How  to  access  static  variable  'n' ?  --->  vector . n

class  vector:
	@staticmethod
	def get1():
		vector.n=int(input('enter no of elements:')) #How  to  read  number  of  elements  into  variable  'n'
	def get2(self):
		self.d=eval(input('enter list elements:'))#How  to  read  the  list  into  the  object
	def add(self , x , y):
		self.d=[]
		for i in range(vector.n):
				self.d.append(a.d[i]+b.d[i]) #How  add  the  lists  held  by  objects  'x'  and  'y'  and  store  the  results  in  list  held  by  owner  object
a=vector()
vector.get1() #How  to  call  get1()  method
a.get2() #How  to  read  the  list  into  1st  object
b=vector()
b.get2() #How  to  read  the  list  into  2nd  object  'b'
c=vector()
c.add(a,b)#How  to  add  the  lists  held  by  objects  'a'  and  'b'  and  store  the  results  in  list  of  3rd  object  'c'
print(c.d) #How  to  print  the  list  of  3rd   object

outputs--
enter no of elements:4
enter list elements:[1,2,3,5]
enter list elements:[4,5,6,7]
[5, 7, 9, 12]


Write  a  program  to  print  only  static  variables  but  not  environment  variables  of   classname . __dict__

Hint:  Use  startswith()  and  endswith()  methods
'''
class  c1:
	x = 1
	y = 2
	z = 3
a={}
b=(c1.__dict__)
for key in b:
	if not key.startswith('__') and not key.endswith('__'):
				 a[key]=b[key]
print('static varibles:',a)	
outputs--
static varibles: {'x': 1, 'y': 2, 'z': 3}
#  End  of  the  class'''
