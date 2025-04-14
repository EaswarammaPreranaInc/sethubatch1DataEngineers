# Public  and  Private  members  demo  program
from time import sleep


class  Test:
    def  __init__(self):
        self.x=10
        self._y=20
        # How  to  initialize  public  variable  'x'  to  10
        # How  to  initialize  private  variable  'y'  to  20
    def  m1(self):
        print('m1  method')
        print(self.x)
        # How  to  print   variable  'x'
        print(self._y)
        # How  to  print  private  variable  'y'
        self.__m2()
        # How  to  call    private  method   m2()
        print('Back to m1 method')
    def  __m2(self):
        print('__m2  method')
        print(self.x)
        # How  to  print   variable  'x'
        print(self._y)
        # How  to  print  private  variable   'y'
# End  of  the  class
t = Test()
print('Outside')
print(t.x)
# How  to  print  variable  'x'
print(t._y)
# How  to  print   variable  'y'
print(t . __dict__)
t.m1()

# How  to  call  method  m1()
# How  to  call   method  m2()
t._Test__m2()
print('End')

#  Find  outputs
class  c1:
    def __init__(self):
        self.x=10
        self._x=20
        self.__x__=30

        # How  to  initialize  public  variable  'x'  with  10
        # How  to  initialize  private  variable  'x'  with  20
        # How  to  initialize  public  dunder  variable  'x'  with  30

    def  m1(self):
        print('public method')
    def  __m1(self):
        print('private method')
    def  __m1__(self):
        print('public Dunder method')
#  End  of  the  class
a = c1()
print(a.x)
print(a._x)
print(a.__x__)
# How  to  print   variable  'x'
# How  to  print  public  dunder  variable  'x'
# How  to  print   private  variable  'x'
# print(a . __x)
a.m1()
a.__m1__()
a._c1__m1()
# How  to  call  public  method  m1()
# How  to  call  public  dunder  method  m1()
# How  to  call  private  method  m1()
# a . __m1()

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
a = c1()
a = None
b = c1()
del    b
c = c1()
c = c1()
d = c1()
e = c1()
'''
a init
a del
b init
b del
c init
c init
c del
d init
e init
c del
d del
e del'''

# Identify  Error (Home  work)
class   c1:
	def  __del__(self , x):
		print('destructor')
a = c1()
a.__del__(25)
'''
destructor
error'''

# Find  outputs (Home  work)
class   c1:
	def  __del__(self):
			print('destructor')
			b = c1()
a = c1()
'''
Infinite destructor'''

# Find  outputs (Home  work)
class   c1:
	def  __init__(self):
		print('constructor')
		del  self
	def  __del__(self):
		print('destructor')
		b = c1()
a = c1()
'''
Infinite constructor following destrcutor'''

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
'''
latest one is executed 3rd destructor'''

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
'''
Object  is  created  at  address  :   2522530414080
Hello
Hi
Object  at  address  2522530414080  is  lost  
Bye
Object  is  created  at  address  :   2522533032208
End
Object  at  address  2522533032208  is  lost  '''

# Find  outputs(Home  work)
class  c1:
        def     __init__(self):
                print('Object  is  created  at  address  :  ' , id(self))
        def     __del__(self):
                print(F'Object  at  address  {id(self)}  is  lost ')
#End of the class
list = [c1() , c1() , c1()]
del  list
'''
it uses last in first out 
1 is created
2 is created
3 is created
3 is lost
1 is lost
2 is lost'''

# Find  outputs  (Home  work)
class   c1:
	def  __del__(self):
		print('destructor')
		return  25
a = c1()
print(a . __del__())
print('Hello')
del   a
'''
destructor
25
Hello
destructor'''
