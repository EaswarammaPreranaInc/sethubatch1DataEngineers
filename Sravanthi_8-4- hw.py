08.04.2025 hw'''
#1
Repeat  prog5a  such  that  methods  are  called  in  another  way

1) What  are  the  two  ways  to  call  a  method ?  --->  object . method()  and  classname . method(object)

2) Import  and   use  triangle  class  defined  in  prog5a  but  do  not   define  triangle  class  again
'''
'''
from prog5a import 
t= triangle# How  to  create  triangle  object
triangle.get(t) # How  to  call  get()  method  in  another  way
triangle.test(t) # How  to  call  test()  method  in  another  way
print('Area : ', triangle.area(t) )#(How  to  call  area()  method  in  another  way)
print('Perimeter: ', triangle.peri(t) )#(How  to  call  peri()  method  in  another  way)
'''

'''
# 2
Write  a  program  to  determine  total , average  and  grade  of  a  student
Inputs  are  Roll Number , Stud  Name , Marks  of  3  subjects  and  Gender
'''

'''
class   Student:
	def   get(self):
		How  to  read  roll  number  into  object  self
		How  to  read  student  name  into  object  self
		How  to  read  gender  into  object  self
		How  to  read  marks  of  3  subjects
	def   compute(self):
		How  to  calculate  total  marks
		How  to  calculate  average  marks
		if  At  least  one  subject  is  below  40:
				How  to  initilaize  grade  to  'Fail'
		elif  average  is  above  >= 70%:
				How  to  initilaize  grade  to  'Distinction'
		elif  average  is  above  >= 60%:
				How  to  initilaize  grade  to  'First  class'
		elif  average  is  above  >= 50%:
				How  to  initilaize  grade  to  'Second  class'
		else:
				How  to  initilaize  grade  to  'Third  class'
	def  disp(self):
		print('Roll  Number  :  ' ,   ???)
		print('Student  Name  :  ' , ???)
		print('Gender  :  ' ,  ???)
		print('Total  Marks  :  ' , ???)
		print('Average  :  ' , ???)
		print('Grade  :  ' , ???)
	def   str(self):
		return  All  the   values  of  object  self  in  the  form  of  string
#End  of  the  class
How  to  create  Student  class  object
How  to  read  inputs  into  object
How  to  store  results  in  object
How  to  print  object  with  disp()  method
How  to  print  object  with  str()  method
'''
'''
class   student:
	def   get(self):
			self.rno=eval(input('Enter roll no:')) # How  to  read  roll  number  into  object  self
			self.sname=input('Enter name:') # How  to  read  student  name  into  object  self
			self.gender=input('Enter gender(m/f):') # How  to  read  gender  into  object  self
			self.m=[] # How  to  read  marks  of  3  subjects
			for i in range(3):
					marks=int(input(F'Enter marks of subject {i+1}:'))
					self.m.append(marks)
	def   compute(self):
			self.tot=sum(self.m) # How  to  calculate  total  marks
			self.avg=self.tot/3 # How  to  calculate  average  marks
			if min(self.m)<40: # At  least  one  subject  is  below  40:
					self.grade='Fail' # How  to  initilaize  grade  to  'Fail'
			elif self.avg>=70: # average  is  above  >= 70%:
					self.grade='Distinction' # How  to  initilaize  grade  to  'Distinction'
			elif self.avg>60: # average  is  above  >= 60%:
					self.grade='First class' # How  to  initilaize  grade  to  'First  class'
			elif self.avg>50: # average  is  above  >= 50%:
					self.grade='Second class' # How  to  initilaize  grade  to  'Second  class'
			else:
					self.grade='Third class' # How  to  initilaize  grade  to  'Third  class'

	def  disp(self):
			print('Roll  Number  :  ' , self.rno)
			print('Student  Name  :  ' , self.sname)
			print('Gender  :  ' ,  self.gender)
			print('Total  Marks  :  ' , self.tot)
			print(F'Average  :   , {self.avg:.2f}')
			print('Grade  :  ' , self.grade)

	def   _str_(self):
			return f'{self.rno} \t {self.sname} \t {self.gender} \t {self.tot} \t {self.avg:.2f} \t {self.grade}'  # All  the   values  of  object  self  in  the  form  of  string

#End  of  the  class
s= student() # How  to  create  Student  class  object
s.get() # How  to  read  inputs  into  object
s.compute() # How  to  store  results  in  object
s.disp() # How  to  print  object  with  disp()  method
print(s) # How  to  print  object  with  str()  method


Output:
Enter roll no:1
Enter name:Ram
Enter gender(m/f):male
Enter marks of subject 1:39
Enter marks of subject 2:39
Enter marks of subject 3:39
Roll  Number  :   1
Student  Name  :   Ram
Gender  :   male
Total  Marks  :   117
Average  :   , 39.00
Grade  :   Fail
1        Ram     male    117     39.00   Fail


Enter roll no:1
Enter name:Ram
Enter gender(m/f):male 
Enter marks of subject 1:60
Enter marks of subject 2:70
Enter marks of subject 3:80
Roll  Number  :   1
Student  Name  :   Ram
Gender  :   male
Total  Marks  :   210
Average  :   , 70.00
Grade  :   Distinction
1        Ram     male    210     70.00   Distinction


Enter roll no:1
Enter name:Ram
Enter gender(m/f):male
Enter marks of subject 1:61
Enter marks of subject 2:61
Enter marks of subject 3:61
Roll  Number  :   1
Student  Name  :   Ram
Gender  :   male
Total  Marks  :   183
Average  :   , 61.00
Grade  :   First class
1        Ram     male    183     61.00   First class


Enter roll no:1
Enter name:Ram
Enter gender(m/f):male
Enter marks of subject 1:59
Enter marks of subject 2:59
Enter marks of subject 3:59
Roll  Number  :   1
Student  Name  :   Ram
Gender  :   male
Total  Marks  :   177
Average  :   , 59.00
Grade  :   Second class
1        Ram     male    177     59.00   Second class


Enter roll no:1
Enter name:Ram
Enter gender(m/f):male
Enter marks of subject 1:41
Enter marks of subject 2:41
Enter marks of subject 3:41
Roll  Number  :   1
Student  Name  :   Ram
Gender  :   male
Total  Marks  :   123
Average  :   , 41.00
Grade  :   Third class
1        Ram     male    123     41.00   Third class
'''

'''
# 3
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

'''
# import  math
# class  Rat:
# 	def  get(self):
# 		How  to  read  numerator  into  object  self
# 		How  to  read  denominator  into  object  self
# 		How  to  call  test()  method
# 	def  test(self):
# 		Ask  user  to  reenter  denom  when  denom  is  zero
# 	def    str(self):
# 			 return  values  of  object  in  the  form  of  rational  number  such   as  '2 / 3'
# 	def   add(self , a , b):
# 		How  to  add  objects  'a'  and  'b' and  store  results  in  object  self
# 		How  to  simplify  object  self
# 	'''
# # '''
# # 	c . add(a , b)
# # 	object  a  --->  2 / 3
# # 	object  b  --->  5 / 9
# # 	object  c  --->  2 / 3 + 5 / 9 = (2 * 9 + 5 * 3) / (5 * 9) = 33 / 27 = 11 / 9
# # '''
	
# 	# def   sub(self , a , b):
# 	# 	How  to  subtract  objects  'a'  and  'b' and  store  results  in  object  self
# 	# 	How  to  simplify  object  self
	
# # '''
# # 	d . sub(a , b)
# # 	object  a  --->  2 / 3
# # 	object  b  --->  5 / 9
# # 	object  d  --->  2 / 3 - 5 / 9 = (2 * 9 - 5 * 3) / (5 * 9) = 3 / 27 = 1 / 9
# # 	'''
# 	'''
# 	def   mul(self , a , b):
# 		How  to  multiply  objects  'a'  and  'b' and  store  results  in  object  self
# 		How  to  simplify  object  self
# 	'''
# '''
# 	e . mul(a , b)
# 	object  a  --->  2 / 3
# 	object  b  --->  5 / 9
# 	object  e  --->  2 / 3 * 5 / 9 = (2 * 5) / (3 * 9) = 10 / 27
# 	'''
# '''
# 	def    div(self , a , b):
# 		How  to  divide  objects  'a'  and  'b' and  store  results  in  object  self
# 		How  to  simplify  object  self
# 	'''
# '''
# 	f . div(a , b)
# 	object  a  --->  2 / 3
# 	object  b  --->  5 / 9
# 	object  f  --->  2 / 3 / 5 / 9 = 2 / 3 * 9 / 5 = (2 * 9) / (3 * 5) = 18 / 15 = 6 / 5
# 	'''
# 	'''
# 	def   simplify(self):
# 			How  to  find  gcd  of  numerator  and   denominator
# 			How  to  simplify  rational  number  in  object  self  i.e.  12 / 15  should  be  simplified  to  4 / 5
# 	'''
# # '''
# # 	c . simplify()
# # 	1)  12 / 15  --->  4 / 5
# # 	2) 10 / 27   --->  10 / 27
# # 	3) 0 / 27  --->   0 / 27
# # 	'''
# 	'''
# # End  of the class
# How  to  create  6  objects  a , b , c , d , e , f
# How  to  read  rational  number  into  object  'a'
# How to  read  rational  number  into  object  'b'
# How  to  add  rational  numbers  in  objects  a  and  b  and  store  results  in  object  'c'
# How  to  subtract  rational  numbers  in  objects  a  and  b  and  store  results  in  object  'd'
# How  to multiply  rational  numbers  in  objects  a  and  b  and  store  results  in  object  'e'
# How  to  divide  rational  numbers  in  objects  a  and  b  and  store  results  in  object  'f'
# How  to  print  object   'c'
# How  to  print  object   'd'
# How  to  print  object   'e'
# if  ???
# 	How  to  print  object  'f
# else:
# 	print('Division  is  not  permitted')
# '''
'''
import math
class rat:
    def get(self):
        self.nr = int(input('Enter the numerator: '))
        self.dr = int(input('Enter the denominator: '))
        self.test()

    def test(self):
        while self.dr == 0:
            self.dr = int(input('Denominator cannot be zero, reenter: '))

    def _str_(self):
        return f'{self.nr}/{self.dr}'

    def add(self, a, b):
        self.nr = a.nr * b.dr + a.dr * b.nr
        self.dr = a.dr * b.dr
        self.simplify()

    def sub(self, a, b):
        self.nr = a.nr * b.dr - a.dr * b.nr
        self.dr = a.dr * b.dr
        self.simplify()  # FIXED typo: was siplify()

    def mul(self, a, b):
        self.nr = a.nr * b.nr
        self.dr = a.dr * b.dr
        self.simplify()

    def div(self, a, b):
        self.nr = a.nr * b.dr
        self.dr = a.dr * b.nr
        self.simplify()

    def simplify(self):
        if self.nr != 0:
            ans = math.gcd(self.nr, self.dr)
            self.nr = self.nr // ans
            self.dr = self.dr // ans

# End of the class
if _name=='main_':
	a = rat()
	b = rat()
	c = rat()
	d = rat()
	e = rat()
	f = rat()

	a.get()
	b.get()

	c.add(a, b)
	d.sub(a, b)
	e.mul(a, b)

	print('Sum: ', c)
	print('Difference: ', d)
	print('Product: ', e)

	if b.nr != 0:
		f.div(a, b)
		print('Division: ', f)
	else:
		print('Division is not permitted')

Output:
Enter the numerator: 2
Enter the denominator: 3
Enter the numerator: 5
Enter the denominator: 9
Sum:  11/9
Difference:  1/9
Product:  10/27
Division:  6/5
'''

'''
# 4
#  dir()  function  demo  program  (Home  work)
from  prog10a   import  Rat
a = Rat()
a . nr = 22
a . dr = 7
print(dir(Rat))
print()
print()
print(dir(a))

Output:
Enter the numerator: 2 
Enter the denominator: 3
Enter the numerator: 5
Enter the denominator: 9
Sum:  11/9
Difference:  1/9
Product:  10/27
Division:  6/5
'''

'''
# 5
#  Find  outputs  (Home  work)
class      Rat:
	def    m1():
		pass
# End  of  the  class
a = Rat() #Empty object
a . nr = 22 # Adds variable nr to object 'a' with variable 22
print(hasattr(a , 'nr')) # True: Variable 'nr' exists in object 'a'
print(hasattr(a , 'dr')) # False: Variable 'dr' does not exist in object 'a' 
print(hasattr(a , 'm1')) # True: Method 'm1' exist in class rat 
print(hasattr(a , 'm2')) # False: method 'm2' does not exist in class rat
print(hasattr(Rat , 'm1')) # True: method 'm1' exist in class rat
print(hasattr(Rat , 'm2')) # False: method 'm2' does not exist in class rat
print(hasattr(Rat , 'nr')) # False: method 'nr' does not exist in class rat

Output:
True
False
True
False
True
False
False
'''


'''
# 6
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


Output:
Meow Meow Meow ....
Bhow Bhow Bhow ....
Mehar  Mehar  Mehar  ....
'''

'''
# 7
#  Find  outputs  (Home  work)
class    c1:
        pass
# End of the class
a = c1()
a . x = 10
varname = input('Enter  variable  name  to  be  added  to  object  :  ')   #  Assume  that  input  is  'y'
value = eval(input('Enter  value  of  the  variable  :  '))   #  Assume  that  input  is   20
setattr(a , varname , value)
print(a . _dict_)
print(a . x) # 10
while  True:
	try:
		varname = input('Enter  variable  name  whose  value  is  to  be  retrieved  :  ')
									#  Assume  that  input  is  x  in  1st   iteration  ,  y  in   2nd   iteration  and  z  in  3rd  iteration
		print(getattr(a , varname))
	except:
		print(F'Invalid  variable   name   :  {varname}')
		break

Output:
Enter  variable  name  to  be  added  to  object  :  y
Enter  value  of  the  variable  :  20
{'x': 10, 'y': 20}
10
'''


'''
# 8
(Home  work)
Write  a  program  to  convert  a  dictionary  {'Empno' : 25 , 'Ename' : 'Rama  Rao' , 'Sal' : 10000.0}  to  Emp  class  object
i.e.  object  should  contain  empno = 25 , ename = 'Rama  Rao' , Sal = 10000.0

Hint:  Use  setattr()  and  getattr()  functions
'''
'''
class  emp:
        pass
#End  of  the  class
dict = {'Empno' : 25 , 'Ename' : 'Rama  Rao' , 'Sal' : 10000.0}
How  to  convert  dictionary  to  object  'e'  with  for  loop
How  to  print  object  'e'  with  for  loop
'''
'''
class emp:
    pass
#End of the class
dict={'Empno':25, 'Ename':'Rama Rao', 'Sai':10000.0}
e=emp()
for key, value in dict.items(): 
    setattr(e, key, value) # How  to  convert  dictionary  to  object  'e'  with  for  loop
for key in dict.keys():
    print(key, getattr(e, key), sep='...')#How  to  print  object  'e'  with  for  loop

Output:
Empno...25
Ename...Rama Rao
Sai...10000.0
'''
