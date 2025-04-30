Q1 #Find  outputs (Home work)
class  Person:
	def  __init__(self):
		self . name  =  ''
	@property
	def   name(self):
		print('getter  method')
		return  self . _name
	@name . setter
	def   name(self , value):
		print('Setter  Method')
		self . _name = value
	@name . deleter
	def  name(self):
		print('Deleter  method ')
		del  self . _name
#end  of  the  class
p = Person()
print(p . name)
p . name = 'Vamsi'
print(p . name)
del   p . name
#print(p . name)  #error - p.name is deleted 
del   p

OP-
Setter  Method
getter  method

Setter  Method
getter  method
Vamsi
Deleter  method
#------------------------------------------------------------------------------------------------
Q2 Write  a  program  to  validate  emp  number , emp  name  and  salary  and  also  print  them

class Emp:
	def __init__(self):
		self.empno=int(input('Enter employee number: ')) 
		self.empname=input('Enter employee name: ')
		self.sal=float(input('Enter employee salary: '))
	@property
	def empno(self):
		return self._empno
	@property
	def empname(self):
		return self._empname
	@property
	def sal(self):
		return self._sal
	@empno.setter
	def empno(self,empno):
		if empno<0:
			raise ValueError('Empno cannot be negative')
		self._empno=empno
	@empname.setter
	def empname(self,empname):
		if empname=='':
			raise ValueError('Emp name cannot be empty string')
		self._empname=empname
	@sal.setter
	def sal(self,sal):
		if sal<0:
			raise  ValueError('Salary cannot be negative')
		self._sal=sal
try:
	e=Emp()
	print('Employee number: ',e.empno)
	print('Emplyee name: ',e.empname)
	print('Employee salary: ',e.sal)
except ValueError as msg:
	print(msg)


OP-
Enter  employee  number :  -10
Empno cannot be negative

Enter  employee  number :  10
Enter  employee  name :
Emp  name cannot be empty  string

Enter  employee  number :  10
Enter  employee  name :  Rama Rao
Enter  salary :  -10
Salary cannot be negative

Enter  employee  number :  10
Enter  employee  name :  Rama  Rao
Enter  salary :  100000
Employee number  :  10
Employee name  :  Rama  Rao
Employee salary :   100000.0
#---------------------------------------------------------------------------------------------------------
Q3 #parent  and  child  classes  have  different  Instance  methods

class   parent:
	def   m1(self):
		print('parent   method')
class   child(parent):
	def   m2(self):
		super().m1()  #How  to  call  m1()  method  of  parent  class
		self.m1()     #How  to  call  m1()  method  of  parent  class  in  another  way  without  creating  another  object
		super(child,self).m1() #How to call m1() method of parent classs in another 
		m1()                   #How  to  call  function  m1()
		#parent . m1()
		print('child  method')
#end  of  the  class
def   m1():
	print('Function')
# End  of  the  function
p=parent()  #How  to  call  m1()  method  of  parent  class
p.m1() 
c=child()  #How  to  call  m2()  method  of  child  class
c.m2()
#p . m2()   #error - there is no m2() method in parent class 
c . m1()   

OP-
parent   method
parent   method
parent   method
parent   method
Function
child  method
parent   method
#-------------------------------------------------------------------------------------
Q4 #parent  and  child  classes  have  same  Instance  method

class  parent:
	def   m1(self):
		print('Parent  Method')
class   child(parent):
	def   m1(self):
		super().m1()  #How  to  call  m1()  method  of  parent  class
		m1()  #How  to  call  function  m1()
		#self . m1()  #recursion error 
		print('Child  Method')
# End  of  the  class
def  m1():
	print('m1  function')
# End of  the  function
a=parent() #How  to  call  m1()  method  of  parent  class
a.m1()
b=child()
b.m1()     #How  to  call  m1()  method  of  child  class

OP-
Parent  Method
Parent  Method
m1  function
Child  Method
#------------------------------------------------------------------------------------
Q5 #parent  and  child  classes  have  different  class  methods

class  parent:
	@classmethod
	def   m1(cls):
		print('parent  Method')
class  child(parent):
	@classmethod
	def   m2(cls):
		super().m1()     #How  to  call  m1()  method  of  parent  class
		super(child,cls).m1()        #How  to  call  m1()  method  of  parent  class  in  another  way
		parent.m1()      #How  to  call  m1()  method  of  parent  class  in  one  more  way
		cls.m1()        #How  to  call  m1()  method  of  parent  class  in  last  way
		#self . m1()        #error - self is not defined
		#m1()            #error - no m1() method outside class
		print('child  Method')
# End  of  the  class
parent.m1()        #How  to  call  m1()  method  of  parent  class
child.m2()          #How  to  call  m2()  method  of  child  class
child . m1()
#super() . m1()      #error - super() function with zero arguments outside class doesn't work
#self . m1()         #error - self is not defined outside class

OP-
parent  Method
parent  Method
parent  Method
parent  Method
parent  Method
child  Method
parent  Method
#-------------------------------------------------------------------------------------------
Q6 #parent  and  Child  classes  have  same  class   method

class   parent:
	@classmethod
	def   m1(cls):
		print('parent  Method')
class   child(parent):
	@classmethod
	def  m1(cls):
		parent.m1() #How  to  call  m1()  method  of  parent  class
		super(child,cls).m1() #How  to  call  m1()  method  of  parent  class  in  another  way
		#cls . m1()       #recursion error
		#self . m1()   # error - self is not defined
		#m1()           #error - no m1() function outside class
		print('child  Method')
# End  of  the  class
parent.m1() #How  to  call  m1()  method  of  parent  class
child.m1()  #How  to  call  m1()  method  of  child  class

OP-
parent  Method
parent  Method
parent  Method
child  Method
#-----------------------------------------------------------------------------------------
Q7 #Parent  and  Child  classes  have  different  static  methods
class   parent:
	@staticmethod
	def  m1():
		print('parent  method')
class   child(parent):
	@staticmethod
	def   m2():
		parent.m1()   #How  to  call  m1()  method  of  parent  class
		child.m1() #How  to  call  m1()  method  of  parent  class  in  another  way
		#super() . m1()  #super() doesn't work for static method
		#self . m1()      #error - self is not defined
		#cls . m1()      #error - cls is not defined
		print('child  method')
#end of the class
parent.m1() #How  to  call  m1()  method  of  parent  class
child.m2()  #How  to  call  m2()  method  of  child  class
child . m1()

OP-
parent  method
parent  method
parent  method
child  method
parent  method
#--------------------------------------------------------------------------------------------
Q8 #Parent  and  Child  classes  have  same  static  method
class   parent:
	@staticmethod
	def   m1():
		print('parent  method')
class   child(parent):
	@staticmethod
	def   m1():
		parent.m1() #How  to  call  m1()  method  of  parent  class
		p=parent()
		p.m1() #How  to  call  m1()  method  of  parent  class in   another way
		#super() . m1() #error 
		#self . m1()     #error
		#cls . m1()      #error
		print('child  method')
#end of the class
parent.m1()   #How  to  call  m1()  method  of  parent  class
child.m1()    #How  to  call  m1()  method  of  child  class

OP-
parent  method
parent  method
parent  method
child  method
#----------------------------------------------------------------------------------------------
Q9 #Parent  and  child  classes  have   static  variables  with  different  names

class   parent:
	x = 10
	def  m1(self):
		print(parent.x)  #How  to  print  variable  'x'    ---10
		print(p.x)       #How  to  print  variable  'x'  in  another  way ----10
		#print(x)        # error - no local variable x
# End  of  parent  class
class   child(parent):
	y = 20
	def  m2(self): 
		print(parent.x)  #How  to  print  variable  'x'    ---10  
		print(c.x)       #How  to  print  variable  'x'  in  another  way ------10
		print(super().x)   #How  to  print  variable  'x' in  one  more  way ----10
		print(self.x)    #How  to  print  variable  'x' in  last  way --------10
		print(child.y)   #How  to  print  variable  'y'     ------20
		print(self.y)    #How  to  print  variable  'y'  in  another  way -----20
		#print(super() . y) #no varaible y in parent class
		#print(y)         #error - no local variable y 
# End  of child  class
p=parent()    #How  to  call   m1()  method  of  parent  class
p.m1() 
c=child()
c.m2()        #How  to  call   m2()  method  of  child  class
#---------------------------------------------------------------------------------------------
Q10 #Parent  and  Child  classes  have  static  variables  with  same  name

class   parent:
	x = 10
	def  m1(self):
		print(parent.x)        #How  to  print  variable  'x'  of  parent  class ------10
		print(self.x)             #How  to  print  variable  'x'  of  parent  class  in  another  way------10
class   child(parent):
	x = 20
	def  m1(self):
		print(parent.x)      #How  to  print  variable  'x'  of  parent  class--------10
		print(super().x)      #How  to  print  variable  'x'  of  parent  class  in  another  way-------10
		print(child.x)       #How  to  print  variable  'x'  of  child  class ----20
		print(self.x)       #How  to  print  variable  'x'  of  child  class  in  another  way   ------20
# End  of  the  class
p=parent() #How  to  call  m1()  method  of  parent  class
p.m1() 
c=child()
c.m1()       #How  to  call  m1()  method  of  child  class
#-------------------------------------------------------------------------------------------------
Q11 #What  are  the  outputs  if  inputs  are  10 , 20 , 30 , 40  , 50 , 60

class   parent:
	def    get(self):
		self.a=int(input('Enter value of a: '))   
		self.b=int(input('Enter value of b: '))     #How  to   read  inputs  into   variables  a  and  b  of  object  self
	def    disp(self):
		print(f'{self.a} \t {self.b} ')        #How  to  print  variables  a  and  b  of  object  self  in  same  line  separated  by  tab
# End  of  Parent  class
class    child(parent):
	def    get(self):
		self.a=int(input('Enter value of a: '))  
		self.b=int(input('Enter value of b: '))     #How  to   read  inputs  into   variables  a  and  b  of  object  self
		self.c=int(input('Enter value of c: '))      
		self.d=int(input('Enter value of d: '))      #How  to   read  inputs  into   variables  c  and  d  of  object  self
	def   disp(self):
		print(f'{self.a} \t {self.b}') # How  to  print  variables  a  and  b  of  object  self  in  same  line  separated  by  tab
		print(f'{self.c} \t {self.d}') #How  to  print  variables  c  and  d  of  object  self  in  same  line  separated  by  tab
	def  total(self):
		return self.a+self.b+self.c+self.d  #return  sum  of  values  in  object  self
# End of child class
print('parent  object')
p=parent()
p.get()   #How  to  read  inputs  into  parent  class  object  'p'
print('child  object')
c=child()
c.get()     #How  to  read  inputs  into  child  class  object  'c'
print('parent  object  :  ' , end = '\t')
p.disp()   # How  to  print  object  'p'
print()
print('child  object  :  ' , end = '\t')
c.disp()         #How  to  print  object  'c'
print('Sum of  the  values  in  child  object :  ' ,c.total())  #How  to  obtain  sum of  values  of  object  'c'

OP-
parent  object
Enter value of a: 10
Enter value of b: 20
child  object
Enter value of a: 30
Enter value of b: 40
Enter value of c: 50
Enter value of d: 60
parent  object  :       10       20

child  object  :        30       40
50       60
Sum of  the  values  in  child  object :   180
'''