#  1. Find  outputs  (Home  work)
def  f1():
	print('f1  function')
def   f2(fun):
	print('f2  function')
	fun() # f1
	print('Back  to  f2  function')
# end of the function
print('Begin') #Begin
f2(f1) #f2 function  f1 function Back to f2 function 
print('End') # end

#  2. Find  outputs  (Home  work) 
def  f1():
	print('f1  function') # prints and then return none 
def   f2 (fun):
	print('f2  function')
	#fun() # error  none type object is not callable 
	print('Back  to  f2  function')
# end of the function
print('Begin')
f2(f1())
print('End')
'''
Begin 
f1 function 
f2 function 
Back to f2 function ''' 

# 3. Find  outputs (Home  work)
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
#inner() # Error 
'''
Outer function 
Hello
Inner Function 
Bye

''' 
# 4. Find  outputs (Home  work)
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
f1 = outer(10) # inner1
f2 = outer(20)# inner 2
f1()
f2()
'''
Outer function 
Outer function 
1 st inner function
2nd inner function 

''' 

# 5. Find  outputs  (Home  work)
def   outer(msg):
	def  inner():
		print(msg)
	return  inner
# End  of  the  function
hi_fun = outer('Hi') # inner with msg hi 
hello_fun = outer('Hello') # '' HEllo 
hi_fun()
hello_fun()

'''
Hi
Hello
'''

#6.Find  outputs  (Home  work)
def   decor(fun): # fun is f1
	print(fun . __name__)
	def   inner():
		return   fun() +  2
	return  inner
@decor # f1= decor(f1) ->  f1 = inner 
def   f1():
	return  10
# End of the function
print('End')

'''
f1
End 

'''

# 7. How  to  call  f1()  function  when  @decor  tag  is  missing  ?
def   decor(fun): # fun is f1
	def   inner():
		x = fun() # x= f1 
		return   x + 2 #12
	return  inner
def  f1():
        return  10
#end  of  the  function
f1 = decor(f1) # iiner 
print(f1()) # call inner  
'''
12
''' 
# 8. Find  outputs(Home  work)
def   decor(fun): # fun is div 
	def  inner(x , y):
		try:
			return  fun(x , y) 
		except:
			return   'Division   by  0  is  not  permitted'
	return  inner
@decor # div= decor(div) --> div = inner 
def  div(a , b):
        return  a / b
# End  of  the  function
print(div(10 , 3)) 
print(div(10 , 0))
#print(inner(10 , 3))# eerorr inner is defined 
'''
3.33
Division by o is not permitted  '''

# 9. Modify  following  div  function  such  that  div(9 , 2)   and   div(2 , 9)  should  return  4.5  only
def  decor(fun):
	#How  to  decorate  the  function  such  that  4.5  is  returned
	def inner(x,y):
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
# 10. Find  outputs (Home  work)
def   decor(fun): # fun is f1
	def   inner():
		print(F'Decorating  {fun . __name__}  function')
		fun()
		print('Decoration  is  finished')
	return  inner
@decor # f1= decor(f1) -->   inner 
def   f1():
	print('Hello')
# End  of  the  function
f1() # inner 
print('Bye')
'''
Decorating  f1 function
Hello
Decoration is finished 
Bye
''' 
# Gift
# 11.  Same  decorator  to  multiple  functions  with  different  signatures
def   decor(fun): # f1
	print(fun . __name__) # f1 f2 f3 f4
	def   inner(*x):  #  x  is  var-arg  parameter
		print(x)
		fun(*x)  #  Unapcks  object   'x'  to  elements
		print('End  of  decoration')
	return  inner
@decor # f1=decor(f1)  -- inner 
def   f1(x):
	print('f1  function  :  ' , x)
@decor 
def   f2(x , y): #  -- inner 
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
'''
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
''' 
# 12. Find  outputs  (Home  work)
def  square(fun): # fun is num 
	def  inner1():
		x = fun()
		return  x * x
	return  inner1
def   double(fun):  # fun is inner 1
	def  inner2():
		y = fun()
		return  2 * y
	return   inner2
@double # num=double(square(num)) --> double(inner1) -->  num is inner 2
@square
def  num():
	return  10
#end of the function
print(num())
'''
200
'''
# 13. Find  outputs  (Home  work)
def   bold(fun):
	def  inner1(): # inner 2
		return  '<b>'  +  fun()  +  '</b>'
	return  inner1
def   italic(fun):
	def   inner2(): # inner 3
		return  '<i>'  +  fun() +  '</i>'
	return  inner2
def   underline(fun): # fun is f1 
	def   inner3():
		return  '<u>'  +  fun()  +  '</u>'
	return  inner3
@bold # f1=bold(italic(underline(f1))) 
@italic
@underline
def   f1():
       return  'Hello  World'
# End  of  the  function
print(f1())
'''
<b><i><u>Hello  World</u></i></b>
'''

'''
14. Write  a  recursive  function  to  determine  gcd (or) hcf  of  2 numbers

1) gcd(12 , 15) =  gcd(15 , 12) = gcd(12 , 3) = gcd(3 , 0) = 3

2) gcd(4 , 7) = gcd(7 , 4) = gcd(4 , 3) = gcd(3 , 1) = gcd(1 , 0) = 1
'''
def  gcd(m , n):
	if  n>0:
		return  gcd(n,m%n)
	else:
		return  m
'''
1) gcd(4 , 6)  ---> gcd(6,4) --> gcd(4,2)--> gcd(2,2)-->gcd(2,0) -->2
'''
m = int(input('Enter  any  number  :  '))
n = int(input('Enter  any  number  :  '))
print('Gcd :  ' ,  gcd(m,n))

'''
15. Write  a  recursive  function  to  find  sum of  the  digits  of  a  number

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
def   sod(n):
	if  n>0:
		return  (n%10)+ sod(n//10)
	else:
		return  0
'''
1) sod(9427) =
'''
n = int(input('Enter  any  number :   '))
print('Sum of the digits :   ' ,  sod(n)) 

'''
16. Write  a  recursive  function  for  fibonacci  term
Use  the  function  to  generate  fibonacci  series

1) What  is  the  fibonacci  series ?  --->  0 , 1 , 1 , 2 , 3 , 5 , 8 , ....

2) What  is  the  formula  for  10th  term ?  --->  9th  term +  8th  term
     What  is  the  formula  for  3rd  term ?  --->  2nd  term +  1st  term
     What  is  the  formula  for  ith  term ?  ---> (i - 1)th   term +  (i - 2)  term

3) What  are  the  first   two  terms ?  --->  0  and  1
'''
def  fib(i):  #  'i'  is  term  number
	if  i==1:
		return   0
	if  i==2:
		return  1
	return  fib(i-1)+fib(i-2)
'''
fib(5) = fib(4)+ fib(3)  --> fib(3)+fib(2) +fib(2)+fib(1) --> fib(2)+Fib(1)+1+1+0 

  Function  call     Number  of  Function  calls        Result
  -------------------------------------------------------------------
       fib(1)               1                            0

	   fib(2)               1                            1

	   fib(3)               3                            1

	   fib(4)               5                            2

	   fib(5)               9                            3 

	   fib(6)               15                          5

	   fib(7)               25                          8
'''
n = int(input('How many terms ? :  '))
print('Fibonacci  series')
for x in range(1,n+1):
	print(fib(x))

#How  to  print  first  'n'  terms  of  fibonacci  series

'''
17. Write  a  recursive  power  function

1) What  is  the  formula  for  4.5 ^ 3 ?  --->  4.5 * 4.5 ^ 2

2) What  is  the  formula  for  4.5 ^ -3 ?  --->  1/4.5 * 4.5 ^ -2

3) What  is  4.5 ^ 0 ?  --->  1
'''
def  power(a , b):
	if b>0:
		return  a* power(a,(b-1))
	if  b<0:
		return  1/a*power(a,(b+1))
	return   1
'''
1) power(4.5 , 3) = 4.5* power(4.5,2) = 4.5*4.5*power(4.5,1)= 4.5*4.5*4.5*1

2) power(4.5 , -3) = 1/4.5* power(4.5,-2)= 1/4.5*1/4.5 power(4.5,-1 ...

3) How  many  function  calls  are  in  power(a , b)  ? --->
'''
a = float(input('Enter  base :  '))
b = int(input('Enter  power :  '))
print(f'Base:{a} Power:{b} Result:{power(a,b)}')
#print(How  to  print  a , b  and  a ^ b)

'''
18. Write  a   recursive  function  to  reverse  a  number

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
from math import *
def  rev(n):
	if  n>0:
		return (n%10)* pow(10,len(str(n))-1) +rev(n//10)
	else:
		return  0
'''
rev(946)  =
'''
n = int(input('Enter  any  number :  '))
print('Reverse   Number :  ' , rev(n))
