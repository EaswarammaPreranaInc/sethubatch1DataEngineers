#Write  a  generator  to  yield  sum , difference , product  and  division  of  2  numbers
#Hint:  Use  generator  function  and  for  loop  to  retrieve  elements
def f1(a,b):
	print('Sum: ',end='')
	yield a+b
	print('Difference: ',end='')
	yield a-b
	print('Product: ',end='')
	yield a*b
	print('Division: ',end='')
	yield a/b
a=int(input("enter a number: "))
b=int(input("enter a number: "))
try:
	for x in f1(a,b):
		print(x)
except ZeroDivisionError:
	print('Divsion by 0 not permitted') 

Output:
enter a number: 5
enter a number: 6
Sum: 11
Difference: -1
Product: 30
Division: 0.8333333333333334

#Design  a  generator  to  yield  from  x (may  be  10)  to   y (may  be  20)
#Hint:  Use  generator  function  and  for  loop
#Hint:  Do  not  use  range  object
def f2(a,b):
	while a<=b:
		yield a
		a+=1
	
a=int(input("enter start number: "))
b=int(input("enter end number: "))
for x in f2(a,b):
	print(x) 
Output:
enter start number: 5
enter end number: 9
5
6
7
8
9
'''
Write  a   generator  to  generate  fibonacci  series
1) What  is  fibonacci  series ?  --->  0 , 1 , 1 , 2 , 3 , 5 , 8 , .....
2) What  is  the  formula  for  10th  term ?  ---> 9th  term + 8th  term
    What  is  the  formula  for  3rd  term ?  ---> 2nd  term + 1st  term
3) What  are  the  first  two  terms ?  ---> 0  and  1
4) Use  generator  function  and  for  loop
'''
def fib(i):
	a,b=0,1
	while a<=i:
		yield  a
		a,b=b,a+b
i=int(input("Fibonnaci series until some number: "))
for x in fib(i):
	print(x) 

Output:
Fibonnaci series until some number: 5
0
1
1
2
3
5
'''
Write  a  generator  to  divide  a  string  into  words
Hint1:  Use  generator  function  and  for   loop
Hint2:  Use  split()  method  of  str  class
''' 
def words(x):
	a=x.split()
	for x in a:
		yield x
x=input("Enter a String: ")
for x in words(x):
	print(x) 

Output:
Enter a String: kjs kjsff kjdsf hth
kjs
kjsff
kjdsf
hth

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

Output:
[10, 20]
<class 'list'>
{40, 50, 30}
<class 'set'>
(60, 70, 80, 90)
<class 'tuple'>
100
<class 'int'>

# Find  outputs
def   f1():
	x = 1
	while  x <=  100000000000000000000:
		yield  x
		x +=  1
# End of  generator
g = f1()
print('Begin')
print(*g)
print('End')

#  Find  outputs
g = (x * x  for  x  in  range(500000000000000000))
print(*g)

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

Output:
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

# Identify  error (Home  work)
def  f1():
        yield  10
        yield  20
        yield  30
        yield  40
# a , b , c = f1(), ValueError
# p , q , r , s , m = f1(), ValueError

#  Find  outputs (Home  work)
def   f1():
	yield    1
	yield    2
	yield    3
# End  of  generator
g =  f1()
#print(len(g))
#print(g * 3)
#print(g[0])
#print(g[1 : 3])
print(*g)

Output:
1 2 3
