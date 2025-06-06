
#1.Find  outputs

'''
import   sys
class   c1:
        pass
# End  of  the  class
a = b = c = d = c1()
print(sys . getrefcount(b)) #5 
print(sys . getrefcount(c1())) #1
print(sys . getrefcount(25)) #NA
print(sys . getrefcount([10 , 20 , 15 , 18])) #1 
print(sys . getrefcount(10.8)) #NA
print(sys . getrefcount({10 , 20 , 15 , 18})) #1
print(sys . getrefcount('Hyd')) # NA
print(sys . getrefcount({10 : 20 , 30 : 40})) #1
print(sys . getrefcount((10 , 20 , 30 , 40))) #NA

'''

#2.Find  outputs  (Home  work)
'''
import  sys
class  Test:
	def  __init__(self):
		print('Constructor  :  ' , id(self))
		return    None
	def  __del__(self):
		print('Destructor  :  ' , id(self))
		return  25
# End  of  the  class
t = Test()  #1. Constructor  :  1000
print(t . __init__()) #2. Constructor  :  1000
print(sys . getrefcount(t)) #3. 2
print(t . __del__()) #4.Destructor  : 1000 #5. 25
print(sys . getrefcount(t)) #6. 2
print('Bye') #7.Bye 

'''



#  Gift
#3.Find  outputs (Home  work)

'''
class  c1:
	def  __init__(self):
		print('Object  is    created')
	def  __del__(self):
		print('Object  is  lost')
#End  of  the  class
def    f1():
	print('Function  Begin') #2. Function  Begin
	a  =  c1() #3. Object  is    created
	print(a) #4. <__main__.c1 Object at 0xaddress>
	print('Function  end') #5. Function  end
	return   a
print('Program  Begin') #1. Program  Begin
b = f1() 
print(b) #6. <__main__.c1 Object at 0xaddress>
print('Program  End') #7. Program  End
#8. Object is lost

'''

#  Gift
'''
#4.Find  outputs (Home  work)
class  c1:
	def  __init__(self):
		print('Object  is    created')
	def  __del__(self):
		print('Object  is  lost')
#End  of  the  class
def    f1():
        print('Function  begin') #2. Function  begin
        a  =  c1() #3. Object  is    created
        print('Function  end') #4. Function  end
        return   a
        #5. Object is lost
        
print('Program  Begin') #1. Program  Begin
f1() 
print('Program  End') #6. Program End 

'''


#5.Find  outputs (Home  work)
'''
class  c1:
	def  __init__(self):
		print('Object  is    created')
	def  __del__(self):
		print('Object  is  lost')
#End  of  the  class
def    f1():
        print('Function  begin') #2. Function  begin
        a  =  c1() #3. Object  is    created
        print('Function  end') #4. Function end 
        #5. Object is lost 
        
print('Program  Begin') #1. Program  Begin
b = f1()
print(b) #6. None 
print('Program  End') #7. Program End

'''

# Most  tricky  program
#6.Circular  reference (Home  work)

'''
class   c1:
	def   __init__(self , k):
		print('c1  class  object  is  created') #3. c1  class  object  is  created
		self . b = k 
		print('End  of  c1  class constructor') #4. End  of  c1  class constructor
	def   __del__(self):
		print('c1  class  object  is  lost')
# End of class c1
class  c2:
	def  __init__(self):
		print('c2  class  object  is  created') #2. c2  class  object  is  created
		self . a = c1(self)
		print('End  of  c2  class constructor') #5. End  of  c2  class constructor
		
		
	def  __del__(self):
		print('c2  class  object  is  lost')
		
#End of class c2
print('Program  begin') #1. Program  begin
x = c2() 
print('program end') #6.program end 
#7. c2  class  object  is  lost
#8. c1  class  object  is  lost

'''

#7.Find  outputs (Home  work)
'''
class   c1:
	def  __del__(self):
		print('Destructor')
		global  b
		b = self
a = c1()
del  a #1. Destructor
print('Hello') #2. Hello 

'''

#(Home  work)
#8.Can  string  be  enumerated ?

'''
import   time
a = input('Enter  any  string  :  ')   #  Assume  that  input  is   HYD
e = enumerate(a)
while   True:
	try:
		print(next(e)) # (0,'H') # (1,'Y') # (2,'D') 
		time . sleep(1)
	except  StopIteration:
	
'''

#9.Can  dictionary  be  enumerated ?   (Home  work)

'''
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
disp(b) # (0,'Empno') #(1,'Emp Name') #(2,'Sal')
c = enumerate(a . values())
disp(c) # (0,25) #(1,'Rama Rao') #(2,10000.0)
d = enumerate(a . items())  
disp(d) # (0,('Empno',25) #(1,('Emp Name','Rama Rao')) #(2,('Sal',10000.0))
f = enumerate(a , start = 5)
disp(f) # (0,'Empno') #(1,'Emp Name') #(2,'Sal')
	
'''


#10.Find  outputs  (Home  work)
'''
import   time
a = ['Telangana' , 'Andhra  Pradesh' , 'Karnataka' , 'TamilNadu' , 'Maharastra']
b = ['Hyderabad' , 'Amaravathi' , 'Bangalore' , 'Chennai' , 'Mumbai']
c = enumerate(a)
for  index , element  in  c:
	print(F'{element:15}  ... {b[index]}')
	time . sleep(1)
	
'''
'''
element:Telangana       ... Hyderabad
element:Andhra Pradesh  ... Amaravathi
element:Karnataka       ... Bangalore
element:TamilNadu       ... Chennai
element:Maharastra      ... Mumbai

'''