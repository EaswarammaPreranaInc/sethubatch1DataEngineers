'''#  What  are  the  outputs  if  inputs  are  25 , Rama  Rao ,  male , 52 , 48 , 55   (Home  work)
from  prog9a  import  Student
s = Student()
print(s . _dict_)
s . get()
print(s . _dict_)
s . compute()
print(s . _dict_)

#outputs
{}
enter rollno : 2
enter name : ram
enter gender : Male
enter the 1 subject marks: 34
enter the 2 subject marks: 56
enter the 3 subject marks: 45
{'ro': 2, 'sname': 'ram', 'm': [34, 56, 45], 'gender': 'Male'}
{'ro': 2, 'sname': 'ram', 'm': [34, 56, 45], 'gender': 'Male', 'tot': 135, 'ave': 45.0}
'''

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

from prog10a import Rat
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
if c.div(a,b):
	print(c)
else:
	print('division not permitted')

'''


'''
Repeat  prog10a  with  list  of  6  objects

Hint:  import  and  use  rat  class  defined  in  prog10a  but  do  not  rewrite  the  class  again

What  are  the  object  names  ?  --->  a[0] , a[1] , a[2] , .....a[5]


from prog10a import Rat
a=[Rat() for i in range(6)]
a[0].get()
a[1].get()
a[2].add(a[0],a[1])
a[3].sub(a[0],a[1])
a[4].mul(a[0],a[1])
print(a[2])
print(a[3])
print(a[4])
if a[5].div(a[0],a[1]):
	print(a[5])
else:
	print('division is not permitted')

'''


'''
# Find  outputs
class  Rat:
	def   _init_(self , nr1 = 22, dr1 = 7):
		self . nr = nr1
		self . dr = dr1
	def   _str_(self):
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
print('a  :  ' , a) # a  :   22  /  7
print('b  :  ' , b) # b  :   9  /  7
print('c  :  ' , c) # c  :   5  /  8
print('d  :  ' , d) # d  :   22  /  9
print('e  :  ' , e) # e  :   2  /  3
print('f  :  ' , f) # f  :   11  /  15
c . _init_()
print('c  :  ' , c) # c  :   22  /  7
a . _init_(3.8  , 4.6) #  Modifies  object  'a'   to  nr = 3.8 , dr = 4.6   replacing  22  and   7
print('a  :  ' , a) # a  :   3.8  /  4.6
#g = Rat(nr1 = 9 , 5) error
#h = Rat(nr = 9 , dr = 5)
'''

'''
# Find  outputs (Home  work)
class  Date:
        def   _init_(self , dd1 , mm1  , yy1):
                self . dd = dd1
                self . mm = mm1
                self . yy = yy1
# End  of  the  class
a = Date(15 , 8 , 1947)
b = Date(yy1 = 1950 , mm1 = 1 , dd1 = 26)
c = Date(mm1 = 7 , dd1 = 19 , yy1 = 1985)
print('a  :  ' , a . _dict_) # a  : {'dd1':15 , 'mm1':8 , 'yy1':1947}
print('b  :  ' , b . _dict_) # b  : {'dd1':26 , 'mm1':1 , 'yy1':1950}
print('c  :  ' , c . _dict_) # c  : {'dd1':19 , 'mm1':7 , 'yy1':1985}
#d = Date() # missing the positional arguments
#e = Date(dd = 30 , mm = 4 , yy = 2022)  # arguments of keys are not same
#f = Date(dd1 = 26 , mm1 = 8 , 2023) # positional arguments follows keyword arguments
'''


'''
# Find  outputs (Home  work)
class  c1:
	def  _init_(self):
		print('c1  class constructor')
		return  25
class  c2:
	def  _init_(self):
		print('c2  class  constructor')
		return  None
class  c3:
	def  _init_(self):
		print('c3  class  constructor')
# End  of  class
#a = c1() # error
b = c2() # c2  class  constructor
print(b) # print type and address of the object i.e <_main_.c2 object at 0x00000205A4D76A50>
print(b . _init_()) # c2  class  constructor <nextline> None
c = c3() # c3  class  constructor
print(c . _init_()) # c3  class  constructor
'''

'''
# Find  outputs (Home  work)
class  c1:
	def  _init_(self):
		print('Constructor')
		b = c1()
# End  of  class
a = c1() 
#output
Constructor
Constructor
Constructor
Constructor
Constructor
Constructor
Constructor
...........
maximum recursion depth exceeded
'''

'''
#  Difference  between  init()    and  init()   methods (Home  work)
class c1:
    def  _init_(self):
        print('Constructor')
        self . x = 10
        self . y = 20
class c2:
    def  init(self):
        print('Method')
        self . x = 30
        self . y = 40
a = c1() # Constructor
print(a . _dict_) # {'x':10 ,'y':20}
b = c2()
print(b . _dict_) # {}
b . init() # Method
print(b . _dict_) # {'x':30 ,'y':40}
'''

'''
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
print(x . _dict_) # {'a':10}
x . m1()
print(x . _dict_) # {'a':10 , 'b':20}
f1()
print(x . _dict_) # {'a': 10, 'b': 20, 'c': 30}
x . d = 40
print(x . _dict_) # {'a': 10, 'b': 20, 'c': 30, 'd':40}
y = c2()
y . m3()
print(x . _dict_) # {'a': 10, 'b': 20, 'c': 30, 'd':40, 'e':50}
z = c1()
print(z . _dict_) # {'a':10 , 'b':20}
'''

'''
# Find  outputs  (Home  work)
class   c1:
	def   _init_(self):
		self . x = 10
		self . y = 20
		self . z = 30
#end  of  the  class
a = c1()
b = c1()
print(a . _dict_) # {'x':10, 'y':20, 'z':30}  
print(b . _dict_) # {'x':10, 'y':20, 'z':30}  
del  a . x
del  b . y
print(a . _dict_) # {'y':20, 'z':30}  
print(b . _dict_) # {'y':10, 'z':30}
#print(a . x) # error
#print(b . y) # error
'''

'''
#  Find  outputs (Home  work)
class   c1:
	def  _init_(self):
		print('1st  constructor')
	def  _init_(self):
		print('2nd  constructor')
	def  _init_(self):
		print('3rd  constructor')
# End  of  the  class
a = c1() # 3rd  constructor
'''


'''
#  Find  outputs  (Home  work)
class   c1:
	def  _init_(self):
		print('No  argument  constructor')
	def  _init_(self , x):
		print('single  argument  constructor : ' , x)
	def  _init_(self , x , y):
		print('Two  argument  constructor : ' , x , y)
# End  of  the  class
a = c1(10 , 20) # Two  argument  constructor : 10 20
b = c1(30) # error
c = c1() # error
'''


'''
#  Find  outputs
class   c1:
	def  _init_(self):
		print('No  argument  constructor')
	def  _init_(self , x):
		print('single  argument  constructor : ' , x)
	def  _init_(self , x = 100 , y = 200):
		print('Two  argument  constructor : ' , x , y)
# End  of  the  class
a = c1(10 , 20) # Two  argument  constructor : 10 20
b = c1(30) # Two  argument  constructor : 30 200
c = c1() # Two  argument  constructor : 100 200
'''


'''
# What  happens  when  function  and  class  have  same  name ?
def   f1():
	print('Function')
	return  25
class   f1:
	def  _init_(self):
		print('Constructor')
#end of the  class
a = f1() # Constructor
print(a) #  <_main_.f1 object at 0x0000020C37766A50>
'''


'''
# Find  outputs (Home  work)
class    c1:
	def   init(self):
		print('Constructor')
def  c1(): #recognised
	print('Function')
#end of the  class
a = c1() 
print(a) # Function <nextline> None
'''

'''
# Find outputs  (Home  work)
class    c1:
        def  _init_(self):
                print('Constructor')
def    c1(x):
        print('Function : ' , x)
# End  of  class  c1
#a = c1()
b = c1(25) # Function : 25
print(b) # None
'''


'''
#  Save  the  program  in  prog9a.py  file
class   c1:
	def  _init_(self):
		print('c1  class  of  prog9a')
a=c1()
'''

'''
#  Find  outputs (Home  work)
from  prog9a  import  c1
class   c1:
	def  _init_(self):
		print('c1  class  of  prog9b')
a = c1()
#output
c1  class  of  prog9b
'''


'''
#  Find  outputs (Home  work)
class   c1:
	def  _init_(self):
		print('c1  class  of  prog9c')
from  prog9a  import  c1
a = c1()
#output
c1  class  of  prog9a
'''


'''
from prog9a import Student
n=int(input("number of students: "))
a=[Student() for i in range(n)]
for i in range(len(a)):
	print(f'student{i+1}')
	a[i].get()
for i in range(len(a)):
	a[i].compute()
#for i in range(len(a)):
	#a[i].disp()
print()
for i in range(len(a)):
	print(a[i])
'''	


'''
#  How  to  use  both  the  classes (i.e.  c1  of  prog9a  and  c1  of  current  program)  with  from  statement
from prog9a import c1 as c2  #How  to  import  class  c1  from  prog9a   with  from  statement
class   c1:
	def  _init_(self):
		print('c1  class  of  prog9d')
a=c1() #How  to  create  c1  class  object  of  current  module
b=c2() #How  to  create  c1  class  object  of  prog9a
#outputs
c1  class  of  prog9d
c1  class  of  prog9a
'''

'''
#How  to  use  both  the  classes (i.e.  c1  of  prog9a  and  c1  of  current  program)  with  import  statement

import prog9a  #How  to  import  prog9a
class   c1:
	def  _init_(self):
		print('c1  class  of  prog9e')
a=c1()  #How  to  create  c1  class  object  of  current  module
b=prog9a.c1() #How  to  create  c1  class  object  of  prog9a
'''
