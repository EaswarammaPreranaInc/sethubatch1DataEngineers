* Python - 2 : Constructors 

# prog5 ; growable - obj: (Find Outputs)
class c1:
    def __init__(self):
        self.a = 10
    def m1(self):
        self.b = 20

# End of the class c1
class c2:
    def m3(self):
        x.e = 50

# End of the class c2
def f1():
    x.c = 30
# End of function f1
x = c1()   # constructor adds variable 'a' to object 'x' with value 10
print(x.__dict__)   # {'a' : 10}
x.m1()   # Method adds variable 'b' to object 'x' with value 20
print(x.__dict__)   # {'a':10, 'b':20}
f1()   # Function adds variable 'c' to object 'x' with value 30
print(x.__dict__)   # {'a' :10, 'b':20, 'c':30}
x.d = 40   # Adds variable 'd' to object 'x' with value 40
print(x.__dict__)   # {'a' :10, 'b':20, 'c':30, 'd':40}
y = c2()   # Empty object : there is no constructor in class c2
y.m3()   # Method of class c2 adds variable 'e' to object 'x' with value 50
print(x.__dict__)  # {'a' :10, 'b':20, 'c':30, 'd':40, 'e': 50}
z = c1()   # constructor adds variable 'a' with value 10
print(z.__dict__)   # {'a' : 10}



# Prog6 : shrinkable - obj (Find outputs)
# Shrinkable - obj ( Find outputs)
class c1:
	def __init__(self):
		self.x = 10
		self.y = 20
		self.z = 30

# End of the class
a = c1()   # object is initialized with x = 10, y = 20 and z = 30 by constructor
b = c1()   # object is initialized with x = 10, y = 20 and z = 30 by constructor
print(a.__dict__)   # {'x' : 10, 'y' = 20, 'z' = 30}
print(b.__dict__)   # {'x' : 10, 'y' = 20, 'z' = 30}
del a . x   # Removes variable 'x' from object 'a'
del b . y   # removes variable 'y' from object 'b'
print(a.__dict__)   # {'y' : 20, 'z' = 30}
print(b.__dict__)   # {'x' : 10, 'z' = 30}
#print(a . x)   # Error : No variable 'x' in object 'a'
#print(b . y)   # Error : no variable 'y' in object 'b'



# prog7a ; (same - constructor - name) (find outputs)
class c1:
    def __init__(self):   # Discarded due to another constructor in same class
        print('1st constructor')

    def __init__(self):   # Discarded due to another constructor in same class
        print('2nd constructor')

    def __init__(self):   # Recognized as it is the last constructor 
        print('3rd constructor')
# End of the class
a = c1()



# prog7b ; Find outputs
class c1:
    def __init__(self):         
        print('No argument constructor')
    
    def __init__(self, x): 
        print('Single argument constructor')
    
    def __init__(self, x, y):         
        print('Two argument constructor')

# End of the class
a = c1(10, 20)
#b = c1(30)   # Error : Arg is not passed for 'y' of the constructor
#c = c1()    # Error : Args are not passed for 'x' and 'y' of the constructor



# prog7c (output)
class c1:
    def __init__(self):
        print('No argument constructor')
    def __init__(self, x):
        print('Single argument constructor:', x)
    def __init__(self,x = 100, y = 200):
        print('Two argument constructor:', x, y)

# End of the class
a = c1(10, 20)    # Two argument constructor : <space> 10 <space> 20
b = c1(30)     # Two argument constructor : <space> 30 <space> 200
c = c1()    # Two argument constructor : <space> 100 <space > 200 



# prog8a ( class - function - same - name)
def f1():    # discarded becoz a class is defined with same name later
	print('Function')
	return 25
class f1:    # Recognized 
	def __init__(self):
		print('constructor')

# end of the class
a = f1()   # Executes constructor of class f1
print(a)   # __str__() method of object class returns type and address of object 'a'



# prog8b (find ouputs)
class c1:
	def __init__(self):
		print('constructor')
def c1():
	print('Function')

# End of the class
a = c1()
print(a)



# prog8c (output)
class c1:    # Discarded becoz a function is with same name later 
    def __init__(self):
        print('constructor')

def c1(x):   # recognized
    print('Function:', x)

# end of the class 
#a = c1()   # Error : Arg is not passed for avg 'x' of function c1()
b = c1(25)   # Executes function c1() which returns none by default
print(b)     # None    



# prog9a.py
# Save the program in prog9a.py file
class c1:
    def __init__(self):
        print('c1 class of prog9a')



# prog9b.py
from prog9a import c1    # Discards class c1 becoz another class with same name is defined later 
class c1:   # Recognized 
	def __init__(self):
		print('c1 class of prog9b')
a = c1()    # Executes constructor of class c1 in same module i.e. c1 class of prog9b



# prog9c.py
class c1:      # Discarded becoz a class with same name c1 is imported from prog9a
	def __init__(self):
		print('c1 class of prog9c')
from prog9a import c1   # Recognized
a = c1()     # Recognized constructor of class c1 from prog9a  i.e. c1 class of prog9a



# prog9d.py
from prog9a import c1 as c2    # How to import class c1 from prog9a with from statement
class c1:
	def __init__(self):
		print('c1 class of prog9d')
a = c1()   # How to create c1 class object of current module
b = c2()   # How to create c1 class object of prog9a



# prog9e.py
import prog9a  # How to import prog9a
class c1:
	def __init__(self):
		print('c1 class of prog9e')
a = c1()    # How to create c1 class object of current module
b = prog9a.c1()   # How to create c1 class object of prog9a


# prog10a.py
class Test:
    def __init__(self):
        self.x = 10    # How to initialize public variable 'x' to 10
        self.__y = 20  # How to initialize private variable 'y' to 20

    def m1(self):
        print('m1 method')
        print('variable x:', self.x)   # how to print variable 'x'
        print('private variable y:', self.__y)   # how to print private variable 'y'
        self.__m2()  # How to call private method m2()
        print('Back to m1 method')

    def __m2(self):
        print('__m2 method')
        print('variable x:', self.x)   # how to print variable 'x'
        print('private variable y:', self.__y)   # how to print private variable 'y'

# End of class

t = Test()   # object is initilaized with x=10 and __y=20 by constructor
print('Outside')
print('variable x:', t.x)   # how to print variable 'x'
print('private variable y:', t._Test__y)  # how to print variable 'y'
# print(t.__y)  # Error : Not private variable can not be used outside the class as it is not visible
print( t.__dict__)  # {'x' : 10, '_Test__y' : 20}
t.m1()  # How to call method m1()
t._Test__m2()  # How to call method m2()
# t.__m2()  # Error : private method can not be called outside the class as it is not visible
print('End')



# prog11.py
class c1:
	def __init__(self):
		self.x = 10   # How to initialize public variable 'x' with 10
		self.__x = 20   # How to initialize private variable 'x' with 20
		self._x__ = 30    # How to initialize public dunder variable 'x' with 30
    
	def m1(self):
		print('public method')
   
	def __m1(self):
		print('private method')
	
	def __m1__(self):
		print('public Dunder method')

# End of the class
a = c1()
print(a.x)  # how to print variable 'x'
print(a._x__)  # how to print public dunder variable 'x'
#print(a.__x)   # Error : Not visible outside the class 
a.m1()   # How to call public method m1()
a.__m1__()   # how to call public dunder method m1()
a.__m1__
a.m1
a._c1__m1()  # How to call private method m1()
# a.__m1()   # Error : Not visible outside the class
