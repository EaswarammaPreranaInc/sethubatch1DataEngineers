#  What  are  the  outputs  if  inputs  are  25 , Rama  Rao ,  male , 52 , 48 , 55   (Home  work)
from  work  import  Student
s = Student()
print(s .__dict__)
s . get()
print(s .__dict__)
s . compute()
print(s .__dict__)
"""
Output:
Enter the rollno: 25
Enter the name: Rama Rao
Enter Gender: male
Enter Marks of 1 Subject: 52
Enter Marks of 2 Subject: 48
Enter Marks of 3 Subject: 55
Roll  Number  :   25
Student  Name  :   Rama Rao
Gender  :   male
Total  Marks  :   155
Average  :   51.666666666666664
Grade  :   Second  class
25       Rama Rao        male    [52, 48, 55]    155     51.67   Second  class
{}
Enter the rollno: 25
Enter the name: Rama Rao
Enter Gender: male
Enter Marks of 1 Subject: 52
Enter Marks of 2 Subject: 48
Enter Marks of 3 Subject: 55
{'rollno': 25, 'name': 'Rama Rao', 'gender': 'male', 'm': [52, 48, 55]}
{'rollno': 25, 'name': 'Rama Rao', 'gender': 'male', 'm': [52, 48, 55], 'total': 155, 'average': 51.666666666666664, 'grade': 'Second  class'}
"""

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

from rational import Rat
a=Rat()
b=Rat()
a.get()
b.get()
c=Rat()


c.add(a,b)
print(c)

c.sub(a,b)
print(c)

c.mul(a,b)
print(c)

c.div(a,b)
print(c)
"""
Output:
Enter numerator: 2
Enter denominator: 4
Enter numerator: 5
Enter denominator: 8
9/8
-1/8
5/16
4/5
"""

'''
Repeat  prog10a  with  list  of  6  objects

Hint:  import  and  use  rat  class  defined  in  prog10a  but  do  not  rewrite  the  class  again

What  are  the  object  names  ?  --->  a[0] , a[1] , a[2] , .....a[5]
'''

from rational import Rat
a=[]
for i in range(6):
	a.append(Rat())

a[0].get()
a[1].get()

a[2].add(a[0],a[1])
print(F"Addition : {a[2]}")
a[3].sub(a[0],a[1])
print(F"Subtraction : {a[3]}")
a[4].mul(a[0],a[1])
print(F"Multiplication : {a[4]}")
a[5].div(a[0],a[1])
print(F"Division : {a[5]}")



# Find  outputs
class  Rat:
	def  __init__(self , nr1 = 22, dr1 = 7):
		self . nr = nr1
		self . dr = dr1
	def  __str__(self):
		return  F'{self . nr}  /  {self . dr}'
#end  of  the  class
a = Rat() #   Object  is  initialized  with  nr =  22 , dr = 7  by  constructor
b = Rat(9)
c = Rat(5,  8)
d = Rat(dr1 = 9)
e = Rat(dr1 = 3 , nr1 = 2)
x = eval(input('Enter numerator  :  '))  #  Assume  that  input  is   11
y = eval(input('Enter Denominator  :  '))    #  Assume  that  input  is    15
f = Rat(x , y)
print('a  :  ' , a)
print('b  :  ' , b)
print('c  :  ' , c)
print('d  :  ' , d)
print('e  :  ' , e)
print('f  :  ' , f)
c .__init__()
print('c  :  ' , c)
a .__init__(3.8  , 4.6) #  Modifies  object  'a'   to  nr = 3.8 , dr = 4.6   replacing  22  and   7
print('a  :  ' , a)
#g = Rat(nr1 = 9 , 5)
#h = Rat(nr = 9 , dr = 5)

"""
Output:
Enter numerator  :  11
Enter Denominator  :  15
a  :   22  /  7
b  :   9  /  7
c  :   5  /  8
d  :   22  /  9
e  :   2  /  3
f  :   11  /  15
c  :   22  /  7
a  :   3.8  /  4.6
"""

# Find  outputs (Home  work)
class  Date:
        def  __init__(self , dd1 , mm1  , yy1):
                self . dd = dd1
                self . mm = mm1
                self . yy = yy1
# End  of  the  class
a = Date(15 , 8 , 1947)
b = Date(yy1 = 1950 , mm1 = 1 , dd1 = 26)
c = Date(mm1 = 7 , dd1 = 19 , yy1 = 1985)
print('a  :  ' , a .__dict__)
print('b  :  ' , b .__dict__)
print('c  :  ' , c .__dict__)
#d = Date()
e = Date(dd1= 30 , mm1= 4 , yy1= 2022)
#f = Date(dd1 = 26 , mm1 = 8 , 2023)

"""
Output:
a  :   {'dd': 15, 'mm': 8, 'yy': 1947}
b  :   {'dd': 26, 'mm': 1, 'yy': 1950}
c  :   {'dd': 19, 'mm': 7, 'yy': 1985}
"""

# Find  outputs (Home  work)
class  c1:
	def __init__(self):
		print('c1  class constructor')
		#return  25
class  c2:
	def __init__(self):
		print('c2  class  constructor')
		return  None
class  c3:
	def __init__(self):
		print('c3  class  constructor')
# End  of  class
a = c1()
b = c2()
print(b)
print(b .__init__())
c = c3()
print(c .__init__())
"""
Output:
c1  class constructor
c2  class  constructor
<__main__.c2 object at 0x000001D6370B6BA0>
c2  class  constructor
None
c3  class  constructor
c3  class  constructor
None
"""

# Find  outputs (Home  work)
class  c1:
	def __init__(self):
		print('Constructor')
		b = c1()
# End  of  class
a = c1()
"""
Output:
constructor
....untill stack is full 
"""

#  Difference  between  init()    and  _init_()   methods (Home  work)
class c1:
    def __init__(self):
        print('Constructor')
        self . x = 10
        self . y = 20
class c2:
    def  __init__(self):
        print('Method')
        self . x = 30
        self . y = 40
a = c1()
print(a .__dict__)
b = c2()
print(b .__dict__)
b .__init__()
print(b .__dict__)
"""
Output:
Constructor
{'x': 10, 'y': 20}
Method
{'x': 30, 'y': 40}
Method
{'x': 30, 'y': 40}
"""

# Find  outputs (Home  work)
class   c1:
        def   _init_(self):
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
print(x .__dict__)
x . m1()
print(x .__dict__)
f1()
print(x .__dict__)
x . d = 40
print(x .__dict__)
y = c2()
y . m3()
print(x .__dict__)
z = c1()
print(z .__dict__)
"""
Output:
{}
{'b': 20}
{'b': 20, 'c': 30}
{'b': 20, 'c': 30, 'd': 40}
{'b': 20, 'c': 30, 'd': 40, 'e': 50}
{}
"""

# Find  outputs  (Home  work)
class   c1:
	def  __init__(self):
		self . x = 10
		self . y = 20
		self . z = 30
#end  of  the  class
a = c1()
b = c1()
print(a . __dict__)
print(b . __dict__)
del  a . x
del  b . y
print(a .__dict__)
print(b . __dict__)
#print(a . x)
#print(b . y)
"""
Output:
{'x': 10, 'y': 20, 'z': 30}
{'x': 10, 'y': 20, 'z': 30}
{'y': 20, 'z': 30}
{'x': 10, 'z': 30}
"""

#  Find  outputs (Home  work)
class   c1:
	def  __init__(self):
		print('1st  constructor')
	def  __init__(self):
		print('2nd  constructor')
	def  __init__(self):
		print('3rd  constructor')
# End  of  the  class
a = c1()
"""
Output:
3rd Constructor
"""

#  Find  outputs  (Home  work)
class   c1:
	def  __init__(self):
		print('No  argument  constructor')
	def  __init__(self , x):
		print('single  argument  constructor : ' , x)
	def  __init__(self , x , y):
		print('Two  argument  constructor : ' , x , y)
# End  of  the  class
a = c1(10 , 20)
#b = c1(30)
#c = c1()
"""
Output:
Two  argument  constructor :  10 20
"""

#  Find  outputs
class   c1:
	def  __init__(self):
		print('No  argument  constructor')
	def  __init__(self , x):
		print('single  argument  constructor : ' , x)
	def  __init__(self , x = 100 , y = 200):
		print('Two  argument  constructor : ' , x , y)
# End  of  the  class
a = c1(10 , 20)
b = c1(30)
c = c1()
"""
Output:
Two  argument  constructor : 10,20
Two  argument  constructor : 30,200
Two  argument  constructor : 100,200
"""

# What  happens  when  function  and  class  have  same  name ?
def   f1():
	print('Function')
	return  25
class   f1:
	def  _init_(self):
		print('Constructor')
#end of the  class
a = f1()
print(a)
"""
Output:
<__main__.f1 object at 0x0000023224D56A50>
"""

# Find  outputs (Home  work)
class    c1:
	def   __init__(self):
		print('Constructor')
def  c1():               #recognised
	print('Function')
#end of the  class
a = c1()
print(a)
"""
Output:
Function
None
"""

# Find outputs  (Home  work)
class    c1:
        def  __init__(self):
                print('Constructor')
def    c1(x):
        print('Function : ' , x)
# End  of  class  c1
#a = c1()
b = c1(25)
print(b)
"""
Output:
Function:25
None
"""

#  Find  outputs (Home  work)
from  prog9a  import  c1
class   c1:
	def  __init__(self):
		print('c1  class  of  prog9b')
a = c1()
"""
Output:
C1 class of prog9b
"""

#  Find  outputs (Home  work)
class   c1:
	def  __init__(self):
		print('c1  class  of  prog9c')
from  prog9a  import  c1
a = c1()
"""
Output:
c1  class  of  prog9a
"""

#  How  to  use  both  the  classes (i.e.  c1  of  prog9a  and  c1  of  current  program)  with  from  statement
from prog9a import c1 as c1_prog9a      #How  to  import  class  c1  from  prog9a   with  from  statement
class   c1:
	def __init__(self):
		print('c1  class  of  prog9d')
#a=c1() 
c1.__init__(c1)               #How  to  create  c1  class  object  of  current  module
b=c1_prog9a()                 #How  to  create  c1  class  object  of  prog9a
"""
Output:
c1  class  of  prog9d
c1  class  of  prog9a
"""

'''
How  to  use  both  the  classes (i.e.  c1  of  prog9a  and  c1  of  current  program)  with  import  statement
'''
import  prog9a
class   c1:
	def  __init__(self):
		print('c1  class  of  prog9e')
a=c1()              #How  to  create  c1  class  object  of  current  module
prog9a.c1()                    #How  to  create  c1  class  object  of  prog9a
"""
Output:
c1  class  of  prog9e
c1  class  of  prog9a
"""
