#Ex-1
# Find  outputs
import   sys
class   c1:
        pass
# End  of  the  class
a = b = c = d = c1() #  5
print(sys . getrefcount(b)) # 1
print(sys . getrefcount(c1())) #
print(sys . getrefcount(25)) #  immutable object can't be  predicted it is reusable
print(sys . getrefcount([10 , 20 , 15 , 18])) # 1
print(sys . getrefcount(10.8)) #  immutable object can't be  predicted it is reusable
print(sys . getrefcount({10 , 20 , 15 , 18})) # 1
print(sys . getrefcount('Hyd'))  # Hyd  can't be  predicted
print(sys . getrefcount({10 : 20 , 30 : 40})) # 1
print(sys . getrefcount((10,20,30,40))) #  immutable object can't be  predicted it is reusable

#Ex-2
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
t = Test() # creating object and automatically execute constructor
print(t . __init__()) # None
print(sys . getrefcount(t)) # 2
print(t . __del__()) # 25
print(sys . getrefcount(t)) # 2
print('Bye') # Bye

#Ex-3
#  Gift
# Find  outputs (Home  work)
class  c1:
	def  __init__(self):
		print('Object  is    created') # Object  is    created
	def  __del__(self):
		print('Object  is  lost') # Object is lost
#End  of  the  class
def    f1():
	print('Function  Begin') # Function  Begin
	a  =  c1() # creating object automatically execute constructor
	print(a) # type and address
	print('Function  end') # Function end
	return   a # object reference a
print('Program  Begin') #  Program  Begin
b = f1() # call f1 function and return object reference
print(b) #  type and address of a
print('Program End') # Program End
# delete object execute __del__

#Ex-4
#  Gift
# Find  outputs (Home  work)
class  c1:
	def  __init__(self):
		print('Object  is    created') # Object  is    created
	def  __del__(self):
		print('Object  is  lost')
#End  of  the  class
def    f1():
        print('Function  begin') # Function  begin
        a  =  c1() # Creating object and constructor executed automatically
        print('Function  end') # Function  end
        return   a # return a
print('Program  Begin') # Program Begin
f1()
print('Program End') # Program End

#Ex-5
# Find  outputs (Home  work)
class c1:
    def __init__(self):
        print('Object  is    created')
    def __del__(self):
        print('Object  is  lost')
#End  of  the  class
def f1():
    print('Function  begin') # Function  begin
    a  =  c1() # creating object and constructor executed automatically
    print('Function  end') # Function  end
    # delete object
print('Program  Begin') # Program  Begin
b = f1() # call f1 function
print(b) # None
print('Program End') # Program End

#Ex-6
# Most  tricky  program
# Circular  reference (Home  work)
class c1:
    def __init__(self , k):
        print('c1  class  object  is  created') # c1  class  object  is  created
        self . b = k # add b variable to object and value is  reference of object of class c2,
        print('End  of  c1  class constructor')
    def __del__(self):
        print('c1  class  object  is  lost')
# End of class c1
class  c2:
	def  __init__(self):
		print('c2  class  object  is  created') # c2  class  object  is  created
		self . a = c1(self) #add a variable to object and assign variable value is object of class c1  and pass reference b object of class 2
		print('End  of  c2  class constructor')
	def  __del__(self):
		print('c2  class  object  is  lost')
#End of class c2
print('Program  begin') # Program begin
x = c2() # creating object of class c2 and execute constructor automatically class c2
print('program end') # program end

#Ex-7
# Find  outputs (Home  work)
class   c1:
	def  __del__(self):
		print('Destructor')
		global  b
		b = self
a = c1() # creating empty Object
del  a #  delete reference a and also destroy object execute destructor  # Destructor
print('Hello') # Hello


#Ex-8
#(Home  work)
#  Can  string  be  enumerated ?
import   time
a = input('Enter  any  string  :  ')   #  Assume  that  input  is   HYD
e = enumerate(a) # create empty enumerate
while   True:
	try:
		print(next(e)) # tuple of two elements (index,next element of sequence) # (0,'H') <nl> (1,'y') <nl> (2,'d')
		time . sleep(1)
	except  StopIteration:
		break

#Ex-9
# Can  dictionary  be  enumerated ?   (Home  work)
import   time
def  disp(e):
	while  True:
		try:
			print(next(e)) # (0,'Empno') <nl> (1,'Emp Name') <nl> (1,'Sal')
			time . sleep(1)
		except:
			break
	print()
a = {'Empno'  :  25 , 'Emp Name'  :  'Rama Rao' , 'Sal' : 10000.0}
b = enumerate(a . keys()) # enumerate the list of keys in advance
disp(b) # (0,'Empno') <nl> (1,'Emp Name') <nl> (1,'Sal')
c = enumerate(a . values()) #  enumerate the list of values  in advance
disp(c) # (0,25) <nl> (1,'Ra ma Rao') <nl> (1,10000.0)
d = enumerate(a . items()) # enumerate list of tuples in advance
disp(d) # (0, ('Empno', 25)) <nl> (1, ('Emp Name', 'Rama Rao')) <nl> (2, ('Sal', 10000.0))
f = enumerate(a , start=5)
disp(f) # (5,'Empno') <nl> (6,'Emp Name') <nl> (7,'Sal')
