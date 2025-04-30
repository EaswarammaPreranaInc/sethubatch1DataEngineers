'''
#1) Find  outputs (Home work)
class  Person:
	def  __init__(self):
		self . name  =  ''
	@property
	def   name(self):
		print('getter  method')
		return  self ._name
	@name . setter
	def   name(self , value):
		print('Setter  Method')
		self . _name = value
	@name . deleter
	def  name(self):
		print('Deleter  method ')
		del  self . _name
#end  of  the  class
p = Person() # non empty object is created by constructor
print(p . name)
p . name = 'Vamsi'
print(p . name)
del   p . name # deleted vamshi 
#print(p . name) #Error : empty
del   p # deleter () Executes when an object is deleted

output:-
-----------
Setter  Method
getter  method

Setter  Method
getter  method
Vamsi
Deleter  method

#2)Write  a  program  to  validate  emp  number , emp  name  and  salary  and  also  print  them

2) Emp  number  and  salary  can  not  be  -ve

3) Emp  name  can  not  be  empty  string

4) class  name   is  Emp

5) 3  getter  and  3  setter  methods

6) Constructor  initializes  empno , ename  and  sal

7) Outside  the  class
    ----------------------
    a) Create  Emp  class  object
    b) Print  empno , ename  and  sal

class Emp:
    def __init__(self, empno, ename, sal):
        self.set_empno(empno)
        self.set_ename(ename)
        self.set_sal(sal)

    # Getter methods
    def get_empno(self):
        return self.__empno

    def get_ename(self):
        return self.__ename

    def get_sal(self):
        return self.__sal

    # Setter methods with validation
    def set_empno(self, empno):
        if empno < 0:
            raise ValueError("Empno cannot be negative")
        self.__empno = empno

    def set_ename(self, ename):
        if ename.strip() == "":
            raise ValueError("Ename cannot be empty")
        if not ename.replace(" ", "").isalpha():
            raise ValueError("Ename must contain only alphabets")
        self.__ename = ename

    def set_sal(self, sal):
        if sal < 0:
            raise ValueError("Salary cannot be negative")
        self.__sal = sal


# Outside the class: taking input and validating
while True:
    try:
        empno = int(input("Enter employee number: "))
        if empno < 0:
            print("Empno cannot be negative")
            continue
        break
    except ValueError:
        print("Please enter a valid integer for empno")

while True:
    ename = input("Enter employee name: ")
    if ename.strip() == "":
        print("Ename cannot be empty")
    elif not ename.replace(" ", "").isalpha():
        print("Ename must contain only alphabets")
    else:
        break

while True:
    try:
        sal = float(input("Enter employee salary: "))
        if sal < 0:
            print("Salary cannot be negative")
            continue
        break
    except ValueError:
        print("Please enter a valid number for salary")

# Create Emp object
e = Emp(empno, ename, sal)

# Print employee details
print("\nEmployee Details:")
print("Employee Number:", e.get_empno())
print("Employee Name:", e.get_ename())
print("Employee Salary:", e.get_sal())

output:-
----------
Enter employee number: -10
Empno cannot be negative
Enter employee number: 80
Enter employee name:
Ename cannot be empty
Enter employee name: 60
Ename must contain only alphabets
Enter employee name: Manisha
Enter employee salary: 50000

Employee Details:
Employee Number: 80
Employee Name: Manisha
Employee Salary: 50000.0


#3)parent  and  child  classes  have  different  Instance  methods
class   parent:
	def   m1(self):
		print('parent   method')
class   child(parent):
	def   m2(self):
		super().m1() # How  to  call  m1()  method  of  parent  class
		parent.m1(self) # How  to  call  m1()  method  of  parent  class  in  another  way  without  creating  another  object
		print(m1()) # How  to  call  function  m1()
		#parent . m1()
		print('child  method')
#end  of  the  class
def   m1():
	print('Function')
# End  of  the  function
c = child()
c.m1() #How  to  call  m1()  method  of  parent  class
c.m2()# How  to  call  m2()  method  of  child  class
#p . m2()
c . m1()

output:-
-----------
parent   method
parent   method
parent   method
Function
None
child  method
parent   method


#4) parent  and  child  classes  have  same  Instance  method
class  parent:
	def   m1(self):
		print('Parent  Method')
class   child(parent):
	def   m1(self):
		super().m1() # How  to  call  m1()  method  of  parent  class
c = child ()
c.m1() # How  to  call  function  m1()
#self . m1()
print('Child  Method')
# End  of  the  class
def  m1():
	print('m1  function')
# End of  the  function
parent().m1() # How  to  call  m1()  method  of  parent  class
m1() # How  to  call  m1()  method  of  child  class

output:-
----------
Parent  Method
Child  Method
Parent  Method
m1  function

#5)parent  and  child  classes  have  different  class  methods
class  parent:
	@classmethod
	def   m1(cls):
		print('parent  Method')
class  child(parent):
	@classmethod
	def   m2(cls):
		parent.m1() # How  to  call  m1()  method  of  parent  class
		super().m1() # How  to  call  m1()  method  of  parent  class  in  another  way
		cls.m1() # How  to  call  m1()  method  of  parent  class  in  one  more  way
		child.m1() # How  to  call  m1()  method  of  parent  class  in  last  way
		# self . m1() Error : No self 
		#m1() # we cannot call m1() method without classname or object here.
		print('child  Method')
# End  of  the  class
parent.m1() # How  to  call  m1()  method  of  parent  class
child.m2() # How  to  call  m2()  method  of  child  class
child . m1()
#super() . m1() # Error: No outside call
#self . m1() # Error : No outside self

output:-
----------
parent  Method
parent  Method
parent  Method
parent  Method
parent  Method
child  Method
parent  Method


#6) parent  and  Child  classes  have  same  class   method
class   parent:
	@classmethod
	def   m1(cls):
		print('parent  Method')
class   child(parent):
	@classmethod
	def  m1(cls):
		parent.m1() # How  to  call  m1()  method  of  parent  class
		super().m1() #How  to  call  m1()  method  of  parent  class  in  another  way
		cls . m1() # Give Recursion Error
		self . m1() # Error : No self ----> NOT EXECUTED
		m1() # we cannot call m1() method without classname or object here.----> NOT EXECUTED
		print('child  Method')# ----> NOT EXECUTED
End  of  the  class
parent.m1() # How  to  call  m1()  method  of  parent  class----> NOT EXECUTED
child.m1() # How  to  call  m1()  method  of  child  class#----> NOT EXECUTED


output:-
-------
without cls.m1()
parent  Method
parent  Method
parent  Method
child  Method
with cls.m1()------> give Recursion here


#7)Parent  and  Child  classes  have  different  static  methods
class   parent:
	@staticmethod
	def  m1():
		print('parent  method')
class   child(parent):
	@staticmethod
	def   m2():
		parent.m1() # How  to  call  m1()  method  of  parent  class
		child.m1() # child How  to  call  m1()  method  of  parent  class  in  another  way
		#super() . m1() # Error
		#self . m1() # Error : NO self outside
		#cls . m1() # Error : No cls outside .
		print('child  method')
#end of the class
parent.m1() # How  to  call  m1()  method  of  parent  class
child.m2()# How  to  call  m2()  method  of  child  class
child . m1()

output:-
-------------
parent  method
parent  method
parent  method
child  method
parent  method

#8)Parent  and  Child  classes  have  same  static  method
class   parent:
	@staticmethod
	def   m1():
		print('parent  method')
class   child(parent):
	@staticmethod
	def   m1():
		parent.m1() # How  to  call  m1()  method  of  parent  class
		super(child, child).m1()# How  to  call  m1()  method  of  parent  class in   another way 
		#super() . m1()# Error
		#self . m1() # Error : NO self
		#cls . m1() # Error:NO cls 
		print('child  method') # -----> NOT EXECUTED
#end of the class
parent.m1() # How  to  call  m1()  method  of  parent  class
child.m1() #How  to  call  m1()  method  of  child  class 

output:-
--------
parent  method
parent  method
parent  method
child  method

#9) Parent  and  child  classes  have   static  variables  with  different  names
class   parent:
	x = 10
	def  m1(self):
		print(parent.x) # How  to  print  variable  'x'
		print(self.x) # How  to  print  variable  'x'  in  another  way
		#print(x)# Error
# End  of  parent  class
class   child(parent):
	y = 20
	def  m2(self):
		print(parent.x) # How  to  print  variable  'x'
		print(self.x) # How  to  print  variable  'x'  in  another  way
		print(child.x)# How  to  print  variable  'x' in  one  more  way
		print(super().x)# How  to  print  variable  'x' in  last  way
		print(child.y)# How  to  print  variable  'y'
		print(self.y) # How  to  print  variable  'y'  in  another  way
		#print(super() . y)# Error
		#print(y) # Error
# End  of child  class
c = child() 
c.m1() # How  to  call   m1()  method  of  parent  class
c.m2() # How  to  call   m2()  method  of  child  class

output:-
------------
10
10
10
10
10
10
20
20


#10) Parent  and  Child  classes  have  static  variables  with  same  name
class   parent:
	x = 10
	def  m1(self):
		print(parent.x) # How  to  print  variable  'x'  of  parent  class
		print(self.__class__.x) # How  to  print  variable  'x'  of  parent  class  in  another  way
class   child(parent):
	x = 20
	def  m1(self):
		print(parent.x) # How  to  print  variable  'x'  of  parent  class
		print(super().x) # How  to  print  variable  'x'  of  parent  class  in  another  way
		print(child.x) # How  to  print  variable  'x'  of  child  class
		print(self.x)# How  to  print  variable  'x'  of  child  class  in  another  way
# End  of  the  class
p = parent()
p.m1() # How  to  call  m1()  method  of  parent  class
c = child()
c.m1() # How  to  call  m1()  method  of  child  class


output:-
----------
0
10
10
10
20
20
'''
#11) What  are  the  outputs  if  inputs  are  10 , 20 , 30 , 40  , 50 , 60
		

class parent:
	def get(self):
		self.a = int(input('enter:'))  # How  to   read  inputs  into   variables  a  and  b  of  object  self
		self.b = int(input('enter:'))
	def disp(self):
		print(self.a, self.b, sep='\t') # How  to  print  variables  a  and  b  of  object  self  in  same  line  separated  by  tab
class child(parent):
    def get(self):
        self.a = int(input('enter:'))  # How  to   read  inputs  into   variables  a  and  b  of  object  self
        self.b = int(input('enter:'))
        self.c = int(input('enter:')) # How  to   read  inputs  into   variables  c  and  d  of  object  self
        self.d = int(input('enter:'))
    def disp(self):
        print(self.a, self.b, sep='\t')# How  to  print  variables  a  and  b  of  object  self  in  same  line  separated  by  tab
        print(self.c, self.d, sep='\t') # How  to  print  variables  c  and  d  of  object  self  in  same  line  separated  by  tab
    def total(self):
        # ? Return sum of all four values
        return self.a + self.b + self.c + self.d
print('parent object')
p = parent()  # How  to  read  inputs  into  parent  class  object  'p'
p.get()  # ? Read input for parent object

print('child object')
c = child()
c.get()  # How  to  read  inputs  into  child  class  object  'c'

print('parent object :', end='\t')
p.disp()  #How  to  print  object  'p'
print()

print('child object :', end='\t')
c.disp()  # How  to  print  object  'c'
print('Sum of the values in child object :', c.total())#  How  to  obtain  sum of  values  of  object  'c'



