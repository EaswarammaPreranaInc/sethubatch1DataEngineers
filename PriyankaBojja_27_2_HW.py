'''
PROGRAM 1
(Home  work)
Write  a  program  to  determine  area  and  perimeter  of  rectangle

1) What  are  the  inputs ?  ---> length  and   breadth

2) What  are  the  outputs  ?  --->  area  and  perimeter

3) What  is  the  area  of  rectangle  ?  --->  length * breadth

4) What  is  the  perimeter  of  rectangle ?  --->  2 * (length + breadth)

sample OP
Enter  length  of  rectangle  : 4
Enter  breadth  of  rectangle :  5
Area  :  20.00
Perimeter :  18.00
'''

a= float(input('Enter length of rectangle : '))
b= float(input('Enter breadth of rectangle : '))
Area = a * b
Perimeter = 2*(a+b)
print('Area : ', Area)
print('Perimeter : ',Perimeter)


'''
PROGRAM 2
(Home  work)
Write  a  program  to  determine  volume  of  a  sphere

1) What  is  the  input ?  --->  radius

2) What  is  the  output ?  --->  volume

3) What  is  the  volume  of  sphere  ?  --->  4 / 3  * pi *  r ^ 3

sample OP
Enter  radius  :  3.5
Volume  :  179.59
'''
import math
r = float(input('Enter radius : '))
Volume = 4/3 * (math.pi) * r ** 3
print(f'Volume of Sphere : {Volume:.2f}')



'''
PROGRAM 3
(Home  work)
Write  a  program  to  determine  simple  interest  and  compound  interest

1) What  are  the  inputs  ?  --->  principle , time  and   rate  of  interest

2) What  are  the  outputs ? --->  Simple  interest   and   compound  interest

3) What  is  simple  interest  formula ?  ---> ptr / 100

4) What  is  compound  interest  formula ?  --->  p * (1  +  r  /  100) ^  t  -  p

sample OP
Enter  principle  :  10000
Enter  time  : 3
Enter  rate  of  interest :  7.5
Simple  Interest : 2250.00
Compound  Interest : 2422.97
'''
P = float(input('Enter Principle : '))
T = float(input('Enter Time : '))
R = float(input('Enter Rate of Interest : '))
SI = P *T *R / 100
CI = P*((1+R)/100)**T - P
print(f'Simple Interest : {SI:.2f}')
print(f'Compound Interest :  {CI:.2f}')



'''
PROGRAM 4
(Home  work)
Write  a  program  to  swap  values  of  two  objects  using  3rd   object

Let  x = 10  and  y = 25
What  are  the  values  of  x  and  y  after  swap ?  --->  x = 25  and   y = 10

sample OP
Enter  1st  input  : 10
Enter  2nd  input  : 25
Before  swap :  x=10      y=25
After  swap :  x=25       y=10
'''
try:
 x = float(input('Enter 1st input : '))
 y = float(input('Enter 2nd input : '))
 print('Before swap : ',x,y)
 temp = x
 x = y
 y = temp
 print('After swap : ',x,y)
except:
 print('Input must be int or float')


'''
PROGRAM 5
(Home  work)
Write  a  program  to  swap  values  of  two  objects  without  using  3rd  object

Hint: One  addition  and  two  subtractions

x = -200
y =  100

sample OP
Enter  1st  input  : 100
Enter  2nd  input  : -200
Before  swap :  x=100.0           y=-200.0
After  swap :  x=-200.0           y=100.0
'''

try:
 x = float(input('Enter 1st input : '))
 y = float(input('Enter 2nd input : '))
 print('Before swap : ',x,y)
 x =x+y
 y=x-y
 x =x-y
 print('After swap : ',x,y)
except:
 print('Input must be int or float')



'''
PROGRAM 6
(Home  work)
Write  a  program  to  swap  values  of  two  objects  without  using  3rd  object

Hint: One  multiplication  and  two  divisions

sample OP
x =  25
y =  10
'''

try:
 x = float(input('Enter 1st input : '))
 y = float(input('Enter 2nd input : '))
 print('Before swap : ',x,y)
 x =x*y
 y=x/y
 x =x/y
 print('After swap : ',x,y)
except:
 print('Input must be int or float')


'''
PROGRAM 7
Write  a  program  to  add ,  subtract , multiply  and  divide  two  complex  numbers

Let  first  input   be  3 + 4j  and  second  input  be   5 + 6j
What  is  the  sum ? --->  (3 + 4j) + (5 + 6j) =  8 + 10j
What  is  the  difference ?  --->  (3 + 4j) - (5 + 6j) =  -2 - 2j
What  is  the  product ?  --->  (3 + 4j) * (5 + 6j) =  15 + 18j + 20j - 24 = -9 + 38j
What  is  the  division ?  --->  (3 + 4j) / (5 + 6j)  =  (3 + 4j) * (5 - 6j) / (5 + 6j)  * (5 - 6j)
												=  (15 - 18j + 20j + 24) / (25 + 36)
												=   39 / 61  + 2j / 61

sample OP
Enter first complex number : 3+4j
Enter second complex number: 5+6j
Sum :  (8+10j)
Difference :  (-2-2j)
Product:  (-9+38j)
Division :  (0.6393442622950819+0.03278688524590165j)
'''

try:
	a = complex(input('Enter first complex number : '))
	b = complex(input('Enter second complex number : '))
	print('Sum : ',a+b)
	print('Difference : ',a-b)
	print('Product : ',a*b)
	print('Division : ', a/b)
except:
	print('input must me complex number')



'''
PROGRAM 8
Write  a  program  to  determine  sum , difference , product , quotient , largest  and  smallest  of  two  numbers.
Also  find  remainder,  sqrt  of  first  input , power, gcd  and  factorial  of  first  input

Hint:  Use  F  string  to  print  results

sample OP
Enter 1st  integer  number :  10
Enter 2nd  integer  number :  7
10 + 7 = 17
10 - 7 = 3
10 * 7 = 70
10 / 7 = 1.4285714285714286
10 % 7 = 3
max(10 , 7) = 10
min(10 , 7) = 7
10 ^ 7 = 10000000
sqrt(10) = 3.1622776601683795
gcd(10 , 7) = 1
fact(10) = 3628800
'''

from math import *
a = eval(input('Enter 1st integer number: '))
b = eval(input('Enter 2nd integer number: '))
print(f'{a} + {b} = {a+b}')
print(f'{a} - {b} = {a-b}')
print(f'{a} * {b} = {a*b}')
print(f'{a} / {b} = {a/b}')
print(f'Max({a},{b}) = {max(a,b)}')
print(f'Min({a},{b}) = {min(a,b)}')
print(f'sqrt({a}) = {sqrt(a)}')
print(f'{a}^{b} = {pow(a,b)}')
print(f'gcd({a},{b}) = {gcd(a,b)}')
print(f'fact({a}) = {factorial(a)}')



'''
PROGRAM 9
Gift
Write  a  program  to  swap  values  of  any  two  objects  in  a  single  statement  without  using  3rd  object

Let  'x'  be  25  and  'y'  be   'Hyd'
What  are  'x'  and  'y'  after  swap ?  --->  Hyd  and  25

Hint:  Swap  references  but  not  objects


sample OP
Enter  1st  input :  25
Enter  2nd  input : Hyd
Before  swap :  x='25'            y='Hyd'
After  swap :  x='Hyd'            y='25'

'''

x = input('Enter 1st input : ')
y = input('Enter 2nd input : ')
print('Before swap : ',x,y)
x,y = y,x
print('After swap : ',x,y)


'''
PROGRAM 10
Write  a  program  to  determine  largest  of  two  inputs  without  using  max()  function

1) What  is  the  output  if  inputs  are  10  and  20 ?   ---> 20

2) What  is   the  output  if  inputs  are  35.8  and  27.9 ?  ---> 35.8

3) What  is  the  output  if  inputs  are  'RAMA'  and  'RAJESH' ?  --->  'RAMA'  becoz  'M' > 'J'

4) What  is  the  output  if  inputs  are  [10 , 20 , 15 , 18 , 19 , 28]  and  [10 , 20 , 25, 17] ?   --->  [10 , 20 , 25 , 17]  becoz  25 > 15

5) Use   ternary  operator

sample OP
Enter 1st input : 'Rama'
Enter 2nd input : 'Rajesh'
Largest  Input  :   Rama

'''

a = input('Enter 1st input: ')
b = input('Enter 2nd input: ')
Max = a if a>b else b
print('Largest Input: ',Max)


'''
PROGRAM 11
Write  a  program  to  determine  largest  of  three  inputs  without  using  max()  function

1) What  is  the  output  if  inputs  are  10 , 20  and  15 ?   --->  20

2) What  is  the  output  if  inputs  are  35.8 , 42.8  and  27.9 ?   ---> 42.8

3) What  is  the  output  if  inputs  are  'RAMA'  , 'RAKESH'  and  'RAJESH' ?   --->  'RAMA'

4) What  is   the  output  if  inputs  are  [10 , 20 , 15 , 18]  , [10 , 20 , 32, 19]  and  [10 , 20 , 25, 17] ?  --->  [10 , 20 , 32 , 19]

5) Use  nested  ternary  operator

sample OP
Enter 1st input : [10,20,15,18]
Enter 2nd input : [10,20,32,19]
Enter 3rd input : [10,20,25,17]
Largest  Input  :  [10, 20, 32, 19]
'''
a = input('Enter 1st input: ')
b = input('Enter 2nd input: ')
c = input('Enter 3rd input: ')
Max = a if a>b else (b if b>c else c)
print('Max is: ',Max)



'''
PROGRAM 12
Write  a  program  to  print   '>'  if  1st  input  >  2nd  input,
                                               '<'  if  1st  input  <  2nd  input  and
                                               '='  if  inputs  are  same

1) What  is  the  result  if  inputs  are  10  and  20 ?  --->  <

2) What  is  the  result  if  inputs  are  70  and  60 ?  --->  >

3) What  is  the  result  if  inputs  are  25  and  25 ?  --->  =

4) Inputs  can  be  integers , floats , strings  and  so  on

5) Use  ternary  operator

sample OP
Enter 1st input : 10
Enter 2nd input : 20
Result :   <
'''
a = eval(input('Enter 1st input: '))
b = eval(input('Enter 2nd input: '))
Result = '>' if a>b else('<' if a<b else '=')
print('Result: ',Result)




'''
PROGRAM 13
Write  a  program  to  print  1  if  input  is  +ve  ,  -1    if  input  is  -ve  and  0  if  input  is  0

1) What  is  the  result  if  input  is  -25 ?  --->  -1

2) What  is  the  result  if  input  is  75 ?  --->  1

3) What  is  the  result  if  input  is  0 ?  ---> 0

4) Use  nested  ternary  operator

sample OP
Enter any number : -25
Result :  -1
'''
a = int(input('Enter any number: '))
Result = 1 if a>0 else(-1 if a<0 else 0)
print('Result: ',Result)



'''
PROGRAM 14
Write  a  program  to  test  input  is  even  number  or  odd  number

1) What  is  an  even  number  ?  --->  Divisible  by  2

2) What  is  an  odd  number  ?  --->  Not  divisible  by  2

3) Use  ternary  operator

'''

a = int(input('Enter any postive integer: '))
res = 'Even number' if a%2==0 else 'odd number'
print(res)