'''
Repeat  prog5a  such  that  methods  are  called  in  another  way

1) What  are  the  two  ways  to  call  a  method ?  --->  object . method()  and  classname . method(object)

2) Import  and   use  triangle  class  defined  in  prog5a  but  do  not   define  triangle  class  again
'''
#How  to  create  triangle  object
from triangle import tri
'''a=tri()
a.get()
if a.test():
    print('Area : ', a.area()) #How  to  call  area()  method  in  another  way)
    print('Perimeter: ', a.peri())'''
s=tri()
tri.get(s)
tri.test(s)
print('Area : ', tri.area(s)) #How  to  call  area()  method  in  another  way)
print('Perimeter: ', tri.peri(s))
#How  to  call  get()  method  in  another  way
#How  to  call  test()  method  in  another  way
#print('Area : ',  a.area()) #How  to  call  area()  method  in  another  way)
#print('Perimeter: ',  a.peri())#How  to  call  peri()  method  in  another  way)
'''
Write  a  program  to  determine  total , average  and  grade  of  a  student
Inputs  are  Roll Number , Stud  Name , Marks  of  3  subjects  and  Gender
'''
class   Student:
	def   get(self):
		self.rolno=int(input("enter roll no: "))#How  to  read  roll  number  into  object  self
		self.stname=(input("enter student name: "))#How  to  read  student  name  into  object  self
		self.gender=input("enter m for male f for female: ")#How  to  read  gender  into  object  self
		self.markslist=eval(input("enter 3 sub marks in a list eg:[90,95,100]: ")) #How  to  read  marks  of  3  subjects
	def   compute(self):
		k=sum(self.markslist)#How  to  calculate  total  marks
		#How  to  calculate  average  marks
		if  self.markslist[0]<40 or self.markslist[1]<40 or self.markslist[2]<40:
				self.Grade="Fail" #How  to  initilaize  grade  to  'Fail'
		elif  k/3 >= 70:
				self.Grade='Distiction'#How  to  initilaize  grade  to  'Distinction'
		elif  k/3  >= 60:
				self.Grade='First class' #How  to  initilaize  grade  to  'First  class'
		elif  k/3  >= 50:
				self.Grade='Second class'#How  to  initilaize  grade  to  'Second  class'
		else:
			self.Grade='Third class'#How  to  initilaize  grade  to  'Third  class'
	def  disp(self):
		print('Roll  Number  :  ' ,self.rolno )
		print('Student  Name  :  ' , self.stname)
		print('Gender  :  ' ,  self.gender)
		print('Total  Marks  :  ' , sum(self.markslist))
		print('Average  :  ' , sum(self.markslist)/3)
		print('Grade  :  ' , self.Grade)
	def   __str__(self):
		return  self.rolno,self.stname, self.gender, self.markslist, self.Grade #All  the   values  of  object  self  in  the  form  of  string
#End  of  the  class
s=Student() #How  to  create  Student  class  object
s.get()#How  to  read  inputs  into  object
s.compute()#How  to  store  results  in  object
s.disp()#)How  to  print  object  with  disp()  method
print(s.__str__())#How  to  print  object  with  __str__()  method
#print(s)
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
import  math
class  Rat:
	def  get(self):
		self.numer=int(input("numerator: "))#How  to  read  numerator  into  object  self
		self.denom=int(input("denominator: "))#How  to  read  denominator  into  object  self
		#How  to  call  test()  method
	def  test(self):
		#self.denom=int(input("re-enter same denominator: "))
		if self.denom==0:
			print("Denominator cannot be zero for a rational number")
			exit
		else:
			pass#Ask  user  to  reenter  denom  when  denom  is  zero
	def    __str__(self):
			return  self.numer, self.denom #alues  of  object  in  the  form  of  rational  number  such   as  '2 / 3'
	def   add(self , a , b):
		self.numer = a.numer*b.denom + b.numer*a.denom
		self.denom = a.denom*b.denom #How  to  add  objects  'a'  and  'b' and  store  results  in  object  self
		return self.numer/(math.gcd(self.numer,self.denom)),self.denom/(math.gcd(self.numer,self.denom))#How  to  simplify  object  self
	'''
	c . add(a , b)
	object  a  --->  2 / 3
	object  b  --->  5 / 9
	object  c  --->  2 / 3 + 5 / 9 = (2 * 9 + 5 * 3) / (5 * 9) = 33 / 27 = 11 / 9
	'''
	def   sub(self , a , b):
		self.numer = a.numer*b.denom - b.numer*a.denom
		self.denom = a.denom*b.denom
		#How  to  subtract  objects  'a'  and  'b' and  store  results  in  object  self
		return self.numer/(math.gcd(self.numer,self.denom)),self.denom/(math.gcd(self.numer,self.denom)) #How  to  simplify  object  self
	'''
	d . sub(a , b)
	object  a  --->  2 / 3
	object  b  --->  5 / 9
	object  d  --->  2 / 3 - 5 / 9 = (2 * 9 - 5 * 3) / (5 * 9) = 3 / 27 = 1 / 9
	'''
	def   mul(self , a , b):
		self.numer = a.numer * b.numer 
		self.denom = a.denom * b.denom #How  to  add  objects  'a'  and  'b' and  store  results  in  object  self
		return self.numer/(math.gcd(self.numer,self.denom)),self.denom/(math.gcd(self.numer,self.denom))#How  to  multiply  objects  'a'  and  'b' and  store  results  in  object  self
		#How  to  simplify  object  self
	'''
	e . mul(a , b)
	object  a  --->  2 / 3
	object  b  --->  5 / 9
	object  e  --->  2 / 3 * 5 / 9 = (2 * 5) / (3 * 9) = 10 / 27
	'''
	def    div(self , a , b):
		self.numer = a.numer * b.denom 
		self.denom = a.denom * b.numer #How  to  add  objects  'a'  and  'b' and  store  results  in  object  self
		if self.denom!=0:
			return self.numer/(math.gcd(self.numer,self.denom)),self.denom/(math.gcd(self.numer,self.denom))
		else:
			print("zero division error")
			exit #How  to  divide  objects  'a'  and  'b' and  store  results  in  object  self
		#How  to  simplify  object  self
	'''
	f . div(a , b)
	object  a  --->  2 / 3
	object  b  --->  5 / 9
	object  f  --->  2 / 3 / 5 / 9 = 2 / 3 * 9 / 5 = (2 * 9) / (3 * 5) = 18 / 15 = 6 / 5
	'''
	#def   simplify(self,n,m):
			#How  to  find  gcd  of  numerator  and   denominator#How  to  simplify  rational  number  in  object  self  i.e.  12 / 15  should  be  simplified  to  4 / 5
'''
	c . simplify()

	1)  12 / 15  --->  4 / 5
	2) 10 / 27   --->  10 / 27
	3) 0 / 27  --->   0 / 27
	'''
# End  of the class
a=Rat()
b=Rat()
c=Rat()
d=Rat()
e=Rat()
f=Rat()
(a.get())#How  to  create  6  objects  a , b , c , d , e , f
#How  to  read  rational  number  into  object  'a'
(b.get())
#How to  read  rational  number  into  object  'b'
print(c.add(a,b))
#How  to  add  rational  numbers  in  objects  a  and  b  and  store  results  in  object  'c'
print(d.sub(a,b))
#How  to  subtract  rational  numbers  in  objects  a  and  b  and  store  results  in  object  'd'
print(e.mul(a,b))
#How  to multiply  rational  numbers  in  objects  a  and  b  and  store  results  in  object  'e'
print(f.div(a,b))
#How  to  divide  rational  numbers  in  objects  a  and  b  and  store  results  in  object  'f'
#How  to  print  object   'c'
#How  to  print  object   'd'
#How  to  print  object   'e'
'''if  ???
	How  to  print  object  'f
else:
	print('Division  is  not  permitted')'''
#  dir()  function  demo  program  (Home  work)
from hw3 import Rat
a = Rat()
a . numer = 22
a . denom = 7
print(dir(Rat))
print()
print()
print(dir(a))
#  Find  outputs  (Home  work)
class      Rat:
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
print(hasattr(Rat , 'nr'))
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
		x . talk()
	else:
		x . bark()
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
e=Emp()
for item in dict:
        setattr(e,item,dict[item])#How  to  convert  dictionary  to  object  'e'  with  for  loop
print(e.__dict__)
for i in e.__dict__:
        print(i,e.__dict__[i])#How  to  print  object  'e'  with  for  loop
