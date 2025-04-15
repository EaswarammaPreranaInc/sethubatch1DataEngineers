'''
#1)  What  are  the  outputs  if  inputs  are  25 , Rama  Rao ,  male , 52 , 48 , 55   (Home  work)
from  manustud  import  Student
s = Student()
print(s . __dict__)
s . get()
print(s . __dict__)
s . compute()
print(s . __dict__)


#2)Repeat  manurate  with  3  objects

Eg:  c = a + b
	 print  c
	 c = a - b
	 print  c
	 c = a * b
	 print  c
	 c = a / b
	 print  c

Hint:  Import  and  use  Rat  class  defined  in  manurate  but  do  not  define  Rat  class   again


from manurate import rat  # Importing the Rat class from manurate module

# Create two rational number objects
a = rat()  
b = rat()
c = rat()

# Read values into a and b (assuming Rat class has a get() method)
print("Enter first rational number:")
a.get()

print("Enter second rational number:")
b.get()

# Perform operations
c . add(a , b)
print("Addition:", c)

c . sub(a , b)
print("Subtraction:", c)

c . mul( a , b)
print("Multiplication:", c)

c . div (a , b)
print("Division:", c)



#3)Repeat  manurate  with  list  of  6  objects

Hint:  import  and  use  rat  class  defined  in  manurate  but  do  not  rewrite  the  class  again

What  are  the  object  names  ?  --->  a[0] , a[1] , a[2] , .....a[5]


from manurate import rat  # Import the Rat class

# Create a list to hold 6 Rat objects
a = [rat() for x in range(6)]

# Read values into each Rat object
for i in range(6):
    print(f"Enter rational number {i + 1}:")
    a[i].get()

# Example operations between first two objects
print("\nPerforming operations between a[0] and a[1]:")
c = rat()
c .add (a[0] , a[1])
print("Addition:", c)

c .sub( a[0] , a[1])
print("Subtraction:", c)

c .mul( a[0] , a[1])
print("Multiplication:", c)

c .div( a[0] , a[1])
print("Division:", c)


------------------------------------------
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
a . _init_(3.8  , 4.6) # Error : Modifies  object  'a'   to  nr = 3.8 , dr = 4.6   replacing  22  and   7
print('a  :  ' , a)
#g = Rat(nr1 = 9 , 5) # Error : positional argument follows keyword argument 
#h = Rat(nr = 9 , dr = 5) # Error : nr and dr  arguments are not there in the module.

output:-
-------
Enter numerator  :  8
Enter Denominator  :  6
a  :   22  /  7
b  :   9  /  7
c  :   5  /  8
d  :   22  /  9
e  :   2  /  3
f  :   8  /  6
c  :   22  /  7
a  :   3.8  /  4.6

#2)Find  outputs (Home  work)
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
#d = Date() # Error : aruments missing
#e = Date(dd = 30 , mm = 4 , yy = 2022) #Error:  here dd , mm, yy arguments are not there in the module. 
#f = Date(dd1 = 26 , mm1 = 8 , 2023) # Error : positional argument follows keyword argument

outputs:-
------
a  :   {'dd': 15, 'mm': 8, 'yy': 1947}
b  :   {'dd': 26, 'mm': 1, 'yy': 1950}
c  :   {'dd': 19, 'mm': 7, 'yy': 1985}


#3) Find  outputs (Home  work)
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
#a = c1() # Error : due to constructor has no return statement.
b = c2() # creating object to the class c2()
print(b) # Direct call to the class c2() throw 'b' and there is no str() in the current module so str() of object class executes and it returns Type and Address of the object.
print(b . _init_()) # Explixit call to the class c2 throw 'b' and returns none to the constructor
c = c3() # creating object to the class c3()
print(c . _init_()) # Explixit call to the class c2 throw 'b' and returns none to the constructor

output:-
----------
c2  class  constructor
<_main_.c2 object at 0x000001EF84456A50>
c2  class  constructor
None
c3  class  constructor
c3  class  constructor
None


#4) Find  outputs (Home  work)
class  c1:
	def  _init_(self):
		print('Constructor')
		b = c1() # creating object to the class c1() -----> prints ---constructor for infinite times and after the stack full we get RecursionError: maximum recursion depth exceeded. 
# End  of  class
a = c1() # creating object to the class c1()-----> prints ---constructor



#5) Difference  between  init()    and  init()   methods (Home  work)
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
a = c1() # creating object to the class c1()-----> prints ---constructor
print(a . _dict_) # {'x': 10, 'y': 20}
b = c2() # creating object to the class c2()
print(b . _dict_) # {}-----> empty dictionary creates bcz there is no value 
b . init() # init () method we are calling here.-----> prints ---method
print(b . _dict_) # {'x': 30, 'y': 40}

output:-
-----------
Constructor
{'x': 10, 'y': 20}
{}
Method
{'x': 30, 'y': 40}


#6)Find  outputs (Home  work)
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
print(x . _dict_) # 'a': 10 added to 'x' throw the constructor
x . m1()
print(x . _dict_) # 'b': 20 added to 'x' throw the method m1()
f1()
print(x . _dict_) # 'c': 30 added to 'x' throw the function f1() which is outside the classes
x . d = 40
print(x . _dict_) # 'd': 40 added to 'x' from the outside 
y = c2() # creates object 'y' to the class c2()
y . m3() # calling m3() method from class c2()
print(x . _dict_) # 'e': 50 added to 'x' throw the different class c2() method m3()
z = c1() # creates object 'z' to the class c1()
print(z . _dict_) # 'a': 10 added to 'z' throw the constructor

outputs:-
---------
{'a': 10}
{'a': 10, 'b': 20}
{'a': 10, 'b': 20, 'c': 30}
{'a': 10, 'b': 20, 'c': 30, 'd': 40}
{'a': 10, 'b': 20, 'c': 30, 'd': 40, 'e': 50}
{'a': 10}

object 'x' -------> {'a': 10, 'b': 20, 'c': 30, 'd': 40, 'e': 50}
object 'y'-------->
object 'z' ------->{'a': 10}


#7)Find  outputs  (Home  work)
class   c1:
	def   _init_(self):
		self . x = 10
		self . y = 20
		self . z = 30
#end  of  the  class
a = c1() # creating onject 'a' to class c1()
b = c1() # creating onject 'b' to class c1()
print(a . _dict_) # {'x': 10, 'y': 20, 'z': 30}-----> x ,y and z values are printed in the Dictionary form
print(b . _dict_) # {'x': 10, 'y': 20, 'z': 30}----->x ,y and z values are printed in the Dictionary form
del  a . x # delete 'x' value form object 'a'
del  b . y # delete 'y' value form object 'a'
print(a . _dict_) # {'y': 20, 'z': 30}
print(b . _dict_) # {'x': 10, 'z': 30}
#print(a . x) # Error : 'x' was deleted
#print(b . y) # Error : 'y' was deleted

output:-
----------
{'x': 10, 'y': 20, 'z': 30}
{'x': 10, 'y': 20, 'z': 30}
{'y': 20, 'z': 30}
{'x': 10, 'z': 30}


#8) Find  outputs (Home  work)
class   c1:
	def  _init_(self):
		print('1st  constructor') # 1st  constructor ignored
	def  _init_(self):
		print('2nd  constructor') #2nd  constructor ignored
	def  _init_(self):
		print('3rd  constructor') # 3rd  constructor recognised ----> last one is recognised here.
# End  of  the  class
a = c1() # creating 'a' object to the class c1()

output:-
---------
3rd  constructor


#9)Find  outputs  (Home  work)
class   c1:
	def  _init_(self):
		print('No  argument  constructor') # No  argument  constructor ignored
	def  _init_(self , x):
		print('single  argument  constructor : ' , x) # single  argument  constructor ignored
	def  _init_(self , x , y):
		print('Two  argument  constructor : ' , x , y) # Two  argument  constructor recognised
# End  of  the  class
a = c1(10 , 20) # Two  argument  constructor :  10 20
#b = c1(30) #  Error: missing 1 required positional argument: 'y' bcz require two arguments
#c = c1() # Error  missing 2 required positional argument: 'x' and  'y' bcz require two arguments

output:-
---------
Two  argument  constructor :  10 20

#10)
class   c1:
	def  _init_(self):
		print('No  argument  constructor') # No  argument  constructor ignored
	def  _init_(self , x):
		print('single  argument  constructor : ' , x) # single  argument  constructor ignored
	def  _init_(self , x = 100 , y = 200):
		print('Two  argument  constructor : ' , x , y) # Two  argument  constructor recognised
# End  of  the  class
a = c1(10 , 20) # Two  argument  constructor recognised-- 10 20
b = c1(30) # Two  argument  constructor recognised ---- 30 200
c = c1() # Two  argument  constructor recognised----100 200

output:-
--------
Two  argument  constructor :  10 20
Two  argument  constructor :  30 200
Two  argument  constructor :  100 200


#11)What  happens  when  function  and  class  have  same  name ?
def   f1():
	print('Function') # function ignores 
	return  25
class   f1:
	def  _init_(self): # class f1 () is recognised.
		print('Constructor') # Constructor
#end of the  class
a = f1() #creating object 'a' to class f1() 
print(a) # <_main_.f1 object at 0x0000027AB3F26A50>


output:-
--------
Constructor
<_main_.f1 object at 0x00000258F7376A50>


#12) Find  outputs (Home  work)
class    c1: # ignored
	def   _init_(self):
		print('Constructor')
def  c1(): #recognised
	print('Function')
#end of the  class
a = c1() #creating object 'a' to class c1() 
print(a)

outputs:-
---------
Function
None

#13)Find outputs  (Home  work)
class    c1:
        def  __init__(self): # constructor ignores 
                print('Constructor')
def    c1(x):
        print('Function : ' , x) # function recognises here
# End  of  class  c1
#a = c1() # create an object 'a' to class c1() 
b = c1(25) # function call with 'x' value 25 and returns none to the class
print(b) # Function :  25
           None


outputs:-
---------
Function :  25
None

#14) Save  the  program  in  manustud.py  file
class   c1:
	def  _init_(self):
		print('c1  class  of  manustud')

#15 Find  outputs (Home  work)
from manustud  import  c1 # we are imported c1 class from manustud----->ignored
class   c1: # constructor is created ----> recognised it and executes constructor here.
	def  __init__(self):
		print('c1  class  of  manustud')
a = c1() # creating object for class c1 () of constructor here.

output:-
-----------
c1  class  of  manustud


#16)Find  outputs (Home  work)
class   c1: # constructor is created ----> ignored 
	def  __init__(self):
		print('c1  class  of  prog9c')
from  manustud  import  c1 # we are imported c1 class from manustud----->recognised and executes.
a = c1()

output:-
---------
c1  class  of  manustud


#17)How  to  use  both  the  classes (i.e.  c1  of  manustud  and  c1  of  current  program)  with  from  statement
How  to  import  class  c1  from  manustud   with  from  statement

class   c1:
	def  _init_(self):
		print('c1  class  of  prog9d')
How  to  create  c1  class  object  of  current  module
How  to  create  c1  class  object  of manustud


from manustud import c1 as ManustudC1  # ? alias to avoid name conflict

class c1:
    def __init__(self):
        print("c1 class of prog9d")

# Object of local c1 class (prog9d)
a = c1()

# Object of imported c1 class (manustud)
b = ManustudC1()

output:-
---------
c1 class of prog9d
c1  class  of  manustud


#18)How  to  use  both  the  classes (i.e.  c1  of  manustud  and  c1  of  current  program)  with  import  statement

How  to  import  manustud
class   c1:
	def  _init_(self):
		print('c1  class  of  prog9e')
How  to  create  c1  class  object  of  current  module
How  to  create  c1  class  object  of  manustud


import manustud  # Importing the whole module

class c1:
    def __init__(self):
        print('c1 class of prog9e')

# Create object of local c1 class
a = c1()

# Create object of manustud.c1 class
b = manustud.c1()


output:-
--------
c1 class of prog9e
c1  class  of  manustud

#19)Repeat  manurate  with  list  of  6  objects

Hint:  import  and  use  rat  class  defined  in  manurate  but  do  not  rewrite  the  class  again

What  are  the  object  names  ?  --->  a[0] , a[1] , a[2] , .....a[5]
'''

from manurate import rat

a = [rat() ,rat() ,rat() ,rat() ,rat() ,rat()]
a[0] .get ()
a[1] . get()
a[2] . add(a[0],a[1])
a[3] . sub(a[0],a[1])
a[4] . mul(a[0],a[1])
print('Sum : ', a[2])
print('Difference : ', a[3])
print('Product : ', a[4])
if a[1] . nr == 0:
	print('Division is not permitted')
else:
	a[5] . div(a[0],a[1])
	print('Division : ' , a[5])



