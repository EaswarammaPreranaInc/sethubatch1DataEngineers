#Find outputs
import sys
class c1:
	pass
#End of the class
a=b=c=d=c1()
print(sys.getrefcount(b)) #5
print(sys.getrefcount(c1())) #1
print(sys.getrefcount(25)) #Error : immutable object
print(sys.getrefcount([10,20,15,18])) #1
print(sys.getrefcount(10.8)) #Error : immutable object
print(sys.getrefcount({10,20,15,18})) #1
print(sys.getrefcount('Hyd')) #1
print(sys.getrefcount({10:20, 30:40})) #1
print(sys.getrefcount((10,20,30,40))) #1



#Find outputs
import sys
class Test:
	def __init__(self):
		print('Constructor :',id(self))
		return None
	def __del__(self):
		print('Destructor :',id(self))
		return 25
#End of the class
t=Test()
print(t.__init__())
print(sys.getrefcount(t))
print(t.__del__())
print(sys.getrefcount(t))
print('Bye')

#Output
Constructor : some address
Constructor : some address
None
2
Destructor : some address
25
2
Bye
Destructor : some address



#Gift
#Find outputs
class c1:
	def __init__(self):
		print('Object is created')
	def __del__(self):
		print('Object is lost')
#End of the class
def f1():
	print('Function Begin')
	a=c1()
	print(a)
	print('Function end')
	return a
print('Program Begin')
b=f1()
print(b)
print('Program End')

#Output
Program Begin
Function Begin
Object is created
<__main__.c1 object at some address>

Function end
<__main__.c1 object at some address>
Program End
Object is lost



#Gift
#Find outputs
class c1:
	def __init__(self):
		print('Object is created')
	def __del__(self):
		print('Object is lost')
#End of the class
def f1():
	print('Function begin')
	a=c1()
	print('Function end')
	return a
print('Program Begin')
f1()
print('Program End')

#Output
Program Begin
Function begin
Object is created
Function end
Object is lost
Program End



#Find outputs
class c1:
	def __init__(self):
		print('Object is created')
	def __del__(self):
		print('Object is lost')
#End of the class
def f1():
	print('Function begin')
	a=c1()
	print('Function end')
print('Program Begin')
b=f1()
print(b)
print('Program End')

#Output
Program Begin
Function begin
Object is created
Function end
Object is lost
None
Program End



#Most tricky program
#Circular reference
class c1:
	def __init__(self , k):
		print('c1 class object is created')
		self.b=k
		print('End of c1 class constructor')
	def __del__(self):
		print('c1 class object is lost')
#End of class c1
class c2:
	def __init__(self):
		print('c2 class object is created')
		self.a=c1(self)
		print('End of c2 class constructor')
	def __del__(self):
		print('c2 class object is lost')
#End of class c2
print('Program begin')
x=c2()
print('program end')

#Output
Program begin
c2 class object is created
c1 class object is created
End of c1 class constructor
End of c2 class constructor
program end
c2 class object is lost
c1 class object is lost




#Find outputs
class c1:
	def __del__(self):
		print('Destructor')
		global b
		b=self
a=c1()
del a
print('Hello')

#Output
Destructor
Hello



#(Home  work)
#Can string be enumerated ?
import time
a=input('Enter any string : ')   #Assume that input is HYD
e=enumerate(a)
while True:
	try:
		print(next(e))
		time.sleep(1)
	except StopIteration:
		break

#Output
HYD
(0,'H')
(1,'Y')
(2,'D')



#Can dictionary be enumerated?
import time
def disp(e):
	while True:
		try:
			print(next(e))
			time.sleep(1)
		except:
			break
	print()
a={'Empno':25,'Emp Name':'Rama Rao','Sal':10000.0}
b=enumerate(a.keys())
disp(b)
c=enumerate(a.values())
disp(c)
d=enumerate(a.items())
disp(d)
f=enumerate(a,start=5)
disp(f)

#output
(0,'Empno')
(1,'Emp Name')
(2,'Sal')
<empty line>
(0,25)
(1,'Rama Rao')
(2,10000.0)
<empty line>
(0, ('Empno', 25))
(1, ('Emp Name', 'Rama Rao'))
(2, ('Sal', 10000.0))
<empty line>
(5, 'Empno')
(6, 'Emp Name')
(7, 'Sal')
<empty line>



#Find outputs 
import time
a=['Telangana','Andhra  Pradesh','Karnataka','TamilNadu','Maharastra']
b=['Hyderabad','Amaravathi','Bangalore','Chennai','Mumbai']
c=enumerate(a)
for index,element in c:
	print(F'{element:15}...{b[index]}')
	time.sleep(1)

#Output
Telangana      ...Hyderabad
Andhra  Pradesh...Amaravathi
Karnataka      ...Bangalore
TamilNadu      ...Chennai
Maharastra     ...Mumbai
