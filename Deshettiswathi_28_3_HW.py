#28/03/25
'''
#   Find  outputs
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
print('End')'

#================================
# Find  outputs  (Home  work)
def  f1(x , y):
	if   x > 40:
		return
	x += y
	f1(x , y)
	print(x)
#End  of  the  function
x = 10
f1(x,x:=x+1)
print(x)#11 21 32 43

#===================================
# Find  outputs   (Home  work)
def  f1(x):
	print(x)
	if   x:
		f1(x - 1)
	print(x)
# End  of  the  function
f1(3)

#====================================
# Find  outputs (Home  work)
def   f1():
	yield  25
	yield  10.8
	yield  'Hyd'
# End of  generator
while  True:
	print(next(f1()))#infinite 25
#========================================

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
#================================================

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
#=======================================

#Find  outputs (Home  work)
import  time
g = (x * x   for    x    in    range(5))
for  y  in   g:
	print(y)
	time . sleep(2)
	print('Hello')
for  y  in g:
	print(y)
#=============================================
# Find  outputs (Home  work)
import  time
for  y  in   (x * x   for    x    in    range(5)):
	print(y)#0 1 4 9 16
	time . sleep(2)
for  y  in   (x * x   for    x    in    range(5)):
	print(y)#0 1 4 9 16
	time.sleep(2)
#==========================================

# Find  outputs(Home  work)
import  time
g1 = (x * x   for  x  in  range(5))
g2 = g1
for  y  in  g1:
	print(y)#0 1 4 9 16
	time . sleep(2)
for  y  in  g2:
	print(y)
print(g1 is g2)#True
#================================================

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
#===========================================

#  Find  outputs
def  f1():
	print('f1  function')
	#f2()
	print('End  of  f1  function')
def  f2():
	print('f2  function')
	f1()
	print('End  of  f2  function')
f1()#f1  function End  of  f1  function
#=======================================================
'''
