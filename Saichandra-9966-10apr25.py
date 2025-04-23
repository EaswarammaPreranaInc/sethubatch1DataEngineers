# proga. Write a program to determine total, average and grade of a student.
Inputs are Roll number,Student name, Marks of 3 subjectsb and Gender.
'''
class Student:
    def get(self):
        self.rno = int(input('Enter roll number: '))
        self.sname = input('Enter student name: ')
        self.gender = input('Enter gender: ')
        self.m = []
        for i in range(3):
            marks = int(input(f'Enter marks of subject {i+1}: '))
            self.m.append(marks)

    def compute(self):
        self.total = sum(self.m)
        self.avg = self.total / 3
        if min(self.m) < 40:
            self.grade = 'Fail'
        elif self.avg >= 70:
            self.grade = 'Distinction'
        elif self.avg >= 60:
            self.grade = 'First Class'
        elif self.avg >= 50:
            self.grade = 'Second Class'
        else:
            self.grade = 'Third Class'

    def disp(self):
        print('Roll Number:', self.rno)
        print('Student Name:', self.sname)
        print('Gender:', self.gender)
        print('Total Marks:', self.total)
        print(f'Average: {self.avg:.2f}')
        print('Grade:', self.grade)

    def __str__(self):
        return f"{self.rno} \t {self.sname} \t {self.gender} \t {self.total} \t {self.avg:.2f} \t {self.grade}"


# End of the class
s = Student()
s.get()
s.compute()
s.disp()
print(s)
'''



# What are the outputs if inputs are 25, Rama Rao, male, 52, 48, 55. (from prog import student)
'''
from proga. import student

s = student()   # Empty object
print(s.__dict__)   # {} 's' is an empty object
s.get()          # Reads inputs into object 's'
print(s.__dict__)   # {'rno' : 25, 'sname' : 'Rama rao', 'gender' : 'm', 'marks' : [52, 48, 55]
s.compute()      # stores results in object s
print(s.__dict__)   # {'rno' : 25, 'sname' : 'Rama rao', 'gender' : 'm', 'marks' : [52, 48, 55] 
                    # 'total' : 155, 'avg' : 51.66, 'grade' : 'Second class'
'''



# Repeat student program for 'n' students
1. Reuse student class defined in above prog but do not rewrite.
2. Use list of objects
'''
from Mod4prog9a import Student  # assuming your class is named Student in Mod4prog9a.py

n = int(input('How many students?: '))   # Read number of students
a = []

# Create and store 'n' Student class objects in list 'a'
for i in range(n):
    a.append(Student())

# Read each student's data
for idx, s in enumerate(a, start=1):
    print(f'\nStudent {idx}')
    s.get()

# Compute results for each student
for s in a:
    s.compute()

# Print each student's details
print("\n--- Student Results ---")
for s in a:
    print(s)
'''



# progb. Write a program to add, subtract, multiply and divide two rational numbers
1. 1st Rational number ---> 2/3    , 2nd rational number ---> 5/9
what is the sum ? ---> 2/3 + 5/9 = (18+15)/27 = 33/27 = 11/9
what is the difference ? ---> 2/3 - 5/9 = 18-15/27 = 3/27 = 1/9
what is the product ? ---> 2/3 * 5/9 = 10/27
what is the divison ? ---> 2/3 / 5/9 = 2/3 * 5/9 = 18/15 = 6/5   ---> Successfull divison and return True

2.  1st Rational number ---> 2/3    , 2nd rational number ---> 0/9
what is the sum ? ---> 2/3 + 0/9 = (18+0)/27 = 18/27 = 2/3
what is the difference ? ---> 2/3 - 0/9 = 18-0/27 = 18/27 = 2/3
what is the product ? ---> 2/3 * 0/9 = 0/27
what is the divison ? ---> 2/3 / 0/9 = 2/3 * 9/0 = 18/0 

3. When is simplification required ? ---> when numerator is non-zero

4. What does div() method return? ---> True when division is successful and false otherwise

'''
import math
class Rat:
    def get(self):
        self.nr = int(input('Enter numerator: '))
        self.dr = int(input('Enter denominator: '))
        self.test()

    def test(self):
        while self.dr == 0:
            self.dr = int(input('Denominator cannot be zero, reenter: '))

    def __str__(self):
        return f'{self.nr} / {self.dr}'

    def add(self, a, b):
        self.nr = a.nr * b.dr + a.dr * b.nr
        self.dr = a.dr * b.dr
        self.simplify()

    def sub(self, a, b):
        self.nr = a.nr * b.dr - a.dr * b.nr
        self.dr = a.dr * b.dr
        self.simplify()

    def mul(self, a, b):
        self.nr = a.nr * b.nr
        self.dr = a.dr * b.dr
        self.simplify()

    def div(self, a, b):
        self.nr = a.nr * b.dr
        self.dr = a.dr * b.nr  # Corrected!
        self.simplify()

    def simplify(self):
        if self.nr != 0:
            ans = math.gcd(self.nr, self.dr)
            self.nr = self.nr // ans
            self.dr = self.dr // ans

# End of class

if __name__ == '__main__':
    a = Rat()
    b = Rat()
    c = Rat()
    d = Rat()
    e = Rat()
    f = Rat()

    a.get()
    b.get()

    c.add(a, b)
    d.sub(a, b)
    e.mul(a, b)

    print('Sum:', c)
    print('Difference:', d)
    print('Product:', e)

    if b.nr != 0:
        f.div(a, b)
        print('Division:', f)
    else:
        print('Division is not permitted')
'''



Repeat progb. with 3 objects
Eg. c = a + b
       print c
       c = a - b
       print c
       c = a * b
       print c
       c = a / b
       print c
Hint : Reuse rat class defined in progb but do not define rat class again
'''
from progb import Rat

a = Rat()
b = Rat()
c = Rat()

a.get()
b.get()

c.add(a, b)
print(f'Addition: {c}')

c.sub(a, b)
print(f'Subtraction: {c}')

c.mul(a, b)
print(f'Multiplication: {c}')

if b.nr == 0:
    print('Division is not permitted')
else:
    c.div(a, b)
    print(f'Division: {c}')
'''



# progc (list of objects)
Repeat proga with list of 6 subjects
Hint: Reuse Rat class defined in proga but do not rewrite the class again
what are the object names ? ---> a[0], a[1], a[2], .....a[5]
'''
from Mod4prog10a import Rat
a = [Rat(), Rat(), Rat(), Rat(), Rat(), Rat()]
a[0].get()  # How to read rational number into 1st object
a[1].get()  # How to read rational number into 2nd object
a[2].add(a[0], a[1])  # How to add rational numbers in first two objects and store results in 3rd object
a[3].sub(a[0], a[1])  # How to sub rational numbers in first two objects and store results in 4th object
a[4].mul(a[0], a[1])  # How to multiply rational numbers in first two objects and store results in 5th object
print('sum:',a[2])   # How to print 3rd object
print('Difference:', a[3])   # How to print 4th object
print('Product:', a[4])   # How to print 5thb object
if a[1].nr == 0:
	print('Division is not permitted')
else:
	a[5].div(a[0], a[1]) # How to print 6th object
'''
def add(self, a, b):
             pass
a[2].add(a[0], a[1])
'''



# import from progb dir() function demo program
from progb import Rat
a = Rat()   # Empty object
a.nr = 22   # adds variable nr to object 'a' with value 22
a.dr = 7    # adds variable dr to object 'a' with value 7
print(dir(Rat))   # ['add', 'div', 'get', 'mul', 'simplify', 'sub', 'test', '__str__', environment variables]
print()
print()
print(dir(a))  # ['add', 'div', 'get', 'mul', 'simplify', 'sub', 'test', '__str__', environment variables, nr, dr]




