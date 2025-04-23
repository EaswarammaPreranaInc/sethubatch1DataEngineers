# Find  outputs (Home  work)
class c1:
    x = 10
    def __init__(self):
	    self . y = 20
a = c1() # a.y=20
b = c1() # b.y=20
a . x += 1 # modifies a.x =11
b . y += 1 # y=21
print(a . x) #11
print(a . y) #20
print(b . x) #10
print(b . y) #21
print(c1 . x) #10
print(a . __dict__) #{y:20,x:11}
print(b . __dict__) # {y=21}
print(c1 . __dict__) #{x:10}

# Find  outputs (Home  work)
class  c1:
	x = 10
	def  m1(self):
		self . x = 20
a = c1() 
a . m1()
print(c1 . x) #10
print(a . x) #20 

# Find  outputs  (Home  work)
class   c1:
	x = 10
	def  __init__(self):
		self . y = 20
	@classmethod
	def   m1(cls):
		cls . x = 30
		cls . y = 40
# End  of  the  class
a = c1() # a.y=20
b = c1() #  b.y=20
c1 . m1()
print(a . x) #30
print(a . y) #20
print(b . x) #30
print(b . y) # 20
print(c1 . x , c1 . y) # 30,40
#print(cls . x , cls . y) # error
#print(self . x , self . y) # error 

#  Find  outputs
class   c1:
	@staticmethod
	def   m1(self):
		print(self)
#  End  of  the   class
c1 . m1(25) # 25
a = c1()
a . m1(35) # 35

#  Find  outputs
class   c1:
	def   m1(self):
		print(self)
#  End  of  the   class
c1 . m1(25)  # 25
a = c1()   
a . m1() # <__main__.c1 object at 0x000002476F746BA0>
#a . m1(35) #  c1.m1() takes 1 positional argument but 2 were given 

#  Find  outputs
class   c1:
	@staticmethod
	def   m1(self):
		print('static  method')
		print(self)
	def   m1(self):
		print('instance  method')
		print(self)
#  End  of  the   class
c1 . m1(25) # 25
a = c1()
a . m1() # type n address
'''
instance  method
25
instance  method
<__main__.c1 object at 0x0000024145A46A50>'''  

# How  to  access  static  variable  in  different  ways  ?
class   c1:
	x = 25
	def   __init__(self):
		print(c1.x)
		print(x)
		#How  to  print  static  variable  'x'
		#How  to  print  static  variable  'x'  in  another  way
		print(x) #25
	def   m1(self):
		print(c1.x)
		print(x)

		#How  to  print  static  variable  'x'
		#How  to  print  static  variable  'x'  in  another  way
		print(cls . x) # error
	@classmethod
	def   m2(cls):
		print(c1.x)
		print(cls . x)
		#How  to  print  static  variable  'x'
		#How  to  print  static  variable  'x'  in  another  way
		print(self . x) # error 
	@staticmethod
	def   m3():
		#How  to  print  static  variable  'x'
		print(cls . x) # error 
		print(self . x) # error 
# End  of  the  class
#How  to  print  static  variable  'x'
#How  to  print  static  variable  'x'  in  another  way
#print(x) #25
#print(self . x) # error 
#print(cls . x) # error 
#How  to  call  method  m1()
a=c1()
a.m1()
#How  to  call  method  m2()
c1.m2()
#How  to  call  method  m3()
c1.m3() """
"""
# How  to  add  static  variable  to  the  class  at  different  locations  of  the  program ?
class   c1:
	How  to  add  static  variable  'a'  with  value  10
	def    _init_(self):
		How  to  add  static  variable  'b'  with  value  20
		How  to  add  instance  variable  'c'  with  value  30
		cls . k = 25
	def   m1(self):
		How  to  add  static  variable  'd'  with  value  40
		How  to  add  instance  variable  'e'  with  value  50
	@classmethod
	def   m2(cls):
		How  to  add  static  variable  'f'  with  value  60
		How  to  add  static  variable  'g'  with  value  70  in  another  way
		self . k = 25
	@staticmethod
	def   m3():
		How  to  add  static  variable  'h'  with  value  80
		self . k = 25
		cls . k = 35
#End  of  the  class
print('Begin')
print(c1 . _dict_)
print()
print()
x = c1()
print('Constructor')
print(c1 . _dict_)
print()
print()
How  to  call  m1()  method
print('Instance  method  m1')
print(c1 ._dict_)
print()
print()
How  to  call  m2()  method
print('class  method   m2')
print(c1 . _dict_)
print()
print()
How  to  call  m3()  method
print('static   method   m3')
print(c1 . _dict_)
print()
print()
How  to  add  static  variable  'i'  with  value  90
How  to  add  instance  variable  'j'  with  value  100
print('Outside  the  class')
print(c1 . _dict_)
print()
print()
print("Object  'x' ")
print(x . _dict_)

# Find  outputs  (Home  work)
class  c1:
        a , b , c  = range(1 , 4)
# End  of  the  class
#How  to  print  variable  'a'
#How  to  print  variable  'b'
#How  to  print  variable  'c'
print(c1.a)
print(c1.b)
print(c1.c) 


# What  are  the  outputs  if  inputs  are  10 , 20 , 30 , 40 , 50 , 60 , 70 (Home  work)
class   Test:
	@classmethod
	def  get1(cls):
		cls . x = int(input('Enter  any  number    :  '))
	def  get2(self):
		self . y = int(input('Enter  any  number  :  '))
		self . z = int(input('Enter  any  number  :  '))
	def   compute(self):
		Test . x += 1 # test. x = test.x+1 --> 11
		self . y  += 1
		self . z  += 1
		self . x  += 1
	def    disp(self):
		print(Test . x , self . y , self . z ,  self . x , sep = '\t')
# End  of  the  class
Test . get1() # static x =10 
a = Test()
b = Test()
c = Test()
a . get2() # a.y=20 a.z=30 
b . get2() # b.y=40 b.z=50
c . get2() # c.y=60 c.z=70
a . compute() # static x= 11 a.y =21 z=31 a.x=12
b . compute() # static 12 b.y=41 z=51 a.x=13 
c . compute() #  static 13 c.y=61 z=71 a.x= 14 
a . disp() # 
b . disp()
c . disp()
'''
Enter  any  number    :  10
Enter  any  number  :  20
Enter  any  number  :  30
Enter  any  number  :  40
Enter  any  number  :  50
Enter  any  number  :  60
Enter  any  number  :  70
13      21      31      12
13      41      51      13
13      61      71      14''' 

'''
Write  a  program  to  add  two  Vector  objects

1) What  are  the  names  of  objects ?  ---> x , y   and  z

2) What  are  the  names  of   lists  held  by  each  object ?  --->  x .  a , y . a  , z . a

3) How  to  access  elements  of  1st  list ?  --->  x . a[i]
    How  to  access  elements  of  2nd  list ?  --->  y . a[i]

4) How  to  access  static  variable  'n' ?  --->  vector . n
'''
class  vector:
	@staticmethod
	def get1():
		vector.n=int(input("Enter number of elements: "))
		#How  to  read  number  of  elements  into  variable  'n'
	def get2(self):
		self.a=eval(input("Enter a list: "))

		# How  to  read  the  list  into  the  object
	def add(self , x , y):
		self.a=[]
		for i in range(vector.n):
			self.a.append(x.a[i]+y.a[i])
		#How  add  the  lists  held  by  objects  'x'  and  'y'  and  store  the  results  in  list  held  by  owner  object
vector.get1()
# How  to  call  get1()  method
x=vector()
x.get2()
y=vector()
y.get2()
#How  to  read  the  list  into  1st  object
#How  to  read  the  list  into  2nd  object  'b'
z=vector()
z.add(x,y)
#How  to  add  the  lists  held  by  objects  'a'  and  'b'  and  store  the  results  in  list  of  3rd  object  'c'
#How  to  print  the  list  of  3rd   object
print(z.a)    

'''
Write  a  program  to  print  only  static  variables  but  not  environment  variables  of   classname . __dict__

Hint:  Use  startswith()  and  endswith()  methods
'''
class  c1:
	x = 1
	y = 2
	z = 3
#  End  of  the  class

d=[]
#print(c1.__dict__)
for x in c1.__dict__:
	if x.startswith('__') and x.endswith('__'):
		pass
	else:
		d.append(x)
print(d)


# What  are  k , l ,  x , y , z , m , n , p , q , s ?  (Home  work)
class   c1:
	x = 10  #  What  is  variable  'x'  ---> static variable 
	def    m1(self):
		self . y = 20   #  What  is  variable  'y'  ---> instance variable 
		z = 30   #  What  is  variable   'z'  ---> local 
		c1 . m = 40   #  What  is  variable   'm'  ---> static variable
#end of the class
def    f1():
	a = c1() # object is created 
	a . p = 50   #  What  is   variable  'p'  ---> instance variable
	c1 . q = 60   #  What  is  variable   'q'  ---> static variable 
	s = 70   #  What  is  variable   's'  ---> local variable of function  
#end of the function
k = 80   #  What  is  variable 'k'  ---> global variable  
c1 . l = 90   #  What  is  variable  'l'  ---> static variable 
b = c1()
b . n = 100   #  What  is  variable  'n' ---> instance variable 

