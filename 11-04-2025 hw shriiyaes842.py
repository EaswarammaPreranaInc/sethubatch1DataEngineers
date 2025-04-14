
#1)
# Public  and  Private  members  demo  program
class  Test:
	def  __init__(self):
		self.x=10
		self.__y=20
	def  m1(self):
		print('m1  method')
		print(t.x)
		print(t._Test__y)
		t._Test__m2()
		print('Back to m1 method')
	def  __m2(self):
		print('__m2  method')
		print(t.x)
		print(t._Test__y)
# End  of  the  class
t = Test()
print('Outside')
print(t.x)
print(t._Test__y)
#print(t .__y)
print(t . __dict__)
t.m1()
t._Test__m2()
#t . __m2()
print('End')

'''
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
'''
#________________________________________________

#2)
#  Find  outputs
class  c1:
	def __init__(self):
		self.x=10 #How  to  initialize  public  variable  'x'  with  10
		self.__x=20 #How  to  initialize  private  variable  'x'  with  20
		self.__x__=30 #How  to  initialize  public  dunder  variable  'x'  with  30
	def  m1(self):
		print('public method')
	def  __m1(self):
		print('private method')
	def  __m1__(self):
		print('public Dunder method')
#  End  of  the  class
a = c1()
print(a.x) #How  to  print   variable  'x'
print(a.__x__) #How  to  print  public  dunder  variable  'x'
print(a._c1__x) #How  to  print   private  variable  'x'
#print(a . __x)
a.m1() #How  to  call  public  method  m1()
a.__m1__() #How  to  call  public  dunder  method  m1()
a._c1__m1() #How  to  call  private  method  m1()
#a .__m1()

#_________________________________
#3)
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

"""
Object  is  created  at  address  :   4378602400
Object  at  address  4378602400  is  lost
Object  is  created  at  address  :   4379872144
Object  at  address  4379872144  is  lost
Object  is  created  at  address  :   4379872144
Object  is  created  at  address  :   4379059488
Object  at  address  4379872144  is  lost
Object  is  created  at  address  :   4379059792
Object  is  created  at  address  :   4378800304
Object  at  address  4379059488  is  lost
Object  at  address  4379059792  is  lost
Object  at  address  4378800304  is  lost
"""
#___________________________________________________________
#4)
# Identify  Error (Home  work)
class   c1:
	def  __del__(self,x):
		print('destructor')
a = c1()
a . __del__(25)#c1.__del__() missing 1 required positional argument: 'x'

#___________________________________________________________

#5)
# Find  outputs (Home  work)
class   c1:
	def  __del__(self):
			print('destructor')
			b = c1()
a = c1() #infinite
#____________________________________________________________

#6)
# Find  outputs (Home  work)
class   c1:
	def  __init__(self):
		print('constructor')
		del  self
	def  __del__(self):
		print('destructor')
		b = c1()
a = c1()#infinate loop

#______________________________________________________________

#7)
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
3rd  destructor
"""

#______________________________________________________________

#8
#Find  outputs (Home  work)
class   c1:
	def   __init__(self):
		print('Object  is  created  at  address  :  ' , id(self))
	def   __del__(self):
		print(F'Object  at  address  {id(self)}  is  lost  ')
#end  of  the  class
c = b = a = c1()
print()
del   a
print('Hello')
del   b
print('Hi')
del   c
print('Bye')
d = c1()
print('End')



"""
Object  is  created  at  address  :   4366444800

Hello
Hi
Object  at  address  4366444800  is  lost  
Bye
Object  is  created  at  address  :   4368075344
End
Object  at  address  4368075344  is  lost 
"""
#______________________________________________________________

#9)
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
Object  is  created  at  address  :   4333742336
Object  is  created  at  address  :   4335716944
Object  is  created  at  address  :   4335717264
Object  at  address  4335717264  is  lost 
Object  at  address  4335716944  is  lost 
Object  at  address  4333742336  is  lost 
"""

#______________________________________________________________

#10)
# Find  outputs  (Home  work)
class   c1:
	def  __del__(self):
		print('destructor')
		return  25
a = c1()
#print(a . _del_())
print('Hello')
del   a

"""
Hello
destructor
"""

