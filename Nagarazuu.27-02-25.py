'''
(Home  work)
Write  a  program  to  determine  area  and  perimeter  of  rectangle

1) What  are  the  inputs ?  ---> length  and   breadth

2) What  are  the  outputs  ?  --->  area  and  perimeter

3) What  is  the  area  of  rectangle  ?  --->  length * breadth

4) What  is  the  perimeter  of  rectangle ?  --->  2 * (length + breadth)
'''

length=eval(input('Enter a length: '))
breadth=eval(input('Enter a breadth: '))
area = length*breadth
perimeter = 2*(length+breadth)
print("area      : {:.2f}".format(area))
print("perimeter : {:.2f}".format(perimeter))

'''Write  a  program  to  determine  volume  of  a  sphere

1) What  is  the  input ?  --->  radius

2) What  is  the  output ?  --->  volume

3) What  is  the  volume  of  sphere  ?  --->  4 / 3  *pi*r^3

import math
radius = eval(input('Enter of radius: '))
volume = 4/3*math.pi*(radius ** 3)
print("Volume: {:.2f}".format(volume))'''

'''Write  a  program  to  determine  simple  interest  and  compound  interest

1) What  are  the  inputs  ?  --->  principle , time  and   rate  of  interest

2) What  are  the  outputs ? --->  Simple  interest   and   compound  interest

3) What  is  simple  interest  formula ?  ---> ptr / 100

4) What  is  compound  interest  formula ?  --->  p * (1  +  r  /  100)^t-p'''


'''principle = eval(input('Enter a principle: '))
time = eval(input('Enter a time: '))
intrest = eval(input('Enter of rate: '))
SI = (principle * time * intrest) / 100
CI = principle * ((1+intrest/100)** time) - principle
print(SI)
print(CI)'''

'''
(Home  work)
Write  a  program  to  swap  values  of  two  objects  using  3rd   object

Let  x = 10  and  y = 25
What  are  the  values  of  x  and  y  after  swap ?  --->  x = 25  and y=10
'''

'''x = 10
y = 25

temp = x
x = y
y = temp

print(x)
print(y)'''

'''
(Home  work)
Write  a  program  to  swap  values  of  two  objects  without  using  3rd  object

Hint: One  addition  and  two  subtractions

x = -200
y =  100


x = -200
y = 100

x = x + y
y = x - y
x = x - y

print(x)
print(y)'''

'''
(Home  work)
Write  a  program  to  swap  values  of  two  objects  without  using  3rd  object

Hint: One  multiplication  and  two  divisions

x =25
y=10


x = 25
y = 10

x = x * y
y = x / y
x = x / y

print(x)
print(y)'''

'''
Write  a  program  to  add ,  subtract , multiply  and  divide  two  complex  numbers

Let  first  input   be  3 + 4j  and  second  input  be   5 + 6j
What  is  the  sum ? --->  (3 + 4j) + (5 + 6j) =  8 + 10j
What  is  the  difference ?  --->  (3 + 4j) - (5 + 6j) =  -2 - 2j
What  is  the  product ?  --->  (3 + 4j) * (5 + 6j) =  15 + 18j + 20j - 24 = -9 + 38j
What  is  the  division ?  --->  (3 + 4j) / (5 + 6j)  =  (3 + 4j) * (5 - 6j) / (5 + 6j)  * (5 - 6j)
												=  (15 - 18j + 20j + 24) / (25 + 36)
												=   39 / 61+j61


a = 3+4j
b = 5+6j
sum = a+b
difference = a-b
product = a*b
divison = a/b
print(sum)
print(difference)
print(product)
print(divison)'''

'''
Write  a  program  to  determine  sum , difference , product , quotient , largest  and  smallest  of  two  numbers.
Also  find  remainder,  sqrt  of  first  input , power, gcd  and  factorial  of  first  input

Hint:  Use  F  string  to  print results

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
fact(10) = 3628800


import math
a = eval(input('Enter a  first value: '))
b = eval(input('Enter a  second value: '))

print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a%b)
print(max(a,b))
print(min(a,b))
print(a ^ b)
print(math.sqrt(a))
print(math.gcd(a,b))
print(math.factorial(a))'''

'''
Gift
Write  a  program  to  swap  values  of  any  two  objects  in  a  single  statement  without  using  3rd  object

Let  'x'  be  25  and  'y'  be   'Hyd'
What  are  'x'  and  'y'  after  swap ?  --->  Hyd  and  25

Hint:  Swap  references  but  not objects


x = eval(input('Enter a  first value: '))
y = eval(input('Enter a  second value: '))

x,y=y,x

print(x)
print(y)'''



'''Write  a  program  to  determine  largest  of  two  inputs  without  using  max()  function

1) What  is  the  output  if  inputs  are  10  and  20 ?   ---> 20

2) What  is   the  output  if  inputs  are  35.8  and  27.9 ?  ---> 35.8

3) What  is  the  output  if  inputs  are  'RAMA'  and  'RAJESH' ?  --->  'RAMA'  becoz  'M' > 'J'

4) What  is  the  output  if  inputs  are  [10 , 20 , 15 , 18 , 19 , 28]  and  [10 , 20 , 25, 17] ?   --->  [10 , 20 , 25 , 17]  becoz  25 > 15

5) Use   ternary operator
'''


'''x = eval(input('Enter a  first value: '))
y = eval(input('Enter a  second value: '))

output = x if x > y else y
print(output)'''


'''
Write  a  program  to  determine  largest  of  three  inputs  without  using  max()  function

1) What  is  the  output  if  inputs  are  10 , 20  and  15 ?   --->  20

2) What  is  the  output  if  inputs  are  35.8 , 42.8  and  27.9 ?   ---> 42.8

3) What  is  the  output  if  inputs  are  'RAMA'  , 'RAKESH'  and  'RAJESH' ?   --->  'RAMA'

4) What  is   the  output  if  inputs  are  [10 , 20 , 15 , 18]  , [10 , 20 , 32, 19]  and  [10 , 20 , 25, 17] ?  --->  [10 , 20 , 32 , 19]

5) Use  nested  ternary operator'''

'''x = eval(input('Enter a  first value: '))
y = eval(input('Enter a  second value: '))
z = eval(input('Enter a third value: '))

output = x if (x > y) else (y if y > z else z)
print(output)'''

'''
Write  a  program  to  print   '>'  if  1st  input  >  2nd  input,
                                               '<'  if  1st  input  <  2nd  input  and
                                               '='  if  inputs  are  same

1) What  is  the  result  if  inputs  are  10  and  20 ?  --->  <

2) What  is  the  result  if  inputs  are  70  and  60 ?  --->  >

3) What  is  the  result  if  inputs  are  25  and  25 ?  --->  =

4) Inputs  can  be  integers , floats , strings  and  so  on

5) Use  ternary operator
'''

'''x = eval(input('Enter a  first value: '))
y = eval(input('Enter a  second value: '))
result = '>' if x > y else ('<' if x < y else '=')
print(result)'''


'''
Write  a  program  to  print  1  if  input  is  +ve  ,  -1    if  input  is  -ve  and  0  if  input  is  0

1) What  is  the  result  if  input  is  -25 ?  --->  -1

2) What  is  the  result  if  input  is  75 ?  --->  1

3) What  is  the  result  if  input  is  0 ?  ---> 0

4) Use  nested  ternary  operator
'''


