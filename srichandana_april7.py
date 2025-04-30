# Identify  error  (Home work)
class   c1:
	def  m1(self):
		pass
class   c2:
    pass
class   c3:
	pass
	# error as its empty class
# Find  outputs  (Home  work)
class   c1:
	pass
# End  of  the  class
a = c1()
print(id(a))#4357840800
print(type(a))#class '__main__.c1'>
print(a . __dict__)  #empty dict
print(a) # #<__main__.c1 object at 0x103bf5fa0>
del  a 
#print(a) #error
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
a . m1() #"3rd method"
m1() #Function
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
a . m1(10 , 20) #'Two argument method: 10 20'
#a . m1(30)  #errror
#a . m1() #error
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
a . m1(10 , 20) #'Two argument method: 10,20'
a . m1(30) # 'Two  argument  method : ' , 30 , 2
a . m1() #default arg 'Two  argument  method : ' , 1 , 3
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
# a . m1() #error c1' object has no attribute 'm1'
#  Find  outputs (Home  work)
class  c1:
        pass
# End  of  class
a = c1()
print(a . __dict__) #{}
a . x = 10
print(a . __dict__) #{x:10}
a . y = 20
print(a . __dict__)#{x:10,y:20}
a . x = 30
print(a . __dict__) ##{x:30,y:20}
a . y = 40
print(a . __dict__) #{x:30,y:40}
del  a . x
print(a . __dict__)#{y:40}
del  a . y
print(a . __dict__)#{}
del   a
#print(a . __dict__) #error
'''  (Home  work)
Write  a  program  to  determine  area  and  perimeter  of  triangle  and  represent  triangle  by  an  object

1) What  is  the  area  of  triangle ?  --->  sqrt(s * (s - a) * (s - b) * (s - c))

2) What  is  the  formula  for  's' ?  --->  (a + b + c) / 2

3) What  is  the  perimeter  of  triangle ?  --->  a + b + c
'''
import  math
class  triangle:
	
	def  get(self):
		self.a=int(input("enter 1st side "))
		self.b=int(input("enter 2nd side "))
		self.c=int(input("enter 3rd side "))
		
		#How  to  read  three  sides  into  object  self
	def  test(self):
		if  self.a+self.b >=  self.c and self.b+self.c>= self.a and self.c+self.a>=self.b: 
				return 1 #pass
		else:
				print('Not  a  triangle')
				return 0  #pass#How  to  stop  execution
	def  area(self):
		s=(self.a+self.b+self.c)/2
		return math.sqrt(s*(s-self.a)*(s-self.b)*(s-self.c))  
	def  peri(self):
		return  self.a+self.b+self.c #perimeter  of  triangle
# End of the class
k=triangle()#How  to  create  triangle  class  object
k.get()#How  to  read  inputs  into  object
k.test()#How  to  test  whether  inputs  are  valid
if k.test():
	print('Area :',k.area())
#print('Area : ',   ???)
print('Perimeter : ',k.peri())#print('Perimeter : ',  ???)
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

		#print(x)# error
		print(self . x)  #error x not 
		self . x += 6 #erroe
# End  of  the  class
a = c1()
a . m1() #10,20
a . m2() #27
print(a . x) #33
#print(self . x)
#print(x) no global x
'''  (Home  work)
Write  a  program  to  add  two  objects  where  each  object  contains  three  values  and
store  results  in   third  object

1st  object   --->  x = 10 , y = 20 , z = 30

2nd  object --->  x = 40 , y = 50 , z = 60

3rd  object  ---> x = 10 + 40 = 50 , y = 20 + 50 = 70 , z = 30 + 60 = 90
'''
class Test:
    def get(self):
        self.x = int(input("1st number: "))
        self.y = int(input("2nd number: "))
        self.z = int(input("3rd number: "))

    def add(self, m, n):
        self.x = m.x + n.x
        self.y = m.y + n.y
        self.z = m.z + n.z

    def disp(self):
        print("\n", self.x, "\n", self.y, "\n", self.z)

# End of class

# Create objects
m = Test()
print('First Object:')
m.get()

n = Test()
print('Second Object:')
n.get()

# Add and store in third object
c = Test()
print('Addition Results:')
c.add(m, n)
c.disp()

#  Find  outputs (Home  work)
class  Date:
	pass
# End of the class
a =  Date()
a . dd = 15
a . mm = 8
a . yy = 1947
print(a.dd) #<__main__.Date object at 0x1034c9fa0>

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
#print(b) #eror
#print(c) #error none
#print(d) #error doesnt take arg
print(b . __str__()) #35 int
print(c . __str__()) #"hyd" none
print(d . __str__(50)) #50
