#  Write  a  program  to  determine  total  and  average  of  student  and  gross pay  and  net  pay  of  teacher
from  abc  import  *
class  person(ABC):
	def   get(self):
		self.number=int(input('Enter number: '))  #How  to   read  number
		self.name=input('Enter name: ')         #How  to   read  name
		self.age=int(input('Enter age: '))        #How  to   read   age
		self.gender=input('Enter gender: ')     #How  to   read   gender
	def   disp(self):
		print(f'number={self.number} \t name={self.name} \t age={self.age} \t gender={self.gender}')  #How  to  print  number , name , age , gender  in  same  line  separated  by  tab
	@abstractmethod
	def   compute(self):
                pass
class  student(person):
	def  get(self):
		super().get()  #How  to  read   number , name , age , gender
		self.m=eval(input('Enter marks of 3 subjects into list: '))    #How  to  read  marks  of  3  subjects  into  list
	def  compute(self):
		self.tot=sum(self.m)     #How  to  calculate  total  marks
		self.av=self.tot/len(self.m)     #How  to  calculate  average  marks
	def  disp(self):
		super().disp()    #How  to  print  number , name , age , gender
		print(f'total={self.tot} \t average={self.av}')   #How  to  print  total  and  average  in  same  line separated  by  tab
class  teacher(person):
	def   get(self):
		super().get()      #How  to  read  number , name , age  and  gender
		self.subject=input('Enter subject: ')    #How  to  read   subject
		self.sal=float(input('Enter salary: '))  #How  to  read   salary
	def   compute(self):
		self.da = self.sal*0.5       #50%  of  salary
		self.hra = self.sal*0.2         #20%  of  salary
		self.grosspay=self.sal+self.da+self.hra  #How  to  calculate  grosspay  and  store  the  result  in  object (grosspay  is  sal + da + hra)
		self.pf = min(0.08 * self.grosspay, 400)               #8%  of  grosspay  but  a  max  of  400
		self.tax = 0.10 * self.grosspay if self.grosspay < 10000 else (0.10*self.grosspay)+(0.15*self.grosspay)     #tax = 10%  of  grosspay  if  grosspay is  < 10000  and  15%  otherwise
		self.netpay=self.grosspay-self.pf-self.tax          #How  to  calculate  netpay  and  store  the  result  in  object  (netpay  is  grosspay - pf - tax)
	def   disp(self):
		super() . disp() # How  to  print  number , name , age , gender
		print(f'subject={self.subject} \t salary={self.sal} \t grosspay={self.grosspay} \t netpay={self.netpay}') # How  to  print  subject , salary , grosspay , netpay  in  same  line   separated  by  tab
# End  of  class
def  menu():
	print('1. Teacher')
	print('2. Student')
	print('3. Exit')
# End  of  the  function
a = []
i = 0
menu()
ch = eval(input('Enter choice : '))
while ch<3:
	if   ch == 1:
		t=teacher()
		a.append(t)      #How  to  append  teacher  object  to  list  'a'
	else:
		s=student()  
		a.append(s)         #How  to  append  student  object  to  list  'a'
	a[i].get()       #How  to  read  inputs  into  object
	a[i].compute()          #How  to  store   results  in  object
	i+=1            #How  to  move  to  next  index
	menu()
	ch = eval(input('Enter choice : '))
#end of loop
print('Teachers')
for obj in a:
	if isinstance(obj,teacher):
		obj.disp()        #How  to  print  all  teacher  objects
print()
print('Students')
for obj in a:
	if isinstance(obj,student):
		obj.disp()         #How  to  print  all  student  objects
print('Good  Bye')

OP-
1. Teacher
2. Student
3. Exit
Enter choice : 1
Enter number: 1
Enter name: Sharada
Enter age: 45
Enter gender: f
Enter subject: Telugu
Enter salary: 50000
1. Teacher
2. Student
3. Exit
Enter choice : 2
Enter number: 1
Enter name: Priya
Enter age: 25
Enter gender: f
Enter marks of 3 subjects into list: [80,90,100]
1. Teacher
2. Student
3. Exit
Enter choice : 1
Enter number: 2
Enter name: Shyamala
Enter age: 38
Enter gender: f
Enter subject: Social
Enter salary: 40000
1. Teacher
2. Student
3. Exit
Enter choice : 2
Enter number: 2
Enter name: Anusha
Enter age: 17
Enter gender: f
Enter marks of 3 subjects into list: [80,90,60]
1. Teacher
2. Student
3. Exit
Enter choice : 3
Teachers
number=1         name=Sharada    age=45          gender=f
subject=Telugu   salary=50000.0          grosspay=85000.0        netpay=71850.0
number=2         name=Shyamala   age=38          gender=f
subject=Social   salary=40000.0          grosspay=68000.0        netpay=57400.0

Students
number=1         name=Priya      age=25          gender=f
total=270        average=90.0
number=2         name=Anusha     age=17          gender=f
total=230        average=76.66666666666667
Good  Bye
