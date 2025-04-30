# Identify  error  (Home work)
class   c1:
	def  m1(self):
		pass
class   c2:
        pass
#class   c3: # Error atleast one method is needed or passs

# Find  outputs  (Home  work)
class   c1:
	pass
# End  of  the  class
a = c1() # create object "a" to class c1
print(id(a))# 100234849
print(type(a)) # <class '__main__.c1'> 
#print(a .__dict___) #{}
print(a)# <__main__.c1 object at address>
del  a # delete object a 

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
a = c1()# created object 'a' to class c1
a . m1()#3rd  method
m1()#Function

 #  Find  outputs  (Home  work)
class   c1:
	def   m1(self):
		print('No  argument  method')
	def   m1(self , x):
		print('Single  argument  method : ' , x)
	def   m1(self , x , y):
		print('Two  argument  method : ' , x , y)
# End  of  class  c1
a = c1()# created object 'a' to class c1
a . m1(10 , 20)#Two  argument  method : 10   20
#a . m1(30)# error, one argument is missing
#a . m1()# error,2 argument is missing

 #  Find  outputs  (Home  work)
class   c1:
	def   m1(self):
		print('No  argument  method')
	def   m1(self , x):
		print('Single  argument  method : ' , x)
	def   m1(self , x = 1  , y = 2):
		print('Two  argument  method : ' , x , y)
# End  of  class  c1
a = c1()# created object 'a' to class c1
a . m1(10 , 20)#Two  argument  method : 10   20
a . m1(30)#Two  argument  method : 30   2
a . m1()#Two  argument  method : 1   2

#  Find  outputs (Home  work)
class  c1:
        pass
# End  of  class
a = c1()# Create object "a"
print(a . __dict__)#{}
a . x = 10
print(a . __dict__)#{'x':10}
a . y = 20
print(a . __dict__)#{'x':10,'y':20}
a . x = 30
print(a . __dict__)#{'x':30,'y':20}
a . y = 40
print(a . __dict__)#{'x':30,'y':40}
del  a . x
print(a . __dict__)#{'y':40}
del  a . y
print(a . __dict__)#{}
del   a
# print(a .__dict__)#Error : there is no a object


  
#Write  a  program  to  determine  area  and  perimeter  of  triangle  and  represent  triangle  by  an  object
import  math
class  triangle:
	def  get(self):
		self.a=eval(input("Enter a number: "))
		self.b=eval(input("Enter a number: "))
		self.c=eval(input("Enter a number: "))
	
	def  test(self):
		if  self.a+self.b > self.c and self.b+self.c>self.a and self.a+self.c > self.b:
			pass
		else:
			print("Not  a  triangle")
			exit()
	def area(self):
		s=(self.a +self.b + self.c)/2
		return math.sqrt(s*(s-self.a)*(s-self.b)*(s-self.c))
	def peri(self):
		return self.a+self.b+self.c
obj=triangle()
obj.get()
obj.test()
print('Area : ', obj.area()  )
print('Peri : ', obj.peri()  )


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
		#print(x) # local variable "X" is not defined 
		print(self . x)
		self . x += 6
# End  of  the  class
a = c1() # created object 'a'
a . m1() # 10 <next> 20
a . m2() # 27
print(a . x) #33
#print(self . x)
#print(x) # x is not defined 


#Write  a  program  to  add  two  objects  where  each  object  contains  three  values  and
#store  results  in   third  object

class test:
    
    def get(self):
        self.a=eval(input("Enter a digit : "))
        self.b=eval(input("Enter a digit : "))
        self.c=eval(input("Enter a digit : "))
    def add(self,m,n):
        self.a= m.a+ n.a
        self.b= m.b+ n.b
        self.c= m.c+n.c
        
    def disp(self):
        print('X : ',self.a)  
        print('y : ',self.b)   
        print('z : ',self.c)     

x=test()    
y=test()
z=test()
print("First object ")
x.get()
print("second object ")
y.get()
print('Addition  results')
z.add(x,y)
z.disp()
