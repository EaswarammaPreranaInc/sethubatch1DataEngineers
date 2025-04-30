'''
PROGRAM_1:
'''
def  f1():
	#a = 3 --->maximum recursion depth exceeded bcoz condition is always true
	#if  a > 0:
		#print(a)
		#a = a - 1 -->local variable a is not declared
		#f1() -->maximum recursion depth exceeded bcoz condition
		print('Hello')
		print('Hi')
		#print(a) -->name 'a' is not defined
		print('Bye')
f1()
print('End')
'''
OUTPUT:
Hello
Hi
Bye
End
'''
# Find  outputs  (Home  work)
def  f1(x , y):
	if   x > 40:
		return
	x += y
	f1(x , y)
	print(x)
x = 10
f1(x,x:=x+1)
print(x)
'''
OUTPUT:
43
32
21
11
'''
# Find  outputs   (Home  work)
def  f1(x):
	print(x)
	if   x:
		f1(x - 1)
	print(x)
f1(3)
'''
OUTPUT:
3
2
1
0
0
1
2
3
'''
# Find  outputs (Home  work)
def   f1():
	yield  25
	yield  10.8
	yield  'Hyd'
#while  True:
	print(next(f1()))
'''
OUTPUT:
25 is printed infinite times bcoz evertime new empty object is created.
'''
#  How  to  iterate  generator  with  for  loop
import  time
def   f1():
	print('One')
	yield  25
	print('Two')
	yield  10.8
	print('Three')
	yield  'Hyd'
	print('Four')
g = f1()
for   x   in   g:
	print(x)
	time . sleep(1)
	print('Hello')
print('End')
print(g)
#print(next(g)) -->StopIteration Error
g = f1()
print(next(g))
'''
OUTPUT:
One
25
Two
10.8
Three
Hyd
Hello
Four
End
<generator object f1 at 0x00000221757A6680>
One
25
'''
# Most  tricky  program
# Find  outputs(Home  work)
import  time
def   f1():
	yield  25
	yield  10.8
	yield  'Hyd'
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
'''
OUTPUT:
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
'''
#Find  outputs (Home  work)
import  time
g = (x * x   for    x    in    range(5))
for  y  in   g:
	print(y)
	time . sleep(2)
	print('Hello')
for y in g:
	print(y)
'''
OUTPUT:
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
'''
# Find  outputs (Home  work)
import  time
for  y  in   (x * x   for    x    in    range(5)):
	print(y)
	time.sleep(2)
for  y  in   (x * x   for    x    in    range(5)):
	print(y)
	time.sleep(2)
'''
OUTPUT:
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
'''
# Find  outputs(Home  work)
import  time
g1 = (x * x   for  x  in  range(5))
g2 = g1
for  y  in  g1:
	print(y)
	time . sleep(2)
for  y  in  g2:
	print(y)
print(g1 is g2)
'''
OUTPUT:
0
1
4
9
16
True
'''
#   Find  outputs
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
'''
OUTPUT:
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
'''
#  Find  outputs
'''def  f1():
	print('f1  function')
	f2()
	print('End  of  f1  function')
def  f2():
	print('f2  function')
	f1()
	print('End  of  f2  function')
f1()'''
'''
OUTPUT:
RecursionError:
function f1 is calling other function f2 and vice verca 
'''

