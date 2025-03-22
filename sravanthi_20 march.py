.............1
#Variable  number  of  arguments  demo  program
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
#f1(t = (10 , 20 , 30))  #  Error  :  var-arg  param  can  not be  ka
output:
(10, 20, 15, 18)
<class 'tuple'>
4

()
<class 'tuple'>
0

([10, 20], (30, 40, 50), {80, 90, 60, 70})
<class 'tuple'>
3

('Hyd',)
<class 'tuple'>
1

((100, 200, 150),)
<class 'tuple'>
............2
#Find  outputs (Home  work)
def   f1(a = 25  , *b):	
        print(F'a : {a}  \t   b  :  {b} ')
# End  of  the  function
f1(10 , 20 , 30 , 40)
f1(50 , 60)
f1(70)
f1(a = 80)
#f1(b = (10 , 20 , 30) , a = 40)
f1()
#f1(a = 10 , (20 , 30 , 40))
#f1(25 , b = (10 , 20 , 30))
#f1(25 , a = (10 , 20 , 30))
f1((10 , 20 , 30) , 10 , 20 , 30)
#f1(a = (10 , 20 , 30) , 10 , 20 , 30)
output:
a : 10             b  :  (20, 30, 40)
a : 50             b  :  (60,)
a : 70             b  :  ()
a : 80             b  :  ()
a : 25             b  :  ()
a : (10, 20, 30)           b  :  (10, 20, 30)
..........3
def    f1(*a , b):
	print(F'a  :  {a}   \t   b  :  {b}')
# End  of  the  function
f1(10 , 20 , 30 , b = 40)
f1(50 , b = 60)
f1(b = 70)
#f1(b = 10 , a = (20 , 30 , 40))
#f1(b = 10 , (20 , 30 , 40))
#f1()
#f1(10 , 20 , 30 , (10 , 20 , 30))
#f1(10 , 20 , 30 , 40)
#f1(25)
f1(10 , 20 , 30 , b = (10 , 20 , 30))
output:
a  :  (10, 20, 30)         b  :  40
a  :  (50,)        b  :  60
a  :  ()           b  :  70
a  :  (10, 20, 30)         b  :  (10, 20, 30)
..........4
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
output:
a  :  10          b  :  (20, 30, 40)      c  :  50
a  :  60          b  :  (70,)     c  :  80
a  :  90          b  :  ()        c  :  100
........5
def   f1(*a):
	print(a)
	print(type(a))
	for  x  in  a:
		print(x)
		print(type(x))
# End  of  the  function
f1([10 , 20] , {30 , 40} , (50 , 60))
output:
([10, 20], {40, 30}, (50, 60))
<class 'tuple'>
[10, 20]
<class 'list'>
{40, 30}
<class 'set'>
(50, 60)
<class 'tuple'>
........6
def   disp(**a):
	print('Results')
	print(type(a))
	print(a)
	print()
#End  of  the  function
disp(RollNo = 10 , StudName = 'Rama  Rao')  #  Dictionary  of  2  key : value  pairs  is  passed  to  the  function
disp(EmpNo = 25 , EmpName = 'Sita' , Salary = 10000.0)
disp(AcNo = 30 , CustName = 'Kiran' , Balance = 20000.0 , Gender = 'm')
disp()
output:
Results
<class 'dict'>
{'RollNo': 10, 'StudName': 'Rama  Rao'}

Results
<class 'dict'>
{'EmpNo': 25, 'EmpName': 'Sita', 'Salary': 10000.0}

Results
<class 'dict'>
{'AcNo': 30, 'CustName': 'Kiran', 'Balance': 20000.0, 'Gender': 'm'}

Results
<class 'dict'>
{}
.........7
def  f1(**a):
	print('Results')
	for  k , v   in   a . items():
		print(k , v , sep = ' ... ')
# End  of  the  function
f1(Empno = 25 , Empname = 'Rama  Rao' , Salary = 10000.0 , Gender = 'm')
f1()
output:
Results
Empno ... 25
Empname ... Rama  Rao
Salary ... 10000.0
Gender ... m
Results
..........8
def   f1(*a):
	print(type(a))
	print(a)
def   f2(**a):
	print(type(a))
	print(a)
# End  of  the  function
f1(25 , 10.8 , 'Hyd' , True)
print()
f2(EmpNum = 25 , EmpName =  'Sita' , Salary = 10000.0)
output:
<class 'tuple'>
(25, 10.8, 'Hyd', True)

<class 'dict'>
{'EmpNum': 25, 'EmpName': 'Sita', 'Salary': 10000.0}
.........9
def   f1(empno , ename , sal):
	print(F'Emp  Number  :  {empno}  \t  Emp  Name  :  {ename}  \t  Salary  :	{sal}')
def   f2(**a):
	print(a)
# End  of  the  function
f1(empno = 25 , ename = 'Sita' , sal = 10000.0)
f1(eno = 25 , empname = 'Sita' , salary = 10000.0)
f2(empno = 25 , ename = 'Sita' , sal = 10000.0)
f2(eno = 25 , empname = 'Sita' , salary = 10000.0)
output:
Emp  Number  :  25        Emp  Name  :  Sita      Salary  :     10000.0
{'empno': 25, 'ename': 'Sita', 'sal': 10000.0}
{'eno': 25, 'empname': 'Sita', 'salary': 10000.0}
...........10
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
output:
25

Hyd
(10, 20, 30)

10.8
(25, 'Hyd', True)
{'EmpNo': 12, 'EmpName': 'Rama  Rao', 'Salary': 10000.0}


	




