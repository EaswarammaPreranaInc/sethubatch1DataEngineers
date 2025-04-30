'''
PROGRAM_1:
'''
#  return  statement  demo  program
def  f1():
	print('f1  function')
	return  25
	print('Hello')
print('Begin')
x =  f1()
print(x)
print('End')
'''
OUTPUT:
Begin
f1  function
25
End
'''
# Find outputs  (Home  work)
def   f1():
	print('Hyd')
	print('Sec')
	print('Cyb')
print('Begin')
x = f1()
print(x)
print(type(x))
print('End')
'''
OUTPUT:
Begin
Hyd
Sec
Cyb
None
<class 'NoneType'>
End
'''
# Find  outputs  (Home  work)
def  f1():
	return  10 , 20 , 30
x = f1()
print(x)
print(type(x))
a , b , c =  f1()
print(a)
print(b)
print(c)
print('for  loop')
for k in f1():
	print(k)
'''
OUTPUT:
(10, 20, 30)
<class 'tuple'>
10
20
30
for  loop
10
20
30
'''
# Find  outputs
def f1():
	return 10
	return 20
	return 30
print('Begin')
x = f1()
print(x)
print('End')
#return 100
'''
OUTPUT:
Begin
10
End
'''
#  Find  outputs
f1()
def   f1():
        print('Hello')
print(f1())
print(f1)
'''
OUTPUT:
Hello
None
<function f1 at 0x00000153B7F71440>
'''
# Find  outputs  (Home  work)
print('Hello')
def  f1():
        print('f1  function')
print('Hi')
print(f1())
print(f1)
print('Bye')
'''
OUTPUT:
Hello
Hi
f1  function
None
<function f1 at 0x00000216E9283F60>
Bye
'''
#  Find  outputs
def    f1():
        print('Hyd')
        print('Sec')
        print('Cyb')
print('Begin')
print(type(f1))
print(id(f1))
print('End')
'''
OUTPUT:
Begin
<class 'function'>
1838395768672
End
'''
# Find  outputs (Home  work)

def  f1():
	print('No-argument  function')
def  f1(x):
	print('Single  argument  function  : ' , x)
def  f1(x,y):
	print('Two  argument  function : ' , x , y)
def  f1(x,y,z):
	print('Three  argument  function : ' , x , y , z)
f1(10,20,30)
#f1(40,50) --->f1() missing 1 required positional argument: 'z'
#f1(60) --->f1() missing 2 required positional arguments: 'y' and 'z'
#f1(60) --->f1() missing 2 required positional arguments: 'y' and 'z'
#f1() --->f1() missing 3 required positional arguments: 'x', 'y', and 'z'
'''
OUTPUT:
Three  argument  function :  10 20 30
'''
# Modify  following  program  such  that  every  function  should  be  executed
def  f1():
	print('No-argument  function')
f1()
def  f1(x):
	print('Single  argument  function  : ' , x)
f1(60)
def  f1(x , y):
	print('Two  argument  function : ' , x , y)
f1(40,50)
def  f1(x , y , z):
	print('Three  argument  function : ',x,y,z)
f1(10,20,30)
'''
OUTPUT:
No-argument  function
Single  argument  function  :  60
Two  argument  function :  40 50
Three  argument  function :  10 20 30
'''
'''
PROGRAM_2:
Write   a  function  to  test  a  number  is  prime  (or)  not.
1) What  is  a  prime  number ?  --->  A  number  without  divisors  except  1  and  itself
'''
def prime(n):
	for i in range(2,(n//2)+1):
		if n%i==0:
			return False
	else:
		return True
n=int(input("Enter number to check prime or not : "))
if n<2:
	print("Invalid input")
elif prime(n):
	print("Prime Number")
else:
	print("Composite Number")
# Find  outputs  (Home  work)
def   disp(empno , ename , sal):
        print(F'Emp  Number  :  {empno} \t  Emp Name  :  {ename} \t  Salary  :  {sal}')
disp(25,'Rama  Rao',10000.0)
disp('Sita',20000.0,35)
'''
OUTPUT:
Emp  Number  :  25        Emp Name  :  Rama  Rao          Salary  :  10000.0
Emp  Number  :  Sita      Emp Name  :  20000.0    Salary  :  35 --->not desired results
'''
# Find  outputs (Home  work)
def    disp(empno , ename , sal):
        print(F'Emp  Number : {empno:4}  \t  Emp  Name : {ename:15}  \t  Salary : {sal}')
disp(25,'Rama Rao',10000.0)
disp(ename = 'Sita' , sal = 20000.0 , empno = 35)
x = 'Rama  Rao'
y = 30000.0
z = 20
disp(x,y,z)
'''
OUTPUT:
Emp  Number :   25        Emp  Name : Rama Rao            Salary : 10000.0
Emp  Number :   35        Emp  Name : Sita                Salary : 20000.0
Emp  Number : Rama  Rao           Emp  Name :         30000.0     Salary : 20
'''
# Find  outputs (Home  work)
def    f1(a , b , c):
	return  a + b * c
print(f1(3 , 4 , 5))
print(f1(*[6 , 7 , 8]))
#print(f1([6 , 7 , 8])) ---> f1() missing 2 required positional arguments: 'b' and 'c'
print(f1(*{1 : 2 , 3 : 4 , 5 : 6}))
#print(f1({'c' : 2 , 'b' :  4 , 'a' : 6})) ---> f1() missing 2 required positional arguments: 'b' and 'c'
#print(f1({'c' : 2 , 'b' :  4 , 'a' : 6})) ---> f1() missing 2 required positional arguments: 'b' and 'c'
#print({{'c' : 2 , 'b' :  4 , 'a' : 6}}) --->unhashable type: 'dict'
#print(f1({'c':2,'a':4,'x':6})) --->f1() missing 2 required positional arguments: 'b' and 'c'
'''
OUTPUT:
23
62
16
'''
# Identify  Error (Home  work)
a = [10 , 20 , 15 , 5 , 12]
#print(sorted(reverse = True , a)) --->positional argument follows keyword argument
#print(sorted(a , rev = True)) --->keyword is reverse
#print(25,10.8,'Hyd',separator='\t') ---> There is no keyword 
#print(25,10.8,'Hyd',endofline='\t') ---> there is no keyword argument 
#print(25,sep='\t',10.8,end='\t','Hyd') --->positional argument follows keyword argument
