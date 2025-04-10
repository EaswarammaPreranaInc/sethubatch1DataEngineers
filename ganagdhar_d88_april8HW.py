
from april7 import  triangle

a=triangle()
triangle.get(a)
triangle.test(a)
print('Area : ', triangle.area(a)  )
print('Peri : ', triangle.peri(a)  )


#Write  a  program  to  determine  total , average  and  grade  of  a  student
#Inputs  are  Roll Number , Stud  Name , Marks  of  3  subjects  and  Gender

class student:

    def get(self):
        self.rno=eval(input("Enter roll number :"))
        self.sname=input("Enter Name :")
        self.gender=input("Enter Gender :")
        self.marks=[]
        for i in range(3):
            m=int(input("Enter a marks of subject : "))
            self.marks.append(m)
    def compute(self):
        total=300
        self.total_marks=sum(self.marks)
        self.avg=self.total_marks/3
        self.grade=(self.avg/total)*100
        if min(self.marks) <40:
            return "Fail"
        elif  self.grade >= 70:
            print ('Distinction')
        elif  self.grade >= 60:
            print ('First class')
        elif  self.grade >= 50:
            print ('Second class')
        else:
            print("Third class")

    def  disp(self):
        print('Roll  Number  :  ' ,   self.rno)
        print('Student  Name  :  ' , self.sname)
        print('Gender  :  ' ,  self.gender)
        print('Total  Marks : ',self.total_marks)
        print('Average  :  ' , self.avg)
        print('Grade  :  ' , self.grade)

    def __str__(self):
        return f"{self.rno}\t{self.sname}\t{self.gender}\t{self.total_marks}\t{self.avg}\t{self.grade}"


#Write  a  program  to  add , subtract , multiply  and  divide  two  rational  numbers

import math
class rat:
    def get(self):
        self.nr=eval(input("Enter Numerator : "))
        self.dr=eval(input("Enter Denominator : "))
        self.test()

    def test(self):
        while self.dr==0:
            self.dr=eval(input("Enter Denominator not be Zero,reenter : "))

    def __str__(self):
        return f"{self.nr}/{self.dr}"
    
    def add(self,m,n):
        self.nr=m.nr * n.dr+ n.nr * m.dr
        self.dr=m.dr * n.dr
        self.simplify()

    def sub(self,m,n):
        self.nr=m.nr * n.dr - n.nr * m.dr
        self.dr=m.dr * n.dr
        self.simplify()
    def mul(self,m,n):
        self.nr=m.nr *  n.nr
        self.dr=m.dr * n.dr
        self.simplify()

    def div(self,m,n):
        self.nr=m.nr* n.dr
        self.dr=m.dr * n.nr
        self.simplify()

    def simplify(self):
        if self.nr !=0:
            common=math.gcd(self.nr,self.dr)
            self.nr=self.nr//common
            self.dr=self.dr//common
       
        


if __name__ == "__main__":
    a=rat()
    b=rat()
    c=rat()
    d=rat()
    e=rat()
    f=rat()
    a.get()
    b.get()
    c.add(a,b)
    d.sub(a,b)
    e.mul(a,b)
    f.div(a,b)
    print("Sum : ",c)
    print("Subtraction : ",d)
    print("Multiplication : ",e)
    if b.nr != 0:
        print("Division : ",f)
    else:
        print("Division is not permitted")




#  Find  outputs  (Home  work)
class      Rat:
	def    m1():
		pass
# End  of  the  class
a = Rat()# empty object 'a' creation
a . nr = 22
print(hasattr(a , 'nr')) #True
print(hasattr(a , 'dr'))# False
print(hasattr(a , 'm1'))#True
print(hasattr(a , 'm2'))# False
print(hasattr(Rat , 'm1'))#True
print(hasattr(Rat , 'm2'))#False
print(hasattr(Rat , 'nr'))#false

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
	if   hasattr(x , 'talk'):#True for first iteration, Flase  for second iter, True  for third iter 
		x . talk()# Meow Meow Meow ....<next line>     Mehar  Mehar  Mehar  ....
	else:
		x . bark() #Bhow Bhow Bhow ....


#  Find  outputs  (Home  work)
class    c1:
        pass
# End of the class
a = c1()
a . x = 10
varname = input('Enter  variable  name  to  be  added  to  object  :  ')   #  Assume  that  input  is  'y'
value = eval(input('Enter  value  of  the  variable  :  '))   #  Assume  that  input  is   20
setattr(a , varname , value) # a.y = 20  create new instance variabke 'y'  to 'a'
print(a . __dict__)#{'x':10,'y':20}
print(a . x) # 10
while  True:
	try:
		varname = input('Enter  variable  name  whose  value  is  to  be  retrieved  :  ')
									#  Assume  that  input  is  x  in  1st   iteration  ,  y  in   2nd   iteration  and  z  in  3rd  iteration
		print(getattr(a , varname)) # 10 <nextline> 20
	except:
		print(F'Invalid  variable   name   :  {varname}')#Invalid  variable   name   : z
		break


#Write  a  program  to  convert  a  dictionary  {'Empno' : 25 , 'Ename' : 'Rama  Rao' , 'Sal' : 10000.0}  to  Emp  class  object
#i.e.  object  should  contain  empno = 25 , ename = 'Rama  Rao' , Sal = 10000.0
dict = {'Empno' : 25 , 'Ename' : 'Rama  Rao' , 'Sal' : 10000.0}
class  Emp:
    pass
e=Emp()
for x,y in dict.items():
    setattr(e,x,y)
for x in dict:
    print(f"{x} : {getattr(e,x)}")
