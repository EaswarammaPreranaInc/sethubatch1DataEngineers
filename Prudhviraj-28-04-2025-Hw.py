# Find  outputs
class   father:
	def  m1(self):
		print('m1  method  of  Father  class')
class   mother:
	def  m1(self):
		print('m1  method  of  Mother  class')
class   uncle:
	def  m1(self):
		print('m1  method  of  Uncle  class')
class   child(father , mother , uncle):
	def  m1(self):
		print('m1  method  of  child  class')
		father.m1(self)    #How  to  call  m1()  method  of  father  class
		super().m1()   #How  to  call  m1()  method  of  father  class  in  another  way
		mother.m1(self)     #How  to  call  m1()  method  of  mother  class
		uncle.m1(self)     #How  to  call  m1()  method  of  uncle  class
		#super(uncle , self) . m1()
# End of the class
print(child .__mro__)
c=child()              #How  to  call  m1()  method  of  child  class
c.m1()
print('Bye')
"""
Output:
(<class '__main__.child'>, <class '__main__.father'>, <class '__main__.mother'>, <class '__main__.uncle'>, <class 'object'>)
m1  method  of  child  class
m1  method  of  Father  class
m1  method  of  Father  class
m1  method  of  Mother  class
m1  method  of  Uncle  class
Bye
"""

# Find outputs  (Home  work)
class  A:                  
	def  m1(self):
		super() . m1()
		print('class A method')
class  B:
	def m1(self):
		super() . m1()
		print('class B method')
class  C:
	def m1(self):
		super() . m1()
		print('class C method')
class  D:
	def m1(self):
		super() . m1()
		print('class D method')
class  X(A , B):
        def m1(self):
                super() . m1()
                print('class X method')
class  Y(B , C , D):
        def m1(self):
                super() . m1()
                print('class Y method')
class  P(X , Y , C):
        def m1(self):
                super() . m1()
                print('class P method')
#end of the class
print(P . mro())
obj= P()
obj.m1()
print('Bye')
"""
Output:
[<class '__main__.P'>, <class '__main__.X'>, <class '__main__.A'>, <class '__main__.Y'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.D'>, <class 'object'>]
"""

# Find  outputs  (Home  work)
class  D:
        def __init__(self):
                super() . __init__()
                print('class D constructor')
class  E:
        def __init__(self):
                super() . __init__()
                print('class E constructor')
class  F:
        def __init__(self):
                super() . __init__()
                print('class F constructor')
class  B(D , E):
        def __init__(self):
                super() . __init__()
                print('class B constructor')
class  C(D , E , F):
        def __init__(self):
                super() . __init__()
                print('class C constructor')
class  A(B , C):
        def __init__(self):
                super() . __init__()
                print('class A constructor')
#end of the class
print(A . mro())
obj = A()
print('Bye')
"""
Output:
[<class '__main__.A'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.D'>, <class '__main__.E'>, <class '__main__.F'>, <class 'object'>]
class F constructor
class E constructor
class D constructor
class C constructor
class B constructor
class A constructor
"""

# Identify  Error
class  c1(c1):(#argument c1 is not defined)
	pass


# Find  outputs
class   c1:
	def  m1(self):
			print('Parent  Method')
class  c1(c1):
	def  m1(self):
		super() . m1()
		print('Child  Method')
a = c1()
a . m1()
"""
Output:
Parent Method
Child Method
"""

# Identify  Error
class   c1(c2):#Error c2 is not defined
	pass
class  c2(c1):
	pass

# Find  outputs
class   c2:
	def  m1(self):
			print('Parent  Method')
class   c1(c2):
	def  m1(self):
			super() . m1()
			print('Child  Method')
class  c2(c1):
	def  m1(self):
			super() . m1()
			print('Grand  Child  Method')
a = c2()
a . m1()
"""
Output:
Parent  Method
Child  Method
Grand  Child  Method
"""

#  Find  outputs  (Home  work)
class  parent:
	def  m1(self):
		print('Overridden  Method')
class  child(parent):
	def  m1(self):
		print('Overriding  Method')
#end of the class
x = parent()
x . m1()
x = child()
x . m1()
"""
Output:
Overridden  Method
Overriding  Method
"""

# Find  outputs   (Home  work)
class   parent:
	def  m1(self):
		print('m1  method  of  parent  class')
	def  m2(self):
		print('m2  method  of  parent class')
class  child(parent):
	def  m1(self):
		print('m1  method  of  child  class')
	def  m3(self):
		print('m3  method  of  child  class')
#end of the class
x = parent()
x . m1()
x . m2()
#x . m3() #Error
x = child()
x . m1()
x . m2() #Error
x . m3()
"""
Output:
m1  method  of  parent  class
m2  method  of  parent class
m1  method  of  child  class
m2  method  of  parent class
m3  method  of  child  class
"""


# Find  outputs  (Home  work)
class  parent:
	def  marriage(self):
		print('Arranged Marriage')
	def  property(self):
		print('One  Crore')
	def  study(self):
		print('Studies only' , end = '\t')
class  child(parent):
	def  marriage(self):
		print('Love Marriage')
	def  study(self):
		super() . study()
		print(' + Entertainment')
#end of the class
c = child()
c . marriage()
c . property()
c . study()
"""
Output:
Love Marriage
One  Crore
Studies  + Entertainment
"""

# Find  outputs  (Home  work)
class  parent:
	def  add(self , x , y):
		return  x + y
class  child(parent):
	def   add(self , x , y , z):
		return  x + y + z
# End of the class
c = child()
print(c . add(10 , 20 , 30))
#print(c . add(10 , 20))
"""
Output:
60
"""


# Find  outputs  (Home  work)
class  parent:
	def  add(self , x , y):
		print('parent  method')
		return  x + y
class  child(parent):
	def   add(self , x , y , z = 3):
		print('child  method')
		return  x + y + z
#End  of  the  class
c = child()
print(c . add(10 , 20 , 30))
print(c . add(10 , 20))
"""
Output:
child method
60
child method
33
"""

#Find  outputs  (Home  work)
class  parent:
	def   m1(self , a , b , /):
		print(F'parent  method   a  :  {a}  \t  b  :  {b}')
class  child(parent):
	def   m1(self , x , y):
		print(F'child  method   x  :  {x}  \t  y  :  {y}')
# End of the class
c = child()
c . m1(x = 10 , y = 20)
c . m1(30 , 40)
"""
Output:
child  method   x  :  10		  y  :  20
child  method   x  :  30          y  :  40
"""

# Find  outputs (Home  work)
from  abc  import  *
class  c1(ABC):
	@abstractmethod
	def  m1(self):
		pass
	def  __init__(self):
		print('c1  class  constructor')
class  c2(ABC):
	def  m1(self):
		pass
	def  __init__(self):
		print('c2  class  constructor')
class  c3:
	@abstractmethod
	def  m1(self):
		pass
	def  __init__(self):
		print('c3  class  constructor')
class  c4(c1):
	def  m1(self):
		pass
	def  __init__(self):
		print('c4  class  constructor')
class  c5(c1):
	def  __init__(self):
		print('c1  class  constructor')
# End  of  the  class
#c1()
c2()
c3()
c4()
#c5()
"""
Output:
c2  class  constructor
c3  class  constructor
c4  class  constructor
"""

# Find  outputs (Home  work)
from   abc    import    *
class   parent(ABC):
	@abstractmethod
	def  m1(self):
		pass
	@abstractmethod
	def  m2(self):
		pass
	@abstractmethod
	def  m3(self):
		pass
class  child(parent):
	def  m1(self):
		print('m1  method  of  child  class')
class  gc(child):
	def  m2(self):
		print('m2  method  of    gc  class')
class  ggc(gc):
	def  m3(self):
		print('m3  method  of  ggc  class')
# End  of  the  class
a = ggc()
a . m1()
a . m2()
a . m3()
#parent()
#child()
#gc()
"""
Output:
m1  method  of  child  class
m2  method  of    gc  class
m3  method  of  ggc  class
"""
'''
'''
Write  a  program  to  determine  area  and  perimeter  of  triangle , circle , rectangle  and  square

1) What  is  the  parent  class ?  ---> shape
    What  are  child  classes ?  ---> triangle , circle , rectangle , square

2) What  is  the  area  of  triangle  ?  --->  sqrt(s * (s - a) *  (s - b) * (s - c))
    What  is  the  value  of  's' ?  ---> (a + b + c) / 2
    What  is  the  perimeter  of  triangle ?  ---> a + b + c

3) What  is  the  area  of  circle ?  --->  3.14159 * a ^ 2  where  'a'  is  radius  of  circle
    What  is  the  circumference  of  circle ?  --->  2 * 3.14159 * a

4) What  is  the  area  of  rectangle  ?  --->  a * b  where  'a'  is  length and  'b'  is  breadth
    What  is  the  perimter  of  rectangle ?  ---> 2 * (a + b)

5) What  is  the  area  of  square ?  ---> a ^ 2
    What  is  the  perimeter  of  square  ?  ---> 4 * a

import   math
from  abc  import  *
class  shape(ABC):
	def   get(self):
		self.a=int(input(""))#How  to  read  input  to  variable  'a'  of  object  self
	@abstractmethod
	def   area(self):
		pass
	@abstractmethod
	def  peri(self):
		pass
	@abstractmethod
	def  test(self):
		pass
class  triangle(shape):
	def   get(self):
		print('Enter  3  sides  of  triangle')
		self.a=int(input("Enter the input side 1: "))  #How  to  read  the  3  sides  of  triangle
		self.b=int(input("Enter the input side 2: "))
		self.c=int(input("Enter the input side 3: "))
	def   area(self):
		s=(self.a+self.b+self.c)/2
		d=math.sqrt(s*(s-self.a)*(s-self.b)*(s-self.c))
		return  d
	def   peri(self):
		return  self.a+self.b+self.c
	def   test(self):
		if  (self.a+self.b>self.c) and (self.b+self.c>self.a) and (self.a+self.c>self.b):
			pass
		else:
			print('Not    a  triangle')
			exit() #How  to  stop  execution
class   circle(shape):
	def   get(self):
		print('Enter  radius  of  circle  : ' , end = '\t')
		super().get()#How  to  read  radius
	def   area(self):
		e=math.pi*self.a**2
		return  e
	def   peri(self):
		f=2*math.pi*self.a
		return  f
	def  test(self):
		if  self.a<=0:   #side  is  -ve
		    print('Radius  can  not  be  -ve')
		    exit()#How  to  stop  execution
class   rectangle(shape):
	def  get(self):
		print('Enter  length  and  breadth  of  rectangle')
		super().get()   #How  to  read  length  and  breadth
		self.g=int(input("Enter the breadth: "))
	def   area(self):
		h=self.a*self.g
		return   h
	def   peri(self):
		i=2*(self.a+self.g)
		return i
	def  test(self):
		if  self.a ==self.g:  #length  and   breadth  same
		    print('Not  a rectangle')
		    exit()#How  to  stop  execution
class   square(shape):
	def   get(self):
		print('Enter  any  side  of  square :  ' , end =  '\t')
		super().get()  #How  to  read  side
	def   area(self):
		k=self.a**2
		return  k
	def   peri(self):
		l=4*self.a
		return  l
	def  test(self):
		pass
#  End  of  the  class
def   menu():
	print('1. Triangle')
	print('2. Circle')
	print('3. Rectangle')
	print('4. Square')
	print('5. Exit')
# End  of  menu  function
def   operation(s):
	s.get()#How  to  read  inputs  to  object  's'
	s.test()#How  to  test  inputs  are  valid  (or)  not
	area=s.area()
	peri=s.peri()
	print('Area  :  ' , area)
	print('Perimeter  :  ' ,  peri);
# End  of  the  function
menu()
ch = eval(input('Enter  choice  :  '))
while ch<=4:
	match   ch:
		case  1:
			operation(triangle())   #How  to  call  operation()  function
		case  2:
			operation(circle())#How  to  call  operation()  function
		case  3:
			operation(rectangle())#How  to  call  operation()  function
		case  4:
			operation(square())#How  to  call  operation()  function
	#end  of  match
	menu()
	ch = int(input('Enter   choice  :  '))
# End of while  loop
print('Good  Bye')
"""
Output:
1. Triangle
2. Circle
3. Rectangle
4. Square
5. Exit
Enter  choice  :  1
Enter  3  sides  of  triangle
Enter the input side 1: 3
Enter the input side 2: 4
Enter the input side 3: 5
Area  :   6.0
Perimeter  :   12
1. Triangle
2. Circle
3. Rectangle
4. Square
5. Exit
Enter   choice  :  2
Enter  radius  of  circle  :    5
Area  :   78.53981633974483
Perimeter  :   31.41592653589793
1. Triangle
2. Circle
3. Rectangle
4. Square
5. Exit
Enter   choice  :  3
Enter  length  and  breadth  of  rectangle
2
Enter the breadth: 4
Area  :   area  of  rectangle: 8
Perimeter  :   perimeter  of  triangle:12
1. Triangle
2. Circle
3. Rectangle
4. Square
5. Exit
Enter   choice  :  4
Enter  any  side  of  square :          3
Area  :   9
Perimeter  :   12
Good Bye
"""
