#8/4/2025 

#1. Triangle 
'''
from math import*
class Triangle:
    
    def get(self):
        self.a=int(input("Enter side a: "))
        self.b=int(input("Enter side b: "))
        self.c=int(input("Enter side c: "))
    
    def test(self,a,b,c):
        if(a+b > c and b+c>a and a+c>b):
            pass 
        
        else:
            print("Not a triangle")
            exit()
    
    def area(self,a,b,c):
        s=(a+b+c)/2 
        return sqrt(s*(s-a)*(s-b)*(s-c))
        
    def peri(self,a,b,c):
        return (a+b+c)
        
t=Triangle()    #How  to  create  triangle  object
Triangle.get(t)   #How  to  call  get()  method  in  another  way
Triangle.test(t,t.a,t.b,t.c)    #How  to  call  test()  method  in  another  way
print('Area : ', Triangle.area(t,t.a,t.b,t.c)) #How  to  call  area()  method  in  another  way
print('Perimeter: ',  Triangle.peri(t,t.a,t.b,t.c))#How  to  call  peri()  method  in  another  way

'''


'''
#2.
Write  a  program  to  determine  total , average  and  grade  of  a  student
Inputs  are  Roll Number , Stud  Name , Marks  of  3  subjects  and  Gender
'''

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
	def   __str__(self):
		return F'{self.rolno} {self.sname} {self.gender} {self.total_marks} {self.average} {self.grade}'
		#All  the   values  of  object  self  in  the  form  of  string
		
		
#End  of  the  class
s=Student()#How  to  create  Student  class  object
s.get() #How  to  read  inputs  into  object
s.compute() #How  to  store  results  in  object
s.disp() #How  to  print  object  with  disp()  method
s.__str__() #How  to  print  object  with  _str_()  method

'''



'''
#3.Write  a  program  to  add , subtract , multiply  and  divide  two  rational  numbers

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

"""
from math import*
class  Rat:
	def  get(self):
		self.nu= int(input("Enter numerator: ")) #How  to  read  numerator  into  object  self
		self.de= int(input("Enter denominator: ")) #How  to  read  denominator  into  object  self
		self.test() #How  to  call  test()  method
		
	def  test(self):
		#Ask  user  to  re enter  denom  when  denom  is  zero
		if(self.de==0):
		    self.de= int(input("Enter denominator: "))
		    
	def    _str_(self):
			 return  F'{self.nu}/{self.de}' #values  of  object  in  the  form  of  rational  number  such   as  '2 / 3'
			 
	def   add(self , a , b):
		self.nu= (a.nu*b.de + b.nu*a.de) #How  to  add  objects  'a'  and  'b' and  store  results  in  object  self
		self.de= (a.de*b.de)
		self.simplify() #How  to  simplify  object  self
	'''
	c . add(a , b)
	object  a  --->  2 / 3
	object  b  --->  5 / 9
	object  c  --->  2 / 3 + 5 / 9 = (2 * 9 + 5 * 3) / (5 * 9) = 33 / 27 = 11 / 9
	'''
	def   sub(self , a , b):
		self.nu= (a.nu*b.de - b.nu*a.de) #How  to  subtract  objects  'a'  and  'b' and  store  results  in  object  self
		self.de= (a.de*b.de) 
		self.simplify() #How  to  simplify  object  self
	'''
	d . sub(a , b)
	object  a  --->  2 / 3
	object  b  --->  5 / 9
	object  d  --->  2 / 3 - 5 / 9 = (2 * 9 - 5 * 3) / (5 * 9) = 3 / 27 = 1 / 9
	'''
	def   mul(self , a , b):
		self.nu= (a.nu*b.nu) #How  to  multiply  objects  'a'  and  'b' and  store  results  in  object  self
		self.de= (a.de*b.de) 
		self.simplify() #How  to  simplify  object  self
	'''
	e . mul(a , b)
	object  a  --->  2 / 3
	object  b  --->  5 / 9
	object  e  --->  2 / 3 * 5 / 9 = (2 * 5) / (3 * 9) = 10 / 27
	'''
	def    div(self , a , b):
		self.nu= (a.nu*b.de) 
		self.de=(a.de*b.nu) #How  to  divide  objects  'a'  and  'b' and  store  results  in  object  self
		self.simplify() #How  to  simplify  object  self
	'''
	f . div(a , b)
	object  a  --->  2 / 3
	object  b  --->  5 / 9
	object  f  --->  2 / 3 / 5 / 9 = 2 / 3 * 9 / 5 = (2 * 9) / (3 * 5) = 18 / 15 = 6 / 5
	'''
	def   simplify(self):
		g=gcd(self.nu,self.de) #How  to  find  gcd  of  numerator  and   denominator
		self.nu=self.nu//g
		self.de=self.de//g  #How  to  simplify  rational  number  in  object  self  i.e.  12 / 15  should  be  simplified  to  4 / 5
	'''
	c . simplify()
	1)  12 / 15  --->  4 / 5
	2) 10 / 27   --->  10 / 27
	3) 0 / 27  --->   0 / 27
	'''
# End  of the class
a=Rat(); b=Rat(); c=Rat();d=Rat();e=Rat();f=Rat() #How  to  create  6  objects  a , b , c , d , e , f
a.get() #How  to  read  rational  number  into  object  'a'
b.get() #How to  read  rational  number  into  object  'b'
c.add(a,b) #How  to  add  rational  numbers  in  objects  a  and  b  and  store  results  in  object  'c'
d.sub(a,b) #How  to  subtract  rational  numbers  in  objects  a  and  b  and  store  results  in  object  'd'
e.mul(a,b) #How  to multiply  rational  numbers  in  objects  a  and  b  and  store  results  in  object  'e'
f.div(a,b) #How  to  divide  rational  numbers  in  objects  a  and  b  and  store  results  in  object  'f'
print(F'{c.nu}/{c.de}') #How  to  print  object   'c'
print(F'{d.nu}/{d.de}') #How  to  print  object   'd'
print(F'{e.nu}/{e.de}') #How  to  print  object   'e'
if  f.de!=0:
	print(F'{f.nu}/{f.de}')#How  to  print  object  'f
else:
	print('Division  is  not  permitted')
	
"""



# 4.dir()  function  demo  program  
'''
from  prog10a   import  Rat
a = Rat()
a . nr = 22
a . dr = 7
print(dir(Rat)) #['environmental_variables','methods']
print()
print(dir(a)) ##['environmental_variables','methods']

'''

#5.Find  outputs 
'''
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

'''


#6.Find  outputs
'''
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
		x . talk() #1.Meow Meow Meow .... #3. Mehar  Mehar  Mehar  ....
	else:
		x . bark() #2.Bhow Bhow Bhow ....
		           
'''


#7. Find  outputs  
'''
class    c1:
        pass
# End of the class
a = c1()
a . x = 10
varname = input('Enter  variable  name  to  be  added  to  object  :  ')   #  Assume  that  input  is  'y'
value = eval(input('Enter  value  of  the  variable  :  '))   #  Assume  that  input  is   20
setattr(a , varname , value)
print(a .__dict__) #{'x':10 , 'y':20}
print(a . x) # 10
while  True:
	try:
		varname = input('Enter  variable  name  whose  value  is  to  be  retrieved  :  ')
									#  Assume  that  input  is  x  in  1st   iteration  ,  y  in   2nd   iteration  and  z  in  3rd  iteration
		print(getattr(a , varname)) #1. 10 20 
	except:
		print(F'Invalid  variable   name   :  {varname}')
		break


'''


'''
#8.
Write  a  program  to  convert  a  dictionary  {'Empno' : 25 , 'Ename' : 'Rama  Rao' , 'Sal' : 10000.0}  to  Emp  class  object
i.e.  object  should  contain  empno = 25 , ename = 'Rama  Rao' , Sal = 10000.0

Hint:  Use  setattr()  and  getattr()  functions
'''

'''
class  Emp:
        pass
#End  of  the  class
d = {'Empno' : 25 , 'Ename' : 'Rama  Rao' , 'Sal' : 10000.0}
e=Emp() 
for i in d:
    setattr(e,i,d[i]) #How  to  convert  dictionary  to  object  'e'  with  for  loop
    
#How  to  print  object  'e'  with  for  loop
for i in d:
    print(getattr(e,i))

'''