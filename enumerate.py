'''import time
lst = [25,10.8,'Hyd',True,None]
e = enumerate(lst,start = 5)
while True:
	try:
		print(next(e))
		time . sleep(1)
	except:
		break
'''

#can be set enumerated?
'''import time
a = {25 , 10.8 , 'Hyd' , True}
print(a)
b = enumerate(a)
while True:
	try:
		print(next(b))
	except StopIteration:
		break
'''


# Find  outputs
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

#output
5 <next line> 1 <next line> 4294967295 <next line> 1 <next line> 3 <next line> 1 <next line> 3 <next line> 1 <next line> 3
'''



'''import  sys
class  Test:
	def __init__(self):
		print('Constructor  :  ' , id(self))
		return  None  
	def  __del__(self):
		print('Destructor  :  ' , id(self))
		return  25
# End  of  the  class
t = Test()
print(t . __init__())
print(sys . getrefcount(t))
print(t . __del__())
print(sys . getrefcount(t))
print('Bye')

#output
Constructor  :   1947813636688
Constructor  :   1947813636688
None
2
Destructor  :   1947813636688
25
2
Bye
Destructor  :   1947813636688
'''


#  Gift
'''class  c1:
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
print('Program  Begin')
b = f1()
print(b)
print('Program  End')

#output
Program  Begin
Function  Begin
Object  is    created
type and address of the memory
type and address of the memory
Program  End
Object  is  lost
'''


'''class  c1:
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
print('Program  Begin')
f1()
print('Program  End')

#output
Program  Begin
Function  begin
Object  is    created
Function  end
Object  is  lost
Program  End
'''



'''class  c1:
	def  __init__(self):
		print('Object  is    created')
	def  __del__(self):
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

#output
Program  Begin
Function  begin
Object  is    created
Function  end
Object  is  lost
None
Program  End
'''


# Most  tricky  program
# Circular  reference 
'''class   c1:
	def   __init__(self , k):
		print('c1  class  object  is  created')
		self . b = k
		print('End  of  c1  class constructor')
	def   __del__(self):
		print('c1  class  object  is  lost')
# End of class c1
class  c2:
	def  __init__(self):
		print('c2  class  object  is  created')
		self . a = c1(self)
		print('End  of  c2  class constructor')
	def  __del__(self):
		print('c2  class  object  is  lost')
#End of class c2
print('Program  begin')
x = c2()
print('program end')

#output
Program  begin
c2  class  object  is  created
c1  class  object  is  created
End  of  c1  class constructor
End  of  c2  class constructor
program end
c2  class  object  is  lost
c1  class  object  is  lost
'''


# Find  outputs (Home  work)
'''class   c1:
	def  __del__(self):
		print('Destructor')   # Destructor
		global  b
		b = self
a = c1()
del  a
print('Hello') # Hello'''


#  Can  string  be  enumerated ?
'''import   time
a = input('Enter  any  string  :  ')   #  Assume  that  input  is   HYD
e = enumerate(a)
while   True:
	try:
		print(next(e))
		time . sleep(1)
	except  StopIteration:
		break

#output
Enter  any  string  :  raju
(0, 'r')
(1, 'a')
(2, 'j')
(3, 'u')
'''


# Can  dictionary  be  enumerated ?   
'''import   time
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

#output
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
(7, 'Sal')
'''



'''import   time
a = ['Telangana' , 'Andhra  Pradesh' , 'Karnataka' , 'TamilNadu' , 'Maharastra']
b = ['Hyderabad' , 'Amaravathi' , 'Bangalore' , 'Chennai' , 'Mumbai']
c = enumerate(a)
for  index , element  in  c:
	print(F'{element:15}  :  {b[index]}')
	time . sleep(1)

#output
Telangana        :  Hyderabad
Andhra  Pradesh  :  Amaravathi
Karnataka        :  Bangalore
TamilNadu        :  Chennai
Maharastra       :  Mumbai
'''




















