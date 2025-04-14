'''  (Home  work)
Write  a  program  to  determine  area  and  perimeter  of  triangle  and  represent  triangle  by  an  object

1) What  is  the  area  of  triangle ?  --->  sqrt(s * (s - a) * (s - b) * (s - c))

2) What  is  the  formula  for  's' ?  --->  (a + b + c) / 2

3) What  is  the  perimeter  of  triangle ?  --->  a + b + c
'''
import  math
class  triangle:
    def  get(self):
        self.a = int(input("Enter first side: "))
        self.b = int(input("Enter second side: "))
        self.c = int(input("Enter third side: "))
        # How  to  read  three  sides  into  object  self
    def  test(self):
        if (self.a+self.b>self.c)and (self.b+self.c>self.a)and (self.c+self.a>self.b):
            pass
        # if  sum  of  every  2  sides  >=  3rd  side:
        # 		Do  nothing
        else:
                print('Not  a  triangle')
                exit()
                # How  to  stop  execution
    def  area(self):
        s = (self.a+self.b+self.c)/2
        return math.sqrt((s * (s - self.a) * (s - self.b) * (s - self.c)))
    def  peri(self):
        return self.a+self.b+self.c
# End of the class
z = triangle()
z.get()
z.test()

# How  to  create  triangle  class  object


# How  to  read  inputs  into  object
# How  to  test  whether  inputs  are  valid
print('Area : ',   z.area())
print('Perimeter : ', z.peri())

'''  (Home  work)
Write  a  program  to  add  two  objects  where  each  object  contains  three  values  and
store  results  in   third  object

1st  object   --->  x = 10 , y = 20 , z = 30

2nd  object --->  x = 40 , y = 50 , z = 60

3rd  object  ---> x = 10 + 40 = 50 , y = 20 + 50 = 70 , z = 30 + 60 = 90
'''
class  Test:
    def   get(self):
        self.a=  int(input("Enter a :"))
        self.b = int(input("Enter b :"))
        self.c = int(input("Enter c :"))
         # How  to  read  inputs  into  variables  x , y  and  z  of  object  self
    def   add(self , m , n):
        self.a = m.a+n.a
        self.b=m.b+n.b
        self.c=m.c+n.c
         # How  to  add  objects  m  and  n  and  store  results  in  object  self
    def  disp(self):
        print(f"a={self.a} b={self.b} c={self.c}")
         # How  to  print  object  self
# End  of  the  class
a= Test()
b =Test()
c =Test()
# How  to  create  three  Test  class  objects  a , b  and  c
print('First  Object')
a.get()
# How  to  read  inputs  into  object  'a'
print('Second  Object')
b.get()
# How  to  read  inputs  into  object  'b'
c.add(a,b)
# How  to  add  objects  a  and  b  and  store  results in  object  'c'
print('Addition  results')
# How  to  print  object  'c'
c.disp()

# Identify  error  (Home work)
class   c1:
    def  m1(self):
        pass
class   c2:
        pass
class   c3:
# class is empty

# Find  outputs  (Home  work)
class c1:
    pass


# End  of  the  class
a = c1()
print(id(a))
print(type(a))
print(a.__dict__)
# print(a)
# del  a
# print(a)
'''
1779267697840
<class '__main__.c1'>
{}
<__main__.c1 object at 0x0000019E449E7CB0>'''

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
a . m1()
m1()
'''
3rd method 
Function'''

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
a . m1(10 , 20)
# a . m1(30)
# a . m1()
'''
Two  argument  method :  10 20'''

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
a . m1(10 , 20)
a . m1(30)
a . m1()
'''
Two  argument  method :  10 20
Two  argument  method :  30 2
Two  argument  method :  1 2'''

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
a . m1()
'''
latest one: Method  of  third  c1  class'''

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
a . m1()
'''
latest class doesnt have method to call'''


#  Find  outputs (Home  work)
class  c1:
        pass
# End  of  class
a = c1()
print(a . __dict__)
a . x = 10
print(a . __dict__)
a . y = 20
print(a . __dict__)
a . x = 30
print(a . __dict__)
a . y = 40
print(a . __dict__)
del  a . x
print(a . __dict__)
del  a . y
print(a . __dict__)
del   a
print(a . __dict__)
'''
{}
{'x': 10}
{'x': 10, 'y': 20}
{'x': 30, 'y': 20}
{'x': 30, 'y': 40}
{'y': 40}
{}
error'''

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
a . m1()
a . m2()
print(a . x)
print(self . x)
print(x)
'''
10 
20 
error'''

#  Find  outputs (Home  work)
class  Date:
	pass
# End of the class
a =  Date()
a . dd = 15
a . mm = 8
a . yy = 1947
print(a)
'''
type and address'''

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
print(a)
# print(b)
# print(c)
# print(d)
print(b . __str__())
print(c . __str__())
print(d . __str__(50))
'''
25 
error
error
no x value
35 
Hyd
None 
50
'''
