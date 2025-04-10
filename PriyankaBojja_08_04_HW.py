Q1 #Repeat  prog5a  such  that  methods  are  called  in  another  way

1) What  are  the  two  ways  to  call  a  method ?  --->  object . method()  and  classname . method(object)
2) Import  and   use  triangle  class  defined  in  prog5a  but  do  not   define  triangle  class  again

from PriyankaBojja_07_04_HW import *
x=triangle()       #How  to  create  triangle  object
triangle.get(x)    #How  to  call  get()  method  in  another  way
triangle.test(x)   #How  to  call  test()  method  in  another  way
print('Area : ',  triangle.area(x))   #How  to  call  area()  method  in  another  way
print('Perimeter: ',  triangle.peri(x)) #How  to  call  peri()  method  in  another  way)

OP-
Enter side a: 4
Enter side b: 5
Enter side c: 6
Area :  9.921567416492215
Perimeter:  15.0
#----------------------------------------------------------------------------------------------------------------------
Q2 #Write  a  program  to  determine  total , average  and  grade  of  a  student
Inputs  are  Roll Number , Stud  Name , Marks  of  3  subjects  and  Gender

class   student:
	def   get(self):
		self.rno=int(input('Enter roll number: '))           #How  to  read  roll  number  into  object  self
		self.sname=input('Enter student name: ')             #How  to  read  student  name  into  object  self
		self.gender=input('Enter gender(m or f): ')          #How  to  read  gender  into  object  self
		self.m=eval(input('Enter list of marks: '))          #How  to  read  marks  of  3  subjects
	def   compute(self):
		self.tot=sum(self.m)                                 #How  to  calculate  total  marks
		self.avg=self.tot/3                                  #How  to  calculate  average  marks
		if  self.m[0]<40 or self.m[1]<40 or self.m[2] <40:   #if At  least  one  subject  is  below  40
				self.grade='Fail'                            #How  to  initilaize  grade  to  'Fail'
		elif  self.avg >= 70:                                #if average  is  above  >= 70%:
				self.grade='Distinction'                     #How  to  initilaize  grade  to  'Distinction'
		elif  self.avg >= 60:                                #if average  is  above  >= 60%:
				self.grade='First class'                     #How  to  initilaize  grade  to  'First  class'
		elif  self.avg >= 50:                                #if average  is  above  >= 50%:
				self.grade='Second class'                    #How  to  initilaize  grade  to  'Second  class'
		else:
				self.grade='Third class'                     #How  to  initilaize  grade  to  'Third  class'
	def  disp(self):
		print('Roll  Number  :  ' ,   self.rno)
		print('Student  Name  :  ' , self.sname)
		print('Gender  :  ' ,  self.gender)
		print('Total  Marks  :  ' , self.tot)
		print('Average  :  ' , self.avg)
		print('Grade  :  ' , self.grade)
	def   __str__(self):
		#return All  the   values  of  object  self  in  the  form  of  string
		return (f'Roll Number : {self.rno}\n'
		        f'Student Name : {self.sname}\n'
			    f'Gender : {self.gender}\n'
			    f'Total Marks : {self.tot}\n'
			    f'Average : {self.avg}\n'
			    f'Grade : {self.grade}\n')
#End  of  the  class
s=student()        #How  to  create  Student  class  object
s.get()            #How  to  read  inputs  into  object
s.compute()        #How  to  store  results  in  object
print()
print('with disp() method')
s.disp()    #How  to  print  object  with  disp()  method
print()
print('with __str__() method')
print(s.__str__())   #How  to  print  object  with  _str_()  method

OP-
Enter roll number: 65
Enter student name: Priyanka
Enter gender(m or f): f
Enter list of marks: [80,85,90]

with disp() method
Roll  Number  :   65
Student  Name  :   Priyanka
Gender  :   f
Total  Marks  :   255
Average  :   85.0
Grade  :   Distinction

with __str__() method
Roll Number : 65
Student Name : Priyanka
Gender : f
Total Marks : 255
Average : 85.0
Grade : Distinction
#-----------------------------------------------------------------------------------------------------------------
Q3 Write  a  program  to  add , subtract , multiply  and  divide  two  rational  numbers

1) 1st  rational  number  --->  2 / 3
    2nd  rational  number  --->   5 / 9
    What  is  the  sum  ?  --->  2 / 3 + 5 / 9 = (18 + 15) / 27 =  33 / 27 =  11 / 9
    What  is  the  difference  ?  --->  2 / 3 - 5 / 9 =  (18 - 15) / 27 =  3 / 27 =  1 / 9
    What  is  the  product  ?  --->	2 / 3 * 5 / 9 =  10 / 27  =  10 / 27
    What  is   the  division  ?  --->  2 / 3 /  5 / 9 =  2 / 3 * 9 / 5 =  18 / 15 =  6 / 5  --->  Successful  division

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
		self.nr=int(input('Enter numerator: '))            #How  to  read  numerator  into  object  self
		self.dr=int(input('Enter denominator: '))          #How  to  read  denominator  into  object  self
		self.test()                                        #How  to  call  test()  method
	def  test(self):
		while self.dr==0:
			 print("Denominator cannot be zero. Please re-enter.")
			 self.dr=int(input('Enter denominator: '))                #Ask  user  to  reenter  denom  when  denom  is  zero
	def    __str__(self):
			 return  f'{self.nr}/{self.dr}'                           #return values  of  object  in  the  form  of  rational  number  such   as  '2 / 3'
	def   add(self , a , b):
		#How  to  add  objects  'a'  and  'b' and  store  results  in  object  self
		#How  to  simplify  object  self
		self.nr = a.nr * b.dr + b.nr * a.dr
		self.dr = a.dr * b.dr
		self.simplify()
	
	#c . add(a , b)
	#object  a  --->  2 / 3
	#object  b  --->  5 / 9
	#object  c  --->  2 / 3 + 5 / 9 = (2 * 9 + 5 * 3) / (5 * 9) = 33 / 27 = 11 / 9
	
	def   sub(self , a , b):
		#How  to  subtract  objects  'a'  and  'b' and  store  results  in  object  self
		#How  to  simplify  object  self
		self.nr = a.nr * b.dr - b.nr * a.dr
		self.dr = a.dr * b.dr
		self.simplify()

	#d . sub(a , b)
	#object  a  --->  2 / 3
	#object  b  --->  5 / 9
	#object  d  --->  2 / 3 - 5 / 9 = (2 * 9 - 5 * 3) / (5 * 9) = 3 / 27 = 1 / 9
	
	def   mul(self , a , b):
		#How  to  multiply  objects  'a'  and  'b' and  store  results  in  object  self
		#How  to  simplify  object  self
		self.nr = a.nr * b.nr
		self.dr = a.dr * b.dr
		self.simplify()
	
	#e . mul(a , b)
	#object  a  --->  2 / 3
	#object  b  --->  5 / 9
	#object  e  --->  2 / 3 * 5 / 9 = (2 * 5) / (3 * 9) = 10 / 27
	
	def    div(self , a , b):
		#How  to  divide  objects  'a'  and  'b' and  store  results  in  object  self
		#How  to  simplify  object  self
		self.nr = a.nr * b.dr
		self.dr = a.dr * b.nr
		self.simplify()
	
	#f . div(a , b)
	#object  a  --->  2 / 3
	#object  b  --->  5 / 9
	#object  f  --->  2 / 3 / 5 / 9 = 2 / 3 * 9 / 5 = (2 * 9) / (3 * 5) = 18 / 15 = 6 / 5
	
	def   simplify(self):
		if self.nr != 0:
			gcd=math.gcd(self.nr,self.dr)  #How  to  find  gcd  of  numerator  and   denominator
			self.nr=self.nr//gcd   #How  to  simplify  rational  number  in  object  self  i.e.  12 / 15  should  be  simplified  to  4 / 5
			self.dr=self.dr//gcd
	
	#c . simplify()
	#1)  12 / 15  --->  4 / 5
	#2) 10 / 27   --->  10 / 27
	#3) 0 / 27  --->   0 / 27

# End  of the class
if __name__=='__main__':
	a=Rat()   #How  to  create  6  objects  a , b , c , d , e , f
	b=Rat()
	c=Rat()
	d=Rat()
	e=Rat()
	f=Rat()
	a.get()                  #How  to  read  rational  number  into  object  'a'
	b.get()                  #How to  read  rational  number  into  object  'b'
	c.add(a,b)               #How  to  add  rational  numbers  in  objects  a  and  b  and  store  results  in  object  'c'
	d.sub(a,b)               #How  to  subtract  rational  numbers  in  objects  a  and  b  and  store  results  in  object  'd'
	e.mul(a,b)               #How  to multiply  rational  numbers  in  objects  a  and  b  and  store  results  in  object  'e'
	f.div(a,b)               #How  to  divide  rational  numbers  in  objects  a  and  b  and  store  results  in  object  'f'
	print('Sum: ',c)         #How  to  print  object   'c'
	print('Difference: ',d)  #How  to  print  object   'd'
	print('Product: ',e)     #How  to  print  object   'e'
	if  b.nr!=0:
		print('Division: ',f)   #How  to  print  object  'f
	else:
		f.div(a,b)
		print('Division  is  not  permitted')

OP-
Enter numerator: 2
Enter denominator: 3
Enter numerator: 5
Enter denominator: 9
Sum:  11/9
Difference:  1/9
Product:  10/27
Division:  6/5
#----------------------------------------------------------------------------------------------------------
Q4 #dir()  function  demo  program  (Home  work)
from  Rational_num   import  Rat
a = Rat()
a . nr = 22
a . dr = 7
print(dir(Rat))
print()
print()
print(dir(a)) 

OP-
['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__firstlineno__', '__format__', '__ge__', '__getattribute__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__static_attributes__', '__str__', '__subclasshook__', '__weakref__', 'add', 'div', 'get', 'mul', 'simplify', 'sub', 'test']


['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__firstlineno__', '__format__', '__ge__', '__getattribute__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__static_attributes__', '__str__', '__subclasshook__', '__weakref__', 'add', 'div', 'dr', 'get', 'mul', 'nr', 'simplify', 'sub', 'test']
#-----------------------------------------------------------------------------------------------
Q5 #Find  outputs  (Home  work)
class      Rat:
	def    m1():
		pass
# End  of  the  class
a = Rat()
a . nr = 22
print(hasattr(a , 'nr')) #True
print(hasattr(a , 'dr')) #False
print(hasattr(a , 'm1')) #True
print(hasattr(a , 'm2')) #False
print(hasattr(Rat , 'm1')) #True
print(hasattr(Rat , 'm2')) #False
print(hasattr(Rat , 'nr')) #False
#----------------------------------------------------------------
Q6 #Find  outputs
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

OP-
Meow Meow Meow ....
Bhow Bhow Bhow ....
Mehar  Mehar  Mehar  ....
#------------------------------------------------------------------------------------------------------------------
Q7 #Find  outputs
class    c1:
        pass
# End of the class
a = c1()
a . x = 10
varname = input('Enter  variable  name  to  be  added  to  object  :  ')   #  Assume  that  input  is  'y'
value = eval(input('Enter  value  of  the  variable  :  '))   #  Assume  that  input  is   20
setattr(a , varname , value)
print(a . __dict__) #{'x' : 10 , 'y' : 20}
print(a . x)        #10
while  True:
	try:
		varname = input('Enter  variable  name  whose  value  is  to  be  retrieved  :  ')
									#  Assume  that  input  is  x  in  1st   iteration  ,  y  in   2nd   iteration  and  z  in  3rd  iteration
		print(getattr(a , varname))
	except:
		print(F'Invalid  variable   name   :  {varname}')
		break

OP-
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
#-------------------------------------------------------------------------------------------------------------------------------------------
Q8 #Write  a  program  to  convert  a  dictionary  {'Empno' : 25 , 'Ename' : 'Rama  Rao' , 'Sal' : 10000.0}  to  Emp  class  object
i.e.  object  should  contain  empno = 25 , ename = 'Rama  Rao' , Sal = 10000.0
Hint:  Use  setattr()  and  getattr()  functions

class  Emp:
        pass
#End  of  the  class
dict = {'Empno' : 25 , 'Ename' : 'Rama  Rao' , 'Sal' : 10000.0}
e=Emp()
for key in dict:    #How  to  convert  dictionary  to  object  'e'  with  for  loop  
	setattr(e,key,dict[key])                #How  to  convert  dictionary  to  object  'e'  with  for  loop
	print(f'{key} : {getattr(e,key)}')      #How  to  print  object  'e'  with  for  loop
   
OP-
Empno : 25
Ename : Rama  Rao
Sal : 10000.0
'''

