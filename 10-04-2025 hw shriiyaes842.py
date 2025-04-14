
#  What  are  the  outputs  if  inputs  are  25 , Rama  Rao ,  male , 52 , 48 , 55   (Home  work)
from  Student_class  import  Student
s = Student()
print(s . __dict__) #{}
s . get()
print(s . __dict__) 
s . compute()
print(s . __dict__) 

'''
{}
Enter roll no of student: 1
Enter name of the student: sita
Enter gender of the student: female
Enter marks of 3 subjects in the form of list:  [30,40,50]
{'rno': 1, 'sname': 'sita', 'gender': 'female', 'm': [30, 40, 50]}
{'rno': 1, 'sname': 'sita', 'gender': 'female', 'm': [30, 40, 50], 'tot': 120, 'avg': 40.0, 'grade': 'Fail'} '''

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
from Rat import Rat
a=Rat()
b=Rat()
c=Rat()
a.get()
b.get()
c.add(a,b)
print(c)
c.sub(a,b)
print(c)
c.mul(a,b)
print(c)
if b.nr==0:
	print("Division is not permitted")
else:
	c.div(a,b)
	print(c) 
from Rat import Rat
a=[Rat(),Rat(),Rat(),Rat(),Rat(),Rat()]
a[0].get()
a[1].get()
a[2].add(a[0],a[1])
a[3].sub(a[0],a[1])
a[4].mul(a[0],a[1])
print(a[2])
print(a[3])
print(a[4])
if a[1].nr==0:
	print("Division is not permitted")
else:
	a[5].div(a[0],a[1])
	print(a[5])


# Find  outputs
class  Rat:
	def   __init__(self , nr1 = 22, dr1 = 7):
		self . nr = nr1
		self . dr = dr1
	def   __str__(self):
		return  F'{self . nr}  /  {self . dr}'
#end  of  the  class
a = Rat() #   Object  is  initialized  with  nr =  22 , dr = 7  by  constructor
b = Rat(9) #nr1 =9 and dr1 =7
c = Rat(5,  8) # nr1=5 dr1=8
d = Rat(dr1 = 9) # nr1=22 dr 1=9
e = Rat(dr1 = 3 , nr1 = 2) # nr1=2 dr1=3
x = eval(input('Enter numerator  :  '))  #  Assume  that  input  is   11
y = eval(input('Enter Denominator  :  '))    #  Assume  that  input  is    15
f = Rat(x , y) # nr1=11 dr1=15
print('a  :  ' , a) # 22/7
print('b  :  ' , b) #9/7
print('c  :  ' , c) #5/8
print('d  :  ' , d) #22/9
print('e  :  ' , e) #2/3
print('f  :  ' , f) #11/15
c . __init__()
print('c  :  ' , c) #22/7
a . __init__(3.8  , 4.6) #  Modifies  object  'a'   to  nr = 3.8 , dr = 4.6   replacing  22  and   7
print('a  :  ' , a) #3.8/4.6
#g = Rat(nr1 = 9 , 5) # error ka cant be before pa
#h = Rat(nr = 9 , dr = 5) # error no nr and dr 

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
#d = Date() # Date.__init__() missing 3 required positional arguments: 'dd1', 'mm1', and 'yy1'
#e = Date(dd = 30 , mm = 4 , yy = 2022)
#f = Date(dd1 = 26 , mm1 = 8 , 2023) # positional argument follows keyword argument
'''
a  :   {'dd': 15, 'mm': 8, 'yy': 1947}
b  :   {'dd': 26, 'mm': 1, 'yy': 1950}
c  :   {'dd': 19, 'mm': 7, 'yy': 1985} ''' 
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
#a = c1() __init__() should return None, not 'int'
b = c2() #c2 class constructor 
print(b) # type n address
print(b . __init__()) #  c2 class constructor none 
c = c3() # c3 class constructor 
print(c . __init__()) # c3 class constructor none 

# Find  outputs (Home  work)
class  c1:
	def  __init__(self):
		print('Constructor')
		b = c1() #RecursionError: maximum recursion depth exceeded Dont create an object inside constructor 
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
a = c1() # constructor 
print(a . __dict__) #{x:10,y:20}
b = c2() # 
print(b . __dict__) #{}
b . init() #Method
print(b . __dict__) #{x:30,y:40}



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
print(x . __dict__) #{a:10}
x . m1() 
print(x . __dict__) #{a:10,b:20}
f1()
print(x . __dict__) #{a:10,b:20,c:30}
x . d = 40
print(x . __dict__) #{a:10,b:20,c:30,d:40}
y = c2()
y . m3()
print(x . __dict__) #{a:10,b:20,c:30,d:40,e:50}
z = c1()
print(z . __dict__) #{a:10} 

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
#print(a . x)
#print(b . y)
'''
{'x': 10, 'y': 20, 'z': 30}
{'x': 10, 'y': 20, 'z': 30}
{'y': 20, 'z': 30}
{'x': 10, 'z': 30}'''
#  Find  outputs (Home  work)
class   c1:
	def  __init__(self):
		print('1st  constructor')
	def  __init__(self):
		print('2nd  constructor')
	def  __init__(self):
		print('3rd  constructor')
# End  of  the  class
a = c1() #3rd Constructor 

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
#b = c1(30) # error need 2 arguments 
#c = c1() # error 
#  Find  outputs
class   c1:
	def  __init__(self):
		print('No  argument  constructor')
	def  __init__(self , x):
		print('single  argument  constructor : ' , x)
	def  __init__(self , x = 100 , y = 200):
		print('Two  argument  constructor : ' , x , y)
# End  of  the  class
a = c1(10 , 20) # Two  argument  constructor : 10 20
b = c1(30) # Two  argument  constructor : 30 200
c = c1() # Two  argument  constructor : 100 200 
# What  happens  when  function  and  class  have  same  name ?
def   f1():
	print('Function')
	return  25
class   f1:
	def  __init__(self):
		print('Constructor')
#end of the  class
a = f1() # f1 refers to class object 
print(a) #Constructor
#<__main__.f1 object at 0x000002583ED16A50>

# Find  outputs (Home  work)
class    c1:
	def   __init__(self):
		print('Constructor')
def  c1(): #recognised
	print('Function')
#end of the  class
a = c1() # function 
print(a) # none   

# Find outputs  (Home  work)
class    c1:
        def  __init__(self):
                print('Constructor')
def    c1(x):
        print('Function : ' , x)
# End  of  class  c1
#a = c1()
b = c1(25) # fucntion : 25
print(b) # none 
'''
#  Save  the  program  in  prog9a.py  file
class   c1:
	def  __init__(self):
		print('c1  class  of  prog9a') '''


#  Find  outputs (Home  work)
from  prog9a  import  c1
class   c1:
	def  __init__(self):
		print('c1  class  of  prog9b')
a = c1() # c1 class  of prog9b

#  Find  outputs (Home  work)
class   c1:
	def  _init_(self):
		print('c1  class  of  prog9c')
from  prog9a  import  c1
a = c1() # c1  class  of  prog9a

#  How  to  use  both  the  classes (i.e.  c1  of  prog9a  and  c1  of  current  program)  with  from  statement
#How  to  import  class  c1  from  prog9a   with  from  statement
from prog9a import c1 as c2
class   c1:
	def  __init__(self):
		print('c1  class  of  prog9d')
a=c1()
#print(a)
b=c2()
#print(b)
#How  to  create  c1  class  object  of  current  module
#How  to  create  c1  class  object  of  prog9a 
'''
How  to  use  both  the  classes (i.e.  c1  of  prog9a  and  c1  of  current  program)  with  import  statement
'''
#How  to  import  prog9a
import prog9a
class   c1:
	def  __init__(self):
		print('c1  class  of  prog9e')
a=c1()
b=prog9a.c1()
#How  to  create  c1  class  object  of  current  module
#How  to  create  c1  class  object  of  prog9a

