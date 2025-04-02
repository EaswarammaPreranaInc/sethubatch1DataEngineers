'''
Write  a  generator  to  yield  sum , difference , product  and  division  of  2  numbers

Hint:  Use  generator  function  and  for  loop  to  retrieve  elements
'''

import time
def f1(a,b):
    yield f'Sum : {a+b}'
    time.sleep(1)
    yield f'Difference : {a-b}'
    time.sleep(1)
    yield f'Product : {a*b}'
    time.sleep(1)
    if b==0:
           yield 'Division by zero is not permitted'
    else:
        yield f'Division : {a/b}'
        time.sleep(1)
        
a = int(input('Enter first no:'))
b = int(input('Enter Second no:'))

for results in f1(a,b):
	print(results)



'''o/p: Enter   first  number  :   10
        Enter   second  number  :   7
        Sum : 17
        Differnece :  3
        Product :  70
        Division : 1.4285714285714286
        Enter   first  number  :   10
        Enter   second  number  :   0
        Sum : 10
        Differnece :  10
        Product :  0
        Division  by zero  is  not  permitted
'''
'''
Design  a  generator  to  yield  from  x (may  be  10)  to   y (may  be  20)

Hint:  Use  generator  function  and  for  loop

Hint:  Do  not  use  range  object
'''
def f2(a,b):
     while  a<=b:
          yield a
          a = a+1
x = int(input('Enter  start  value : ')) # 10
y = int(input('Enter  end  value :'))  # 20   
for res in f2(x,y):
     print(res)       
'''o/p: Enter  start  value :  10
        Enter  end  value :  20
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
'''
'''
Write  a   generator  to  generate  fibonacci  series

1) What  is  fibonacci  series ?  --->  0 , 1 , 1 , 2 , 3 , 5 , 8 , .....

2) What  is  the  formula  for  10th  term ?  ---> 9th  term + 8th  term
    What  is  the  formula  for  3rd  term ?  ---> 2nd  term + 1st  term

3) What  are  the  first  two  terms ?  ---> 0  and  1

4) Use  generator  function  and  for  loop
'''
def fibb(a):
     x, y = 0, 1
     while x<=a:
          yield x
          x, y = y, x+y
n = int(input('What is the last value:'))  
for num in fibb(n):
     print(num)        
'''o/p: What  is  the  last  value  :  10
        0
        1
        1
        2
        3
        5
        8
'''
'''
Write  a  generator  to  divide  a  string  into  words

Hint1:  Use  generator  function  and  for   loop

Hint2:  Use  split()  method  of  str  class
'''
def string(a):
       for word in a.split():
              yield word
txt = input('Enter any string: ')
print('Words of string: ')
for res in string(txt):
       print(res)              
'''
o/p:Enter  any   string  :  Hyd is green city
    Words  of  the  string
    Hyd
    is
    green
    city'''
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
'''o/p: [10,20]
        <class 'list'>
        {30,40,50}
        <class 'set'>
        (60,70,80,90)
        <class  'tuple'>
        100
        <class 'int'>'''
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
'''o/p: Begin
        Memory Error becoz of stack is full'''
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
g = f1() # Empty generator is created
for   m   in   g:
	print(m) # One <next line> 1 <next line> Two <next line> 2 <next line> Three <next line> 3 <next line> End
x ,  y ,  z  =  f1() # One <next line> Two <next line> Three <next line> End 
print(x) # 1
print(y) # 2
# Identify  error (Home  work)
def  f1():
        yield  10
        yield  20
        yield  30
        yield  40
a , b , c = f1() # Error becoz the values are more than the variables
p , q , r , s , m = f1() # Error becoz no of variables are more than the objts/values
#  Find  outputs (Home  work)
def   f1():
	yield    1
	yield    2
	yield    3
# End  of  generator
g =  f1() # Empty generator is created
print(len(g)) # Error becoz there is no len function for generator
print(g * 3) # Error due to no repetation for generator
print(g[0]) # Error due to no indexing for generator
print(g[1 : 3]) # Error becoz of no indexing there also no slicing 
print(*g) # 1 2 3
