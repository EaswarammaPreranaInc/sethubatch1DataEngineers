Q1 #Identify  error  (Home work)
class   c1:
	def  m1(self):
		pass
class   c2:
        pass
class   c3:     #Indentation error - inside class something has to be written
#-----------------------------------------------------------------------------------------
Q2 #Find  outputs  (Home  work)
class   c1:
	pass
# End  of  the  class
a = c1() 
print(id(a))      #2313716984400
print(type(a))    #<class '____main____.c1'>
print(a . ____dict____) #{}
print(a)          #<____main____.c1 object at 0x0000021AB4476A50>
del  a
print(a)          #error - object a is deleted
#----------------------------------------------------------------------------------------
Q3 #Find  outputs
def   m1():
		print('Function')
class   c1:
	def   m1(self):
		print('1st  method')
	def   m1(self):
		print('2nd  method')
	def   m1(self):
		print('3rd  method')
# End  of  class  c1
a = c1()  
a . m1() #3rd method
m1()     #Function
#------------------------------------------------------------------------------------
Q4 #Find  outputs  (Home  work)
class   c1:
	def   m1(self):
		print('No  argument  method')
	def   m1(self , x):
		print('Single  argument  method : ' , x)
	def   m1(self , x , y):
		print('Two  argument  method : ' , x , y)
# End  of  class  c1
a = c1()
a . m1(10 , 20) # Two  argument  method :  10 20
#a . m1(30) #error - argument for y is not given 
#a . m1()   #error - x, y arguments are not given
#--------------------------------------------------------------------------------
Q5 #Find  outputs  (Home  work)
class   c1:
	def   m1(self):
		print('No  argument  method')
	def   m1(self , x):
		print('Single  argument  method : ' , x)
	def   m1(self , x = 1  , y = 2):
		print('Two  argument  method : ' , x , y)
# End  of  class  c1
a = c1()
a . m1(10 , 20) #Two  argument  method :  10 20
a . m1(30)      #Two  argument  method :  30 2
a . m1()        #Two  argument  method :  1 2
#-------------------------------------------------------------------------
Q6 #Find  outputs  (Home  work)
class   c1:
	def   m1(self):
		print('Method  of  first  c1  class')
class   c1:
	def   m1(self):
		print('Method  of  second  c1  class')
class   c1:
	def   m1(self):
		print('Method  of  third  c1  class')
a = c1()
a . m1()  #Method  of  third  c1  class
#-------------------------------------------------------------------
Q7 #Find  outputs  (Home  work)
class   c1:
	def   m1(self):
		print('Method  of  first  c1  class')
class   c1:
	def   m1(self):
		print('Method  of  second  c1  class')
class   c1:
	pass
a = c1()
a . m1() # error - class c1 does not have m1 method
#-------------------------------------------------------------------
Q8 #Find  outputs
class  c1:
        pass
# End  of  class
a = c1()
print(a . __dict__) #{}
a . x = 10
print(a . __dict__) #{'x' : 10}
a . y = 20
print(a . __dict__) #{'x' : 10,'y' : 20}
a . x = 30
print(a . __dict__) #{'x' : 30,'y' : 20}
a . y = 40
print(a . __dict__) #{'x' : 30,'y' : 40}
del  a . x
print(a . __dict__) #{'y' : 40}
del  a . y
print(a . __dict__) #{}
del   a
#print(a . __dict__) #error - object a is deleted
#-----------------------------------------------------------------------------------------------------------------
Q9 #Write  a  program  to  determine  area  and  perimeter  of  triangle  and  represent  triangle  by  an  object

1) What  is  the  area  of  triangle ?  --->  sqrt(s * (s - a) * (s - b) * (s - c))
2) What  is  the  formula  for  's' ?  --->  (a + b + c) / 2
3) What  is  the  perimeter  of  triangle ?  --->  a + b + c

import  math
class  triangle:
	def  get(self):
		self.a = float(input("Enter side a: "))   #How to read three sides into object self
		self.b = float(input("Enter side b: "))
		self.c = float(input("Enter side c: "))  
	def  test(self):
		if (self.a + self.b > self.c and self.b + self.c > self.a and self.a + self.c > self.b):
			pass
		else:
			print('Not  a  triangle')
			exit()         #How  to  stop  execution
	def  area(self):
		s=(self.a+self.b+self.c)/2
		return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))       #return   area  of  triangle
	def  peri(self):
		return self.a + self.b + self.c                                        #return  perimeter  of  triangle
# End of the class
if __name__ == "__main__":
	x=triangle()     #How  to  create  triangle  class  object
	x.get()          #How  to  read  inputs  into  object
	x.test()         #How  to  test  whether  inputs  are  valid
	print('Area : ',   x.area())
	print('Perimeter : ',  x.peri())

OP-
Enter side a: 3
Enter side b: 4
Enter side c: 5
Area :  6.0
Perimeter :  12.0

Enter side a: 5
Enter side b: 4
Enter side c: 1
Not  a  triangle
#----------------------------------------------------------------------------
Q10 #Find  outputs
class   c1:
	def  m1(self):
		x = 10
		self . x = 20
		print(x)          #10
		print(self . x)   #20
		x += 5          
		self . x += 7
	def   m2(self):
		#print(x)         #error - x is not defined inside m2() method
		print(self . x)   #27
		self . x += 6   
# End  of  the  class
a = c1()
a . m1()
a . m2()
print(a . x) #33
#print(self . x)           #error - self is not defined outside function
print(x)                   #error - no global variable x 
#------------------------------------------------------------------------------------------------------------------------------
Q11 #Write  a  program  to  add  two  objects  where  each  object  contains  three  values  and store  results  in   third  object

1st  object   --->  x = 10 , y = 20 , z = 30
2nd  object --->  x = 40 , y = 50 , z = 60
3rd  object  ---> x = 10 + 40 = 50 , y = 20 + 50 = 70 , z = 30 + 60 = 90

class  Test:
	def   get(self):
		#How  to  read  inputs  into  variables  x , y  and  z  of  object  self
		self.x=int(input('Enter x: '))
		self.y=int(input('Enter y: '))
		self.z=int(input('Enter z: '))
	def   add(self , m , n):
		#How  to  add  objects  m  and  n  and  store  results  in  object  self
		c.x=a.x+b.x
		c.y=a.y+b.y
		c.z=a.z+b.z
	def  disp(self):
		#How  to  print  object  self
		print(f'x={c.x} , y={c.y} , z={c.z}')
# End  of  the  class
#How  to  create  three  Test  class  objects  a , b  and  c
a=Test()
b=Test()
c=Test()
print('First  Object')
a.get()    #How  to  read  inputs  into  object  'a'
print('Second  Object')
b.get()    #How  to  read  inputs  into  object  'b'
c.add(a,b) #How  to  add  objects  a  and  b  and  store  results in  object  'c'
print('Addition  results')
c.disp()    #How  to  print  object  'c'

OP-
First  Object
Enter x: 1
Enter y: 2
Enter z: 3
Second  Object
Enter x: 4
Enter y: 5
Enter z: 6
Addition  results
x=5 , y=7 , z=9
#----------------------------------------------------------------------------------------------------
Q12 #Find  outputs (Home  work)
class  Date:
	pass
# End of the class
a =  Date()
a . dd = 15
a . mm = 8
a . yy = 1947
print(a)  #<__main__.Date object at 0x000001E880DA6A50>
#-------------------------------------------------------------
Q13 #Find  outputs (Home  work)
class   c1:
	def  __str__(self):
			return  '25'
class   c2:
	def  __str__(self):
			return   35
class   c3:
	def  __str__(self):
			print('Hyd')
class   c4:
	def  __str__(self , x):
			return   F'{x}'
#end of the class
a = c1()
b = c2()
c = c3()
d = c4()
print(a)  #25
#print(b)  #error - must return string object but int 35 is returned
#print(c)  #Error -  must return string object but None is returned
#print(d)   #error - argument for x is not given
print(b . __str__()) #35
print(c . __str__()) # Hyd <next line> None
print(d . __str__(50)) #50
