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

from Apr08Opps import Rat
a=Rat()
b=Rat()
c=Rat()
a.get()
b.get()
c.add(a,b)
print('Sum:',c)
c.sub(a,b)
print('sub:',c)
c.mul(a,b)
print('mul:',c)
c.div(a,b)
if b.numerator!=0:
		
		print('div:',c)
else:
	print('Division not possoble:')


Repeat  prog10a  with  list  of  6  objects

Hint:  import  and  use  rat  class  defined  in  prog10a  but  do  not  rewrite  the  class  again

What  are  the  object  names  ?  --->  a[0] , a[1] , a[2] , .....a[5]
'''
from  Apr08Opps import Rat
a=[]
for i in range(6):
		a.append(Rat())
a[0].get()
a[1].get()

a[2].add(a[0],a[1])
print('sum:',a[2])
a[3].sub(a[0],a[1])
print('sub:',a[3])
a[4].mul(a[0],a[1])
print('mul:',a[4])
a[5].div(a[0],a[1])
print('div:',a[5])
'''


# Find  outputs
class  Rat:
	def   __init__(self , nr1 = 22, dr1 = 7):
		self . nr = nr1
		self . dr = dr1
	def   __str__(self):
		return  F'{self . nr}  /  {self . dr}'
#end  of  the  class
a = Rat() #   Object  is  initialized  with  nr =  22 , dr = 7  by  constructor
b = Rat(9) #object is intialized with nr=9, dr=7
c = Rat(5,  8)#object is intialized with nr=5, dr=8
d = Rat(dr1 = 9)#object is intialized with nr=22, dr=9
e = Rat(dr1 = 3 , nr1 = 2)#object is intialized with nr=2, dr=3
x = eval(input('Enter numerator  :  '))  #  Assume  that  input  is   11
y = eval(input('Enter Denominator  :  '))    #  Assume  that  input  is    15
f = Rat(x , y)#object is intialized with nr=11, dr=15
print('a  :  ' , a)#22/7
print('b  :  ' , b)#9/7
print('c  :  ' , c)#5/8
print('d  :  ' , d)#22/9
print('e  :  ' , e)#2/3
print('f  :  ' , f)#11/15
c . __init__()
print('c  :  ' , c)#22/7
a . __init__(3.8  , 4.6) #  Modifies  object  'a'   to  nr = 3.8 , dr = 4.6   replacing  22  and   7
print('a  :  ' , a)#3.8/4.6
#g = Rat(nr1 = 9 , 5)#error positional argument follows keyword argument
h = Rat(nr1 = 9 , dr1 = 5) 

outputs--
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
print('a  :  ' , a . __dict__)#{15:8:1947}
print('b  :  ' , b . __dict__)#{ dd1 : 26, mm1 : 1,yy1 : 1950 , }
print('c  :  ' , c . __dict__)#{ dd1 : 19 ,mm1 : 7 , yy1 : 1985}
d = Date()#error 
#e = Date(dd = 30 , mm = 4 , yy = 2022)
#f = Date(dd1 = 26 , mm1 = 8 , 2023)#error

# Find  outputs (Home  work)
class  c1:
	def  __init__(self):
		print('c1  class constructor')
		#return  25
class  c2:
	def  __init__(self):
		print('c2  class  constructor')
		return  None
class  c3:
	def  __init__(self):
		print('c3  class  constructor')
# End  of  class
a = c1()#'c1  class  constructor'
b = c2()#'c2  class  constructor'
print(b)#'c2  class  constructor' <next line> None
print(b . __init__())#'c2  class  constructor' <next line> None
c = c3()#'c3  class  constructor'
print(c . __init__())#'c3  class  constructor' <next line> None

# Find  outputs (Home  work)
class  c1:
	def  __init__(self):
		print('Constructor')
		#b = c1() #recursion
# End  of  class
a = c1()#'Constructor'

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
a = c1()#'Constructor'
print(a . __dict__)#{x:10,y:20}
b = c2()#'Method'
print(b . __dict__)
b . init()#error
print(b . __dict__)#{x:30,y:40}

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
x = c1()#
print(x . __dict__)#{a:10}
x . m1()
print(x . __dict__)#{a:10,b:20}
f1()
print(x . __dict__)#{a:10,b:20,c:30}
x . d = 40
print(x . __dict__)#{a:10,b:20,c:30,d:40}
y = c2()
y . m3()
print(x . __dict__)#{a:10,b:20,c:30,d:40,e:50}
z = c1()
print(z . __dict__)#{a:10}


# Find  outputs  (Home  work)
class   c1:
	def   __init__(self):
		self . x = 10
		self . y = 20
		self . z = 30
#end  of  the  class
a = c1()
b = c1()
print(a . __dict__)#{x:10,y:20,z:30}
print(b . __dict__)#{x:10,y:20,z:30}
del  a . x
del  b . y
print(a . __dict__)#{y:20,z:30}
print(b . __dict__)#{x:10,z:30}
#print(a . x)#error
#print(b . y)#error

#  Find  outputs (Home  work)
class   c1:
	def  __init__(self):
		print('1st  constructor')
	def  __init__(self):
		print('2nd  constructor')
	def  __init__(self):
		print('3rd  constructor')
# End  of  the  class
a = c1()#'3rd  constructor'

#  Find  outputs  (Home  work)
class   c1:
	def  __init__(self):
		print('No  argument  constructor')
	def  __init__(self , x):
		print('single  argument  constructor : ' , x)
	def  __init__(self , x , y):
		print('Two  argument  constructor : ' , x , y)
# End  of  the  class
a = c1(10 , 20)#'Two  argument  constructor : ' , 10,20
#b = c1(30)#error
#c = c1()#error

#  Find  outputs
class   c1:
	def  __init__(self):
		print('No  argument  constructor')
	def  __init__(self , x):
		print('single  argument  constructor : ' , x)
	def  __init__(self , x = 100 , y = 200):
		print('Two  argument  constructor : ' , x , y)
# End  of  the  class
a = c1(10 , 20)#'Two  argument  constructor : ' , 10,20
b = c1(30)#'Two  argument  constructor : ' , 30 , 200
c = c1()#'Two  argument  constructor : ' , 100,200

# What  happens  when  function  and  class  have  same  name ?
def   f1():
	print('Function')
	return  25
class   f1:
	def  __init__(self):
		print('Constructor')
#end of the  class
a = f1()#'Constructor'
print(a)#type and adress

# Find  outputs (Home  work)
class    c1:
	def   __init__(self):
		print('Constructor')
def  c1(): #recognised
	print('Function')
#end of the  class
a = c1()#
print(a)#'Function' <Next line> None

# Find outputs  (Home  work)
class    c1:
        def  __init__(self):
                print('Constructor')
def    c1(x):
        print('Function : ' , x)
# End  of  class  c1
#a = c1()
b = c1(25)
print(b)#'Function : ' , 25 <next line>None

#  Find  outputs (Home  work)
from  prog9a  import  c1
class   c1:
	def  _init_(self):
		print('c1  class  of  prog9b')
a = c1()

#  How  to  use  both  the  classes (i.e.  c1  of  prog9a  and  c1  of  current  program)  with  from  statement
 #How  to  import  class  c1  from  prog9a   with  from  statement
class   c1:
	def  __init__(self):
		print('c1  class  of  prog9d')
a=c1() #How  to  create  c1  class  object  of  current  module
from prog9a import c1
b=c1() #How  to  create  c1  class  object  of  prog9a


How  to  use  both  the  classes (i.e.  c1  of  prog9a  and  c1  of  current  program)  with  import  statement


class   c1:
	def  __init__(self):
		print('c1  class  of  prog9e')
a=c1() #How  to  create  c1  class  object  of  current  module
from   prog9a import c1
b=c1() #How  to  create  c1  class  object  of  prog9a'''
