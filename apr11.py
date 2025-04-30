'''
# Public  and  Private  members  demo  program
class  Test:
	def  __init__(self):
		self.x=10            #How  to  initialize  public  variable  'x'  to  10
		self.__y=20 #How  to  initialize  private  variable  'y'  to  20
	def  m1(self):
		print('m1  method')
		print(self.x) #How  to  print   variable  'x'
		print(self._Test__y) #How  to  print  private  variable  'y'
		self._Test__m2()  #How  to  call    private  method   m2()
		print('Back to m1 method')
	def  __m2(self):
		print('__m2  method')
		print(self.x)#How  to  print   variable  'x'
		print(self._Test__y) #How  to  print  private  variable   'y'
# End  of  the  class
t = Test()
print('Outside')
print(t.x)#How  to  print  variable  'x'
print(t._Test__y) #How  to  print   variable  'y'
#print(t . __y)
print(t . __dict__)
t.m1() #How  to  call  method  m1()
t._Test__m2()#How  to  call   method  m2()
#t . __m2()
print('End')
'''
'''
class  c1:
	def __init__(self):
		self.x=10 #ow  to  initialize  public  variable  'x'  with  10
		self.__x=20 #How  to  initialize  private  variable  'x'  with  20
		self.__x__=30 #How  to  initialize  public  dunder  variable  'x'  with  30
	def  m1(self):
		print('public method')
	def  __m1(self):
		print('private method')
	def  _m1_(self):
		print('public Dunder method')
#  End  of  the  class
a = c1()
print(a.x)#How  to  print   variable  'x'
print(a.__x__)#How  to  print  public  dunder  variable  'x'
print(a._c1__x)#How  to  print   private  variable  'x'
#print(a . __x)
a.m1() #How  to  call  public  method  m1()
a._m1_() #How  to  call  public  dunder  method  m1()
a._c1__m1()#How  to  call  private  method  m1()
#a . __m1()
#output
10
30
20
public method
public Dunder method
private method
'''
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
#output
Object  is  created  at  address  :   2101694717712
Object  at  address  2101694717712  is  lost
Object  is  created  at  address  :   2101694717712
Object  at  address  2101694717712  is  lost
Object  is  created  at  address  :   2101694717712
Object  is  created  at  address  :   2101694717952
Object  at  address  2101694717712  is  lost
Object  is  created  at  address  :   2101694717712
Object  is  created  at  address  :   2101694718000
Object  at  address  2101694717952  is  lost
Object  at  address  2101694717712  is  lost
Object  at  address  2101694718000  is  lost
'''
'''
# Identify  Error (Home  work)
class   c1:
	def __init__(self):
		print("constructor")
	def  __del__(self  ):
		print('destructor')
a = c1()
#a . __del__()
'''
'''
# Find  outputs (Home  work)
class   c1:
	def  __del__(self):
			print('destructor')
			#b = c1() #getting infinite loop
a = c1()
'''
'''
# Find  outputs (Home  work)
class   c1:
	def  __init__(self):
		print('constructor')
		del  self
	def  __del__(self):
		print('destructor')
		b = c1()
a = c1()
#output 
infinite loop becz its calling the c1() in c1().
'''
'''
class   c1:
	def   _init_(self):
		print('Object  is  created  at  address  :  ' , id(self))
	def   _del_(self):
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
# output
Hello
Hi
Bye
End
'''
'''
class  c1:
        def     __init__(self):
                print('Object  is  created  at  address  :  ' , id(self))
        def     __del__(self):
                print(F'Object  at  address  {id(self)}  is  lost ')
#End of the class
list = [c1() , c1() , c1()]
del  list
#output
Object  is  created  at  address  :   2226048229040
Object  is  created  at  address  :   2226048229280
Object  is  created  at  address  :   2226048229328
Object  at  address  2226048229328  is  lost
Object  at  address  2226048229280  is  lost
Object  at  address  2226048229040  is  lost
'''
# Find  outputs  (Home  work)
class   c1:
	def  __del__(self):
		print('destructor')
		return  25
a = c1()
print(a . __del__())
print('Hello')
del   a







































































