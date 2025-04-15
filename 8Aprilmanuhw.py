'''
#1) from manu . triangle import*
triangle = triangle()   #  How  to  create  triangle  object
triangle.get() # How  to  call  get()  method  in  another  way
if triangle. test():#How  to  call  test()  method  in  another  way
	print('Area : ', triangle.area ())
	print('Perimeter : ',  triangle.peri())

#2)      Write  a  program  to  determine  total , average  and  grade  of  a  student
Inputs  are  Roll Number , Stud  Name , Marks  of  3  subjects  and  Gender

class   Student:
	def   get(self):
		How  to  read  roll  number  into  object  self
		How  to  read  student  name  into  object  self
		How  to  read  gender  into  object  self
		How  to  read  marks  of  3  subjects
	def   compute(self):
		How  to  calculate  total  marks
		How  to  calculate  average  marks
		if  At  least  one  subject  is  below  40:
				How  to  initilaize  grade  to  'Fail'
		elif  average  is  above  >= 70%:
				How  to  initilaize  grade  to  'Distinction'
		elif  average  is  above  >= 60%:
				How  to  initilaize  grade  to  'First  class'
		elif  average  is  above  >= 50%:
				How  to  initilaize  grade  to  'Second  class'
		else:
				How  to  initilaize  grade  to  'Third  class'
	def  disp(self):
		print('Roll  Number  :  ' ,   ???)
		print('Student  Name  :  ' , ???)
		print('Gender  :  ' ,  ???)
		print('Total  Marks  :  ' , ???)
		print('Average  :  ' , ???)
		print('Grade  :  ' , ???)
	def   _str_(self):
		return  All  the   values  of  object  self  in  the  form  of  string
#End  of  the  class
How  to  create  Student  class  object
How  to  read  inputs  into  object
How  to  store  results  in  object
How  to  print  object  with  disp()  method
How  to  print  object  with  _str_()  method



class Student:
    def __init__(self):
        # Initialize the attributes to store student details
        self.roll_number = ""
        self.name = ""
        self.gender = ""
        self.marks = []
        self.total_marks = 0
        self.average = 0
        self.grade = ""

    def get(self):
        # Read roll number, student name, gender, and marks for 3 subjects
        self.roll_number = input("Enter Roll Number: ")
        self.name = input("Enter Student Name: ")
        self.gender = input("Enter Gender: ")
        self.marks = []
        for i in range(3):
            mark = float(input(f"Enter marks for subject {i + 1}: "))
            self.marks.append(mark)

    def compute(self):
        # Calculate total marks and average
        self.total_marks = sum(self.marks)
        self.average = self.total_marks / 3
        
        # Determine grade based on the conditions
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
        # Display the details of the student
        print('Roll Number: ', self.roll_number)
        print('Student Name: ', self.name)
        print('Gender: ', self.gender)
        print('Total Marks: ', self.total_marks)
        print('Average: ', self.average)
        print('Grade: ', self.grade)

    def __str__(self):
        # Return string representation of the student object
        return f"Roll Number: {self.roll_number}, Name: {self.name}, Gender: {self.gender}, Total Marks: {self.total_marks}, Average: {self.average}, Grade: {self.grade}"

# Main program to create and work with Student object
# 1. Create a Student object
student1 = Student()

# 2. Read inputs into the student object
student1.get()

# 3. Store results and compute the grade
student1.compute()

# 4. Print student details using disp() method
student1.disp()

# 5. Print student details using __str__() method
print(student1)  # This will automatically call the __str__ method

outputs:-
--------
Enter Roll Number: 23
Enter Student Name: ramesh
Enter Gender: male
Enter marks for subject 1: 60
Enter marks for subject 2: 58
Enter marks for subject 3: 98
Roll Number:  23
Student Name:  ramesh
Gender:  male
Total Marks:  216.0
Average:  72.0
Grade:  Distinction
Roll Number: 23, Name: ramesh, Gender: male, Total Marks: 216.0, Average: 72.0, Grade: Distinction


#3)Write  a  program  to  add , subtract , multiply  and  divide  two  rational  numbers

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

import  math
class  Rat:
	def  get(self):
		How  to  read  numerator  into  object  self
		How  to  read  denominator  into  object  self
		How  to  call  test()  method
	def  test(self):
		Ask  user  to  reenter  denom  when  denom  is  zero
	def    _str_(self):
			 return  values  of  object  in  the  form  of  rational  number  such   as  '2 / 3'
	def   add(self , a , b):
		How  to  add  objects  'a'  and  'b' and  store  results  in  object  self
		How  to  simplify  object  self
	
	c . add(a , b)
	object  a  --->  2 / 3
	object  b  --->  5 / 9
	object  c  --->  2 / 3 + 5 / 9 = (2 * 9 + 5 * 3) / (5 * 9) = 33 / 27 = 11 / 9
	
	def   sub(self , a , b):
		How  to  subtract  objects  'a'  and  'b' and  store  results  in  object  self
		How  to  simplify  object  self
	
	d . sub(a , b)
	object  a  --->  2 / 3
	object  b  --->  5 / 9
	object  d  --->  2 / 3 - 5 / 9 = (2 * 9 - 5 * 3) / (5 * 9) = 3 / 27 = 1 / 9
	
	def   mul(self , a , b):
		How  to  multiply  objects  'a'  and  'b' and  store  results  in  object  self
		How  to  simplify  object  self
	
	e . mul(a , b)
	object  a  --->  2 / 3
	object  b  --->  5 / 9
	object  e  --->  2 / 3 * 5 / 9 = (2 * 5) / (3 * 9) = 10 / 27
	
	def    div(self , a , b):
		How  to  divide  objects  'a'  and  'b' and  store  results  in  object  self
		How  to  simplify  object  self
	
	f . div(a , b)
	object  a  --->  2 / 3
	object  b  --->  5 / 9
	object  f  --->  2 / 3 / 5 / 9 = 2 / 3 * 9 / 5 = (2 * 9) / (3 * 5) = 18 / 15 = 6 / 5
	
	def   simplify(self):
			How  to  find  gcd  of  numerator  and   denominator
			How  to  simplify  rational  number  in  object  self  i.e.  12 / 15  should  be  simplified  to  4 / 5
	
	c . simplify()
	1)  12 / 15  --->  4 / 5
	2) 10 / 27   --->  10 / 27
	3) 0 / 27  --->   0 / 27
	
# End  of the class
How  to  create  6  objects  a , b , c , d , e , f
How  to  read  rational  number  into  object  'a'
How to  read  rational  number  into  object  'b'
How  to  add  rational  numbers  in  objects  a  and  b  and  store  results  in  object  'c'
How  to  subtract  rational  numbers  in  objects  a  and  b  and  store  results  in  object  'd'
How  to multiply  rational  numbers  in  objects  a  and  b  and  store  results  in  object  'e'
How  to  divide  rational  numbers  in  objects  a  and  b  and  store  results  in  object  'f'
How  to  print  object   'c'
How  to  print  object   'd'
How  to  print  object   'e'
if  ???
	How  to  print  object  'f
else:
	print('Division  is  not  permitted')



import math

class Rat:
    def __init__(self):
        self.numerator = 0
        self.denominator = 0

    def get(self):
        # Read the numerator and denominator into the object
        self.numerator = int(input("Enter numerator: "))
        self.denominator = int(input("Enter denominator: "))
        
        # Call the test() method to check if the denominator is zero
        self.test()

    def test(self):
        # If the denominator is zero, ask the user to reenter it
        while self.denominator == 0:
            print("Denominator cannot be zero!")
            self.denominator = int(input("Reenter denominator: "))
        
    def __str__(self):
        # Return the rational number in the form of 'numerator / denominator'
        return f"{self.numerator} / {self.denominator}"

    def add(self, a, b):
        # Add two rational numbers a and b, and store the result in the current object (self)
        # a = self, b = another Rat object
        common_denominator = a.denominator * b.denominator
        new_numerator = (a.numerator * b.denominator) + (b.numerator * a.denominator)
        
        # Store the result in the current object
        self.numerator = new_numerator
        self.denominator = common_denominator
        
        # Simplify the result
        self.simplify()

    def simplify(self):
        # Simplify the fraction by dividing both numerator and denominator by their GCD
        gcd = math.gcd(self.numerator, self.denominator)
        self.numerator //= gcd
        self.denominator //= gcd

# Main program
# Create two Rat objects
rat1 = Rat()
rat2 = Rat()

# Read values into the objects
print("Enter details for the first rational number:")
rat1.get()
print("Enter details for the second rational number:")
rat2.get()

# Display the original rational numbers
print("First Rational Number:", rat1)
print("Second Rational Number:", rat2)

# Add the two rational numbers and store the result in rat1
rat1.add(rat1, rat2)

# Display the result of the addition
print("Sum of the two rational numbers:", rat1)

outputs:-
--------
Enter details for the first rational number:
Enter numerator: 1
Enter denominator: 2
Enter details for the second rational number:
Enter numerator: 4
Enter denominator: 5
First Rational Number: 1 / 2
Second Rational Number: 4 / 5
Sum of the two rational numbers: 13 / 10


#4)dir()  function  demo  program  (Home  work)
from  prog10a   import  Rat
a = Rat()
a . nr = 22
a . dr = 7
print(dir(Rat))
print()
print()
print(dir(a))

 #5)Find  outputs  (Home  work)
class      Rat:
	def    m1():
		pass
# End  of  the  class
a = Rat()
a . nr = 22
print(hasattr(a , 'nr')) #True
print(hasattr(a , 'dr')) # False
print(hasattr(a , 'm1')) # True
print(hasattr(a , 'm2')) # False
print(hasattr(Rat , 'm1')) # True
print(hasattr(Rat , 'm2')) # False
print(hasattr(Rat , 'nr')) # False


#6) Find  outputs  (Home  work)
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
		x . talk()
	else:
		x . bark()

output:-
----------
Meow Meow Meow ....
Bhow Bhow Bhow ....
Mehar  Mehar  Mehar  ....



#7) Find  outputs  (Home  work)
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
'''
#8) Find  outputs  (Home  work)
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






outputs:-
-------------

Enter  variable  name  to  be  added  to  object  :  u
Enter  value  of  the  variable  :  60
{'x': 10, 'u': 60}
10
Enter  variable  name  whose  value  is  to  be  retrieved  :  u
60
Enter  variable  name  whose  value  is  to  be  retrieved  :  x
10
Enter  variable  name  whose  value  is  to  be  retrieved  :  u
60
Enter  variable  name  whose  value  is  to  be  retrieved  :  6
Invalid  variable   name   :  6
Press any key to continue . . .

