

#1.Find  outputs 
'''
def  f1():
	print('f1  function') #3. f1 function
def   f2(fun):
	print('f2  function') #2. f2 function
	fun()
	print('Back  to  f2  function') #4. Back  to  f2  function
# end of the function
print('Begin') #1.Begin
f2(f1)
print('End') #5. End 

'''

#2.Find  outputs
'''
def  f1():
	print('f1  function') #2. f1 function
def   f2 (fun):
	print('f2  function') #3. f2 function
	#fun() #Error due to no None() 
	print('Back  to  f2  function') #4. Back to f2 function
# end of the function
print('Begin') #1. Begin
f2(f1())
print('End') #5. End

'''


#3.Find  outputs
'''
def   outer():
	print('Outer  Function') #1. Outer Function
	def  inner():
		print('Inner function')
	return   inner
# End  of  the  function
fun = outer() #fun = inner 
print('Hello') #2. Hello
fun() #3. Inner function
print('Bye') #4. Bye 

'''


#4.Find  outputs
'''
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
f1 = outer(10) #1. Outer Function #f1= inner1 
f2 = outer(20) #2. Outer Function #f2=inner2
f1() #3. 1st inner function
f2() #4. 2nd inner function
#inner() #Error no inner() outside the outer()
'''


#5.Find  outputs 
'''
def   outer(msg):
	def  inner():
		print(msg)
	return  inner
# End  of  the  function
hi_fun = outer('Hi') #h1_fun =inner 
hello_fun = outer('Hello') #hello_fun=inner 
hi_fun() #1.Hi
hello_fun() #2. Hello
'''


#6.Find  outputs
'''
def   decor(fun):
	print(fun . _name_) #1. 'f1'
	def   inner():
		return   fun() +  2
	return  inner
@decor #f1=decor(f1) ===> f1=inner 
def   f1():
	return  10
# End of the function
print('End') #2. End
'''


#7.How  to  call  f1()  function  when  @decor  tag  is  missing  ?
'''
def   decor(fun):
	def   inner():
		x = fun() #10
		return   x + 2 #12
	return  inner
def  f1():
        return  10
#end  of  the  function
f1 = decor(f1) #f1=inner 
print(f1()) # 1. 12
'''

#8.Find  outputs
'''
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
print(div(10 , 3)) #3.3333
print(div(10 , 0)) #Division   by  0  is  not  permitted
#print(inner(10 , 3)) #Error no inner()

'''

#9.Modify  following  div  function  such  that  div(9 , 2)   and   div(2 , 9)  should  return  4.5  only
'''
def  decor(fun):
	#How  to  decorate  the  function  such  that  4.5  is  returned
	def inner(a,b):
	    if(a<b):
	        a,b=b,a
	
	    return fun(a,b)
	return inner 
	
@decor #div = decor(div)
def  div(a , b):
    return   a /b
print(div(9 , 2)) #  4.5
print(div(2 , 9)) #  4.5

'''

#10.Find  outputs
'''
def   decor(fun):
	def   inner():
		print(F'Decorating  {fun ._name_}  function') #1. Decoration f1 function 
		fun() #2. Hello 
		print('Decoration  is  finished') #3. Decoration is finished 
	return  inner
@decor #f1=decor(f1) #f1=inner
def   f1():
	print('Hello')
# End  of  the  function
f1() #No 
print('Bye') #4.Bye
'''

# Gift
#11.Same  decorator  to  multiple  functions  with  different  signatures
'''
def   decor(fun):
	print(fun . _name_) 
	def   inner(*x):  #  x  is  var-arg  parameter
		print(x)
		fun(*x)  #  Unapcks  object   'x'  to  elements
		print('End  of  decoration')
	return  inner
	
@decor #f1=decor(f1) ==> f1=inner #1. 'f1'
def   f1(x):
	print('f1  function  :  ' , x)
	
@decor #f2=decor(f2) ==> f2=inner #2. 'f2'
def   f2(x , y):
	print('f2  function  :  ' , x , y )
	
@decor #f3=decor(f3) ==> f3=inner #3. 'f3'
def  f3(x , y , z):
	print('f3 function : ' , x , y , z)
	
@decor #f4=decor(f4) ==> f4=inner #4. 'f4'
def   f4():
	print('f4 function')
# end of function
f1(10) #5. (10,) #6. f1  function  :  10 #7. End  of  decoration
f2(25 , 10.8) #8. (25,10.8) #9. f2  function  :  25 10.8  #10. End  of  decoration
f3('Hyd' ,  True  , 3 + 4j) #11. ('Hyd',True,(3+4j)) #12. f3 function  :  Hyd True (3+4j) #13. End  of  decoration
f4() #14. ()  #15. f4  function  :  #16. End of decoration

'''

#12.Find  outputs 
'''
def  square(fun):
	def  inner1():
		x = fun() #x=10
		return  x * x #100
	return  inner1
def   double(fun):
	def  inner2():
		y = fun() #y=inner1 () ==> y=100
		return  2 * y #200
	return   inner2
@double #num=double(square(num)) ==> num=double(inner1)==> num=inner2
@square
def  num():
	return  10
#end of the function
print(num()) #200

'''

#13.Find  outputs 
'''
def   bold(fun):
	def  inner1():
		return  '<b>'  +  fun()  +  '</b>' #1.<b><i><u>Hello World</u></i></b>
	return  inner1
def   italic(fun):
	def   inner2():
		return  '<i>'  +  fun() +  '</i>'
	return  inner2
def   underline(fun):
	def   inner3():
		return  '<u>'  +  fun()  +  '</u>'
	return  inner3
@bold #f1=bold(italic(underline(f1))) #f1=bold(italic(inner3)) #f1=bold(inner2) #f1=inner1
@italic
@underline
def   f1():
       return  'Hello  World'
# End  of  the  function
print(f1())
'''

'''
15.
Write  a  recursive  function  to  determine  gcd (or) hcf  of  2 numbers

1) gcd(12 , 15) =  gcd(15 , 12) = gcd(12 , 3) = gcd(3 , 0) = 3

2) gcd(4 , 7) = gcd(7 , 4) = gcd(4 , 3) = gcd(3 , 1) = gcd(1 , 0) = 1
'''

'''
def  gcd(m , n):
	if  (n==0):
		return  m
	else:
		return  gcd(n,m%n)

m = int(input('Enter  any  number  :  '))
n = int(input('Enter  any  number  :  '))
print('Gcd :  ' ,  gcd(m,n))

'''


'''
15.
Write  a  recursive  function  to  find  sum of  the  digits  of  a  number

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
'''

"""
def   sod(n):
	if  n==0:
		return  0
	else:
		return  n%10 + sod(n//10)
'''
1) sod(9427) =
'''
n = int(input('Enter  any  number :   '))
print('Sum of the digits :   ' ,sod(n))

"""


'''
16.
Write  a  recursive  function  for  fibonacci  term
Use  the  function  to  generate  fibonacci  series

1) What  is  the  fibonacci  series ?  --->  0 , 1 , 1 , 2 , 3 , 5 , 8 , ....

2) What  is  the  formula  for  10th  term ?  --->  9th  term +  8th  term
     What  is  the  formula  for  3rd  term ?  --->  2nd  term +  1st  term
     What  is  the  formula  for  ith  term ?  ---> (i - 1)th   term +  (i - 2)  term

3) What  are  the  first   two  terms ?  --->  0  and  1
'''

"""
def  fib(i):  #  'i'  is  term  number
	if  i==1:
		return   0
	if  i==2:
		return  1
	return  fib(i-1) + fib(i-2)
'''
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
'''
n = int(input('How many terms ? :  '))
print('Fibonacci  series')
#How  to  print  first  'n'  terms  of  fibonacci  series
for i in range(1,n+1):
    print(fib(i),end=" ")
    
"""


'''
17.
Write  a  recursive  power  function

1) What  is  the  formula  for  4.5 ^ 3 ?  --->  4.5 * 4.5 ^ 2

2) What  is  the  formula  for  4.5 ^ -3 ?  --->  1/4.5 * 4.5 ^ -2

3) What  is  4.5 ^ 0 ?  --->  1
'''

"""
def  power(a , b):
	if b==0:
		return  1
	if  b>0:
		return a*pow(a,b-1)
	return   (1/a)*power(a,b+1)
'''
1) power(4.5 , 3) =

2) power(4.5 , -3) =

3) How  many  function  calls  are  in  power(a , b)  ? --->
'''
a = float(input('Enter  base :  '))
b = int(input('Enter  power :  '))
print(F'a={a} b={b} {a}^{b}={power(a,b)}') #How  to  print  a , b  and  a ^ b

"""


'''

18. 

Write  a   recursive  function  to  reverse  a  number

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
'''

"""
from math import *
def  rev(n):
	if  n==0:
		return  0
	else:
	    l=len(str(n))-1
	    return  (n%10)(10*l)+rev(n//10)
'''
rev(946)  =
'''
n = int(input('Enter  any  number :  '))
print('Reverse   Number :  ' , rev(n))

"""