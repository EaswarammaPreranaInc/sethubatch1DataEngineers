#HW-1
'''class      Rat:
	def    m1():
		pass
# End  of  the  class
a = Rat()
a . nr = 22
print(hasattr(a , 'nr'))
print(hasattr(a , 'dr'))
print(hasattr(a , 'm1'))
print(hasattr(a , 'm2'))
print(hasattr(Rat , 'm1'))
print(hasattr(Rat , 'm2'))
print(hasattr(Rat , 'nr'))'''



# HW-2
'''class  Cat:
	def  talk(self):
		print('Meow Meow Meow ....')
class  Dog:
	def  bark(self):
		print('Bhow Bhow Bhow ....')
class  Goat:
	def  talk(self):
		print('Mehar  Mehar  Mehar  ....')
#end of the class
a = [Cat() , Dog() , Goat()]
for  x  in   a:
	if   hasattr(x , 'talk'):
		x . talk()
	else:
		x . bark()
		
#output
Meow Meow Meow ....
Bhow Bhow Bhow ....
Mehar  Mehar  Mehar  ....'''


#  HW-3
'''class    c1:
        pass
# End of the class
a = c1()
a . x = 10
varname = input('Enter  variable  name  to  be  added  to  object  :  ')   #  Assume  that  input  is  'y'
value = eval(input('Enter  value  of  the  variable  :  '))   #  Assume  that  input  is   20
setattr(a , varname , value)
print(a . _dict_)
print(a . x) # 10
while  True:
	try:
		varname = input('Enter  variable  name  whose  value  is  to  be  retrieved  :  ')
       #  Assume  that  input  is  x  in  1st   iteration  ,  y  in   2nd   iteration  and  z  in  3rd  iteration
		print(getattr(a , varname))
	except:
		print(F'Invalid  variable   name   :  {varname}')
		break'''


'''
# HW-4
Write  a  program  to  convert  a  dictionary  {'Empno' : 25 , 'Ename' : 'Rama  Rao' , 'Sal' : 10000.0}  to  Emp  class  object
i.e.  object  should  contain  empno = 25 , ename = 'Rama  Rao' , Sal = 10000.0

Hint:  Use  setattr()  and  getattr()  functions

class  Emp:
        pass
#End  of  the  class
dict = {'Empno' : 25 , 'Ename' : 'Rama  Rao' , 'Sal' : 10000.0}
e = Emp()
for key , value in dict.items():
        setattr(e , key , value)  # How  to  convert  dictionary  to  object  'e'  with  for  loop
for attr in dict:
        print(f'{attr} = {getattr(e , attr)}')  # How  to  print  object  'e'  with  for  loop
'''

# HW-5
'''
Write  a  program  to  determine  total , average  and  grade  of  a  student
Inputs  are  Roll Number , Stud  Name , Marks  of  3  subjects  and  Gender


class Student:
    def get(self):
        self.roll_no = input("Enter Roll Number: ")
        self.name = input("Enter Student Name: ")
        self.gender = input("Enter Gender: ")
        self.marks = []
        for i in range(1, 4):
            mark = int(input(f"Enter Marks of Subject {i}: "))
            self.marks.append(mark)

    def compute(self):
        self.total = sum(self.marks)
        self.average = self.total / 3

        if any(mark < 40 for mark in self.marks):
            self.grade = 'Fail'
        elif self.average >= 70:
            self.grade = 'Distinction'
        elif self.average >= 60:
            self.grade = 'First class'
        elif self.average >= 50:
            self.grade = 'Second class'
        else:
            self.grade = 'Third class'

    def disp(self):
        print('Roll Number  :', self.roll_no)
        print('Student Name :', self.name)
        print('Gender       :', self.gender)
        print('Total Marks  :', self.total)
        print('Average      :', self.average)
        print('Grade        :', self.grade)

    def __str__(self):
        return (f"Roll Number: {self.roll_no}, Name: {self.name}, Gender: {self.gender}, "
                f"Total: {self.total}, Average: {self.average:.2f}, Grade: {self.grade}")


s = Student()  # # Create Student class object
s.get()  # Read inputs into object
s.compute() # Compute results and store in object
s.disp()  # Print using disp() method
print(s) # Print using __str__() method'''


# HW-6
import math
class Triangle:
    def get(self):
        self.a = int(input("Enter side 1: "))
        self.b = int(input("Enter side 2: "))
        self.c = int(input("Enter side 3: "))

    def test(self):
        if (self.a + self.b > self.c) and (self.a + self.c > self.b) and (self.b + self.c > self.a):
            pass
        else:
            print('Not a triangle')
            exit()
    def area(self):
        s = (self.a + self.b + self.c) / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))

    def peri(self):
        return self.a + self.b + self.c

# Create Triangle object
if __name__ == '__main__':
    t = Triangle()
    t.get()
    t.test()
    print('Area :', t.area())
    print('Perimeter :', t.peri())





