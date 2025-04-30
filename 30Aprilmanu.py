'''
#1)   Write  a  progran  to  add  num  class  objects  and  join  str  class  objects
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
	def __init__(self):
		self.x = 0 
	def  get(self):
			self. x = eval(input(" enter the number")) # How  to  read  number  into  variable  'x' of  object  self
	def  add(self , m , n):
			self.x  = m.x + n.x # How  to  add  objects  m  and  n  and  store  result  in  object  self
	def  display(self):
			print(" sum is:" ,self.x) #How  to  print  sum  result)
class   string(datatype):
	def __init__(self):
		self.x = ""
	def  get(self):
			self.x = input(" Enter the string: ") # How  to  read  string  into  variable  'x' of  object  self
	def add(self , m , n):
			self.x = m.x + n.x # How  to  join  objects  m  and  n  and  store  result  in  object  self
	def  display(self):
			print(" joined string is :" , self.x ) # How  to  print  the   join  result)
def   menu():
	print('1. Add  numbers')
	print('2. Join  Strings')
	print('3. Exit')
# End  of  the  function
menu()
ch =  int(input('Enter choice : '))
while  ch != 3: # repeat   until  user  input  is  3
		if   ch == 1:
				list = [number(), number() , number()] # How  to  create  list  of  3  number  class  objects
		elif ch ==2 :
			list = [ string(), string(), string() ] # How  to  create  list  of  3  string  class  objects
		else:
			print("Invalid choice.")
			menu()
			ch = int(input(" Enter choice: ")) 
			continue
		list[0].get() # How  to  read  input  into  first  object
		list[1].get() # How  to  read  input  into  2nd  object
		list[2].add(list[0],list[1]) #  #How  to  add  (or)  join  the  two  objects  and  store  the  result  in  3rd  object
		list[2].display() # How  to  print  3rd  object
		menu()
		ch = eval(input('Enter  choice : '))
# end of  while  loop
print('Good  Bye')

output:-
---------
1. Add  numbers
2. Join  Strings
3. Exit
Enter choice : 1
 enter the number8
 enter the number4
 sum is: 12
1. Add  numbers
2. Join  Strings
3. Exit
Enter  choice : 2
 Enter the string: Hyder
 Enter the string: abad
 joined string is : Hyderabad
1. Add  numbers
2. Join  Strings
3. Exit
Enter  choice : 3
Good  Bye

#2)# Identify  Error  (Home  work)
try: 
	print('Hyd')
	print('Sec')
	print('Cyb')
output:-
-------
need to write except suit or finally suit to complete try suits.


#3)Find  outputs  (Home  work)
#print(7 / 0) # Error : ZeroDivisionError
try:
	print(7 / 0)
except  ZeroDivisionError: # it will handle for only above 7/0 
	print('Division  by  zero  is  not  permitted')
#print(7 / 0) # Error : ZeroDivisionError
print('Bye')

output:-
----------
Division  by  zero  is  not  permitted
Bye

#4) Identify  error  (Home  work)
except:
        print('Hyd')
        print('Sec')
        print('Cyb')

output:-
-------
need to write try suit above  , it is a sequence try than except suit write  to complete except suits.

#5)Find  outputs (Home  work)
try:
        print('One')
        print('Two')
        print('Three')
#print('Four') # Error : need to write (or) expexts finally or except suits.
except:
		print('Five')# not considered
		print('Six')# not considered
		print('Seven')# not considered
print('Eight')

output:-
----------
One
Two
Three
Eight

#6)Identify  error  (Home  work)
try:
	print('try suite')
#except: # error: default 'except:' must be last
	print('default  except')
except NameError:
	print('Name  Error') # not considered 
output:-
----------
try suite
default  except


#7)Identify  error  (Home  work)
try:
	print('try suite')
#except: # error: default 'except:' must be last
	print('1st  default  except')
except:
	print('2nd  default  except') # ignored.
output:-
---------
try suite
1st  default  except
'''

#8)Write  a  program  to  determine  total  and  average  of  student  and  gross pay  and  net  pay  of  teacher
from  abc  import  *
class  person(ABC):
	def   get(self):
		self . number = int(input('Enter  number  :  '))   # How  to   read  number
		self . name = input('Enter  name :  ')  #  How  to   read  name
		self . age = int(input('Enter  age :  ')) #  How  to   read   age
		self . gender = input('Enter  gender :  ')   # How  to   read   gender
	def   disp(self):
		print(self . number , self . name , self . age , self . gender , sep = '\t' , end = '\t')  #  How  to  print  number , name , age , gender  in  same  line  separated  by  tab
	@abstractmethod
	def   compute(self):
                pass
'''
1) Why  is  compute()  an  abstract  method ?  --->  No  idea  what  to  calculate

2) What  is  the  advantage  of  writing  ABC ?  --->  Every  child  class  should  implement  compute()  method

3) What  happens  if  at  least  one  child  class  does  not  implement  compute()  method  ?  --->
																										That  child  class  object  can  not  be  created
'''
class  student(person):
	def  get(self):
		super() . get()  #  How  to  read   number , name , age , gender
		self . m = []
		for  i  in  range(3):  #  How  to  read  marks  of  3  subjects  into  list
				marks = int(input(F'Enter  marks  for  subject  {i + 1}  :  '))
				self . m . append(marks)
	def  compute(self):
		self . tot = sum(self . m)  #  How  to  calculate  total  marks
		self . avg = self . tot / 3  #  How  to  calculate  average  marks
	def  disp(self):
		super() . disp()  #  How  to  print  number , name , age , gender
		print(self . tot , self . avg , sep = '\t')  #  How  to  print  total  and  average  in  same  line separated  by  tab
class  teacher(person):
	def   get(self):
		super() . get()  #  How  to  read  number , name , age  and  gender
		self . sub = input('Enter  subject :  ')   # How  to  read   subject
		self . sal = float(input('Enter  salary  :  '))  #  How  to  read   salary
	def   compute(self):
		da = 0.50 * self . sal #   50%  of  salary
		hra = 0.20 * self . sal  #   20%  of  salary
		self . gp =  self . sal + da + hra  #  How  to  calculate  grosspay  and  store  the  result  in  object (grosspay  is  sal + da + hra)
		pf = min(0.08 * self . gp , 400)  #  8%  of  grosspay  but  a  max  of  400
		if  self . gp < 10000:
				tax = 0.10 * self . gp  #  10%  of  grosspay  if  grosspay is  < 10000  and  15%  otherwise
		else:
				tax = 0.10 * 10000 + 0.15 * (self . gp - 10000)
		self . np =  self . gp - pf - tax   #  How  to  calculate  netpay  and  store  the  result  in  object  (netpay  is  grosspay - pf - tax)
	'''
	What  are  da , hra , pf  and  tax ?  --->  Local  variables of  compute()  method
	'''
	def   disp(self):
		super() . disp() # How  to  print  number , name , age , gender
		print(self.sub , self.sal , self.gp , self.np , sep = '\t') # How  to  print  subject , salary , grosspay , netpay  in  same  line   separated  by  tab
# End  of  class
def  menu():
	print('1. Teacher')
	print('2. Student')
	print('3. Exit')
# End  of  the  function
a = []
i = 0
menu()
ch = eval(input('Enter choice : '))  #  2
while  ch < 3:  #  Repeat  until  input  is  3
	if   ch == 1:
		a . append(teacher())  #  How  to  append  teacher  object  to  list  'a'
	else:
		a . append(student())  #  How  to  append  student  object  to  list  'a'
	a[i] . get()  #  How  to  read  inputs  into  object
	a[i] . compute()   # How  to  store   results  in  object
	i += 1   #  How  to  move  to  next  index  --->  4
	menu()
	ch = eval(input('Enter choice : '))  #  3
#end of loop
print('Teachers')
#How  to  print  all  teacher  objects
for   x  in  a:  # 'x' is  each  object  of  list   'a'
	if  isinstance(x , teacher):
		x . disp()
print()
print('Students')
#How  to  print  all  student  objects
for   x  in  a:  # 'x' is  each  object  of  list   'a'
	if  isinstance(x , student):
		x . disp()
print('Good  Bye')


output:-
---------
1. Teacher
2. Student
3. Exit
Enter choice : 1
Enter  number  :  888
Enter  name :  mahaveer
Enter  age :  60
Enter  gender :  male
Enter  subject :  maths
Enter  salary  :  15000
1. Teacher
2. Student
3. Exit
Enter choice : 2
Enter  number  :  333
Enter  name :  naveen
Enter  age :  23
Enter  gender :  male
Enter  marks  for  subject  1  :  80
Enter  marks  for  subject  2  :  90
Enter  marks  for  subject  3  :  60
1. Teacher
2. Student
3. Exit
Enter choice : 2
Enter  number  :  666
Enter  name :  manisha
Enter  age :  22
Enter  gender :  female
Enter  marks  for  subject  1  :  100
Enter  marks  for  subject  2  :  90
Enter  marks  for  subject  3  :  80
1. Teacher
2. Student
3. Exit
Enter choice : 1
Enter  number  :  111
Enter  name :  m
Enter  age :  46
Enter  gender :  female
Enter  subject :  python
Enter  salary  :  30000
1. Teacher
2. Student
3. Exit
Enter choice : 3
Teachers
888     mahaveer        60      male    maths   15000.0 25500.0 21775.0
111     m       46      female  python  30000.0 51000.0 43450.0

Students
333     naveen  23      male    230     76.66666666666667
666     manisha 22      female  270     90.0
Good  Bye