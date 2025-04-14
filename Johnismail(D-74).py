'''
Repeat  prog5a  such  that  methods  are  called  in  another  way

1) What  are  the  two  ways  to  call  a  method ?  --->  object . method()  and  classname . method(object)

2) Import  and   use  triangle  class  defined  in  prog5a  but  do  not   define  triangle  class  again

from Apr7Opps import triangle

a=triangle() #How  to  create  triangle  object
triangle.get(a) #How  to  call  get()  method  in  another  way
triangle.test(a) #How  to  call  test()  method  in  another  way
print('Area : ',  triangle.area(a)) #How  to  call  area()  method  in  another  way)
print('Perimeter: ',triangle.peri(a)) #  How  to  call  peri()  method  in  another  way)



Write  a  program  to  determine  total , average  and  grade  of  a  student
Inputs  are  Roll Number , Stud  Name , Marks  of  3  subjects  and  Gender


class   Student:
	def   get(self):
		self.Rollno=int(input('enter Rollno:')) #How  to  read  roll  number  into  object  self
		self.Name=input('enter Name:') #How  to  read  student  name  into  object  self
		self.gender=input('enter gender:') #How  to  read  gender  into  object  self
		self.m=[] #How  to  read  marks  of  3  subjects
		for i in range(3):
				self.marks=int(input(f'enter{i+1} marks:'))
				self.m.append(self.marks)
		
	def   compute(self):

		self.tot=sum(self.m) #How  to  calculate  total  marks
		self.avg=self.tot/len(self.m) #How  to  calculate  average  marks
		if  min(self.m)<=40:  # At  least  one  subject  is  below  40:
				self.grade='Fail'
												 #How  to  initilaize  grade  to  'Fail'
		elif  self.avg>= 70:
				 self.grade='Distinction'
				 #How  to  initilaize  grade  to  'Distinction'
		elif  self.avg>= 60:
				self.grade='First class'
				#How  to  initilaize  grade  to  'First  class'
		elif  self.avg>= 50:
				self.grade='Second class'
				 #How  to  initilaize  grade  to  'Second  class'
		else:
				self.grade='Third class'
				#How  to  initilaize  grade  to  'Third  class'
	def  disp(self):
		print('Roll  Number  :  ' ,self.Rollno)
		print('Student  Name  :  ' , self.Name)
		print('Gender  :  ' , self.gender)
		print('Total  Marks  : ' ,self.tot)
		print('Average  :  ' ,self.avg)
		print('Grade  :  ' ,self.grade )
	def   __str__(self):
		  print(f'{self.Rollno}\t{self.Name}\t{self.gender}\t{self.tot}\t{self.avg}\t{self.grade}')
		        
#End  of  the  class
a=Student() #How  to  create  Student  class  object
a.get() #How  to  read  inputs  into  object
a.compute() #How  to  store  results  in  object
a.disp() #How  to  print  object  with  disp()  method
a.__str__() #How  to  print  object  with  __str__()  method


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
"""
import  math
class  Rat:
	def  get(self):
		self.numerator=int(input('enter nume value:')) #How  to  read  numerator  into  object  self
		self.denominator=int(input('enter demo value:')) #How  to  read  denominator  into  object  self
		self.test()
					
	def  test(self):
		while self.denominator==0:
			
				self.denominator=int(input('enter non zero deno:'))#Ask  user  to  reenter  denom  when  denom  is  zero
	def __str__(self):
			return(f'{self.numerator}/{self.denominator}')
			 #return  values  of  object  in  the  form  of  rational  number  such   as  '2 / 3'
	def add(self , a , b):
			self.numerator=a.numerator*b.denominator + a.denominator*b.numerator
			self.denominator=a.denominator*b.denominator
			self.simplify() #How  to  add  objects  'a'  and  'b' and  store  results  in  object  self
		#How  to  simplify  object  self
	
	c . add(a , b)
	object  a  --->  2 / 3
	object  b  --->  5 / 9
	object  c  --->  2 / 3 + 5 / 9 = (2 * 9 + 5 * 3) / (5 * 9) = 33 / 27 = 11 / 9
	
	def   sub(self , a , b):
					self.numerator=a.numerator*b.denominator-a.denominator*b.numerator
					self.denominator=a.denominator*b.denominator 
					self.simplify()#How  to  subtract  objects  'a'  and  'b' and  store  results  in  object  self
		#How  to  simplify  object  self
	
	d . sub(a , b)
	object  a  --->  2 / 3
	object  b  --->  5 / 9
	object  d  --->  2 / 3 - 5 / 9 = (2 * 9 - 5 * 3) / (5 * 9) = 3 / 27 = 1 / 9
	
	def   mul(self , a , b):
				self.numerator = a.numerator * b.numerator
				self.denominator = a.denominator * b.denominator
				self.simplify() #How  to  multiply  objects  'a'  and  'b' and  store  results  in  object  self
		#How  to  simplify  object  self
	
	e . mul(a , b)
	object  a  --->  2 / 3
	object  b  --->  5 / 9
	object  e  --->  2 / 3 * 5 / 9 = (2 * 5) / (3 * 9) = 10 / 27
	
	def    div(self , a , b):
					self.numerator= a.numerator * b.denominator
					self.denominator = a.denominator * b.numerator 
					self.simplify() #How  to  divide  objects  'a'  and  'b' and  store  results  in  object  self
		#How  to  simplify  object  self
	
	f . div(a , b)
	object  a  --->  2 / 3
	object  b  --->  5 / 9
	object  f  --->  2 / 3 / 5 / 9 = 2 / 3 * 9 / 5 = (2 * 9) / (3 * 5) = 18 / 15 = 6 / 5
	
	def   simplify(self):
			gcd=math.gcd(self.numerator,self.denominator)
			self.numerator//=gcd
			self.denominator//=gcd #How  to  find  gcd  of  numerator  and   denominator
			#How  to  simplify  rational  number  in  object  self  i.e.  12 / 15  should  be  simplified  to  4 / 5

	c . simplify()
	1)  12 / 15  --->  4 / 5
	2) 10 / 27   --->  10 / 27
	3) 0 / 27  --->   0 / 27
	
# End  of the class
a=Rat()
b=Rat()
c=Rat()
d=Rat()
e=Rat()
f=Rat() #How  to  create  6  objects  a , b , c , d , e , f
a.get() #How  to  read  rational  number  into  object  'a'
b.get() #How to  read  rational  number  into  object  'b'
c.add(a,b) #How  to  add  rational  numbers  in  objects  a  and  b  and  store  results  in  object  'c'
d.sub(a,b)#How  to  subtract  rational  numbers  in  objects  a  and  b  and  store  results  in  object  'd'
e.mul(a,b)#How  to multiply  rational  numbers  in  objects  a  and  b  and  store  results  in  object  'e'
f.div(a,b)#How  to  divide  rational  numbers  in  objects  a  and  b  and  store  results  in  object  'f'
print('sum:',c)#How  to  print  object   'c'
print('sub:',d)#How  to  print  object   'd'
print('mul:',e)#How  to  print  object   'e'

if  b.numerator!=0:
			print('div:',f)#How  to  print  object   'f'
else:
	print('Division  is  not  permitted')

#  Find  outputs  (Home  work)
class      Rat:
	def    m1():
		pass
# End  of  the  class
a = Rat()
a . nr = 22
print(hasattr(a , 'nr'))#True
print(hasattr(a , 'dr'))#False
print(hasattr(a , 'm1'))#True
print(hasattr(a , 'm2'))#False
print(hasattr(Rat , 'm1'))#True
print(hasattr(Rat , 'm2'))#False
print(hasattr(Rat , 'nr'))#False

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
outputs--
Meow Meow Meow ....
Bhow Bhow Bhow ....
Mehar  Mehar  Mehar  ....
"""

(Home  work)
Write  a  program  to  convert  a  dictionary  {'Empno' : 25 , 'Ename' : 'Rama  Rao' , 'Sal' : 10000.0}  to  Emp  class  object
i.e.  object  should  contain  empno = 25 , ename = 'Rama  Rao' , Sal = 10000.0

Hint:  Use  setattr()  and  getattr()  functions
'''
class  emp:
        pass
#End  of  the  class
e=emp()
dict = {'Empno' : 25 , 'Ename' : 'Rama  Rao' , 'Sal' : 10000.0}
for key, values in dict.items():
			setattr(e, key, values)		
#How  to  convert  dictionary  to  object  'e'  with  for  loop
for key in dict.keys():
			print(key, 'getattr(e , values)' ,sep='...')  #How  to  print  object  'e'  with  for  loop
