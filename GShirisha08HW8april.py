#Repeat  prog5a  such  that  methods  are  called  in  another  way
#1) What  are  the  two  ways  to  call  a  method ?  --->  object . method()  and  classname . method(object)
#2) Import  and   use  triangle  class  defined  in  prog5a  but  do  not   define  triangle  class  again
#How  to  create  triangle  object
#How  to  call  get()  method  in  another  way
#How  to  call  test()  method  in  another  way
#print('Area : ',  How  to  call  area()  method  in  another  way)
#print('Perimeter: ',  How  to  call  peri()  method  in  another  way)

from import5aHw8april import triangle
t=triangle()
triangle.get(t)
triangle.test(t)
print('Area : ',   triangle.area(t))
print('Perimeter : ',  triangle.peri(t))

#output:
Enter the first side of the triangle:5
Enter the second side of the triangle:4
Enter the third side of the triangle:6
Area :  14.031215200402281
Perimeter :  15



#Write  a  program  to  determine  total , average  and  grade  of  a  student
#Inputs  are  Roll Number , Stud  Name , Marks  of  3  subjects  and  Gender

class   student:
	def   get(self):
		self.rno= eval(input('Enter roll number:'))    #How  to  read  roll  number  into  object  self
		self.sname=input('Enter student name:')    #How  to  read  student  name  into  object  self
		self.gender=input('Enter gender(m/f):')  #How  to  read  gender  into  object  self
		self.m= []     #How  to  read  marks  of  3  subjects
		for i in range(3):
			marks=int(input('Enter marks of subject{i+1}:'))
			self.m.append(marks)
	def   compute(self): 
		self.tot=sum(self.m) #How  to  calculate  total  marks
		self.avg=self.tot/3  #How  to  calculate  average  marks
		if  min(self.m)<40:  #At  least  one  subject  is  below  40:
				self.grade='Fail' #How  to  initilaize  grade  to  'Fail'
		elif  self.avg>=70:    # average  is  above  >= 70%:
				self.grade='Distincton' # How  to  initilaize  grade  to  'Distinction'
		elif  self.avg>=60:   #average  is  above  >= 60%:
				self.grade='First class'  #How  to  initilaize  grade  to  'First  class'
		elif  self.avg>=50:    #average  is  above  >= 50%:
				self.grade='Second class'  #How  to  initilaize  grade  to  'Second  class'
		else:
				self.grade='Third class' #How  to  initilaize  grade  to  'Third  class'
	def  disp(self):
		print('Roll  Number  :  ' ,   self.rno)
		print('Student  Name  :  ' , self.sname)
		print('Gender  :  ' ,  self.gender)
		print('Total  Marks  :  ' , self.tot)
		print(f'Average  :  , {self.avg:.2f}')
		print('Grade  :  ' , self.grade)
	def   __str__(self):
		return f'{self.rno} \t {self.sname} \t {self.gender} \t {self.tot} \t {self.avg:.2f} \t {self.grade}' # All  the   values  of  object  self  in  the  form  of  string
#End  of  the  class
s=student() #defHow  to  create  Student  class  object
s.get() #How  to  read  inputs  into  object
s.compute() #How  to  store  results  in  object
s.disp() #How  to  print  object  with  disp()  method
print(s) #How  to  print  object  with  _str_()  method

output:
Enter roll number:1
Enter student name:Rama Rao
Enter gender(m/f):m
Enter marks of subject{i+1}:80
Enter marks of subject{i+1}:70
Enter marks of subject{i+1}:90
Roll  Number  :   1
Student  Name  :   Rama Rao
Gender  :   m
Total  Marks  :   240
Average  :  , 80.00
Grade  :   Distincton
1        Rama Rao        m       240     80.00   Distincton



#add, subtract, multiply and divide two rational numbers
import math
class Rat:
	def get(self):
		self.nr=int(input('nr : ')) #Read numerator into object self
		self.dr=int(input('dr : ')) #Read denominator into object self
		self.test()
	def test(self):
		if self.dr==0:
			self.dr=int(input('Enter denominator value other than zero: '))
	def __str__(self):
		return F'{self.nr}/{self.dr}'
	def add(self,a,b):
		self.nr=(a.nr*b.dr+a.dr*b.nr)
		self.dr=(a.dr*b.dr)
		x=self.simplify()
		self.nr,self.dr=self.nr//x,self.dr//x
	def sub(self,a,b):
		self.nr=(a.nr*b.dr-a.dr*b.nr)
		self.dr=(a.dr*b.dr)
		x=self.simplify()
		self.nr,self.dr=self.nr//x,self.dr//x
	def mul(self,a,b):
		self.nr=(a.nr*b.nr)
		self.dr=(a.dr*b.dr)
		x=self.simplify()
		self.nr,self.dr=self.nr//x,self.dr//x
	def div(self,a,b):
		self.nr=(a.nr*b.dr)
		self.dr=(a.dr*b.nr)
		x=self.simplify()
		self.nr,self.dr=self.nr//x,self.dr//x
	def simplify(self):
		return math.gcd(self.nr,self.dr)
#End of the class
a=Rat()
print('First rational number')
a.get()
print('a :',a)
b=Rat()
print('Second rational number')
b.get()
print('b :',b)
c,d,e,f=Rat(),Rat(),Rat(),Rat()
c.add(a,b) #add 2 rational numbers a and b
d.sub(a,b) #subtaract rational numbers
e.mul(a,b) #multiply 2 rational numbers
f.div(a,b) #divide 2 rational numbers
print(c)
print(d)
print(e)
print(f)

#Output
First rational number
nr : 2
dr : 3
a : 2/3
Second rational number
nr : 5
dr : 9
b : 5/9
11/9
1/9
10/27
6/5


#dir() function demo program
from April8 import Rat
a=Rat()
a.nr=22
a.dr=7
print(dir(Rat)) #list of environment variables and methods in the form of strings
print()
print()
print(dir(a)) #list of environment variables, instance variables and methods in the form of strings

#Output
['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'add', 'div', 'get', 'mul', 'simplify', 'sub', 'test']
['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'add', 'div', 'dr', 'get', 'mul', 'nr', 'simplify', 'sub', 'test']


#Find outputs
class Rat:
	def m1():
		pass
a=Rat()
a.nr=22
print(hasattr(a,'nr')) #True
print(hasattr(a,'dr')) #False
print(hasattr(a,'m1')) #True
print(hasattr(a,'m2')) #False
print(hasattr(Rat,'m1')) #True
print(hasattr(Rat,'m2')) #False
print(hasattr(Rat,'nr')) #False


#Find outputs
class Cat:
	def talk(self):
		print('Meow Meow Meow ....')
class Dog:
	def bark(self):
		print('Bhow Bhow Bhow ....')
class Goat:
	def talk(self):
		print('Mehar Mehar Mehar ....')
#End of the class
a=[Cat(),Dog(),Goat()]
for x in a:
	if hasattr(x,'talk'):
		x.talk()
	else:
		x.bark()

#Output
Meow Meow Meow ....
Bhow Bhow Bhow ....
Mehar Mehar Mehar ....


#Find outputs
class c1:
	pass
#End of the class
a=c1()
a.x=10
varname=input('Enter variable name to be added to object : ') 
value=eval(input('Enter value of the variable : '))
setattr(a,varname,value)
print(a.__dict__)
print(a.x)
while True:
	try:
		varname=input('Enter variable name whose value is to be retrived : ')
		print(getattr(a,varname))
	except:
		print(F'Invalid variable name : {varname}')
		break

#Output
Enter variable name to be added to object : y
Enter value of the variable : 25
{'x': 10, 'y': 25}
10
Enter variable name whose value is to be retrived : y
25
Enter variable name whose value is to be retrived : z
Invalid variable name : z


#convert a dictionary {'Empno':25, 'Ename':'Rama Rao', 'Sal':10000.0} to Emp class object
#i.e. object should contain empno=25,ename='Rama Rao', Sal=10000.0
class c1:
	pass
#End of the class
a=c1()
d={'Empno':25, 'Ename':'Rama Rao', 'Sal':10000.0}
for x in d:
	setattr(a,x,d[x])
for x in d:
	print(F'{x} = {getattr(a,x)}')

#Output
Empno = 25
Ename = Rama Rao
Sal = 10000.0
