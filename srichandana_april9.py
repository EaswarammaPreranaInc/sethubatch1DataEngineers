#  What  are  the  outputs  if  inputs  are  25 , Rama  Rao ,  male , 52 , 48 , 55   (Home  work)
from student  import  Student
s = Student()
print(s . __dict__)
s . get()
print(s . __dict__)
s . compute()
print(s . __dict__)
#  What  are  the  outputs  if  inputs  are  25 , Rama  Rao ,  male , 52 , 48 , 55   (Home  work)
from  student  import  Student
s = Student()
print(s . __dict__)
s . get()
print(s . __dict__)
s . compute()
print(s . __dict__)
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
from rat import Rat
a=Rat()
b=Rat()
c=Rat()
a.get()
a.test()
b.get()
b.test()
print(c.add(a,b))
print(c.sub(a,b))
print(c.mul(a,b))
print(c.div(a,b))
'''
Repeat  prog10a  with  list  of  6  objects

Hint:  import  and  use  rat  class  defined  in  prog10a  but  do  not  rewrite  the  class  again

What  are  the  object  names  ?  --->  a[0] , a[1] , a[2] , .....a[5]
'''
from rat import Rat
a=[Rat() for i in range(6)] 
a[0]=Rat()
a[1]=Rat()
a[2]=Rat()
a[3]=Rat()
a[4]=Rat()
a[5]=Rat()
a[0].get()
a[0].test()
a[1].get()
a[1].test()
print(a[2].add(a[0],a[1]))
print(a[3].sub(a[0],a[1]))
print(a[4].mul(a[0],a[1]))
print(a[5].div(a[0],a[1]))
# Find  outputs
class  Rat:
	def   __init__(self , nr1 = 22, dr1 = 7):
		self . nr = nr1
		self . dr = dr1
	def   __str__(self):
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
c . __init__()
print('c  :  ' , c)
a . __init__(3.8  , 4.6) #  Modifies  object  'a'   to  nr = 3.8 , dr = 4.6   replacing  22  and   7
print('a  :  ' , a)
g = Rat(nr1 = 9 )#error pa after ka
h = Rat(nr1 = 9 , dr1 = 5) #error arg names
print(h,g)
# Find  outputs (Home  work)
class  Date:
        def   __init__(self , dd1 , mm1  , yy1):
                self . dd = dd1
                self . mm = mm1
                self . yy = yy1
# End  of  the  class
a = Date(15 , 8 , 1947)
b = Date(yy1 = 1950 , mm1 = 1 , dd1 = 26)
c = Date(mm1 = 7 , dd1 = 19 , yy1 = 1985)
print('a  :  ' , a . __dict__)
print('b  :  ' , b . __dict__)
print('c  :  ' , c . __dict__)
#d = Date() args not passed
e = Date(dd1 = 30 , mm1 = 4 , yy1 = 2022) #error arg are supposed to be mm1 not mm
f = Date(dd1 = 26 , mm1 = 8 , yy1=2003 ) #pa after ka
print('e  :  ' , e . __dict__)
print('f  :  ' , f . __dict__)
# Find  outputs (Home  work)
class  c1:
	def  __init__(self):
		print('c1  class constructor')
		return  None
class  c2:
	def  __init__(self):
		print('c2  class  constructor')
		return  None
class  c3:
	def  __init__(self):
		print('c3  class  constructor')
# End  of  class
a = c1() #__init__() should return None, not 'int'
b = c2()
print(b) #<__main__.c2 object at 0x10630d580>
print(b . __init__())
c = c3()
print(c . __init__())
# Find  outputs (Home  work)
class  c1:
	def  __init__(self):
		print('Constructor')
		#b = c1() recursive class object creation without return 
# End  of  class
a = c1()
#  Difference  between  init()    and  __init__()   methods (Home  work)
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
a = c1()
print(a . __dict__)
b = c2()
print(b . __dict__)
b . init()
print(b . __dict__)
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
print(x . __dict__)
x . m1()
print(x . __dict__)
f1()
print(x . __dict__)
x . d = 40
print(x . __dict__)
y = c2()
y . m3()
print(x . __dict__)
z = c1()
print(z . __dict__)
# Find  outputs  (Home  work)
class   c1:
	def   __init__(self):
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
print(a . __dict__)
print(b . __dict__)
#print(a . x) deleted attribute can't be called
#print(b . y)deleted attribute can't be called
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
b = c1(30,2) #2 pa one given
c = c1(2,4)
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
# What  happens  when  function  and  class  have  same  name ?
def   f1():
	print('Function')
	return  25
class   f1:
	def  __init__(self):
		print('Constructor')
		
#end of the  class
a = f1() #Constructor
print(a) #<__main__.f1 object at 0x105b01ca0>
# Find  outputs (Home  work)
class    c1:
	def   __init__(self):
		print('Constructor')
def  c1(): #recognised
	print('Function')
#end of the  class
a = c1()
print(a)
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
#  Save  the  program  in  hw18.py  file
class   c1:
	def  __init__(self):
		print('c1  class  of  prog9a')
#
#  Find  outputs (Home  work)
from  hw18  import  c1
class   c1:
	def  __init__(self):
		print('c1  class  of  prog9b')
a = c1()
#  Find  outputs (Home  work)
class   c1:
	def  __init__(self):
		print('c1  class  of  prog9c')
from  hw18  import  c1
a = c1()
#  How  to  use  both  the  classes (i.e.  c1  of  prog9a  and  c1  of  current  program)  with  from  statement
from hw18 import c1 as d1#How  to  import  class  c1  from  prog9a   with  from  statement
class   c1:
	def  __init__(self):
		print('c1  class  of  prog9d')
s=c1() #How  to  create  c1  class  object  of  current  module
k=d1() #How  to  create  c1  class  object  of  prog9a
'''
How  to  use  both  the  classes (i.e.  c1  of  prog9a  and  c1  of  current  program)  with  import  statement
'''
import hw18 #How  to  import  prog9a
class   c1:
	def  __init__(self):
		print('c1  class  of  prog9e')
f=c1() #How  to  create  c1  class  object  of  current  module
k=hw18.c1() #How  to  create  c1  class  object  of  prog9a
'''
How  to  use  both  the  classes (i.e.  c1  of  prog9a  and  c1  of  current  program)  with  import  statement
'''
import hw18 
#How  to  import  prog9a
class   c1:
	def  __init__(self):
		print('c1  class  of  prog9e')
#How  to  create  c1  class  object  of  current  module
#How  to  create  c1  class  object  of  prog9a
 #How  to  import  prog9a
f=c1() #How  to  create  c1  class  object  of  current  module
k=hw18.c1()
