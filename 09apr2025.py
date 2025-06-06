
'''
class   Student:
	def   get(self):
		self.rolno=int(input("Enter roll number: ")) #How  to  read  roll  number  into  object  self
		self.sname=input("Enter name: ") #How  to  read  student  name  into  object  self
		self.gender=input("Enter gender: ") #How  to  read  gender  into  object  self
		self.marks= list(map(int,input("Enter marks: ").split())) #How  to  read  marks  of  3  subjects
		
	def   compute(self):
		self.total_marks=sum(self.marks) #How  to  calculate  total  marks
		self.average=self.total_marks/len(self.marks) #How  to  calculate  average  marks
		
		if  self.marks[0]<40 or self.marks[1]<40 or self.marks[2]<40 : #At  least  one  subject  is  below  40
				self.grade="Fail" #How  to  initilaize  grade  to  'Fail'
		elif  self.average >= 70:
				self.grade="Distinction" #How  to  initilaize  grade  to  'Distinction'
		elif  self.average >= 60:
				self.grade="First class" #How  to  initilaize  grade  to  'First  class'
		elif  self.average >= 50:
				self.grade="Second class" #How  to  initilaize  grade  to  'Second  class'
		else:
				self.grade="Third class" #How  to  initilaize  grade  to  'Third  class'
				
	def  disp(self):
		print('Roll  Number  :  ' ,   self.rolno)
		print('Student  Name  :  ' , self.sname)
		print('Gender  :  ' ,  self.gender)
		print('Total  Marks  :  ' , self.total_marks)
		print('Average  :  ' , self.average)
		print('Grade  :  ' , self.grade)
	def   _str_(self):
		return F'{self.rolno} {self.sname} {self.gender} {self.total_marks} {self.average} {self.grade}'
		#All  the   values  of  object  self  in  the  form  of  string
		
		
#End  of  the  class

if __name__=='__main__':
	s=Student()#How  to  create  Student  class  object
	s.get() #How  to  read  inputs  into  object
	s.compute() #How  to  store  results  in  object
	s.disp() #How  to  print  object  with  disp()  method
	s._str() #How  to  print  object  with  _str()  method

'''

# 1.What  are  the  outputs  if  inputs  are  25 , Rama  Rao ,  male , 52 , 48 , 55   (Home  work)

'''
from  Madhan  import  Student
s = Student()
print(s . __dict__) #{}

s . get()
print(s . __dict__) # {'rolno':25, 'sname':'Rama Rao','gender':'male','marks':[52,48,55]}

s . compute()
print(s . __dict__) 
# {'rolno':25, 'sname':'Rama Rao','gender':'male','marks':[52,48,55] 'total_marks': 155 , 'average': 90.0,'grade':'Second class'}

'''


'''
#2.

Madhan.py file
'''

'''
from math import*
class  Rat:
	def  get(self):
		self.nu= int(input("Enter numerator: ")) #How  to  read  numerator  into  object  self
		self.de= int(input("Enter denominator: ")) #How  to  read  denominator  into  object  self
		self.test() #How  to  call  test()  method
		
	def  test(self):
		#Ask  user  to  re enter  denom  when  denom  is  zero
		while(self.de==0):
		    self.de= int(input("Enter denominator: "))
		    
	def  __str__(self):
			 return  F'{self.nu}/{self.de}' #values  of  object  in  the  form  of  rational  number  such   as  '2 / 3'
			 
	def   add(self , a , b):
		self.nu= (a.nu*b.de + b.nu*a.de) #How  to  add  objects  'a'  and  'b' and  store  results  in  object  self
		self.de= (a.de*b.de)
		self.simplify() #How  to  simplify  object  self
	
	def   sub(self , a , b):
		self.nu= (a.nu*b.de - b.nu*a.de) #How  to  subtract  objects  'a'  and  'b' and  store  results  in  object  self
		self.de= (a.de*b.de) 
		self.simplify() #How  to  simplify  object  self
	
	def   mul(self , a , b):
		self.nu= (a.nu*b.nu) #How  to  multiply  objects  'a'  and  'b' and  store  results  in  object  self
		self.de= (a.de*b.de) 
		self.simplify() #How  to  simplify  object  self
	
	def    div(self , a , b):
		self.nu= (a.nu*b.de) 
		self.de=(a.de*b.nu) #How  to  divide  objects  'a'  and  'b' and  store  results  in  object  self
		self.simplify() #How  to  simplify  object  self
	
	def   simplify(self):
		g=gcd(self.nu,self.de) #How  to  find  gcd  of  numerator  and   denominator

		if(self.de!=0):
			self.nu=self.nu//g
			self.de=self.de//g  #How  to  simplify  rational  number  in  object  self  i.e.  12 / 15  should  be  simplified  to  4 / 5
	
	


# End  of the class

if __name__=='__main__':
	a=Rat(); b=Rat(); c=Rat();d=Rat();e=Rat();f=Rat() #How  to  create  6  objects  a , b , c , d , e , f
	a.get() #How  to  read  rational  number  into  object  'a'
	b.get() #How to  read  rational  number  into  object  'b'
	c.add(a,b) #How  to  add  rational  numbers  in  objects  a  and  b  and  store  results  in  object  'c'
	d.sub(a,b) #How  to  subtract  rational  numbers  in  objects  a  and  b  and  store  results  in  object  'd'
	e.mul(a,b) #How  to multiply  rational  numbers  in  objects  a  and  b  and  store  results  in  object  'e'
	f.div(a,b) #How  to  divide  rational  numbers  in  objects  a  and  b  and  store  results  in  object  'f'
	print(F'addition: {c}') #How  to  print  object   'c'
	print(F'subtraction: {d}') #How  to  print  object   'd'
	print(F'multiplication: {e}') #How  to  print  object   'e'
	if  f.de!=0:
		print(F'division: {f}')#How  to  print  object  'f
	else:
		print('Division  is  not  permitted')
		
'''


'''
2.Repeat  prog10a  with  3  objects

Eg:  c = a + b
	 print  c
	 c = a - b
	 print  c
	 c = a * b
	 print  c
	 c = a / b
	 print  c

Hint:  Import  and  use  Rat  class  defined  in  prog10a  but  do  not  define  Rat  class   again
'''

'''
from Madhan import Rat

a=Rat()
b=Rat()
a.get()
b.get()

c=Rat()
c.add(a,b)
print(c)

c.sub(a,b)
print(c)

c.mul(a,b)
print(c)

c.div(a,b)
print(c)

'''


'''
3.
Repeat  prog10a  with  list  of  6  objects

Hint:  import  and  use  rat  class  defined  in  prog10a  but  do  not  rewrite  the  class  again

What  are  the  object  names  ?  --->  a[0] , a[1] , a[2] , .....a[5]
'''

'''
from Madhan import Rat

a=[]

for i in range(6):
	a.append(Rat())

a[0].get()
a[1].get()

a[2].add(a[0],a[1])
print(a[2])

a[3].sub(a[0],a[1])
print(a[3])

a[4].mul(a[0],a[1])
print(a[4])

a[5].add(a[0],a[1])
print(a[5])


'''


#4.Find  outputs

'''
class  Rat:
	def   __init__(self , nr1 = 22, dr1 = 7):
		self . nr = nr1
		self . dr = dr1
	def   __str__(self):
		return  F'{self . nr}  /  {self . dr}'
#end  of  the  class
a = Rat() #   Object  is  initialized  with  nr =  22 , dr = 7  by  constructor
b = Rat(9) #   Object  is  initialized  with  nr =  9 , dr = 7  by  constructor
c = Rat(5,  8) #   Object  is  initialized  with  nr =  5 , dr = 8  by  constructor
d = Rat(dr1 = 9) #   Object  is  initialized  with  nr =  22 , dr = 9  by  constructor
e = Rat(dr1 = 3 , nr1 = 2) #   Object  is  initialized  with  nr =  2 , dr = 3  by  constructor
x = eval(input('Enter numerator  :  '))  #  Assume  that  input  is   11
y = eval(input('Enter Denominator  :  '))    #  Assume  that  input  is    15
f = Rat(x , y) #   Object  is  initialized  with  nr =  11 , dr = 15  by  constructor
print('a  :  ' , a) #22/7
print('b  :  ' , b) #9/7
print('c  :  ' , c) #5/8
print('d  :  ' , d) #22/9
print('e  :  ' , e) #2/3
print('f  :  ' , f) #11/15
c . __init__() # Modifies  object  'c'   to  nr = 22 , dr = 7  replacing  5  and   8
print('c  :  ' , c) #22/7
a . __init__(3.8  , 4.6) #  Modifies  object  'a'   to  nr = 3.8 , dr = 4.6   replacing  22  and   7
print('a  :  ' , a) # 3.8/4.6
#g = Rat(nr1 = 9 , 5) #Error due to PA after KA
#h = Rat(nr = 9 , dr = 5) #  Error because no KA nr,dr

'''


#5.Find  outputs (Home  work)

'''
class  Date:
    def   __init__(self , dd1 , mm1  , yy1):
        self . dd = dd1
        self . mm = mm1
        self . yy = yy1
        
# End  of  the  class
a = Date(15 , 8 , 1947)
b = Date(yy1 = 1950 , mm1 = 1 , dd1 = 26)
c = Date(mm1 = 7 , dd1 = 19 , yy1 = 1985)
print('a  :  ' , a . __dict__) # a : {'dd': 15 , 'mm': 8, 'yy': 1947}
print('b  :  ' , b . __dict__)  #b : {'dd': 26 , 'mm': 1, 'yy': 1950}
print('c  :  ' , c . __dict__)  # a : {'dd': 19 , 'mm': 7, 'yy': 1985}
#d = Date() #Error constructor req 3 args 
#e = Date(dd = 30 , mm = 4 , yy = 2022) #Error due to no KA dd,mm,yy
#f = Date(dd1 = 26 , mm1 = 8 , 2023) #Error due to PA (2023) after KA

'''

#6. Find  outputs (Home  work)
'''
class  c1:
	def  __init__(self):
		print('c1  class constructor')
		return  25 
class  c2:
	def  __init__(self):
		print('c2  class  constructor')
		return  None
class  c3:
	def  __init__(self):
		print('c3  class  constructor')
# End  of  class
#a = c1() # error constructor returning other than None 
b = c2() # c2  class constructor
print(b) # <__main__.c2 object at 0xaddress>
print(b .__init__()) #c2  class constructor \n None
c = c3() #c3  class  constructor
print(c . __init__()) #None

'''


#7.Find  outputs (Home  work)

'''
class  c1:
	def  __init__(self):
		print('Constructor')
		b = c1() #2. Constructor ....infinite times (Recursion Error)
# End  of  class
a = c1() #1.Constructor 

'''

#8.Difference  between  init()    and  _init_()   methods (Home  work)
'''
class c1:
    def  __init__(self):
        print('Constructor')
        self . x = 10
        self . y = 20
class c2:
    def  init(self):
        print('Method')
        self . x = 30
        self . y = 40
a = c1() #Constructor
print(a .__dict__) #{'x':10 , 'y': 20}

b = c2()
print(b .__dict__) #{}
b . init() #Method
print(b .__dict__) #{'x':30 , 'y': 40}

'''


#9.Find  outputs (Home  work)
'''
class   c1:
        def  __init__(self):
                self . a = 10
        def   m1(self):
                self . b = 20
#End  of  class  c1
class   c2:
        def  m3(self):
                x . e = 50
# End  of  class  c2
def   f1():
        x . c = 30
#  End  of  function  f1
x = c1()
print(x . __dict__) #{'a':10}
x . m1()
print(x . __dict__) #{'a':10,'b':20}
f1()
print(x . __dict__) #{'a':10,'b':20, 'c':30}
x . d = 40
print(x . __dict__) #{'a':10,'b':20, 'c':30,'d':40}
y = c2()
y . m3()
print(x . __dict__) #{'a':10,'b':20, 'c':30,'d':40,'e':50}
z = c1()
print(z . __dict__) #{'a':10}

'''

#10.Find  outputs  (Home  work)

'''
class   c1:
	def __init__(self):
		self . x = 10
		self . y = 20
		self . z = 30
#end  of  the  class
a = c1()
b = c1()
print(a .__dict__) #{'x':10,'y':20,'z':30}
print(b .__dict__) #{'x':10,'y':20,'z':30}
del  a . x
del  b . y
print(a .__dict__) #{y':20,'z':30}
print(b .__dict__) #{'x':10,z':30}
#print(a . x) #Error 
#print(b . y) #Error

'''

#11.Find  outputs (Home  work)
'''
class   c1:
	def  __init__(self):
		print('1st  constructor')
	def  __init__(self):
		print('2nd  constructor')
	def  __init__(self):
		print('3rd  constructor')
# End  of  the  class
a = c1() #3rd  constructor
'''

#12.Find  outputs  (Home  work)
'''
class   c1:
	def  __init__(self):
		print('No  argument  constructor')
	def  __init__(self , x):
		print('single  argument  constructor : ' , x)
	def  __init__(self , x , y):
		print('Two  argument  constructor : ' , x , y)
# End  of  the  class
a = c1(10 , 20) #Two  argument  constructor : 10 20 
#b = c1(30) #Error no arg for y
#c = c1() #Error no arg for x,y

'''

#13.Find  outputs
'''
class   c1:
	def  __init__(self):
		print('No  argument  constructor')
	def  __init__(self , x):
		print('single  argument  constructor : ' , x)
	def  __init__(self , x = 100 , y = 200):
		print('Two  argument  constructor : ' , x , y)
# End  of  the  class
a = c1(10 , 20) #Two  argument  constructor : 10 20
b = c1(30) #Two  argument  constructor : 30 200
c = c1() #Two  argument  constructor : 100 200
'''

#14.What  happens  when  function  and  class  have  same  name ?
'''
def   f1():
	print('Function')
	return  25
class   f1:
	def  __init__(self):
		print('Constructor')
#end of the  class
a = f1() #Constructor
print(a) #<__main__.f1 object at 0xaddress>

'''

#15.Find  outputs (Home  work)
'''
class    c1:
	def   __init__(self):
		print('Constructor')
def  c1(): #recognised
	print('Function')
#end of the  class
a = c1() #Function
print(a) #None

'''

#16.Find outputs  (Home  work)

'''
class    c1:
        def  __init__(self):
                print('Constructor')
def    c1(x):
        print('Function : ' , x)
# End  of  class  c1
#a = c1()
b = c1(25) #Function :  25 
print(b) #None

'''

#17.Save  the  program  in  Madhan.py  file

'''
class   c1:
	def  __init__(self):
		print('c1  class  of  prog9a')
		
'''

#17.Find  outputs (Home  work)

'''
from  Madhan  import  c1
class   c1:
	def  __init__(self):
		print('c1  class  of  prog9b')
a = c1() #c1  class  of  prog9b

'''

#18.Find  outputs (Home  work)
'''
class   c1:
	def  __init__(self):
		print('c1  class  of  prog9c')
from  Madhan import  c1
a = c1() #c1  class  of  prog9a

'''

# 19.How  to  use  both  the  classes (i.e.  c1  of  prog9a  and  c1  of  current  program)  with  from  statement
'''
from Madhan import c1 as C1 #How  to  import  class  c1  from  prog9a   with  from  statement
class   c1:
	def  __init__(self):
		print('c1  class  of  prog9d')
c=c1() #How  to  create  c1  class  object  of  current  module
#c1  class  of  prog9d


a=C1() #How  to  create  c1  class  object  of  prog9a
#c1  class  of  prog9a
 
 '''
 

#20.How  to  use  both  the  classes (i.e.  c1  of  prog9a  and  c1  of  current  program)  with  import  statement


'''
import Madhan #How  to  import  prog9a
class   c1:
	def  __init__(self):
		print('c1  class  of  prog9e')
e=c1() #How  to  create  c1  class  object  of  current  module
#c1  class  of  prog9e

a=Madhan.c1() #How  to  create  c1  class  object  of  prog9a
#c1  class  of  prog9a

'''