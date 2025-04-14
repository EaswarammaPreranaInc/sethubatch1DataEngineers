#  Variable  number  of  arguments  demo  program
def   f1(*t):
	print(t)
	print(type(t))
	print(len(t))
	print()
# End  of  the  function
f1(10 , 20 , 15 , 18)   #  Tuple  of  4  elements  is  passed  to  the  function
f1()
f1([10 , 20] , (30 , 40 , 50) , {60 , 70 , 80 , 90})
f1('Hyd')
tpl = (100 , 200 , 150)
f1(tpl)
#f1(t = (10 , 20 , 30))  #  Error  :  var-arg  param  can  not be  KA
def avg(*a):
    try:
        return sum(a)/len(a)
    except ZeroDivisionError:
        return "there should be atleast 2 numbers "
    except TypeError:
        return sum(*a)/len(*a)
        
# End  of  the  function
print(avg(10 , 20 , 15 , 18)) #  Average  of  10 , 20 , 15  and  18
print(avg(25 , 10.8 , True))
print(avg(10.8 , 20.6 , 15.2 , 14.9 , 9.8))
print(avg())
print(avg(25))
print(avg(3 + 4j , 5 + 6j))
tpl = (10 , 20 , 15 , 18)
print(avg(tpl))
#Gift
#Write  a  function  to  concatenate  strings  passed  from  the  function  call ? (Home  work)

def  concat(*a):
    try:
        return ' '.join(a)
    except:
        return "enter only string input"
        
print(concat('Sankar', 'Dayal', 'Sarma'))  # Sankar Dayal Sarma
print(concat('Hyd', 'Is', 'Green', 'City'))
print(concat('Python', 'Is', 'A', 'Great', 'Language'))
print(concat())
print(concat('Python'))
print(concat(1, 2, 3
#Find  outputs (Home  work)
def   f1(a = 25  , *b,c = 25  ,):	
        print(F'a : {a}  \t   b  :  {b} \t c: {c}')
# End  of  the  function
f1(10 , 20 , 30 , 40)
f1(50 , 60)
f1(70)
f1(a = 80)
#f1(b = (10 , 20 , 30) , a = 40)
f1(20,5,c=30)
#f1(a = 10 , (20 , 30 , 40))
#f1(25 , b = (10 , 20 , 30))
#f1(25 , a = (10 , 20 , 30))
f1((10 , 20 , 30) , 10 , 20 , 30)
#f1(a = (10 , 20 , 30) , 10 , 20 , 30)
#Find  outputs (Home  work)
def    f1(*a , b):
	print(F'a  :  {a}   \t   b  :  {b}')
# End  of  the  function
f1(10 , 20 , 30 , b = 40)
f1(50 , b = 60)
f1(b = 70)
#f1(b = 10 , a = (20 , 30 , 40))  #KA should go after PA
#f1(b = 10 , (20 , 30 , 40))  #KA should go after PA
#f1()
#f1(10 , 20 , 30 , (10 , 20 , 30)) #KA should be given, only a is given
#f1(10 , 20 , 30 , 40)
#f1(25)
f1(10 , 20 , 30 , b = (10 , 20 , 30))
#Find  outputs (Home  work)
def   f1(a , *b , c):
        print(F'a  :  {a}  \t  b  :  {b}  \t  c  :  {c}')
# End  of  the  function
f1(10 , 20 , 30 , 40 , c = 50)
f1(60 , 70 , c = 80)
f1(90 , c = 100)
#f1(a = 1 , 2 , c = 3)
#f1(1 , 2 , 3)
#f1(a = 1 , b = 2 , c = 3)
#f1(a = 25 , 100 , 200 , 300 , c = 35)
# Which  of  the  following  are  valid  ?  (Home  work)
#def   f1(*a , *b): * argument may appear only once
#        pass
def  f2(*a , b): #valid
        pass
def  f3(a , *b):#valid
        pass
def  f4(a , b):#valid
        pass
def    f5(a , *b , c):
        pass
#def   f6( * , a , *b , c):* argument may appear only once
 #      pass
#def   f7(a , *b , c ,  /): / must be ahead of *
 #      pass
# Find  outputs  (Home  work)
def   f1(*a):
	print(a)
	print(type(a))
	for  x  in  a:
		print(x)
		print(type(x))
# End  of  the  function
f1([10 , 20] , {30 , 40} , (50 , 60))
# Variable  number  of  keyword  arguments  demo  program
def   disp(**a):
	print('Results')
	print(type(a))
	print(a)
	print()
#End  of  the  function
disp(RollNo = 10 , StudName = 'Rama  Rao')  #  Dictionary  of  2  key : value  pairs  is  passed  to  the  function
disp(EmpNo = 25 , EmpName = 'Sita' , Salary = 10000.0) #KA entered into function gets stored as dict in KA as Keys and values
disp(AcNo = 30 , CustName = 'Kiran' , Balance = 20000.0 , Gender = 'm')
disp()
# Find  outputs  (Home  work)
def  f1(**a):
	print('Results')
	for  k , v   in   a . items():
		print(k , v , sep = ' ... ')
# End  of  the  function
f1(Empno = 25 , Empname = 'Rama  Rao' , Salary = 10000.0 , Gender = 'm')
f1()
'''Results
Empno ... 25
Empname ... Rama  Rao
Salary ... 10000.0
Gender ... m
Results'''
# Find  outputs (Home  work)
def   f1(*a): #PA only
	print(type(a))
	print(a)
def   f2(**a):#KA only
	print(type(a))
	print(a)
# End  of  the  function
f1(25 , 10.8 , 'Hyd' , True)
print()
f2(EmpNum = 25 , EmpName =  'Sita' , Salary = 10000.0)
#  Find  outputs (Home work)
def   f1(empno , ename , sal):
	print(F'Emp  Number  :  {empno}  \t  Emp  Name  :  {ename}  \t  Salary  :	{sal}')
def   f2(**a):
	print(a)
# End  of  the  function
f1(empno = 25 , ename = 'Sita' , sal = 10000.0)
#f1(eno = 25 , empname = 'Sita' , salary = 10000.0)
f2(empno = 25 , ename = 'Sita' , sal = 10000.0)
f2(eno = 25 , empname = 'Sita' , salary = 10000.0)
# Find  outputs   (Home  work)
def    f1(a ,  *b , **c):
	print(a)
	if   b:
		print(b)
	if  c:
		print(c)
# End  of  the  function
f1(25)
print()
f1('Hyd' , 10 , 20 , 30)
print()
f1(10.8 , 25 , 'Hyd' , True , EmpNo = 12 , EmpName = 'Rama  Rao' , Salary = 10000.0)
25

Hyd
(10, 20, 30)

10.8
(25, 'Hyd', True)
{'EmpNo': 12, 'EmpName': 'Rama  Rao', 'Salary': 10000.0}
#Find  outputs (Home  work)
a = 10
def   f1():
	b = 40
	print('a : ' , a)
	print('b : ' , b)
	print('c : ' , c)
	print()
# End  of  f1()  function
b = 20
def    f2():
	a = 50
	print('a : ' , a)
	print('b : ' , b)
	print('c : ' , c)
# End  of  f2()  function
c = 30
print('a : ' , a)
print('b : ' , b)
print('c : ' , c)
print()
a +=  1
b +=  1
c +=  1
f1()
a +=  1
b +=  1
c +=  1
f2()
print('Bye')
# Find  outputs (Home  work)
def   f1():
	a = 20
	print(a)
	a += 1
#End  of  the  function
a = 10
print(a) #10
a += 1
f1() #20
print(a) #11
# Find  outputs  (Home  work)
def   f1():
	a = 20
	print(a) #20
	dict = globals()
	print(dict['a']) #11
	a = 30
	dict['a'] = 40
#  End  of  f1()  function
a = 10
print(a) #10
a += 1
f1()
print(a) #40
# Find  outputs (Home  work)
def  f1():
	x = 20
	print(x) #20
	print(globals()['x']) #10
# End  of  the  function
f1()
# Find outputs (Home  work)
def  f1():
	a = 40
	b = 50
	c = 60
	print(a , b , c)
	dict = globals()
	print(dict['a'] , dict['b'] , dict['c'])
	dict['a'] = 100
	dict['b'] = 200
	dict['c'] = 300
def  f2():
	print(a , b , c)
# End  of  f2  function
a = 10
b = 20
c = 30
f1()
f2()
'''40 50 60
10 20 30
100 200 300'''
# global  keyword  demo  program (Home  work)
def    f1():
	x = 20
	print(x) #20
def   f2():
	global  x
	x = 30
	print(x) #30
	x += 1
def   f3():
	global  y
	y = 40
	print("r",y)
	y += 1
def   f4():
	x = 50
	#global   x
#  End  of  the  functions
x = 10
print(x) #10
x += 1
f1()
print(x) #11
f2() #
print(x) #31
x += 1
f3()
print("r",y)
f4()
print(x) #32
# Find outputs (Home  work)
def  f1():
	global  a
	a = 20
	print(a) #20
	print(globals()['a']) #20
	a = 30
# End of the function
a = 10
print(a)#10
f1()
print(a) #30
# Find  outputs(Home  work)
def  f1():
	global  z
	#print(z)
	z = 10
	print(globals()['z'])
	z = 20
	print(z)
	z = 30
def  f2():
	print(z)
# End  of   f2   function
f1()
f2()
print(z)
# Find outputs (Home  work)
def  f1():
	global   a
	a = 10
	print(a)
	a = 20
def  f2():
	global  a
	print(a)
	a = 30
def  f3():
	print(a)
	globals()['a'] = 40
# End  of  the  function
f1() #10
f2() #20
f3() #
print(a)

