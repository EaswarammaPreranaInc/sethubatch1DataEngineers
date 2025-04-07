'''
#1) Identify  error  (Home work)
class   c1:
	def  m1(self):
		pass
class   c2:
        pass
class   c3: # Error due to after class we have to write something atleast pass , if dont have statements.


#2)Find  outputs  (Home  work)
class   c1:
	pass
# End  of  the  class
a = c1() # creating object 'a' to class c1()
print(id(a)) # 2352771656272 ---> Id or Address of object 'a'.
print(type(a)) # <class '_main_.c1'> ----> type od object'a'.
print(a . _dict_) # {}---> empty dictionary prints bcz there is no arguments for object 'a'.
print(a) # <_main_.c1 object at 0x00000223CC1E6A50> --------> here Type and Address of objeectn'a' we gets .
del  a # deletion of object 'a'
#print(a) # Error due to 'a' ----> there is no object 'a' it was deleted 'a' 
print(a . dict)

output:-
---------
2352771656272
<class '__main__.c1'>
{}
<__main__.c1 object at 0x000001A6E48D6A50>


#3) Find  outputs  (Home  work)

def   m1():
		print('Function') # Function
class   c1:
	def   m1(self):
		print('1st  method') # 1st  method prints
	def   m1(self):
		print('2nd  method')# Replaces 1st  method with 2nd  method
	def   m1(self):
		print('3rd  method') # Replaces 2nd  method with 3rd  method
# End  of  class  c1
a = c1() # creating object 'a' to class c1()
a . m1() # calling m1() with respect to class c1()
m1() # calling m1 method of outside class 

output:-
-----------
3rd  method
Function



#4)#  Find  outputs  (Home  work)
class   c1:
	def   m1(self):
		print('No  argument  method') # No  argument  method prints
	def   m1(self , x):
		print('Single  argument  method : ' , x) #Replaces  No  argument  method Single  argument  method
	def   m1(self , x , y):
		print('Two  argument  method : ' , x , y)# Replaces Single  argument  method with Two  argument  method. Atlast it is consider in calling method m1().
# End  of  class  c1
a = c1() # creating object 'a' to class c1()
a . m1(10 , 20) # calling m1() with respect to class c1() with two arguments 
#a . m1(30) # Error : single arguments
#a . m1() # Error : No arguments

output:-
-----------
Two  argument  method :  10 20


#5)Find  outputs  (Home  work)
class   c1:
	def   m1(self):
		print('No  argument  method') # No  argument  method prints
	def   m1(self , x):
		print('Single  argument  method : ' , x) #Replaces  No  argument  method Single  argument  method
	def   m1(self , x = 1  , y = 2):
		print('Two  argument  method : ' , x , y) # Replaces Single  argument  method with Two  argument  method. Atlast it is consider in calling method m1().
# End  of  class  c1
a = c1() # creating object 'a' to class c1()
a . m1(10 , 20) # calling m1() with respect to class c1() with two arguments , here x = 10 and  y = 20
a . m1(30) #calling m1() with respect to class c1() with two arguments , here x = 30 and  y = 2
a . m1() # calling m1() with respect to class c1() with two arguments , here x = 1 and  y = 2

output:-
---------
Two  argument  method :  10 20
Two  argument  method :  30 2
Two  argument  method :  1 2


#6) Find  outputs  (Home  work)
class   c1:
	def   m1(self):
		print('Method  of  first  c1  class') # Method  of  first  c1  class prints
class   c1:
	def   m1(self):
		print('Method  of  second  c1  class') # Replaces Method  of  first  c1  class with Method  of  second  c1  class
class   c1:
	def   m1(self):
		print('Method  of  third  c1  class') # Replaces Method  of  second  c1  class with Method  of  third  c1  class
a = c1() # creating object 'a' to class c1()
a . m1() # calling m1() with respect to class c1() 

output:-
--------
Method  of  third  c1  class


#7)Find  outputs  (Home  work)
class   c1:
	def   m1(self):
		print('Method  of  first  c1  class') # Method  of  first  c1  class prints
class   c1:
	def   m1(self):
		print('Method  of  second  c1  class') # Replaces Method  of  first  c1  class with Method  of  second  c1  class
class   c1:
	pass # Replaces Method  of  second  c1  class with pass i,e., pass returns None 
a = c1() # creating object 'a' to class c1()
#a . m1() #  Error : due to pass returns None 

outputs:-
-------

Nothing is there to print here.


#8) Find  outputs (Home  work)
class  c1:
        pass
# End  of  class
a = c1()
print(a . __dict__) # {} ---> there is no argumenents for 'a'
a . x = 10
print(a . __dict__) # {'x': 10}----> 'a' has single argument x= 10
a . y = 20
print(a . __dict__) # {'x': 10, 'y': 20} # 'a' has two arguments  x= 10 and y = 20
a . x = 30
print(a . __dict__) # {'x': 30, 'y': 20} # 'a' has two arguments  x= 30 and y = 20
a . y = 40
print(a . __dict__) # {'x': 30, 'y': 40} 'a' has two arguments  x= 30 and y = 40
del  a . x
print(a . __dict__) #{ 'y': 40}----->  'a' has single argument  y = 40 and x is deleted
del  a . y
print(a . __dict__) # {} -----> 'a' has No argument  both x and y are deleted
del   a
print(a . __dict__) #Error: There is no 'a' it was deleted 

outputs:-
---------
{}
{'x': 10}
{'x': 10, 'y': 20}
{'x': 30, 'y': 20}
{'x': 30, 'y': 40}
{'y': 40}
{}



#9) (Home  work)
Write  a  program  to  determine  area  and  perimeter  of  triangle  and  represent  triangle  by  an  object

1) What  is  the  area  of  triangle ?  --->  sqrt(s * (s - a) * (s - b) * (s - c))

2) What  is  the  formula  for  's' ?  --->  (a + b + c) / 2

3) What  is  the  perimeter  of  triangle ?  --->  a + b + c


import  math
class  triangle:
	def  get(self):
		self.a = int(input("Enter the side a : :") )
		self.b = int(input("Enter the side b :"))
		self.c = int(input("Enter the side c :"))    #How  to  read  three  sides  into  object  self
	def  test(self):
		if  self.a + self. b > self. c and self.a + self. c > self.b and self.c + self. a> self.a:
			print('Triangle')
			return True # sum  of  every  2  sides  >=  3rd  side:
			#Do  nothing
		else:
			print('Not  a  triangle')
			return False  #	How  to  stop  execution
	def  area(self):
		s = (self.a+self.b+self.c)/2
		area = math . sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))
		return area # area  of  triangle
	def  peri(self):
		peri = self.a + self.b + self.c
		return peri # perimeter  of  triangle
# End of the class
triangle = triangle() #How  to  create  triangle  class  object
triangle.get() #How  to  read  inputs  into  object
if triangle. test():#How  to  test  whether  inputs  are  valid
	print('Area : ', triangle.area ())
	print('Perimeter : ',  triangle.peri())

#10)Find  outputs  (Home  work)

class   c1:
	def  m1(self):
		x = 10
		self . x = 20
		print(x) # 10
		print(self . x) # 20
		x += 5 # x is incremented by 5 --->25
		self . x += 7 #  self . x isincremented by 7 --->27
	def   m2(self):
		#print(x)
		print(self . x)
		self . x += 6
# End  of  the  class
a = c1()
a . m1()
#a . m2()
print(a . x) # 27
#print(self . x)
#print(x)

outputs:-
-----------
10
20
27


#11) (Home  work)
Write  a  program  to  add  two  objects  where  each  object  contains  three  values  and
store  results  in   third  object

1st  object   --->  x = 10 , y = 20 , z = 30

2nd  object --->  x = 40 , y = 50 , z = 60

3rd  object  ---> x = 10 + 40 = 50 , y = 20 + 50 = 70 , z = 30 + 60 = 90

class  Test:
	def   get(self):
		self.x = int(input("Enter x: "))
		self.y = int(input("Enter y: "))
		self.z = int(input("Enter z: ")) # How  to  read  inputs  into  variables  x , y  and  z  of  object  self
	def   add(self , m , n):
		self.x = m.x + n.x
		self.y = m.y + n.y
		self.z = m.z + n.z # How  to  add  objects  m  and  n  and  store  results  in  object  self
	def  disp(self):
		print(f" x={self.x}, y = {self.y} , z = {self.z}") # How  to  print  object  self
# End  of  the  class
a = Test()
b = Test()
c = Test() # How  to  create  three  Test  class  objects  a , b  and  c
print('First  Object')
a.get() # How  to  read  inputs  into  object  'a'
print('Second  Object')
b.get() # How  to  read  inputs  into  object  'b'
print('Second  Object')
c.add(a,b) #How  to  add  objects  a  and  b  and  store  results in  object  'c'
print('Addition  results')
c.disp() # How  to  print  object  'c'

outputs:-
----------
First  Object
Enter x: 3
Enter y: 2
Enter z: 1
Second  Object
Enter x: 4
Enter y: 6
Enter z: 8
Second  Object
Addition  results
 x=7, y = 8 , z = 9


#12)Find  outputs (Home  work)
class  Date:
	pass # Returns pass , if there is no _str_ method in the program so it executes _str_ method of an object , we Type and addressof an object here.
# End of the class
a =  Date()
a . dd = 15
a . mm = 8
a . yy = 1947
print(a) # <__main__.Date object at 0x000001F9B4BC6A50>


#13) Find  outputs (Home  work)
class   c1:
	def  _str_(self):
			return  '25'
class   c2:
	def  _str_(self):
			return   35
class   c3:
	def  _str_(self):
			print('Hyd')
class   c4:
	def  _str_(self , x):
			return   F'{x}'
#end of the class
a = c1()
b = c2()
c = c3()
d = c4()
print(a) # <__main__.c1 object at 0x000002BE13876A50>
print(b) # <__main__.c2 object at 0x000002BE13876BA0>
print(c) # <__main__.c3 object at 0x000002BE13876CF0>
print(d) # <__main__.c4 object at 0x000002BE13876E40>
print(b . _str_()) # 35
print(c . _str_()) # Hyd
print(d . _str_(50)) # None
                       50

outputs:-
----------
<__main__.c1 object at 0x000002BE13876A50>
<__main__.c2 object at 0x000002BE13876BA0>
<__main__.c3 object at 0x000002BE13876CF0>
<__main__.c4 object at 0x000002BE13876E40>
35
Hyd
None
50

