program1:
Write  a  generator  to  yield  sum , difference , product  and  division  of  2  numbers
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

program2:
Design  a  generator  to  yield  from  x (may  be  10)  to   y (may  be  20)
def f1(x,y):
	while x<=y:
		yield x
		x=x+1
x=int(input('enter start value : '))
y=int(input('enter end value : '))
g=f1(x,y)
for i in g:
	print(i)

program3:
Write  a   generator  to  generate  fibonacci  series
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

program4:
Write  a  generator  to  divide  a  string  into  words
def f1(s):
	a=s.split()
	yield a
s=input('Enter  any   string : ')
print('words in string')
g=f1(s)
for i in g:
	for j in i:
		print(j)

program5:
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

output:
[10, 20]
<class 'list'>
{40, 50, 30}
<class 'set'>
(60, 70, 80, 90)
<class 'tuple'>
100
<class 'int'>

program6:
def   f1():
	x = 1
	while  x <=  100000000000000000000:
		yield  x
		x +=  1
# End of  generator
g = f1()
print('Begin')#Begin
print(*g)
print('End')

program6:
def f1():
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
output:
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

program7:
def  f1():
        yield  10
        yield  20
        yield  30
        yield  40
a , b , c = f1()#error
p , q , r , s , m = f1()#error

program8:
def   f1():
	yield    1
	yield    2
	yield    3
# End  of  generator
g =  f1()
print(len(g))#error
print(g * 3)#error
print(g[0])#error
print(g[1 : 3])#error
print(*g)#123

