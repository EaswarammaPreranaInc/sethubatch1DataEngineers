Q1 #Find  outputs
import   sys
class   c1:
        pass
# End  of  the  class
a = b = c = d = c1()
print(sys . getrefcount(b)) #5
print(sys . getrefcount(c1())) #1
print(sys . getrefcount(25))   #4294967295
print(sys . getrefcount([10 , 20 , 15 , 18])) #1
print(sys . getrefcount(10.8))  #3
print(sys . getrefcount({10 , 20 , 15 , 18})) #1
print(sys . getrefcount('Hyd')) #3  
print(sys . getrefcount({10 : 20 , 30 : 40})) #1
print(sys . getrefcount((10 , 20 , 30 , 40))) #3
#-----------------------------------------------------------------------------------
Q2 #Find  outputs  (Home  work)
import  sys
class  Test:
	def  __init__(self):
		print('Constructor  :  ' , id(self))  #Constructor  :   1643309460048
		return    None
	def  __del__(self):
		print('Destructor  :  ' , id(self)) #Destructor  :   1643309460048
		return  25
# End  of  the  class
t = Test()
print(t . __init__())  ##Constructor  :   1643309460048     None
print(sys . getrefcount(t)) #2
print(t . __del__())    #25
print(sys . getrefcount(t)) #2
print('Bye')  #Bye  Destructor  :   1643309460048
#----------------------------------------------------------------------------------------
Q3 #Find  outputs (Home  work)
class  c1:
	def  __init__(self):
		print('Object  is    created') #Object is crerated
	def  __del__(self):
		print('Object  is  lost')      #prints Object is lost when program is executed 
#End  of  the  class
def    f1():
	print('Function  Begin')  #Function Begin
	a  =  c1()
	print(a)    #prints type and address of object a 
	print('Function  end')    #Function end
	return   a
print('Program  Begin')   #Program Begin
b = f1()    #return object a to b
print(b)     #prints type and address of object a
print('Program  End') #Program End

OP-
Program Begin
Function Begin
Object is created
<__main__.c1 object at 0x000001C3FB7F6A50>
Function end
<__main__.c1 object at 0x000001C3FB7F6A50>
Program End
Object is lost
#-----------------------------------------------------------------------------------------------
Q4 #Find  outputs (Home  work)

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
print('Program  Begin') 
f1()
print('Program  End')

OP-
Program Begin
Function Begin
Object is created
Function end
Object is lost
Program End
#--------------------------------------------------------------------------------------------
Q5 #Find  outputs (Home  work)
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
print('Program  Begin')
b = f1()
print(b)
print('Program  End')

OP-
Program Begin
Function begin
Object is created
Function end
Object is lost
None
Program End
#----------------------------------------------------------------------------------
Q6 # Circular  reference (Home  work)
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

OP-
Program begin
c2 class object is created
c1 class object is created
End of c1 class constructor
End of c2 class constructor
program end
c2 class object is lost
c1 class object is lost
#--------------------------------------------------------------------------------------
Q7 #Find  outputs (Home  work)

class   c1:
	def  __del__(self):
		print('Destructor')
		global  b
		b = self
a = c1()  
del  a    #Destructor
print('Hello') #Hello
#---------------------------------------------------------------------------------
Q8 #Can  string  be  enumerated ?
import   time
a = input('Enter  any  string  :  ')   #  Assume  that  input  is   HYD
e = enumerate(a)
while   True:
	try:
		print(next(e))
		time . sleep(1)
	except  StopIteration:
		break

OP-
Enter  any  string  :  HYD
(0, 'H')
(1, 'Y')
(2, 'D')
#-------------------------------------------------------------------------------------------
Q9 #Can  dictionary  be  enumerated ?   (Home  work)
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
disp(b)  #(0, 'Empno')  (1, 'Emp Name')  (2, 'Sal')
c = enumerate(a . values())
disp(c)  #(0, 25)  (1, 'Rama Rao')  (2, 10000.0)
d = enumerate(a . items())
disp(d)  #(0, ('Empno', 25))  (1, ('Emp Name', 'Rama Rao'))  (2, ('Sal', 10000.0))
f = enumerate(a , start = 5)
disp(f)  #(5, 'Empno')  (6, 'Emp Name')  (7, 'Sal')
#-----------------------------------------------------------------------------------------
Q10 #Find  outputs  (Home  work)
import   time
a = ['Telangana' , 'Andhra  Pradesh' , 'Karnataka' , 'TamilNadu' , 'Maharastra']
b = ['Hyderabad' , 'Amaravathi' , 'Bangalore' , 'Chennai' , 'Mumbai']
c = enumerate(a)
for  index , element  in  c:
	print(F'{element:15}  ... {b[index]}')
	time . sleep(1)

OP-
Telangana        ... Hyderabad
Andhra  Pradesh  ... Amaravathi
Karnataka        ... Bangalore
TamilNadu        ... Chennai
Maharastra       ... Mumbai
