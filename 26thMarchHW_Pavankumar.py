'''
PROGRAM_1
'''
#  Find  outputs  (Home  work)
def  f1():
	print('f1  function')
def   f2(fun):#fun is f1
	print('f2  function')
	fun()
	print('Back  to  f2  function')
print('Begin')
f2(f1)
print('End')
'''
OUTPUT:
Begin
f2 function
f1 funtion
Back  to f2  function
End
'''
#  Find  outputs  (Home  work)
def  f1():
	print('f1  function')
def   f2 (fun):#fun is None
	print('f2  function')
	#fun() ---> 'NoneType' object is not callable
	print('Back  to  f2  function')
print('Begin')
f2(f1())
print('End')
'''
OUTPUT:
Begin
f1  function
f2  function
Back  to   f2 function
End
'''
# Find  outputs (Home  work)
def   outer():
	print('Outer  Function')
	def  inner():
		print('Inner function')
	return   inner
fun = outer()
print('Hello')
fun()
print('Bye')
#inner() --->name 'inner' is not defined.
'''
OUTPUT:
Outer  Function
Hello
Inner function
Bye
'''
# Find  outputs (Home  work)
def  outer(x):
	print('Outer  Function')
	def  inner1():
		print('1st  inner  function')
	def  inner2():
		print("2nd  inner  function")
	if   x == 10:
		return  inner1
	else:
		return  inner2
f1 = outer(10)#f1 points to inner1 fun
f2 = outer(20)#f2 points to inner2 fun
f1()
f2()
'''
OUTPUT:
Outer  Function
Outer  Function
1st  inner  function
2nd  inner  function
'''
# Find  outputs  (Home  work)
def   outer(msg):
	def  inner():
		print(msg)
	return  inner
hi_fun = outer('Hi')
hello_fun = outer('Hello')
hi_fun()
hello_fun()
'''
OUTPUT:
Hi
Hello
'''
#  Find  outputs  (Home  work)
def   decor(fun):#fun points to f1
	print(fun . __name__)
	def   inner():
		return   fun() +  2
	return  inner 
@decor #f1 =decor(f1) ,f1 points to inner fun f1=inner
def   f1():
	return  10
print('End')
'''
OUTPUT:
f1
End
'''
#  How  to  call  f1()  function  when  @decor  tag  is  missing  ?
def   decor(fun):#fun points to f1 fun
	def   inner():
		x = fun()
		return   x + 2
	return  inner
def  f1():
        return  10
f1 = decor(f1) #inner
print(f1())
'''
OUTPUT:
12
'''
# Find  outputs(Home  work)
def   decor(fun):
	def  inner(x , y):
		try:
			return  fun(x , y)
		except:
			return   'Division   by  0  is  not  permitted'
	return  inner
@decor #div =decor(div)
def  div(a , b):
        return  a / b
print(div(10 , 3))
print(div(10 , 0))
#print(inner(10,3)) ---> name 'inner' is not defined.
'''
OUTPUT:
3.33333
'Division   by  0  is  not  permitted'
'''
# Modify  following  div  function  such  that  div(9 , 2)   and   div(2 , 9)  should  return  4.5  only
def  decor(fun):#fun --->div
	def inner(x,y):
		if x>y:
			return fun(x,y)
		else:
			return fun(y,x)
	return inner
@decor #div=decor(div)
def  div(a , b):
    return   a /b
print(div(9,2))#  4.5
print(div(2,9))#  4.5
'''
OUTPUT:
4.5
4.5
'''
#  Find  outputs (Home  work)
def   decor(fun): #fun--->f1
	def   inner():
		print(F'Decorating  {fun . __name__}  function')
		fun()
		print('Decoration  is  finished')
	return  inner
@decor #f1=decor(f1),f1-->inner
def   f1():
	print('Hello')
f1()
print('Bye')
'''
OUTPUT:
Decorating  f1  function
Hello
Decoration  is  finished
Bye
'''
# Same  decorator  to  multiple  functions  with  different  signatures
def   decor(fun):
	print(fun . __name__)
	def   inner(*x):  #  x  is  var-arg  parameter
		print(x)
		fun(*x)  #  Unapcks  object   'x'  to  elements
		print('End  of  decoration')
	return  inner
@decor #f1=decor(f1) -->inner
def   f1(x):
	print('f1  function  :  ' , x)
@decor # f2-->inner
def   f2(x , y):
	print('f2  function  :  ' , x , y )
@decor
def  f3(x , y , z):
	print('f3 function : ' , x , y , z)
@decor
def   f4():
	print('f4 function')
f1(10)
f2(25 , 10.8)
f3('Hyd',True,3+4j)
f4()
'''
OUTPUT:
f1
f2
f3
f4
(10,)
f1  function  :  10
End  of  decoration
(25,10.8)
f2  function  :  25 10.8
End of decoration
('Hyd',True,(3+4j))
f3 function :   Hyd True (3+4j)
End of decoration
()
f4 function
End of decoration
'''
# Find  outputs  (Home  work)
def  square(fun): #fun->num fun
	def  inner1():
		x = fun()
		return  x * x
	return  inner1
def   double(fun):#fun->inner1
	def  inner2():
		y = fun()
		return  2 * y
	return   inner2
@double #num=double(square(num))->double(inner1)->inner2
@square 
def  num():
	return  10
print(num())
'''
OUTPUT:
200
'''
# Find  outputs  (Home  work)
def   bold(fun):#fun->inner2
	def  inner1():
		return  '<b>'  +  fun()  +  '</b>'
	return  inner1
def   italic(fun):#fun->inner3
	def   inner2():
		return  '<i>'  +  fun() +  '</i>'
	return  inner2
def   underline(fun):#fun->f1
	def   inner3():
		return  '<u>'  +  fun()  +  '</u>'
	return  inner3
@bold #f1=bold(italic(underline(f1)))->bold(italic(inner3))->bold(inner2)->inner1
@italic #f1=italic(underline(f1))
@underline #f1=underline(f1)
def   f1():
       return  'Hello  World'
print(f1())
'''
OUTPUT:
<b><i><u>Hello  World</u></i></b>
'''
'''
PROGRAM_2:
Write  a  recursive  function  to  determine  gcd (or) hcf  of  2 numbers
'''
m = int(input('Enter  any  number  :  '))
n = int(input('Enter  any  number  :  '))
def gcd(m,n):
	if n>0:
		return gcd(n,m%n)
	else:
		return m
print('Gcd : ',gcd(m,n))
'''
OUTPUT:
Enter  any  number  :  12
Enter  any  number  :  15
Gcd :  3
Enter  any  number  :  4
Enter  any  number  :  6
Gcd :  2
'''
'''
PROGRAM_3:
Write  a  recursive  function  to  find  sum of  the  digits  of  a  number
'''
n = int(input('Enter  any  number :   '))
def sod(num):
	if num>0:
		return num%10+sod(num//10)
	else:
		return 0
print(sod(n))
'''
OUTPUT:
Enter  any  number :   678
21
Enter  any  number :   9427
22
'''
'''
PROGRAM_4:
Write  a  recursive  function  for  fibonacci  term
Use  the  function  to  generate  fibonacci  series

1) What  is  the  fibonacci  series ?  --->  0 , 1 , 1 , 2 , 3 , 5 , 8 , ....
'''
def fib(m):
	if m==1:
		return 0
	if m==2:
		return 1
	return fib(m-1)+fib(m-2)
n=int(input("Enter a number :"))
for i in range(1,n+1):
	print(fib(i),end=' ')
print()
'''
OUTPUT:
Enter a number :5
0 1 1 2 3 Press any key to continue . . .
'''
'''
PROGRAM_5:
Write  a  recursive  power  function

1) What  is  the  formula  for  4.5 ^ 3 ?  --->  4.5 * 4.5 ^ 2

2) What  is  the  formula  for  4.5 ^ -3 ?  --->  1/4.5 * 4.5 ^ -2

'''
def pow(x,y):
	if y>0:
		return x*pow(x,y-1)
	if y<0:
		return (1/x)*pow(x,y+1)
	else:
		return 1
x=int(input("Enter x value :"))
y=int(input("Enter y value :"))
print(pow(x,y))
'''
OUTPUT:
Enter x value :2
Enter y value :-2
0.25
Enter x value :8
Enter y value :3
512
'''
'''
PROGRAM_6:
Write  a   recursive  function  to  reverse  a  number

'''
def rev(n):
	if n>0:
		return (n%10)*(10**(len(str(n))-1))+rev(n//10)
	else:
		return 0
a=int(input("Enter a number to get reverse :"))
print(rev(a))
'''
OUTPUT:
Enter a number to get reverse :3986
6893
Enter a number to get reverse :946
649
'''
