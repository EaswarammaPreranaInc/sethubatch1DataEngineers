'''
# 1
#  What  are  the  outputs  if  inputs  are  25 , Rama  Rao ,  male , 52 , 48 , 55   (Home  work)
from  prog9a  import  student
s = student()
print(s . _dict_)
s . get()
print(s . _dict_)
s . compute()
print(s . _dict_)

Output:
{}
Enter roll no: 25
Enter name: Rama Rao
Enter gender (m/f): male
Enter marks of subject 1: 52
Enter marks of subject 2: 48
Enter marks of subject 3: 55
{'rno': 25, 'sname': 'Rama Rao', 'gender': 'male', 'm': [52, 48, 55]}
{'rno': 25, 'sname': 'Rama Rao', 'gender': 'male', 'm': [52, 48, 55], 'tot': 155, 'avg': 51.666666666666664, 'grade': 'Second class'} 
'''

'''
#2
Repeat student program for 'n' students
1) Reuse student class defined in prog9a but do not rewrite

2) Use list of objects 

How to read number of students into variable 'n'
How to store 'n' student class objects in class in list 'a'
How to read each student data into the object held by the list 
How to store results in each object held by the list
How to print each object held by the list 
'''
'''
from prog9a import student
n = int(input('How many students: '))
a = []
for i in range(n):
    a.append(student())
i = 1
for s in a:
    print(f'student {i}')
    s.get()
    i += 1
for s in a:
    s.compute()
for s in a:
    print(s)
'''
'''
Output:
How many students: 3
student 1
Enter roll no: 111
Enter name: Rama Rao
Enter gender (m/f): male
Enter marks of subject 1: 50
Enter marks of subject 2: 60
Enter marks of subject 3: 70
student 2
Enter roll no: 222
Enter name: Ajay
Enter gender (m/f): male
Enter marks of subject 1: 40
Enter marks of subject 2: 50
Enter marks of subject 3: 60
student 3
Enter roll no: 333
Enter name: Sita
Enter gender (m/f): female
Enter marks of subject 1: 45
Enter marks of subject 2: 55
Enter marks of subject 3: 65
111     Rama Rao        male    180     60.00   Second class
222     Ajay    male    150     50.00   Third class
333     Sita    female  165     55.00   Second class
'''

# 3
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
'''
from prog10a import rat
a=rat()
b=rat()
c=rat()
a.get()
b.get()
c.add(a,b)
print(f'Addition:{c}')
c.sub(a,b)
print(f'Subtraction:{c}')
c.mul(a,b)
print(f'Multiplication:{c}')
if b.nr==0:
    print('Division is not permitted')
else:
    c.div(a,b)
    print(F'Division:{c}')


Ouput:
Enter the numerator: 2
Enter the denominator: 3
Enter the numerator: 5
Enter the denominator: 9
Addition:11/9
Subtraction:1/9
Multiplication:10/27
Division:6/5
'''

# 4
'''
Repeat  prog10a  with  list  of  6  objects

Hint:  import  and  use  rat  class  defined  in  prog10a  but  do  not  rewrite  the  class  again

What  are  the  object  names  ?  --->  a[0] , a[1] , a[2] , .....a[5]
'''
'''
from prog10a import rat
a=[rat(), rat(), rat(), rat(), rat(), rat()]
a[0].get()
a[1].get()
a[2].add(a[0],a[1])
a[3].sub(a[0],a[1])
a[4].mul(a[0],a[1])
print('Sum:', a[2])
print('Difference:', a[3])
print('Product:', a[4])
if a[1].nr==0:
    print('Division is not permitted')
else:
    a[5].div(a[0],a[1])
    print('Division:',a[5])
'''
'''
Ouput:
Enter the numerator: 2
Enter the denominator: 3
Enter the numerator: 5
Enter the denominator: 9
Sum: 11/9
Difference: 1/9
Product: 10/27
Division: 6/5
'''

'''
# 5
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
print('a  :  ' , a)
print('b  :  ' , b)
print('c  :  ' , c)
print('d  :  ' , d)
print('e  :  ' , e)
print('f  :  ' , f)
c . _init_()
print('c  :  ' , c)
a . _init_(3.8  , 4.6) #  Modifies  object  'a'   to  nr = 3.8 , dr = 4.6   replacing  22  and   7
print('a  :  ' , a)
# g = Rat(nr1 = 9 , 5) # positional argument follows keyword argument
h = Rat(nr = 9 , dr = 5)

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
'''

'''
# 6
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
print('a  :  ' , a . _dict_)
print('b  :  ' , b . _dict_)
print('c  :  ' , c . _dict_)
# d = Date() # Error: Date._init_() missing 3 required positional arguments: 'dd1', 'mm1', and 'yy1'
# e = Date(dd = 30 , mm = 4 , yy = 2022) # got an unexpected keyword argument 'dd'
# f = Date(dd1 = 26 , mm1 = 8 , 2023) #positional argument follows keyword argument
'''

'''
OUtput:
a  :   {'dd': 15, 'mm': 8, 'yy': 1947}
b  :   {'dd': 26, 'mm': 1, 'yy': 1950}
c  :   {'dd': 19, 'mm': 7, 'yy': 1985}
'''
'''
# 7
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
# a = c1() #_init_() should return None, not 'int'
b = c2()
print(b)
print(b . _init_())
c = c3()
print(c . _init_())

Output:
c2  class  constructor
<_main_.c2 object at 0x000002C74DAC6CF0>
c2  class  constructor
None
c3  class  constructor
c3  class  constructor
None
'''

'''
# 8
# Find  outputs (Home  work)
class  c1:
	def  _init_(self):
		print('Constructor')
		# b = c1() # recursion error
# End  of  class
a = c1()


Output:
Constructor
'''

'''
# 9
#  Difference  between  init()    and  _init_()   methods (Home  work)
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
a = c1()
print(a . _dict_)
b = c2()
print(b . _dict_)
b . init()
print(b . _dict_)

Output:
Constructor
{'x': 10, 'y': 20}
{}
Method
{'x': 30, 'y': 40}
'''

'''
# 10
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
print(x . _dict_)
x . m1()
print(x . _dict_)
f1()
print(x . _dict_)
x . d = 40
print(x . _dict_)
y = c2()
y . m3()
print(x . _dict_)
z = c1()
print(z . _dict_)

Output:
{'a': 10}
{'a': 10, 'b': 20}
{'a': 10, 'b': 20, 'c': 30}
{'a': 10, 'b': 20, 'c': 30, 'd': 40}
{'a': 10, 'b': 20, 'c': 30, 'd': 40, 'e': 50}
{'a': 10}
'''

'''
# 11
# Find  outputs  (Home  work)
class   c1:
	def   _init_(self):
		self . x = 10
		self . y = 20
		self . z = 30
#end  of  the  class
a = c1()
b = c1()
print(a . _dict_)
print(b . _dict_)
del  a . x
del  b . y
print(a . _dict_)
print(b . _dict_)
# print(a . x) # 'c1' object has no attribute 'x'
# print(b . y) # 'c1' object has no attribute 'y'

Output:
{'x': 10, 'y': 20, 'z': 30}
{'x': 10, 'y': 20, 'z': 30}
{'y': 20, 'z': 30}
{'x': 10, 'z': 30}
'''


'''
# 12
#  Find  outputs (Home  work)
class   c1:
	def  _init_(self):
		print('1st  constructor')
	def  _init_(self):
		print('2nd  constructor')
	def  _init_(self):
		print('3rd  constructor')
# End  of  the  class
a = c1()

Output:
3rd  constructor
'''


'''
# 13
#  Find  outputs  (Home  work)
class   c1:
	def  _init_(self):
		print('No  argument  constructor')
	def  _init_(self , x):
		print('single  argument  constructor : ' , x)
	def  _init_(self , x , y):
		print('Two  argument  constructor : ' , x , y)
# End  of  the  class
a = c1(10 , 20) # Two  argument  constructor :  10 20
# b = c1(30) # missing 1 required positional argument: 'y'
# c = c1() #missing 2 required positional arguments: 'x' and 'y'

Output:
Two  argument  constructor :  10 20
'''

'''
# 14
#  Find  outputs
class   c1:
	def  _init_(self):
		print('No  argument  constructor')
	def  _init_(self , x):
		print('single  argument  constructor : ' , x)
	def  _init_(self , x = 100 , y = 200):
		print('Two  argument  constructor : ' , x , y)
# End  of  the  class
a = c1(10 , 20)
b = c1(30)
c = c1()


Output:
Two  argument  constructor :  10 20
Two  argument  constructor :  30 200
Two  argument  constructor :  100 200
'''

'''
# 15
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

Output:
<_main_.f1 object at 0x0000017E05D36A50>
'''

'''
# 16
# Find  outputs (Home  work)
class    c1:
	def   _init_(self):
		print('Constructor')
def  c1(): #recognised
	print('Function')
#end of the  class
a = c1()
print(a)

Ouptut:
Function
None
'''

'''
# 17
# Find outputs  (Home  work)
class    c1:
        def  _init_(self):
                print('Constructor')
def    c1(x):
        print('Function : ' , x)
# End  of  class  c1
#a = c1()
b = c1(25)
print(b)

Output:
Function :  25
None
'''

'''
# 18
#  Save  the  program  in  prog9a.py  file
class   c1:
	def  _init_(self):
		print('c1  class  of  prog9a')
'''

'''
# 19
#  Find  outputs (Home  work)
from  prog9a  import  c1
class   c1:
	def  _init_(self):
		print('c1  class  of  prog9b')
a = c1()

Output:
c1  class  of  prog9b
'''

'''
# 20
#  Find  outputs (Home  work)
class   c1:
	def  _init_(self):
		print('c1  class  of  prog9c')
from  prog9a  import  c1
a = c1()

Output:
c1  class  of  prog9a
'''

'''
# 21
#  How  to  use  both  the  classes (i.e.  c1  of  prog9a  and  c1  of  current  program)  with  from  statement
How  to  import  class  c1  from  prog9a   with  from  statement
class   c1:
	def  _init_(self):
		print('c1  class  of  prog9d')
How  to  create  c1  class  object  of  current  module
How  to  create  c1  class  object  of  prog9a
'''
'''
import prog9a #How  to  import  class  c1  from  prog9a   with  from  statement
class   c1:
    def  _init_(self):
    	print('c1  class  of  prog9d')
a=c1() # How  to  create  c1  class  object  of  current  module
a=prog9a.c1()# How  to  create  c1  class  object  of  prog9a

Output:
c1  class  of  prog9d
c1  class  of  prog9a
'''

# 22
'''
How  to  use  both  the  classes (i.e.  c1  of  prog9a  and  c1  of  current  program)  with  import  statement
'''
'''
How  to  import  prog9a
class   c1:
	def  _init_(self):
		print('c1  class  of  prog9e')
How  to  create  c1  class  object  of  current  module
How  to  create  c1  class  object  of  prog9a
'''
'''
from prog9a import c1 as c1_1# How  to  import  prog9a
class   c1:
	def  _init_(self):
		print('c1  class  of  prog9e')
a=c1()# How  to  create  c1  class  object  of  current  module
b=c1_1()# How  to  create  c1  class  object  of  prog9a

Output:
1  class  of  prog9e
c1  class  of  prog9e
'''
