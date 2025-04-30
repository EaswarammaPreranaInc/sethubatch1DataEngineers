#Find outputs
class c1:
	pass
class c2(c1):
	pass
#End of the class
print(issubclass(c2,c1))      #True
print(issubclass(int,float))  #False
print(issubclass(str,object)) #True
print(issubclass(c1,object))  #True
print(issubclass(c2,object))  #True
a=c1()
b=c2()
print(issubclass(b,a))        #Error (1st arg should be class)
print(issubclass(c2,a))       #Error (2nd arg should be class/tuple of classes)



#Find outputs
class c1:
	pass
class c2(c1):
	pass
class c3(c2):
	pass
class c4(c3):
	pass
print(issubclass(c4,c3))  #True
print(issubclass(c4,c2))  #True
print(issubclass(c4,c1))  #True
print(issubclass(c4,object)) #True
print(issubclass(c4,(int,float,str,bool)))    #False
print(issubclass(c4,(int,float,c1,str,bool))) #True
print(issubclass(c4,[int,float,c1,str,bool])) #Error due to list



#Find outputs
class c1:
	pass
class c2(c1):
	pass
class c3(c2):
	pass
class c4:
	pass
print(isinstance(25,int))       #True
print(isinstance(10.8,float))   #True
print(isinstance('Hyd',str))    #True
print(isinstance(3+4j,complex)) #True
print(isinstance(True,bool))    #True
print(isinstance(True,int))     #True
print(isinstance('True',str))   #True
print(isinstance(True,str))     #False
print()
a=c3()
print(isinstance(a,c3))         #True
print(isinstance(a,c2))         #True
print(isinstance(a,c1))         #True
print(isinstance(a,object))     #True
print(isinstance(a,c4))         #False
print(isinstance(a,(int,float,str,bool)))     #False
print(isinstance(a,(int,float,c3,str,bool)))  #True
print(isinstance(a,(int,float,c1,str,bool)))  #True
print(isinstance(a,[int,float,c3,str,bool]))  #Error due to list



#Multilevel inheritance demo program
class A:
	def m1(self):
		print('class A method')
class B(A):
	def m1(self):
		print('class B method')
class C(B):
	def m1(self):
		print('class C method')
class D(C):
	def m1(self):
		print('class D method')
		super().m1() #How to call method m1() of class C
		super(D,D()).m1() #How to call method m1() of class C in another way
		super(D,self).m1()#How to call method m1() of class C in one more way
		super(C,C()).m1() #How to call method m1() of class B
		super(C,self).m1() #How to call method m1() of class B in another way
		super(B,B()).m1() #How to call method m1() of class A
		super(B,self).m1() #How to call method m1() of class A in another way
		#super(A,self).m1() #Error : no m1() in object class
		#super(C).m1() #Error : one more arg is missing
a=D()
a.m1() #How to call method m1() of class D



#Find outputs
class father:
	def height(self):
		print('Father Height')
class mother:
	def color(self):
		print('Mother Color')
class child(mother,father):
	def qualification(self):
		print('Child Qualifiication')
c=child()
c.qualification() #Child Qualifiication
c.color()  #Mother Color
c.height() #Father Height
c.m1()     #Error : no m1() in child class



#Find outputs
class uncle:
	def m1(self):
		print('Uncle Method')
class mother:
	def m1(self):
		print('Mother Method')
class father:
	def m1(self):
		print('Father Method')
class child(father,mother,uncle):
	def m1(self):
		print('Child Method')
c=child()
c.m1()  #Child Method



#Find outputs
class uncle:
	def m1(self):
		print('Uncle Method')
class mother:
	def m1(self):
		print('Mother Method')
class father:
	def m1(self):
		print('Father Method')
class child(father,mother,uncle):
	pass
c=child()
c.m1()  #Father Method



#Find outputs
class uncle:
	def m1(self):
		print('Uncle Method')
class mother:
	def m1(self):
		print('Mother Method')
class father:
	pass
class child(father,mother,uncle):
	pass
c=child()
c.m1()  #Mother Method



#Find outputs
class uncle:
	def m1(self):
		print('Uncle Method')
class mother:
	pass
class father:
	pass
class child(father,mother,uncle):
	pass
c=child()
c.m1()  #Uncle Method



#Find outputs
class uncle:
	pass
class mother:
	pass
class father:
	pass
class child(father,mother,uncle):
	pass
c=child()
c.m1()  #Error : no m1()



#Parent and child class constructors
class parent:
	def __init__(self):
		print('parent constructor')
	def __del__(self):
		print('parent destructor')
class child(parent):
	def __init__(self):
		super().__init__() #How to call parent class constructor
		print('child constructor')
	def __del__(self):
		super().__del__() #How to call parent class destructor
		print('child destructor')
c=child()
print('Bye')

#Outputs
parent constructor
child constructor
Bye
parent destructor
child destructor



#Find outputs
class parent:
	def __init__(self):
		print('parent constructor')
	def __del__(self):
		print('parent destructor')
class child(parent):
	def __init__(self):
		print('child constructor')
	def __del__(self):
		print('child destructor')
c=child()
print('Bye')

#Outputs
child constructor
Bye
child destructor



#Find outputs
class parent:
	def __init__(self):
		print('parent constructor')
	def __del__(self):
		print('parent destructor')
class child(parent):
	pass
print('Bye') #Bye



#Parent and child constructor demo program
class parent:
	def __init__(self,a1,b1):
		self.a=a1
		self.b=b1
	def disp(self):
		print(self.a,self.b,sep='\t',end='\t')
class child(parent):
	def __init__(self,a2=0,b2=0,c2=0,d2=0):
		super().__init__(a2,b2) #How to call parent class constructor with a2, b2
		self.c=c2
		self.d=d2
	def disp(self):
		super().disp() #How to call parent class disp() method
		print(self.c,self.d,sep='\t')
x=child(10,20,30,40)
y=child()
print('Object x')
x.disp()
print('Object y')
y.disp()

#Outputs
Object x
10      20      30      40
Object y
0       0       0       0



#Find outputs
class parent:
	x=100
	def __init__(self):
		self.x=10
class child(parent):
	def __init__(self):
		super().__init__()
		self.y=20
	def disp(self):
		print(super().x) #How to print static variable 'x'
		print(self.x) #How to print variable 'x' of object 'c'
		print(self.y) #How to print variable 'y' of object 'c'
		#print(self.y)
c=child()
c.disp()

#Outputs
100
10
20



#Find outputs
class parent:
	x=10
	def __init__(self):
		self.x=20
class child(parent):
	def __init__(self):
		self.x=30
		print(self.x)
		super().__init__()
	def disp(self):
		print(self.x)
		print(super().x)
c=child()
c.disp()

#Outputs
30
20
10



#Find outputs
class parent:
	a=10 #How to add static variable 'a' to parent class with value 10
	def __init__(self):
		print('Parent Constructor')
		self.x=30 #How to add instance variable 'x' with value 30
	def m1(self):
		print('Parent class instance method :',self.x) #How to print variable 'x'
	@classmethod
	def m2(cls):
		print('Parent class "class" method :',cls.a) #How to print static variable 'a'
		print('Parent class "class" method :',parent.a) #How to print static variable 'a' in another way
		#print(self.a) #Error : no self
	@staticmethod
	def m3():
		print('Parent class static method :',parent.a) #How to print static variable 'a'
	def __del__(self):
		print('parent destructor :',self.x) #How to print variable 'x'
class child(parent):
	b=20 #How to add static variable 'y' with value 20
	def __init__(self):
		super().__init__() #How to call parent class constructor
		print('Child constructor')
		self.y=40 #How to add instance variable with value 'y'
	def m1(self):
		super().m1() #How to call m1() method of parent class
		print('Child class instance method')
		print(self.y) #How to print variable 'y'
	@classmethod
	def m2(cls):
		super().m2() #How to call m2() method of parent class
		super(child,cls).m2() ##How to call m2() method of parent class in another way
		#cls.m2()  #Error : recursion
		#self.m2() #Error : no self
		print('Child class "class" method')
		print(cls.a) #How to print static variable 'a'
		print(parent.a) #How to print static variable 'a' in another way
		#print(super().a)
		print(child.a) #How to print static variable 'a' in last way
		print(child.b) #How to print static variable 'b'
		print(cls.b) #How to print static variable 'b' in another way
	@staticmethod
	def m3():
		parent.m3() #How to call m3() method of parent class
		#self.m3() #Error : no self
		#cls.m3() #Error : no cls
		print('child class static method',parent.a) #How to print static variable 'a'
		print(child.a) #How to print static variable 'a' in another way
		print(child.b) #How to print static variable 'b'
	def __del__(self):
		super().__del__() #How to call destructor of parent class
		print('child destructor',self.y) #How to print variable 'y'
c=child()
c.m2() #How to call m2() method of child class
c.m3() #How to call m3() method of child class
c.m1() #How to call m1() method of child class

#Outputs
Parent Constructor
Child constructor
Parent class "class" method : 10
Parent class "class" method : 10
Parent class "class" method : 10
Parent class "class" method : 10
Child class "class" method
10
10
10
20
20
Parent class static method : 10
child class static method 10
10
20
Parent class instance method : 30
Child class instance method
40
parent destructor : 30
child destructor 40
