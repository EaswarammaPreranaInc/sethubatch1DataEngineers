'''
(Home  work)
Write  a  program  to  determine  area  and  perimeter  of  rectangle

1) What  are  the  inputs ?  ---> length  and   breadth

2) What  are  the  outputs  ?  --->  area  and  perimeter

3) What  is  the  area  of  rectangle  ?  --->  length * breadth

4) What  is  the  perimeter  of  rectangle ?  --->  2 * (length + breadth)
'''
l = float(input('Enter length of rectangle :'))#Enter  length  of  rectangle  : 4
b = float(input('Enter breadth of rectangle :')) # Enter  breadth  of  rectangle :  5
Area  = l*b
Perimeter = 2*(l+b)
print(F'Area of rectangle: {Area:.2f}') # Area of rectangle: 20.00
print(F'Perimeter of rectangle: {Perimeter:.2f}') # Perimeter of rectangle: 18.00
'''
(Home  work)
Write  a  program  to  determine  volume  of  a  sphere

1) What  is  the  input ?  --->  radius

2) What  is  the  output ?  --->  volume

3) What  is  the  volume  of  sphere  ?  --->  4 / 3  * pi *  r ^ 3
'''
import math
r = float(input('Enter a no:')) #Enter  radius  :  3.5
v = 4/3 * math.pi * r ** 3
print(F'Volume of the sphere : {v:.2f}') # Volume of the sphere : 179.59
'''
(Home  work)
Write  a  program  to  determine  simple  interest  and  compound  interest

1) What  are  the  inputs  ?  --->  principle , time  and   rate  of  interest

2) What  are  the  outputs ? --->  Simple  interest   and   compound  interest

3) What  is  simple  interest  formula ?  ---> ptr / 100

4) What  is  compound  interest  formula ?  --->  p * (1  +  r  /  100) ^  t  -  p
'''
p = float(input('Enter a principle amount:')) #Enter  principle  :  10000
t = float(input('Enter time:')) #Enter  time  : 3
r = eval(input('Enter rate:')) #Enter  rate  of  interest :  7.5
SI = (p*t*r)/100              #Simple  Interest : 2250.00
CI = p*(1+r/100)**t-p        #Compound  Interest : 2422.97
print(F'Simple Interest : {SI : .2f}')
print(F'Compount Interest : {CI : .2f}')
'''
(Home  work)
Write  a  program  to  swap  values  of  two  objects  using  3rd   object

Let  x = 10  and  y = 25
What  are  the  values  of  x  and  y  after  swap ?  --->  x = 25  and   y = 10
'''
x = int(input('Enter 1st input:'))                 #Enter  1st  input  : 10
y = int(input('Enter 2nd input:')) #Enter  2nd  input  : 25
temp = x
x = y
y = temp
print(F'After swap: x = {x} y = {y}')
'''
(Home  work)
Write  a  program  to  swap  values  of  two  objects  without  using  3rd  object

Hint: One  addition  and  two  subtractions

x = -200
y =  100
'''
x = int(input('Enter a no:')) #Enter  1st  input  : 100
y = int(input('Enter a no:')) #Enter  2nd  input  : -200
x = x+y #Before  swap :  x=100.0           y=-200.0
y = x-y#After  swap :  x=-200.0           y=100.0
x = x-y
print(F'After swap : x = {x}  y = {y}') # After swap x = 100  y = -200
'''
(Home  work)
Write  a  program  to  swap  values  of  two  objects  without  using 3rd  object

Hint: One  multiplication  and  two  divisions

x =  25
y =  10
'''
x = int(input('Enter a no:')) #Enter  1st  input  : 25
y = int(input('Enter a no:')) #Enter  2nd  input  : 10
x = x*y
y = x/y
x = x/y
print(F'After swap : x = {x}  y = {y}') # After swap x = 10  y = 25
'''
Write  a  program  to  add ,  subtract , multiply  and  divide  two  complex  numbers

Let  first  input   be  3 + 4j  and  second  input  be   5 + 6j
What  is  the  sum ? --->  (3 + 4j) + (5 + 6j) =  8 + 10j
What  is  the  difference ?  --->  (3 + 4j) - (5 + 6j) =  -2 - 2j
What  is  the  product ?  --->  (3 + 4j) * (5 + 6j) =  15 + 18j + 20j - 24 = -9 + 38j
What  is  the  division ?  --->  (3 + 4j) / (5 + 6j)  =  (3 + 4j) * (5 - 6j) / (5 + 6j)  * (5 - 6j)
												=  (15 - 18j + 20j + 24) / (25 + 36)
												=   39 / 61  + 2j / 61
'''
x = complex(input('Enter a complex no:'))#Enter first complex number : 3+4j
y = complex(input('Enter a complex no:'))#Enter second complex number: 5+6j
print(F'Sum : x + y = {x+y} ') #Sum :  (8+10j)
print(F'Difference : x - y = {x-y} ')#Difference :  (-2-2j)
print(F'Product : x * y = {x*y} ') #Product:  (-9+38j)
print(F'DIvision : x / y = {x/y} ') #Division :  (0.6393442622950819+0.03278688524590165j)
'''
Write  a  program  to  determine  sum , difference , product , quotient , largest  and  smallest  of  two  numbers.
Also  find  remainder,  sqrt  of  first  input , power, gcd  and  factorial  of  first  input

Hint:  Use  F  string  to  print  results
'''
x = eval(input('Enter a  no:')) # Enter 1st  integer  number :  10
y = eval(input('Enter a  no:'))#Enter 2nd  integer  number :  7
print(f'{x+y}')#10 + 7 = 17
print(f'{x-y}') #10 - 7 = 3
print(f'{x*y}')#10 * 7 = 70
print(f'{x/y}') #10 / 7 = 1.4285714285714286
print(f'{x%y}')#10 % 7 = 3
print(f'{max(x,y)}')#max(10 , 7) = 10
print(f'{min(x,y)}') #min(10 , 7) = 7
print(f'{x**y}') #10 ^ 7 = 10000000
print(f'{math.sqrt(x)}')#sqrt(10) = 3.1622776601683795
print(f'{math.gcd(x,y)}')#gcd(10 , 7) = 1
print(f'{math.factorial(x)}') #fact(10) = 3628800
'''
Gift
Write  a  program  to  swap  values  of  any  two  objects  in  a  single  statement  without  using  3rd  object

Let  'x'  be  25  and  'y'  be   'Hyd'
What  are  'x'  and  'y'  after  swap ?  --->  Hyd  and  25

Hint:  Swap  references  but  not  objects
'''
x = eval(input('Enter a no:')) #Enter  1st  input  : 25
y = eval(input('Enter a no:')) #Enter  2nd  input  : Hyd
x , y = y , x
print(F'After swap : x = {x}  y = {y}')
'''
Write  a  program  to  determine  largest  of  two  inputs  without  using  max()  function

1) What  is  the  output  if  inputs  are  10  and  20 ?   ---> 20

2) What  is   the  output  if  inputs  are  35.8  and  27.9 ?  ---> 35.8

3) What  is  the  output  if  inputs  are  'RAMA'  and  'RAJESH' ?  --->  'RAMA'  becoz  'M' > 'J'

4) What  is  the  output  if  inputs  are  [10 , 20 , 15 , 18 , 19 , 28]  and  [10 , 20 , 25, 17] ?   --->  [10 , 20 , 25 , 17]  becoz  25 > 15

5) Use   ternary  operator
'''
'''Enter 1st input : 'Rama'
Enter 2nd input : 'Rajesh'
Largest  Input  :   Rama'''
'''
Write  a  program  to  determine  largest  of  three  inputs  without  using  max()  function

1) What  is  the  output  if  inputs  are  10 , 20  and  15 ?   --->  20

2) What  is  the  output  if  inputs  are  35.8 , 42.8  and  27.9 ?   ---> 42.8

3) What  is  the  output  if  inputs  are  'RAMA'  , 'RAKESH'  and  'RAJESH' ?   --->  'RAMA'

4) What  is   the  output  if  inputs  are  [10 , 20 , 15 , 18]  , [10 , 20 , 32, 19]  and  [10 , 20 , 25, 17] ?  --->  [10 , 20 , 32 , 19]

5) Use  nested  ternary  operator
'''
x = eval(input('Enter list:'))#Enter 1st input : [10,20,15,18]
y = eval(input('Enter list:'))#Enter 2nd input : [10,20,32,19]
z = eval(input('Enter list:'))#Enter 3rd input : [10,20,25,17]
print(max(x,y,z))#Largest  Input  :  [10, 20, 32, 19]
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
x = eval(input('Enter 1st input :')) # 10
y = eval(input('Enter 2nd input :')) # 20
if x>y:
    print('Result : >')
elif x<y:
    print('Result : <')
else:
    print('Result : =')    

#Result :   <
'''
Write  a  program  to  print  1  if  input  is  +ve  ,  -1    if  input  is  -ve  and  0  if  input  is  0

1) What  is  the  result  if  input  is  -25 ?  --->  -1

2) What  is  the  result  if  input  is  75 ?  --->  1

3) What  is  the  result  if  input  is  0 ?  ---> 0

4) Use  nested  ternary  operator
'''
x = int(input('Enter any number :' ))
res = 1 if x>0 else(-1 if x<0 else 0)
print(res)
'''
Write  a  program  to  test  input  is  even  number  or  odd  number

1) What  is  an  even  number  ?  --->  Divisible  by  2

2) What  is  an  odd  number  ?  --->  Not  divisible  by  2

3) Use  ternary  operator
'''
x = int(input('Enter any number except 0:' ))
res = 'Even' if x%2==0 else 'Odd'
print(res)
