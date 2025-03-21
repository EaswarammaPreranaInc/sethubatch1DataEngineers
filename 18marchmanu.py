'''
#1) return  statement  demo  program
def  f1():
	print('f1  function') # 2nd executed so print 'F1 function'
	return  25 # returns 25 to the function call
	print('Hello') # Hello is skiped here if it returns next stmts are skipped
# End  of  the  function
print('Begin') # 1st executes so print'Begin'
x =  f1() # function call here
print(x) # Returns 25
print('End') # End

#2) Find outputs  (Home  work)
def   f1(): 2nd f1 () executes so print
	print('Hyd') # Hyd
	print('Sec') # Sec
	print('Cyb')# Cyb
# End  of  the  function
print('Begin') # 1st executed so print 'Begin'
x = f1() # function calls here
print(x) # None by default bcz there is no return object here by default it will takes ' None'
print(type(x))# <class 'NoneType'>
print('End') # End

#3)Find  outputs  (Home  work)
def  f1():# it executes 1st f1 ()
	return  10 , 20 , 30 # Returns (10,20,30)
# End  of  the  function
x = f1() # function call here
print(x) # Returns (10,20,30)
print(type(x)) #< class 'Tuple'>
a , b , c =  f1()
print(a) # 10
print(b)# 20
print(c)# 30
print('for  loop')# for loop
for  k   in   f1(): variable k will take on each value from the iterable returned by f1(), one by one.
	print(k) # 10 <next line> 20<next line> 30

#4)Find  outputs
def    f1(): #it will executes 1st F1()
        return  10 # return  10
        return  20 # skipped
        return  30 # skipped
# End  of  the  function
print('Begin') # Begin
x = f1() # function call here
print(x) # return  10
print('End') # End
return   100 # Error due to return is outside of function 

#5) Find  outputs
#f1() # Error due to ,we have to call  f1 () after the Def but not before 
def   f1():
        print('Hello') # Hello
print(f1()) # None , here f1() by defaults returns None 
print(f1) # Dunder _str method is executed internally here so we get,<function f1 at 0x000002436FA61440>

#6)Find  outputs  (Home  work)

print('Hello') # Hello
def  f1():
        print('f1  function') # fi function
#End  of   function
print('Hi') # Hi
print(f1()) # None , here f1() by defaults returns None
print(f1) # Dunder _str method is executed internally here so we get,<function f1 at 0x0000021B36B21440>
print('Bye') # Bye

#7)Find  outputs

def    f1():
        print('Hyd') # fi() is not called so not performed the operations
        print('Sec')
        print('Cyb')
#End  of  the  function
print('Begin') # Begin
print(type(f1)) # <class 'function'>
print(id(f1)) # 2074333156416
print('End') # End

#8)Find  outputs (Home  work)

def  f1():
	print('No-argument  function')
def  f1(x):
	print('Single  argument  function  : ' , x)
def  f1(x , y):
	print('Two  argument  function : ' , x , y)
def  f1(x , y , z):
	print('Three  argument  function : ' , x , y , z)
f1(10 , 20 , 30) # function call for Three argument function , so prints 10, 20, 30
f1(40 , 50) #  Error due to  f1() missing 1 required positional arguments: 'y' and 'z'
f1(60) # Error due to f1() missing 2 required positional arguments: 'y' and 'z'
f1() # Error due to f1() missing 3 required positional arguments: 'x', 'y', and 'z'

#9) Modify  following  program  such  that  every  function  should  be  executed

def  f1():
	print('No-argument  function')
def  f1(x):
	print('Single  argument  function  : ' , x)
def  f1(x , y):
	print('Two  argument  function : ' , x , y)
def  f1(x , y , z):
	print('Three  argument  function : ' , x , y , z)
f1(10,20,30)
print(f1())
f1(20,30)
print(f1())
f1(10)
print(f1())
f1()
print(f1())



def f1(*args):
    if len(args) == 0:
        print('No-argument function')
    elif len(args) == 1:
        print('Single argument function:', args[0])
    elif len(args) == 2:
        print('Two argument function:', args[0], args[1])
    elif len(args) == 3:
        print('Three argument function:', args[0], args[1], args[2])
    else:
        print('Unsupported number of arguments')

# Function calls
f1(10, 20, 30)  # Three argument function
print(f1())      # No-argument function, and print None (since f1() returns None)
f1(20, 30)       # Two argument function
print(f1())      # No-argument function, print None
f1(10)           # Single argument function
print(f1())      # No-argument function, print None
f1()              # No-argument function
print(f1())      # No-argument function, print None

(or)

def f1():
    print('No-argument function') # None

def f1_single(x):
    print('Single argument function:', x) # 60

def f1_two(x, y):
    print('Two argument function:', x, y) # 40 50

def f1_three(x, y, z):
    print('Three argument function:', x, y, z) # 10 20 30


f1() # f1 () executes but returns 'None'
f1_single(60) # f1 () executes but returns 60
f1_two(40, 50) # # f1 () executes but returns 40 50
f1_three(10, 20, 30) # f1 () executes but returns 10 20 30

# 10) Write   a  function  to  test  a  number  is  prime  (or)  not.
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
	print('Invalid  input')
elif  input  is  prime  number:
	print('Prime  number')
else:
	print('Composite  number')


import math

def prime(n):
    if n <= 1:
        print("Invalid number")
        return  # Exit the function if input is invalid
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            print("Composite number")
            return  # Exit the function if divisor is found
    print("Prime number")  # If no divisor is found, it's prime

try:
    num = int(input("Enter the number: "))
    prime(num)
except ValueError:
    print("Invalid input. Please enter an integer.")


#11)Find  outputs  (Home  work)

def   disp(empno , ename , sal): # position arguments with display ()
        print(F'Emp  Number  :  {empno} \t  Emp Name  :  {ename} \t  Salary  :  {sal}')
# End  of  the  function
disp(25 , 'Rama  Rao' , 10000.0) # Emp  Number  :  25        Emp Name  :  Rama  Rao          Salary  :  10000.0
disp('Sita' , 20000.0 , 35) # Emp  Number  :  Sita      Emp Name  :  20000.0    Salary  :  35

#12)Find  outputs  (Home  work)

def    f1(a , b , c):
          print(F'a  :  {a}    \t  b  :  {b}  \t  c :  {c}')
# End  of  the  function
f1(a = 10 , b = 20 , c = 30)  #  a : 10  <tab>  b : 20 <tab>  c : 30
f1(25 , 10.8 , 'Hyd')   #  a :  25   <tab>  b :  10.8  <tab>  c :  Hyd
f1(b = 40.7 , a = 50.2 , c = 60.5)   #  a :  50.2   <tab>  b :  40.7  <tab>  c :  60.5
f1(c = 'Hyd' , b = 'Sec' , a = 'Cyb') # a :  Cyb  <tab>   b :  Sec  <tab>  c :  Hyd
f1(c = 3 + 4j , a = True , b = None)  # a :  True <tab>   b  :  None <tab> c :  (3+4j)
f1(25 , c = 10.8 , b = 'Hyd') # a  :  25 <tab> b  :  Hyd  <tab>  c :  10.8
#f1(a = 100 , 200 , 300)  #  Error  becoz  pa's  are  after  ka
#f1(True , None , b = 'Hyd')  #  Error  becoz arg  is  passed  for  'b'  twice
#f1(10 , 20 , x = 30)  #  Error  becoz  arg  'x'  does  not  exist  for  f1()  function

#13) Find  outputs (Home  work)

def    disp(empno , ename , sal):
        print(F'Emp  Number : {empno:4}  \t  Emp  Name : {ename:15}  \t  Salary : {sal}')
# End  of  the  function
disp(25 , 'Rama Rao' , 10000.0) # Emp  Number :   25        Emp  Name : Rama Rao            Salary : 10000.0
disp(ename = 'Sita' , sal = 20000.0 , empno = 35) # Emp  Number :   35        Emp  Name : Sita            Salary : 20000.0
x = 'Rama  Rao'
y = 30000.0 # replace with these values
z = 20
disp(x , y , z) # Emp  Number :   Rama Rao        Emp  Name : 30000.0           Salary : 20

#14)Find  outputs (Home  work)

def    f1(a , b , c):
	return  a + b * c
#end  of  the  function
print(f1(3 , 4 , 5)) #23 ---(4*5=20 +3)
print(f1(*[6 , 7 , 8])) # 62 --- (7*8=56+6)
#print(f1([6 , 7 , 8])) # Error due to [6,7,8],  f1() missing 2 required positional arguments: 'b' and 'c'
print(f1(*{1 : 2 , 3 : 4 , 5 : 6})) #16----(3*5=15+1)---unpacking the dict and done operations
print(f1(**{'c' : 2 , 'b' :  4 , 'a' : 6})) # 14---(4*2=8+6)---unpacking the dict and done operations
#print(f1({'c' : 2 , 'b' :  4 , 'a' : 6})) # Error due to ,f1() missing 2 required positional arguments: 'b' and 'c'
print({**{'c' : 2 , 'b' :  4 , 'a' : 6}}) # {'c': 2, 'b': 4, 'a': 6}
#print(f1(**{'c' : 2 , 'a' : 4 , 'x' : 6})) # f1() got an unexpected keyword argument 'x'

#15)Identify  Error (Home  work)

a = [10 , 20 , 15 , 5 , 12]
print(sorted(reverse = True , a)) # positional argument followed by keyword argument
print(sorted(a , rev = True)) # sort() not there  keyword argument 'rev'
print(25 , 10.8 , 'Hyd' , separator = '\t') # print() not there keyword argument 'separator', we have 'sep'.
print(25 , 10.8 , 'Hyd' , endofline = '\t') # print() not there keyword argument 'endofline' , we have 'end'
print(25 ,  sep = '\t' , 10.8 , end = '\t' , 'Hyd') #  positional argument followed by the keyword argument

'''
import math

def prime(n):
    if n <= 1:
        print("Invalid number")
        return  # Exit the function if input is invalid
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            print("Composite number")
            return  # Exit the function if divisor is found
    print("Prime number")  # If no divisor is found, it's prime

try:
    num = int(input("Enter the number: "))
    prime(num)
except ValueError:
    print("Invalid input. Please enter an integer.")


