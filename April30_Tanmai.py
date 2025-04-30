"""# Identify  Error  (Home  work)
try: 
	print('Hyd')
	print('Sec')
	print('Cyb') # error no except suite / finally
# Find  outputs  (Home  work)
#print(7 / 0) # zero devision error  
try:
	print(7 / 0)
except  ZeroDivisionError:
	print('Division  by  zero  is  not  permitted') # Division by zero is not permitted 
print(7 / 0) #  error 
print('Bye') # Bye  

# Identify  error  (Home  work)
#except:
        print('Hyd')
        print('Sec')
        print('Cyb') # there should be try block

# Find  outputs (Home  work) 
try:
        print('One')
        print('Two')
        print('Three')
#print('Four') # error  
except:
		print('Five')
		print('Six')
		print('Seven')
print('Eight')

# Identify  error  (Home  work)
try:
	print('try suite')
except: # should at the end 
	print('default  except')
except NameError:
	print('Name  Error')

# Identify  error  (Home  work)
try:
	print('try suite')
except: # only one except suit should be used  
	print('1st  default  except')
except:
	print('2nd  default  except') """

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
			self.x=int(input("Enter a number: "))
			#How  to  read  number  into  variable  'x' of  object  self
	def  add(self , m , n):
		self.add=(m.x+n.x)
			#How  to  add  objects  m  and  n  and  store  result  in  object  self
	def  display(self):
			print (self.add) #(How  to  print  sum  result)
class   string(datatype):
	def  get(self):
			self.x=input ("Enter a string: ") #How  to  read  string  into  variable  'x' of  object  self
	def  add(self , m , n):
			self.add=m.x+n.x
			#How  to  join  objects  m  and  n  and  store  result  in  object  self
	def  display(self):
			print (self.add) #(How  to  print  the   join  result)
def   menu():
	print('1. Add  numbers')
	print('2. Join  Strings')
	print('3. Exit')
# End  of  the  function
menu()
ch =  eval(input('Enter choice : '))

while ch <3:  #repeat   until  user  input  is  3
		a=[]
		if   ch == 1:
			for i in range(3):
				a.append(number() )
				#How  to  create  list  of  3  number  class  objects
		else:
			for i in range(3):
				a.append(string())
				#How  to  create  list  of  3  string  class  objects
		a[0].get()#How  to  read  input  into  first  object
		a[1].get() #How  to  read  input  into  2nd  object
		a[2].add(a[0],a[1])  #How  to  add  (or)  join  the  two  objects  and  store  the  result  in  3rd  object
		a[2].display() #How  to  print  3rd  object
		menu()
		ch = eval(input('Enter  choice : '))
# end of  while  loop
print('Good  Bye')
