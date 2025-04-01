#   Find  outputs
def  f1():
	a = 3
	if  a > 0:
		print(a)
		a = a - 1
		f1()
		print('Hello')
		print('Hi')
		print(a)
	print('Bye')
f1()
print('End')
"""
Output:
3
3
3
3
3
"""
# Find  outputs  (Home  work)
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
"""
output:
43
32
21
11
"""
# Find  outputs   (Home  work)
def  f1(x):
	print(x)
	if   x:
		f1(x - 1)
	print(x)
# End  of  the  function
f1(3)
"""
Output:
3
2
1
0
0
1
2
3
"""

# Find  outputs (Home  work)
def   f1():
	yield  25
	yield  10.8
	yield  'Hyd'
# End of  generator
while  True:
	print(next(f1()))
"""
Output:
25
25
25
25-->infinite times executes
"""

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
print(next(g))
"""
Output:
One
25
Hello
Two
10.8
Hello
Three
Hyd
Hello
Four
End
<generator object f1 at 0x00000171B5125F00>
"""
# Most  tricky  program
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
"""
Output:
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
"""

#Find  outputs (Home  work)
import  time
g = (x * x   for    x    in    range(5))
for  y  in   g:
	print(y)
	time . sleep(2)
	print('Hello')
for  y  in   g:
	print(y)
"""
Output:
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
"""

# Find  outputs (Home  work)
import  time
for  y  in   (x * x   for    x    in    range(5)):
	print(y)
	time . sleep(2)
for  y  in   (x * x   for    x    in    range(5)):
	print(y)
	time . sleep(2)
"""
Output:
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
"""

# Find  outputs(Home  work)
import  time
g1 = (x * x   for  x  in  range(5))
g2 = g1
for  y  in  g1:
	print(y)
	time . sleep(2)
for  y  in  g2:
	print(y)
print(g1  is  g2)
"""
Output:
0
1
4
9
16
True
"""
