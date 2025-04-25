#Ex-1
# Find  outputs (Home  work)
class c1:
    x = 10
    def __init__(self):
	    self . y = 20
a = c1() # create non-empty object  and execute constructor initialize y = 20
b = c1() #  create non-empty object  and execute constructor initialize y = 20
a . x += 1 # create variable x initialize   and assign object a x=11
b . y += 1 #   modifies variable y  = 21
print(a . x) # 11
print(a . y) # 20
print(b . x) # 10
print(b . y) # 21
print(c1 . x) # 10
print(a . __dict__) # all variables of object a  in the form dict
print(b . __dict__) # all variables of object b in the form dict
print(c1 . __dict__) # all variable x and environment variable

# Find  outputs (Home  work)
class  c1:
	x = 10
	def  m1(self):
		self . x = 20
a = c1() # create empty object
a . m1() # call m1  and initialize variable of x
print(c1 . x) # print static variable x is 10
print(a . x) # print object variable x is 20

#Ex-3
# Find  outputs  (Home  work)
class   c1:
	x = 10
	def  __init__(self):
		self . y = 20
	@classmethod
	def   m1(cls):
		cls . x = 30 # static variable x is modified
		cls . y = 40 # initialize static variable  y
# End  of  the  class
a = c1() # creating non-empty object and execute ,initialize  variable y
b = c1() # creating non-empty object and execute ,initialize  variable y
c1 . m1() # call static method  m1
print(a . x) # print static variable x is  30
print(a . y) # print object variable y  20
print(b . x) # print static variable x is  30
print(b . y) # print object variable y  20
print(c1 . x , c1 . y) # print static variable   x is 30   and  y is 40
# print(cls . x , cls . y) # Error because cls is not define
# print(self . x , self . y) # Error because self not define

#Ex-4
#  Find  outputs
class   c1:
	@staticmethod
	def   m1(self): # Here self is 25
		print(self) # 25
#  End  of  the   class
c1 . m1(25) # call static method and pass PV is 25
a = c1() # create empty object
a . m1(35) # call static method and pass PV is 35

#Ex-5
#  Find  outputs
class   c1:
	def   m1(self):
		print(self) # type and address
#  End  of  the   class
#c1 . m1(25) # Error because  m1 method accepting  only object reference (self)
a = c1() # creating empty object
a . m1() # calling object method
# a . m1(35) # # Error because  m1 method accepting  only object reference (self)

#Ex-6
#  Find  outputs
class   c1:
	@staticmethod
	def   m1(self):
		print('static  method')
		print(self)
	def   m1(self): # recognized
		print('instance  method') # instance method  # instance method
		print(self) # 25                             # type and address
#  End  of  the   class
c1 . m1(25) # manually using class name to   call instance  method m1 and  pass PV is 25
a = c1() # create empty object
a . m1() # call object method

#Ex-7
# How  to  access  static  variable  in  different  ways  ?
class   c1:
	x = 25
	def   __init__(self):
		print(c1.x) # How  to  print  static  variable  'x'
		print(self.x) # How  to  print  static  variable  'x'  in  another  way
		# print(x) # x is not define in constructor
	def   m1(self):
		print(c1.x)# How  to  print  static  variable  'x'
		print(self.x)# How  to  print  static  variable  'x'  in  another  way
		# print(cls . x) # cls is not define
	@classmethod
	def   m2(cls):
		print(c1.x) # How  to  print  static  variable  'x'
		print(cls.x) # How  to  print  static  variable  'x'  in  another  way
		# print(self . x) # self not define
	@staticmethod
	def   m3():
		print(c1.x)# How  to  print  static  variable  'x'
		# print(cls . x) # cls not define
		# print(self . x) # self not define
# End  of  the  class
print(c1.x)#How  to  print  static  variable  'x'
a=c1()
print(a.x)# How  to  print  static  variable  'x'  in  another  way
# print(x) # x not define
#print(self . x) # self not define
#print(cls . x) # cls not define
a.m1()# How  to  call  method  m1()
c1.m2()# How  to  call  method  m2()
c1.m3()# How  to  call  method  m3()

#Ex-8
# How  to  add  static  variable  to  the  class  at  different  locations  of  the  program ?
class c1:
    a = 10# How  to  add  static  variable  'a'  with  value  10
    def __init__(self):
        c1.b=20 # How  to  add  static  variable  'b'  with  value  20
        self.c=30 # How  to  add  instance  variable  'c'  with  value  30
        # cls . k = 25 # Error because cls not define
    def m1(self):
        c1.d=40 # How  to  add  static  variable  'd'  with  value  40
        self.e=50 #How  to  add  instance  variable  'e'  with  value  50
    @classmethod
    def m2(cls):
	    cls.f=60 # How  to  add  static  variable  'f'  with  value  60
	    c1.g=70 # How  to  add  static  variable  'g'  with  value  70  in  another  way
	    # self . k = 25 # Error self not defined
    @staticmethod
    def m3():
	    c1.h=80 # How  to  add  static  variable  'h'  with  value  80
	    # self . k = 25 # Error self not defined
		# cls . k = 35 # cls is not define
#End  of  the  class
print('Begin')   # Begin
print(c1 . __dict__) # all in the form of static variables dict {'a':10 } and environment variable
print()
print()
x = c1() # creating object and execute constructor and initialize static variable b is 20 and  self.c is 30
print('Constructor')
print(c1 . __dict__)  # all static variables  in the form of dict {'a':10,'b':20 } and environment variable
print()
print()
print()
x.m1() #  How  to  call  m1()  method and initialize static variable d is 40 and self.e is 50
print('Instance  method  m1')
print(c1 .__dict__) # {'a':10,'b':20,'d':30 } and environment variable
print()
print()
c1.m2()   # or x.m2() # How  to  call  m2()  method and initialize static variable f is 50 and g is 60
print('class  method   m2')
print(c1 . __dict__) # {'a':10,'b':20,'d':30,'e':50,'g':60 } and environment variable
print()
print()
c1.m3() # How  to  call  m3()  method and initialize static  variable  'h'  with  value  80
print('static   method   m3')
print(c1 . __dict__) # {'a':10,'b':20,'d':30,'e':50,'g':60 ,'h':80} and environment variable
print()
print()
c1.i=90 # How  to  add  static  variable  'i'  with  value  90
c1.j=100# How  to  add  instance  variable  'j'  with  value  100
print('Outside  the  class')
print(c1 . __dict__) # {'a':10,'b':20,'d':30,'g':60 ,'h':80,'i':90,'j':100} and environment variable
print()
print()
print("Object  'x' ")
print(x . __dict__) # {'c':30,'e':50}

#Ex-9
# Find  outputs  (Home  work)
class  c1:
        a , b , c  = range(1 , 4)
# End  of  the  class
print(c1.a) # How  to  print  variable  'a'
print(c1.b)# How  to  print  variable  'b'
print(c1.c) # How  to  print  variable  'c'

#Ex-10
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
Test . get1() # instance variable x =  10
a = Test() # create object empty object
b = Test() # create object empty object
c = Test()  # # create object empty object
a . get2()  # a object variables  variables y = 20 and z = 30
b . get2() # b object variables  y = 40 and z = 50
c . get2() # c object variables  y = 60 and z = 70
a . compute() # 11  21  31  12
b . compute() # 12  41  51  13
c . compute() # 13  61  71  14
a . disp() # 13	21	31	12
b . disp() # 13	41	51	13
c . disp() # 13	61	71	14

#Ex-11
'''
Write  a  program  to  add  two  Vector  objects

1) What  are  the  names  of  objects ?  ---> x , y   and  z

2) What  are  the  names  of   lists  held  by  each  object ?  --->  x .  a , y . a  , z . a

3) How  to  access  elements  of  1st  list ?  --->  x . a[i]
    How  to  access  elements  of  2nd  list ?  --->  y . a[i]

4) How  to  access  static  variable  'n' ?  --->  vector . n
'''
class vector:
    
    @staticmethod
    def get1():
        vector . n = int(input('Enter number of elements: ')) # How  to  read  number  of  elements  into  variable  'n'
    def get2(self):
        self.a = []
        for i in range(vector.n):# How  to  read  the  list  into  the  object
            x=int(input('Enter  any  number to the list    :  '))
            self.a.append(x)
    def add(self , x , y):
        self.b=[]
        for i in range(vector.n):# How  add  the  lists  held  by  objects  'x'  and  'y'  and  store  the  results  in  list  held  by  owner  object
            self.b.append(x.a[i]+y.a[i])
vector.get1() # How  to  call  get1()  method
x = vector()
x.get2() # How  to  read  the  list  into  1st  object
y =vector()
y.get2() # How  to  read  the  list  into  2nd  object  'b'
z =vector()
z.add(x,y) # How  to  add  the  lists  held  by  objects  'a'  and  'b'  and  store  the  results  in  list  of  3rd  object  'c'
for x in z.b:# How  to  print  the  list  of  3rd   object
    print(x)

#Ex-12
'''
Write  a  program  to  print  only  static  variables  but  not  environment  variables  of   classname . _dict_

Hint:  Use  startswith()  and  endswith()  methods
'''
class  c1:
	x = 1
	y = 2
	z = 3
#  End  of  the  class
a=c1.__dict__
b ={}
for x in a.keys():
    if not (x.startswith('__') and  x.endswith('__')):
        b[x]=a[x]
print(b)

#Ex-13
# What  are  k , l ,  x , y , z , m , n , p , q , s ?  (Home  work)
class   c1:
	x = 10  #  What  is  variable  'x'  ---> static variable
	def    m1(self):
		self . y = 20   #  What  is  variable  'y'  ---> y is Instance variable
		z = 30   #  What  is  variable   'z'  ---> Z is L V
		c1 . m = 40   #  What  is  variable   'm'  ---> m is static variable
#end of the class
def    f1():
	a = c1()
	a . p = 50   #  What  is   variable  'p'  ---> Instance variable
	c1 . q = 60   #  What  is  variable   'q'  ---> static variable
	s = 70   #  What  is  variable   's'  ---> L V
#end of the function
k = 80   #  What  is  variable 'k'  ---> G V
c1 . l = 90   #  What  is  variable  'l'  ---> l is Instance variable
b = c1()
b . n = 100   #  What  is  variable  'n' ---> Instance variable
