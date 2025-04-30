#Ex-1
# Public  and  Private  members  demo  program
class Test:
    def __init__(self):
        self.x =  10   # How  to  initialize  public  variable  'x'  to  10
        self.__y = 20    # How  to  initialize  private  variable  'y'  to  20
    def m1(self):
        print('m1  method')
        print(self.x)  # How  to  print   variable  'x'
        print(self.__y)  # How  to  print  private  variable  'y'
        self.__m2() # How  to  call    private  method   m2()
        print('Back to m1 method')
    def __m2(self):
        print('__m2  method')
        print(self.x) # How  to  print   variable  'x'
        print(self.__y) # How  to  print  private  variable   'y'
# End  of  the  class
t = Test()
print('Outside')
print(t.x)# How  to  print  variable  'x'
print(t._Test__y) # How  to  print   variable  'y'
# print(t.__y) # Error because invalid sysntax
print(t.__dict__)
t.m1()# How  to  call  method  m1()
t._Test__m2()# How  to  call   method  m2()
# t . __m2() # Error because __m2 there no method
print('End') # End

#Ex-2
#  Find  outputs
class  c1:
	def __init__(self):
		self.x=10   # How  to  initialize  public  variable  'x'  with  10
		self.__x=20 # How  to  initialize  private  variable  'x'  with  20
		self.__x__=30 # How  to  initialize  public  dunder  variable  'x'  with  30
	def  m1(self):
		print('public method')
	def  __m1(self):
		print('private method')
	def  __m1__(self):
		print('public Dunder method')
#  End  of  the  class
a = c1()
print(a.x) # How  to  print   variable  'x'
print(a.__x__) # How  to  print  public  dunder  variable  'x'
print(a._c1__x)# How  to  print   private  variable  'x'
# print(a.__x) # Error because object does not have variable __x
a.m1()# How  to  call  public  method  m1()
a.__m1__()# How  to  call  public  dunder  method  m1()
a._c1__m1() # How  to  call  private  method m1()
#a.__m1() # Error because object does not have a __m1 method

#Ex-3
'''
Find  outputs
Assume  that  addresses  of  objects   'a' , 'b' , 'c' , 'd'  and  'e'  are  1000 , 2000 , 3000 , 4000  and  5000  respectively
'''
class   c1:
	def   __init__(self):
		print('Object  is  created  at  address  :  ' , id(self))
	def   __del__(self):
		print(F'Object  at  address  {id(self)}  is  lost')
# End    of    the    class
a = c1() # create object
a = None # object is destroyed and None object is assign to a
b = c1() # create another new object and assign to reference b
del    b # delete reference b and object does not have
c = c1() # create another object
c = c1() # old object is destroy object and create new Object
d=c1()   #  create new Object and assign reference d
e=c1() # create new Object and assign reference d

#Ex-4
# Identify  Error (Home  work)
class c1:
    def __del__(self , x):
        print(self)
        print('destructor')
a = c1() # object is created
# a.__del__(25) # Error  because  __del__ does not contain any arguments except self

#Ex-5
# Find  outputs (Home  work)
class   c1:
	def  __del__(self):
			print('destructor') # print destructor infinite times
			b=c1() # again creating object and execute __del__ infinite
a=c1() # create object

#Ex-6
# Find  outputs (Home  work)
class   c1:
	def  __init__(self):
		print('constructor')
		del  self
	def  __del__(self):
		print('destructor') # print destructor infinite times
		b=c1() # creating object and constructor automatically
a=c1() # creating object and constructor automatically infinite times

#Ex-7
#  Find  outputs( Home  work)
class   c1:
	def  __del__(self):
		print('1st  destructor')
	def  __del__(self):
		print('2nd  destructor')
	def  __del__(self):
		print('3rd  destructor')
# End  of  the class
a = c1() # creating empty object when object is destroy 3rd  __del__ executed 

#Ex-8
#Find  outputs (Home  work)
class   c1:
	def   __init__(self):
		print('Object  is  created  at  address  :  ' , id(self))
	def   __del__(self):
		print(F'Object  at  address  {id(self)}  is  lost  ')
#end  of  the  class
c = b = a = c1()
del   a
print('Hello')
del   b
print('Hi')
del   c
print('Bye')
d = c1()
print('End')


#Ex-9
# Find  outputs(Home  work)
class c1:
    def __init__(self):
        print('Object  is  created  at  address  :  ' , id(self))
    def __del__(self):
        print(F'Object  at  address  {id(self)}  is  lost ')
#End of the class
list = [c1() , c1() ,c1()] # creating list of different objects and execute __init__  of constructor of every object
del list #  execute __del__  of destructor of every object when object is destroy


#Ex-10
# Find  outputs  (Home  work)
class   c1:
	def  __del__(self):
		print('destructor')
		return  25
a = c1() # createing empty object
print(a . __del__()) # call destructor explicitly and return 25
print('Hello') # Hello
del a # delete reference a and object also destroy
