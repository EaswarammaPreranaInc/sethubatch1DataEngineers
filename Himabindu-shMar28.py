'''#   Find  outputs
def  f1():
	a = 3
	if  a > 0:
		print(a)
		a = a - 1
		#f1()
		print('Hello')
		print('Hi')
		print(a)
	print('Bye')
f1()
print('End')

#output:
3
Hello
Hi
2
Bye
End
'''

'''
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

#output:
'''

'''
# Find  outputs   (Home  work)
def  f1(x):
	print(x)
	if   x:
		f1(x - 1)
	print(x)
# End  of  the  function
f1(3)

outputs:
3
2
1
0
0
1
2
3
'''

	
'''
# Find  outputs (Home  work)
def   f1():
	yield  25
	yield  10.8
	yield  'Hyd'
# End of  generator
while  True:
	print(next(f1()))


#outputs 25 print infinity times
	
'''

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
# End  of  generator
g = f1()
for   x   in   g:
	print(x)
	time . sleep(1)
	print('Hello')
#  End  of  for  loop
print('End')
print(g)
#print(next(g))
g = f1()
print(next(g))

#outputs:
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
<generator object f1 at 0x00000129AFCD65C0>
One
25
'''

'''
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

#outputs:
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

'''
#Find  outputs (Home  work)
import  time
g = (x * x   for    x    in    range(5))
for  y  in   g:
	print(y)
	time . sleep(2)
	print('Hello')
for  y  in   g:
	print(y)

output:
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

'''
# Find  outputs (Home  work)
import  time
for  y  in   (x * x   for    x    in    range(5)):
	print(y)
	time . sleep(2)
for  y  in   (x * x   for    x    in    range(5)):
	print(y)
	time . sleep(2)

output:
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
print(g1  is  g2) 

#output:
0
1
4
9
16
True
'''


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

outputs:
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

'''
#  Find  outputs
def  f1():
	print('f1  function')
	f2()
	print('End  of  f1  function')
def  f2():
	print('f2  function')
	f1()
	print('End  of  f2  function')
f1() # error due recursion 
'''
