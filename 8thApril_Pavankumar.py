'''
PROGRAM_1:
Repeat  prog5a  such  that  methods  are  called  in  another  way

1) What  are  the  two  ways  to  call  a  method ?  --->  object . method()  and  classname . method(object)

2) Import  and   use  triangle  class  defined  in  prog5a  but  do  not   define  triangle  class  again
'''
'''
from progtriangle import triangle 
obj1=triangle()
obj1.get()
obj1.test()
print('Area : ',triangle.area(obj1))
print('Perimeter: ',triangle.peri(obj1))
'''
'''
OUTPUT:
Enter side a : 3
Enter side b : 4
Enter side c : 5
Area :  6.0
Perimeter:  12
'''
'''
PROGRAM_2:

Write  a  program  to  determine  total , average  and  grade  of  a  student
Inputs  are  Roll Number , Stud  Name , Marks  of  3  subjects  and  Gender
'''
class   Student:
	def   get(self):
		self.rollnum=int(input("Enter Roll Number    : "))
		self.stu_name=input("Enter student name   : ")
		self.gender=input("Enter gender name    : ")
		self.marks=[]
		for i in range(3):
			self.marks.append(eval(input("Enter list of marks  : ")))
	def   compute(self):
		self.total=sum(self.marks)
		self.average=self.total/len(self.marks)
		if  min(self.marks)<40:
			     self.grade="Fail"
		elif  self.average>=70:
				 self.grade='Distinction'
		elif  self.average>= 60:
				 self.grade='First  class'
		elif  self.average>= 50:
				 self.grade='Second  class'
		else:
			     self.grade='Third  class'
	def  disp(self):
		print('Roll  Number   :  ' ,self.rollnum)
		print('Student  Name  :  ' ,self.stu_name)
		print('Gender         :  ' ,self.gender)
		print('Total  Marks   :  ' ,self.total)
		print('Average        :  ' ,self.average)
		print('Grade          :  ' ,self.grade)
	def   __str__(self):
		return  f'Roll Number: {self.rollnum},Student Name: {self.stu_name},Gender : {self.gender},Total Marks: {self.total},TotalMarks: {self.total},Average: {self.average},Grade: {self.grade}'
if __name__=="__main__":
		obj=Student()
		obj.get()
		obj.compute()
		obj.disp()
		print(obj)
'''
OUTPUT:
Enter Roll Number    : 79
Enter student name   : Pavan
Enter gender name    : m
Enter list of marks  : 47
Enter list of marks  : 56
Enter list of marks  : 77
Roll  Number   :   79
Student  Name  :   Pavan
Gender         :   m
Total  Marks   :   180
Average        :   60.0
Grade          :   First  class
Roll  Number : 79,Student  Name  : Pavan,Gender : m,Total  Marks : 180,Total  Marks : 180,Average : 60.0,Grade : First  class
'''
#  Find  outputs  (Home  work)
class      Rat:
	def    m1():
		pass
if __name__=="__main__":
		a = Rat()
		a . nr = 22
		print(hasattr(a , 'nr'))
		print(hasattr(a , 'dr'))
		print(hasattr(a , 'm1'))
		print(hasattr(a , 'm2'))
		print(hasattr(Rat,'m1'))
		print(hasattr(Rat,'m2'))
		print(hasattr(Rat,'nr'))
'''
OUTPUT:
True
False
True
False
True
False
False
'''
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
if __name__=="__main__":
	a=[Cat(),Dog(),Goat()]
	for  x  in   a:
		if   hasattr(x,'talk'):
			x.talk()
		else:
		    x.bark()
'''
OUTPUT:
Meow Meow Meow ....
Bhow Bhow Bhow ....
Mehar  Mehar  Mehar  ....
'''
#  Find  outputs  (Home  work)
class    c1:
        pass
a = c1()
a . x = 10
if __name__=="__main__":
	varname = input('Enter  variable  name  to  be  added  to  object  :  ')   #  Assume  that  input  is  'y'
	value = eval(input('Enter  value  of  the  variable  :  '))   #  Assume  that  input  is   20
	setattr(a , varname , value)
	print(a . __dict__)
	print(a . x)
	while  True:
		try:
			varname = input('Enter  variable  name  whose  value  is  to  be  retrieved  :  ')
										#  Assume  that  input  is  x  in  1st   iteration  ,  y  in   2nd   iteration  and  z  in  3rd  iteration
			print(getattr(a , varname))
		except:
			print(F'Invalid  variable   name   :  {varname}')
			break
'''
OUTPUT:
Enter  variable  name  to  be  added  to  object  :  y
Enter  value  of  the  variable  :  20
{'x': 10, 'y': 20}
10
Enter  variable  name  whose  value  is  to  be  retrieved  :  x
10
Enter  variable  name  whose  value  is  to  be  retrieved  :  y
20
Enter  variable  name  whose  value  is  to  be  retrieved  :  z
Invalid  variable   name   :  z
'''
'''
PROGRAM_3:
Write  a  program  to  convert  a  dictionary  {'Empno' : 25 , 'Ename' : 'Rama  Rao' , 'Sal' : 10000.0}  to  Emp  class  object
i.e.  object  should  contain  empno = 25 , ename = 'Rama  Rao' , Sal = 10000.0

Hint:  Use  setattr()  and  getattr()  functions
'''
class  Emp:
        pass
dict = {'Empno' : 25 , 'Ename' : 'Rama  Rao' , 'Sal' : 10000.0}
e=Emp()
if __name__=="__main__":
	for i,j in dict.items():
		setattr(e,i,j)
	for i in dict.keys():
		print(getattr(e,i))
'''
OUTPUT:
25
Rama  Rao
10000.0
'''
'''
PROGRAM_3:

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
import  math
class  Rat:
	def  get(self):
		self.nr=eval(input("Enter numerator : "))
		self.dr=eval(input("Enter denominator : "))
		self.test()
	def  test(self):
		while True:
			if self.dr==0:
				print("Re-enter the denominator value : ")
				self.dr=eval(input("Enter denominator : "))
			else:
				break
	def  __str__(self):
			 return f'{self.nr} / {self.dr}'
	def   add(self , a , b):
		self.nr=a.nr*b.dr+b.nr*a.dr
		self.dr=a.dr*b.dr
		self.simplify(self.nr,self.dr)
	def   sub(self , a , b):
		self.nr=a.nr*b.dr-b.nr*a.dr
		self.dr=a.dr*b.dr
		self.simplify(self.nr,self.dr)
	def   mul(self , a , b):
		self.nr=a.nr*b.nr
		self.dr=a.dr*b.dr
		self.simplify(self.nr,self.dr)
	def    div(self , a , b):
		self.nr=a.nr*b.dr
		self.dr=a.dr*b.nr
		self.simplify(self.nr,self.dr)
	def   simplify(self,nr,dr):
			self.nr=nr//math.gcd(nr,dr)
			self.dr=dr//math.gcd(nr,dr)
a=Rat()
b=Rat()
c=Rat()
d=Rat()
e=Rat()
f=Rat()
a.get()
b.get()
c.add(a,b)
d.sub(a,b)
e.mul(a,b)
f.div(a,b)
print("Addition  : ",c)
print("Substraction : ",d)
print("Multiplication : ",e)
if a.dr!=0 and b.nr!=0:
	print('Division : ',f)
else:
	print('Division  is  not  permitted')
'''
OUTPUT:
Enter numerator : 2
Enter denominator : 3
Enter numerator : 5
Enter denominator : 9
Addition  :  11 / 9
Substraction :  1 / 9
Multiplication :  10 / 27
Division :  6 / 5
'''


