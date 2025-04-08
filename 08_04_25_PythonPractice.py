'''
Repeat  prog5a  such  that  methods  are  called  in  another  way

1) What  are  the  two  ways  to  call  a  method ?  --->  object . method()  and  classname . method(object)

2) Import  and   use  triangle  class  defined  in  prog5a  but  do  not   define  triangle  class  again
'''
from trianglefunction import Triangle

t = Triangle() #How  to  create  triangle  object
Triangle.get(t) #How  to  call  get()  method  in  another  way
if Triangle.test(t):
    print('Valid Triangle') #How  to  call  test()  method  in  another  way
    print('Area : ',Triangle.area(t)) #  How  to  call  area()  method  in  another  way)
    print('Perimeter: ', Triangle.peri(t)) #  How  to  call  peri()  method  in  another  way)
else:
    print('Not a Triangle:')   
'''o/p: Enter side a: 3
        Enter side b: 4
        Enter side c: 5
        Area : 6.0
        Perimeter : 12.0'''    

'''
Write  a  program  to  determine  total , average  and  grade  of  a  student
Inputs  are  Roll Number , Stud  Name , Marks  of  3  subjects  and  Gender
'''
class   Student:
	def   get(self):
		self.rno = int(input('Enter a value: ')) #How  to  read  roll  number  into  object  self
		self.sname = input('Enter a value: ') # How  to  read  student  name  into  object  self
		self.gender = input('Enter a value: ') #How  to  read  gender  into  object  self
		self.m = [] #How  to  read  marks  of  3  subjects
		for i in range(3):
			mark = int(input(f'Enter mark {i+1}: '))
			self.m.append(mark)
	def   compute(self):
		self.tot = sum(self.m) #How  to  calculate  total  marks
		self.avg = self.tot/3 #How  to  calculate  average  marks
		if  any(mark<40 for mark in self.m): #At  least  one  subject  is  below  40
				self.grade = 'Fail' #How  to  initilaize  grade  to  'Fail'
		elif  self.avg >= 70: #average  is  above  >= 70%
				self.grade = 'Distinction' #How  to  initilaize  grade  to  'Distinction'
		elif  self.avg >= 60: #average  is  above  >= 60%:
				self.grade = 'First  class' #How  to  initilaize  grade  to  'First  class'
		elif  self.avg >= 50: #average  is  above  >= 50%:
				self.grade = 'Second class' #How  to  initilaize  grade  to  'Second  class'
		else:
				self.grade = 'Third class' #How  to  initilaize  grade  to  'Third  class'
	def  disp(self):
		print('Roll  Number  :  ' ,  self.rno)
		print('Student  Name  :  ' , self.sname)
		print('Gender  :  ' , self.gender)
		print('Total  Marks  :  ' , self.tot)
		print('Average  :  ' , self.avg)
		print('Grade  :  ' , self.grade)
	def   __str__(self):
		return  f'Roll No : {self.rno}, Name : {self.sname}, Gender : {self.gender}, Total : {self.tot}, Average : {self.avg :.2f},Grade : {self.grade}' #All  the   values  of  object  self  in  the  form  of  string
#End  of  the  class
s = Student() #How  to  create  Student  class  object
s.get() #How  to  read  inputs  into  object
s.compute() #How  to  store  results  in  object
s.disp() #How  to  print  object  with  disp()  method
print(s) #How  to  print  object  with  _str_()  method

'''
Write  a  program  to  add , subtract , multiply  and  divide  two  rational  numbers

1) 1st  rational  number  --->  2 / 3
    2nd  rational  number  --->   5 / 9
    What  is  the  sum  ?  --->  2 / 3 + 5 / 9 = (18 + 15) / 27 =  33 / 27 =  11 / 9
    What  is  the  difference  ?  --->  2 / 3 - 5 / 9 =  (18 - 15) / 27 =  3 / 27 =  1 / 9
    What  is  the  product  ?  --->	2 / 3 * 5 / 9 =  10 / 27  =  10 / 27
    What  is   the  division  ?  --->  2 / 3 /  5 / 9 =  2 / 3 * 9 / 5 =  18 / 15 =  6 / 5  --->  Succesful  division

2) 1st  rational  number  --->  2 / 3
    2nd  rational  number  --->   0 / 9
    What  is  the  sum  ?  --->  2 / 3 + 0 / 9 =  (18 + 0) / 27 =  18 / 27 =  2 / 3
    What  is  the  difference  ?  --->  2 / 3 - 0 / 9 =  (18 - 0) / 27 =  18 / 27 = 2 / 3
    What  is  the  product  ?  --->  2 / 3 * 0 / 9 =  0 / 27  --->  Simplification  is  not  required  becoz  numerator  is  0
    What  is   the  division  ?  --->  2 / 3 /  0 / 9 =  2 / 3 * 9 / 0 =  18 / 0  ---> Division  is  not   permitted

3) When  is  simplification  required ?  --->  When  numerator  is  non-zero'''

import math

class Rat:
    def get(self):
        self.num = int(input("Enter numerator: "))
        self.den = int(input("Enter denominator (non-zero): "))
        self.test()

    def test(self):
        while self.den == 0:
            print("Denominator cannot be zero.")
            self.den = int(input("Re-enter denominator: "))

    def __str__(self):
        return f"{self.num} / {self.den}"

    def add(self, a, b):
        self.num = a.num * b.den + b.num * a.den
        self.den = a.den * b.den
        self.simplify()

    def sub(self, a, b):
        self.num = a.num * b.den - b.num * a.den
        self.den = a.den * b.den
        self.simplify()

    def mul(self, a, b):
        self.num = a.num * b.num
        self.den = a.den * b.den
        self.simplify()

    def div(self, a, b):
        if b.num == 0:
            self.num = None  # invalid
            self.den = None
        else:
            self.num = a.num * b.den
            self.den = a.den * b.num
            self.simplify()

    def simplify(self):
        if self.num != 0:
            g = math.gcd(self.num, self.den)
            self.num //= g
            self.den //= g

# --- Main Program ---
a = Rat()
b = Rat()
c = Rat()
d = Rat()
e = Rat()
f = Rat()

print("\nEnter first rational number:")
a.get()
print("Enter second rational number:")
b.get()

c.add(a, b)
d.sub(a, b)
e.mul(a, b)
f.div(a, b)

print("\nSum        :", c)
print("Difference :", d)
print("Product    :", e)

if f.num is not None:
    print("Division   :", f)
else:
    print("Division is not permitted (division by zero).")
    


#  dir()  function  demo  program  (Home  work)
from trianglefunction import Rat
a = Rat()
a.nr = 22
a.dr = 7
print(dir(Rat))
print()
print(dir(a))    

#  Find  outputs  (Home  work)
class      Rat:
	def    m1():
		pass
# End  of  the  class
a = Rat()
a . nr = 22
print(hasattr(a , 'nr')) # True
print(hasattr(a , 'dr')) # False
print(hasattr(a , 'm1')) # True
print(hasattr(a , 'm2')) # False
print(hasattr(Rat , 'm1')) # True
print(hasattr(Rat , 'm2')) # False
print(hasattr(Rat , 'nr')) # False becoz nr is only objt of a not class
# Find  outputs  (Home  work)
class  Cat:
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
		x . talk() # Meow Meow Meow <next iteration> Mehar Mehar Mehar
	else:
		x . bark() # Bhow Bhow Bhow
#  Find  outputs  (Home  work)
class    c1:
        pass
# End of the class
a = c1()
a . x = 10
varname = input('Enter  variable  name  to  be  added  to  object  :  ')   #  Assume  that  input  is  'y'
value = eval(input('Enter  value  of  the  variable  :  '))   #  Assume  that  input  is   20
setattr(a , varname , value)
print(a . __dict__)
print(a . x) # 10
while  True:
	try:
		varname = input('Enter  variable  name  whose  value  is  to  be  retrieved  :  ')
									#  Assume  that  input  is  x  in  1st   iteration  ,  y  in   2nd   iteration  and  z  in  3rd  iteration
		print(getattr(a , varname))
	except:
		print(F'Invalid  variable   name   :  {varname}')
		break
'''o/p: Enter  variable  name  to  be  added  to  object  :  y
        Enter  value  of  the  variable  :  20
        {'x': 10, 'y': 20}
        10
        Enter  variable  name  whose  value  is  to  be  retrieved  :  x
        10
        Enter  variable  name  whose  value  is  to  be  retrieved  :  y
        20'''	
	
'''
(Home  work)
Write  a  program  to  convert  a  dictionary  {'Empno' : 25 , 'Ename' : 'Rama  Rao' , 'Sal' : 10000.0}  to  Emp  class  object
i.e.  object  should  contain  empno = 25 , ename = 'Rama  Rao' , Sal = 10000.0

Hint:  Use  setattr()  and  getattr()  functions
'''
class  Emp:
        pass
#End  of  the  class
emp_dict = {'Empno':25,'Ename':'Rama Rao','Sal':10000.0}
e = Emp()
for key,value in emp_dict.items():
	setattr(e,key,value)
for key in emp_dict:
	print(f'{key} : {getattr(e,key)}')	
	
'''o/p: Empno : 25
        Ename : Rama Rao
        Sal : 10000.0'''    