# Find  outputs
import   sys
class   c1:
        pass
# End  of  the  class
a = b = c = d = c1() # One objct d and remaining a b c are ref 
print(sys . getrefcount(b)) # 5 (a,b,c,d and self)
print(sys . getrefcount(c1())) # 1 becoz of d
print(sys . getrefcount(25)) # immutable 25 so ref keep on changing
print(sys . getrefcount([10 , 20 , 15 , 18])) # 1 
print(sys . getrefcount(10.8)) # immutable 10.8 so ref keep on changing
print(sys . getrefcount({10 , 20 , 15 , 18})) # 1
print(sys . getrefcount('Hyd')) # Immutable Hyd so ref changing
print(sys . getrefcount({10 : 20 , 30 : 40})) # 1
print(sys . getrefcount((10 , 20 , 30 , 40))) # Immutable so ref keep changing

# Find  outputs  (Home  work)
import  sys
class  Test:
	def  __init__(self):
		print('Constructor  :  ' , id(self))
		return    None
	def  __del__(self):
		print('Destructor  :  ' , id(self))
		return  25
# End  of  the  class
t = Test() # Constructor is created at address may be 1000
print(t . __init__()) # Constructor is created at address may be 1000 and None is returned becoz of explicit call
print(sys . getrefcount(t)) # 2
print(t . __del__()) # Destructor is executed and remove address 1000 and 25 returned becoz of explicit call
print(sys . getrefcount(t)) # 2
print('Bye') # Bye
# Destructor is executed and remove address 1000

#  Gift
# Find  outputs (Home  work)
class  c1:
	def  __init__(self):
		print('Object  is    created')
	def  __del__(self):
		print('Object  is  lost')
#End  of  the  class
def    f1():
	print('Function  Begin')
	a  =  c1()
	print(a)
	print('Function  end')
	return   a
print('Program  Begin') # Program Begin
b = f1() # Function Begin <nxt line> Object is created <nxt line>  Type and address of a <nxt line> Function end
print(b) # Type and address of b
print('Program  End') # Program End
# Object is lost

#  Gift
# Find  outputs (Home  work)
class  c1:
	def  __init__(self):
		print('Object  is    created')
	def  __del__(self):
		print('Object  is  lost')
#End  of  the  class
def    f1():
        print('Function  begin')
        a  =  c1()
        print('Function  end')
        return   a
print('Program  Begin') # Program  Begin
f1() # Function Begin <nxt line> Object is created <nxt line> Function end <nxt line> Object  is  lost
print('Program  End') # Program  End
# Find  outputs (Home  work)
class  c1:
	def  __init__(self):
		print('Object  is    created')
	def  __del__(self):
		print('Object  is  lost')
#End  of  the  class
def    f1():
        print('Function  begin')
        a  =  c1()
        print('Function  end')
print('Program  Begin') # Program Begin
b = f1() # Function begin <nxt line> Object is created <nxt line> Function end <nxt line> Object is lost
print(b) # None
print('Program  End') # Program End

# Most  tricky  program
# Circular  reference (Home  work)
class   c1:
	def   __init__(self , k): # self = x.a and k = x
		print('c1  class  object  is  created')
		self . b = k # x.a.b = x
		print('End  of  c1  class constructor')
	def   __del__(self):
		print('c1  class  object  is  lost')
# End of class c1
class  c2:
	def  __init__(self): # self = x
		print('c2  class  object  is  created')
		self . a = c1(self) # x.a = c1(x)
		print('End  of  c2  class constructor')
	def  __del__(self):
		print('c2  class  object  is  lost')
#End of class c2
print('Program  begin') # Program  begin
x = c2() # c2  class  object  is  created <nxt line> c1  class  object  is  created <nxt line> End  of  c1  class constructor <nxt line> End  of  c2  class constructor
print('program end') # program end
# c2  class  object  is  lost
# c1  class  object  is  lost
# Find  outputs (Home  work)
class   c1:
	def  __del__(self): # self = a
		print('Destructor')
		global  b
		b = self # b = a
a = c1() 
del  a # Destructor 
print('Hello') # Hello
#(Home  work)
#  Can  string  be  enumerated ?
import   time
a = input('Enter  any  string  :  ')   #  Assume  that  input  is   HYD
e = enumerate(a) # empty object 
while   True:
	try:
		print(next(e)) # (0,H) <nl> (1,Y) <nl> (2,D) <nl> stopIterationError 
		time . sleep(1)
	except  StopIteration:
		break

# Can  dictionary  be  enumerated ?   (Home  work)
import   time
def  disp(e): # e = b , e = c , e = d , e = f
	while  True:
		try:
			print(next(e))
			time . sleep(1)
		except:
			break
	print()
a = {'Empno'  :  25 , 'Emp Name'  :  'Rama Rao' , 'Sal' : 10000.0}
b = enumerate(a . keys()) # Empty object
disp(b) # (0,Empno) <nl> (1,Emp Name) <nl> (2,Sal)
c = enumerate(a . values())
disp(c) # (0,25) <nl> (1,Rama Rao) <nl> (2,10000.0)
d = enumerate(a . items()) 
disp(d) # (0,(Empno,25)) <nl> (1,(Emp Name,Rama Rao)) <nl> (2,(Sal,10000.0))
f = enumerate(a , start = 5)
disp(f) # (5, 'Empno') <nl> (6, 'Emp Name') <nl> (7, 'Sal')
# Find  outputs  (Home  work)
import   time
a = ['Telangana' , 'Andhra  Pradesh' , 'Karnataka' , 'TamilNadu' , 'Maharastra']
b = ['Hyderabad' , 'Amaravathi' , 'Bangalore' , 'Chennai' , 'Mumbai']
c = enumerate(a)
for  index , element  in  c:
	print(F'{element:15}  ... {b[index]}')
	time . sleep(1)
'''o/p: Telangana        ... Hyderabad
        Andhra  Pradesh  ... Amaravathi
        Karnataka        ... Bangalore
        TamilNadu        ... Chennai
        Maharastra       ... Mumbai'''	
	