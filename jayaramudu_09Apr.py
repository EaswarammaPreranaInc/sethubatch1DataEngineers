#Ex-1
#What  are  the  outputs  if  inputs  are  25 , Rama  Rao ,  male , 52 , 48 , 55   (Home  work)
import sys
sys.path.append("D:\\python\\April\\08-04-25-HW")  # ✅ Add the directory only
import pro9a # ✅ Import the file name (module), not class

s = pro9a.Student()  # ✅ Access the class inside pro9a
print(s.__dict__) #Empty dict
s.get() # take values
print(s.__dict__) # {'rno': 123, 'sname': 'Ramudu', 'gender': 'M', 'm': [45, 25.89]}
s.compute()
print(s.__dict__) # {'rno': 123, 'sname': 'Ramudu', 'gender': 'M', 'm': [45, 25.89], 'tot': 70.89, 'average': 35.445, 'grade': 'Fail'}

#Ex-2
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

Hint:  Import  and  use  Rat  class  defined  in  prog10a  but  do  not  define  Rat  class  again
'''

import sys
sys.path.append('D:\\python\\April\\08-04-25-HW')
from pro1 import Rat
a=Rat()
b=Rat()
c=Rat()
a.get()
b.get()
c.add(a,b)
print(F'Addition :  {c}')
c.sub(a,b)
print(F'Subtraction : {c}')
c.mul(a,b)
print(F'Multiplication : {c}')
if b.num==0:
    print('Division not Permitted')
else:
    c.div(a,b)
    print(F'Division : {c}')


#Ex-3
'''
Repeat  prog10a  with  list  of  6  objects

Hint:  import  and  use  rat  class  defined  in  prog10a  but  do  not  rewrite  the  class  again

What  are  the  object  names  ?  --->  a[0] , a[1] , a[2] ,.....a[5]
'''
import sys
sys.path.append("D:\\python\\April\\08-04-25-HW")  # Update with the directory path
import pro1  # Import the module where the Rat class is defined

a = [pro1.Rat() for _ in range(6)]  # List of 6 Rat objects

a[0].get()  # Get input for first rational number
a[1].get()  # Get input for second rational number

a[2].add(a[0], a[1])
a[3].sub(a[0], a[1])
a[4].mul(a[0], a[1])
a[5].div(a[0], a[1])

print("Sum:", a[2])
print("Difference:", a[3])
print("Product:", a[4])

if a[5].num ==0:
    print("Division is not permitted")
else:
    print("Division:", a[5])


#Ex-4
# Find  outputs
class  Rat:
	def   _init_(self , nr1 = 22, dr1 = 7):
		self . nr = nr1
		self . dr = dr1
	def   _str_(self):
		return  F'{self . nr}  /  {self . dr}'
#end  of  the  class
a = Rat() #   Object  is  initialized  with  nr =  22 , dr = 7  by  constructor
b = Rat(9)    # nr = 9, dr = 7
c = Rat(5,  8) # nr=5 , dr=8
d = Rat(dr1 = 9) # nr=22,dr=9
e = Rat(dr1 = 3 , nr1 = 2) # nr=3 dr=2
x = eval(input('Enter numerator  :  '))  #  Assume  that  input  is   11
y = eval(input('Enter Denominator  :  '))    #  Assume  that  input  is    15
f = Rat(x , y) # nr=11 ,dr=15
print('a  :  ' , a) # 22/7
print('b  :  ' , b) # 9/7
print('c  :  ' , c) # 5/8
print('d  :  ' , d) # 22/9
print('e  :  ' , e) #2/3
print('f  :  ' , f) #11/15
c . __init__() #Now c is
print('c  :  ' , c) # 22/7
a . _init_(3.8  , 4.6) #  Modifies  object  'a'   to  nr = 3.8 , dr = 4.6   replacing  22  and   7
print('a  :  ' , a)
#g = Rat(nr1 = 9 , 5) # Error because KA after PA not Perminated
h = Rat(nr= 9, dr=5)

#Ex-5
class Date:
    def __init__(self, dd1, mm1, yy1):  # ✅ Correct constructor
        self.dd = dd1
        self.mm = mm1
        self.yy = yy1
# End of the class

# Create 3 Date objects with valid parameters
a = Date(15, 8, 1947)  # Independence Day
b = Date(yy1=1950, mm1=1, dd1=26)  # Republic Day
c = Date(mm1=7, dd1=19, yy1=1985)  # Any custom date
print('a :', a.__dict__)  # {'dd': 15, 'mm': 8, 'yy': 1947}
print('b :', b.__dict__)  # {'dd': 26, 'mm': 1, 'yy': 1950}
print('c :', c.__dict__)  # {'dd': 19, 'mm': 7, 'yy': 1985}
# d = Date()  #   missing required arguments
e = Date(dd1=30, mm1=4, yy1=2022)  #  Valid call
print('e :', e.__dict__)  # {'dd': 30, 'mm': 4, 'yy': 2022}
f = Date(26, 8, 2023)
print('f :', f.__dict__)  # {'dd': 26, 'mm': 8, 'yy': 2023}


#Ex-6
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
#a = c1() # create object of class c1 __init__ automatically executed it will throw error can't return int
b = c2() # create object of class c2 and  __init__ automatically executed # c2  class  constructor c2
# print(b) # Error because
print(b . __init__()) # Explicitly called    c2 class  constructor  <nl> None
c = c3() # # create object of class c3 and  __init__ automatically executed # c2  class  constructor c3
print(c.__init__())   # Explicitly called  c3 class  constructor  <nl> None

#Ex-7
# Find  outputs (Home  work)
class  c1:
	def  __init__(self):
		print('Constructor')
		b = c1()
# End  of class
a=c1() # create object of class c1 __init__ automatically executed Error occur  RecursionError

#Ex-8
#  Difference  between  init()    and  _init_()   methods (Home  work)
class c1:
    def  __init__(self):
        print('Constructor') # Constructor
        self . x = 10
        self . y = 20
class c2:
    def  init(self):
        print('Method') # Method
        self . x = 30
        self . y = 40
a = c1() # create object of class c1 __init__ automatically executed
print(a . __dict__) # {'x': 10, 'y': 20}
b = c2() # create empty object of class c2
print(b . __dict__) # {}
b . init()
print(b.__dict__) # {'x': 30, 'y': 40}

#Ex-9
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
x = c1() # create object of class c1 __init__ automatically executed
print(x . __dict__) # {'a':10}
x . m1() # call m1 method of c1
print(x . __dict__) # {'a':10,'b':20}
f1() # call f1 function and add variable x object c=30
print(x . __dict__) # {'a':10,'b':20,'c':30}
x . d = 40 # add variable d to object x
print(x . __dict__) # {'a': 10, 'b': 20, 'c': 30, 'd': 40}
y = c2() # create empty object class c2
y . m3() # m3 method of c2 and add variable d to object x
print(x . __dict__) # {'a': 10, 'b': 20, 'c': 30, 'd': 40, 'e': 50}
z = c1() # create object of class c1 __init__ automatically executed and reset
print(z.__dict__) # {'a': 10}

#Ex-10
# Find  outputs  (Home  work)
class   c1:
	def   __init__(self):
		self . x = 10
		self . y = 20
		self . z = 30
#end  of  the  class
a = c1() # create object of class c1 __init__ automatically executed
b = c1() #  create new object of class c1 __init__ automatically executed
print(a . __dict__) # {'x': 10, 'y': 20, 'z': 30}
print(b . __dict__) # {'x': 10, 'y': 20, 'z': 30}
del  a . x # delete x object a
del  b . y # delete y object b
print(a . __dict__) # {'y': 20, 'z': 30}
print(b . __dict__) # {'x': 10, 'z': 30}
#print(a .x) # Error because variable x  not in object a
#print(b.y) # Error because variable y  not in object b

#Ex-11
#  Find  outputs (Home  work)
class   c1:
	def  __init__(self):
		print('1st  constructor')
	def  __init__(self):
		print('2nd  constructor')
	def  __init__(self):
		print('3rd  constructor')
# End  of  the class
a=c1() # # create object of class c1 3rd __init__ automatically executed # 3rd  constructor

#Ex-12
#  Find  outputs  (Home  work)
class   c1:
	def  __init__(self):
		print('No  argument  constructor')
	def  __init__(self , x):
		print('single  argument  constructor : ' , x)
	def  __init__(self , x , y): # 3r one recognized remaining ignored
		print('Two  argument  constructor : ' , x , y)
# End  of  the  class
a = c1(10 , 20) # Two  argument  constructor :  10 20
#b =c1(30) # missing one PA
#c=c1() # Error because missing PA

#Ex-13
#  Find  outputs
class   c1:
	def  __init__(self):
		print('No  argument  constructor')
	def  __init__(self , x):
		print('single  argument  constructor : ' , x)
	def  __init__(self , x = 100 , y = 200):# 3rd one recognized remaining ignored
		print('Two  argument  constructor : ' , x , y)
# End  of  the  class
a = c1(10 , 20) # Two  argument  constructor :  10 20
b =c1(30) # x=30 and y value is default Two  argument  constructor :  30 200
c=c1() # x is default value and y is default value # Two  argument  constructor :  100 200

#Ex-14
# What  happens  when  function  and  class  have  same  name ?
def   f1():
	print('Function')
	return  25
class   f1:
	def  __init__(self):
		print('Constructor')
#end of the  class
a=f1() # create object class c1 because of function f1 and class names same last is recognized
print(a) # type and address of object

#Ex-15
# Find  outputs (Home  work)
class    c1:
	def   __init__(self):
		print('Constructor')
def  c1(): #recognised
	print('Function')
#end of the  class
a=c1() #  call function c1 because of function f1 and class names same last is recognized
print(a) # None

#Ex-16
# Find outputs  (Home  work)
class    c1:
        def  __init__(self):
                print('Constructor')
def    c1(x):
        print('Function : ' , x) # Function : 25
# End  of  class  c1
#a = c1()
b =c1(25)  #  call function c1 because of function f1 and class names same last is recognized
print(b) # None

#Ex-17
#  Find  outputs (Home  work)
from  prog9a  import  c1 # import class c1
class   c1:
	def  __init__(self):
		print('c1  class  of  prog9b')
a=c1() # create object current module class c1 ,#  c1  class  of  prog9b

#Ex-18
#  Find  outputs (Home  work)
class   c1:
	def  _init_(self):
		print('c1  class  of  prog9c')
from  prog9a  import c1 #  import class c1 and recognized
a=c1() # create object of prog9a class c1 # c1  class  of prog9a

#Ex-19
#  How  to  use  both  the  classes (i.e.  c1  of  prog9a  and  c1  of  current  program)  with  from  statement
from prog9a import c1 as c1_1# How  to  import  class  c1  from  prog9a   with  from  statement
class   c1:
	def  __init__(self):
		print('c1  class  of  prog9d')
a= c1()# How  to  create  c1  class  object  of  current  module
b= c1_1() # How  to  create  c1  class  object  of prog9a

#Ex-20
'''
How  to  use  both  the  classes (i.e.  c1  of  prog9a  and  c1  of  current  program)  with  import  statement
'''
import prog9a # How  to  import  prog9a
class   c1:
	def  __init__(self):
		print('c1  class  of  prog9e')
a=c1() # How  to  create  c1  class  object  of  current  module
a=prog9a.c1()# How  to  create  c1  class  object of prog9a

