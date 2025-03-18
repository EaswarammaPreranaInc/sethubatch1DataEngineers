#  return  statement  demo  program
def  f1(): # funtion header
	print('f1  function')
	return  25  
	print('Hello')
# End  of  the  function
print('Begin') # Begin 
x =  f1() 
print(x) # f1 function <next line> 25 but not executed next print stmt becoz after return no stmt execute
print('End') # End

# Find outputs  (Home  work)
def   f1():
	print('Hyd')
	print('Sec')
	print('Cyb')
# End  of  the  function
print('Begin') # Begin
x = f1()
print(x) # Hyd <next line> Sec <next line> Cyb <next line> None
print(type(x)) # <class 'NoneType'>
print('End') # End

#  Gift
# Find  outputs  (Home  work)
def  f1():
	return  10 , 20 , 30
# End  of  the  function
x = f1()
print(x) # (10,20,30)
print(type(x)) # <class 'tuple'>
a , b , c =  f1()
print(a) # 10
print(b) # 20
print(c) # 30
print('for  loop') # for loop
for  k   in   f1():
	print(k) # 10 <next line> 20 <next line> 30
	
# Find  outputs
def    f1():
        return  10
        return  20
        return  30
# End  of  the  function
print('Begin') # Begin
x = f1()
print(x) # 10
print('End') # End
#return   100   # SyntaxError: 'return' outside function 

#  Find  outputs
f1()
def   f1():
        print('Hello')
print(f1()) # Hello <next line> None
print(f1) # Type and address of funtion

# Find  outputs  (Home  work)
print('Hello') # Hello
def  f1():
        print('f1  function')
#End  of   function
print('Hi')# Hi
print(f1()) # f1 funtion <next line> None
print(f1) # Type and address of funtion
print('Bye') # Bye
#  Find  outputs
def    f1():
        print('Hyd')
        print('Sec')
        print('Cyb')
#End  of  the  function
print('Begin') # Begin
print(type(f1)) # <class 'function'>
print(id(f1)) # Address of function f1
print('End') # End

# Find  outputs (Home  work)
def  f1():
	print('No-argument  function')
def  f1(x):
	print('Single  argument  function  : ' , x)
def  f1(x , y):
	print('Two  argument  function : ' , x , y)
def  f1(x , y , z):
	print('Three  argument  function : ' , x , y , z)
f1(10 , 20 , 30) # Three  argument  function : 10,20,30
#f1(40 , 50) # Error: f1() missing 1 required positional argument: 'z' 
#f1(60) # Error: f1() missing 2 required positional arguments: 'y' and 'z'
#f1() # Error: f1() missing 3 required positional arguments: 'x', 'y', and 'z'

# Modify  following  program  such  that  every  function  should  be  executed
def  f1():
	print('No-argument  function')
f1()	
def  f1(x):
	print('Single  argument  function  : ' , x)
f1(1)	
def  f1(x , y):
	print('Two  argument  function : ' , x , y)
f1(20,30)	
def  f1(x , y , z):
	print('Three  argument  function : ' , x , y , z)
f1(20,30,40)	

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
1) prime(25)  --->
    How  many  times  is  for  loop  executed ?  --->

2) prime(11) --->
    How  many  times  is  for  loop  executed ?  --->

3) prime(2) --->
    How  many  times  is  for  loop  executed ?  --->

4) prime(49) --->
    How  many  times  is  for  loop  executed ?  --->
'''

def is_prime(n):
    if n < 2:
        return False  # 0 and 1 are not prime numbers
    
    for i in range(2, int(n ** 0.5) + 1):  # Check divisibility up to sqrt(n)
        if n % i == 0:
            return False  # Found a divisor, so not prime

    return True  # No divisors found, it's a prime number

# Reading input and checking validity
try:
    num = int(input("Enter a number: "))
    
    if num < 0:
        print("Invalid input")
    elif is_prime(num):
        print("Prime number")
    else:
        print("Composite number")

except ValueError:
    print("Invalid input")



# Find  outputs  (Home  work)
def   disp(empno , ename , sal):
        print(F'Emp  Number  :  {empno} \t  Emp Name  :  {ename} \t  Salary  :  {sal}')
# End  of  the  function
disp(25 , 'Rama  Rao' , 10000.0) # Emp  Number  : 25  Emp Name  : 'Rama  Rao'  Salary  : 10000.0
disp('Sita' , 20000.0 , 35) # Emp  Number  : Sita  Emp Name  : 20000.0  Salary  : 35
# Find  outputs  (Home  work)
def    f1(a , b , c):
          print(F'a  :  {a}    \t  b  :  {b}  \t  c :  {c}')
# End  of  the  function
f1(a = 10 , b = 20 , c = 30)  #  a : 10  <tab>  b : 20 <tab>  c : 30
f1(25 , 10.8 , 'Hyd')   #  a :  25   <tab>  b :  10.8  <tab>  c :  Hyd
f1(b = 40.7 , a = 50.2 , c = 60.5)   #  a :  50.2   <tab>  b :  40.7  <tab>  c :  60.5
f1(c = 'Hyd' , b = 'Sec' , a = 'Cyb') # a : Cyb  <tab>  b :  Sec  <tab>   c : Hyd 
f1(c = 3 + 4j , a = True , b = None)  # a : True  <tab>  b : None  <tab>   c : 3+4j 
f1(25 , c = 10.8 , b = 'Hyd') # a : 25   <tab>  b  : Hyd  <tab>   c : 10.8
#f1(a = 100 , 200 , 300)  #  Error  becoz  pa's  are  after  ka
#f1(True , None , b = 'Hyd')  #  Error  becoz arg  is  passed  for  'b'  twice
#f1(10 , 20 , x = 30)  #  Error  becoz  arg  'x'  does  not  exist  for  f1()  function
#f1(10 , 20)  #  Error :  Arg  is  not  passed  for  'c'
# Find  outputs (Home  work)
def    disp(empno , ename , sal):
        print(F'Emp  Number : {empno:4}  \t  Emp  Name : {ename:15}  \t  Salary : {sal}')
# End  of  the  function
disp(25 , 'Rama Rao' , 10000.0) # Emp  Number : 25 <tab> Emp  Name : Rama Rao  <tab> Salary : 10000.0
disp(ename = 'Sita' , sal = 20000.0 , empno = 35) # Emp  Number : 35 <tab> Emp  Name : Rama Rao  <tab> Salary : 10000.0
x = 'Rama  Rao'
y = 30000.0
z = 20
disp(x , y , z) # Emp  Number : Rama  Rao        Emp  Name :   30000.0       Salary : 20
#  Gift
# Find  outputs (Home  work)
def    f1(a , b , c):
	return  a + b * c
#end  of  the  function
print(f1(3 , 4 , 5)) # 23
print(f1(*[6 , 7 , 8])) #  62
#print(f1([6 , 7 , 8])) # Error: f1() missing 2 required positional arguments: 'b' and 'c'
print(f1(*{1 : 2 , 3 : 4 , 5 : 6})) # 16
print(f1(**{'c' : 2 , 'b' :  4 , 'a' : 6})) # 14
#print(f1({'c' : 2 , 'b' :  4 , 'a' : 6})) # Error: f1() missing 2 required positional arguments: 'b' and 'c'
print({**{'c' : 2 , 'b' :  4 , 'a' : 6}}) # {'c': 2, 'b': 4, 'a': 6}
#print(f1(**{'c' : 2 , 'a' : 4 , 'x' : 6})) # Error: f1() got an unexpected keyword argument 'x'
# Identify  Error (Home  work)
a = [10 , 20 , 15 , 5 , 12]
#print(sorted(reverse = True , a))
#print(sorted(a , rev = True)) # Error: sort() got an unexpected keyword argument 'rev'
#print(25 , 10.8 , 'Hyd' , separator = '\t') # Error: print() got an unexpected keyword argument 'separator'
print(25 , 10.8 , 'Hyd' , endofline = '\t') # Error: print() got an unexpected keyword argument 'endofline'
#print(25 ,  sep = '\t' , 10.8 , end = '\t' , 'Hyd')