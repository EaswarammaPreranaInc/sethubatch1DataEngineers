#Ex-1
#  return  statement  demo  program
def  f1():
	print('f1  function')
	return  25
	print('Hello')
# End  of  the  function
print('Begin')    # Begin <nl> f1 function
x =  f1() # return 25
print(x) # 25
print('End') # End
print()

#Ex-2
# Find outputs  (Home  work)
def   f1():
	print('Hyd')
	print('Sec')
	print('Cyb')
# End  of  the  function
print('Begin') # Begin <nl> 'Hyd' <nl> 'Sec' <nl> 'Cyb'
x = f1() # Return None
print(x) # None
print(type(x)) # class NoneType
print('End') # 'End'
print()

#Ex-3
#  Gift
# Find  outputs  (Home  work)
def  f1():
	return  10 , 20 , 30
# End  of  the  function
x = f1()  # tuple (10,20,30)
print(x) # (10,20,30)
print(type(x)) # class tuple
a , b , c =  f1() # a=10,b=20,c=30
print(a) # 10
print(b) # 20
print(c) # 30
print('for  loop')
for  k   in  f1():
	print(k)      # 10 <nl> 20 <nl> 30
print()

#Ex-4
# Find  outputs
def    f1():
        return  10
        return  20
        return  30
# End  of  the  function
print('Begin') # Begin
x = f1() # return 10 remaining return statements are ignored
print(x) # 10
print('End') # End
#return 100 # Error  because return always last line of function
print()


#Ex-5
#  Find  outputs
#f1() # Error because before function call must be defined function
def   f1():
        print('Hello')
print(f1()) # Hello <nl> None
print(f1) # function name and random address
print()

#Ex-6
# Find  outputs  (Home  work)
print('Hello')  # Hello
def  f1():
        print('f1  function')
#End  of   function
print('Hi') # Hi
print(f1()) # f1 function <nl> None
print(f1)  #  function name and random address
print('Bye') # 'Bye'
print()

#Ex-7
#  Find  outputs
def    f1():
        print('Hyd')
        print('Sec')
        print('Cyb')
#End  of  the  function
print('Begin') # Begin
print(type(f1)) # class function
print(id(f1)) # random address
print('End') # End
print()

#Ex-8:-
# Find  outputs (Home  work)
def  f1():
	print('No-argument  function')
def  f1(x):
	print('Single  argument  function  : ' , x)
def  f1(x , y):
	print('Two  argument  function : ' , x , y)
def  f1(x , y , z):
	print('Three  argument  function : ' , x , y , z)
f1(10 , 20 , 30) # Three argument function: ,10  20 30
f1(40 ,50) # Two  argument  function : 40 50
f1(60) # Single  argument  function  : 60
f1() # No-argument  function
print()

Ex-9
# Modify  following  program  such  that  every  function  should  be  executed
def  f1():
	print('No-argument  function')
f1() # No-argument  function
def  f1(x):
	print('Single  argument  function  : ' , x)
f1(10) # Single  argument  function  : 10
def  f1(x , y):
	print('Two  argument  function : ' , x , y)
f1(1,2) # Two  argument  function : 1  2
def  f1(x , y , z):
	print('Three  argument  function :',x,y,z)
f1(1,2,3) # Three  argument  function :1  2  3
print()


#Ex-10
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

1) prime(25)  --->
    How  many  times  is  for  loop  executed ?  --->

2) prime(11) --->
    How  many  times  is  for  loop  executed ?  --->

3) prime(2) --->
    How  many  times  is  for  loop  executed ?  --->

4) prime(49) --->
    How  many  times  is  for  loop  executed ?  --->
'''

def isPrime(x):
    b = True
    for i in range(2,(x // 2)+1):
        if x % i == 0:
            b = False
            break
    return b
a = eval(input('Enter a number : '))
if a <=1:
    print('1 is not aprime number')
elif isPrime(a):
    print('Prime  number')
else:
    print('Composite number')
print()

# Ex-11:
# Find  outputs  (Home  work)
def   disp(empno , ename , sal):
    print(F'Emp  Number  :  {empno} \t  Emp Name  :  {ename} \t  Salary  :  {sal}')
# End  of  the  function
disp(25 , 'Rama  Rao' , 10000.0)  # Emp  Number  :  25 	  Emp Name  :  Rama  Rao 	  Salary  :  10000.0
disp('Sita',20000.0,35) # Emp  Number  :  Sita 	  Emp Name  :  20000.0 	  Salary  :  35
print()

#Ex-12:-
# Find  outputs  (Home  work)
def    f1(a , b , c):
          print(F'a  :  {a}    \t  b  :  {b}  \t  c :  {c}')
# End  of  the  function
f1(a = 10 , b = 20 , c = 30)  #  a : 10  <tab>  b : 20 <tab>  c : 30
f1(25 , 10.8 , 'Hyd')   #  a :  25   <tab>  b :  10.8  <tab>  c :  Hyd
f1(b = 40.7 , a = 50.2 , c = 60.5)   #  a :  50.2   <tab>  b :  40.7  <tab>  c :  60.5
f1(c = 'Hyd' , b = 'Sec' , a = 'Cyb') # a : 'Cyb' <tab> b : Sec <tab> c : Hyd
f1(c = 3 + 4j , a = True , b = None) # a  :  True <tab> b  :  None <tab> c :  (3+4j)
f1(25 , c = 10.8 , b = 'Hyd') # a :  25   <tab>  b : Hyd   <tab>  c :  10.8
#f1(a = 100 , 200 , 300)  #  Error  becoz  pa's  are  after  ka
#f1(True , None , b = 'Hyd')  #  Error  becoz arg  is  passed  for  'b'  twice
#f1(10 , 20 , x = 30)  #  Error  becoz  arg  'x'  does  not  exist  for  f1()  function
#f1(10 , 20)  #  Error :  Arg  is  not  passed for 'c'
print()


#Ex-13
# Find  outputs (Home  work)
def    disp(empno , ename , sal):
        print(F'Emp  Number : {empno:4}  \t  Emp  Name : {ename:15}  \t  Salary : {sal}')
# End  of  the  function
disp(25 , 'Rama Rao' , 10000.0) # Emp  Number :   25 <tab> Emp  Name : Rama Rao <tab> Salary : 10000.0
disp(ename = 'Sita' , sal = 20000.0 , empno = 35) # Emp  Number :   35 <tab> Emp  Name : Sita <tab> Salary : 20000.0
x = 'Rama  Rao'
y = 30000.0
z = 20
disp(x,y,z) # Emp  Number : Rama  Rao <tap> Emp  Name :  30000.0 <tab> Salary : 20
print()




#Ex-14
#  Gift
# Find  outputs (Home  work)
def    f1(a , b , c):
	return  a + b * c
#end  of  the  function
print(f1(3 , 4 , 5)) #23
print(f1(*[6 , 7 , 8])) # unpacking list of elements a = 3, b =7 , c = 8 return vlaue is 62
# print(f1([6 , 7 , 8])) # f1 function accepting 3 values but only one  positional arguments missing 2
print(f1(*{1 : 2 , 3 : 4 , 5 : 6})) # unpacking list of keys f1(1,3,5) return value 16
#print(f1({'c' : 2 , 'b' :  4 , 'a' : 6})) # f1 function accepting 3 values but only one  positional arguments missing 2
#print(f1({'c' : 2 , 'b' :  4 , 'a' : 6})) #f1 function accepting 3 values but only one  positional arguments missing 2
#print({{'c' : 2 , 'b' :  4 , 'a' : 6}})# Error because nested dict
#print(f1({'c' : 2 , 'a' :4,'x':6})) #f1 function accepting 3 values but only one  positional arguments missing 2
print()

# Ex-15
# Identify  Error (Home  work)
a = [10 , 20 , 15 , 5 , 12]
#print(sorted(reverse = True , a)) #keyword argument 'reverse' before list a
print(sorted(a , rev = True)) # unexpected keyword argument 'rev'
#print(25 , 10.8 , 'Hyd' , separator = '\t') # there is no  keyword argument separator
#print(25 , 10.8 , 'Hyd' , endofline = '\t') #  there is no  keyword argument endofline
#print(25 ,  sep = '\t' , 10.8 , end='\t','Hyd') # before use positional arguments first after use keyword argument

