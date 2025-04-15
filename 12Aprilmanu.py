'''
#2) Find  outputs
import   sys
class   c1:
        pass
# End  of  the  class
a = b = c = d = c1()
print(sys . getrefcount(b)) # creates four variables pointing to the same object, so its reference count should be at least 5 (four variables + the function argument).
print(sys . getrefcount(c1())) # functional argument(self)
print(sys . getrefcount(25)) #  Immutable types like float , int, str, and tuple may have higher counts due to internal caching (e.g., small integers and short strings).
print(sys . getrefcount([10 , 20 , 15 , 18])) # functional argument(self)
print(sys . getrefcount(10.8)) # #  Immutable types like flaot ,int, str, and tuple may have higher counts due to internal caching (e.g., small integers and short strings).
print(sys . getrefcount({10 , 20 , 15 , 18})) # functional argument(self)
print(sys . getrefcount('Hyd')) #  Immutable types like float , int, str, and tuple may have higher counts due to internal caching (e.g., small integers and short strings).
print(sys . getrefcount({10 : 20 , 30 : 40})) # functional argument(self)
print(sys . getrefcount((10 , 20 , 30 , 40))) #  Immutable types like float, int, str, and tuple may have higher counts due to internal caching (e.g., small integers and short strings).

output:-
---------
5
1
4294967295
1
3
1
3
1
3


#2)Find  outputs  (Home  work)
import  sys
class  Test:
	def  __init__(self):
		print('Constructor  :  ' , id(self))
		return    None
	def  __del__(self):
		print('Destructor  :  ' , id(self))
		return  25
# End  of  the  class
t = Test() # Test object is creating 't'
print(t . __init__()) # explicit call
print(sys . getrefcount(t)) 
print(t . __del__())
print(sys . getrefcount(t)) # explicit call
print('Bye')

output:-
----------
Constructor  :   1710800005712
Constructor  :   1710800005712
None
2
Destructor  :   1710800005712
25
2
Bye
Destructor  :   1710800005712

#3)Gift
# Find  outputs (Home  work)
class  c1:
	def  __init__(self): # Constructor created
		print('Object  is    created')
	def  __del__(self): # Destructor created
		print('Object  is  lost')
#End  of  the  class
def    f1():
	print('Function  Begin')
	a  =  c1() # Constructor is called here
	print(a) # Prints object reference
	print('Function  end')
	return   a # 'a' is returned, so still referenced after function exits
print('Program  Begin')
b = f1() # Calls f1, creating object to b
print(b) # Prints object reference
print('Program  End')

output:-
----------
Program  Begin
Function  Begin
Object  is    created
<__main__.c1 object at 0x0000020CBD466A50>
Function  end
<__main__.c1 object at 0x0000020CBD466A50>
Program  End
Object  is  lost

#4)Gift
# Find  outputs (Home  work)
class  c1:
	def  __init__(self): # constructor created
		print('Object  is    created')
	def  __del__(self): # Destructor created
		print('Object  is  lost')
#End  of  the  class
def    f1():
        print('Function  begin')
        a  =  c1()  # Calls c1, creating object to a
        print('Function  end')
        return   a # returns None to constructor call here.
print('Program  Begin')
f1()
print('Program  End')

output:-
--------
Program  Begin
Function  begin
Object  is    created
Function  end
Object  is  lost
Program  End

#5) Find  outputs (Home  work)
class  c1:
	def  __init__(self):
		print('Object  is    created') # constructor created
	def  __del__(self): # Destructor created
		print('Object  is  lost')
#End  of  the  class
def    f1():
        print('Function  begin')
        a  =  c1() # Calls c1, creating object to b
        print('Function  end')
print('Program  Begin')
b = f1() # Calls f1, creating object to b
print(b)
print('Program  End')

output:-
--------
Program  Begin
Function  begin
Object  is    created
Function  end
Object  is  lost
None (return not there none is returned here)
Program  End

#6) Most  tricky  program
# Circular  reference (Home  work)

class   c1:
	def   __init__(self , k): # Constructor created
		print('c1  class  object  is  created')
		self . b = k
		print('End  of  c1  class constructor')
	def   __del__(self): # Destructor created
		print('c1  class  object  is  lost')
# End of class c1
class  c2:
	def  __init__(self): # Constructor created
		print('c2  class  object  is  created')
		self . a = c1(self)
		print('End  of  c2  class constructor')
	def  __del__(self):# Destructor created
		print('c2  class  object  is  lost')
#End of class c2
print('Program  begin')
x = c2() # call c2 we are creating object  'x' 
print('program end')

output:-
----------
Program  begin
c2  class  object  is  created
c1  class  object  is  created
End  of  c1  class constructor
End  of  c2  class constructor
program end
c2  class  object  is  lost
c1  class  object  is  lost


#7) Find  outputs (Home  work)
class   c1:
	def  __del__(self): # Destructor created 
		print('Destructor')
		global  b
		b = self
a = c1() # call c1 we are creating object  'a'
del  a
print('Hello')

output:-
---------
Destructor
Hello

#8)Can  string  be  enumerated ?
import   time
a = input('Enter  any  string  :  ')   #  Assume  that  input  is   HYD
e = enumerate(a) # creating tuple of 1st element index number and 2nd element is element of string
while   True:
	try:
		print(next(e))
		time . sleep(1)
	except  StopIteration:
		break
output:-
Enter  any  string  :  HYD
(0, 'H')
(1, 'Y')
(2, 'D')

#9)Can  dictionary  be  enumerated ?   (Home  work)
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
print(b)
disp(b)# prints tuple of indexs as 1st element and keys as 2nd element
c = enumerate(a . values())
print(c)
disp(c) # prints tuple of indexs as 1st element and values as 2nd element
d = enumerate(a . items())
print(d)
disp(d) # prints tuple of indexs as 1st element and keys and values as 2nd element
f = enumerate(a , start = 5)
disp(f) # prints tuple of indexs(index starts with 5 number here) as 1st element and by default keys as 2nd element

output:-
---------
<enumerate object at 0x000002284363B100>
(0, 'Empno')
(1, 'Emp Name')
(2, 'Sal')

<enumerate object at 0x0000022843639F80>
(0, 25)
(1, 'Rama Rao')
(2, 10000.0)

<enumerate object at 0x000002284369B010>
(0, ('Empno', 25))
(1, ('Emp Name', 'Rama Rao'))
(2, ('Sal', 10000.0))

(5, 'Empno')
(6, 'Emp Name')
(7, 'Sal')
'''
#10) Find  outputs  (Home  work)
import   time
a = ['Telangana' , 'Andhra  Pradesh' , 'Karnataka' , 'TamilNadu' , 'Maharastra']
b = ['Hyderabad' , 'Amaravathi' , 'Bangalore' , 'Chennai' , 'Mumbai']
c = enumerate(a)
for  index , element  in  c:
	print(F'{element:15}  ... {b[index]}')
	time . sleep(1)