'''Write  a  program  to  determine  total , average  and  grade  of  a  student
Inputs  are  Roll Number , Stud  Name , Marks  of  3  subjects  and  Gender

class   Student:
	def   get(self):
		self.ro=int(input('enter rollno : '))  #How  to  read  roll  number  into  object  self
		self.sname=input('enter name : ') #How  to  read  student  name  into  object  self
		self.m=[] # How  to  read  gender  into  object  self
		self.gender=input('enter gender : ') #How  to  read  marks  of  3  subjects
		for x in range(3):
			a=int(input(f'enter the {x+1} subject marks: '))
			self.m.append(a)
	def   compute(self):
		self.tot=self.m[0]+self.m[1]+self.m[2] #How  to  calculate  total  marks
		self.ave=(self.m[0]+self.m[1]+self.m[2])/3  #How  to  calculate  average  marks
		if  self.m[0]<40 or self.m[1]<40 or self.m[2]<40 :  #At  least  one  subject  is  below  40:
				return 'Fail'  #How  to  initilaize  grade  to  'Fail'
		elif  self.ave >= 70: # is  above  >= 70%:
				return 'Distinction' #How  to  initilaize  grade  to  'Distinction'
		elif  self.ave>=60:  #  is  above  >= 60%:
				return 'First  class'  #How  to  initilaize  grade  to  'First  class'
		elif  self.ave>=50:   #average  is  above  >= 50%:
				return  'Second  class'  #How  to  initilaize  grade  to  'Second  class'
		else:
				return 'Third  class'  #How  to  initilaize  grade  to  'Third  class'
	def  disp(self):
		print('Roll  Number  :  ' ,   self.ro)
		print('Student  Name  :  ' , self.sname)
		print('Gender  :  ' ,  self.gender)
		print('Total  Marks  :  ' , self.tot)
		print('Average  :  ' , self.ave)
		print('Grade  :  ' ,s.compute() )
	def   __str__(self):
		return  f'{self.ro} {self.sname} {self.m} {self.gender}'   #All  the   values  of  object  self  in  the  form  of  string
#End  of  the  class
if __name__=="__main__":
	s=Student()  #How  to  create  Student  class  object
	s.get()  #How  to  read  inputs  into  object
	s.compute()  #How  to  store  results  in  object
	s.disp()  #How  to  print  object  with  disp()  method
	print(s) #How  to  print  object  with  _str_()  method
'''


'''
import  math
class  Rat:
	def  get(self):
		self.num=int(input('numerator : '))  #How  to  read  numerator  into  object  self
		self.deno=int(input('denominator : '))  #How  to  read  denominator  into  object  self
		self.test() #How  to  call  test()  method
	def  test(self):
		if self.deno==0:
			print('enter deno greater than zero')
			self.deno=int(input()) #Ask  user  to  reenter  denom  when  denom  is  zero
	def    __str__(self):
			 return  f'{self.num}/{self.deno}'  #values  of  object  in  the  form  of  rational  number  such   as  '2 / 3'
	def   add(self , a , b):
		self.num=a.num*b.deno + b.num*a.deno 
		self.deno=a.deno*b.deno #How  to  add  objects  'a'  and  'b' and  store  results  in  object  self
		self.simplify() #How  to  simplify  object  self
	def   sub(self , a , b):
		self.num=a.num*b.deno - b.num*a.deno 
		self.deno=a.deno*b.deno  #How  to  subtract  objects  'a'  and  'b' and  store  results  in  object  self
		self.simplify() #How  to  simplify  object  self
	def   mul(self , a , b):
		self.num=a.num * b.num
		self.deno=a.deno*b.deno  #How  to  multiply  objects  'a'  and  'b' and  store  results  in  object  self
		self.simplify()  #How  to  simplify  object  self
	def    div(self , a , b):
		if b.num != 0:
			self.num=a.num*b.deno
			self.deno=a.deno*b.num #How  to  divide  objects  'a'  and  'b' and  store  results  in  object  self
			self.simplify()
			return True #How  to  simplify  object  self
		else:
			return False
	
	def   simplify(self):
			gcd=math.gcd(self.num,self.deno)  #How  to  find  gcd  of  numerator  and   denominator
			if gcd !=0 :
				self.num//=gcd
				self.deno//=gcd  #How  to  simplify  rational  number  in  object  self  i.e.  12 / 15  should  be  simplified  to  4 / 5
	
# End  of the class
a=Rat()
b=Rat()
c=Rat()
d=Rat()
e=Rat()
f=Rat()  #How  to  create  6  objects  a , b , c , d , e , f
print('1st rational number numeratorn and denominator')
a.get()  #How  to  read  rational  number  into  object  'a'
print('2nd rational number numerator and denominator')
b.get() #How to  read  rational  number  into  object  'b'
c.add(a,b) #How  to  add  rational  numbers  in  objects  a  and  b  and  store  results  in  object  'c'
d.sub(a,b) #How  to  subtract  rational  numbers  in  objects  a  and  b  and  store  results  in  object  'd'
e.mul(a,b) #How  to multiply  rational  numbers  in  objects  a  and  b  and  store  results  in  object  'e'
#How  to  divide  rational  numbers  in  objects  a  and  b  and  store  results  in  object  'f'
print(c) #How  to  print  object   'c'
print(d) #How  to  print  object   'd'
print(e) #How  to  print  object   'e'
if  f.div(a,b):
	print(f) #How  to  print  object  'f
else:
	print('Division  is  not  permitted')

'''


'''
#  dir()  function  demo  program  (Home  work)
from prog10a import Rat
a = Rat()
a . nr = 22
a . dr = 7
print(dir(Rat))
print()
print()
print(dir(a))
'''


'''
#  Find  outputs  (Home  work)
class      Rat:
	def    m1():
		pass
# End  of  the  class
a = Rat()
a . nr = 22
print(hasattr(a , 'nr')) # True
print(hasattr(a , 'dr')) #False
print(hasattr(a , 'm1')) # True
print(hasattr(a , 'm2')) # False
print(hasattr(Rat , 'm1')) # True
print(hasattr(Rat , 'm2')) #False
print(hasattr(Rat , 'nr')) # False
'''


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
#end of the class
a = [Cat() , Dog() , Goat()] # refereance 'a' points to the list of object of Cat class , object of Dog class , object of Goat class
for  x  in   a:
	if   hasattr(x , 'talk'):
		x . talk()
	else:
		x . bark()

#outputs
Meow Meow Meow ....
Bhow Bhow Bhow ....
Mehar  Mehar  Mehar  ....
'''


'''
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
#output
Enter  variable  name  to  be  added  to  object  :  y
Enter  value  of  the  variable  :  9
{'x': 10, 'y': 9}
10
Enter  variable  name  whose  value  is  to  be  retrieved  :  x
10
Enter  variable  name  whose  value  is  to  be  retrieved  :  y
9
Enter  variable  name  whose  value  is  to  be  retrieved  :  s
Invalid  variable   name   :  s
'''

'''
(Home  work)
Write  a  program  to  convert  a  dictionary  {'Empno' : 25 , 'Ename' : 'Rama  Rao' , 'Sal' : 10000.0}  to  Emp  class  object
i.e.  object  should  contain  empno = 25 , ename = 'Rama  Rao' , Sal = 10000.0

Hint:  Use  setattr()  and  getattr()  functions
'''

'''
class  Emp:
        pass
#End  of  the  class
dict = {'Empno' : 25 , 'Ename' : 'Rama  Rao' , 'Sal' : 10000.0}
a=Emp()
for x in dict:#How  to  convert  dictionary  to  object  'e'  with  for  loop
	setattr(a,x,dict[x])
	print(f'{x} = {getattr(a,x)}')
#How  to  print  object  'e'  with  for  loop
'''

'''
Repeat  prog5a  such  that  methods  are  called  in  another  way

1) What  are  the  two  ways  to  call  a  method ?  --->  object . method()  and  classname . method(object)

2) Import  and   use  triangle  class  defined  in  prog5a  but  do  not   define  triangle  class  again

import math
from prog5a import triangle
s=triangle() #How  to  create  triangle  object
triangle.get(s) #How  to  call  get()  method  in  another  way
triangle.test(s)  #How  to  call  test()  method  in  another  way
print('Area : ', triangle.area(s)) # How  to  call  area()  method  in  another  way)
print('Perimeter: ',  triangle.peri(s)) #How  to  call  peri()  method  i)
'''
