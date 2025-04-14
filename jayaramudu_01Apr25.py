#Ex-1
'''
Write  a  generator  to  yield  sum , difference , product  and  division  of  2  numbers

Hint:  Use  generator  function  and  for  loop  to  retrieve  elements
'''
from time import sleep

a = int(input('Enter   first  number  :   '))
b = int(input('Enter   second  number  :   '))

def fun(x,y):
    yield  'Sum: '+str(x+y)
    yield  'Difference: '+str(x-y)
    yield  'Product:  '+ str(x*y)
    try:
        yield 'Division '+str(x/y)
    except ZeroDivisionError:
        yield 'Division  by zero  is not  permitted'
for i in fun(a,b):
    print(i)
    sleep(1)

#Ex-2
'''
Design  a  generator  to  yield  from  x (may  be  10)  to   y (may  be  20)

Hint:  Use  generator  function  and  for  loop

Hint:  Do  not  use  range object
'''
from time import sleep

a = int(input('Enter   start  value  :   '))
b = int(input('Enter   end  value  :   '))
def fun(x,y):
    n = x
    while n <= y:
        yield n
        n = n+1
for i in fun(a,b):
    print(i)
    sleep(1)

#Ex-3
'''
Write  a   generator  to  generate  fibonacci  series

1) What  is  fibonacci  series ?  --->  0 , 1 , 1 , 2 , 3 , 5 , 8 , .....

2) What  is  the  formula  for  10th  term ?  ---> 9th  term + 8th  term
    What  is  the  formula  for  3rd  term ?  ---> 2nd  term + 1st  term

3) What  are  the  first  two  terms ?  ---> 0  and  1

4) Use  generator  function  and  for loop
'''
from time import sleep

n = int(input('What  is  the  last  value : '))

def fun(x):

    a = 0
    b = 1
    c = a + b
    yield a
    yield b
    while c < x:

        yield c
        a = b
        b = c
        c = a + b
for i in fun(n):
    if n==0:
        break
    print(i)

    sleep(1)



#Ex-4
'''
Write  a  generator  to  divide  a  string  into  words

Hint1:  Use  generator  function  and  for   loop

Hint2:  Use  split()  method  of str class
'''
from time import sleep

from time import sleep

s = input('Enter any string: ')

def fun(string):
    words = string.split()
    for word in words:
        yield word
for word in fun(s):
    print(word)
    sleep(1)
#Ex-1
# Find  outputs
def   f1():
        yield   [10 , 20]
        yield  {30 , 40 , 50}
        yield  60  , 70 , 80 , 90
        yield  100
# End  of  generator
g = f1() # creates empty generator
for   x   in   g:
	print(x)          # [10 , 20]       # {30 , 40 , 50}   # 60  , 70 , 80 , 90   # 100
	print(type(x))    # class list     # class set         # class tuple          # class int

#Ex-2
#  Find  outputs
def   f1():
	x = 1
	while  x <=  100000000000000000000:
		yield  x
		x +=  1
# End of  generator
g = f1()          # creates empty generator
print('Begin')    # Begin
# print(*g)  # Error occur MemoryError
print('End') # End

#Ex-3
#  Find  outputs
g = (x * x  for  x  in  range(500000000000000000))
print(*g) #  Error occur MemoryError

#Ex-4
#  Find    outputs (Home  work)
def      f1():
	print('One') # one  # One
	yield    1
	print('Two') # Two  # Two
	yield    2
	print('Three') # Three  # Three
	yield    3
	print('End')    # End    # End
# End  of  generator
g = f1() # Error  creates empty generator
for   m   in   g:  # m =  1    # m = 2         # m = 3
	print(m)      # 1          # 2              # 3
x ,  y ,  z  =  f1() #  (1,2,3)
print(x) # 1
print(y) # 2
print(z) # 3


#Ex-5
# Identify  error (Home  work)
def  f1():
        yield  10
        yield  20
        yield  30
        yield  40
# a , b , c = f1() #  fun return 4 elements but 3
# p , q , r,s,m = f1() # excepted 5 but 4

#Ex-6
#  Find  outputs (Home  work)
def   f1():
	yield    1
	yield    2
	yield    3
# End  of  generator
g =  f1() # creates empty object
#print(len(g)) # Error because len method not in generator
# print(g * 3) # Error because generator  not repeated
#print(g[0]) # generator doesn't have random access
#print(g[1:3])  # there is no slicing generator
print(*g) # unpack generator 1 2 3

