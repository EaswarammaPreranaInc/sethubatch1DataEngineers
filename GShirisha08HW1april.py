#generator to yield sum, difference, product and division of 2 numbers
def f1(x,y):
	try:
		yield F'Sum: {x+y}'
		yield F'Difference: {x-y}'
		yield F'Product: {x*y}'
		yield F'Division: {x/y}'
	except ZeroDivisionError:
		yield 'Division by zero is not permitted'
a=int(input('Enter first number : '))
b=int(input('Enter second number : '))
for i in f1(a,b):
	print(i)

#Output
Enter first number : 10
Enter second number : 3
Sum: 13
Difference: 7
Product: 30
Division: 3.3333333333333335

Enter first number : 3
Enter second number : 0
Sum: 3
Difference: 3
Product: 0
Division by zero is not permitted

#generator to yield from x(may be 10) to y(may be 20)
g=(x for x in range(a,b+1))
for i in g:
	print(i)


#Output
Enter start value: 5
Enter end value: 10
5
6
7
8
9
10

#generate fibonacci series using generator
def fib(n):
    a,b=0,1
    for i in range(n):
        yield a
        a,b=b,a+b
n=int(input('What is the last value : '))
for x in fib(n):
	if(x>n):
		break
	print(x)

#Output
What is the last value : 10
0
1
1
2
3
5
8

#divide a string into words using generator
s=input('Enter any string: ')
def gen(x):
	l=s.split(' ')
	for x in l:
		yield x
print(*gen(s),end='\n')

#Output
Enter any string: hi hey
hi
hey

#Find outputs
def f1():
	yield [10,20]
	yield {30,40,50}
	yield 60,70,80,90
	yield 100
# End of generator
g = f1()
for x in g:
	print(x) 
	print(type(x))

#Output
[10, 20]
<class 'list'>
{40, 50, 30}
<class 'set'>
(60, 70, 80, 90)
<class 'tuple'>
100
<class 'int'>

#Find outputs
def f1():
	x = 1
	while x<=100000000000000000000: #Range is large
		yield x
		x+=1
#End of generator
g = f1()
print('Begin')
print(*g)
print('End')

#Find outputs
g=(x*x for x in range(500000000000000000))
print(*g) #takes too much time and space

#Find outputs 
def f1():
	print('One')
	yield 1
	print('Two')
	yield 2
	print('Three')
	yield 3
	print('End')
g=f1()
for m in g:
	print(m)
x,y,z=f1()
print(x)
print(y)
print(z)

#Outputs
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


#Identify  error 
def f1():
        yield 10
        yield 20
        yield 30
        yield 40
a,b,c=f1() #Error (less no of references)
p,q,r,s,m=f1() #Error (more no of references)

#Find  outputs 
def f1():
	yield 1
	yield 2
	yield 3
g=f1()
print(len(g)) #Error
print(g*3) #Error
print(g[0]) #Error
print(g[1:3]) #Error
print(*g) #1 2 3
