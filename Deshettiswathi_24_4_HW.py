Q1 Write  a  program  to  determine  area  and  circumference  of  circle.  Also  find  area  and  volume  of  cylinder

import  math
class   circle:
	def   get(self):
	    self.r=int(input('Enter radius of circle :')) #How  to  read  radius  into  object  self
	def   area(self):
		return  math.pi*self.r**2           #area  of  circle
	def   cir(self):
		return  2*math.pi*self.r                       #circumference  of  circle
# End  of  circle  class
class  cylinder(circle):
	def   get(self):
		self.r=int(input('Enter radius of cylinder: '))   #How  to  read  radius  into  object  self
		self.h=int(input('Enter height of cylinder: '))    #How  to  read  height  into  object  self
	def  area(self):
		return  (2*math.pi*self.r**2)+(2*math.pi*self.r*self.h)          #area  of  cylinder
	def  volume(self):
		return   math.pi*self.r**2*self.h                           #volume  of  cylinder
# End of cylinder class
def    menu():
	print('1 . Circle')
	print('2 . Cylinder')
	print('3 . Exit')
#end of menu function
menu()
c=circle()
cy=cylinder()
ch = eval(input('Enter choice : '))
while ch<3:
	match  ch:
		case  1:
				c.get()  #How  to  read  raidus  into  circle  object
				print(f'Area  :    {c.area():.2f}' )
				print(f'Circumference :    {c.cir():.2f}')
		case  2:
				cy.get()    #How  to  read  raidus  and  height  into  cylinder  object
				print(f'Area :    {cy.area():.2f}')
				print(f'Volume :     {cy.volume():.2f}')
	#end  of  match
	menu()
	ch = eval(input('Enter choice : '))
print('Bye')

OP-1 . Circle
2 . Cylinder
3 . Exit
Enter choice : 1
Enter radius of circle :4
Area  :    50.27
Circumference :    25.13
1 . Circle
2 . Cylinder
3 . Exit
Enter choice : 2
Enter radius of cylinder: 4
Enter height of cylinder: 8
Area :    301.59
Volume :     402.12
1 . Circle
2 . Cylinder
3 . Exit
Enter choice : 3
Bye
#-----------------------------------------------------------------------------------------------------------------------------------
Q2 Write  a  program  to  determine  area  and  perimeter  of  rectangle  and  square. Also  find  surface  area  and  volume  of  cube

class   Square:
	def   get(self):
		self.a=int(input('Enter side of a square: '))      #How  to  read  side  of  square
	def   area(self):
		return    self.a**2         #area  of  square
	def   peri(self):
		return    4*self.a          #perimeter  of  square
class   Rectangle(Square):
	def   get(self):
		self.a=int(input('Enter length of rectangle: '))  #How  to  read  length  of  rectangle
		self.b=int(input('Enter breadth of rectangle: ')) #How  to  read  breadth  of  rectangle
	def   area(self):
		 return   self.a*self.b              #area  of  rectangle
	def   peri(self):
		return  2*(self.a*self.b)            #perimeter  of   rectangle
class   Cube(Square):
	def   get(self):
		 self.a=int(input('Enter side of a cube: '))    #How  to  read  side  of  cube
	def   area(self):
		return   6*self.a**2                              #area  of  cube
	def   volume(self):
		return  self.a**3                                  #volume  of  cube
def  menu():
	print('1 . Square')
	print('2 . Rectangle')
	print('3 . Cube')
	print('4 . Exit')
# End  of  the  function
menu()
ch = int(input('Enter  choice : '))
s=Square()
r=Rectangle()
c=Cube()
while  ch< 4:
	match   ch:
		case   1:
			s.get()          #How  to  read  side  into   square  object  's'
			print(f'Area   :  {s.area():.2f}' )
			print(f'Perimeter  :  {s.peri():.2f}')
		case   2:
			r.get()    #How  to  read  length  and  breadth  into   rectangle  object  'r'
			print(f'Area  :  {r.area():.2f}')
			print(f'Perimeter  :  {r.peri():.2f}')
		case   3:
			c.get()        #How  to  read  side  into  cube  object  'c'
			print(f'Area  :  {c.area():.2f}')
			print(f'Volume  :  {c.volume():.2f}')
	menu()
	ch = int(input('Enter  choice : '))

OP-
1 . Square
2 . Rectangle
3 . Cube
4 . Exit
Enter  choice : 1
Enter side of a square: 3
Area   :  9.00
Perimeter  :  12.00
1 . Square
2 . Rectangle
3 . Cube
4 . Exit
Enter  choice : 2
Enter length of rectangle: 8
Enter breadth of rectangle: 5
Area  :  40.00
Perimeter  :  80.00
1 . Square
2 . Rectangle
3 . Cube
4 . Exit
Enter  choice : 3
Enter side of a cube: 7
Area  :  294.00
Volume  :  343.00
1 . Square
2 . Rectangle
3 . Cube
4 . Exit
Enter  choice : 4
#-----------------------------------------------------------------------------------
Q3 #Find  outputs
class  c1:
	def  m1(self):
		print('m1  method  of  class  c1')
class  c2:
	def  m1(self):
		print('m1 method of class c2')
class  c3:
	@classmethod
	def  m1(cls):
		print('m1 method of  class c3')
class  c4:
	@staticmethod
	def  m1():
		print('m1 method of  class c4')
class  c5(c1):
	def  m1(self):
		print('m1 method of class c5')
	def  m2(self):
		c3.m1()    #How  to  call  m1()  method  of  class  c3
		c4.m1()      #How  to  call  m1()  method  of  class  c4
		a.m1()      #How  to  call  m1()  method  of  class  c2
		super().m1()      #How  to  call  m1()  method  of  class  c1
		b.m1()   #How  to  call  m1()  method  of  class  c5
		m1()          #How  to  call  m1()  function
# End  of  class  c5
def  m1():
	print('m1 function')
# End  of  the  function
a=c2()
b=c5()
b.m2()  #How  to  call  m2()  method  of  class  c5

OP-
m1 method of  class c3
m1 method of  class c4
m1 method of class c2
m1  method  of  class  c1
m1 method of class c5
m1 function
