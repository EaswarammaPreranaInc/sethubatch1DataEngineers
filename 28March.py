
#  1.   Find  outputs
def  f1():
	a = 3
	if  a > 0:
		print(a) 
		a = a - 1
		#f1() #RecursionError: maximum recursion depth exceeded
		print('Hello')
		print('Hi')
		print(a)
	print('Bye')
f1() 
print('End')

'''
3
i think infinte recrussion error bcz 3 is reduced 2 and everytime condition is checked. '''

#* 2. Find  outputs  (Home  work)
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
'''
11>40
21>40 false
32>40
43>40 True 
print 43 

Output: 43
32
21
11 bcz stack saves after function call they executed last in last out 
''' 
# 3*.  Find  outputs   (Home  work)
def  f1(x):
	print(x)
	if   x:
		f1(x - 1)
	print(x)
# End  of  the  function
f1(3) 
'''

outputs :
	3
	2
	1
	0
	0
	1
	2
	3 ''' 
# 4.  Find  outputs (Home  work)
def   f1():
	yield  25
	yield  10.8
	yield  'Hyd'
# End of  generator
while  True:
	print(next(f1())) 
	'''
	empty generator is created 
	25
	25
	25  continously '''
# 5. How  to  iterate  generator  with  for  loop
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
#print(next(g)) # error 
g = f1()
print(next(g))

'''
one 
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
Type and address
One
25

'''

# *6.  Most  tricky  program
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
for  x  in   f1():  # a new generator object  is created 
	print(x)
print()
gen = f1()
print(next(gen)) #25
for  x  in   f1():  # a new generator object is created 
	print(x)
print(next(gen))
'''
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
10.8 '''

#7. Find  outputs (Home  work) 
import  time
g = (x * x   for    x    in    range(5))
for  y  in   g:
	print(y)
	time . sleep(2)
	print('Hello')
for  y  in   g: # for loop same generator which is exhusted 
	print(y)
'''
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
 # 8. Find  outputs (Home  work)
import  time
for  y  in   (x * x   for    x    in    range(5)):
	print(y)
	time . sleep(2)
for  y  in   (x * x   for    x    in    range(5)):
	print(y)
	time . sleep(2)
'''
0
1
4
9
16
0
1
4
9
16 '''

# 9. Find  outputs(Home  work)
import  time
g1 = (x * x   for  x  in  range(5))
g2 = g1
for  y  in  g1:
	print(y)
	time . sleep(2)
for  y  in  g2:
	print(y)
print(g1  is  g2)

'''
0
1
4
9
16
True '''

# 10.  Find  outputs
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
End'''

# 11. Find  outputs  
def  f1():
	print('f1  function')
	#f2()
	print('End  of  f1  function')
def  f2():
	print('f2  function')
	# f1()
	print('End  of  f2  function')
f1()

'''
f1 function 
f2 function 
each statement are called infintely 

'''
