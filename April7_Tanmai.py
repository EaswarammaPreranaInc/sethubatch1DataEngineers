# Identify  error  (Home work)
class   c1: 
	def  m1(self):
		pass
class   c2:
        pass
#class   c3: # error there nothing inside the class atleast write pass

# Find  outputs  (Home  work)
class   c1:
	pass
# End  of  the  class
a = c1()
print(id(a)) # id of object is displayed 
print(type(a)) # c1() or class '__main__.c1'
print(a . __dict__)  #{}
print(a) # Type and address of a 
del  a # deleted object 
#print(a) # error 

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
m1()  #Function 

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
a . m1(10 , 20) # Two argumnet method:  10 20
#a . m1(30) # error
#a . m1()#error 

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
a . m1(30) # Two  argument  method :  30 2
a . m1() # Two  argument  method : 1 2

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
a . m1() #Method  of  third  c1  class 

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
#a . m1() # error  no m1 

#  Find  outputs (Home  work)
class  c1:
        pass
# End  of  class
a = c1()
print(a . __dict__) # {}
a . x = 10
print(a . __dict__) #{x:10}
a . y = 20
print(a . __dict__) #{x:10,y:20}
a . x = 30
print(a . __dict__) #{x:30,y:20}
a . y = 40
print(a . __dict__)#{x:30,y:40}
del  a . x
print(a . __dict__) #{y:40}
del  a . y
print(a . __dict__) #{}
del   a
#print(a . __dict__) # error 

'''  (Home  work)
Write  a  program  to  determine  area  and  perimeter  of  triangle  and  represent  triangle  by  an  object

1) What  is  the  area  of  triangle ?  --->  sqrt(s * (s - a) * (s - b) * (s - c)) # Heron's formula bcz we dont know height of triangle 

2) What  is  the  formula  for  's' ?  --->  (a + b + c) / 2

3) What  is  the  perimeter  of  triangle ?  --->  a + b + c
'''
import  math
class  triangle:
	def  get(self):
		#How  to  read  three  sides  into  object  self
		print("1 st side: ", self.a)
		print("2 nd side: ", self.b)
		print("3 rd side: ", self.c)



	def  test(self):
		#if  sum  of  every  2  sides  >=  3rd  side:
				#Do  nothing
				
					if (self.a+self.b)>self.c and (self.b+self.c)>self.a and (self.c+self.a)>self.b:
						print("Triangle")
					else:
						print('Not  a  triangle')
						exit()
				#How  to  stop  execution
    
	def  area(self):
			s=(self.a+self.b+self.c)/2 # it s a local variable bcz triangle cant have more than 3 variables i.e sides
			return  math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c)) #area  of  triangle
	def  peri(self):
			return  self.a+self.b+self.c  #perimeter  of  triangle
# End of the class
#How  to  create  triangle  class  object
tri=triangle()
tri.a=int(input("Enter is 1st side of triangle: "))
tri.b=int(input("Enter is 2nd side of triangle: "))
tri.c=int(input("Enter is 3rd side of triangle: "))
tri.get()
#How  to  read  inputs  into  object
tri.test()
#How  to  test  whether  inputs  are  valid
print('Area : ',   tri.area())
print('Perimeter : ',  tri.peri()) 

#  Find  outputs  (Home  work)
class   c1:
	def  m1(self):
		x = 10
		self . x = 20
		print(x) # 10
		print(self . x) # 20
		x += 5
		self . x += 7
	def   m2(self):
		#print(x) # error 
		print(self . x)  #27
		self . x += 6  
# End  of  the  class
a = c1() 
a . m1() 
a . m2()
print(a . x) #33
#print(self . x) # error 
#print(x) # error  



#  Find  outputs (Home  work)
class  Date:
	pass
# End of the class
a =  Date() # object is created 
a . dd = 15 # three instance variable of object are created 
a . mm = 8
a . yy = 1947
print(a) # type and address of object 

#  Find  outputs (Home  work)
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
print(a) #25
#print(b) # error 
#print(c) #error print(print(Hyd)) --> print(none)
#print(d) # error 
print(b . __str__()) # 35
print(c . __str__()) # Hyd None
print(d . __str__(50)) # 50

'''  (Home  work)
Write  a  program  to  add  two  objects  where  each  object  contains  three  values  and
store  results  in   third  object

1st  object   --->  x = 10 , y = 20 , z = 30

2nd  object --->  x = 40 , y = 50 , z = 60

3rd  object  ---> x = 10 + 40 = 50 , y = 20 + 50 = 70 , z = 30 + 60 = 90
'''
class  test:
	def   get(self):
		self.x=int(input("Enter a 1 st number: "))
		self.y=int(input("Enter a 2 nd number: "))
		self.z=int(input("Enter a 3 rd number: "))
		# How  to  read  inputs  into  variables  x , y  and  z  of  object  self
	def   add(self , m , n):
		self.x=m.x+n.x
		self.y=m.y+n.y
		self.z=m.z+n.z

		
		 #How  to  add  objects  m  and  n  and  store  results  in  object  self
	def  disp(self):
		 print(self.x)
		 print(self.y)
		 print(self.z)#How  to  print  object  self
# End  of  the  class
a=test()
b=test()
c=test()
#How  to  create  three  Test  class  objects  a , b  and  c
print('First  Object')
a.get()
#How  to  read  inputs  into  object  'a'
print('Second  Object')
b.get()
#How  to  read  inputs  into  object  'b'
#How  to  add  objects  a  and  b  and  store  results in  object  'c'
print('Addition  results')
c.add(a,b)
c.disp()
#How  to  print  object  'c'
