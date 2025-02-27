'''
(Home  work)
Write  a  program  to  determine  area  and  perimeter  of  rectangle

1) What  are  the  inputs ?  ---> length  and   breadth

2) What  are  the  outputs  ?  --->  area  and  perimeter

3) What  is  the  area  of  rectangle  ?  --->  length * breadth

4) What  is  the  perimeter  of  rectangle ?  --->  2 * (length + breadth)
'''


a = float(input('enter length of rectangle : '))
b = float(input('enter breath of rectangle : '))
area  = a*b
perimeter = 2*(a+b)
print('Area',area)
print('perimeter',perimeter)
# output:
# enter length of rectangle : 12
# enter breath of rectangle : 23
# Area 276.0
# perimeter 70.0

'''
(Home  work)
Write  a  program  to  determine  volume  of  a  sphere

1) What  is  the  input ?  --->  radius

2) What  is  the  output ?  --->  volume

3) What  is  the  volume  of  sphere  ?  --->  4 / 3  * pi *  r ^ 3
'''

import math
try:
 a = float(input('Enter radius : '))
 a = 4/3 *math.pi*a**3
 print(F'volume : {a:.2f}')
except:
    print("Please enter integer number")
# output:
# Enter radius : 24
# volume : 57905.84

'''
(Home  work)
Write  a  program  to  determine  simple  interest  and  compound  interest

1) What  are  the  inputs  ?  --->  principle , time  and   rate  of  interest

2) What  are  the  outputs ? --->  Simple  interest   and   compound  interest

3) What  is  simple  interest  formula ?  ---> ptr / 100

4) What  is  compound  interest  formula ?  --->  p * (1  +  r  /  100) ^  t  -  p
'''
P = float(input('Enter principle : '))
T = float(input("Enter time : "))
R = float(input("Enter rate of interest : "))
SI = (P * R * T) / 100
A = P * (1 + R / 100) ** T
CI = A - P
print('Simple Interest : ',SI)
print(F'Compound Interest : {CI:.2f}')
# output:
# Enter principle : 12
# Enter time : 2
# Enter rate of interest : 5.7
# Simple Interest :  1.368
# Compound Interest : 1.41

'''
(Home  work)
Write  a  program  to  swap  values  of  two  objects  using  3rd   object

Let  x = 10  and  y = 25
What  are  the  values  of  x  and  y  after  swap ?  --->  x = 25  and   y = 10
'''
x = int(input("Enter integer : "))
y = int(input("Enter integer : "))
print(F'Before swap: {x = } | {y = }')
temp = x
x = y
y = temp
print(F'After swap: {x = } | {y = }')
# output:
# Enter integer : 12
# Enter integer : 23
# Before swap: x = 12 | y = 23
# After swap: x = 23 | y = 12
'''
(Home  work)
Write  a  program  to  swap  values  of  two  objects  without  using  3rd  object

Hint: One  addition  and  two  subtractions

x = -200
y =  100
'''
x = int(input("Enter integer number: "))
y = int(input("Enter integer number: "))
print(F'Before swapping : {x = } {y = }')
x = x-y
y = x+y
x = y-x
print(F'After swapping : {x = } {y = }')
# output:
# Enter integer number: 12
# Enter integer number: 29
# Before swapping : x = 12 y = 29
# After swapping : x = 29 y = 12

'''
(Home  work)
Write  a  program  to  swap  values  of  two  objects  without  using  3rd  object

Hint: One  multiplication  and  two  divisions

x =  25
y =  10
'''
x = int(input("Enter integer number: "))
y = int(input("Enter integer number: "))
print(F'Before swapping : {x = } {y = }')
x = x/y
y = int(y*x)
x = int(y/x)
print(F'After swapping : {x = } {y = }')
# output:
# Enter integer number: 19
# Enter integer number: 99
# Before swapping : x = 19 y = 99
# After swapping : x = 99 y = 19

'''
Write  a  program  to  add ,  subtract , multiply  and  divide  two  complex  numbers


'''
try:
    x = complex(input("Enter 1st complex number: "))
    y = complex(input("Enter 2nd complex number: "))
    add = x+y
    sub = x-y
    mult = x*y
    div = x/y
    print("Addition : ",add)
    print("Subtraction: ",sub)
    print("Multiplication : ",mult)
    print("Division : ",div)
except:
    print("please enter complex number")
# output:
# Enter 1st complex number: 3+4j
# Enter 2nd complex number: 10+9j
# Addition :  (13+13j)
# Subtraction:  (-7-5j)
# Multiplication :  (-6+67j)
# Division :  (0.3646408839779005+0.07182320441988949j)


'''
Write  a  program  to  determine  sum , difference , product , quotient , largest  and  smallest  of  two  numbers.
Also  find  remainder,  sqrt  of  first  input , power, gcd  and  factorial  of  first  input

Hint:  Use  F  string  to  print  results
'''
import math

x = int(input("Enter 1st number: "))
y = int(input("Enter 2nd number: "))
add = x+y
sub = x-y
mult = x*y
div = x/y
mod = x%y
max = max(x,y)
min = min(x,y)
pow = pow(x,y)
sqrt_x = math.sqrt(x)
sqrt_y = math.sqrt(y)
gcd = math.gcd(x,y)
fact_x = math.factorial(x)
fact_y = math.factorial(y)
print(F"Addition : {add}")
print(F"Subtraction: {sub}")
print(F"Multiplication : {mult}")
print(F"Division : {div:.2f}")
print(F"Module : {mod}")
print(F"Max of x,y : {max}")
print(F"Min of x,y : {min}")
print(F"Power of x^y: {pow}")
print(F"Square root of {x}:{sqrt_x}")
print(F"Square root of {y}:{sqrt_y}")
print(F"Gcd : ",gcd)
print(F"Factorial of {x}:{fact_x}")
print(F"Factorial of {y}:{fact_y}")
# output:
# Enter 1st number: 4
# Enter 2nd number: 9
# Addition : 13
# Subtraction: -5
# Multiplication : 36
# Division : 0.44
# Module : 4
# Max of x,y : 9
# Min of x,y : 4
# Power of x^y: 262144
# Square root of 4:2.0
# Square root of 9:3.0
# Gcd :  1
# Factorial of 4:24
# Factorial of 9:362880


'''
Write  a  program  to  swap  values  of  any  two  objects  in  a  single  statement  without  using  3rd  object

Let  'x'  be  25  and  'y'  be   'Hyd'
What  are  'x'  and  'y'  after  swap ?  --->  Hyd  and  25

Hint:  Swap  references  but  not  objects
'''
x = eval(input("Enter 1st value : "))
y = eval(input("Enter 2nd value : "))
print(F"Before swapping : {x=} | {y=}")
x,y=y,x
print(F"After swapping : {x=} | {y=}")
# output:
# Enter 1st value : 25
# Enter 2nd value : "Hyd"
# Before swapping : x=25 | y='Hyd'
# After swapping : x='Hyd' | y=25


'''
Write  a  program  to  determine  largest  of  two  inputs  without  using  max()  function

1) What  is  the  output  if  inputs  are  10  and  20 ?   ---> 20

2) What  is   the  output  if  inputs  are  35.8  and  27.9 ?  ---> 35.8

3) What  is  the  output  if  inputs  are  'RAMA'  and  'RAJESH' ?  --->  'RAMA'  becoz  'M' > 'J'

4) What  is  the  output  if  inputs  are  [10 , 20 , 15 , 18 , 19 , 28]  and  [10 , 20 , 25, 17] ?   --->  [10 , 20 , 25 , 17]  becoz  25 > 15

5) Use   ternary  operator
'''
x = eval(input("Enter 1st value : "))
y = eval(input("Enter 2nd value : "))
max = x if x>y else y
print("Maximum of x and y : ",  max)
# output:
# Enter 1st value : [10 , 20 , 15 , 18 , 19 , 28]
# Enter 2nd value : [10 , 20 , 25, 17]
# Maximum of x and y :  [10, 20, 25, 17]


'''
Write  a  program  to  determine  largest  of  three  inputs  without  using  max()  function

1) What  is  the  output  if  inputs  are  10 , 20  and  15 ?   --->  20

2) What  is  the  output  if  inputs  are  35.8 , 42.8  and  27.9 ?   ---> 42.8

3) What  is  the  output  if  inputs  are  'RAMA'  , 'RAKESH'  and  'RAJESH' ?   --->  'RAMA'

4) What  is   the  output  if  inputs  are  [10 , 20 , 15 , 18]  , [10 , 20 , 32, 19]  and  [10 , 20 , 25, 17] ?  --->  [10 , 20 , 32 , 19]

5) Use  nested  ternary  operator
'''
x = eval(input("Enter 1st value : "))
y = eval(input("Enter 2nd value : "))
z = eval(input("Enter 3rd value : "))
max = x if x>y and x>z else y if y>x and y>z else z
print("Maximum of x,y and z :",max)

# output:
# Enter 1st value : 30
# Enter 2nd value : 9010
# Enter 3rd value : 10000000000
# Maximum of x,y and z : 10000000000

'''
Write  a  program  to  print   '>'  if  1st  input  >  2nd  input,
                                               '<'  if  1st  input  <  2nd  input  and
                                               '='  if  inputs  are  same

1) What  is  the  result  if  inputs  are  10  and  20 ?  --->  <

2) What  is  the  result  if  inputs  are  70  and  60 ?  --->  >

3) What  is  the  result  if  inputs  are  25  and  25 ?  --->  =

4) Inputs  can  be  integers , floats , strings  and  so  on

5) Use  ternary  operator
'''

x = eval(input("Enter 1st value : "))
y = eval(input("Enter 2nd value : "))
print(">" if x>y else "<" if x<y else "=")
# output:
# Enter 1st value : 30
# Enter 2nd value : 30
# =

'''
Write  a  program  to  print  1  if  input  is  +ve  ,  -1    if  input  is  -ve  and  0  if  input  is  0

1) What  is  the  result  if  input  is  -25 ?  --->  -1

2) What  is  the  result  if  input  is  75 ?  --->  1

3) What  is  the  result  if  input  is  0 ?  ---> 0

4) Use  nested  ternary  operator
'''
x = eval(input("Enter value : "))
print(1 if x>=1 else -1 if x<=-1 else 0)
# output:
# Enter value : -214311111111111111
# -1

'''
Write  a  program  to  test  input  is  even  number  or  odd  number

1) What  is  an  even  number  ?  --->  Divisible  by  2

2) What  is  an  odd  number  ?  --->  Not  divisible  by  2

3) Use  ternary  operator
'''
x = int(input("Enter value : "))
print("Even" if x%2==0 else "odd")
# output:
# Enter value : 24355555555555555555555555588
# Even
