''' #triangle program in diff way
from d import *
p=triangle()
triangle.get(p)
triangle.test(p)
print('Area : ',  p.area())
print('Perimeter: ', p.peri())
'''
'''
class   Student:
	def   get(self):
		self.rno=(input("enter roll number: "))#How  to  read  roll  number  into  object  self
		self.sname=(input("enter student name: "))#How  to  read  student  name  into  object  self
		self.gender=(input("enter the gender: "))#How  to  read  gender  into  object  self
		self.m=eval(input("enter marks of 3 subjects in list : "))#How  to  read  marks  of  3  subjects
	def   compute(self):
		self.tot=sum(self.m)#How  to  calculate  total  marks
		self.avge=sum(self.m)/len(self.m)#How  to  calculate  average  marks
		if  self.m[0] and self.m[1] and self.m[2] <= 40:
			self.grade='Fail' #How  to  initilaize  grade  to  'Fail'
		elif  self.avge >= 70:
				self.grade='Distinction' #How  to  initilaize  grade  to  'Distinction'
		elif  self.avge >= 60:
				self.grade='First class' #How  to  initilaize  grade  to  'First  class'
		elif  self.avge >= 50:
				self.grade='Second class' #How  to  initilaize  grade  to  'Second  class'
		else:
				self.grade='Third  class'  #How  to  initilaize  grade  to  'Third  class'
	def  disp(self):
		print('Roll  Number  : ' ,   self.rno)
		print('Student  Name  : ' , self.sname)
		print('Gender  : ' ,  self.gender)
		print('Total  Marks  : ' , self.tot)
		print(f'Average  :  {self.avge:.2f}')
		print('Grade  : ' , self.grade)
	def   __str__(self):
		return F'Roll.no: {self.rno}, Name:{self.sname} , Gender:{self.gender} , total: {self.tot}, Average:{self.avge:.2f}, Grade:{self.grade}' #All  the   values  of  object  self  in  the  form  of  string
#End  of  the  class
s=Student()#How  to  create  Student  class  object
s.get()#How  to  read  inputs  into  object
s.compute()#How  to  store  results  in  object
s.disp()#How  to  print  object  with  disp()  method
print(s) #How  to  print  object  with  _str_()  method
'''

import  math
class  Rat:
	def  get(self):
		self.num=int(input("Enter the number"))#How  to  read  numerator  into  object  self
		self.den=int(input("Enter the number"))#How  to  read  denominator  into  object  self
		self.test()
	def  test(self):
		while self.den==0:
			self.den=int(input('Renter the denominator'))#Ask  user  to  reenter  denom  when  denom  is  zero
	def    __str__(self):
			 return  f"{self.num}/{self.den}" #values  of  object  in  the  form  of  rational  number  such   as  '2 / 3'
	def   add(self , a , b):
		self.num=a.num*b.den+a.den*b.num 
		self.den=a.den*b.den #How  to  add  objects  'a'  and  'b' and  store  results  in  object  self
		self.simplify() #How  to  simplify  object  self
	
	def   sub(self , a , b):
		self.num=a.num*b.den-a.den*b.num 
		self.den=a.den*b.den #How  to  subtract  objects  'a'  and  'b' and  store  results  in  object  self
		self.simplify()#How  to  simplify  object  self
	
	def   mul(self , a , b):
		self.num=a.num*b.num 
		self.den=a.den*b.den #How  to  multiply  objects  'a'  and  'b' and  store  results  in  object  self
		self.simplify() #How  to  simplify  object  self
	
	def    div(self , a , b):
		self.num=a.num*b.den 
		self.den=a.den*b.num #How  to  divide  objects  'a'  and  'b' and  store  results  in  object  self
		self.simplify() # How  to  simplify  object  self
	
	def   simplify(self):
			gcd=math.gcd(self.num,self.den)#How  to  find  gcd  of  numerator  and   denominator
			self.num//=gcd
			self.den//=gcd #How  to  simplify  rational  number  in  object  self  i.e.  12 / 15  should  be  simplified  to  4 / 5
	
# End  of the class
#How  to  create  6  objects  a , b , c , d , e , f
a=Rat()
b=Rat()
c=Rat()
d=Rat()
e=Rat()
f=Rat()
if __name__=='__main__':
	a.get()#How  to  read  rational  number  into  object  'a'
	b.get()#How to  read  rational  number  into  object  'b'
	c.add(a,b)#How  to  add  rational  numbers  in  objects  a  and  b  and  store  results  in  object  'c'
	d.sub(a,b)#How  to  subtract  rational  numbers  in  objects  a  and  b  and  store  results  in  object  'd'
	e.mul(a,b)#How  to multiply  rational  numbers  in  objects  a  and  b  and  store  results  in  object  'e'
	f.div(a,b)#How  to  divide  rational  numbers  in  objects  a  and  b  and  store  results  in  object  'f'
	print(c)#How  to  print  object   'c'
	print(d)#How  to  print  object   'd'
	print(e)#How  to  print  object   'e'
	if  f.den>0:
		print(f)
	else:
		print('Division  is  not  permitted')







































