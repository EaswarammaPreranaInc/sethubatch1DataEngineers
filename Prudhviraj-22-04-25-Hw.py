# Find  outputs (Home work)
class  Person:
	def  __init__(self):
		self ._name  =  ''
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
print(p ._name)
del   p ._name
#print(p ._name)
del   p
"""
Output:
getter  method

Setter  Method
Vamsi
"""

# parent  and  child  classes  have  different  Instance  methods
class   parent:
	def   m1(self):
		print('parent   method')
class   child(parent):
	def   m2(self):
		a=parent()
		a.m1()         #How  to  call  m1()  method  of  parent  class
		super().m1()   #How  to  call  m1()  method  of  parent  class  in  another  way  without  creating  another  object
		self.m1()      #How  to  call  function  m1()
		parent . m1(self)
		print('child  method')
#end  of  the  class
def   m1():
	print('Function')
# End  of  the  function
p=parent()
p.m1()      #How  to  call  m1()  method  of  parent  class
c=child()
c.m2()      #How  to  call  m2()  method  of  child  class
#p . m2()
#c . m1()
"""
Output:
parent   method
parent   method
parent   method
parent   method
parent   method
child  method
"""

#  parent  and  child  classes  have  same  Instance  method
class  parent:
	def   m1(self):
		print('Parent  Method')
class   child(parent):
	def   m1(self):
		super().m1()#How  to  call  m1()  method  of  parent  class
		m1() #How  to  call  function  m1()
		#self . m1()
		print('Child  Method')
# End  of  the  class
def  m1():
	print('m1  function')
# End of  the  function
p=parent()
p.m1()        #How  to  call  m1()  method  of  parent  class
c=child()   
c.m1()      #How  to  call  m1()  method  of  child  class
"""
Output:
Parent  Method
Parent  Method
m1  function
Child  Method
"""

# parent  and  child  classes  have  different  class  methods
class  parent:
	@classmethod
	def   m1(cls):
		print('parent  Method')
class  child(parent):
	@classmethod
	def   m2(cls):
		super().m1()    #How  to  call  m1()  method  of  parent  class
		a=parent()   #How  to  call  m1()  method  of  parent  class  in  another  way
		a.m1()
		cls.m1() #How  to  call  m1()  method  of  parent  class  in  one  more  way
		c.m1()   #How  to  call  m1()  method  of  parent  class  in  last  way
		#self . m1()
		#m1()
		print('child  Method')
# End  of  the  class
p=parent()
p.m1()       #How  to  call  m1()  method  of  parent  class
c=child()    #How  to  call  m2()  method  of  child  class
c.m2()
child . m1()
#super() . m1()
#self . m1()
"""
Output:
parent  Method
parent  Method
parent  Method
parent  Method
parent  Method
child  Method
parent  Method
"""

# parent  and  Child  classes  have  same  class   method
class   parent:
	@classmethod
	def   m1(cls):
		print('parent  Method')
class   child(parent):
	@classmethod
	def  m1(cls):
		super().m1()   #How  to  call  m1()  method  of  parent  class
		a=parent()
		a.m1()         #How  to  call  m1()  method  of  parent  class  in  another  way
		#cls . m1() --->Leads to recursion  
		#self . m1()
		#m1()
		print('child  Method')
# End  of  the  class
p=parent()
p.m1()           #How  to  call  m1()  method  of  parent  class
c=child()        #How  to  call  m1()  method  of  child  class
c.m1()
"""
Output:
parent  Method
parent  Method
parent  Method
child  Method
"""

# Parent  and  Child  classes  have  different  static  methods
class   parent:
	@staticmethod
	def  m1():
		print('parent  method')
class   child(parent):
	@staticmethod
	def   m2():
		c.m1()        #How  to  call  m1()  method  of  parent  class
		a=parent()    #How  to  call  m1()  method  of  parent  class  in  another  way
		a.m1()
		super() . m1()
		self . m1()
		cls . m1()
		print('child  method')
#end of the class
p=parent()   #How  to  call  m1()  method  of  parent  class
p.m1()
c=child()    #How  to  call  m2()  method  of  child  class
c.m1()
#child . m1()
"""
Output:
parent  method
parent  method
"""

# Parent  and  Child  classes  have  same  static  method
class   parent:
	@staticmethod
	def   m1():
		print('parent  method')
class   child(parent):
	@staticmethod
	def   m1():
		parent.m1()    #How  to  call  m1()  method  of  parent  class
		#How  to  call  m1()  method  of  parent  class in   another way
		#super() . m1()
		#self . m1()
		#cls . m1()
		print('child  method')
#end of the class  
parent.m1()    
child.m1()
"""
Output:
parent  method
parent  method
child  method
"""

# Parent  and  child  classes  have   static  variables  with  different  names
class   parent:
	x = 10
	def  m1(self):
		print(self.x)             #How  to  print  variable  'x'
		print(parent.x)           #How  to  print  variable  'x'  in  another  way
		#print(x)
# End  of  parent  class
class   child(parent):
	y = 20
	def  m2(self):
		print(self.x)          #How  to  print  variable  'x'
		print(parent.x)        #How  to  print  variable  'x'  in  another  way
		print(child.x)         #How  to  print  variable  'x' in  one  more  way
		print(super().x)       #How  to  print  variable  'x' in  last  way
		print(self.y)          #How  to  print  variable  'y'
		print(child.y)         #How  to  print  variable  'y'  in  another  way
		#print(super() . y)
		print(self.y)
# End  of child  class
p=parent()#How  to  call   m1()  method  of  parent  class
p.m1()
c=child() #How  to  call   m2()  method  of  child  class
c.m2()
"""
Output:
10
10
10
10
10
10
20
20
20
"""

# Parent  and  Child  classes  have  static  variables  with  same  name
class   parent:
	x = 10
	def  m1(self):
		print(self.x)#How  to  print  variable  'x'  of  parent  class
		print(parent.x)#How  to  print  variable  'x'  of  parent  class  in  another  way
class   child(parent):
	x = 20
	def  m1(self):
		print(super().m1())   #How  to  print  variable  'x'  of  parent  class
		print(p.m1())    #How  to  print  variable  'x'  of  parent  class  in  another  way
		print(self.x)         #How  to  print  variable  'x'  of  child  class
		print(child.x)        #How  to  print  variable  'x'  of  child  class  in  another  way
# End  of  the  class
p=parent()  #How  to  call  m1()  method  of  parent  class
p.m1()
c=child()   #How  to  call  m1()  method  of  child  class
c.m1()
"""
Output:
10
10
20
10
None
10
10
None
20
20
"""

#  What  are  the  outputs  if  inputs  are  10 , 20 , 30 , 40  , 50 , 60
class   parent:
	def    get(self):
		self.a=int(input("Enter the Number: "))
		self.b=int(input("Enter the Number: "))
	def    disp(self):
		print(self.a,self.b,sep='\t')#How  to  print  variables  a  and  b  of  object  self  in  same  line  separated  by  tab
# End  of  Parent  class
class    child(parent):
	def    get(self):
		self.a=int(input("Enter the Number: "))
		self.b=int(input("Enter the Number: "))
		self.c=int(input("Enter the Number: "))
		self.d=int(input("Enter the Number: "))
	def   disp(self):
		print(self.a,self.b,sep='\t')
		print(self.c,self.d,sep='\t')
	def  total(self):
			return self.a + self.b + self.c + self.d
# End of child class
print('parent  object')
p = parent()  # 
p.get()#How  to  read  inputs  into  parent  class  object  'p'
print('child  object')
c=child()   #How  to  read  inputs  into  child  class  object  'c'
c.get()
print('parent  object  :  ' , end = '\t')
p.disp()#How  to  print  object  'p'
print()
print('child  object  :  ' , end = '\t')
c.disp() #How  to  print  object  'c'
print('Sum of  the  values  in  child  object :  ' ,  c.total())
"""
Output:
parent  object
Enter the Number: 10
Enter the Number: 20
child  object
Enter the Number: 30
Enter the Number: 40
Enter the Number: 50
Enter the Number: 60
parent  object  :       10      20

child  object  :        30      40
50      60
Sum of  the  values  in  child  object :   180
"""
'''
'''
1) Write  a  program  to  validate  emp  number , emp  name  and  salary  and  also  print  them

2) Emp  number  and  salary  can  not  be  -ve

3) Emp  name  can  not  be  empty  string

4) class  name   is  Emp

5) 3  getter  and  3  setter  methods

6) Constructor  initializes  empno , ename  and  sal

7) Outside  the  class
    ----------------------
    a) Create  Emp  class  object
    b) Print  empno , ename  and  sal

try:
	class employe:
		def __init__(self):
			self.empno=eval(input("Enter the Employee id: "))
			self.empname=input("Enter the Employee Name: ")
			self.sal=eval(input("Enter the Employee Salary: "))
		@property
		def empno(self):
			return self._empno
		@empno.setter
		def empno(self,empno):
				if empno<0:
					raise ValueError('Employee id cannot be Negative')
				else:
					self._empno=empno
		@property
		def empname(self):
			return self._empname
		@empname.setter
		def empname(self,empname):
			if empname==" ":
				raise ValueError('Empty String is not Permitted')
			else:
				self._empname=empname
		@property
		def sal(self):
			return self._sal
		@sal.setter
		def sal(self,sal):
			if sal<0:
				raise ValueError('Employee Salary cannot be Negative')
			else:
				self._sal=sal
	a=employe()
	print("Employee id:",a.empno)
	print("Employee name  :",a.empname)
	print("Employee Salary  :",a.sal)
except Exception as e:
	print(e)
