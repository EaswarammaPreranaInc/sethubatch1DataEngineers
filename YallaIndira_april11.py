'''#Public  and  Private  members  demo  program
class  Test:
	def  __init__(self):
		self.x=10  #How  to  initialize  public  variable  'x'  to  10
		self.__y=20  #How  to  initialize  private  variable  'y'  to  20
	def  m1(self):
		print('m1  method')
		print(self.x) #How  to  print   variable  'x'
		print(self.__y) #How  to  print  private  variable  'y'
		self.__m2() #How  to  call    private  method   m2()
		print('Back to m1 method')
	def  __m2(self):
		print('__m2  method')
		print(self.x) #How  to  print   variable  'x'
		print(self.__y) #How  to  print  private  variable   'y'
# End  of  the  class
t = Test()
print('Outside')
print(t.x)  #How  to  print  variable  'x'
print(t._Test__y) #How  to  print   variable  'y'
#print(t . __y) # we can not cal directlly pravite instance variable it is not visible to outside class
print(t . __dict__)
t.m1()  #How  to  call  method  m1()
t._Test__m2() #How  to  call   method  m2()
#t . __m2()  # we can not cal directlly pravite method it is not visible to outside class
print('End')
'''

'''
#  Find  outputs
class  c1:
	def __init__(self):
		self.x=10  #How  to  initialize  public  variable  'x'  with  10
		self.__x=20  #How  to  initialize  private  variable  'x'  with  20
		self.__x__=30  #How  to  initialize  public  dunder  variable  'x'  with  30
	def  m1(self):
		print('public method')
	def  __m1(self):
		print('private method')
	def  __m1__(self):
		print('public Dunder method')
#  End  of  the  class
a = c1()
print(a.x) #How  to  print   variable  'x'
print(a._c1__x) #How  to  print  public  dunder  variable  'x'
print(a.__x__) #How  to  print   private  variable  'x'
#print(a . __x) # error
a.m1() #How  to  call  public  method  m1()
a.__m1__() #How  to  call  public  dunder  method  m1()
a._c1__m1() #How  to  call  private  method  m1()
#a . __m1() # error
'''


'''
Find  outputs
Assume  that  addresses  of  objects   'a' , 'b' , 'c' , 'd'  and  'e'  are  1000 , 2000 , 3000 , 4000  and  5000  respectively

class   c1:
	def   __init__(self):
		print('Object  is  created  at  address  :  ' , id(self))
	def   __del__(self):
		print(F'Object  at  address  {id(self)}  is  lost')
# End    of    the    class
a = c1() # Object  is  created  at  address  :  maybe 100000
a = None  
b = c1()
del    b
c = c1()
c = c1()
d = c1()
e = c1()

#outputs
Object  is  created  at  address  :   2246151269280
Object  at  address  2246151269280  is  lost
Object  is  created  at  address  :   2246154291792
Object  at  address  2246154291792  is  lost
Object  is  created  at  address  :   2246154291792
Object  is  created  at  address  :   2246151743360
Object  at  address  2246154291792  is  lost
Object  is  created  at  address  :   2246151743664
Object  is  created  at  address  :   2246151469488
Object  at  address  2246151743360  is  lost
Object  at  address  2246151743664  is  lost
Object  at  address  2246151469488  is  lost
'''

'''
# Identify  Error (Home  work)
class   c1:
	def  __del__(self , x):  # no arguments for destructor
		print('destructor')
a = c1()
a . __del__(25)
'''


'''
# Find  outputs (Home  work)
class   c1:
	def  __del__(self):
			print('destructor')
			b = c1()
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
#infinity times constructor and destructor will print
'''


'''
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

#output
3rd  destructor
'''

'''
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

#outputs
Object  is  created  at  address  :   2337665935952
Hello
Hi
Object  at  address  2337665935952  is  lost
Bye
Object  is  created  at  address  :   2337669089872
End
Object  at  address  2337669089872  is  lost
'''


'''
# Find  outputs(Home  work)
class  c1:
        def     __init__(self):
                print('Object  is  created  at  address  :  ' , id(self))
        def     __del__(self):
                print(F'Object  at  address  {id(self)}  is  lost ')
#End of the class
list = [c1() , c1() , c1()]
del  list
#output
Object  is  created  at  address  :   2247718955600
Object  is  created  at  address  :   2247722175056
Object  is  created  at  address  :   2247722175376
Object  at  address  2247722175376  is  lost
Object  at  address  2247722175056  is  lost
Object  at  address  2247718955600  is  lost
'''

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

#output
destructor
25
Hello
destructor
'''
