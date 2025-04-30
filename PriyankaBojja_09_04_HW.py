Q1 #What  are  the  outputs  if  inputs  are  25 , Rama  Rao ,  male , 52 , 48 , 55   (Home  work)
from  Rational_num  import  student
s = student()
print(s . __dict__) 
s . get()
print(s . __dict__) 
s . compute()
print(s . __dict__)

OP-
{}
Enter roll number: 2
Enter student name: priya
Enter gender(m or f): f
Enter list of marks: [44,50,69]
{'rno': 2, 'sname': 'priya', 'gender': 'f', 'm': [44, 50, 69]}
{'rno': 2, 'sname': 'priya', 'gender': 'f', 'm': [44, 50, 69], 'tot': 163, 'avg': 54.333333333333336, 'grade': 'Second class'}
#---------------------------------------------------------------------------------------------------------
Q2 #Repeat  prog10a  with  3  objects

Eg:  c = a + b
	 print  c
	 c = a - b
	 print  c
	 c = a * b
	 print  c
	 c = a / b
	 print  c

Hint:Import  and  use  Rat  class  defined  in  prog10a  but  do  not  define  Rat  class   again

from Rational_num import Rat
a=Rat()
b=Rat()
c=Rat()
a.get()
b.get()
c.add(a,b)
print(f'Addition: {c}')
c.sub(a,b)
print(f'Substraction: {c}')
c.mul(a,b)
print(f'Multiplication: {c}')
if b.nr==0:
	print('Division not permitted')
else:
	c.div(a,b)
	print(f'Division: {c}')

OP-
Enter numerator: 2
Enter denominator: 4
Enter numerator: 0
Enter denominator: 6
Addition: 1/2
Substraction: 1/2
Multiplication: 0/24
Division not permitted
#---------------------------------------------------------------------------------------------------------
Q3 #Repeat  prog10a  with  list  of  6  objects

Hint:  import  and  use  rat  class  defined  in  prog10a  but  do  not  rewrite  the  class  again
What  are  the  object  names  ?  --->  a[0] , a[1] , a[2] , .....a[5]

from Rational_num import Rat 
a=[]
for s in range(6):
	a.append(Rat())
a[0].get()
a[1].get()
a[2].add(a[0],a[1])
a[3].sub(a[0],a[1])
a[4].mul(a[0],a[1])
print(f'Addition: {a[2]}')
print(f'Substraction: {a[3]}')
print(f'Multiplication: {a[4]}')
if a[1].nr==0:
	print('Division not permitted')
else:
	a[5].div(a[0],a[1])
	print(f'Division: {a[5]}')

OP-
Enter numerator: 1
Enter denominator: 2
Enter numerator: 3
Enter denominator: 4
Addition: 5/4
Substraction: -1/4
Multiplication: 3/8
Division: 2/3
#------------------------------------------------------------------------------------------------------
Q4 #Find  outputs
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
print('a  :  ' , a) # a : 22/7
print('b  :  ' , b) # b : 9/7
print('c  :  ' , c) # c : 5/8
print('d  :  ' , d) # d : 22/9
print('e  :  ' , e) # e : 2/3
print('f  :  ' , f) # f : 11/15
c . __init__()      #Modifies  object  'a'   to  nr1 = 22 , dr1 = 7   replacing  5  and   8
print('c  :  ' , c) # c : 22/7
a . __init__(3.8  , 4.6) #Modifies  object  'a'   to  nr1 = 3.8 , dr1 = 4.6   replacing  22  and   7
print('a  :  ' , a) # a : 3.8/4.6 
#g = Rat(nr1 = 9 , 5)  #error- Keyword argument must be given after positional argument
#h = Rat(nr = 9 , dr = 5)  #error - arguments are nr1 and dr1 but not nr and dr
#----------------------------------------------------------------------------------------------------------
Q5 #Find  outputs (Home  work)
class  Date:
        def   __init__(self , dd1 , mm1  , yy1):
                self . dd = dd1
                self . mm = mm1
                self . yy = yy1
# End  of  the  class
a = Date(15 , 8 , 1947)
b = Date(yy1 = 1950 , mm1 = 1 , dd1 = 26)
c = Date(mm1 = 7 , dd1 = 19 , yy1 = 1985)
print('a  :  ' , a . __dict__) # a  :   {'dd': 15, 'mm': 8, 'yy': 1947}
print('b  :  ' , b . __dict__) # b  :   {'dd': 26, 'mm': 1, 'yy': 1950}
print('c  :  ' , c . __dict__) # c  :   {'dd': 19, 'mm': 7, 'yy': 1985}
#d = Date() #error - no arguments are passing
#e = Date(dd = 30 , mm = 4 , yy = 2022) #error - no arguments dd,mm,yy
#f = Date(dd1 = 26 , mm1 = 8 , 2023) #error - Keyword arguments must be given after positional arguments 
#-----------------------------------------------------------------------------
Q6 #Find  outputs (Home  work)
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
#a = c1()  #error- __init__ in c1 class must return None but returning int 25.
b = c2()   #c2 class constructor
print(b)   #<__main__.c2 object at 0x00000197AED36A50>
print(b . __init__()) #c2 class constructor <next line> None
c = c3()  #c3 class constructor
print(c . __init__()) #c3 class constructor <next line> None
#--------------------------------------------------------------------------------------------------------
Q7 #Find  outputs (Home  work)
class  c1:
	def  __init__(self):
		print('Constructor')
		b = c1()
# End  of  class
a = c1() # Prints Constructor infinite times due to object creation in __init__ 
#-------------------------------------------------------------------------------------------------
Q8 #Difference  between  init()    and  __init__()   methods (Home  work)
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
a = c1() #Constructor
print(a . __dict__) #{'x':10,'y':20}
b = c2() #object is empty because no __init__ in c2 class
print(b . __dict__) #{} 
b . init() #Method
print(b . __dict__) #{'x':30,'y':40}
#-----------------------------------------------------------------------------------
Q9 #Find  outputs
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
print(x . __dict__) #{'a':10}
x . m1()
print(x . __dict__) #{'a': 10, 'b': 20}
f1()
print(x . __dict__) #{'a': 10, 'b': 20, 'c': 30}
x . d = 40
print(x . __dict__) #{'a': 10, 'b': 20, 'c': 30, 'd': 40}
y = c2()
y . m3()
print(x . __dict__) #{'a': 10, 'b': 20, 'c': 30, 'd': 40, 'e': 50}
z = c1()
print(z . __dict__) #{'a': 10}
#-------------------------------------------------------------------------
Q10 #Find  outputs  (Home  work)
class   c1:
	def   __init__(self):
		self . x = 10
		self . y = 20
		self . z = 30
#end  of  the  class
a = c1()
b = c1()
print(a . __dict__) #{'x': 10, 'y': 20, 'z': 30}
print(b . __dict__) #{'x': 10, 'y': 20, 'z': 30}
del  a . x
del  b . y
print(a . __dict__) #{'y': 20, 'z': 30}
print(b . __dict__) #{'x': 10, 'z': 30}
print(a . x) #error - a.x is deleted
print(b . y) #error - b.y is deleted
#--------------------------------------------------------------------------
Q11 #Find  outputs (Home  work)
class   c1:
	def  __init__(self):
		print('1st  constructor')
	def  __init__(self):
		print('2nd  constructor')
	def  __init__(self):
		print('3rd  constructor')
# End  of  the  class
a = c1() #3rd constructor
#--------------------------------------------------------------------------
Q12 #Find  outputs  (Home  work)
class   c1:
	def  __init__(self):
		print('No  argument  constructor')
	def  __init__(self , x):
		print('single  argument  constructor : ' , x)
	def  __init__(self , x , y):
		print('Two  argument  constructor : ' , x , y)
# End  of  the  class
a = c1(10 , 20) #Two  argument  constructor :  10 20
b = c1(30)      #error - argument for y is not given
c = c1()        #error - arguments for x and y are not given
#-----------------------------------------------------------------------------
Q13 #Find  outputs
class   c1:
	def  __init__(self):
		print('No  argument  constructor')
	def  __init__(self , x):
		print('single  argument  constructor : ' , x)
	def  __init__(self , x = 100 , y = 200):
		print('Two  argument  constructor : ' , x , y)
# End  of  the  class
a = c1(10 , 20) #Two  argument  constructor :  10 20
b = c1(30)      #Two  argument  constructor :  30 200
c = c1()        #Two  argument  constructor :  100 200
#------------------------------------------------------------------------
Q14 #What  happens  when  function  and  class  have  same  name ?
def   f1():
	print('Function')
	return  25
class   f1:
	def  __init__(self):
		print('Constructor')
#end of the  class
a = f1() #Constructor 
print(a) #<__main__.f1 object at 0x000002088E996A50> 
#-----------------------------------------------------------------------
Q15 #Find  outputs (Home  work)
class    c1:
	def   __init__(self):
		print('Constructor')
def  c1(): #recognised
	print('Function')
#end of the  class
a = c1() #Function 
print(a) #None - function returns none 
#--------------------------------------------------------------
Q16 #Find outputs  (Home  work)
class    c1:
        def  __init__(self):
                print('Constructor')
def    c1(x):
        print('Function : ' , x)
# End  of  class  c1
#a = c1() #error- no argument is passing for x
b = c1(25) # Function :  25
print(b)   #None
#-------------------------------------------------------------
Q17 #Save  the  program  in  prog9a.py  file
class   c1:
	def  __init__(self):
		print('c1  class  of  prog9a')
#--------------------------------------------------------------------
Q18 #Find  outputs (Home  work)

from  prog9a  import  c1
class   c1:
	def  __init__(self):
		print('c1  class  of  prog9b')
a = c1() #c1  class  of  prog9b ------> prog9a c1 is discarded due to same class name
#--------------------------------------------------------------
Q19 #Find  outputs (Home  work)

class   c1:
	def  __init__(self):
		print('c1  class  of  prog9c')
from  prog9a  import  c1
a = c1() #c1  class  of  prog9a ----> c1 in current program is discarded due to same class name
#---------------------------------------------------------------------------------------------------------------
Q20 #How  to  use  both  the  classes (i.e.  c1  of  prog9a  and  c1  of  current  program)  with  from  statement

from prog9a import c1 as c2     #How  to  import  class  c1  from  prog9a   with  from  statement
class   c1:
	def  __init__(self):
		print('c1  class  of  prog9d')
a=c1()   #How  to  create  c1  class  object  of  current  module
b=c2()   #How  to  create  c1  class  object  of  prog9a

OP-
c1  class  of  prog9d
c1  class  of  prog9a
#--------------------------------------------------------------------------------------------------------------
Q21 #How  to  use  both  the  classes (i.e.  c1  of  prog9a  and  c1  of  current  program)  with  import  statement

import prog9a   #How  to  import  prog9a
class   c1:
	def  __init__(self):
		print('c1  class  of  prog9e')
a=c1()          #How  to  create  c1  class  object  of  current  module
b=prog9a.c1()   #How  to  create  c1  class  object  of  prog9a

OP-
c1  class  of  prog9e
c1  class  of  prog9a
#------------------------------------------------------------------------------------------------------------------------
Q22 #Repeat student program for n students

1) Reuse student program but do not rewrite
2) use list of objects

from Rational_num import student
n=int(input('Enter number of objects: '))
a=[]
for s in range(n):
	a.append(student())
i=1
for s in a:
	print(f'student{i}')
	s.get()
	i+=1
for s in a:
	s.compute()
for s in a:
	print(s)

OP-
Enter number of objects: 3
student1
Enter roll number: 1
Enter student name: Priya
Enter gender(m or f): f
Enter list of marks: [65,87,56]
student2
Enter roll number: 2
Enter student name: Riya
Enter gender(m or f): f
Enter list of marks: [87,65,97]
student3
Enter roll number: 3
Enter student name: Sariya
Enter gender(m or f): f
Enter list of marks: [98,65,34]
1       Priya   f       208     69.33333333333333       First class
2       Riya    f       249     83.0    Distinction
3       Sariya  f       197     65.66666666666667       Fail


