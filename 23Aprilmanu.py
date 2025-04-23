'''
#1)Also  find  area  and  volume  of  cylinder

1) What  is  the  area  of  circle ?  --->  3.14159 * r ^ 2

2) What  is  the  circumference  of  circle ?  --->  2 * 3.14159 * r

3) What  is  the  area  of  cylinder ?  --->  2 * 3.14159  r ^ 2 + 2 * 3.14159 * r * h

4) What  is  the  volume  of  cylinder ?  --->  3.14159 * r ^ 2 *  h

5) Reuse  parent  class  methods  in  child  class  but  do  not  rewrite

import math

class circle:
    def get(self):
        self.r = int(input('Enter radius: '))  # How  to  read  radius  into  object  self

    def area(self):
        return 3.14159 * self.r ** 2  # Area of circle

    def cir(self):
        return 2 * 3.14159 * self.r  # Circumference of circle

# End of circle class

class cylinder(circle):
    def get(self):
        super().get()  # How  to  read  radius  into  object  self
        self.h = int(input('Enter height: '))  # How  to  read  height  into  object  self

    def area(self):
        return 2 * 3.14159 * self.r ** 2 + 2 * 3.14159 * self.r * self.h  # Area of cylinder

    def volume(self):
        return 3.14159 * self.r ** 2 * self.h  # Volume of cylinder

# End of cylinder class

def menu():
    print('1 . Circle')
    print('2 . Cylinder')
    print('3 . Exit')
# End of menu function

menu()
ch = int(input('Enter choice: '))

while ch != 3:
    match ch:
        case 1:
            c = circle()
            c.get() #How  to  read  raidus  into  circle  object
            print('Area:', c.area())
            print('Circumference:', c.cir())
        case 2:
            cyl = cylinder()
            cyl.get() # How  to  read  raidus  and  height  into  cylinder  object
            print('Area:', cyl.area())
            print('Volume:', cyl.volume())
        case 3:
            print('Invalid choice. Please try again.')
    
    menu()
    ch = int(input('Enter choice: '))

print('Bye')

output:-
--------
1 . Circle
2 . Cylinder
3 . Exit
Enter choice: 1
Enter radius: 8
Area: 201.06176
Circumference: 50.26544
1 . Circle
2 . Cylinder
3 . Exit
Enter choice: 2
Enter radius: 6
Enter height: 4
Area: 376.9908
Volume: 452.38896
1 . Circle
2 . Cylinder
3 . Exit
Enter choice: 3
Bye

#2)Write  a  program  to  determine  area  and  perimeter  of  rectangle  and  square.
Also  find  surface  area  and  volume  of  cube

1) What  is  the  area  of  square ?  --->  a ^ 2
    What  is  the  perimeter  of  square ?  --->  4 *  a

2) What  is  the  area  of  rectangle ?  --->  a * b
    What  is  the  perimeter  of  rectangle ?  --->  2 * (a + b)

3) What  is  the  surface  area  of  cube ? --->  6 * a ^ 2
     What  is  the  volume  of  cube  ?  ---> a ^ 3

4) Reuse  parent  class  methods  in  child   classes  but  do  not  rewrite

import math 
class   Square:
	def   get(self):
		self.a = int(input('Enter side a: '))  # How  to  read  side  of  square
	def   area(self):
		return   self.a ** 2 #area  of  square
	def   peri(self):
		return   4* self.a # perimeter  of  square
class   Rectangle(Square):
	def   get(self):
		super().get() # How  to  read  length  of  rectangle
		self.b = int(input('Enter side b: ')) # How  to  read  breadth  of  rectangle
	def   area(self):
		 return   self.a*self.b # area  of  rectangle
	def   peri(self):
		return  2* (self.a+self.b) # perimeter  of   rectangle
class   Cube(Square):
	def   get(self):
		 super().get() # How  to  read  side  of  cube
	def   area(self):
		return  6* self.a** 2 #  area  of  cube
	def   volume(self):
		return  self.a ** 3 #volume  of  cube
def  menu():
	print('1 . Square')
	print('2 . Rectangle')
	print('3 . Cube')
	print('4 . Exit')
# End  of  the  function
menu()
ch = int(input('Enter  choice : '))
while ch != 4 : # repeat  until  user  input  is  4
	match   ch:
		case   1:
			s = Square ()
			s.get() # How  to  read  side  into   square  object  's'
			print('Area   :  ' , s.area())
			print('Perimeter  :  ' , s.peri())
		case   2:
			rect = Rectangle() 
			rect.get () #How  to  read  length  and  breadth  into   rectangle  object  'r'
			print('Area  :  ' , rect.area())
			print('Perimeter  :  ' ,  rect.peri())
		case   3:
			cub = Cube() 
			cub.get() # How  to  read  side  into  cube  object  'c'
			print('Area  :   ' , cub.area())
			print('Volume  :  ' ,  cub.peri())
		case  4:
			print('Invalid choice. Please try again:')
	menu()
	ch = int(input('Enter  choice : '))
print('Bye')

output:-
----------
1 . Square
2 . Rectangle
3 . Cube
4 . Exit
Enter  choice : 1
Enter side a: 8
Area   :   64
Perimeter  :   32
1 . Square
2 . Rectangle
3 . Cube
4 . Exit
Enter  choice : 6
1 . Square
2 . Rectangle
3 . Cube
4 . Exit
Enter  choice : 2
Enter side a: 4
Enter side b: 6
Area  :   24
Perimeter  :   20
1 . Square
2 . Rectangle
3 . Cube
4 . Exit
Enter  choice : 3
Enter side a: 8
Area  :    384
Volume  :   32
1 . Square
2 . Rectangle
3 . Cube
4 . Exit
Enter  choice : 4
Bye
'''
#3) Find  outputs

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
		c3.m1(self) # How  to  call  m1()  method  of  class  c3------>classmethod
		c4.m1() # How  to  call  m1()  method  of  class  c4------->staticmethod
		c2().m1(self) # How  to  call  m1()  method  of  class  c2------> regular
		c1.m1(self) # How  to  call  m1()  method  of  class  c1-----> superclass
		self.m1() # How  to  call  m1()  method  of  class  c5----> overridden 
		m1() # How  to  call  m1()  function-------> function s-----> global m1()
# End  of  class  c5
def  m1():
	print('m1 function')
# End  of  the  function
a =c5()
a.m2 # How  to  call  m2()  method  of  class  c5

