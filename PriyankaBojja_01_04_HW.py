Q1 #Write  a  generator  to  yield  sum , difference , product  and  division  of  2  numbers

import time
def f1():
	yield f'Sum : {a+b}'
	yield f'Difference : {a-b}'
	yield f'Product : {a*b}'
	try:
		yield f'Division : {a/b}'
	except:
		print('Division by zero is not permitted')
a=int(input('Enter first number : '))
b=int(input('Enter second number : '))
g=f1()
for x in g:
	print(x)
	time.sleep(2)

OP-
Enter first number : 2
Enter second number : 0
Sum : 2
Difference : 2
Product : 0
Division by zero is not permitted
#---------------------------------------------------------------------------------------------------------------------
Q2 #Design  a  generator  to  yield  from  x (may  be  10)  to   y (may  be  20)
#Hint:  Use  generator  function  and  for  loop
#Hint:  Do  not  use  range  object

import time
def f1(a,b):
	while a<=b:
		yield a
		a+=1
a=int(input('Enter start value : '))
b=int(input('Enter end value : '))
g=f1(a,b)
for x in g:
	print(x)
	time.sleep(2)

Enter start value : 62
Enter end value : 69
62
63
64
65
66
67
68
69
#-------------------------------------------------------------------------------------------
Q3 #Write  a   generator  to  generate  fibonacci  series

import time
def f1(i):
	a=0
	yield a
	b=1
	yield b
	c=a+b
	while c<i:
		yield c
		a=b
		b=c
		c=a+b
i=int(input('Enter last value : '))
g=f1(i)
for x in g:
	print(x)
	if i==0:
		break
	time.sleep(2)

OP-
Enter last value : 5
0
1
1
2
3
#---------------------------------------------------------------------------------
Q4 #Write  a  generator  to  divide  a  string  into  words

import time
def f1(a):
	l=a.split()
	for w in l:
		yield w
a=input('Enter string: ')
g=f1(a)
print('Words of string')
for x in g:
	print(x)
	time.sleep(1)

OP-
Enter string: Iam Priyanka
Words of string
Iam
Priyanka
#-------------------------------------------------------
Q5 # Find  outputs
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

OP-
[10, 20]
<class 'list'>
{40, 50, 30}
<class 'set'>
(60, 70, 80, 90)
<class 'tuple'>
100
<class 'int'>
#---------------------------------------------------------
Q6 #Find  outputs
def   f1():
	x = 1
	while  x <=  100000000000000000000:
		yield  x
		x +=  1
# End of  generator
g = f1()
print('Begin') #Begin
print(*g)       #Memory error
print('End')   #End

#---------------------------------------------------------------
Q7 #Find  outputs
g = (x * x  for  x  in  range(500000000000000000))
print(*g)  #Memory error
#-----------------------------------------------------------
Q8 #Find    outputs (Home  work)

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

OP-
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
#--------------------------------------------------------------
Q9 #Identify  error (Home  work)
def  f1():
        yield  10
        yield  20
        yield  30
        yield  40
#a , b , c = f1()   #error - less number of values to unpack
#p , q , r , s , m = f1()  #error - morenumber of values to unpack
#----------------------------------------------------------
Q10 #Find  outputs (Home  work)
def   f1():
	yield    1
	yield    2
	yield    3
# End  of  generator
g =  f1()
#print(len(g)) # error - len argument must be sequence
#print(g * 3)   # error- generator cannot be repeated
#print(g[0])     #error - generator is not indexed
#print(g[1 : 3])  #error - cannot slice generator due to not indexed
print(*g)     # 1 2 3 