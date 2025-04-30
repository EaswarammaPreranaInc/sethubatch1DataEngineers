'''
1#) Public  and  Private  members  demo  program
class  Test:
	def  __init__(self):
		self.x = 10 # How  to  initialize  public  variable  'x'  to  10
		self. __y = 20 # How  to  initialize  private  variable  'y'  to  20
	def  m1(self):
		print('m1  method') #------> m1  method
		print( 'x:' , self.x) # How  to  print   variable  'x'------> x : 10
		print('y:' , self.__y) # How  to  print  private  variable  'y'------> y : 20
		self.__m2() # How  to  call    private  method   m2()-----> __m2 method
		print('Back to m1 method') # ------> Back to m1 method
	def  __m2(self):
		print('__m2  method') # ------> __m2 method  
		print('x:' , self.x) # How  to  print   variable  'x'----->after m2() call ----> x : 10
		print('y:' , self. __y) #How  to  print  private  variable   'y' -----> y: 20
# End  of  the  class
t = Test()
print('Outside') # Outside
print('x:' , t.x) # How  to  print  variable  'x'-----> x: 10
print('y:' , t._Test__y) # How  to  print   variable  'y'-----> y: 20
#print(t . __y)   # Error : Again, this would raise an AttributeError
print(t . __dict__) # ------> {'x': 10, '_Test__y': 20}
t.m1() # How  to  call  method  m1()
t._Test__m2() # How  to  call   method  m2()
#t . __m2() # Error we cannot call without Test here . 
print('End') # End.

output:-
--------
Outside
x: 10
y: 20
{'x': 10, '_Test__y': 20}
m1  method
x: 10
y: 20
__m2  method
x: 10
y: 20
Back to m1 method
__m2  method
x: 10
y: 20
End


#2) Find  outputs
class  c1:
	def __init__(self):
		self . x = 10 # How  to  initialize  public  variable  'x'  with  10
		self . __x = 20 # How  to  initialize  private  variable  'x'  with  20
		self. __x__ = 30 # How  to  initialize  public  dunder  variable  'x'  with  30
	def  m1(self):
		print('public method')
	def  __m1(self):
		print('private method')
	def  __m1__(self):
		print('public Dunder method')
#  End  of  the  class
a = c1()
print('x:' , a.x) # How  to  print   variable  'x'
print('x:' , a.__x__) # How  to  print  public  dunder  variable  'x'
print('x:' , a._c1__x) #How  to  print   private  variable  'x'
#print(a . __x) # This will raise AttributeError (uncomment to test failure)
a. m1() # How  to  call  public  method  m1()
a .__m1__() # How  to  call  public  dunder  method  m1()
a._c1__m1() #How  to  call  private  method  m1()
#a . __m1() # This would raise AttributeError

output:-
--------------
x: 10
x: 30
x: 20
public method
public Dunder method
private method


#3)Find  outputs
Assume  that  addresses  of  objects   'a' , 'b' , 'c' , 'd'  and  'e'  are  1000 , 2000 , 3000 , 4000  and  5000  respectively

class   c1:
	def   __init__(self):
		print('Object  is  created  at  address  :  ' , id(self))
	def   __del__(self):
		print(F'Object  at  address  {id(self)}  is  lost')
# End    of    the    class
a = c1() # object 'a' is created 
a = None # object 'a' is lost due to reference points to new object
b = c1() # object 'b' is created
del   b # object 'b' is deleted
c = c1() # object 'c' is created
c = c1() # object 'c' is lost and refernce points to object 'c1 ' is created
d = c1()  # object 'd' is created 
e = c1()  # object 'e' is created

output:-
-----------
Object  is  created  at  address  :   1717339843152
Object  at  address  1717339843152  is  lost
Object  is  created  at  address  :   1717342473104
Object  at  address  1717342473104  is  lost
Object  is  created  at  address  :   1717342473104
Object  is  created  at  address  :   1717340317568
Object  at  address  1717342473104  is  lost
Object  is  created  at  address  :   1717340317872
Object  is  created  at  address  :   1717340043696
Object  at  address  1717340317568  is  lost
Object  at  address  1717340317872  is  lost
Object  at  address  1717340043696  is  lost


#4)Identify  Error (Home  work)
class   c1:
	def  __del__(self , x):
		print('destructor')
a = c1()
a . __del__(25) # deletes x value.

output:-
-----------
destructor
Exception ignored in: <function c1.__del__ at 0x000001E17167F060>
TypeError: c1.__del__() missing 1 required positional argument: 'x'


#5) Find  outputs (Home  work)
class   c1:
	def  __del__(self):
			print('destructor') # infinite time destructor creates here ------> everytime new destructor is creating
			b = c1() # destructor
a = c1() destructor

output:-
----------
destructor
destructor
destructor
destructor
destructor
destructor
 .
 .
 .
 .

infinite destructor created line by line here.


#6)Find  outputs (Home  work)
class   c1:
	def  __init__(self):
		print('constructor')
		del  self
	def  __del__(self):
		print('destructor')
		b = c1()
a = c1()

outputs:-
-------
destructor
constructor
destructor
constructor
destructor
constructor
destructor
constructo
destructor
    .
	.
	.
infinite times we get constructor and destructor


#7) Find  outputs( Home  work)
class   c1:
	def  __del__(self):
		print('1st  destructor') # ignored
	def  __del__(self):
		print('2nd  destructor') # ignored
	def  __del__(self):
		print('3rd  destructor') # recognised 
# End  of  the  class
a = c1()

output:-
---------
3rd  destructor


#8)Find  outputs (Home  work)
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

output:-
-----------
Object  is  created  at  address  :   2492679875488
Hello
Hi
Object  at  address  2492679875488  is  lost
Bye
Object  is  created  at  address  :   2492683160144
End
Object  at  address  2492683160144  is  lost


#9)Find  outputs(Home  work)
class  c1:
        def     __init__(self):
                print('Object  is  created  at  address  :  ' , id(self))
        def     __del__(self):
                print(F'Object  at  address  {id(self)}  is  lost ')
#End of the class
list = [c1() , c1() , c1()] # # list object created
del  list # list object lost


output:-
----------
Object  is  created  at  address  :   1622497585744
Object  is  created  at  address  :   1622500870736
Object  is  created  at  address  :   1622500871056
Object  at  address  1622500871056  is  lost
Object  at  address  1622500870736  is  lost
Object  at  address  1622497585744  is  lost


'''
#10)Find  outputs  (Home  work)
class   c1:
	def  __del__(self):
		print('destructor')
		return  25
a = c1()
print(a . __del__())
print('Hello')
del   a


