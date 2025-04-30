Q1 #Find  outputs  (Home  work)
def  f1():
	print('f1  function')
def   f2(fun):
	print('f2  function')
	fun()
	print('Back  to  f2  function')
# end of the function
print('Begin')
f2(f1)
print('End')

OP-
Begin
f2  function
f1  function
Back  to  f2  function
End
#-------------------------------------------------------------------------------------------
Q2 #Find  outputs  (Home  work)
def  f1():
	print('f1  function')  #print f1 function and return None
def   f2 (fun): 
	print('f2  function')  #print f2  function
	#fun()                  #None() error because None is object but not function
	print('Back  to  f2  function')
# end of the function
print('Begin')
f2(f1())   # f1() is executed first  --->f2(None)
print('End')

OP-
Begin
f1  function
f2  function
Back  to  f2  function
End
#--------------------------------------------------------------------------------------------
Q3 #Find  outputs (Home  work)
def   outer():
	print('Outer  Function')
	def  inner():
		print('Inner function')
	return   inner
# End  of  the  function
fun = outer()
print('Hello')
fun()
print('Bye')
#inner()  #error- inner() cannot be callable directly from outside of the function

OP-
Outer  Function
Hello
Inner function
Bye
#---------------------------------------------------------------------------------------------
Q4 #Find  outputs (Home  work)
def  outer(x):
	print('Outer  Function')
	def  inner1():
		print('1st  inner  function')
	# End  of  inner1
	def  inner2():
		print("2nd  inner  function")
	# End  of  inner2
	if   x == 10:
		return  inner1
	else:
		return  inner2
#end of the function
f1 = outer(10)
f2 = outer(20)
f1()
f2()

OP-
Outer  Function
Outer  Function
1st  inner  function
2nd  inner  function
#--------------------------------------------------------------------------------------
Q5 #Find  outputs  (Home  work)
def   outer(msg):
	def  inner():
		print(msg)
	return  inner
# End  of  the  function
hi_fun = outer('Hi')
hello_fun = outer('Hello')
hi_fun()
hello_fun()

OP-
Hi
Hello
#----------------------------------------------------------------------------------------------
Q6 #Find  outputs  (Home  work)
def   decor(fun):
	print(fun . __name__)  #f1
	def   inner():
		return   fun() +  2
	return  inner
@decor
def   f1():
	return  10
# End of the function
print('End')  #End
#---------------------------------------------------------------------------------------------
Q7 # Find  outputs(Home  work)
def   decor(fun):
	def  inner(x , y):
		try:
			return  fun(x , y)
		except:
			return   'Division   by  0  is  not  permitted'
	return  inner
@decor
def  div(a , b):
        return  a / b
# End  of  the  function
print(div(10 , 3)) #3.3333333333333335
print(div(10 , 0)) #Division   by  0  is  not  permitted
print(inner(10 , 3)) #error inner is not defined
#----------------------------------------------------------------------------------------------------------------
Q8 #Modify  following  div  function  such  that  div(9 , 2)   and   div(2 , 9)  should  return  4.5  only
def  decor(fun):
	def inner(x,y):                 #How  to  decorate  the  function  such  that  4.5  is  returned
		if x>y:
			return fun(x,y)
		else:
			return fun(y,x)
	return inner
@decor
def  div(a , b):
    return   a /b
print(div(9 , 2)) #  4.5
print(div(2 , 9)) #  4.5
#-----------------------------------------------------------------------------------------------------
Q9 #Find  outputs (Home  work)
def   decor(fun):
	def   inner():
		print(F'Decorating  {fun . __name__}  function')  #Decorating  f1  function
		fun()                                             #Hello
		print('Decoration  is  finished')                 #Decoration  is  finished
	return  inner
@decor
def   f1():
	print('Hello')
# End  of  the  function
f1()
print('Bye')          #Bye
#----------------------------------------------------------------------------------------------------
Q10 # Same  decorator  to  multiple  functions  with  different  signatures
def   decor(fun):
	print(fun . __name__)
	def   inner(*x):        # x  is  var-arg  parameter
		print(x)
		fun(*x)             #Unapcks  object   'x'  to  elements
		print('End  of  decoration')
	return  inner
@decor
def   f1(x):
	print('f1  function  :  ' , x)
@decor
def   f2(x , y):
	print('f2  function  :  ' , x , y )
@decor
def  f3(x , y , z):
	print('f3 function : ' , x , y , z)
@decor
def   f4():
	print('f4 function')
# end of function
f1(10)
f2(25 , 10.8)
f3('Hyd' ,  True  , 3 + 4j)
f4()

OP-
f1
f2
f3
f4
(10,)
f1  function  :   10
End  of  decoration
(25, 10.8)
f2  function  :   25 10.8
End  of  decoration
('Hyd', True, (3+4j))
f3 function :  Hyd True (3+4j)
End  of  decoration
()
f4 function
End  of  decoration
#------------------------------------------------------------------------------------------------
Q11 #Find  outputs  (Home  work)
def  square(fun):   #fun points to num 
	def  inner1():
		x = fun()
		return  x * x   #100
	return  inner1
def   double(fun):      #fun points to innner1
	def  inner2():  
		y = fun()        #y=100
		return  2 * y    #100*2= 200
	return   inner2
@double  #num=double(square(num())) -----> num=double(inner1) ---->num=inner2
@square
def  num():
	return  10
#end of the function
print(num())       #200
#-----------------------------------------------------------------------------------------------------
Q12 #Find  outputs  (Home  work)
def   bold(fun):  #fun points to inner2
	def  inner1():
		return  '<b>'  +  fun()  +  '</b>'
	return  inner1
def   italic(fun):   #fun points to inner3
	def   inner2():
		return  '<i>'  +  fun() +  '</i>'
	return  inner2
def   underline(fun):  #fun points to f1
	def   inner3():
		return  '<u>'  +  fun()  +  '</u>'
	return  inner3
@bold           #f1=bold(italic(underline(f1))---->f1=bold(italic(inner3))--->f1=bold(inner2) --->f1=inner1
@italic
@underline
def   f1():
       return  'Hello  World'
# End  of  the  function
print(f1())

OP-
<b><i><u>Hello  World</u></i></b>
#------------------------------------------------------------------------------------------------------
Q13 #Write  a  recursive  function  to  determine  gcd (or) hcf  of  2 numbers

def  gcd(m , n):
	if  n==0:
		return  m
	else:
		return  gcd(n,m%n)
m = int(input('Enter  any  number  :  '))
n = int(input('Enter  any  number  :  '))
print('Gcd :  ' ,  gcd(m,n))

OP-
Enter  any  number  :  97
Enter  any  number  :  3
Gcd :   1
#----------------------------------------------------------------------------------------------
Q14 #Write  a  recursive  function  to  find  sum of  the  digits  of  a  number

def   sod(n):
	if  n==0:
		return  0
	else:
		return  n%10+sod(n//10)
n = int(input('Enter  any  number :   '))
print('Sum of the digits :   ' ,  sod(n))

OP-
Enter  any  number :   9427
Sum of the digits :    22
#----------------------------------------------------------------------------------------------
Q15 #Write  a  recursive  function  for  fibonacci  term

def fib(i):
    if i == 1:
        return 0
    elif i == 2:
        return 1
    else:
        return fib(i - 1) + fib(i - 2) 
n = int(input('How many terms: '))
print(f"Term {n} in Fibonacci series: {fib(n)}")
print('Fibonacci series:')
a, b = 0, 1  
if n == 1:
    print(a)
    exit()
print(a, b, end=' ') 
for i in range(2, n): 
    c = a + b
    print(c, end=' ')  # Print next term
    a, b = b, c  # Update values

OP-
How many terms: 10
Term 10 in Fibonacci series: 34
Fibonacci series:
#-----------------------------------------------------------------------------------
Q16 #Write  a  recursive  power  function

def  power(a , b):
	if b>0:
		return  a*power(a,b-1)
	if  b<0:
		return  (1/a)*power(a,b+1)
	else:
		return  1
a = float(input('Enter  base :  '))
b = int(input('Enter  power :  '))
print(F'{a} ^ {b} = {power(a,b)}')

OP-
Enter  base :  5
Enter  power :  -2
5.0 ^ -2 = 0.04000000000000001

Enter  base :  5
Enter  power :  2
5.0 ^ 2 = 25.0
#--------------------------------------------------------------------------------------
Q17 #Write  a   recursive  function  to  reverse  a  number

from math import *
def  rev(n):
	if  n>0:
		return  n%10*pow(10,len(str(n))-1)+rev(n//10)
	else:
		return  0
n = int(input('Enter  any  number :  '))
print('Reverse   Number :  ' , rev(n))

OP-
Enter  any  number :  946
Reverse   Number :   649.0
#--------------------------------------------------------------------------------------------
Q18 #How  to  call  f1()  function  when  @decor  tag  is  missing  ?
def   decor(fun):
	def   inner():
		x = fun()
		return   x + 2
	return  inner
def  f1():
        return  10
#end  of  the  function
f1 = decor(f1)
print(f1()) #12
