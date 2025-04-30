# Find  outputs
import   sys
class   c1:
        pass
a = b = c = d = c1()
print(sys . getrefcount(b))
print(sys . getrefcount(c1()))
print(sys . getrefcount(25))
print(sys . getrefcount([10 , 20 , 15 , 18]))
print(sys . getrefcount(10.8))
print(sys . getrefcount({10 , 20 , 15 , 18}))
print(sys . getrefcount('Hyd'))
print(sys . getrefcount({10 : 20 , 30 : 40}))
print(sys . getrefcount((10,20,30,40)))
'''
OUTPUT:
5
1
4294967295
1
3
1
3
1
3
'''
# Find  outputs  (Home  work)
import  sys
class  Test:
	def  __init__(self):
		print('Constructor  :  ' , id(self))
		return    None
	def  __del__(self):
		print('Destructor  :  ' , id(self))
		return  25
t = Test()
print(t . __init__())
print(sys . getrefcount(t))
print(t . __del__())
print(sys . getrefcount(t))
print('Bye')
'''
OUTPUT:
Constructor  :   2602714821504
Constructor  :   2602714821504
None
2
Destructor  :   2602714821504
25
2
Bye
Destructor  :   2602714821504
'''
# Find  outputs (Home  work)
class  c1:
	def  __init__(self):
		print('Object  is    created')
	def  __del__(self):
		print('Object  is  lost')
def    f1():
	print('Function  Begin')
	a  =  c1()
	print(a)
	print('Function  end')
	return   a
print('Program  Begin')
b = f1()
print(b)
print('Program  End')
'''
OUTPUT:
Program Begin
Function Begin
Object is created
Type and address of a
Function end 
Type and address
Program End 
object is lost
'''
#  Gift
# Find  outputs (Home  work)
class  c1:
	def  __init__(self):
		print('Object  is    created')
	def  __del__(self):
		print('Object  is  lost')
def    f1():
        print('Function  begin')
        a  =  c1()
        print('Function  end')
        return   a
print('Program  Begin')
f1()
print('Program  End')
'''
OUTPUT:
Program Begin
Function begin
Object is created 
Function end 
Object is lost 
Program End 
'''
# Find  outputs (Home  work)
class  c1:
	def  __init__(self):
		print('Object  is    created')
	def  __del__(self):
		print('Object  is  lost')
def    f1():
        print('Function  begin')
        a  =  c1()
        print('Function  end')
print('Program  Begin')
b = f1()
print(b)
print('Program  End')
'''
OUTPUT:
Program Begin
Function begin
Object is created 
Function end 
object is lost 
None
Program end
'''
# Most  tricky  program
# Circular  reference (Home  work)
class   c1:
	def   __init__(self , k):
		print('c1  class  object  is  created')
		self . b = k
		print('End  of  c1  class constructor')
	def   __del__(self):
		print('c1  class  object  is  lost')
class  c2:
	def  __init__(self):
		print('c2  class  object  is  created')
		self . a = c1(self)
		print('End  of  c2  class constructor')
	def  __del__(self):
		print('c2  class  object  is  lost')
print('Program  begin')
x = c2()
print('program end')
'''
OUTPUT:
Program begin
c2  class  object  is  created
c1  class  object  is  created
End  of  c1  class constructor
End  of  c2  class constructor
program end
c2  class  object  is  lost
c1  class  object  is  lost
'''
# Find  outputs (Home  work)
class   c1:
	def __del__(self):
		print('Destructor')
		global  b
		b = self
a = c1()
del  a
print('Hello')
'''
OUTPUT:
Destructor
Hello
'''
#(Home  work)
#  Can  string  be  enumerated ?
import   time
a = input('Enter  any  string  :  ')   #  Assume  that  input  is   HYD
e = enumerate(a)
while   True:
	try:
		print(next(e))
		time . sleep(1)
	except  StopIteration:
		break
'''
OUTPUT:
(0,'H')
(1,'Y')
(2,'D')
'''
# Can  dictionary  be  enumerated ?   (Home  work)
import   time
def  disp(e):
	while  True:
		try:
			print(next(e))
			time . sleep(1)
		except:
			break
	print()
a = {'Empno'  :  25 , 'Emp Name'  :  'Rama Rao' , 'Sal' : 10000.0}
b = enumerate(a . keys())
disp(b)
c = enumerate(a . values())
disp(c)
d = enumerate(a . items())
disp(d)
f = enumerate(a,start=5)
disp(f)
'''
OUTPUT:
(0,'Empno')
(1,'Emp Name')
(2,'Sal')
(0,25)
(1,'Rama Rao')
(2,10000.0)
(0,('Empno', 25))
(1,('Emp Name','Rama Rao'))
(2,('Sal',10000.0))
(5,'Empno')
(6,'Emp Name')
(7,'Sal')
'''
# Find  outputs  (Home  work)
import   time
a = ['Telangana' , 'Andhra  Pradesh' , 'Karnataka' , 'TamilNadu' , 'Maharastra']
b = ['Hyderabad' , 'Amaravathi' , 'Bangalore' , 'Chennai' , 'Mumbai']
c = enumerate(a)
for  index , element  in  c:
	print(F'{element:15}  ... {b[index]}')
	time.sleep(1)
'''
OUTPUT:
Telangana        ... Hyderabad
Andhra  Pradesh  ... Amaravathi
Karnataka        ... Bangalore
TamilNadu        ... Chennai
Maharastra       ... Mumbai
'''
