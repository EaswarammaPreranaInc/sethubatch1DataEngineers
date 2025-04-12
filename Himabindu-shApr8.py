'''# Identify  error  (Home work)
class   c1:  
	def  m1(self):
		pass
class   c2:  # empty class
        pass
class   c3: # error
'''

'''
# Find  outputs  (Home  work)
class   c1:
	pass
# End  of  the  class
a = c1()  # creat the class object i.e 'a'
print(id(a)) # prints the address of the object 'a'
print(type(a)) # print type of object 'a' i.e <class '_main_.c1'>
print(a . _dict_)  # empty dict i.e {}
print(a) # print type and address of the object of 'a' it means return the _str_ of class object
del  a # remove the object class object 'a'
print(a) # error 
'''


'''
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
a = c1()
a . m1() # 3rd method
m1() # function 
'''

'''
#  Find  outputs  (Home  work)
class   c1:
	def   m1(self):
		print('No  argument  method')
	def   m1(self , x):
		print('Single  argument  method : ' , x)
	def   m1(self , x , y):
		print('Two  argument  method : ' , x , y)
# End  of  class  c1
a = c1() # create object 'a' of c1 class
a . m1(10 , 20) # Two  argument  method :  10  20
a . m1(30)  # error missing argument 'y'
a . m1() # error missing two arguments of 'x' and 'y'
'''

'''
#  Find  outputs  (Home  work)
class   c1:
	def   m1(self):
		print('No  argument  method')
	def   m1(self , x):
		print('Single  argument  method : ' , x)
	def   m1(self , x = 1  , y = 2):
		print('Two  argument  method : ' , x , y)
# End  of  class  c1
a = c1()
a . m1(10 , 20) # Two  argument  method : 10 20
a . m1(30) # Two  argument  method : 30 2
a . m1() # Two  argument  method : 1 2
'''


'''
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
'''

'''
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
a . m1() # error c1 class object has no attribute m1
'''

'''
#  Find  outputs (Home  work)
class  c1:
        pass
# End  of  class
a = c1()
print(a . _dict_) # {}
a . x = 10
print(a . _dict_) # {'x':10}
a . y = 20
print(a . _dict_) # {'x':10 , 'y':20}
a . x = 30
print(a . _dict_) # {'x':30 , 'y':20}
a . y = 40
print(a . _dict_) # {'x':30 , 'y':40}
del  a . x
print(a . _dict_) # {'y':40}
del  a . y
print(a . _dict_) # {}
del   a
#print(a . _dict_) # error
'''


'''  (Home  work)
Write  a  program  to  determine  area  and  perimeter  of  triangle  and  represent  triangle  by  an  object

1) What  is  the  area  of  triangle ?  --->  sqrt(s * (s - a) * (s - b) * (s - c))

2) What  is  the  formula  for  's' ?  --->  (a + b + c) / 2

3) What  is  the  perimeter  of  triangle ?  --->  a + b + c

import  math
class  triangle:
	def  get(self):
		print('a:',self.a)
		print('b:',self.b)
		print('c:',self.c)
	def  test(self):
		if  self.a+self.b>=self.c and self.b+self.c>=self.a and self.c+self.a>=self.b:
			return True
		else:
			print('Not  a  triangle')
			return False

	def  area(self):
			x = (self.a + self.b + self.c) / 2
			return math.sqrt(x * (x - self.a) * (x - self.b) * (x - self.c))
	def  peri(self):
			return  self.a+self.b+self.c
# End of the class
s=triangle()  #How  to  create  triangle  class  object
s.a=int(input())
s.b=int(input())
s.c=int(input())  #How  to  read  inputs  into  object
s.get() 
if s.test():#How  to  test  whether  inputs  are  valid
	print('Area : ',  s.area())
	print('Perimeter : ',  s.peri())
'''

'''
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
		#print(x)  # error no local x here
		print(self . x)
		self . x += 6
# End  of  the  class
a = c1()
a . m1() # 10 <nextline> 20
a . m2() # 27
print(a . x) # 33
#print(self . x) # self is not abject here not define self
#print(x) # x is not defined
'''

'''  (Home  work)
Write  a  program  to  add  two  objects  where  each  object  contains  three  values  and
store  results  in   third  object

1st  object   --->  x = 10 , y = 20 , z = 30

2nd  object --->  x = 40 , y = 50 , z = 60

3rd  object  ---> x = 10 + 40 = 50 , y = 20 + 50 = 70 , z = 30 + 60 = 90

class  Test:
	def   get(self):
		 self.x=float(input()) 
		 self.y=float(input()) 
		 self.z=float(input()) #How  to  read  inputs  into  variables  x , y  and  z  of  object  self
	def   add(self , m , n):
		 self.x=m.x+n.x
		 self.y=m.y+n.y
		 self.z=m.z+n.z #How  to  add  objects  m  and  n  and  store  results  in  object  self
	def  disp(self):
		 print(f'x={self.x},y={self.y},z={self.z}')
# End  of  the  class
a=Test() 
b=Test()
c=Test()  #How  to  create  three  Test  class  objects  a , b  and  c
print('First  Object')
a.get() #How  to  read  inputs  into  object  'a'
print('Second  Object')
b.get()  #How  to  read  inputs  into  object  'b'
c.add(a,b)  #How  to  add  objects  a  and  b  and  store  results in  object  'c'
print('Addition  results')
c.disp() #How  to  print  object  'c'

'''

'''
#  Find  outputs (Home  work)
class  Date:
	pass
# End of the class
a =  Date()
a . dd = 15
a . mm = 8
a . yy = 1947
print(a) # print type and address of the object 'a' i.e <_main_.Date object at 0x00000270CC336CF0>
'''

'''
#  Find  outputs (Home  work)
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
print(a) # 25
#print(b) # error
#print(c) # error return None so error
#print(d) # error
print(b . _str_()) # 35
print(c . _str_()) # None
print(d . _str_(50)) # 50
'''
