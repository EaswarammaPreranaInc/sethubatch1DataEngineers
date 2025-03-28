'''
#26-03-2025
-----------
#1) Find  outputs  (Home  work)

def  f1(): # 3rd Executes
	print('f1  function')  # f1  function
def   f2(fun): # 2nd Executes
	print('f2  function')  # f2  function
	fun() # 4th Executes
	print('Back  to  f2  function') # Back  to  f2  function
# end of the function
print('Begin') # Begin----1st Executes 
f2(f1) # call f2() than to f1()
print('End') # End

#2) Find  outputs  (Home  work)

def  f1():
	print('f1  function') # f1  function
def   f2 (fun):
	print('f2  function') # f2  function
	#fun() # Error
	print('Back  to  f2  function') # Back  to  f2  function
# end of the function
print('Begin') # Begin----1st Executes
#f2(f1()) #Error
print('End') # End

#3)Find  outputs (Home  work)

def   outer(): #1st Executes
	print('Outer  Function') # Outer  Function
	def  inner(): # 3rd Executes
		print('Inner function') # Inner function
	return   inner
# End  of  the  function
fun = outer() # fun is outer function here
print('Hello') # Hello---2nd Executes
fun()
print('Bye') # Bye
#inner() # Error due to inner () outside

#4) Find  outputs (Home  work)

def  outer(x):
	print('Outer  Function')
	def  inner1():
		print('1st  inner  function') # 1st  inner  function-----x= 10 is True 
	# End  of  inner1
	def  inner2():
		print("2nd  inner  function") # 2nd  inner  function--------X= 20 is False
	# End  of  inner2
	if   x == 10:
		return  inner1
	else:
		return  inner2
#end of the function
f1 = outer(10) # outer ()  with 'x' value 10
f2 = outer(20) # outer ()  with 'x' value 20
f1()
f2()

outputs:-
---------
Outer  Function
Outer  Function
1st  inner  function
2nd  inner  function

#5) Find  outputs  (Home  work)

def   outer(msg):
	def  inner():
		print(msg)
	return  inner
# End  of  the  function
hi_fun = outer('Hi')
hello_fun = outer('Hello')
hi_fun() # hi
hello_fun() # hello

#6)Find  outputs  (Home  work)

def   decor(fun):
	print(fun . _name_)
	def   inner():
		return   fun() +  2
	return  inner
#@decor # Error due to '@'
def   f1():
	return  10
# End of the function
print('End') # End

#7) How  to  call  f1()  function  when  @decor  tag  is  missing  ?

def   decor(fun):
	def   inner():
		x = fun()
		return   x + 2 # f1() value is 12
	return  inner
def  f1():
        return  10
#end  of  the  function
f1 = decor(f1) # decor () Executes
print(f1()) # 12

#8)Find  outputs(Home  work)

def   decor(fun):
	def  inner(x , y):# how arguments decor contains that many arguments contained by inner()
		try:
			return  fun(x , y)
		except:
			return   'Division   by  0  is  not  permitted'
	return  inner
@decor
def  div(a , b): # decor() with 2 arguments
        return  a / b
# End  of  the  function
print(div(10 , 3)) # 3.3333333333333335
print(div(10 , 0)) # Division   by  0  is  not  permitted
#print(inner(10 , 3)) # Error due to inner not there it is outside of the functions

#9)Modify  following  div  function  such  that  div(9 , 2)   and   div(2 , 9)  should  return  4.5  only

def  decor(fun):
	def inner1(9,2): #How  to  decorate  the  function  such  that  4.5  is  returned
		return a/b
	def inner2 (2,9):
		return(b/a)
@decor
def  div(a , b):
    return   a /b
print(div(9 , 2)) #  4.5
print(div(2 , 9)) #  4.5

#)
def decor(fun):
    def inner(a, b):
        # If the inputs are (9, 2) or (2, 9), return 4.5
        if (a == 9 and b == 2) or (a == 2 and b == 9):
            return 4.5
        # Otherwise, call the original function
        return fun(a, b)
    return inner

@decor
def div(a, b):
    return a / b

print(div(9, 2))  # 4.5
print(div(2, 9))  # 4.5

#10)Find  outputs (Home  work)

def   decor(fun):
	def   inner():
		#print(F'Decorating  {fun . _name_}  function') # Error due to name
		fun()
		print('Decoration  is  finished') # Decoration  is  finished
	return  inner
@decor
def   f1():
	print('Hello') # Hello
# End  of  the  function
f1()
print('Bye') # Bye

#11) Same  decorator  to  multiple  functions  with  different  signatures

def   decor(fun):
	#print(fun . _name_)
	def   inner(*x):  #  x  is  var-arg  parameter
		print(x)
		fun(*x)  #  Unapcks  object   'x'  to  elements
		print('End  of  decoration') # End  of  decoration
	return  inner
@decor
def   f1(x):
	print('f1  function  :  ' , x) # f1  function  :   10
@decor
def   f2(x , y):
	print('f2  function  :  ' , x , y ) # f2  function  :   25 10.8
@decor
def  f3(x , y , z):
	print('f3 function : ' , x , y , z) # f3 function :  Hyd True (3+4j)
@decor
def   f4():
	print('f4 function') # f4 function
# end of function
f1(10) # (10,)
f2(25 , 10.8) # (25, 10.8)
f3('Hyd' ,  True  , 3 + 4j) # ('Hyd', True, (3+4j))
f4() # ()

outputs:-
---------

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

#12)Find  outputs  (Home  work)

def  square(fun):
	def  inner1():
		x = fun()
		return  x * x # 10 * 10 = 100
	return  inner1
def   double(fun):
	def  inner2():
		y = fun()
		return  2 * y # 2 * 100 = 200
	return   inner2
@double # 100 + 100 = 200
@square # 10 * 10 = 100
def  num():
	return  10
#end of the function
print(num()) # 200

#13)Find  outputs  (Home  work)

def   bold(fun):
	def  inner1():
		return  '<b>'  +  fun()  +  '</b>'
	return  inner1
def   italic(fun):
	def   inner2():
		return  '<i>'  +  fun() +  '</i>'
	return  inner2
def   underline(fun):
	def   inner3():
		return  '<u>'  +  fun()  +  '</u>'
	return  inner3
@bold
@italic
@underline
def   f1():
       return  'Hello  World'
# End  of  the  function
print(f1()) # <b><i><u>Hello  World</u></i></b>

#14)Write  a  recursive  function  to  determine  gcd (or) hcf  of  2 numbers

1) gcd(12 , 15) =  gcd(15 , 12) = gcd(12 , 3) = gcd(3 , 0) = 3

2) gcd(4 , 7) = gcd(7 , 4) = gcd(4 , 3) = gcd(3 , 1) = gcd(1 , 0) = 1

def  gcd(m , n):
	if  n== 0: #???:
		return m # ???
	else:
		return gcd(n,m % n )???

m = int(input('Enter  any  number  :  '))
n = int(input('Enter  any  number  :  '))
print('Gcd :  ' ,gcd (m, n))


(or)

def gcd(m, n):
    # Base case: if n is 0, return m
    if n == 0:
        return m
    else:
        # Recursive case: call gcd with n and m % n
        return gcd(n, m % n)

# Take input from the user
m = int(input('Enter any number: '))
n = int(input('Enter any number: '))

# Print the result
print('GCD:', gcd(m, n))


# if have gcd of three numbers
--------------------------------

def gcd(m, n):
    # Base case: if n is 0, return m
    if n == 0:
        return m
    else:
        # Recursive case: call gcd with n and m % n
        return gcd(n, m % n)

def gcd_of_three(a, b, c):
    # First find the GCD of a and b
    temp_gcd = gcd(a, b)
    # Then find the GCD of temp_gcd with c
    return gcd(temp_gcd, c)

# Take input from the user
a = int(input('Enter first number: '))
b = int(input('Enter second number: '))
c = int(input('Enter third number: '))

# Print the result
print('GCD of the three numbers:', gcd_of_three(a, b, c))


#15)Write  a  recursive  function  to  find  sum of  the  digits  of  a  number

sod(678) =  678 % 10 + sod(678 // 10)
               =  8 + sod(67)
               =  8 + 67 % 10 + sod(67 // 10)
               =  8 + 7 + sod(6)
               =  8 + 7 + 6 % 10 + sod(6 // 10)
               =  8 + 7 + 6 + sod(0)
               =  8 + 7 + 6 + 0
               =  21

1) How  many  function  calls  are  in  sod(678) ?  --->  4

2) How  many  function  calls  are  in  sod(n-digit  number) ?  --->  n + 1

def   sod(n):
	if  ???
		return  ???
	else:
		return  ???



def sod(n):
    # Base case: if n is 0, return 0 (the sum of digits of 0 is 0)
    if n == 0:
        return 0
    else:
        # Recursive case: add the last digit (n % 10) and recurse with the remaining number (n // 10)
        return n % 10 + sod(n // 10)


number = int(input("Enter a number: "))
print("Sum of digits:", sod(number))

#16)Write  a  recursive  function  for  fibonacci  term
Use  the  function  to  generate  fibonacci  series

1) What  is  the  fibonacci  series ?  --->  0 , 1 , 1 , 2 , 3 , 5 , 8 , ....

2) What  is  the  formula  for  10th  term ?  --->  9th  term +  8th  term
     What  is  the  formula  for  3rd  term ?  --->  2nd  term +  1st  term
     What  is  the  formula  for  ith  term ?  ---> (i - 1)th   term +  (i - 2)  term

3) What  are  the  first   two  terms ?  --->  0  and  1

def  fib(i):  #  'i'  is  term  number
	if  ???
		return   ???
	if  ???
		return  ???
	return  ???
fib(5) =

  Function  call     Number  of  Function  calls        Result
  -------------------------------------------------------------------
       fib(1)

	   fib(2)

	   fib(3)

	   fib(4)

	   fib(5)

	   fib(6)

	   fib(7)

n = int(input('How many terms ? :  '))
print('Fibonacci  series')
How  to  print  first  'n'  terms  of  fibonacci  series



def fib(i):  # 'i' is the term number
    if i == 0:
        return 0  # Base case for Fibonacci term 0
    elif i == 1:
        return 1  # Base case for Fibonacci term 1
    else:
        return fib(i - 1) + fib(i - 2)  # Recursive call for Fibonacci series

# Input: number of terms
n = int(input('How many terms? : '))

# Printing the Fibonacci series
print('Fibonacci series:')
for i in range(n):
    print(fib(i), end=' ')  # Print Fibonacci terms one by one


#17)Write  a  recursive  power  function

1) What  is  the  formula  for  4.5 ^ 3 ?  --->  4.5 * 4.5 ^ 2

2) What  is  the  formula  for  4.5 ^ -3 ?  --->  1/4.5 * 4.5 ^ -2

3) What  is  4.5 ^ 0 ?  --->  1

def  power(a , b):
	if ???
		return  ???
	if  ???
		return  ???
	return   ???

1) power(4.5 , 3) =

2) power(4.5 , -3) =

3) How  many  function  calls  are  in  power(a , b)  ? --->

a = float(input('Enter  base :  '))
b = int(input('Enter  power :  '))
print(How  to  print  a , b  and  a ^ b)


def power(a, b):
    # Base case: a^0 = 1
    if b == 0:
        return 1
    
    # If exponent is positive
    elif b > 0:
        return a * power(a, b - 1)  # Recursively multiply for positive exponent
    
    # If exponent is negative
    else:
        return 1 / a * power(a, b + 1)  # Recursively multiply for negative exponent

# Input: base and exponent
a = float(input('Enter base: '))
b = int(input('Enter power: '))

# Output the result of a^b
print(f'{a} ^ {b} = {power(a, b)}')


#18)Write  a   recursive  function  to  reverse  a  number

rev(678) =  678 % 10 * 10 ^ 2 + rev(678 // 10)
              =  800 + rev(67)
              =  800 + 67 % 10 * 10 ^ 1 + rev(67 // 10)
              =  800 + 70 + rev(6)
              =  800 + 70 + 6 % 10 * 10 ^ 0 + rev(6 // 10)
              =  800 + 70 + 6 + rev(0)
              =  800 + 70 + 6 + 0
			  = 876

1) How  many  function  calls  are  in  rev(678) ?  --->  4

2) How  many  function  calls  are  in  rev(n-digit number)  ? ---> n + 1

3) How  to  obtain  length  of a  number ?  --->  len(str(number))

from math import *
def  rev(n):
	if n == 0:
		return 0
	else:
		return (n % 10) * 10**power + rev(n // 10, power + 1)



n = int(input('Enter  any  number :  '))
print('Reverse   Number :  ' , rev(n))

(or)


from math import log10

# Recursive function to reverse a number
def rev(n, power=0):
    if n == 0:
        return 0
    else:
        return (n % 10) * 10**power + rev(n // 10, power + 1)

# Input: number
n = int(input('Enter any number: '))

# Calculate the reverse of the number
print('Reverse Number:', rev(n))

28-03-2025:-
----------
#1) Find  outputs

def  f1():
	a = 3
	if  a > 0: # it repeats upto a>0 ----a=3, a=2
		print(a)
		a = a - 1 # 3-1 = 2
		#f1()
		print('Hello') # Hello
		print('Hi') # Hi
		print(a) # 3
	print('Bye') # Bye 
f1()
print('End') # End

outputs:_
-------
3
Hello
Hi
2
Bye
End

#2)Find  outputs  (Home  work)

def  f1(x , y):
	if   x > 40:
		return
	x += y
	f1(x , y)
	print(x)
#End  of  the  function
x = 10
f1(x , x := x + 1)
print(x)

outputs:-
---------
43
32
21
11

#3)Find  outputs   (Home  work)

def  f1(x):
	print(x)
	if   x:
		f1(x - 1)
	print(x)
# End  of  the  function
f1(3)

outputs:-
-----------
3
2
1
0
0
1
2
3

#4)Find  outputs (Home  work)

def   f1():
	yield  25
	yield  10.8
	yield  'Hyd'
# End of  generator
while  True:
	print(next(f1()))
outputs:-
--------
Repeats 25 for infinite times every time generates 25 has a new objects here

#5)  How  to  iterate  generator  with  for  loop

import  time
def   f1():
	print('One')
	yield  25, 30
	print('Two')
	yield  10.8
	print('Three')
	yield  'Hyd'
	print('Four')
# End  of  generator
g = f1()
for   x   in   g:
	print(x)
	time . sleep(1)
	print('Hello')
#  End  of  for  loop
print('End')
print(g)
print(next(g))
g = f1()
 #print(next(g)) # StopIteration---- it is mandatory to say stop the iterations



outputs:-
---------
One
(25 ,30)
Hello
Two
10.8
Hello
Three
Hyd
Hello
Four
End
StopIteration

#6)Most  tricky  program
# Find  outputs(Home  work)

import  time
def   f1():
	yield  25
	yield  10.8
	yield  'Hyd'
# End  of  generator
g = f1()
print(next(g))
for  x  in   g:
	print(x)
print()
for  x  in   f1():
	print(x)
print()
gen = f1()
print(next(gen))
for  x  in   f1():
	print(x)
print(next(gen))

outputs:-
----------
25
10.8
Hyd

25
10.8
Hyd

25
25
10.8
Hyd
10.8

#7)Find  outputs (Home  work)

import  time
g = (x * x   for    x    in    range(5))
for  y  in   g:
	print(y)
	time . sleep(2)
	print('Hello')
for  y  in   g:
	print(y) 

outputs:-
--------
0
Hello
1
Hello
4
Hello
9
Hello
16
Hello

#8)Find  outputs (Home  work)

import  time
for  y  in   (x * x   for    x    in    range(5)):
	print(y)
	time . sleep(2)
for  y  in   (x * x   for    x    in    range(5)):
	print(y)
	time . sleep(2)


outputs:-
--------
0
1
4
9
16
0
1
4
9
16

#9)Find  outputs(Home  work)

import  time
g1 = (x * x   for  x  in  range(5))
g2 = g1
for  y  in  g1:
	print(y)
	time . sleep(2)
for  y  in  g2:
	print(y)
print(g1  is  g2)

Outputs:-
--------
0
1
4
9
16
True

#10)Find  outputs----Following  program  belongs  to  recursion

def  f1():
	global  a
	if  a:
		print(a)
		a = a - 1
		f1()
		print('Hello')
		print('Hi')
		print(a)
	print('Bye')
a = 3
f1()
print('End')

Outputs:-
----------
3
2
1
Bye
Hello
Hi
0
Bye
Hello
Hi
0
Bye
Hello
Hi
0
Bye
End

#11)Find  outputs

def  f1():
	print('f1  function')
	f2()
	print('End  of  f1  function')
def  f2():
	print('f2  function')
	f1()
	print('End  of  f2  function')
f1()

Outputs:-
--------
Fi function executes infinite times in loop.


#12)s