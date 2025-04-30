#1  Find  outputs  (Home  work)
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

Output:
Begin
f2  function
f1  function
Back  to  f2  function
End

#2 Find  outputs  (Home  work)
def  f1():
	print('f1  function')
def   f2 (fun):
	print('f2  function')
	#fun()
	print('Back  to  f2  function')
# end of the function
print('Begin')
f2(f1())
print('End')

Output:
Begin
f1  function
f2  function
Back  to  f2  function
End

#3 Find  outputs (Home  work)
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
#inner()

Output:
Outer  Function
Hello
Inner function
Bye

#4 Find  outputs (Home  work)
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

Output:
Outer  Function
Outer  Function
1st  inner  function
2nd  inner  function

#5 Find  outputs  (Home  work)
def   outer(msg):
	def  inner():
		print(msg)
	return  inner
# End  of  the  function
hi_fun = outer('Hi')
hello_fun = outer('Hello')
hi_fun()
hello_fun()

Output:
Hi
Hello

#6 Find  outputs  (Home  work)
def   decor(fun):
#	print(fun . _name_)
	def   inner():
		return   fun() +  2
	return  inner
@decor
def   f1():
	return  10
# End of the function
print('End')

Output:
End

#7  How  to  call  f1()  function  when  @decor  tag  is  missing  ?
def   decor(fun):
	def   inner():
		x = fun()
		return   x + 2
	return  inner
def  f1():
        return  10
#end  of  the  function
f1 = decor(f1)
print(f1())

Output:
12

#8 Find  outputs(Home  work)
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
print(div(10 , 3))
print(div(10 , 0))
#print(inner(10 , 3))

Output:
3.3333333333333335
Division   by  0  is  not  permitted

#9 Modify  following  div  function  such  that  div(9 , 2)   and   div(2 , 9)  should  return  4.5  only
def  decor(fun):
	def inner(a,b):
		if a<b:
			a,b=b,a
		return fun(a,b)
	return inner
@decor
def  div(a , b):
    return   a /b
print(div(9 , 2)) #  4.5
print(div(2 , 9)) #  4.5

Output:
4.5
4.5

#10 Find  outputs (Home  work)
def   decor(fun):
	def   inner():
#		print(F'Decorating  {fun . _name_}  function')
		fun()
		print('Decoration  is  finished')
	return  inner
@decor
def   f1():
	print('Hello')
# End  of  the  function
f1()
print('Bye')

Output:
Hello
Decoration  is  finished
Bye

#11 Same  decorator  to  multiple  functions  with  different  signatures
def   decor(fun):
#	print(fun . _name_)
	def   inner(*x):  #  x  is  var-arg  parameter
		print(x)
		fun(*x)  #  Unapcks  object   'x'  to  elements
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

Output:
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

#12 Find  outputs  (Home  work)
def  square(fun):
	def  inner1():
		x = fun()
		return  x * x
	return  inner1
def   double(fun):
	def  inner2():
		y = fun()
		return  2 * y
	return   inner2
@double
@square
def  num():
	return  10
#end of the function
print(num())

Output:
200

#13  Find  outputs  (Home  work)
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
print(f1())

Output:
<b><i><u>Hello  World</u></i></b>

#14  Write  a  recursive  function  to  determine  gcd (or) hcf  of  2 numbers
#1) gcd(12 , 15) =  gcd(15 , 12) = gcd(12 , 3) = gcd(3 , 0) = 3
#2) gcd(4 , 7) = gcd(7 , 4) = gcd(4 , 3) = gcd(3 , 1) = gcd(1 , 0) = 1
def  gcd(m , n):
	if  n==0:
		return  m
	else:
		return  gcd(n, m%n)
m = int(input('Enter  any  number  :  '))
n = int(input('Enter  any  number  :  '))
print('Gcd :  ' ,  gcd(m,n))

Output:
Enter  any  number  :  12
Enter  any  number  :  36
Gcd :   12

#15 Write  a  recursive  function  to  find  sum of  the  digits  of  a  number
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
	if  n==0:
		return  0
	else:
		return  n%10 + sod(n//10)
n = int(input('Enter  any  number :   '))
print('Sum of the digits :   ' ,  sod(n))

Output:
Enter  any  number :   9427
Sum of the digits :    22

#16 Write  a  recursive  function  for  fibonacci  term
Use  the  function  to  generate  fibonacci  series
1) What  is  the  fibonacci  series ?  --->  0 , 1 , 1 , 2 , 3 , 5 , 8 , ....
2) What  is  the  formula  for  10th  term ?  --->  9th  term +  8th  term
     What  is  the  formula  for  3rd  term ?  --->  2nd  term +  1st  term
     What  is  the  formula  for  ith  term ?  ---> (i - 1)th   term +  (i - 2)  term
3) What  are  the  first   two  terms ?  --->  0  and  1

def  fib(i):  #  'i'  is  term  number
	if  i==0:
		return   0
	if  i==1:
		return  1
	return  fib(i-1) + fib(i-2)
n = int(input('How many terms ? :  '))
print('Fibonacci  series')
for i in range(n):
    print(fib(i), end=" ") 

Output:
How many terms ? :  7
Fibonacci  series
0 1 1 2 3 5 8 

#17 Write  a  recursive  power  function
1) What  is  the  formula  for  4.5 ^ 3 ?  --->  4.5 * 4.5 ^ 2
2) What  is  the  formula  for  4.5 ^ -3 ?  --->  1/4.5 * 4.5 ^ -2
3) What  is  4.5 ^ 0 ?  --->  1

def pow(a, b):
    if b == 0:
        return 1
    if b > 0:
        return a * pow(a, b - 1) 
    else:
        return 1 / pow(a, -b) 
a = float(input('Enter  base :  '))
b = int(input('Enter  power :  '))
print(f"{a} ^ {b} = {pow(a, b)}")

Output:
Enter  base :  8
Enter  power :  6
8.0 ^ 6 = 262144.0

#18 Write  a   recursive  function  to  reverse  a  number
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

from math import log10

def rev(n):
    if n == 0:
        return 0
    num_digits = int(log10(n)) 
    return (n % 10) * (10 ** num_digits) + rev(n // 10)  
n = int(input('Enter  any  number :  '))
print('Reverse   Number :  ' , rev(n))

Output:
Enter  any  number :  7581346
Reverse   Number :   643185