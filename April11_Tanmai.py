
# Public  and  Private  members  demo  program
class  Test:
	def  __init__(self):
		self.x=10
		self.__y=20
		#How  to  initialize  public  variable  'x'  to  10
		#How  to  initialize  private  variable  'y'  to  20
	def  m1(self):
		print('m1  method')
		print(self.x)
		print(self.__y)
		#How  to  print   variable  'x'
		#How  to  print  private  variable  'y'
		self.__m2()
		#How  to  call    private  method   m2()
		print('Back to m1 method')
	def  __m2(self):
		print('__m2  method')
		print(self.x)
		print(self.__y)
		#How  to  print   variable  'x'
		#How  to  print  private  variable   'y'
# End  of  the  class
t = Test()
print('Outside')
print(t.x)
print(t._Test__y)
#How  to  print  variable  'x'
#How  to  print   variable  'y'
#print(t . __y) # cant be used directly bcz its a private instance 
print(t . __dict__) # {x:10,'_Test.__y':20}
t.m1()
t._Test__m2()
#How  to  call  method  m1()
#How  to  call   method  m2()
#t . __m2()
print('End') 

#  Find  outputs
class  c1:
	def __init__(self):
		self.x=10
		self.__x=20
		self.__x__=30
		#How  to  initialize  public  variable  'x'  with  10
		#How  to  initialize  private  variable  'x'  with  20
		#How  to  initialize  public  dunder  variable  'x'  with  30
	def  m1(self):
		print('public method')
	def  __m1(self):
		print('private method')
	def  _m1_(self):
		print('public Dunder method')
#  End  of  the  class
a = c1()
a.x=10
a.__x__=30
print(a.x)
print(a._c1__x)
print(a.__x__)


#How  to  print   variable  'x'
#How  to  print  public  dunder  variable  'x'
#How  to  print   private  variable  'x'
#print(a . __x) # no such variable 
a.m1()
a._m1_()
a._c1__m1()
#How  to  call  public  method  m1()
#How  to  call  public  dunder  method  m1()
#How  to  call  private  method  m1()
#a . __m1() cant access directly 

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
a = c1() # when object is created constructor is executed Object  is  created  at  address  :  
a = None # reference is modified destructor executed and object is lost 
b = c1() # object .. 
del    b # ref b deleted 
c = c1() # object .
c = c1()
d = c1()
e = c1() 

# Identify  Error (Home  work)
class   c1:
	def  __del__(self , x):
		print('destructor')
a = c1() #
a . __del__(25) # deelted the ref destructor executed  

# Find  outputs (Home  work)
class   c1:
	def  __del__(self):
			print('destructor')
			b = c1() # destructor infinte times dont create object inside destructor 
a = c1() # destructor

# Find  outputs (Home  work)
class   c1:
	def  __init__(self):
		print('constructor')
		del  self # ref is deleted .. desrtructor executed 
	def  __del__(self):
		print('destructor')
		b = c1()  # object created before lossing object destructor executed infinte destructors 
a = c1()  # object created constructor executed ..
'''
constructor 
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
a = c1() # 3rd destructor 
 
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
Object  is  created  at  address  :   3145085774752
Hello
Hi
Object  at  address  3145085774752  is  lost
Bye
Object  is  created  at  address  :   3145091811920
End
Object  at  address  3145091811920  is  lost'''  


# Find  outputs(Home  work)
class  c1:
        def     __init__(self):
                print('Object  is  created  at  address  :  ' , id(self))
        def     __del__(self):
                print(F'Object  at  address  {id(self)}  is  lost ')
#End of the class
list = [c1(),c1(),c1()] 
del list
'''
Object  is  created  at  address  :   2164140042832
Object  is  created  at  address  :   2164142869072
Object  is  created  at  address  :   2164142869392
Object  at  address  2164142869392  is  lost
Object  at  address  2164142869072  is  lost
Object  at  address  2164140042832  is  lost '''

# Find  outputs  (Home  work)
class   c1:
	def  __del__(self):
		print('destructor') #  
		return  25
a = c1() 
print(a . __del__()) # executed destructor 25  object is not distrubed ..
print('Hello') # Hello 
del   a # destructor  
