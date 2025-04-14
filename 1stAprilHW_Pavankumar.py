'''
PROGRAM_1:
Write  a  generator  to  yield  sum , difference , product  and  division  of  2  numbers

Hint:  Use  generator  function  and  for  loop  to  retrieve  elements
'''
import time
def f1(a,b):
	yield F'Sum : {a+b}'
	time.sleep(1)
	yield f'Product : {a*b}'
	time.sleep(1)
	try:
		yield F'Division : {a/b}'
	except:
		yield 'Division by 0 is not permitted'
	time.sleep(1)
	if a>b:
		yield f'Difference : {a-b}'
	else:
		yield f'Difference : {b-a}'
m=int(input("Enter first number : "))
n=int(input("Enter Second number : "))
gen=f1(m,n)
for i in gen:
	print(i)
'''
OUTPUT:
Enter first number : 10
Enter Second number : 7
Sum : 17
Product : 70
Division : 1.4285714285714286
Difference : 3
Enter first number : 10
Enter Second number : 0
Sum : 10
Product : 0
Division by 0 is not permitted
Difference : 10
'''
'''
PROGRAM_2:

Design  a  generator  to  yield  from  x (may  be  10)  to   y (may  be  20)

Hint:  Use  generator  function  and  for  loop

Hint:  Do  not  use  range  object
'''
def f1(a,b):
	while a<=b:
		yield a
		a+=1
x=int(input("Enter starting number value :"))
y=int(input("Enter ending number value :"))
g=f1(x,y)
for i in g:
	print(i)
'''
OUTPUT:
Enter starting number value :10
Enter ending number value :20
10
11
12
13
14
15
16
17
18
19
20
'''
'''
Write  a   generator  to  generate  fibonacci  series

1) What  is  fibonacci  series ?  --->  0 , 1 , 1 , 2 , 3 , 5 , 8 , .....

4) Use  generator  function  and  for  loop
'''
def f1(a):
	if a==1:
		yield 0
	elif a==2:
		yield 0
		yield 1
	else:
		x=z=0
		y=1
		yield x
		yield y
		while z<a-2:
			c=x+y
			yield c
			x=y
			y=c
			z+=1
n=int(input("Enter number to get fibonacci series upto that number : "))
gen=f1(n)
for i in gen:
	print(i)
'''
OUTPUT:
Enter number to get fibonacci series upto that number : 10
0
1
1
2
3
5
8
13
21
34
'''
'''
Write  a  generator  to  divide  a  string  into  words

Hint1:  Use  generator  function  and  for   loop

Hint2:  Use  split()  method  of  str  class
'''
def f1(s):
	a=s.split(' ')
	for i in a:
		yield i
s=input("Enter input String : ")
gen=f1(s)
for i in gen:
	print(i)
'''
OUTPUT:
Enter input String : Hyd is green city
Hyd
is
green
city
'''
# Find  outputs
def   f1():
        yield   [10 , 20]
        yield  {30 , 40 , 50}
        yield  60  , 70 , 80 , 90
        yield  100
g = f1()
for   x   in   g:
	print(x)
	print(type(x))
'''
OUTPUT:
[10,20]
class list
{30,40,50}
class set
(60,70,80,90)
class tuple
100
class int
'''
#  Find  outputs
def   f1():
	x = 1
	while  x <=  100000000000000000000:
		yield  x
		x +=  1
g = f1()
print('Begin')
print(*g)
print('End')
'''
OUTPUT:
Begin
1 2 3 4...... 100000000000000000000
End
'''
#  Find  outputs
g = (x * x  for  x  in  range(500000000000000000))
print(*g)
'''
OUTPUT:
0 1 4 9 16 25 36 49 64 81 100 121 144 169 196 225 256 289 324 361 400 441 ........
'''
#  Find    outputs (Home  work)
def      f1():
	print('One')
	yield    1
	print('Two')
	yield    2
	print('Three')
	yield    3
	print('End')
g = f1()
for   m   in   g:
	print(m)
x ,  y ,  z  =  f1()
print(x)
print(y)
print(z)
'''
OUTPUT:
One
1
Two
2
Three
3
End
One
Two
Three
End
1
2
3
'''
# Identify  error (Home  work)
'''def  f1():
        yield  10
        yield  20
        yield  30
        yield  40
'''
#a,b,c=f1() -> too many values to unpack
#p,q,r,s,m=f1() ->not enough values to unpack
#  Find  outputs (Home  work)
def   f1():
	yield    1
	yield    2
	yield    3
g =  f1()
#print(len(g)) ->generator cannot support length function
#print(g * 3) ->unsupported operand type(s) for *: 'generator' and 'int'
#print(g[0]) ->'generator' object is not subscriptable
#print(g[1 : 3]) ->generator object does not support slicing operation 
print(*g)
'''
OUTPUT:
1 2 3
'''
