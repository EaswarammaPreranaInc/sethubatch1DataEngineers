'''import   sys
class   c1:
        pass
# End  of  the  class
a = b = c = d = c1()
print(sys . getrefcount(b))
print(sys . getrefcount(c1()))
print(sys . getrefcount(25))
print(sys . getrefcount([10 , 20 , 15 , 18]))
print(sys . getrefcount(10.8))
print(sys . getrefcount({10 , 20 , 15 , 18}))
print(sys . getrefcount('Hyd'))
print(sys . getrefcount({10 : 20 , 30 : 40}))
print(sys . getrefcount((10 , 20 , 30 , 40)))

output:
5
1
4294967295
1
3
1
3
1
3


import  sys
class  Test:
	def  _init_(self):
		print('Constructor  :  ' , id(self))
		return    None
	def  _del_(self):
		print('Destructor  :  ' , id(self))
		return  25
# End  of  the  class
t = Test()
print(t . _init_())
print(sys . getrefcount(t))
print(t . _del_())
print(sys . getrefcount(t))
print('Bye')

output:
Constructor  :   1769332370000
Constructor  :   1769332370000
None
2
Destructor  :   1769332370000
25
2
Bye
Destructor  :   1769332370000

# Find  outputs (Home  work)
class  c1:
	def  _init_(self):
		print('Object  is    created')
	def  _del_(self):
		print('Object  is  lost')
#End  of  the  class
def    f1():
	print('Function  Begin')
	a  =  c1()
	print(a)
	print('Function  end')
	return   a
print('Program  Begin')
b = f1()
print(b)
print('Program  End')

output:
Program  Begin
Function  Begin
Object  is    created
<_main_.c1 object at 0x0000021309826A50>
Function  end
<_main_.c1 object at 0x0000021309826A50>
Program  End
Object  is  lost

# Find  outputs (Home  work)
class  c1:
	def  _init_(self):
		print('Object  is    created')
	def  _del_(self):
		print('Object  is  lost')
#End  of  the  class
def    f1():
        print('Function  begin')
        a  =  c1()
        print('Function  end')
        return   a
print('Program  Begin')
f1()
print('Program  End')

output:
Program  Begin
Function  begin
Object  is    created
Function  end
Object  is  lost
Program  End

class  c1:
	def  _init_(self):
		print('Object  is    created')
	def  _del_(self):
		print('Object  is  lost')
#End  of  the  class
def    f1():
        print('Function  begin')
        a  =  c1()
        print('Function  end')
print('Program  Begin')
b = f1()
print(b)
print('Program  End')

output:
Program  Begin
Function  begin
Object  is    created
Function  end
Object  is  lost
None
Program  End

# Circular  reference (Home  work)
class   c1:
	def   _init_(self , k):
		print('c1  class  object  is  created')
		self . b = k
		print('End  of  c1  class constructor')
	def   _del_(self):
		print('c1  class  object  is  lost')
# End of class c1
class  c2:
	def  _init_(self):
		print('c2  class  object  is  created')
		self . a = c1(self)
		print('End  of  c2  class constructor')
	def  _del_(self):
		print('c2  class  object  is  lost')
#End of class c2
print('Program  begin')
x = c2()
print('program end')

ouput:
Program  begin
c2  class  object  is  created
c1  class  object  is  created
End  of  c1  class constructor
End  of  c2  class constructor
program end
c2  class  object  is  lost
c1  class  object  is  lost

class   c1:
	def  _del_(self):
		print('Destructor')
		global  b
		b = self
a = c1()
del  a
print('Hello')

output:
Destructor
Hello

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

OUTPUT:
Enter  any  string  :  HYD
(0, 'H')
(1, 'Y')
(2, 'D')

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
f = enumerate(a , start = 5)
disp(f)

OUTPUT:
(0, 'Empno')
(1, 'Emp Name')
(2, 'Sal')

(0, 25)
(1, 'Rama Rao')
(2, 10000.0)

(0, ('Empno', 25))
(1, ('Emp Name', 'Rama Rao'))
(2, ('Sal', 10000.0))

(5, 'Empno')
(6, 'Emp Name')
(7, 'Sal')'''

import   time
a = ['Telangana' , 'Andhra  Pradesh' , 'Karnataka' , 'TamilNadu' , 'Maharastra']
b = ['Hyderabad' , 'Amaravathi' , 'Bangalore' , 'Chennai' , 'Mumbai']
c = enumerate(a)
for  index , element  in  c:
	print(F'{element:15}  ... {b[index]}')
	time . sleep(1)

OUTPUT:
Telangana        ... Hyderabad
Andhra  Pradesh  ... Amaravathi
Karnataka        ... Bangalore
TamilNadu        ... Chennai
Maharastra       ... Mumbai
