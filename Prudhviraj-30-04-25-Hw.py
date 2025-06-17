# Identify  Error  (Home  work)
try: 
	print('Hyd')
	print('Sec')
	print('Cyb') # Error Due to No Except Block 


# Find  outputs  (Home  work)
print(7 / 0)
try:
	print(7 / 0)
except  ZeroDivisionError:
	print('Division  by  zero  is  not  permitted')
print(7 / 0) #Error Zero Division Error
print('Bye')

# Identify  error  (Home  work)
except:                #Error due to No try block
        print('Hyd')
        print('Sec')
        print('Cyb')

# Find  outputs (Home  work)
try:
        print('One')
        print('Two')
        print('Three')
print('Four') #Error due to Expecting error block
except:
		print('Five')
		print('Six')
		print('Seven')
print('Eight')

# Identify  error  (Home  work)
try:
	print('try suite')
except:                        #this Except block should be at last
	print('default  except')
except NameError:
	print('Name  Error')

# Identify  error  (Home  work)
try:
	print('try suite')
except:                  
	print('1st  default  except')
except:                            #Only one except block must be in the code
	print('2nd  default  except')


#  Write  a  progran  to  add  num  class  objects  and  join  str  class  objects
from  abc  import  abstractmethod , ABC
class   datatype(ABC):
	@abstractmethod
	def  get(self):
		pass
	@abstractmethod
	def  add(self , m ,  n):
		pass
	@abstractmethod
	def  display(self):
		pass
class   number(datatype):
	def  get(self):
			self.x=int(input("Enter any Number: "))  #How  to  read  number  into  variable  'x' of  object  self
	def  add(self , m , n):
			self.x=m.x+n.x  #How  to  add  objects  m  and  n  and  store  result  in  object  self
	def  display(self):
			print(F"The result of sum is {self.x}")  #How  to  print  sum  result)
class   string(datatype):	
	def  get(self):
			self.x=input("Enter any string: ")#How  to  read  string  into  variable  'x' of  object  self
	def  add(self , m , n):
			self.x=m.x+n.x   #How  to  join  objects  m  and  n  and  store  result  in  object  self
	def  display(self):
			print(F"The resul of join is {self.x}")#How  to  print  the   join  result)
def   menu():
	print('1. Add  numbers')
	print('2. Join  Strings')
	print('3. Exit')
# End  of  the  function
menu()
ch =  eval(input('Enter choice : '))
while  ch<3:    #repeat   until  user  input  is  3
		if   ch == 1:
				L=[number() for _ in range(3)]
		else:
			L = [string() for _ in range(3)] 
		L[0].get()      #How  to  read  input  into  first  object
		L[1].get()     #How  to  read  input  into  2nd  object
		L[2].add(L[0],L[1])  #How  to  add  (or)  join  the  two  objects  and  store  the  result  in  3rd  object
		L[2].display()  #How  to  print  3rd  object
		menu()
		ch = eval(input('Enter  choice : '))
# end of  while  loop
print('Good  Bye')
