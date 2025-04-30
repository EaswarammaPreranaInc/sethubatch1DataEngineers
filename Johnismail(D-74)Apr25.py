'''# Find  outputs
class  c1:
        pass
class  c2(c1):
        pass
# End of the class
print(issubclass(c2 , c1)) #True
print(issubclass(int , float)) #False
print(issubclass(str , object)) #True
print(issubclass(c1 , object))#True
print(issubclass(c2 , object))#True
a = c1()
b = c2()
print(issubclass(b , a))#Error 
print(issubclass(c2 , a)) #Error


# Find outputs
class c1:
        pass
class  c2(c1):
        pass
class  c3(c2):
        pass
class  c4(c3):
        pass
print(issubclass(c4 , c3)) #True
print(issubclass(c4 , c2)) #True
print(issubclass(c4 , c1)) #True
print(issubclass(c4 , object)) #True
print(issubclass(c4 , (int , float , str , bool))) #False
print(issubclass(c4 , (int , float , c1 , str , bool))) #True
print(issubclass(c4 , [int , float , c1 , str , bool])) # issubclass() arg 2 must be a class, a tuple of classes

#  Find  outputs
class  c1:
        pass
class  c2(c1):
        pass
class  c3(c2):
        pass
class  c4:
        pass
#  End  of  the  class
print(isinstance(25 , int)) #True
print(isinstance(10.8 , float))#True
print(isinstance('Hyd' , str))#True
print(isinstance(3 + 4j , complex))#True
print(isinstance(True , bool))#True
print(isinstance(True , int))#True
print(isinstance('True' , str))#True
print(isinstance(True , str))#False
print()
a = c3()
print(isinstance(a , c3))##True
print(isinstance(a , c2))#True
print(isinstance(a , c1))#True
print(isinstance(a , object))#True
print(isinstance(a , c4))#False
print(isinstance(a , (int  ,  float  ,  str  ,  bool)))#False
print(isinstance(a , (int  ,  float  ,  c3 , str  ,  bool)))#True
print(isinstance(a , (int  ,  float  ,  c1  ,  str  ,  bool)))#True
print(isinstance(a , [int  ,  float  ,  c3 , str  ,  bool]))#Error


#  Multilevel  inheritance  demo  program
class  A:
	def    m1(self):
		print('class   A  method')
class  B(A):
	def  m1(self):
		print('class  B   method')
class   C(B):
	def  m1(self):
		print('class   C    method')
class   D(C):
	def   m1(self):
		print('class   D   method')
		super(D,D()).m1() #How  to  call  method  m1()  of  class  C
		a=C()
		a.m1() #how  to  call  method  m1()  of  class  C  in  another  way
		super(C,self).m1() #How  to  call  method  m1()  of  class  C  in  one  more  way
		super(C,C()).m1() #How  to  call  method  m1()  of  class  B
		b=B()
		b.m1() #How  to  call  method  m1()  of  class  B  in  another  way
		c=A()
		c.m1()#How  to  call  method  m1()  of  class  A
		super().m1() #How  to  call  method  m1()  of  class  A  in  another  way
		#super(A , self) . m1() #Error
		#super(C) . m1() #error
# End  of  the  class
d=D()
d.m1() #How  to  call  method  m1()  of  class  D

# Find  outputs  (Home  work)
class  father:
        def  height(self):
                print('Father  Height')
class  mother:
        def  color(self):
                print('Mother  Color')
class  child(mother , father):
        def  qualification(self):
                print('Child Qualification')
# End  of  the  class
c  =  child()
c . qualification() #'Child Qualification'
c . color() #'Mother  Color'
c . height() #'Father  Height'
#c . m1()

#  Find  outputs
class  uncle:
        def  m1(self):
                print('Uncle  Method')
class  mother:
        def  m1(self):
                print('Mother  Method')
class  father:
        def  m1(self):
                print('Father  Method')
class  child(father , mother , uncle):
        def  m1(self):
                print('Child  Method')
#end  of  the  class
c = child()
c . m1() #'Child  Method'

# Find  outputs
class  uncle:
        def  m1(self):
                print('Uncle  Method')
class  mother:
        def  m1(self):
                print('Mother  Method')
class  father:
        def  m1(self):
                print('Father  Method')
class  child(father , mother , uncle):
	pass
#end  of  the  class
c = child()
c . m1() #'Father  Method'

# Find  outputs
class  uncle:
        def  m1(self):
                print('Uncle  Method')
class  mother:
        def  m1(self):
                print('Mother  Method')
class  father:
        pass
class  child(father , mother , uncle):
        pass
#end  of  the  class
c = child()
c . m1()# 'Mother  Method'

# Find  outputs
class  uncle:
        def  m1(self):
                print('Uncle  Method')
class  mother:
        pass
class  father:
        pass
class  child(father , mother , uncle):
        pass
#end  of  the  class
c = child()
c . m1() #'Uncle  Method'

# Find  outputs
class  uncle:
        pass
class  mother:
        pass
class  father:
        pass
class  child(father , mother , uncle):
        pass
#end  of  the  class
c = child()
c . m1() #child object has no method m1()

# Parent  and  Child  constructor  demo  program  (Home  work)
class  parent:
	def   __init__(self , a1 , b1):
		self . a = a1
		self . b = b1
	def disp(self):
		print(self . a , self . b , sep = '\t' , end = '\t')
class   child(parent):
	def __init__(self , a2 = 0  , b2 = 0 , c2 = 0  , d2 = 0):
		super().__init__() #How  to  call  parent  class  constructor  with  a2 , b2
		self . c = c2
		self . d = d2
	def  disp(self):
		super().disp() #How  to  call  parent  class  disp()  method
		print(self . c , self . d , sep = '\t')
#end of the class
x = child(10 , 20 , 30 , 40)
y = child()
print('Object  x')
x . disp()
print('Object  y')
y . disp()
'''
# Find outputs  (Home  work)
class  parent:
	x = 100
	def   __init__(self):
		self . x = 10
class   child(parent):
	def   __init__(self):
		super() . __init__()
		self . y = 20
	def disp(self):
		print(parent.x )#How  to  print  static  variable  'x')
		print(self.x) #How  to  print  variable  'x'  of  object  'c')
		print(self.y) #How  to  print  variable  'y'  of  object  'c')
		#print(
		print(self . y)
#end of the class
c = child()
c . disp()
