'''
Write  a  generator  to  yield  sum , difference , product  and  division  of  2  numbers

Hint:  Use  generator  function  and  for  loop  to  retrieve  elements

try:
	def f1(x,y):
		yield x+y
		yield x-y
		yield x*y
		yield x/y
	x=int(input())
	y=int(input())
	g=f1(x,y)
	print('Sum : ',next(g))
	print('Difference : ',next(g))
	print('Product : ',next(g))
	print('Division : ',next(g))
except StopIteration:
	print("no elements in generatorn")
except ZeroDivisionError:
	print('Division  by zero  is  not  permitted')

'''
'''
Design  a  generator  to  yield  from  x (may  be  10)  to   y (may  be  20)

Hint:  Use  generator  function  and  for  loop

Hint:  Do  not  use  range  object


def f1(x,y):
	while x<=y:
		yield x
		x=x+1
x=int(input('enter start value : '))
y=int(input('enter end value : '))
g=f1(x,y)
for i in g:
	print(i)
'''

'''
Write  a   generator  to  generate  fibonacci  series

1) What  is  fibonacci  series ?  --->  0 , 1 , 1 , 2 , 3 , 5 , 8 , .....

2) What  is  the  formula  for  10th  term ?  ---> 9th  term + 8th  term
    What  is  the  formula  for  3rd  term ?  ---> 2nd  term + 1st  term

3) What  are  the  first  two  terms ?  ---> 0  and  1

4) Use  generator  function  and  for  loop


def f1(n):
	x=0
	y=1
	yield x
	yield y
	while x+y<=n:
		sum=x+y
		yield sum
		x=y
		y=sum
n=int(input('last value : '))
g=f1(n)
for i in g:
	print(i)
'''

'''
Write  a  generator  to  divide  a  string  into  words

Hint1:  Use  generator  function  and  for   loop

Hint2:  Use  split()  method  of  str  class

def f1(s):
	a=s.split()
	yield a
s=input('Enter  any   string : ')
print('words in string')
g=f1(s)
for i in g:
	for j in i:
		print(j)

'''
'''
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

#outputs:
[10, 20]
<class 'list'>
{40, 50, 30}
<class 'set'>
(60, 70, 80, 90)
<class 'tuple'>
100
<class 'int'>
'''

'''
#  Find  outputs
def   f1():
	x = 1
	while  x <=  100000000000000000000:
		yield  x
		x +=  1
# End of  generator
g = f1()
print('Begin')
print(*g) # memory error
print('End')
'''

'''
#  Find  outputs
g = (x * x  for  x  in  range(500000000000000000))
print(*g) # memory error
'''

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
# End  of  generator
g = f1()
for   m   in   g:
	print(m)
x ,  y ,  z  =  f1()
print(x)
print(y)
print(z)

'''


'''
# Identify  error (Home  work)
def  f1():
        yield  10
        yield  20
        yield  30
        yield  40
a , b , c = f1()
p , q , r , s , m = f1()
'''

'''
#  Find  outputs (Home  work)
def   f1():
	yield    1
	yield    2
	yield    3
# End  of  generator
g =  f1()
print(len(g)) # error no length in generator
print(g * 3)  # error
print(g[0])   # error no index in generator
print(g[1 : 3]) #  error no slice in generator
print(*g) # 1 2 3
'''
