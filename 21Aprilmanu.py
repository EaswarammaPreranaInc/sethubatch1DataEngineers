'''
# Find  outputs (Home  work)
class c1:
    x = 10 # Adds static variable 'x' to class c1 with value 10
    def __init__(self):
	    self . y = 20 # Adds variable 'y' to object self with value 20
a = c1() # object is initialized with y = 20 by constructor.
b = c1() # object is initialized with y = 20 by constructor
a . x += 1 # variable 'x' is incremented by 1 
b . y += 1 # variable 'y' is incremented by 1 
print(a . x) # static variable as there is no variable 'x' in object 'a' i.e, 10.
print(a . y) # static variable as there is no variable 'y' in object 'a' i.e, 20.
print(b . x)  # static variable as there is no variable 'x' in object 'b' i.e, 11.
print(b . y) # static variable as there is no variable 'y' in object 'b' i.e, 21.
print(c1 . x) # static variable as there is no variable 'x' in class c1 i.e, 10.
print(a . __dict__) # {'y': 20, 'x': 11}
print(b . __dict__) # {'y': 21}
print(c1 . __dict__) # {'__module__': '__main__', '__firstlineno__': 2, 'x': 10, '__init__': <function c1.__init__ at 0x000001BD784BF060>, '__static_attributes__': ('y',), '__dict__': <attribute '__dict__' of 'c1' objects>, '__weakref__': <attribute '__weakref__' of 'c1' objects>, '__doc__': None}


static variable ----> x = 10

object 'a' ----> y = 20, x = 11

object 'b' ----> y = 21



output:-
---------
11
20
10
21
10
{'y': 20, 'x': 11}
{'y': 21}
{'__module__': '__main__', '__firstlineno__': 2, 'x': 10, '__init__': <function c1.__init__ at 0x000001BD784BF060>, '__static_attributes__': ('y',), '__dict__': <attribute '__dict__' of 'c1' objects>, '__weakref__': <attribute '__weakref__' of 'c1' objects>, '__doc__': None}


#2) Find  outputs (Home  work)
class  c1:
	x = 10 # Adds static variable 'x' to class c1 with value 10
	def  m1(self):
		self . x = 20 # Adds variable 'x' to object self with value 20
a = c1() # object is initialized with x = 20 by constructor.
a . m1() # method m1 is calling through the object 'a'.
print(c1 . x) # 10 
print(a . x) # 20

output:-
--------
10
20

#3)Find  outputs  (Home  work)
class   c1:
	x = 10 # Adds static variable 'x' to class c1 with value 10
	def  __init__(self):
		self . y = 20 # Adds variable 'y' to object self with value 20
	@classmethod # classmethod is created here 
	def   m1(cls):
		cls . x = 30 # Adds variable 'x' to object cls of class method()  with value 30
		cls . y = 40 # Adds variable 'y' to object cls of class method()  with value 40
# End  of  the  class
a = c1() # object is initialized with y = 20 by constructor.
b = c1() # object is initialized with y = 20 by constructor.
c1 . m1() # calling m1 method() of classmethod()
print(a . x) # 30
print(a . y) # 20
print(b . x) # 30
print(b . y) # 20
print(c1 . x , c1 . y) # 30, 40 
#print(cls . x , cls . y) #  no 'cls' outside the class
#print(self . x , self . y)#  no 'self' outside the class


static variable ---> x = 30 , y = 40
object 'a' -----> y = 20
object 'b' -----> y = 20

output:-
-----------
30
20
30
20
30 40

#4)  Find  outputs
class   c1:
	@staticmethod # staticmethod is created here
	def   m1(self):
		print(self)
#  End  of  the   class
c1 . m1(25) # static method bcz it is called thrw classname c1 with self 25.
a = c1() # object is initialized by constructor.
a . m1(35) # static method bcz it is called thrw classname c1 with self 35.


output:-
---------
25
35


#5) Find  outputs
class   c1:
	def   m1(self):
		print(self) # type and address of the object self .
#  End  of  the   class
c1 . m1(25) # static method bcz it is called thrw classname c1 with self 25.
a = c1() # object is initialized by constructor.
a . m1() # method m1 is calling through object 'a' so consider as a instance method.
#a . m1(35) # Error: due to argument 35.

output:-
----------
25
<__main__.c1 object at 0x00000289099C6A50>


#6)  Find  outputs
class   c1:
	@staticmethod
	def   m1(self): # it is discarded .
		print('static  method') 
		print(self)
	def   m1(self): # consider this method.
		print('instance  method') # instance  method
		print(self) # <__main__.c1 object at 0x0000024947F26A50>
#  End  of  the   class
c1 . m1(25) # 25-------> static method bcz it is called thrw classname c1 with self 25.
a = c1() # object is initialized by constructor.
a . m1() # instance method m1 is calling through object 'a'.

output:-
-------------
instance  method
25
instance  method
<__main__.c1 object at 0x0000024947F26A50>


#7)How  to  access  static  variable  in  different  ways  ?
class   c1:
	x = 25
	def   __init__(self):
		print(c1.x) #How  to  print  static  variable  'x'
		print(self.x) #How  to  print  static  variable  'x'  in  another  way
		#print(x) # Error: due to No local variable 'x' .

	def   m1(self):
		print(c1. x) #How  to  print  static  variable  'x'
		print(self.x) #How  to  print  static  variable  'x'  in  another  way
		#print(cls . x) # Error : due to No cls in m1() method
	@classmethod
	def   m2(cls):
		print(cl .x) #How  to  print  static  variable  'x'
		print(c1s .x) #How  to  print  static  variable  'x'  in  another  way
		#print(self . x) # Error : NO self in m1() method
	@staticmethod
	def   m3():
		print( c1.x) #How  to  print  static  variable  'x'
		#print(cls . x) # Error : NO cls in m3() method
		#print(self . x) # Error : NO self in m3() method
# End  of  the  class
a = c1() 
print(c1.x) # How  to  print  static  variable  'x'
print(a.x)# How  to  print  static  variable  'x'  in  another  way
#print(x) # Error : No global variable 'x' in the program.
#print(self . x) # Error : NO self outside the class
#print(cls . x) # Error : NO cls outside the class.
a.m1() # How  to  call  method  m1()
c1.m2 () # How  to  call  method  m2()
c1.m3() # How  to  call  method  m3()


output:-
--------------
25
25
25
25

#8) How  to  add  static  variable  to  the  class  at  different  locations  of  the  program ?
class   c1:
	a = 10 # How  to  add  static  variable  'a'  with  value  10
	def    __init__(self):
		c1.b = 20 # How  to  add  static  variable  'b'  with  value  20
		self . c = 30 # How  to  add  instance  variable  'c'  with  value  30
		#cls . k = 25 # Error: No cls in constructor
	def   m1(self):
		c1.d = 40 # How  to  add  static  variable  'd'  with  value  40
		self . e = 50 # How  to  add  instance  variable  'e'  with  value  50
	@classmethod
	def   m2(cls):
		c1  . f = 60 # How  to  add  static  variable  'f'  with  value  60
		cls . g = 70 # How  to  add  static  variable  'g'  with  value  70  in  another  way
		#self . k = 25 # Error : No self in m2() method.
	@staticmethod
	def   m3():
		c1 . h  = 80 # How  to  add  static  variable  'h'  with  value  80
		#self . k = 25 # Error :No self in m3() method.
		#cls . k = 35 # Error : No cls in m3() method.
#End  of  the  class
print('Begin')
print(c1 . __dict__)
print()
print()
x = c1() # object is initialised with c = 30 by constructor.
print('Constructor')
print(c1 . __dict__)# {'a': 10 ,'b': 20}
print()
print()
x . m1() # How  to  call  m1()  method
print('Instance  method  m1')
print(c1 .__dict__) # {'a': 10 ,'b': 20 , 'd': 40} 
print()
print()
c1. m2() #How  to  call  m2()  method
print('class  method   m2')
print(c1 . __dict__) # {'a': 10 ,'b': 20,'d': 40 ,'f': 60, 'g' : 70}
print()
print()
c1 . m3() # How  to  call  m3()  method
print('static   method   m3')
print(c1 . __dict__) # {'a': 10 ,'b': 20,'d': 40 ,'f': 60, 'g' : 70, 'h' : 80}
print()
print()
c1 . i = 90 # How  to  add  static  variable  'i'  with  value  90
x . j = 100 # How  to  add  instance  variable  'j'  with  value  100
print('Outside  the  class')
print(c1 . __dict__)# {'a': 10 ,'b': 20,'d': 40 ,'f': 60, 'g' : 70, 'h' : 80, 'i': 90}
print()
print()
print("Object  'x' ") # {'c': 30 ,'e': 50,'j': 100 }
print(x . __dict__)

output:-
------------
Begin
{'__module__': '__main__', '__firstlineno__': 505, 'a': 10, '__init__': <function c1.__init__ at 0x000001E6516CF060>, 'm1': <function c1.m1 at 0x000001E6516E80E0>, 'm2': <classmethod(<function c1.m2 at 0x000001E6516E8180>)>, 'm3': <staticmethod(<function c1.m3 at 0x000001E6516E8220>)>, '__static_attributes__': ('c', 'e'), '__dict__': <attribute '__dict__' of 'c1' objects>, '__weakref__': <attribute '__weakref__' of 'c1' objects>, '__doc__': None}


Constructor
{'__module__': '__main__', '__firstlineno__': 505, 'a': 10, '__init__': <function c1.__init__ at 0x000001E6516CF060>, 'm1': <function c1.m1 at 0x000001E6516E80E0>, 'm2': <classmethod(<function c1.m2 at 0x000001E6516E8180>)>, 'm3': <staticmethod(<function c1.m3 at 0x000001E6516E8220>)>, '__static_attributes__': ('c', 'e'), '__dict__': <attribute '__dict__' of 'c1' objects>, '__weakref__': <attribute '__weakref__' of 'c1' objects>, '__doc__': None, 'b': 20}


Instance  method  m1
{'__module__': '__main__', '__firstlineno__': 505, 'a': 10, '__init__': <function c1.__init__ at 0x000001E6516CF060>, 'm1': <function c1.m1 at 0x000001E6516E80E0>, 'm2': <classmethod(<function c1.m2 at 0x000001E6516E8180>)>, 'm3': <staticmethod(<function c1.m3 at 0x000001E6516E8220>)>, '__static_attributes__': ('c', 'e'), '__dict__': <attribute '__dict__' of 'c1' objects>, '__weakref__': <attribute '__weakref__' of 'c1' objects>, '__doc__': None, 'b': 20, 'd': 40}


class  method   m2
{'__module__': '__main__', '__firstlineno__': 505, 'a': 10, '__init__': <function c1.__init__ at 0x000001E6516CF060>, 'm1': <function c1.m1 at 0x000001E6516E80E0>, 'm2': <classmethod(<function c1.m2 at 0x000001E6516E8180>)>, 'm3': <staticmethod(<function c1.m3 at 0x000001E6516E8220>)>, '__static_attributes__': ('c', 'e'), '__dict__': <attribute '__dict__' of 'c1' objects>, '__weakref__': <attribute '__weakref__' of 'c1' objects>, '__doc__': None, 'b': 20, 'd': 40, 'f': 60, 'g': 70}


static   method   m3
{'__module__': '__main__', '__firstlineno__': 505, 'a': 10, '__init__': <function c1.__init__ at 0x000001E6516CF060>, 'm1': <function c1.m1 at 0x000001E6516E80E0>, 'm2': <classmethod(<function c1.m2 at 0x000001E6516E8180>)>, 'm3': <staticmethod(<function c1.m3 at 0x000001E6516E8220>)>, '__static_attributes__': ('c', 'e'), '__dict__': <attribute '__dict__' of 'c1' objects>, '__weakref__': <attribute '__weakref__' of 'c1' objects>, '__doc__': None, 'b': 20, 'd': 40, 'f': 60, 'g': 70, 'h': 80}


Outside  the  class
{'__module__': '__main__', '__firstlineno__': 505, 'a': 10, '__init__': <function c1.__init__ at 0x000001E6516CF060>, 'm1': <function c1.m1 at 0x000001E6516E80E0>, 'm2': <classmethod(<function c1.m2 at 0x000001E6516E8180>)>, 'm3': <staticmethod(<function c1.m3 at 0x000001E6516E8220>)>, '__static_attributes__': ('c', 'e'), '__dict__': <attribute '__dict__' of 'c1' objects>, '__weakref__': <attribute '__weakref__' of 'c1' objects>, '__doc__': None, 'b': 20, 'd': 40, 'f': 60, 'g': 70, 'h': 80, 'i': 90}


Object  'x'
{'c': 30, 'e': 50, 'j': 100}

#9) Find  outputs  (Home  work)
class  c1:
        a , b , c  = range(1 , 4) # unpacking range objects heres.
# End  of  the  class
print(c1.a) #How  to  print  variable  'a'
print(c1.b) # How  to  print  variable  'b'
print(c1.c) #How  to  print  variable  'c'

output:-
--------
1
2
3



#10)What  are  the  outputs  if  inputs  are  10 , 20 , 30 , 40 , 50 , 60 , 70 (Home  work)
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
		self . x  += 1 # c.x = c.x+1----> c. x = 13+1=14
	def    disp(self):
		print(Test . x , self . y , self . z ,  self . x , sep = '\t')
# End  of  the  class
Test . get1()
a = Test() # Three empty object
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


output:-
---------
Enter  any  number    :  8
Enter  any  number  :  6
Enter  any  number  :  5
Enter  any  number  :  4
Enter  any  number  :  9
Enter  any  number  :  2
Enter  any  number  :  3
11      7       6       10
11      5       10      11
11      3       4       12

#11)Write  a  program  to  add  two  Vector  objects

1) What  are  the  names  of  objects ?  ---> x , y   and  z

2) What  are  the  names  of   lists  held  by  each  object ?  --->  x .  a , y . a  , z . a

3) How  to  access  elements  of  1st  list ?  --->  x . a[i]
    How  to  access  elements  of  2nd  list ?  --->  y . a[i]

4) How  to  access  static  variable  'n' ?  --->  vector . n


class  vector:
	@staticmethod
	def get1():
		vector.n = int(input("Enter number of elements: ")) # How  to  read  number  of  elements  into  variable  'n'
	def get2(self):
		self.d = eval(input('Enter a list: ' ))
	def add (self , x , y ):
		self . d = [ ]
		for i in range(vector.n):
			self.d.append(x .d[i] + y. d[i]) # How  to  read  the  list  into  the  object
vector. get1() #How  to  call  get1()  method
a = vector()
a. get2()  # How  to  read  the  list  into  1st  object
b = vector()
b. get2() # How  to  read  the  list  into  2nd  object 'b'
c = vector() 
c. add (a, b)  # How  to  add  the  lists  held  by  objects  'a'  and  'b'  and  store  the  results  in  list  of  3rd  object  'c'
print("Resulting vector:", c.d) #How  to  print  the  list  of  3rd   object

output:-
-------------
Enter number of elements: 4
Enter a list: [10,20,30,40]
Enter a list: [50,60,70,80]
Resulting vector: [60, 80, 100, 120]

#12)Write  a  program  to  print  only  static  variables  but  not  environment  variables  of   classname . _dict_

Hint:  Use  startswith()  and  endswith()  methods

class  c1:
	x = 1
	y = 2
	z = 3
#  End  of  the  class


class c1:
    x = 1
    y = 2
    z = 3
# End of the class
a = {}
b = c1 .__dict__

# Extract only static variables
for key in b:
	if not key. startswith('__') and not key. endswith('__'):
		a[key] = b[key]
# Print in the required format
print("static variables of class c1 :", a)

output:-
--------
static variables of class c1 : {'x': 1, 'y': 2, 'z': 3}




#13) What  are  k , l ,  x , y , z , m , n , p , q , s ?  (Home  work)
class   c1:
	x = 10  #  What  is  variable  'x'  --->
	def    m1(self):
		self . y = 20   #  What  is  variable  'y'  --->
		z = 30   #  What  is  variable   'z'  --->
		c1 . m = 40   #  What  is  variable   'm'  --->
#end of the class
def    f1():
	a = c1()
	a . p = 50   #  What  is   variable  'p'  --->
	c1 . q = 60   #  What  is  variable   'q'  --->
	s = 70   #  What  is  variable   's'  --->
#end of the function
k = 80   #  What  is  variable 'k'  --->
c1 . l = 90   #  What  is  variable  'l'  --->
b = c1()
b . n = 100   #  What  is  variable  'n' --->

output:-
-----------
Variable	What is it?
k	Global variable
l	Class variable (c1.l)
x	Class variable (defined in class body)
y	Instance variable (self.y in method)
z	Local variable (inside method m1)
m	Class variable (c1.m)
n	Instance variable (attached to object b)
p	Instance variable (attached to object a)
q	Class variable (c1.q)
s	Local variable (inside function f1)
'''
