#Determine area and circumference of circle
#Also find area and volume of cylinder
import math
class circle:
	def get(self):
		self.r=float(input('Enter radius : ')) #read radius into object self
	def area(self):
		return math.pi*self.r**2
	def cir(self):
		return 2*math.pi*self.r
class cylinder(circle):
	def get(self):
		super().get()  #read radius into object self
		self.h=float(input('Enter height : ')) #read height into object self
	def area(self):
		return super().cir()*self.h+2*super().area()
	def volume(self):
		return super().area()*self.h
def menu():
	print('1. Circle')
	print('2. Cylinder')
	print('3. Exit')
menu()
ch=eval(input('Enter choice : '))
while ch<3:
	match ch:
		case 1:
			c=circle()
			c.get()
			print('Area :',c.area())
			print('Circumference :',c.cir())
		case 2:
			c=cylinder()
			c.get()
			print('Area :',c.area())
			print('Volume :',c.volume())
	menu()
	ch=eval(input('Enter choice : '))
print('Bye')

#Output
1. Circle
2. Cylinder
3. Exit
Enter choice : 1
Enter radius : 3
Area : 28.274333882308138
Circumference : 18.84955592153876
1. Circle
2. Cylinder
3. Exit
Enter choice : 2
Enter radius : 3
Enter height : 2
Area : 94.24777960769379
Volume : 56.548667764616276
1. Circle
2. Cylinder
3. Exit
Enter choice : 3
Bye



#determine area and perimeter of rectangle and square
#Also find surface area and volume of cube
import math
class square:
	def get(self):
		self.s=float(input('Enter side length : ')) 
	def area(self):
		return self.s**2
	def peri(self):
		return 4*self.s
class rectangle(square):
	def get(self):
		self.l=float(input('Enter length : '))
		self.b=float(input('Enter breadth : '))
	def area(self):
		return self.l*self.b
	def peri(self):
		return 2*(self.l+self.b)
class cube(square):
	def get(self):
		super().get()
	def area(self):
		return 6*super().area()
	def volume(self):
		return super().area()*self.s
def menu():
	print('1. Square')
	print('2. Rectangle')
	print('3. Cube')
	print('4. Exit')
menu()
ch=int(input('Enter choice : '))
while ch<4:
	match ch:
		case 1:
			c=square()
			c.get()
			print('Area :',c.area())
			print('Perimeter :',c.peri())
		case 2:
			c=rectangle()
			c.get()
			print('Area :',c.area())
			print('Perimeter :',c.peri())
		case 3:
			c=cube()
			c.get()
			print('Area :',c.area())
			print('Volume :',c.volume())
	menu()
	ch=int(input('Enter choice : '))

#Output
1. Square
2. Rectangle
3. Cube
4. Exit
Enter choice : 1
Enter side length : 4
Area : 16.0
Perimeter : 16.0
1. Square
2. Rectangle
3. Cube
4. Exit
Enter choice : 2
Enter length : 3
Enter breadth : 4
Area : 12.0
Perimeter : 14.0
1. Square
2. Rectangle
3. Cube
4. Exit
Enter choice : 3
Enter side length : 4
Area : 96.0
Volume : 64.0
1. Square
2. Rectangle
3. Cube
4. Exit
Enter choice : 4



#Find outputs
class c1:
	def m1(self):
		print('m1 method of class c1')
class c2:
	def m1(self):
		print('m1 method of class c2')
class c3:
	@classmethod
	def m1(cls):
		print('m1 method of class c3')
class c4:
	@staticmethod
	def m1():
		print('m1 method of class c4')
class c5(c1):
	def m1(self):
		print('m1 method of class c5')
	def m2(self):
		c3.m1() #m1 of class c3
		c4.m1() #m1 of class c4
		c=c2()
		c.m1() #m1 of class c2
		super().m1() #m1 of class c1
		self.m1() #m1 of class c5
		m1() #m1 function
def m1():
	print('m1 function')
x=c5()
x.m2() #m2 of class c5

#Output
m1 method of class c3
m1 method of class c4
m1 method of class c2
m1 method of class c1
m1 method of class c5
m1 function
