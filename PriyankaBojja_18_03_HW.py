'''
Q1 # return  statement  demo  program
def  f1():
	print('f1  function')
	return  25
	print('Hello')
# End  of  the  function
print('Begin')
x =  f1()
print(x)
print('End')

OP-
Begin
f1  function
25
End

Q2 #Find outputs  (Home  work)
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

OP-
Begin
Hyd
Sec 
Cyb
None
<class 'NoneType'>
End

Q3 #Find  outputs  (Home  work)
def  f1():
	return  10 , 20 , 30
# End  of  the  function
x = f1()
print(x)  #(10,20,30)
print(type(x))  #<class 'tuple'>
a , b , c =  f1()
print(a)  #10
print(b)  #20
print(c)  #30
print('for  loop')  #for loop
for  k   in   f1():
	print(k)     #10 \n 20 \n 30

Q4 #Find  outputs
def    f1():
        return  10
        return  20
        return  30

# End  of  the  function
print('Begin')  #Begin
x = f1()
print(x)        # 10
print('End')    #End
return   100    #error - return statement must be inside function

#Q5 #Find  outputs
#f1()  #error - f1() function is not defined
def   f1():
        print('Hello')
print(f1())    #Hello \n None
print(f1)      #<function f1 at 0x0000026899CE1440>

Q6#Find  outputs  (Home  work)
print('Hello')  #Hello
def  f1():
        print('f1  function')
#End  of   function
print('Hi')  #Hi
print(f1())  #f1 function \n None
print(f1)    #<function f1 at 0x0000021255191440>
print('Bye') #Bye

Q7 #Find  outputs
def    f1():
        print('Hyd')
        print('Sec')
        print('Cyb')
#End  of  the  function
print('Begin')   #Begin
print(type(f1))  #<class 'function'>
print(id(f1))    #2035009786944
print('End')     #End

Q8 #Find  outputs (Home  work)
def  f1():
	print('No-argument  function')
def  f1(x):
	print('Single  argument  function  : ' , x)
def  f1(x , y):
	print('Two  argument  function : ' , x , y)
def  f1(x , y , z):
	print('Three  argument  function : ' , x , y , z)
f1(10 , 20 , 30)  # Three  argument  function : 10  20  30
#f1(40 , 50)   #error because of only two arguments - 3 is needed
#f1(60)        #  error because of only one arguments - 3 is needed
#f1()           #error because of no arguments - 3 is needed

Q9 #Modify  following  program  such  that  every  function  should  be  executed
def  f1():
	print('No-argument  function')
f1()
def  f1(x):
	print('Single  argument  function  : ' , x)
f1(10)
def  f1(x , y):
	print('Two  argument  function : ' , x , y)
f1(20,30)
def  f1(x , y , z):
	print('Three  argument  function : ' , x , y , z)
f1(40,50,60)

OP-
No-argument  function
Single  argument  function  :  10
Two  argument  function :  20 30
Three  argument  function :  40 50 60


#Q10 Write   a  function  to  test  a  number  is  prime  (or)  not.
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

def prime(n):
		if n<0:
			return 'Invalid Input'
		for x in range(2,(n//2)+1):
			if n%x==0:
				return 'Composite Number'
		else:
			return 'Prime Number'
num=int(float(input('Enter a number: ')))
print(prime(num))

OP-
Enter a number: 2
Prime Number

Enter a number: 65.0
Composite Number

Enter a number: -5
Invalid Input


Q11 #Find  outputs  (Home  work)
def   disp(empno , ename , sal):
        print(F'Emp  Number  :  {empno} \t  Emp Name  :  {ename} \t  Salary  :  {sal}')
# End  of  the  function
disp(25 , 'Rama  Rao' , 10000.0)  #Emp  Number  :  25        Emp Name  :  Rama  Rao          Salary  :  10000.0 
disp('Sita' , 20000.0 , 35)        #Emp  Number  :  Sita      Emp Name  :  20000.0    Salary  :  35

Q12 Find  outputs  (Home  work)
def    f1(a , b , c):
          print(F'a  :  {a}    \t  b  :  {b}  \t  c :  {c}')
# End  of  the  function
f1(a = 10 , b = 20 , c = 30)  #  a : 10  <tab>  b : 20 <tab>  c : 30
f1(25 , 10.8 , 'Hyd')   #  a :  25   <tab>  b :  10.8  <tab>  c :  Hyd
f1(b = 40.7 , a = 50.2 , c = 60.5)   #  a :  50.2   <tab>  b :  40.7  <tab>  c :  60.5
f1(c = 'Hyd' , b = 'Sec' , a = 'Cyb') # a : Cyb  <tab> b : Sec <tab>  c : Hyd
f1(c = 3 + 4j , a = True , b = None)  # a : True  <tab>  b : None <tab>  c: (3+4j)
f1(25 , c = 10.8 , b = 'Hyd')         # a : 25  <tab>  b: Hyd <tab>  c: 10.8
#f1(a = 100 , 200 , 300)  #  Error  becoz  pa's  are  after  ka
#f1(True , None , b = 'Hyd')  #  Error  becoz arg  is  passed  for  'b'  twice
#f1(10 , 20 , x = 30)  #  Error  becoz  arg  'x'  does  not  exist  for  f1()  function
#f1(10 , 20)  #  Error :  Arg  is  not  passed  for  'c'

Q13 #Find  outputs (Home  work)
def    disp(empno , ename , sal):
        print(F'Emp  Number : {empno:4}  \t  Emp  Name : {ename:15}  \t  Salary : {sal}')
# End  of  the  function
disp(25 , 'Rama Rao' , 10000.0)     #Emp  Number :   25    Emp  Name : Rama Rao     Salary : 10000.0
disp(ename = 'Sita' , sal = 20000.0 , empno = 35) #Emp  Number :   35   Emp  Name : Sita    Salary : 20000.0
x = 'Rama  Rao'
y = 30000.0
z = 20
disp(x , y , z)  #Emp  Number : Rama  Rao     Emp  Name : 30000.0     Salary : 20

Q14 #Find  outputs (Home  work)
def    f1(a , b , c):
	return  a + b * c
#end  of  the  function
print(f1(3 , 4 , 5)) # 3 + (4 * 5) = 3 + 20 = 23
print(f1(*[6 , 7 , 8])) # 6 + (7 * 8) = 6 + 56 = 62
#print(f1([6 , 7 , 8]))  # error - because only 1 argument is given.
print(f1(*{1 : 2 , 3 : 4 , 5 : 6})) # 1 + (3 * 5) = 1 + 15 = 16
print(f1(**{'c' : 2 , 'b' :  4 , 'a' : 6})) # 6 + (4 * 2) = 6 + 8 = 14
#print(f1({'c' : 2 , 'b' :  4 , 'a' : 6})) # error - only 1 argument is given 
print({**{'c' : 2 , 'b' :  4 , 'a' : 6}}) # {'c' : 2 , 'b' :  4 , 'a' : 6}
#print(f1(**{'c' : 2 , 'a' : 4 , 'x' : 6})) # error - x varaible is not defined

Q15 #Identify  Error (Home  work)
a = [10 , 20 , 15 , 5 , 12]
print(sorted(reverse = True , a)) #error- positional argument 'a' should be given as 1st argument
print(sorted(a , rev = True))     #error due to rev 
print(25 , 10.8 , 'Hyd' , separator = '\t') #error due to seperator 
print(25 , 10.8 , 'Hyd' , endofline = '\t') #error due to endofline
print(25 ,  sep = '\t' , 10.8 , end = '\t' , 'Hyd') #error  -  positional argument '10.8' should be given before keyword argument
'''