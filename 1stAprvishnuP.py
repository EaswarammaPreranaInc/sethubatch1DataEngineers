"""
#1APR2025
#Write  a  generator  to  yield  sum , difference , product  and  division  of  2  numbers
try:
	import time
	a =int(input('enter 1st number:'))
	b =int(input('enter 2nd number:'))
	def cal():
		for x in range(1):
			yield a+b
			time.sleep(1)
			yield a-b
			time.sleep(1)
			yield a*b
			time.sleep(1)
			yield a/b
	op = ["sum:", "dif:", "mul:", "div:"]
	g = cal()
	for i in range(4):
		print(op[i],next(g))
except ZeroDivisionError:
	print('division by zero not permitted')

#Write  a  generator  to  divide  a  string  into  words
def w(a):
    for x in a.split():
        yield x

a = "Vishnu is good boy"
for i in w(a):
    print(i)

#Write  a   generator  to  generate  fibonacci  series
try:
	import time
	def fib():
		a, b = 0, 1
		while a<=10:
			yield a
			time.sleep(1)
			a,b= b,a+b
	g = fib()
except StopIteration:
	print("end")

# x to y
import time
def f1(x, y):
    while x <= y:
        yield x
        x += 1
        time.sleep(1)
x = int(input('enter starting number'))
y = int(input('enter ending number'))
for i in f1(x, y):
    print(i)
# Find  outputs
def   f1():
        yield   [10 , 20]
        yield  {30 , 40 , 50}
        yield  60  , 70 , 80 , 90
        yield  100
# End  of  generator
g = f1()
for   x   in   g:
	print(x)
	print(type(x))

#output
[10, 20]
<class 'list'>
{40, 50, 30}
<class 'set'>
(60, 70, 80, 90)
<class 'tuple'>
100
<class 'int'>

#  Find  outputs
def   f1():
	x = 1
	while  x <= 100000000000000000000:
		yield  x
		x +=  1
# End of  generator
g = f1()
print('Begin')
#print(*g)#memoryerror
print('End')

 #  Find  outputs
g = (x * x  for  x  in  range(500000000000000000))
#print(*g)#memoryerror

#  Find    outputs (Home  work)
def      f1():
	print('One')
	yield    1
	print('Two')
	yield    2
	print('Three')
	yield    3
	print('End')
# End  of  generator
g = f1()
for   m   in   g:
	print(m)
x ,  y ,  z  =  f1()
print(x)
print(y)
print(z)
#ouput
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

 # Identify  error (Home  work)
def  f1():
        yield  10
        yield  20
        yield  30
        yield  40
#a , b , c = f1()#less objects
#p , q , r , s , m = f1()#more objects

#  Find  outputs (Home  work)
def   f1():
	yield    1
	yield    2
	yield    3
# End  of  generator
g =  f1()
#print(len(g))#error gen has no len()
#print(g * 3)
#print(g[0])#error
#print(g[1 : 3])#error
print(*g)#1 2 3
"""
