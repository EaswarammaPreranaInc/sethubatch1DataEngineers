# Public  and  Private  members  demo  program
class  Test:
	def  __init__(self):
		self.x=10        #How  to  initialize  public  variable  'x'  to  10
		self.__y=20     #How  to  initialize  private  variable  'y'  to  20
	def  m1(self):
		print('m1  method')
		print(self.x)       #How  to  print   variable  'x'
		print(self.__y)       #How  to  print  private  variable  'y'
		self.__m2()#How  to  call    private  method   m2()
		print('Back to m1 method')
	def  __m2(self):
		print('__m2  method')
		print(self.x)              #How  to  print   variable  'x'
		print(self.__y)#How  to  print  private  variable   'y'
# End  of  the  class
t = Test()
print('Outside')
print(t.x)        #How  to  print  variable  'x'
#How  to  print   variable  'y'
print(t ._Test__y)
print(t .__dict__)
t.m1()#How  to  call  method  m1()
t._Test__m2()#How  to  call   method  m2()
#t .__m2()
print('End')
"""
Output:
Outside
10
20
{'x': 10, '_Test__y': 20}
m1  method
10
20
__m2  method
10
20
Back to m1 method
__m2  method
10
20
End
"""

#  Find  outputs
class  c1:
	def __init__(self):
		self.x=10         #How  to  initialize  public  variable  'x'  with  10
		self.__x=20       #How  to  initialize  private  variable  'x'  with  20
		self.__x__=30     #How  to  initialize  public  dunder  variable  'x'  with  30
	def  m1(self):
		print('public method')
	def  __m1(self):
		print('private method')
	def  __m1__(self):
		print('public Dunder method')
#  End  of  the  class
a = c1()
print(a.x)       #How  to  print   variable  'x'
print(a.__x__)   #How  to  print  public  dunder  variable  'x'
print(a._c1__x)  #How  to  print   private  variable  'x'
#print(a . __x)
a.m1()        #How  to  call  public  method  m1()
a.__m1__()        #How  to  call  public  dunder  method  m1()
a._c1__m1()              #How  to  call  private  method  m1()
#a . __m1()
"""
Output:
10
30
20
public method
public Dunder method
private method
"""


#Find  outputs
#Assume  that  addresses  of  objects   'a' , 'b' , 'c' , 'd'  and  'e'  are  1000 , 2000 , 3000 , 4000  and  5000  respectively

class   c1:
	def   __init__(self):
		print('Object  is  created  at  address  :  ' , id(self))
	def   __del__(self):
		print(F'Object  at  address  {id(self)}  is  lost')
# End    of    the    class
a = c1()
a = None
b = c1()
del    b
c = c1()
c = c1()
d = c1()
e = c1()
"""
Output:
Object  is  created  at  address  :   2791105194576
Object  at  address  2791105194576  is  lost
Object  is  created  at  address  :   2791108283280
Object  at  address  2791108283280  is  lost
Object  is  created  at  address  :   2791108283280
Object  is  created  at  address  :   2791105668992
Object  at  address  2791108283280  is  lost
Object  is  created  at  address  :   2791105669296
Object  is  created  at  address  :   2791105395120
Object  at  address  2791105668992  is  lost
Object  at  address  2791105669296  is  lost
Object  at  address  2791105395120  is  lost
"""

# Identify  Error (Home  work)
class   c1:
	def  __del__(self , x):
		print('destructor')
a = c1()
a . __del__(25)
"""
Output:
destructor
"""

# Find  outputs (Home  work)
class   c1:
	def  __del__(self):
			print('destructor')
			b = c1()
a = c1()
"""
Output:
destructor 
infinite loop
"""

# Find  outputs (Home  work)
class   c1:
	def  __init__(self):
		print('constructor')
		del  self
	def  __del__(self):
		print('destructor')
		b = c1()
a = c1()
"""
Output:
constructor
destructor
infinite loop
"""

#  Find  outputs( Home  work)
class   c1:
	def  __del__(self):
		print('1st  destructor')
	def  __del__(self):
		print('2nd  destructor')
	def  __del__(self):
		print('3rd  destructor')
# End  of  the  class
a = c1()
"""
Output:
3rd  destructor
"""

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
"""
Output:
Object  is  created  at  address  :   1882633563040
Hello
Hi
Object  at  address  1882633563040  is  lost
Bye
Object  is  created  at  address  :   1882636192336
End
Object  at  address  1882636192336  is  lost
"""

# Find  outputs(Home  work)
class  c1:
        def     __init__(self):
                print('Object  is  created  at  address  :  ' , id(self))
        def     __del__(self):
                print(F'Object  at  address  {id(self)}  is  lost ')
#End of the class
list = [c1() , c1() , c1()]
del  list
"""
Output:
Object  is  created  at  address  :   2258995538512
Object  is  created  at  address  :   2258998168144
Object  is  created  at  address  :   2258998168464
Object  at  address  2258998168464  is  lost
Object  at  address  2258998168144  is  lost
Object  at  address  2258995538512  is  lost
"""

# Find  outputs  (Home  work)
class   c1:
	def  __del__(self):
		print('destructor')
		return  25
a = c1()
print(a . __del__())
print('Hello')
del   a

"""
Output:
destructor
25
Hello
destructor
"""
