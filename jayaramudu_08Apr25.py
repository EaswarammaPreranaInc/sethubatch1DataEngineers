'''
Repeat  prog5a  such  that  methods  are  called  in  another  way

1) What  are  the  two  ways  to  call  a  method ?  --->  object . method()  and  classname . method(object)

2) Import  and   use  triangle  class  defined  in  prog5a  but  do  not   define  triangle  class  again
'''
import sys
sys.path.append('D:\\python\\Programs\\07-04-25-HW')

import traingle


a=traingle.triangle() # How  to  create  triangle  object
a.get() # How  to  call  get()  method  in  another  way
a.test() # How  to  call  test()  method  in  another  way
print('Area : ',  a.area())  # How  to  call  area()  method  in  another  way
print('Perimeter: ',  a.peri()) # How  to  call  peri()  method  in  another way


#Ex-2
'''
Write  a  program  to  determine  total , average  and  grade  of  a  student
Inputs  are  Roll Number , Stud  Name , Marks  of  3  subjects  and  Gender
'''
class   Student:
	def   get(self):
		self.rno =eval(input('Enter a roll number: ')) # How  to  read  roll  number  into  object  self
		self.sname=input('Enter a Student name: ')# How  to  read  student  name  into  object  self
		self.gender=input('Enter a genter: ') #How  to  read  gender  into  object  self
		self.m=eval(input('Enter a list of marks 3: ')) # How  to  read  marks  of  3  subjects
	def   compute(self):
		self.tot=sum(self.m) # How  to  calculate  total  marks
		self.average=sum(self.m)/len(self.m)#How  to  calculate  average  marks
		if self.average < 40: # At  least  one  subject  is  below  40
				self.grade='Fail'  #How  to  initilaize  grade  to  'Fail'
		elif  self.average  >= 70:    #    average  is  above  >= 70%
				self.grade=  'Distinction' # How  to  initilaize  grade  to  'Distinction'
		elif   self.average    >= 60: # average  is  above  >= 60%
				 self.grade= 'First  class' # How  to  initilaize  grade  to  'First  class'
		elif  self.average  >= 50:  # average  is  above  >= 50%
				self.grade='Second  class' # How  to  initilaize  grade  to 'Second  class'
		else:
				self.grade='Third class' # How  to  initilaize  grade  to  'Third  class'
	def  disp(self):
		print('Roll  Number  :  ' ,   self.rno)
		print('Student  Name  :  ' , self.sname)
		print('Gender  :  ' ,  self.gender)
		print('Total  Marks  :  ' , self.tot)
		print('Average  :  ' , self.average)
		print('Grade  :  ' , self.grade)
	def   _str_(self):
		return  F'Roll  Number: {self.rno} Student  Name: {self.sname}  Gender:{self.gender} Total Marks: {self.tot} Average: {self.average} Grage:{self.grade} '# All  the   values  of  object  self  in  the  form  of  string
#End  of  the  class
a=Student()# How  to  create  Student  class  object
a.get() # How  to  read  inputs  into  object
a.compute()# How  to  store  results  in  object
a.disp() # How  to  print  object  with  disp()  method
print(a._str_()) # How  to  print  object  with  _str_()  method

#Ex-3
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

3) When  is  simplification  required ?  --->  When  numerator  is  non-zero
'''

import math

class Rat:
    def get(self):
        self.num = int(input("Enter numerator: "))  # Read numerator into object self
        self.den = int(input("Enter denominator: "))  # Read denominator into object self
        while self.den == 0:  # Check for zero denominator
            self.test()  # Call test() method

    def test(self):  # Ask user to reenter denom when denom is zero
        print("Denominator cannot be zero. Please re-enter.")
        self.den = int(input("Enter denominator again: "))
        while self.den == 0:  # Ensure the denominator is not zero
            print("Denominator cannot be zero. Please re-enter.")
            self.den = int(input("Enter denominator again: "))

    def __str__(self):  # Corrected method name
        return f"{self.num} / {self.den}"  # Values of object in the form of rational number

    def add(self, a, b):
        self.num = a.num * b.den + b.num * a.den  # Add objects 'a' and 'b' and store results in object self
        self.den = a.den * b.den
        self.simplify()  # Simplify object self

    def sub(self, a, b):
        self.num = a.num * b.den - b.num * a.den  # Subtract objects 'a' and 'b' and store results in object self
        self.den = a.den * b.den
        self.simplify()  # Simplify object self

    def mul(self, a, b):
        self.num = a.num * b.num  # Multiply objects 'a' and 'b' and store results in object self
        self.den = a.den * b.den
        self.simplify()  # Simplify object self

    def div(self, a, b):
        if b.num == 0:  # Check if the numerator of b is zero
            self.num = None
            self.den = None
        else:
            self.num = a.num * b.den  # Divide objects 'a' and 'b' and store results in object self
            self.den = a.den * b.num
            self.simplify()  # Simplify object self

    def simplify(self):  # Find gcd of numerator and denominator
        if self.num == 0:
            self.den = 1  # 0/x is already simplest, set denominator to 1
            return
        gcd = math.gcd(self.num, self.den)
        self.num //= gcd
        self.den //= gcd  # Simplify rational number in object self

# Create 6 objects a, b, c, d, e, f
a = Rat()
b = Rat()
c = Rat()
d = Rat()
e = Rat()
f = Rat()

a.get()  # Read rational number into object 'a'
b.get()  # Read rational number into object 'b'
c.add(a, b)  # Add rational numbers in objects a and b and store results in object 'c'
d.sub(a, b)  # Subtract rational numbers in objects a and b and store results in object 'd'
e.mul(a, b)  # Multiply rational numbers in objects a and b and store results in object 'e'
f.div(a, b)  # Divide rational numbers in objects a and b and store results in object 'f'

print("Sum:", c)  # Print object 'c'
print("Difference:", d)  # Print object 'd'
print("Product:", e)  # Print object 'e'
if f.num is not None:
    print("Division:", f)  # Print object 'f'
else:
    print("Division is not permitted")

#Ex-4
#  dir()  function  demo  program  (Home  work)
from  prog10   import  Rat
a = Rat()
a . nr = 22
a . dr = 7
print(dir(Rat)) # Methods of class and Environment variables
print()
print()
print(dir(a)) # variables of Methods of class  object and Environment variables


#Ex-5
#  Find  outputs  (Home  work)
class Rat:
  #def m1(): # Error because formal argument must be thire
        #pass
    pass
# End  of  the  class
a = Rat()
a . nr = 22
print(hasattr(a , 'nr'))  # True because nr present object a
print(hasattr(a , 'dr')) # False because dr not present object a
print(hasattr(a , 'm1')) # False m1  not present in an object
print(hasattr(a , 'm2')) # False because m1 not present
print(hasattr(Rat , 'm1')) # False because m1 not present in a class
print(hasattr(Rat , 'm2')) # False because m2 not present in a  class
print(hasattr(Rat,'nr')) # False because nr not present in a class


#Ex-6
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
	if   hasattr(x , 'talk'): # cat() is True          # Dog() False      # Goat()
		x . talk()            # Meow Meow Meow ....                       # Mehar Mehar Mehar ....
	else:
		x.bark()  # Dog Bhow Bhow Bhow ....


#Ex-7
#  Find  outputs  (Home  work)
class    c1:
        pass
# End of the class
a = c1()
a . x = 10
varname = input('Enter  variable  name  to  be  added  to  object  :  ')   #  Assume  that  input  is  'y'
value = eval(input('Enter  value  of  the  variable  :  '))   #  Assume  that  input  is   20
setattr(a , varname , value) # setattr(a,y,20)
print(a . __dict__) # {'x':10,'y':20}
print(a . x) # 10
while  True:
	try:
		varname = input('Enter  variable  name  whose  value  is  to  be  retrieved  :  ')
									#  Assume  that  input  is  x  in  1st   iteration  ,  y  in   2nd   iteration  and  z  in  3rd  iteration
		print(getattr(a , varname)) # 10  and 20
	except:
		print(F'Invalid  variable   name   :  {varname}') # Invalid variable name :  z
		break


#Ex-8
'''
(Home  work)
Write  a  program  to  convert  a  dictionary  {'Empno' : 25 , 'Ename' : 'Rama  Rao' , 'Sal' : 10000.0}  to  Emp  class  object
i.e.  object  should  contain  empno = 25 , ename = 'Rama  Rao' , Sal = 10000.0

Hint:  Use  setattr()  and  getattr()  functions
'''
class  Emp:
        pass
#End  of  the  class
dict = {'Empno' : 25 , 'Ename' : 'Rama  Rao' , 'Sal' : 10000.0}
e = Emp()
for x in dict.keys():
     setattr(e,x,dict[x])# How  to  convert  dictionary  to  object  'e'  with  for  loop
for x in e.__dict__:
    print(F"{x} : {getattr(e, x)}") # How  to  print  object  'e' with  for loop
