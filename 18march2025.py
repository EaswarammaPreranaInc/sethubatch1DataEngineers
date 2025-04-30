#  return  statement  demo  program
'''
def  f1():
	print('f1  function')
	return  25
	print('Hello')
# End  of  the  function
print('Begin')# Begin
x =  f1() #function is assinged to referance x
print(x) # f1 function
print('End') # End
'''

# Find outputs  (Home  work)
'''
def   f1():
	print('Hyd')
	print('Sec')
	print('Cyb')
# End  of  the  function
print('Begin')# Begin
x = f1()
print(x) # Hyd
         # sec
		 # cyb
		 # None
print(type(x)) # <class 'None'>
print('End') # End
'''


# Find  outputs  (Home  work)
'''
def  f1():
	return  10 , 20 , 30
# End  of  the  function
x = f1()
print(x)# (10,20,30)
print(type(x))# <class 'tuple'>
a , b , c =  f1()
print(a)# 10 
print(b)# 20
print(c)# 30
print('for  loop')# for loop
for  k   in   f1():
	print(k)
# 10
# 20
# 30
'''
	

# Find  outputs
'''
def    f1():
        return  10
        return  20
        return  30
# End  of  the  function
print('Begin')# Begin
x = f1()
print(x)# 10
print('End')# End
# return  100# error
'''

#  Find  outputs
'''
f1()# f1() is not defined error
def   f1():
        print('Hello')
print(f1())# hello,none
print(f1)# <class 'function'> at address of the f1
'''

# Find  outputs  (Home  work)
'''
print('Hello')
def  f1():
        print('f1  function')
#End  of   function
print('Hi')# Hi
print(f1())# f1 function 
           # None
print(f1)# <class 'function'> at address of the f1
print('Bye')# Bye
'''

#  Find  outputs
'''
def    f1():
        print('Hyd')
        print('Sec')
        print('Cyb')
#End  of  the  function
print('Begin')# Begin
print(type(f1))# <class 'function'>
print(id(f1))# decimal address of f1
print('End')# end
'''

# Find  outputs (Home  work)
'''
def  f1():
	print('No-argument  function')
def  f1(x):
	print('Single  argument  function  : ' , x)
def  f1(x , y):
	print('Two  argument  function : ' , x , y)
def  f1(x , y , z):
	print('Three  argument  function : ' , x , y , z)
f1(10 , 20 , 30)# Three arguments function : 10 20 30
#f1(40 , 50)# error
#f1(60)# error
#f1()# Three arguments function :,x,y,z
'''

# Modify  following  program  such  that  every  function  should  be  executed
'''
def  f1():
	print('No-argument  function')
f1()
def  f1(x):
	print('Single  argument  function  : ' , x)
f1(10)
def  f1(x , y):
	print('Two  argument  function : ' , x , y)
f1(10,20)
def  f1(x , y , z):
	print('Three  argument  function : ' , x , y , z)
f1(3,3,3)
'''


# Write   a  function  to  test  a  number  is  prime  (or)  not.
'''
1) What  is  a  prime  number ?  --->  A  number  without  divisors  except  1  and  itself

2) Let  input  be  25
    What  is  the  range  of  divisors ? --->  i =   2 , 3 , 4 , 5 , 6 , ..... 12

3) Let  input   be  11
    What  is   the  range  of  divisors ? --->  i =  2 , 3 , 4 , 5

4) What  action  to  be  made  if  'i'  is  not  a  divisor  of  input  number ?  ---> Move  to  the  next  element  of  range  object

5) What  action  to  be  made  if  'i'  is  a  divisor  of  input  number ?  ---> return   False

6) What  action  to  be  made  if  there  are  no  divisiors  to  input  number  ? ---> return  True  outside  the  loop


def   prime(n):
	c=0
	for i in range(2,n):
		if n%i==0:
			c=1
		if c==1:
			return('False')
		else:
			return('True')
print(prime(int(input("enter the integer number : "))))
'''

# Find  outputs  (Home  work)
'''
def   disp(empno , ename , sal):
        print(F'Emp  Number  :  {empno} \t  Emp Name  :  {ename} \t  Salary  :  {sal}')
# End  of  the  function
disp(25 , 'Rama  Rao' , 10000.0)# emp number :25    emp name : 'rama rao'   salary : 10000.0
disp('Sita' , 20000.0 , 35)     # emp number : 'sita'    emp name: 20000.0   salary : 35
'''

# Find  outputs  (Home  work)
'''
def    f1(a , b , c):
        print(F'a  :  {a}    \t  b  :  {b}  \t  c :  {c}')
# End  of  the  function
f1(a = 10 , b = 20 , c = 30)  #  a : 10  <tab>  b : 20 <tab>  c : 30
f1(25 , 10.8 , 'Hyd')   #  a :  25   <tab>  b :  10.8  <tab>  c :  Hyd
f1(b = 40.7 , a = 50.2 , c = 60.5)   #  a :  50.2   <tab>  b :  40.7  <tab>  c :  60.5
f1(c = 'Hyd' , b = 'Sec' , a = 'Cyb')# a:cyb    b: sec    c: hyd
f1(c = 3 + 4j , a = True , b = None)# a: true  b: None    c: 3+4j
f1(25 , c = 10.8 , b = 'Hyd')# a: 25   b: hyd   c: 10.8 
#f1(a = 100 , 200 , 300)  #  Error  becoz  pa's  are  after  ka
#f1(True , None , b = 'Hyd')  #  Error  becoz arg  is  passed  for  'b'  twice
#f1(10 , 20 , x = 30)  #  Error  becoz  arg  'x'  does  not  exist  for  f1()  function
#f1(10 , 20)  #  Error :  Arg  is  not  passed  for  'c'
'''

# Find  outputs (Home  work)
'''
def    disp(empno , ename , sal):
        print(F'Emp  Number : {empno:4}  \t  Emp  Name : {ename:15}  \t  Salary : {sal}')
# End  of  the  function
disp(25 , 'Rama Rao' , 10000.0)# emp number : 25   b: rama rao   salary : 10000.0
disp(ename = 'Sita' , sal = 20000.0 , empno = 35)# emp number : 35   emp name : sita:  salary : 20000.0
x = 'Rama  Rao'
y = 30000.0
z = 20
disp(x , y , z)# emp number : rama rao     emp name : 300000.0     salary :20
'''

# Find  outputs (Home  work)
'''
def    f1(a , b , c):
	return  a + b * c
#end  of  the  function
print(f1(3 , 4 , 5))# 23
print(f1(*[6 , 7 , 8]))# 62
print(f1([6 , 7 , 8]))# error
print(f1(*{1 : 2 , 3 : 4 , 5 : 6}))# 16
print(f1(**{'c' : 2 , 'b' :  4 , 'a' : 6}))# 14
print(f1({'c' : 2 , 'b' :  4 , 'a' : 6}))# error
print({**{'c' : 2 , 'b' :  4 , 'a' : 6}})# {c:2,b:4,a:6}
print(f1(**{'c' : 2 , 'a' : 4 , 'x' : 6}))# error
'''

# Identify  Error (Home  work)
'''
a = [10 , 20 , 15 , 5 , 12]
print(sorted(reverse = True , a))# error
print(sorted(a , rev = True))# error their is no rev function in python we have only reverse function
print(25 , 10.8 , 'Hyd' , separator = '\t')# error
print(25 , 10.8 , 'Hyd' , endofline = '\t')#   error  
print(25 ,  sep = '\t' , 10.8 , end = '\t' , 'Hyd')# error
'''