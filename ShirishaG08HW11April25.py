#Public and Private members demo program
class Test:
	def __init__(self):
		self.x=10 #How  to  initialize  public  variable  'x'  to  10
		self.__y=20 #How  to  initialize  private  variable  'y'  to  20
	def m1(self):
		print('m1 method')
		print(self.x) #How  to  print   variable  'x'
		print(self.__y) #How  to  print  private  variable  'y'
		self.__m2() #How  to  call    private  method   m2()
		print('Back to m1 method')
	def __m2(self):
		print('__m2 method')
		print(self.x) #How  to  print   variable  'x'
		print(self.__y) #How  to  print  private  variable   'y'
#End of the class
t = Test()
print('Outside') #Outside
print(t.x) #How  to  print  variable  'x'
print(t._Test__y) #How  to  print   variable  'y'
#print(t.__y) #Error
print(t.__dict__) #{x:10,'_Test__y':20}
t.m1() #How  to  call  method  m1()
t._Test__m2() #How  to  call   method  m2()
t.__m2() #Error
print('End') #End



#Find outputs
class c1:
	def __init__(self):
		self.x=10 #How to initialize public variable 'x' with 10
		self.__x=20 #How to initialize private variable 'x' with 20
		global __x__ #How to intialize public dunder variable 'x'
		__x__ = 30
	def m1(self):
		print('public method')
	def __m1(self):
		print('Private method')
	def __m1__(self):
		print('public dunder method')
#End of the class
a=c1() 
print(a.x) #How to print public variable x
print(__x__) #How to print public dunder variable x
print(a._c1__x) #How to print private variable 'x'
print(a.__x) #Error
a.m1() #How to call public m1() method
a.__m1__() #How to call public dunder method
a._c1__m1() #How to call private method m1()
a.__m1() #Error



#Find outputs
#Assume addresses of objects 'a','b','c','d' and 'e' are 1000,2000,3000,4000,5000 respectively
class c1:
	def __init__(self):
		print('Object is created at address : ',id(self))
	def __del__(self):
		print(F'Object at address {id(self)} is lost')
#End of class
a=c1() #Object is created at address : 1000
a=None #Object at address 1000 is lost
b=c1() #Object is created at address : 2000
del b  #Object at address 2000 is lost
c=c1() #Object is created at address : 3000
c=c1() #Object is created at address : 3000
       #Object at address 3000 is lost
d=c1() #Object is created at address : 4000
e=c1() #Object is created at address : 5000
#Object at address 3000 is lost
#Object at address 4000 is lost
#Object at address 5000 is lost



#Iddentify error
class c1:
	def __del__(self,x): #destructor cannot take arguments except self
		print('destructor')
a=c1()
a.__del__(25) #destructor cannot take arguments



#Find outputs
class c1:
	def __del__(self):
		print('destructor') #destructor printed infinite times
		b=c1() #call destructor every time 'b' is about to be lost
a=c1()



#Find outputs
class c1:
	def __init__(self):
		print('Constructor')
		del self
	def __del__(self): 
		print('destructor')
		b=c1()
a=c1()

#Output
Constructor
Destructor #object 'b' is created for class c1
Constructor 
Destructor #object 'b' is created for class c1
Constructor 
Destructor #object 'b' is created for class c1
.
.
.
so on (infinite times)



#Find outputs
class c1:
	def __del__(self):
		print('1st destructor')
		del self
	def __del__(self): 
		print('2nd destructor')
	def __del__(self):
		print('3rd destructor')
a=c1() #3rd destructor



#Find outputs
class c1:
	def __init__(self):
		print('Object is created at address : ',id(self))
	def __del__(self):
		print(F'Object at address {id(self)} is lost')
#End of class
c=b=a=c1()
del a
print('Hello')
del b
print('Hi')
del c
print('Bye')
d=c1()
print('End')

#Output
Object is created at address :  2130249282192
Hello
Hi
Object at address 2130249282192 is lost
Bye
Object is created at address :  2130249282192
End
Object at address 2130249282192 is lost



#Find outputs
class c1:
	def __init__(self):
		print('Object is created at address : ',id(self))
	def __del__(self):
		print(F'Object at address {id(self)} is lost')
#End of class
list=[c1(),c1(),c1()]
del list

#Output
Object is created at address :  2151419244672
Object is created at address :  2151419244912
Object is created at address :  2151419244960
Object at address 2151419244960 is lost
Object at address 2151419244912 is lost
Object at address 2151419244672 is lost



#Find outputs
class c1:
	def __del__(self):
		print('Destructor')
		return 25
a=c1()
print(a.__del__())
print('Hello')
del a

#Output
Destructor
25
Hello
Destructor
