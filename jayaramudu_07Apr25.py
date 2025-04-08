#Ex-1
class   c1:
	def  m1(self):
		pass
class   c2:
        pass
class  c3: # Error here because at least statement otherwise we can write pass
    pass

#Ex-2
class   c1:
	pass
# End  of  the  class
a = c1() # create a object
print(id(a)) # address of the object of a
print(type(a)) # class object
print(a . __dict__) # create empty dict
print(a) # print name __main__.c1 and address of a object
del  a # delete object a
#print(a) # a is not define

#Ex-3
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
a = c1() # create a object
a.m1() # call method of class c1 m1
m1() # call a m1 function

#Ex-4
#  Find  outputs  (Home  work)
class   c1:
	def   m1(self):
		print('No  argument  method')
	def   m1(self , x):
		print('Single  argument  method : ' , x)
	def   m1(self , x , y):
		print('Two  argument  method : ' , x , y)
# End  of  class  c1
a = c1() #create a object of class c1
a . m1(10 , 20) # calling m1 method of c1 class
#a .m1(30) # Error because m1 method accept two  PA but only one
#a.m1() # Error because m1 method accept two  PA but empty PA

#Ex-5
#  Find  outputs  (Home  work)
class   c1:
	def   m1(self):
		print('No  argument  method')
	def   m1(self , x):
		print('Single  argument  method : ' , x)
	def   m1(self , x = 1  , y = 2):
		print('Two  argument  method : ' , x , y)
# End  of  class  c1
a = c1() # create a object of class c1
a . m1(10 , 20) # calling m1 method of class c1   # Two  argument  method :  10 20
a .m1(30) # calling m1 method of class c1 # Two  argument  method :  30 2
a.m1() # calling m1 method of class c1 # Two  argument  method :  1 2

#Ex-6
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
a=c1() # create a object of last class of c1
a.m1() # calling m1 of last class of m1 # Method  of  third  c1  class

#Ex-7
# Find  outputs  (Home  work)
class   c1:
	def   m1(self):
		print('Method  of  first  c1  class')
class   c1:
	def   m1(self):
		print('Method  of  second  c1  class')
class   c1:
	pass
a=c1() #  create a object of last class of c1
a.m1() # Error m1 method not present in last class c1

#Ex-7
#  Find  outputs (Home  work)
class  c1:
        pass
# End  of  class
a = c1()
print(a . __dict__) # Empty dict
a . x = 10  # add instance variable x to object
print(a . __dict__) # {'x':10}
a . y = 20  # add instance variable y to object
print(a . __dict__) # {'x':10,'y':20}
a . x = 30 # modifies x value because x already there
print(a . __dict__) # # {'x':30,'y':20}
a . y = 40 #  modifies y value because y already there
print(a . __dict__)  # {'x':30,'y':40}
del  a . x # delete variable x
print(a . __dict__) # {'y':40}
del  a . y  # delete variable y
print(a . __dict__) # empty dict {}
del   a # delete object a
# print(a.__dict__) # Error because object a is not define


#Ex-8
'''  (Home  work)
Write  a  program  to  determine  area  and  perimeter  of  triangle  and  represent  triangle  by  an  object

1) What  is  the  area  of  triangle ?  --->  sqrt(s * (s - a) * (s - b) * (s - c))

2) What  is  the  formula  for  's' ?  --->  (a + b + c) / 2

3) What  is  the  perimeter  of  triangle ?  --->  a + b + c
'''
import math

class triangle:
    def get(self):
        # How  to  read  three  sides  into  object  self
        self.x = eval(input('Enter 1st side: '))
        self.y = eval(input('Enter 2nd side: '))
        self.z = eval(input('Enter 3rd side: '))

    def test(self):
        #  sum  of  every  2  sides  >=  3rd  side
        if self.x + self.y > self.z and self.y + self.z > self.x and self.x + self.z > self.y:
            return True
        else:
            print('Not a triangle')
            return False

    def area(self):
        s = (self.x + self.y + self.z) / 2
        return math.sqrt(s * (s - self.x) * (s - self.y) * (s - self.z))

    def peri(self):
        return self.x + self.y + self.z

# Create an object and use methods
a = triangle()
a.get()

if a.test():
    print('Area:', a.area())
    print('Perimeter:', a.peri())

# #Ex-9
# #  Find  outputs  (Home  work)
# class   c1:
# 	def  m1(self):
# 		x = 10 # LV of m1 method
# 		self . x = 20 # x is instance of variable
# 		print(x) # 10
# 		print(self . x) # 20
# 		x += 5 # 15
# 		self . x += 7 # 27
# 	def   m2(self):
# 		#print(x) # x not define in LV
# 		print(self . x) # x is instance of variable 27
# 		self . x += 6 # 33
# # End  of  the  class
# a = c1()
# a . m1()
# a . m2()
# print(a . x) # 33
# #print(self.x) # Error  because here self not define
# #print(x) # Error because x not define

#Ex-10
'''  (Home  work)
Write  a  program  to  add  two  objects  where  each  object  contains  three  values  and
store  results  in   third  object

1st  object   --->  x = 10 , y = 20 , z = 30

2nd  object --->  x = 40 , y = 50 , z = 60

3rd  object  ---> x = 10 + 40 = 50 , y = 20 + 50 = 70 , z = 30 + 60 = 90
'''
class  Test:

	def   get(self):
		 # How  to  read  inputs  into  variables  x , y  and  z  of  object  self
         self.x = eval(input('Enter 1st value: '))
         self.y = eval(input('Enter 2nd value: '))
         self.z = eval(input('Enter 3rd value: '))

	def   add(self , m , n):
		 # How  to  add  objects  m  and  n  and  store  results  in  object  self
         self.x=(m.x+n.x)
         self.y=m.y+n.y
         self.z=m.z +  n.z

	def  disp(self):
		 # How  to  print  object  self
         print(self.x,self.y,self.z,sep=' ')

# End  of  the  class
a = Test() # How  to  create  three  Test  class  objects  a , b  and  c
print('First  Object')
a.get()  # How  to  read  inputs  into  object  'a'
print('Second  Object')
b =Test()  # How  to  read  inputs  into  object  'b'
b.get()# How  to  add  objects  a  and  b  and  store  results in  object  'c'
print('Addition  results')
c = Test()
c.add(a,b)
c.disp()# How  to  print object 'c'

#Ex-11
#  Find  outputs (Home  work)
class  Date:
	pass
# End of the class
a =  Date()
a . dd = 15
a . mm = 8
a . yy=1947
print(a) # print name (__main__.Date) and address of object a

#Ex-12
#  Find  outputs (Home  work)
class   c1:
	def  __str__(self):
			return  '25'
class   c2:
	def  __str__(self):
			return   35 # ERROR: __str__ must return a string, not int
class   c3:
	def  __str__(self):
			print('Hyd')
class   c4:
	def  __str__(self , x):
			return   F'{x}'
#end of the class
a = c1() # create object of class c1
b = c2()  # create object of class c2
c = c3() # create object of class c3
d = c4() # create object of class c4
print(a)  # print name (__main__.c1) and address of object a # 25
#print(b) # __str__ must return a string, not int
# print(c) # Error: __str__() prints 'Hyd' but returns None
#print(d) # Error because missing PA
print(b . __str__()) # 35
# print(c . __str__()) Erroe because c.__str__ doest not return anything
print(d.__str__(50)) # 50
