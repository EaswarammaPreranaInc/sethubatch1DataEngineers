#Ex-1
'''
Write  a  program  to  determine  area  and  circumference  of  circle.
Also  find  area  and  volume  of  cylinder

1) What  is  the  area  of  circle ?  --->  3.14159 * r ^ 2

2) What  is  the  circumference  of  circle ?  --->  2 * 3.14159 * r

3) What  is  the  area  of  cylinder ?  --->  2 * 3.14159  r ^ 2 + 2 * 3.14159 * r * h

4) What  is  the  volume  of  cylinder ?  --->  3.14159 * r ^ 2 *  h

5) Reuse  parent  class  methods  in  child  class  but  do  not  rewrite
'''
import  math
class   circle:
    def   get(self):
        self.r=int(input('Enter a radius : '))#How  to  read  radius  into  object  self
    def   area(self):
        return  math.pi * self.r * self.r ; # area  of  circle
    def   cir(self):
        return  2 * math.pi * self.r# circumference  of  circle
# End  of  circle  class
class  cylinder(circle):
        def   get(self):
            super().get()# How  to  read  radius  into  object  self
            self.h=int(input('Enter a height: ')) #How  to  read  height  into  object  self
        def  area(self):
            return 2 * math.pi * self.r * (self.r + self.h)#area  of  cylinder
        def  volume(self):
            return   math.pi * (self.r * self.r) * self.h  # volume  of  cylinder
# End of cylinder class
def    menu():
	print('1 . Circle')
	print('2 . Cylinder')
	print('3 . Exit')
#end of menu function
menu()
ch = eval(input('Enter choice : '))
while True: #Repeat  until  user  input  is  3
    match  ch:
        case  1:
                c=circle()
                c.get() #How  to  read  raidus  into  circle  object
                print('Area  :  ' ,  c.area())
                print('Circumference :  ' ,  c.cir())
        case  2:
                c=cylinder()
                c.get()# How  to  read  raidus  and  height  into  cylinder  object
                print('Area : ' ,  c.area())
                print('Volume :  ' ,c.volume())
        case _:
            exit()
	#end  of  match
    menu()
    ch = eval(input('Enter choice : '))
print('Bye')

#Ex-2
'''
Write  a  program  to  determine  area  and  perimeter  of  rectangle  and  square.
Also  find  surface  area  and  volume  of  cube

1) What  is  the  area  of  square ?  --->  a ^ 2
    What  is  the  perimeter  of  square ?  --->  4 *  a

2) What  is  the  area  of  rectangle ?  --->  a * b
    What  is  the  perimeter  of  rectangle ?  --->  2 * (a + b)

3) What  is  the  surface  area  of  cube ? --->  6 * a ^ 2
     What  is  the  volume  of  cube  ?  ---> a ^ 3

4) Reuse  parent  class  methods  in  child   classes  but  do  not  rewrite
'''



class   Square:
	def   get(self):
		self.a=int(input('Enter a side : '))#How  to  read  side  of  square
	def   area(self):
		return   self.a * self.a#area  of  square
	def   peri(self):
		return   4 * self.a  # perimeter  of  square
class Rectangle(Square):
    def get(self):
        super().get() # How  to  read  length  of  rectangle
        self.b=int(input('Enter a breadth of of rectangle : ')) # How  to  read  breadth  of  rectangle
    def   area(self):
        return   self.a * self.b # area  of  rectangle
    def   peri(self):
        return  2 * (self.a + self.b) # perimeter  of   rectangle
class Cube(Square):
    def   get(self):
        super().get() #How  to  read  side  of  cube
    def area(self):
        return   6 * self.a * self.a# area  of  cube
    def   volume(self):
        return  self.a * self.a * self.a
def  menu():
	print('1 . Square')
	print('2 . Rectangle')
	print('3 . Cube')
	print('4 . Exit')
# End  of  the  function
menu()
ch = int(input('Enter  choice : '))
while True: # repeat  until  user  input  is  4
    match ch:
        case 1:
            s=Square()# How  to  read  side  into   square  object  's'
            s.get()
            print('Area   :  ' ,  s.area())
            print('Perimeter  :  ' , s.peri())
        case   2:
            rec=Rectangle() # How  to  read  length  and  breadth  into   rectangle  object  'r'
            rec.get()
            print('Area  :  ' , rec.area() )
            print('Perimeter  :  ' , rec.peri())
        case   3:
            c=Cube()# How  to  read  side  into  cube  object  'c'
            c.get()
            print('Area  :   ' ,  c.area())
            print('Volume  :  ' ,  c.volume())
        case _:
            break
    menu()
    ch = int(input('Enter  choice : '))

#Ex-3
# Find  outputs
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
	def m2(self):
		c3.m1() # How  to  call  m1()  method  of  class  c3
		c4.m1() # How  to  call  m1()  method  of  class  c4
		a = c2()
		a.m1()# How  to  call  m1()  method  of  class  c2
		b= c1()
		b.m1() # How  to  call  m1()  method  of  class  c1
		self.m1() # How  to  call  m1()  method  of  class  c5
		m1() # How  to  call  m1()  function
# End  of  class  c5
def  m1():
	print('m1 function')
# End  of  the  function
c=c5()
c.m2()# How  to  call  m2()  method  of  class c5
