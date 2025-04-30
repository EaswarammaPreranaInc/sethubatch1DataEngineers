
# Find  outputs
import   sys
class   c1:
        pass
# End  of  the  class
a = b = c = d = c1()
print(sys . getrefcount(b)) # 1
print(sys . getrefcount(c1()))# 6
print(sys . getrefcount(25))#1
print(sys . getrefcount([10 , 20 , 15 , 18]))# 3
print(sys . getrefcount(10.8))#1
print(sys . getrefcount({10 , 20 , 15 , 18}))#1
print(sys . getrefcount('Hyd'))# 3
print(sys . getrefcount({10 : 20 , 30 : 40}))#1
print(sys . getrefcount((10 , 20 , 30 , 40)))#3


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
t = Test() # constructor : 1000
print(t . __init__())# Constructor : 1000 <nextline> None
print(sys . getrefcount(t))# 2
print(t . __del__())#Destructor  : 1000 <nextline>25
print(sys . getrefcount(t)) #2
print('Bye')#Bye
#Destructor : 1000

#  Gift
class  c1:
	def  __init__(self):
		print('Object  is    created',id(self))
	def  __del__(self):
		print('Object  is  lost',id(self))
 #End  of  the  class
def    f1():
	print('Function  Begin')
	a  =  c1()
	print(a)
	print('Function  end')
	return   a
print('Program  Begin') # program Begin
b = f1() #Function begin <nextline> Object 'a'  is    created <next line> <__main__.c1 object at 109350983> <next line> Function  end
print(b)# <__main__.c1object at and 109350983>
print('Program  End') # Program end
#destructor :109350983

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
f1() # Function Begin <nextline> Object  is    created <nextline> Function  end <nextline> Object  is  lost
print('Program  End') #Program  End

# Most  tricky  program
# Circular  reference (Home  work)
class   c1:
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


'''
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
class   c1:
	def  __del__(self):
		print('Destructor')
		global  b
		b = self
a = c1()
del  a
print('Hello')

'''
Destructor
a is lost
hello

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
(0,H)
(1,Y)
(2,D)
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
'''
(0,Empno)
(1,Emp Name)
(2,Sal)

'''
c = enumerate(a . values())
disp(c)
'''
(0,25)
(1,Rama Rao)
(2,10000.0)

'''
d = enumerate(a . items())
disp(d)
'''
(0,(Empno,25))
(1,(Emp Name,Rama Rao))
(2,(Sal,1000.0))

'''
f = enumerate(a , start = 5)
disp(f)
'''
(5,Empno)
(6,Emp Name)
(7,Sal)

'''
# Find  outputs  (Home  work)
import   time
a = ['Telangana' , 'Andhra  Pradesh' , 'Karnataka' , 'TamilNadu' , 'Maharastra']
b = ['Hyderabad' , 'Amaravathi' , 'Bangalore' , 'Chennai' , 'Mumbai']
c = enumerate(a)
for  index , element  in  c:
	print(F'{element:15}  ... {b[index]}')
	time . sleep(1)
'''
Telangana        ... Hyderabad
Andhra  Pradesh  ... Amaravathi
Karnataka        ... Bangalore
TamilNadu        ... Chennai
Maharastra       ... Mumbai
'''

