# Find  outputs (Home  work)
class c1:
    x = 10
    def __init__(self):
	    self . y = 20
a = c1()
b = c1()
a . x += 1
b . y += 1
print(a . x)
print(a . y)
print(b . x)
print(b . y)
print(c1 . x)
print(a . __dict__)
print(b . __dict__)
print(c1 . __dict__)
"""
Output:
11
20
10
21
10
{'y':20,'x':10}
{'y':20}
{'y':20,'x':10,EV's}
"""

# Find  outputs (Home  work)
class  c1:
	x = 10
	def  m1(self):
		self . x = 20
a = c1()
a . m1()
print(c1 . x)
print(a . x)
"""
Output:
10
20
"""

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
a = c1()
b = c1()
c1 . m1()
print(a . x)
print(a . y)
print(b . x)
print(b . y)
print(c1 . x , c1 . y)
#print(cls . x , cls . y)
#print(self . x , self . y)
"""
Output:
30
20
30
20
30,40
"""

#  Find  outputs
class   c1:
	@staticmethod
	def   m1(self):
		print(self)
#  End  of  the   class
c1 . m1(25)
a = c1()
a . m1(35)
"""
Output:
25
35
"""

#  Find  outputs
class   c1:
	def   m1(self):
		print(self)
#  End  of  the   class
c1 . m1(25)
a = c1()
a . m1()
#a . m1(35)
"""
Output:
25
<type and address of m1()>
"""

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
c1 . m1(25)
a = c1()
a . m1()
"""
Output:
instance  method
25
instance  method
<type and address of object>
"""

# How  to  access  static  variable  in  different  ways  ?
class   c1:
	x = 25
	def   __init__(self):
		print(self.x)     #How  to  print  static  variable  'x'
		print(c1.x)       #How  to  print  static  variable  'x'  in  another  way
		#print(x)
	def   m1(self):
		print(self.x)      #How  to  print  static  variable  'x'
		print(c1.x)        #How  to  print  static  variable  'x'  in  another  way
		#print(cls . x)
	@classmethod
	def   m2(cls):
		print(cls.x)       #How  to  print  static  variable  'x'
		print(c1.x)        #How  to  print  static  variable  'x'  in  another  way
		#print(self . x)
	@staticmethod
	def   m3():
		print(c1.x)         #How  to  print  static  variable  'x'
		print(cls . x)
		print(self . x)
# End  of  the  class
print(c1.x) 
c=c1()
print(c.x)#How  to  print  static  variable  'x'  in  another  way
#print(x)
#print(self . x)
#print(cls . x)
c.m1()        #How  to  call  method  m1()
c.m2()        #How  to  call  method  m2()
c.m3()        #How  to  call  method  m3()



#How  to  add  static  variable  to  the  class  at  different  locations  of  the  program ?
class   c1:
	x=10 #How  to  add  static  variable  'a'  with  value  10
	def    _init_(self):
		c1.b=20 #How  to  add  static  variable  'b'  with  value  20
		self.c=30 #How  to  add  instance  variable  'c'  with  value  30
		#cls . k = 25 #Error no cls 
	def   m1(self):
		c1.d=40 #How  to  add  static  variable  'd'  with  value  40
		self.e=50 #How  to  add  instance  variable  'e'  with  value  50
	@classmethod
	def   m2(cls):
		c1.f=60 #How  to  add  static  variable  'f'  with  value  60
		cls.g=70 #How  to  add  static  variable  'g'  with  value  70  in  another  way
		#self . k = 25 #Error no self 
	@staticmethod
	def   m3():
		c1.h=80 #How  to  add  static  variable  'h'  with  value  80
		#self . k = 25 #Error no self 
		#cls . k = 35 #Error no cls 
#End  of  the  class
print('Begin') #1. Begin #c1---> x=10 
print(c1 . _dict_) #2. {'x':10,Ev's }
print()
print()
x = c1() 
# c1---> x=10 ,c1.b=20
# x.c=30 

print('Constructor') #3. Constructor
print(c1 . _dict_) #4. {'x':10,'b':20,Ev's}
print()
print()

x.m1() #How  to  call  m1()  method
# c1---> x=10 ,c1.b=20,c1.d=40 
# x.c=30 ,x.e=50

print('Instance  method  m1') #5. Instance  method  m1
print(c1 ._dict_) # {'x':10,'b':20,'d':40,Ev's}
print()
print()

c1.m2() #How  to  call  m2()  method
# c1---> x=10 ,c1.b=20,c1.d=40 ,c1.f=60,c1.g=70 
# x.c=30 ,x.e=50

print('class  method   m2') #class  method   m2
print(c1 . _dict_) # {'x':10,'b':20,'d':40,'f':60,'g':70,Ev's}
print()
print()

c1.m3() #How  to  call  m3()  method
# c1---> x=10 ,c1.b=20,c1.d=40 ,c1.f=60,c1.g=70,c1.h=80 
# x.c=30 ,x.e=50
print('static   method   m3') #static   method   m3
print(c1 . _dict_) # {'x':10,'b':20,'d':40,'f':60,'g':70,,'h':80,Ev's}
print()
print()
c1.i=90 #How  to  add  static  variable  'i'  with  value  90
x.j=100 #How  to  add  instance  variable  'j'  with  value  100
print('Outside  the  class') #Outside  the  class 
print(c1 . _dict_) # {'x':10,'b':20,'d':40,'f':60,'g':70,,'h':80,'i':90,Ev's}
print()
print()
print("Object  'x' ") # Object x
print(x . _dict_) #{'c':30 ,'e':50,'j':100}


# Find  outputs  (Home  work)
class  c1:
        a , b , c  = range(1 , 4)
# End  of  the  class
d=c1()
print(d.a)
print(d.c)
"""
Output:
1
3
"""

# What  are  the  outputs  if  inputs  are  10 , 20 , 30 , 40 , 50 , 60 , 70 (Home  work)
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
"""
Output:
Enter  any  number    :  5
Enter  any  number  :  6
Enter  any  number  :  7
Enter  any  number  :  9
Enter  any  number  :  0
Enter  any  number  :  1
Enter  any  number  :  2
8       7       8       7
8       10      1       8
8       2       3       9
"""


# What  are  k , l ,  x , y , z , m , n , p , q , s ?  (Home  work)
class   c1:
	x = 10  #  What  is  variable  'x'  ---> static variable
	def    m1(self):
		self . y = 20   #  What  is  variable  'y'  --->instance variable
		z = 30   #  What  is  variable   'z'  --->local variable to m1()
		c1 . m = 40   #  What  is  variable   'm'  --->static variable
#end of the class
def    f1():
	a = c1()
	a . p = 50   #  What  is   variable  'p'  --->static variable
	c1 . q = 60   #  What  is  variable   'q'  --->static variable
	s = 70   #  What  is  variable   's'  --->local variable to f1()
#end of the function
k = 80   #  What  is  variable 'k'  --->global variable
c1 . l = 90   #  What  is  variable  'l'  ---> static variable
b = c1()
b . n = 100   #  What  is  variable  'n' ---> static variable



#Write  a  program  to  print  only  static  variables  but  not  environment  variables  of   classname . _dict_
#Hint:  Use  startswith()  and  endswith()  methods

class  c1:
	x = 1
	y = 2
	z = 3	
#  End  of  the  class
s={key:value for key,value in c1.__dict__.items() if not(key.startswith('__') and (key.endswith('__')))}
print(F"static  variables  of  class  c1={s}")
"""
Output:
static  variables  of  class  c1={'x': 1, 'y': 2, 'z': 3}
"""

'''
Write  a  program  to  add  two  Vector  objects

1) What  are  the  names  of  objects ?  ---> x , y   and  z

2) What  are  the  names  of   lists  held  by  each  object ?  --->  x .  a , y . a  , z . a

3) How  to  access  elements  of  1st  list ?  --->  x . a[i]
    How  to  access  elements  of  2nd  list ?  --->  y . a[i]

4) How  to  access  static  variable  'n' ?  --->  vector . n
'''
class  vector:
	@staticmethod
	def get1():
		vector.n=int(input("Enter n: ")) #How  to  read  number  of  elements  into  variable  'n'
	def get2(self):
		self.a=[]#How  to  read  the  list  into  the  object
		for i in range(vector.n):
		    self.a.append(eval(input("Enter element of list: ")))
	def add(self , x , y):
	    self.a=[]
	    for i in range(vector.n):
		    self.a.append(x.a[i]+y.a[i]) #How  add  the  lists  held  by  objects  'x'  and  'y'  and  store  the  results  in  list  held  by  owner  object
vector.get1() #How  to  call  get1()  method
x=vector() 
x.get2() #How  to  read  the  list  into  1st  object
y=vector() 
y.get2() #How  to  read  the  list  into  2nd  object  'b'
z=vector() 
z.add(x,y) #How  to  add  the  lists  held  by  objects  'a'  and  'b'  and  store  the  results  in  list  of  3rd  object  'c'
print(z.a) #How  to  print  the  list  of  3rd   objec
