'''def f1():
	a=3
	if a>0:
		print(a)
		a=a-1
		print(a)
		f1()
		print('hello')
		print('hi')
		print(a)
		print('bye')
f1()
print('end')

output : error as it gets loop as a= 3 and again starts from a=3 as f1() called recursive.
'''
'''
def f1(x,y):
	if x>40:
		return
	x+=y
	f1(x,y)
	print(x)
x=10
f1(x,x:=x+1)
print(x)
'''
'''
def f1(x):
	print(x)
	if x:
		f1(x-1)
	print(x)
f1(3)
'''
'''
def f1():
	yield 25
	yield 10.8
	yield 'hyd'
while True:
	print(next(f1()))
'''
'''
import time
g1=(x*x for x in range(5))
g2=g1
for y in g1:
	print(y)
	time.sleep(2)
for y in g2:
	print(y)
print(g2 is g1)
'''


















