# How  to  import  only  variable  'x' ,  functions  add()   and  mul()  and  class  c1  of  cal  module ?  (Home  work)
'''
print('Begin')
import cal  # add , mul  and  class  c1  of  cal  moudle  with  from  statement
print(cal.x) # How  to  print  variable  'x'  of  cal   module
print(cal.y) 
print(cal . x) 
print(cal.add(10 , 7)) #How  to  call  add()  function  of  cal  module  by  passing  10  and  7)
print(cal.sub(10 , 7))
print(cal.mul(10,7)) #How  to  call  mul()  function  of  cal  module  by  passing  10  and  7)
print(cal.div(10 , 7))
a=cal.c1()
a.m1() #How  to  call  m1()  method  of  class  c1  in  cal  module

output:
Begin
100
200
100
17
3
70
1.4285714285714286
m1  method

# Identify  error  (Home work)
class   c1:
	def  m1(self):
		pass
class   c2:
        pass
#class   c3: # after defining the class there should be some arguments


# Find  outputs  (Home  work)
class   c1:
	pass
# End  of  the  class
a = c1()
print(id(a))  # Address of the class cl
print(type(a)) # <class '_main_.c1'>
#print(a . dict)  #  'a' is not defined 
#print(a) #'a' is not defined 
del  a  # 'a' is not defined 
#print(a)  # 'a' is not defined

#  Find  outputs  (Home  work)
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
a = c1() # class is created 
a . m1() # 3rd method
m1() # 'Function

#  Find  outputs  (Home  work)
class   c1:
	def   m1(self):
		print('No  argument  method')
	def   m1(self , x):
		print('Single  argument  method : ' , x)
	def   m1(self , x , y):
		print('Two  argument  method : ' , x , y)
# End  of  class  c1
a = c1()
a . m1(10 , 20) # Two  argument  method 
#a . m1(30)  # only one argument is being passed and y is missing
#a . m1() # there are no arguments and it should be 2 arguments 


# Find  outputs  (Home  work)
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
a . m1() # Method  of  third  c1  class


# Find  outputs  (Home  work)
class   c1:
	def   m1(self):
		print('Method  of  first  c1  class')
class   c1:
	def   m1(self):
		print('Method  of  second  c1  class')
class   c1:
	pass
a = c1()
a . m1() # Error due to class c1 has 0 args


# Find  outputs  (Home  work)
class   c1:
	def   m1(self):
		print('Method  of  first  c1  class')
class   c1:
	def   m1(self):
		print('Method  of  second  c1  class')
class   c1:
	pass
a = c1()
#a . m1() # c1 doesn't have any methods


#  Find  outputs (Home  work)
class  c1:
        pass
# End  of  class
a = c1()
print(a . dict) # creates an empty dictionary{}
a . x = 10
#print(a . dict) # adds an element to the {x:10}
a . y = 20
#print(a . dict) #{x:10, y:20}
a . x = 30
#print(a . dict)  #{x:30, y:20}
a . y = 40
#print(a . dict) #{x:30, y:40}
del  a . x
#print(a . dict) # {y:40}
del  a . y
#print(a . dict) #{}
del   a
#print(a . dict) # object a doesn't exists

'''
Write  a  program  to  determine  area  and  perimeter  of  triangle  and  represent  triangle  by  an  object

1) What  is  the  area  of  triangle ?  --->  sqrt(s * (s - a) * (s - b) * (s - c))

2) What  is  the  formula  for  's' ?  --->  (a + b + c) / 2

3) What  is  the  perimeter  of  triangle ?  --->  a + b + c
'''
import  math
class  triangle:
	def  get(self):
		self.a=eval(input('Enter the first side of the triangle:'))
		self.b=eval(input('Enter the second side of the triangle:'))
		self.c=eval(input('Enter the third side of the triangle:'))
	def  test(self):
		if  self.a+self.b>self.c and self.a+self.c>self.b and self.b+self.c>self.a:
				pass
		else:
			print('Not  a  triangle')
			exit()
	def  area(self):
			s=(self.a+self.b+self.c)/2
			return math.sqrt(s*(self.a)(s-self.b)(s-self.c))
	def  peri(self):
			return  self.a+self.b+self.c
# End of the class
t=triangle()
t.get()
t.test()
print('Area : ',   t.area())
print('Perimeter : ',  t.peri())

output:
Enter the first side of the triangle:5
Enter the second side of the triangle:7
Enter the third side of the triangle:9
Area :  16.60195771588399
Perimeter :  21


#  Find  outputs  (Home  work)
class   c1:
	def  m1(self):
		x = 10
		self . x = 20
		print(x)
		print(self . x)
		x += 5
		self . x += 7
	def   m2(self):
		print(x)
		print(self . x)
		self . x += 6
# End  of  the  class
a = c1()
a . m1() # 10 <nextline> 20
#a . m2() 
print(a . x) # 27
#print(self . x)
#print(x)  #  x is not defined

'''
Write  a  program  to  add  two  objects  where  each  object  contains  three  values  and
store  results  in   third  object

1st  object   --->  x = 10 , y = 20 , z = 30

2nd  object --->  x = 40 , y = 50 , z = 60

3rd  object  ---> x = 10 + 40 = 50 , y = 20 + 50 = 70 , z = 30 + 60 = 90

class  Test:
	def   get(self):
		 self.x=int(input('Enter the value of x:'))
		 self.y=int(input('Enter the value of y:'))
		 self.z=int(input('Enter the value of z:'))
	def   add(self , m , n):
		self.x=m.x+n.x
		self.y=m.y+n.y
		self.z=m.z+n.z # How  to  add  objects  m  and  n  and  store  results  in  object  self
	def  disp(self):
		 print((f"x = {self.x}, y = {self.y}, z = {self.z}"))
# End  of  the  class
a = Test()
b = Test()
c = Test() # How  to  create  three  Test  class  objects  a , b  and  c
print('First  Object')
a.get() # How  to  read  inputs  into  object  'a'
print('Second  Object')
b.get() #How  to  read  inputs  into  object  'b'
c.add(a,b) # How  to  add  objects  a  and  b  and  store  results in  object  'c'
print('Addition  results')
c.disp() #How  to  print  object  'c'

output:
First  Object
Enter the value of x:10
Enter the value of y:20
Enter the value of z:30
Second  Object
Enter the value of x:40
Enter the value of y:50
Enter the value of z:60
Addition  results
x = 50, y = 70, z = 90
'''

#  Find  outputs (Home  work)
class  Date:
	pass
# End of the class
a =  Date()
a . dd = 15
a . mm = 8
a . yy = 1947
print(a) # address of date object


#  Find  outputs (Home  work)
class   c1:
	def  str(self):
			return  '25'
class   c2:
	def  str(self):
			return   35
class   c3:
	def  str(self):
			print('Hyd')
class   c4:
	def  str(self , x):
			return   F'{x}'
#end of the class
a = c1()
b = c2()
c = c3()
d = c4()
print(a) # address of '_main_.c1'
print(b)  # address of '_main_.c2'
print(c)  # address of '_main_.c3'
print(d)  # address of '_main_.c4'
print(b . str()) # 35
print(c . str()) # hyd
print(d . str(50)) # None <next line> 50

