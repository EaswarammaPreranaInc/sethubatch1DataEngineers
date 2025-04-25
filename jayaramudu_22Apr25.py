#Ex-1
# Find  outputs (Home work)
class  Person:
	def  __init__(self):
		self . name  =  ''
	@property
	def   name(self):
		print('getter  method')
		return  self . _name
	@name.setter
	def   name(self , value):
		print('Setter  Method')  # Setter  Method
		self . _name = value
	@name . deleter
	def  name(self):
		print('Deleter  method ')
		del  self . _name
#end  of  the  class
p = Person() # create  non-empty object and initialize variable name is empty
print(p . name) #  getter  method #  Empty name
p . name = 'Vamsi' # setter  method  modifies object variable name
print(p . name)  #  setter  method Vamsi
del   p . name # Deleter  method  delete _name
# print(p . name) # getter  method  Error because no variable name
del   p # delete object

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
'''

class Emp:
    def __init__(self):
        self.empno=int(input('Enter  employee  number : '))
        self.ename=input('Enter a emp name: ')
        self.sal=int(input("Enter a emp salary: "))

    @property
    def empno(self):
        return self._empno
    @empno.setter
    def empno(self,value):
        if value > 0:
         self._empno=value
        else:
            raise  ValueError(" Empno cannot be negative")
    @property
    def ename(self):
        return self._ename
    @ename.setter
    def ename(self,value):
        if value!='':
            self._ename=value
        else:
            raise ValueError('Emp  name cannot be empty string')
    @property
    def sal(self):
        return self._sal
    @sal.setter
    def sal(self,value):
        if value>0:
            self._sal=value
        else:
            raise ValueError("Salary cannot be negative")
try:
    e=Emp()
    print('Employee  number : ',e.empno)
    print('Employee name  : ',e.ename)
    print('Employee name  : ',e.sal)
except ValueError as msg:
    print(msg)

# parent  and  child  classes  have  different  Instance  methods
class   parent:
	def   m1(self):
		print('parent   method')
class   child(parent):
	def   m2(self):
		self.m1()  # How  to  call  m1()  method  of  parent  class
		super().m1()# How  to  call  m1()  method  of  parent  class  in  another  way  without  creating  another  object
		m1() # How  to  call  function  m1()
		# parent . m1()
		print('child  method')
#end  of  the  class
def   m1():
	print('Function')
# End  of  the  function
p= parent()
p.m1()# How  to  call  m1()  method  of  parent  class
c=child()
c.m2() # How  to  call  m2()  method  of  child  class
# p . m2() # Error because m2 method not in parent class
c . m1() # call parent m1 method thorough child class object reference

#Ex-4
#  parent  and  child  classes  have  same  Instance  method
class  parent:
	def   m1(self):
		print('Parent  Method')
class   child(parent):
	def   m1(self):
		super.m1() # How  to  call  m1()  method  of  parent  class
		m1() #How  to  call  function  m1()
		self . m1()
		print('Child  Method')
# End  of  the  class
def  m1():
	print('m1  function')
# End of  the  function
p=parent()
p.m1()# How  to  call  m1()  method  of  parent  class
c= child()
c.m1()# How  to  call  m1()  method  of  child  class

#Ex-5
# parent  and  child  classes  have  different  class  methods
class parent:
    @classmethod
    def   m1(cls):
        print('parent  Method')
class child(parent):
    @classmethod
    def m2(cls):
        super().m1() # How  to  call  m1()  method  of  parent  class
        cls.m1() #  How  to  call  m1()  method  of  parent  class  in  another  way
        super(child,child()).m1() # How  to  call  m1()  method  of  parent  class  in  one  more  way

        parent.m1() #How  to  call  m1()  method  of  parent  class  in  last  way
        # self . m1() # self not define
	    # m1() # m1 method not define G V
    print('child  Method')
# End  of  the  class

parent.m1()# How  to  call  m1()  method  of  parent  class
child.m2()# How  to  call  m2()  method  of  child  class
#super() . m1() # missing  one PA
# self . m1() # self not define

#Ex-6
# parent  and  Child  classes  have  same  class   method
class   parent:
	@classmethod
	def   m1(cls):
		print('parent  Method')
class   child(parent):
	@classmethod
	def  m1(cls):
		super().m1() # How  to  call  m1()  method  of  parent  class
		super(child,child()).m1()# How  to  call  m1()  method  of  parent  class  in  another  way
		# cls . m1()
		# self . m1() # self not define
		# m1() # there is no m1 function
		print('child  Method')
# End  of  the  class
parent.m1() # How  to  call  m1()  method  of  parent  class
child.m1() # How  to  call  m1()  method  of  child  class

#Ex-7
# Parent  and  Child  classes  have  different  static  methods
class   parent:
	@staticmethod
	def  m1():
		print('parent  method')
class   child(parent):
	@staticmethod
	def   m2():
		parent.m1() # How  to  call  m1()  method  of  parent  class
		super(child,child()) .m1()# How  to  call  m1()  method  of  parent  class  in  another  way
		#super() . m1()
		# self . m1() # self not define
		# cls . m1() #
		print('child  method')
#end of the class
parent.m1() # How  to  call  m1()  method  of  parent  class
child.m2() # How  to  call  m2()  method  of  child  class
child . m1()

#Ex-8
# Parent  and  Child  classes  have  same  static  method
class   parent:
	@staticmethod
	def   m1():
		print('parent  method')
class   child(parent):
	@staticmethod
	def   m1():
		parent.m1() # How  to  call  m1()  method  of  parent  class
		super(child,child()).m1() # How  to  call  m1()  method  of  parent  class in   another way
		# super() . m1()
		#self . m1()  # self is not define
		#cls . m1() # cls not define
		print('child  method')
#end of the class
parent.m1() # How  to  call  m1()  method  of  parent  class
child.m1() # How  to  call  m1()  method  of  child  class

#Ex-9
# Parent  and  child  classes  have   static  variables  with  different  names
class   parent:
	x = 10
	def  m1(self):
		print(self.x) #How  to  print  variable  'x'
		print(parent.x) # How  to  print  variable  'x'  in  another  way
		# print(x) # x is not define
# End  of  parent  class
class   child(parent):
	y = 20
	def  m2(self):
		print(parent.x)# How  to  print  variable  'x'
		print(self.x)# How  to  print  variable  'x'  in  another  way
		print(super(child,child()).x) # How  to  print  variable  'x' in  one  more  way
		print(child.x)# How  to  print  variable  'x' in  last  way
		print(self.y) # How  to  print  variable  'y'
		print(child.y) # How  to  print  variable  'y'  in  another  way
		# print(super() . y) # Error parent' has no attribute 'y'
		# print(y) # y not define
# End  of child  class
p=parent()
p.m1() # How  to  call   m1()  method  of  parent  class
c=child()
c.m2() # How  to  call   m2()  method  of  child  class

#Ex-10
# Parent  and  Child  classes  have  static  variables  with  same  name
class   parent:
	x = 10
	def  m1(self):
		print(self.x) # How  to  print  variable  'x'  of  parent  class
		print(parent.x)# How  to  print  variable  'x'  of  parent  class  in  another  way
class   child(parent):
	x = 20
	def  m1(self):
		print(parent.x) # How  to  print  variable  'x'  of  parent  class
		print(super(child,child()).x) # How  to  print  variable  'x'  of  parent  class  in  another  way
		print(self.x)# How  to  print  variable  'x'  of  child  class
		print(child.x)# How  to  print  variable  'x'  of  child  class  in  another  way
# End  of  the  class
p=parent()
p.m1()#How  to  call  m1()  method  of  parent  class
c=child()
c.m1() # How  to  call  m1()  method  of  child  class

#Ex-11
#  What  are  the  outputs  if  inputs  are  10 , 20 , 30 , 40  , 50 , 60
class   parent:
        def get(self):
            self.a=int(input('Enter any number: '))
            self.b=int(input("Enter any number: ")) # How  to   read  inputs  into   variables  a  and  b  of  object  self
        def    disp(self):
            print(self.a,self.b,end="\t") # How  to  print  variables  a  and  b  of  object  self  in  same  line  separated  by  tab
# End  of  Parent  class
class    child(parent):
    def    get(self):
        super().get() # How  to   read  inputs  into   variables  a  and  b  of  object  self
        self.c = int(input('Enter any number: '))
        self.d = int(input("Enter any number: ")) # How  to   read  inputs  into   variables  c  and  d  of  object  self
    def   disp(self):
        def disp(self):
            print(self.a, self.b, sep='\t') # How  to  print  variables  a  and  b  of  object  self  in  same  line  separated  by  tab
            print(self.c, self.d, sep='\t') # How  to  print  variables  c  and  d  of  object  self  in  same  line  separated  by  tab
    def  total(self):
        return self.a + self.b + self.c + self.d #   sum  of  values  in  object  self
# End of child class
print('parent  object')
p=parent()
p.get() # How  to  read  inputs  into  parent  class  object  'p'
print('child  object')
c=child()
c.get() # How  to  read  inputs  into  child  class  object  'c'
print('parent  object  :  ' , end = '\t')
print(p) # How  to  print  object  'p'
print()
print('child  object  :  ' , end = '\t')
print(c) # How  to  print  object  'c'
print('Sum of  the  values  in  child  object :  ' , c.total()) # How  to  obtain  sum of  values  of  object  'c'
