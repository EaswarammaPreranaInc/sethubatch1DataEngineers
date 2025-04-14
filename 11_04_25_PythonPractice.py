# Public  and  Private  members  demo  program
class  Test:
	def  __init__(self):
		self.x = 10 #How  to  initialize  public  variable  'x'  to  10
		self.__y = 20 #How  to  initialize  private  variable  'y'  to  20
	def  m1(self):
		print('m1  method')
		print(self.x) #How  to  print   variable  'x'
		print(self.__y)#How  to  print  private  variable  'y'
	    #self.__m2()	#How  to  call    private  method   m2()
		print('Back to m1 method')
	def  __m2(self):
		print('__m2  method')
		print(self.x)#How  to  print   variable  'x'
		print(self.__y)#How  to  print  private  variable   'y'
# End  of  the  class
t = Test()
print('Outside') # Outside
print(t.x)# 10 (How  to  print  variable  'x')
print(t._Test__y)# 20 (How  to  print   variable  'y')
#print(t . __y) # Error: 'Test' object has no attribute '__y'
print(t . __dict__) # {'x': 10, '_Test__y': 20}
t.m1()# m1 method <nxt line> 10 <nxt line> 20 <nxt line> Back to m1 method (How  to  call  method  m1())
t._Test__m2()# __m2 method <nxt line> 10 <nxt line> 20 <nxt line> End (How  to  call   method  m2())
#t . __m2() # Error: 'Test' object has no attribute '__m2'
print('End')
#  Find  outputs
class  c1:
	def __init__(self):
		self.x = 10 #How  to  initialize  public  variable  'x'  with  10
		self.__x = 20 #How  to  initialize  private  variable  'x'  with  20
		self.__x__ = 30 #How  to  initialize  public  dunder  variable  'x'  with  30
	def  m1(self):
		print('public method')
	def  __m1(self):
		print('private method')
	def  __m1__(self):
		print('public Dunder method')
#  End  of  the  class
a = c1()
print(a.x) #How  to  print   variable  'x'
print(a.__x__)#How  to  print  public  dunder  variable  'x'
print(a._c1__x)#How  to  print   private  variable  'x'
#print(a . __x) # Error: 'c1' object has no attribute '__x'
a.m1()#How  to  call  public  method  m1()
a.__m1__()#How  to  call  public  dunder  method  m1()
a._c1__m1()#How  to  call  private  method  m1()
#a . __m1() # Error: 'c1' object has no attribute '__m1'
'''o/p: 10
        30
        20
        public method
        public Dunder method
        private method'''

#Find  outputs
#Assume  that  addresses  of  objects   'a' , 'b' , 'c' , 'd'  and  'e'  are  1000 , 2000 , 3000 , 4000  and  5000  respectively

class   c1:
	def   __init__(self):
		print('Object  is  created  at  address  :  ' , id(self))
	def   __del__(self):
		print(F'Object  at  address  {id(self)}  is  lost')
# End    of    the    class
a = c1() # Objt is created at address 1000
a = None # Objt at address 1000 is lost
b = c1() # Objt is created at address 2000
del    b # Objct at address 2000 is lost
c = c1() # Objct is created at address 3000
c = c1() # Objct is created at address 4000 Objct at address 3000 is lost
d = c1() # Objct is created at address 5000
e = c1() # Objct is created at address 6000
# Identify  Error (Home  work)
class   c1:
	def  __del__(self , x):
		print('destructor') # destructor
a = c1()
a . __del__(25) # destructor is executed
# Find  outputs (Home  work)
class   c1:
	def  __del__(self):
			print('destructor') 
			b = c1() # Infinite execution of destructor
a = c1()
# Find  outputs (Home  work)
class   c1:
	def  __init__(self):
		print('constructor')
		del  self
	def  __del__(self):
		print('destructor')
		b = c1() # Infinite Mutual execution of the constructor and destructor
a = c1()
#  Find  outputs( Home  work)
class   c1:
	def  __del__(self):
		print('1st  destructor')
	def  __del__(self):
		print('2nd  destructor')
	def  __del__(self):
		print('3rd  destructor')
# End  of  the  class
a = c1() # 3rs destructor is executed
#Find  outputs (Home  work)
class   c1:
	def   __init__(self):
		print('Object  is  created  at  address  :  ' , id(self))
	def   __del__(self):
		print(F'Object  at  address  {id(self)}  is  lost  ')
#end  of  the  class
c = b = a = c1() # one class objct and two references
del   a # destructor is executed and ref a is lost
print('Hello') # Hello
del   b # destructor is executed and ref b is lost
print('Hi') # Hi
del   c # destructor is executed and ref b is lost
print('Bye') # Bye
d = c1() # new constructor d is created
print('End') # End
# destructor is executed and d is lost
# Find  outputs(Home  work)
class  c1:
        def     __init__(self):
                print('Object  is  created  at  address  :  ' , id(self))
        def     __del__(self):
                print(F'Object  at  address  {id(self)}  is  lost ')
#End of the class
list = [c1() , c1() , c1()]
del  list
'''o/p: Object  is  created  at  address  :   1897278761552
		Object  is  created  at  address  :   1897281522256
		Object  is  created  at  address  :   1897281522576
		Object  at  address  1897281522576  is  lost
		Object  at  address  1897281522256  is  lost
		Object  at  address  1897278761552  is  lost'''
# Find  outputs  (Home  work)
class   c1:
	def  __del__(self):
		print('destructor')
		return  25
a = c1() 
print(a . __del__()) # destructor <next line> 25
print('Hello') # Hello
del   a # destructor 



