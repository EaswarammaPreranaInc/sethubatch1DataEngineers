#1  return  statement  demo  program
def  f1():
	print('f1  function')
	return  25
	print('Hello')
# End  of  the  function
print('Begin')
x =  f1()
print(x)
print('End')

Output:
Begin
f1  function
25
End

#2 Find outputs  (Home  work)
def   f1():
	print('Hyd')
	print('Sec')
	print('Cyb')
# End  of  the  function
print('Begin')
x = f1()
print(x)
print(type(x))
print('End')

Output:
Begin
Hyd
Sec
Cyb
None
<class 'NoneType'>
End

#3 Find  outputs  (Home  work) 
def  f1():
	return  10 , 20 , 30
# End  of  the  function
x = f1()
print(x)
print(type(x))
a , b , c =  f1()
print(a)
print(b)
print(c)
print('for  loop')
for  k   in   f1():
	print(k)

Output:
(10, 20, 30)
<class 'tuple'>
10
20
30
for  loop
10
20
30

#4 Find  outputs
def    f1():
        return  10
        return  20
        return  30
# End  of  the  function
print('Begin')
x = f1()
print(x)
print('End')
#return   100

Output:
Begin
10
End

#5 Find  outputs
#f1()
def   f1():
        print('Hello')
print(f1())
print(f1)

Output:
Hello
None
<function f1 at 0x0000016F556E3E20>

#6  Find  outputs  (Home  work)
print('Hello')
def  f1():
        print('f1  function')
#End  of   function
print('Hi')
print(f1())
print(f1)
print('Bye')

Output:
Hello
Hi
f1  function
None
<function f1 at 0x000001D13FA83E20>
Bye

#7 Find  outputs
def    f1():
        print('Hyd')
        print('Sec')
        print('Cyb')
#End  of  the  function
print('Begin')
print(type(f1))
print(id(f1))
print('End')

Output:
Begin
<class 'function'>
2036306492960
End

#8 Find  outputs (Home  work)
def  f1():
	print('No-argument  function')
def  f1(x):
	print('Single  argument  function  : ' , x)
def  f1(x , y):
	print('Two  argument  function : ' , x , y)
def  f1(x , y , z):
	print('Three  argument  function : ' , x , y , z)
f1(10 , 20 , 30)
#f1(40 , 50)
#f1(60)
#f1()

Output:
Three  argument  function :  10 20 30

#9 Modify  following  program  such  that  every  function  should  be  executed
def  f1():
	print('No-argument  function')
f1()
def  f1(x):
	print('Single  argument  function  : ' , x)
f1(10)
def  f1(x , y):
	print('Two  argument  function : ' , x , y)
f1(10 , 20)
def  f1(x , y , z):
	print('Three  argument  function : ' , x , y , z)
f1(10 , 20 , 30)

Output:
No-argument  function
Single  argument  function  :  10
Two  argument  function :  10 20
Three  argument  function :  10 20 30

#10 
'''Write   a  function  to  test  a  number  is  prime  (or)  not.
1) What  is  a  prime  number ?  --->  A  number  without  divisors  except  1  and  itself
2) Let  input  be  25
    What  is  the  range  of  divisors ? --->  i =   2 , 3 , 4 , 5 , 6 , ..... 12
3) Let  input   be  11
    What  is   the  range  of  divisors ? --->  i =  2 , 3 , 4 , 5
4) What  action  to  be  made  if  'i'  is  not  a  divisor  of  input  number ?  ---> Move  to  the  next  element  of  range  object
5) What  action  to  be  made  if  'i'  is  a  divisor  of  input  number ?  ---> return   False
6) What  action  to  be  made  if  there  are  no  divisiors  to  input  number  ? ---> return  True  outside  the  loop
def   prime(n):
	return  true   when  'n'  is  prime  number  and  False  otherwise
1) prime(25)  --->
    How  many  times  is  for  loop  executed ?  --->
2) prime(11) --->
    How  many  times  is  for  loop  executed ?  --->
3) prime(2) --->
    How  many  times  is  for  loop  executed ?  --->
4) prime(49) --->
    How  many  times  is  for  loop  executed ?  --->
How  to  read  a  number
if   input  is  invalid:
	print('Invalid  input')1
elif  input  is  prime  number:
	print('Prime  number')
else:
	print('Composite  number')'''

def prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    for i in range(2, int(n**0.5) + 1): 
        if n % i == 0:
            return False  
    return True  

n = int(input('Enter a number: '))
if n==1:
    print('Neither Prime nor Composite')
elif n<1:
	print('Input must be positive')
elif prime(n):
    print('Prime Number')
else:
	print('Composite Number')

Output:
Enter a number: 23
Prime Number

#11 Find  outputs  (Home  work)
def   disp(empno , ename , sal):
        print(F'Emp  Number  :  {empno} \t  Emp Name  :  {ename} \t  Salary  :  {sal}')
# End  of  the  function
disp(25 , 'Rama  Rao' , 10000.0)
disp('Sita' , 20000.0 , 35)

Output:
Emp  Number  :  25        Emp Name  :  Rama  Rao          Salary  :  10000.0
Emp  Number  :  Sita      Emp Name  :  20000.0    Salary  :  35

#12 Find  outputs  (Home  work)
def    f1(a , b , c):
          print(F'a  :  {a}    \t  b  :  {b}  \t  c :  {c}')
# End  of  the  function
f1(a = 10 , b = 20 , c = 30)  #  a : 10  <tab>  b : 20 <tab>  c : 30
f1(25 , 10.8 , 'Hyd')   #  a :  25   <tab>  b :  10.8  <tab>  c :  Hyd
f1(b = 40.7 , a = 50.2 , c = 60.5)   #  a :  50.2   <tab>  b :  40.7  <tab>  c :  60.5
f1(c = 'Hyd' , b = 'Sec' , a = 'Cyb')
f1(c = 3 + 4j , a = True , b = None)
f1(25 , c = 10.8 , b = 'Hyd')
#f1(a = 100 , 200 , 300)  #  Error  becoz  pa's  are  after  ka
#f1(True , None , b = 'Hyd')  #  Error  becoz arg  is  passed  for  'b'  twice
#f1(10 , 20 , x = 30)  #  Error  becoz  arg  'x'  does  not  exist  for  f1()  function
#f1(10 , 20)  #  Error :  Arg  is  not  passed  for  'c'

Output:
a  :  10          b  :  20        c :  30
a  :  25          b  :  10.8      c :  Hyd
a  :  50.2        b  :  40.7      c :  60.5
a  :  Cyb         b  :  Sec       c :  Hyd
a  :  True        b  :  None      c :  (3+4j)
a  :  25          b  :  Hyd       c :  10.8

#13 Find  outputs (Home  work)
def    disp(empno , ename , sal):
        print(F'Emp  Number : {empno:4}  \t  Emp  Name : {ename:15}  \t  Salary : {sal}')
# End  of  the  function
disp(25 , 'Rama Rao' , 10000.0)
disp(ename = 'Sita' , sal = 20000.0 , empno = 35)
x = 'Rama  Rao'
y = 30000.0
z = 20
disp(x , y , z)

Output:
Emp  Number :   25        Emp  Name : Rama Rao            Salary : 10000.0
Emp  Number :   35        Emp  Name : Sita                Salary : 20000.0
Emp  Number : Rama  Rao           Emp  Name :         30000.0     Salary : 20

#14 Find  outputs (Home  work)
def    f1(a , b , c):
	return  a + b * c
#end  of  the  function
print(f1(3 , 4 , 5))
print(f1(*[6 , 7 , 8]))
#print(f1([6 , 7 , 8]))
print(f1(*{1 : 2 , 3 : 4 , 5 : 6}))
print(f1(**{'c' : 2 , 'b' :  4 , 'a' : 6}))
#print(f1({'c' : 2 , 'b' :  4 , 'a' : 6}))
print({**{'c' : 2 , 'b' :  4 , 'a' : 6}})
#print(f1(**{'c' : 2 , 'a' : 4 , 'x' : 6}))

Output:
23
62
16
14
{'c': 2, 'b': 4, 'a': 6}

#15 Identify  Error (Home  work)
a = [10 , 20 , 15 , 5 , 12]
#print(sorted(reverse = True , a))				       SyntaxError: positional argument follows keyword argument
#print(sorted(a , rev = True))                         TypeError: 'rev' is an invalid keyword argument for sort()
#print(25 , 10.8 , 'Hyd' , separator = '\t')           TypeError: 'separator' is an invalid keyword argument for print()
#print(25 , 10.8 , 'Hyd' , endofline = '\t')           TypeError: 'endofline' is an invalid keyword argument for print()
#print(25 ,  sep = '\t' , 10.8 , end = '\t' , 'Hyd')   SyntaxError: positional argument follows keyword argument