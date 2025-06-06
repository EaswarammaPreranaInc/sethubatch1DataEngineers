#  What  are  the  outputs  if  inputs  are  25 , Rama  Rao ,  male , 52 , 48 , 55   (Home  work)
from  trianglefunction  import  Student
s = Student()
print(s . __dict__)
s . get()
print(s . __dict__)
s . compute()
print(s . __dict__)
'''o/p: {}
        Enter a rollno: 25
        Enter a Name: Rama Rao
        Enter a Gender : male
        Enter mark 1: 52
        Enter mark 2: 48
        Enter mark 3: 55
        {'rno': 25, 'sname': 'Rama Rao', 'gender': 'male', 'm': [52, 48, 55]}
        {'rno': 25, 'sname': 'Rama Rao', 'gender': 'male', 'm': [52, 48, 55], 'tot': 155, 'avg': 51.666666666666664, 'grade': 'Second class'}'''

'''
Repeat  prog10a  with  3  objects

Eg:  c = a + b
	 print  c
	 c = a - b
	 print  c
	 c = a * b
	 print  c
	 c = a / b
	 print  c

Hint:  Import  and  use  Rat  class  defined  in  prog10a  but  do  not  define  Rat  class   again
'''
from trianglefunction import Rat

# Create 3 objects
a = Rat()
b = Rat()
c = Rat()

print("Enter first rational number:")
a.get() 

print("Enter second rational number:")
b.get()

# Addition
c.add(a,b)
print("Sum =", c)

# Subtraction
c.sub(a,b)
print("Difference =", c)

# Multiplication
c.mul(a,b)
print("Product =", c)

# Division
if b.num != 0:
    c.div(a,b)
    print("Division =", c)
else:
    print("Division is not permitted")
'''o/p: Enter first rational number:
		Enter numerator: 2
		Enter denominator (non-zero): 3
		Enter second rational number:
		Enter numerator: 5
		Enter denominator (non-zero): 9
		Sum = 11 / 9
		Difference = 1 / 9
		Product = 10 / 27
		Division = 6 / 5'''    
	
'''
Repeat  prog10a  with  list  of  6  objects

Hint:  import  and  use  rat  class  defined  in  prog10a  but  do  not  rewrite  the  class  again

What  are  the  object  names  ?  --->  a[0] , a[1] , a[2] , .....a[5]
'''
from trianglefunction import Rat

# Create a list of 6 Rat objects
a = [Rat() for _ in range(6)]

# Get input for first rational number (a[0])
print("Enter first rational number:")
a[0].get()

# Get input for second rational number (a[1])
print("Enter second rational number:")
a[1].get()

# Perform addition and store in a[2]
a[2].add(a[0], a[1])
print("Addition:", a[2])

# Perform subtraction and store in a[3]
a[3].sub(a[0], a[1])
print("Subtraction:", a[3])

# Perform multiplication and store in a[4]
a[4].mul(a[0], a[1])
print("Multiplication:", a[4])

# Perform division and store in a[5]
if a[1].num != 0:
    a[5].div(a[0], a[1])
    print("Division:", a[5])
else:
    print("Division not permitted")
'''o/p: Enter first rational number:
		Enter numerator: 2
		Enter denominator (non-zero): 3
		Enter second rational number:
		Enter numerator: 5
		Enter denominator (non-zero): 9
		Addition: 11 / 9
		Subtraction: 1 / 9
		Multiplication: 10 / 27
		Division: 6 / 5'''    
# Find  outputs
class  Rat:
	def   __init__(self , nr1 = 22, dr1 = 7):
		self . nr = nr1
		self . dr = dr1
	def   __str__(self):
		return  F'{self . nr}  /  {self . dr}'
#end  of  the  class
a = Rat() #   Object  is  initialized  with  nr =  22 , dr = 7  by  constructor
b = Rat(9) # Object is initialized with nr = 9 , dr = 7 by constructor
c = Rat(5,  8) # Object is initialized with nr = 5 , dr = 8 by constructor
d = Rat(dr1 = 9) # nr1 = 22, dr1 = 9
e = Rat(dr1 = 3 , nr1 = 2) # nr1 = 2, dr1 = 3
x = eval(input('Enter numerator  :  '))  #  Assume  that  input  is   11
y = eval(input('Enter Denominator  :  '))    #  Assume  that  input  is    15
f = Rat(x , y)
print('a  :  ' , a)
print('b  :  ' , b)
print('c  :  ' , c)
print('d  :  ' , d)
print('e  :  ' , e)
print('f  :  ' , f)
c . __init__() # Resets c valu to default value 22 and 7
print('c  :  ' , c) # 22/7
a . __init__(3.8  , 4.6) #  Modifies  object  'a'   to  nr = 3.8 , dr = 4.6   replacing  22  and   7
print('a  :  ' , a) # 3.8/4.6
#g = Rat(nr1 = 9 , 5) # Syntax Error becoz positional arg after keyword argmnt
h = Rat(nr = 9 , dr = 5)

# Find  outputs (Home  work)
class  Date:
        def   __init__(self , dd1 , mm1  , yy1):
                self . dd = dd1
                self . mm = mm1
                self . yy = yy1
# End  of  the  class
a = Date(15 , 8 , 1947) # dd1 = 15  mm1 = 8  yy1 = 1947
b = Date(yy1 = 1950 , mm1 = 1 , dd1 = 26) # dd1 = 26  mm1 = 1  yy1 = 1950
c = Date(mm1 = 7 , dd1 = 19 , yy1 = 1985)  # dd1 = 19  mm1 = 7  yy1 = 1985
print('a  :  ' , a . __dict__) # {'dd' : 15, 'mm' : 8, 'yy' : 1947}
print('b  :  ' , b . __dict__) # {'dd' : 26, 'mm' : 1, 'yy' : 1950}
print('c  :  ' , c . __dict__) # {'dd' : 19, 'mm' : 7, 'yy' : 1985}
d = Date() # Error: Date.__init__() missing 3 required positional arguments: 'dd1', 'mm1', and 'yy1'
e = Date(dd = 30 , mm = 4 , yy = 2022) # Error becoz no dd,mm,yy argmnts
#f = Date(dd1 = 26 , mm1 = 8 , 2023) # Error becoz of positional argmt after keyword argmnt

# Find  outputs (Home  work)
class  c1:
	def  __init__(self):
		print('c1  class constructor')
		return  25
class  c2:
	def  __init__(self):
		print('c2  class  constructor')
		return  None
class  c3:
	def  __init__(self):
		print('c3  class  constructor')
# End  of  class
#a = c1() # Error: __init__() should return None, not 'int'
b = c2() # c2  class  constructor
print(b) # Type and Address of b
print(b . __init__()) # c2 class constructor <next line> None(Explicitly modifying the constructor) 
c = c3() # c3 class constructor
print(c . __init__()) # c3 class constructor <next line> None(Explicitly modifying the constructor) 

# Find  outputs (Home  work)
class  c1:
	def  __init__(self):
		print('Constructor')
		#b = c1() # Error: maximum recursion depth exceeded
# End  of  class
a = c1() 
#  Difference  between  init()    and  _init_()   methods (Home  work)
class c1:
    def  __init__(self):
        print('Constructor')
        self . x = 10
        self . y = 20
class c2:
    def  init(self):
        print('Method')
        self . x = 30
        self . y = 40
a = c1() # Constructor
print(a . __dict__) # {'x': 10, 'y': 20} 
b = c2() # {} <nl> Method
print(b . __dict__) 
b . init() # Method
print(b . __dict__) # {'x': 30, 'y': 40}
# Find  outputs (Home  work)
class   c1:
        def   __init__(self):
                self . a = 10
        def   m1(self):
                self . b = 20
#End  of  class  c1
class   c2:
        def  m3(self):
                x . e = 50
# End  of  class  c2
def   f1():
        x . c = 30
#  End  of  function  f1
x = c1()
print(x . __dict__) # {'a': 10}
x . m1()
print(x . __dict__) # {'a': 10, 'b': 20}
f1()
print(x . __dict__) # {'a': 10, 'b': 20, 'c': 30}
x . d = 40
print(x . __dict__) # {'a': 10, 'b': 20, 'c': 30, 'd': 40}
y = c2()
y . m3()
print(x . __dict__) # {'a': 10, 'b': 20, 'c': 30, 'd': 40, 'e': 50}
z = c1()
print(z . __dict__) # {'a': 10}
# Find  outputs  (Home  work)
class   c1:
	def   __init__(self):
		self . x = 10
		self . y = 20
		self . z = 30
#end  of  the  class
a = c1()
b = c1()
print(a . __dict__) # {'x': 10, 'y': 20, 'z': 30}
print(b . __dict__) # {'x': 10, 'y': 20, 'z': 30}
del  a . x
del  b . y
print(a . __dict__) # {'y': 20, 'z': 30}
print(b . __dict__) # {'x': 10, 'z': 30}
#print(a . x) # Error: 'c1' object has no attribute 'x'
#print(b . y) # Error: 'c1' object has no attribute 'y'
#  Find  outputs (Home  work)
class   c1:
	def  __init__(self):
		print('1st  constructor')
	def  __init__(self):
		print('2nd  constructor')
	def  __init__(self):
		print('3rd  constructor')
# End  of  the  class
a = c1() # 3rd constructor
#  Find  outputs  (Home  work)
class   c1:
	def  __init__(self):
		print('No  argument  constructor')
	def  __init__(self , x):
		print('single  argument  constructor : ' , x)
	def  __init__(self , x , y):
		print('Two  argument  constructor : ' , x , y)
# End  of  the  class
a = c1(10 , 20) # Two  argument  constructor : 10 20
#b = c1(30) # Error becoz of one arg
#c = c1() # Error becoz of no two args
#  Find  outputs
class   c1:
	def  __init__(self):
		print('No  argument  constructor')
	def  __init__(self , x):
		print('single  argument  constructor : ' , x)
	def  __init__(self , x = 100 , y = 200):
		print('Two  argument  constructor : ' , x , y)
# End  of  the  class
a = c1(10 , 20) # Two argument constructor : 10 20
b = c1(30) # Two argument constructor : 30 200
c = c1() # Two argument constructor : 100 200
# What  happens  when  function  and  class  have  same  name ?
def   f1():
	print('Function')
	return  25
class   f1:
	def  __init__(self):
		print('Constructor')
#end of the  class
a = f1() # Constructor
print(a) # Type and Address of a
# Find  outputs (Home  work)
class    c1:
	def   __init__(self):
		print('Constructor')
def  c1(): #recognised
	print('Function')
#end of the  class
a = c1() # Function
print(a) # None
# Find outputs  (Home  work)
class    c1:
        def  __init__(self):
                print('Constructor')
def    c1(x):
        print('Function : ' , x)
# End  of  class  c1
#a = c1()
b = c1(25) # Function 25
print(b) # None
#  Save  the  program  in  prog9a.py  file
class   c1:
	def  __init__(self):
		print('c1  class  of  prog9a')
#  Find  outputs (Home  work)
from  trianglefunction  import  c1 as c1a
class   c1:
	def  __init__(self):
		print('c1  class  of  prog9b')
a = c1a() # c1 class of prog9a

#  How  to  use  both  the  classes (i.e.  c1  of  prog9a  and  c1  of  current  program)  with  from  statement
from trianglefunction import c1 as c1a#How  to  import  class  c1  from  prog9a   with  from  statement
class   c1:
	def  __init__(self):
		print('c1  class  of  prog9d')
a = c1()#How  to  create  c1  class  object  of  current  module
a = c1a()#How  to  create  c1  class  object  of  prog9a
