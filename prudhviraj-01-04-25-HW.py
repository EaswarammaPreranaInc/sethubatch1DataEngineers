'''
Write  a  generator  to  yield  sum , difference , product  and  division  of  2  numbers

Hint:  Use  generator  function  and  for  loop  to  retrieve elements
'''
try:
	import time
	a=int(input("Enter the First number: "))
	b=int(input("Enter the Second number: "))
	def cal():
		for i in range(1):
			yield a+b
			time.sleep(1)
			yield a-b
			time.sleep(1)
			yield a*b
			time.sleep(1)
			yield a/b
	operations = ["Sum:", "Difference:", "Product:", "Division:"]
	generator = cal()
	for i in range(4):
		print(operations[i], next(generator))
except ZeroDivisionError:
	print("Division  by zero  is not permitted")
"""
Output:
Enter the First number: 10
Enter the Second number: 0
Sum: 10
Difference: 10
Product: 0
Division  by zero  is not permitted


Enter the First number: 10
Enter the Second number: 7
Sum: 17
Difference: 3
Product: 70
Division: 1.4285714285714286

"""

'''
Design  a  generator  to  yield  from  x (may  be  10)  to   y (may  be  20)

Hint:  Use  generator  function  and  for  loop

Hint:  Do  not  use  range  object
'''
import time
a=int(input("Enter the Start number: "))
b=int(input("Enter the End number: "))
def cal(a,b):
    for i in (a,b+1):
        yield i
        time.sleep(1)
g=cal(a,b)
for value in g:
    print(value)

import time
a = int(input("Enter the Start number: "))
b = int(input("Enter the End number: "))
def cal(a, b):
    c=a
    while c<=b:
        yield c
        time.sleep(1)
        c+=1
g = cal(a, b)
for value in g:
    print(value)
"""
Output:
Enter the Start number: 10
Enter the End number: 20
10
11
12
13
14
15
16
17
18
19
20
"""
'''
Write  a   generator  to  generate  fibonacci  series

1) What  is  fibonacci  series ?  --->  0 , 1 , 1 , 2 , 3 , 5 , 8 , .....

2) What  is  the  formula  for  10th  term ?  ---> 9th  term + 8th  term
    What  is  the  formula  for  3rd  term ?  ---> 2nd  term + 1st  term

3) What  are  the  first  two  terms ?  ---> 0  and  1

4) Use  generator  function  and  for  loop
'''
import time
n=int(input("Enter the number: "))
def fib(limit):
    a = 0
    b = 1
    while a<=limit:
        yield a
        a,b=b,a+b
        time.sleep(1)
g=fib(n)
for value in g:
    print(value)

"""
Output:
Enter the number: 10
0
1
1
2
3
5
8
"""
'''
Write  a  generator  to  divide  a  string  into  words

Hint1:  Use  generator  function  and  for   loop

Hint2:  Use  split()  method  of  str  class
'''
import time
n=input("Enter the String: ").split()
def string(words):
    for i in words:
        yield i
        time.sleep(1)
g=string(n)
for value in g:
    print(value)
"""
Output:
Enter the String: Hyd is green city
Hyd
is
green
city
"""

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
"""
Output:
[10, 20]
<class 'list'>
{40, 50, 30}
<class 'set'>
(60, 70, 80, 90)
<class 'tuple'>
100
<class 'int'>
"""

#  Find  outputs
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
"""
Output:
Begin
"""

#  Find  outputs
g = (x * x  for  x  in  range(500000000000000000))
print(*g)
"""
Output:
Memory Error
"""

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
"""
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
"""
