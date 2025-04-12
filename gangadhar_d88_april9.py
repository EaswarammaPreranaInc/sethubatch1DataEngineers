#  What  are  the  outputs  if  inputs  are  25 , Rama  Rao ,  male , 52 , 48 , 55   (Home  work)
from  april8 import  student
s = student()
print(s . __dict__)# {}
s . get()
print(s . __dict__)#{'rno':25,'sname':'Rama Rao','gender':'male','marks':[52,48,55]}
s . compute()
print(s . __dict__)#{'rno':25,'sname':'Rama Rao','gender':'male','marks':[52,48,55],'total_marks': 190, 'avg': 63.333333333333336, 'grade': 21.11111111111111}
'''
'''
# Find  outputs
class Rat:
	def __init__(self , nr1 = 22, dr1 = 7):
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
print('a  :  ' , a) # a : 22/7
print('b  :  ' , b) # b :  9/7
print('c  :  ' , c) # c : 5/8
print('d  :  ' , d) # d : 22/9
print('e  :  ' , e)# e  : 2/3
print('f  :  ' , f) # f : 11/15

c .__init__()
print('c  :  ' , c)# c : 22/7
a . __init__(3.8  , 4.6) #  Modifies  object  'a'   to  nr = 3.8 , dr = 4.6   replacing  22  and   7
print('a  :  ' , a)#a : 3.8/4.6
#g = Rat(nr1 = 9 , 5) # error : KA BEFORE PA
#h = Rat(nr = 9 , dr = 5)#error: there a "h " object
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
print('a  :  ' , a . __dict__) # a : {'dd': 15, 'mm': 8, 'yy': 1947}
print('b  :  ' , b . __dict__) # b  : {'dd': 26, 'mm': 1, 'yy': 1950}
print('c  :  ' , c . __dict__) # c:{'dd': 19, 'mm': 7, 'yy': 1985}
#d = Date()#error ,requires 3 arguments
#e = Date(dd = 30 , mm = 4 , yy = 2022)#error: There is no dd,mm,yy arguments
#f = Date(dd1 = 26 , mm1 = 8 , 2023)#error: KA BEFORE PA
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
#a = c1()# error : return stmt contain int 25
b = c2() 
print(b)# c2  class  constructor <next line> type and address
print(b . __init__())# c2  class  constructor <next line> None
c = c3()# c3  class  constructor <next line> None
print(c . __init__())# c3  class  constructor <next line> None

 # Find  outputs (Home  work)
class  c1:
	def  __init__(self):
		print('Constructor')
		b = c1()
# End  of  class
#a = c1() # Error : calling itself infinity times

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
a = c1() # create object and executed constructor 10,20
print(a . __dict__)# Constructor <nextline> {'x':10,'y':20}
b = c2()
print(b . __dict__) #{}
b . init()
print(b . __dict__) # method <nextline> {'x':30,'y':40}

# Find  outputs (Home  work)
class   c1:
    def  __init__(self):
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
print(x . __dict__) #{'a':10}
x . m1()
print(x .__dict__) #{'a':10,'b':20}
f1()
print(x . __dict__) #{'a':10,'b':20,'c': 30}
x . d = 40
print(x . __dict__)#{'a':10,'b':20,'c': 30,'d': 40}
y = c2()
y . m3()
print(x . __dict__)#{'x':10,'y':20,'c': 30,'d': 40,'e':50}
z = c1()
print(z . __dict__)#{'x':10}


 # What  happens  when  function  and  class  have  same  name ?
def   f1():
	print('Function')
	return  25
class   f1:
	def  __init__(self):
		print('Constructor')
#end of the  class
a = f1() 
print(a)# Constructor <nextline> <class '__main__'.f1>
# Find  outputs (Home  work)
class    c1:
	def   __init__(self):
		print('Constructor')
def  c1(): #recognised
	print('Function')
#end of the  class
a = c1()
print(a)# Function <nextline> NOne

# Find outputs  (Home  work)
class    c1:
        def  __init__(self):
            print('Constructor')
def    c1(x):
    print('Function : ' , x)
# End  of  class  c1
#a = c1()
b = c1(25)
print(b)# Function: 25 <nextline> None
#  Save  the  program  in  prog9a.py  file


#  Find  outputs (Home  work)
from  april9a  import  c1
class   c1:
	def  _init_(self):
		print('c1  class  of  prog9b')
a = c1() # c1  class  of  prog9a 

#  Find  outputs (Home  work)
class   c1:
	def  __init__(self):
		print('c1  class  of  prog9c')

from  april9a import  c1
a = c1() # c1  class  of  prog9a 


#  How  to  use  both  the  classes (i.e.  c1  of  prog9a  and  c1  of  current  program)  with  from  statement
#How  to  import  class  c1  from  prog9a   with  from  statement
import c1 as c1_april9a
class   c1:
	def  __init__(self):
		print('c1  class  of  prog9d')
#How  to  create  c1  class  object  of  current  module
a=c1()# c1  class  of  prog9d
#How  to  create  c1  class  object  of  prog9a
a=c1_april9a()#c1  class  of  prog9a
 
#How  to  use  both  the  classes (i.e.  c1  of  prog9a  and  c1  of  current  program)  with  import  statement
#How  to  import  prog9a
import april9a
class   c1:
	def  __init__(self):
		print('c1  class  of  prog9e')
#How  to  create  c1  class  object  of  current  module
a=c1() # c1  class  of  prog9e
#How  to  create  c1  class  object  of  prog9a
a=april9a.c1() # c1  class  of  prog9a

Repeat  prog10a  with  3  objects

Eg:  c = a + b
	 print  c
	 c = a - b
	 print  c
	 c = a * b
	 print  c
	 c = a / b
	 print  c

from april8 import rat
a=rat()
b=rat()
a.get()
b.get()
c=rat()
c.add(a,b)
print("Sum : ",c)
c.sub(a,b)
print("Subtraction : ",c)
c.mul(a,b)
print("Multiplication : ",c)
c.div(a,b)
if b.nr != 0:
    print("Division : ",c)
else:
	print("Division is not permitted")


#Repeat  prog10a  with  list  of  6  objects

from april8 import rat
x=rat()
a=[rat(),rat(),rat(),rat(),rat(),rat()]
a[0].get()
a[1].get()
a[2].add(a[0],a[1])
a[3].sub(a[0],a[1])
a[4].mul(a[0],a[1])
a[5].div(a[0],a[1])
print("Sum : ",a[2])
print("Subtraction : ",a[3])
print("Multiplication : ",a[4])
if a[1].nr != 0:
	print("Division : ",a[5])
else:
	print("Division is not permitted")


