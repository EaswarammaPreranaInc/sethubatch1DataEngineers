#1
##  return  statement  demo  program
def  f1():
	print('f1  function')
	return  25
	print('Hello')
# End  of  the  function
print('Begin')#Begain
x =  f1()
print(x)#f1 function,25
print('End')#end

#2
# Find outputs  (Home  work)
def   f1():
	print('Hyd')
	print('Sec')
	print('Cyb')
	return
# End  of  the  function
print('Begin')#begin
x = f1()
print(x)#hyd,sec,cyd
print(type(x))#<class 'NoneType'>
print('End')#end

#3
#  Gift
# Find  outputs  (Home  work)
def  f1():
	return  10 , 20 , 30
# End  of  the  function
x = f1()
print(x)#(10,20,30)
print(type(x))#<class 'tuple'>
a , b , c =  f1()
print(a)#10
print(b)#20
print(c)#30
print('for  loop')#for loop
for  k   in   f1():
	print(k)

"""
10
20
30
"""

#4
# Find  outputs
def    f1():
        return  10
        return  20
        return  30
# End  of  the  function
print('Begin')#begin
x = f1()
print(x)#10
print('End')#Endd

#5
#  Find  outputs
#f1()#error
def   f1():
        print('Hello')
print(f1())#hello
print(f1)#None,<function f1 at >

#6
# Find  outputs  (Home  work)
print('Hello')#hello
def  f1():
        print('f1  function')
#End  of   function
print('Hi')#hi
print(f1())#f1  function,None
print(f1)#
print('Bye')#Bye


#7
#  Find  outputs
def    f1():
        print('Hyd')
        print('Sec')
        print('Cyb')
#End  of  the  function
print('Begin')#begin
print(type(f1))#<class 'function'>
print(id(f1))#4303581920
print('End')#End

#8
# Find  outputs (Home  work)
def  f1():
	print('No-argument  function')
def  f1(x):
	print('Single  argument  function  : ' , x)
def  f1(x , y):
	print('Two  argument  function : ' , x , y)
def  f1(x , y , z):
	print('Three  argument  function : ' , x , y , z)
f1(10,20,30)#Three  argument  function :  10 20 30
#f1(40,50)error
#f1(60)#error
#f1()#error

#9
# Modify  following  program  such  that  every  function  should  be  executed
def  f1():
	print('No-argument  function')
	return 1
print(f1())
def  f1(x):
	print('Single  argument  function  : ' , x)
	return 1
print(f1(1))
def  f1(x , y):
	print('Two  argument  function : ' , x , y)
	return 1
print(f1(1,2))
def  f1(x , y , z):
	print('Three  argument  function : ' , x , y , z)
	return 1
print(f1(1,2,3))


#10
'''
Write   a  function  to  test  a  number  is  prime  (or)  not.
1) What  is  a  prime  number ?  --->  A  number  without  divisors  except  1  and  itself

2) Let  input  be  25
    What  is  the  range  of  divisors ? --->  i =   2 , 3 , 4 , 5 , 6 , ..... 12

3) Let  input   be  11
    What  is   the  range  of  divisors ? --->  i =  2 , 3 , 4 , 5

4) What  action  to  be  made  if  'i'  is  not  a  divisor  of  input  number ?  ---> Move  to  the  next  element  of  range  object

5) What  action  to  be  made  if  'i'  is  a  divisor  of  input  number ?  ---> return   False

6) What  action  to  be  made  if  there  are  no  divisiors  to  input  number  ? ---> return  True  outside  the  loop
'''
'''
def   prime(n):
	count = 0
	if n<2:
		return False
	elif n==2:
		return True
	else:
		for i in range(2,int(n**0.5)+1):
			count+=1
			print(count)
			if n%i == 0:
				return False
	return True
	#return  true   when  'n'  is  prime  number  and  False  otherwise

a = int(input('Enter a number : '))#How  to  read  a  number
if   a<0:#input  is  invalid:
	print('Invalid  input')
elif  prime(a):#input  is  prime  number:
	print('Prime  number')
else:
	print('Composite  number')

1) prime(25)  ---> Composite  number
    How  many  times  is  for  loop  executed ?  --->4

2) prime(11) --->Prime number
    How  many  times  is  for  loop  executed ?  --->2

3) prime(2) --->Prime number 
    How  many  times  is  for  loop  executed ?  --->0

4) prime(49) --->Composite number
    How  many  times  is  for  loop  executed ?  --->6
'''

def prime(n):
	for i in range(2,n//2+1):
		if n%i==0:
			return False
	return True

a = int(input('Enter a number : '))#How  to  read  a  number
if   a<0:#input  is  invalid:
	print('Invalid  input')
elif  prime(a):#input  is  prime  number:
	print('Prime  number')
else:
	print('Composite  number')


#11
# Find  outputs  (Home  work)
def   disp(empno , ename , sal):
        print(F'Emp  Number  :  {empno} \t  Emp Name  :  {ename} \t  Salary  :  {sal}')
# End  of  the  function
disp(25 , 'Rama  Rao' , 10000.0)#Emp  Number  :  25 	  Emp Name  :  Rama  Rao 	  Salary  :  10000.0
disp('Sita' , 20000.0 , 35)#Emp  Number  :  Sita 	  Emp Name  :  20000.0 	  Salary  :  35

#12
# Find  outputs  (Home  work)
def    f1(a , b , c):
          print(F'a  :  {a}    \t  b  :  {b}  \t  c :  {c}')
# End  of  the  function
f1(a = 10 , b = 20 , c = 30)  #  a : 10  <tab>  b : 20 <tab>  c : 30
f1(25 , 10.8 , 'Hyd')   #  a :  25   <tab>  b :  10.8  <tab>  c :  Hyd
f1(b = 40.7 , a = 50.2 , c = 60.5)   #  a :  50.2   <tab>  b :  40.7  <tab>  c :  60.5
f1(c = 'Hyd' , b = 'Sec' , a = 'Cyb')#a  :  Cyb    	  b  :  Sec  	  c :  Hyd
f1(c = 3 + 4j , a = True , b = None)#a  :  True    	  b  :  None  	  c :  (3+4j)
f1(25 , c = 10.8 , b = 'Hyd')#a  :  25    	  b  :  Hyd  	  c :  10.8
#f1(a = 100 , 200 , 300)  #  Error  becoz  pa's  are  after  ka
#f1(True , None , b = 'Hyd')  #  Error  becoz arg  is  passed  for  'b'  twice
#f1(10 , 20 , x = 30)  #  Error  becoz  arg  'x'  does  not  exist  for  f1()  function
#f1(10 , 20)  #  Error :  Arg  is  not  passed  for  'c'

#13
# Find  outputs (Home  work)
def    disp(empno , ename , sal):
        print(F'Emp  Number : {empno:4}  \t  Emp  Name : {ename:15}  \t  Salary : {sal}')
# End  of  the  function
disp(25 , 'Rama Rao' , 10000.0)#Emp  Number :   25  	  Emp  Name : Rama Rao         	  Salary : 10000.0
disp(ename = 'Sita' , sal = 20000.0 , empno = 35)#Emp  Number :   35  	  Emp  Name : Sita             	  Salary : 20000.0
x = 'Rama  Rao'
y = 30000.0
z = 20
disp(x , y , z)#Emp  Number : Rama  Rao  	  Emp  Name :         30000.0  	  Salary : 20

#14
#  Gift
# Find  outputs (Home  work)
def    f1(a , b , c):
	return  a + b * c
#end  of  the  function
print(f1(3 , 4 , 5))#23
print(f1(*[6 , 7 , 8]))#62
#print(f1([6 , 7 , 8]))#error
print(f1(*{1 : 2 , 3 : 4 , 5 : 6}))#16
print(f1(**{'c' : 2 , 'b' :  4 , 'a' : 6}))#14
#print(f1({'c' : 2 , 'b' :  4 , 'a' : 6}))#error
#print({**{'c' : 2 , 'b' :  4 , 'a' : 6}})#error
#print(f1(**{'c' : 2 , 'a' : 4 , 'x' : 6}))#error


#15
# Identify  Error (Home  work)
a = [10 , 20 , 15 , 5 , 12]
#print(sorted(reverse = True , a))#
#print(sorted(a , rev = True))
#print(25 , 10.8 , 'Hyd' , separator = '\t')#error
#print(25 , 10.8 , 'Hyd' , endofline = '\t')#error
#print(25 ,  sep = '\t' , 10.8 , end = '\t' , 'Hyd')#error

