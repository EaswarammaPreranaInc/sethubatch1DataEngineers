Q1 #Public  and  Private  members  demo  program
class  Test:
	def  __init__(self):
		self.x=10       #How  to  initialize  public  variable  'x'  to  10
		self.__y=20     #How  to  initialize  private  variable  'y'  to  20
	def  m1(self):
		print('m1  method')
		print(self.x)           #How  to  print   variable  'x'
		print(self._Test__y)    #How  to  print  private  variable  'y'
		self._Test__m2()        #How  to  call    private  method   m2()
		print('Back to m1 method')
	def  __m2(self):
		print('__m2  method')
		print(self.x)           #How  to  print   variable  'x'
		print(self._Test__y)     #How  to  print  private  variable   'y'
# End  of  the  class
t = Test()
print('Outside')
print(t.x)     #How  to  print  variable  'x'
print(t._Test__y)     #How  to  print   variable  'y'
#print(t . __y)  #error - y is private instance variable. cannot access ouside of the class
print(t . __dict__)
t.m1()       #How  to  call  method  m1()
t._Test__m2() #How  to  call   method  m2() 
#t . __m2()     #error -  __m2() is private and cannot accesses outside the class
print('End')

OP-
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
#---------------------------------------------------------------------------------
Q2 #Find  outputs

class  c1:
	def __init__(self):
		self.x=10                #How  to  initialize  public  variable  'x'  with  10
		self.__y=20              #How  to  initialize  private  variable  'x'  with  20
		self.__x__=30            #How  to  initialize  public  dunder  variable  'x'  with  30
	def  m1(self):
		print('public method')
	def  __m1(self):
		print('private method')
	def  __m1__(self):
		print('public Dunder method')
#  End  of  the  class
a = c1()
print(a.x)      #How  to  print   variable  'x'
print(a.__x__)  #How  to  print  public  dunder  variable  'x'
print(a._c1__y) #How  to  print   private  variable  'x'
#print(a . __x)  #error - no __x in the program
a.m1()          #How  to  call  public  method  m1()
a.__m1__()      #How  to  call  public  dunder  method  m1()
a._c1__m1()     #How  to  call  private  method  m1()
#a . __m1()      #error - __m1 is private and cannot access outside the class 

OP-
10
30
20
public method
public Dunder method
private method
#----------------------------------------------------------------------------------------------------
Q3 #Find  outputs. Assume  that  addresses  of  objects   'a' , 'b' , 'c' , 'd'  and  'e'  are  1000 , 2000 , 3000 , 4000  and  5000  respectively

class   c1:
	def   __init__(self):
		print('Object  is  created  at  address  :  ' , id(self))
	def   __del__(self):
		print(F'Object  at  address  {id(self)}  is  lost')
# End    of    the    class
a = c1()   #Object  is  created  at  address  :   1000
a = None   #Object  at  address  1000  is  lost
b = c1()   #Object  is  created  at  address  :   2000
del    b   #Object  at  address  2000  is  lost
c = c1()   #Object  is  created  at  address  :   2000
c = c1()   #Object  is  created  at  address  :   3000
           #Object  at  address  2000  is  lost
d = c1()   #Object  is  created  at  address  :   4000
e = c1()   #Object  is  created  at  address  :   5000
           #Object  at  address  3000  is  lost
		   #Object  at  address  4000  is  lost
		   #Object  at  address  5000  is  lost
#----------------------------------------------------------------------------------------------
Q4 #Identify  Error (Home  work)
class   c1:
	def  __del__(self , x): #destructor cannot take arguments except self
		print('destructor')
a = c1()
a . __del__(25)  #destructor
#------------------------------------------------------------------------------------
Q5 #Find  outputs (Home  work)
class   c1:
	def  __del__(self):
			print('destructor')
			b = c1()
a = c1()  #prints destructor infinite times due to object creation inside __del__  

#_----------------------------------------------------------------------------
Q6 #Find  outputs (Home  work)
class   c1:
	def  __init__(self):
		print('constructor')
		del  self
	def  __del__(self):
		print('destructor')
		b = c1()
a = c1()  #prints constructor destructor infinite times due to object creation inside __del__ 
#----------------------------------------------------------------------------
Q7 #Find  outputs( Home  work)
class   c1:
	def  __del__(self):
		print('1st  destructor')
	def  __del__(self):
		print('2nd  destructor')
	def  __del__(self):
		print('3rd  destructor')
# End  of  the  class
a = c1() #3rd destructor
#-------------------------------------------------------------------------
Q8 #Find  outputs (Home  work)
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

OP-
Object  is  created  at  address  :   2494005734304
Hello
Hi
Object  at  address  2494005734304  is  lost
Bye
Object  is  created  at  address  :   2494009018960
End
Object  at  address  2494009018960  is  lost
#-----------------------------------------------------------------------------
Q9 #Find  outputs(Home  work)
class  c1:
        def     __init__(self):
                print('Object  is  created  at  address  :  ' , id(self))
        def     __del__(self):
                print(F'Object  at  address  {id(self)}  is  lost ')
#End of the class
list = [c1() , c1() , c1()]
del  list

OP-
Object  is  created  at  address  :   2061009644112
Object  is  created  at  address  :   2061013060176
Object  is  created  at  address  :   2061013060496
Object  at  address  2061013060496  is  lost
Object  at  address  2061013060176  is  lost
Object  at  address  2061009644112  is  lost
#-------------------------------------------------------------------------------
Q10 #Find  outputs  (Home  work)
class   c1:
	def  _del_(self):
		print('destructor')
		return  25
a = c1()
print(a . _del_())
print('Hello')
del   a

OP-
destructor
25
Hello