1. # Write a program to determine area and perimeter of retangle
x=float(input('Enter length of triangle : '))  # reads string input and converts to float 
y=float(input('Enter breadth of rectangle : '))  # reads string input and converts to float 
area= x*y  # Area of rectangle= length * breadth(x * y)
perimeter= 2*(x+y)  # perimeter of rectangle= 2(length+breadth)
print(F"Area : {area:.2f}")  # prints area
print(F"Perimeter : {perimeter:.2f}")  # prints perimeter


# Outputs
# Enter  length  of  rectangle  : 4
# Enter  breadth  of  rectangle :  5
# Area  :  20.00
# Perimeter :  18.00



2. # Write a program to determine volume of sphere
import math
r=float(input('Enter radius : '))  # reads the string input and converts to float
volume= 4/3 * math.pi * r**3  # volume of sphere= 4/3 * pi * r**3
print(f'Volume : {volume:.2f}')  # prints volume value


# Outputs
# Enter  radius  :  3.5
# Volume  :  179.59



3. # write a program to determine simple interest and compound interest
p=eval(input('Enter principle : '))  # reads string input and converts to appropriate object
t=eval(input('Enter time : '))  # reads string input and converts to appropriate object
r=eval(input('Enter rate of interest : '))  # reads string input and converts to appropriate object
SI= p*t*r/100  # simple interest= p*t*r/100 (p=principle,t=time,r=rate of interest)
CI= p * (1+r/100) ** t-p  # compound interest= p*(1+r/100) ** t-p
print(f'Simple Interest : {SI:.2f}')  # prints SI value
print(f'Compund Interest : {CI:.2f}')


# Outputs
# Enter  principle  :  10000
# Enter  time  : 3
# Enter  rate  of  interest :  7.5
# Simple  Interest : 2250.00
# Compound  Interest : 2422.97



4. # Write a program to swap values of two objects using third object
x=eval(input('Enter 1st input : '))  # reads string input and converts to appropriate object
y=eval(input('Enter 2st input : '))  # reads string input and converts to appropriate object
print(f'Before swap : x={x}\ty={y}')  # prints values before swapping
temp=x
x=y
y=temp
print(f'After swap : x={x}\ty={y}')  # prints values after swapping


# Outputs
# Enter  1st  input  : 10
# Enter  2nd  input  : 25
# Before  swap :  x=10      y=25
# After  swap :  x=25       y=10



5.  # Write a program to swap values of 2 objects without using third object
x=eval(input('Enter 1st input : '))  # reads string input and converts to appropriate object
y=eval(input('Enter 2st input : '))  # reads string input and converts to appropriate object
print(f'Before swap : x={x:.1f}\ty={y:.1f}')  # prints values before swapping
x=x+y  # x=100,y=-200-->x=100-200-->x=-100
y=x-y  # y=x-y-->y=-100-(-200)-->y=-100+200-->y=100
x=x-y  # x=x-y-->x=-100-100-->x=-200
print(f'After swap : x={x:.1f}\ty={y:.1f}')  # prints values after swapping2

# Outputs
# Enter  1st  input  : 100
# Enter  2nd  input  : -200
# Before  swap :  x=100.0           y=-200.0
# After  swap :  x=-200.0           y=100.0



6.  # Write a program to swap values of 2 objects without using third object
x=eval(input('Enter 1st input : '))  # reads string input and converts to appropriate object
y=eval(input('Enter 2st input : '))  # reads string input and converts to appropriate object
print(f'Before swap : x={x:.1f}\ty={y:.1f}')  # prints values before swapping
x=x*y
y=x/y
x=x/y
print(f'After swap : x={x}\ty={y}')  # prints values after swapping2

# x=25
# y=10




7.  # Write a program to add,subtract,multiply and divide two complex numbers
x=eval(input('Enter 1st complex number : '))  # reads string input and converts to appropriate object
y=eval(input('Enter 2st complex number : '))  # reads string input and converts to appropriate object
sum=x+y
subtract=x-y
product=x*y
divide=x/y
print(f'Sum : {sum}')  # prints sum value 
print(f'Subtract : {subtract}')  # prints subtraction value
print(f'Product : {product}')  # prints multiplication value
print(f'Division : {divide}')  # prints division value


# Outputs
# Enter first complex number : 3+4j
# Enter second complex number: 5+6j
# Sum :  (8+10j)
# Difference :  (-2-2j)
# Product:  (-9+38j)
# Division :  (0.6393442622950819+0.03278688524590165j)



8.  # Write  a  program  to  determine  sum , difference , product , quotient , largest  and  smallest  of  two  numbers.
# Also  find  remainder,  sqrt  of  first  input , power, gcd  and  factorial  of  first  input
import math
x=eval(input('Enter 1st integer number : '))
y=eval(input('Enter 2nd integer number : '))
print(f'{x} + {y} = {x+y}')
print(f'{x} - {y} = {x-y}')
print(f'{x} * {y} = {x*y}')
print(f'{x} / {y} = {x/y}')
print(f'{x} % {y} = {x%y}')
print(f'max({x},{y}) = {max(x,y)}')
print(f'min({x},{y}) = {min(x,y)}')
print(f'{x}**{y} = {x**y}')
print(f'sqrt({x}) = {math.sqrt(x)}')
print(f'gcd({x},{y}) = {math.gcd(x,y)}')
print(f'fact({x}) = {math.factorial(x)}')


# Outputs
# Enter 1st  integer  number :  10
# Enter 2nd  integer  number :  7
# 10 + 7 = 17
# 10 - 7 = 3
# 10 * 7 = 70
# 10 / 7 = 1.4285714285714286
# 10 % 7 = 3
# max(10 , 7) = 10
# min(10 , 7) = 7
# 10 ^ 7 = 10000000
# sqrt(10) = 3.1622776601683795
# gcd(10 , 7) = 1
# fact(10) = 3628800




9.  # Write  a  program  to  swap  values  of  any  two  objects  in  a  single  statement  without  using  3rd  object
x=eval(input('Enter 1st input : '))  # reads string input and converts to appropriate object
y=eval(input('Enter 2st input : '))  # reads string input and converts to appropriate object
print(f'Before swap : x={x}\ty={y}')  # prints values before swapping
x,y=y,x
print(f'After swap : x={x}\ty={y}')  # prints values after swapping2

# Outputs
# Enter  1st  input :  25
# Enter  2nd  input : Hyd
# Before  swap :  x='25'            y='Hyd'
# After  swap :  x='Hyd'            y='25'




10. # Write  a  program  to  determine  largest  of  two  inputs  without  using  max()  function
x=eval(input('Enter 1st input : '))  # reads string input and converts to appropriate object
y=eval(input('Enter 2st input : '))  # reads string input and converts to appropriate object
max=x if x>y else y
print(f'Largest input : {max}')

# Outputs
# Enter 1st input : 'Rama'
# Enter 2nd input : 'Rajesh'
# Largest  Input  :   Rama




11.  # Write  a  program  to  determine  largest  of  three  inputs  without  using  max()  function
x=eval(input('Enter 1st input : '))  # reads string input and converts to appropriate object
y=eval(input('Enter 2st input : '))  # reads string input and converts to appropriate object
z=eval(input('Enter 3rd input : '))  # reads string input and converts to appropriate object
max=x if x>y and x>z else y if y>x and y>z else z
print(f'Largest input : {max}')

# Outputs
# Enter 1st input : [10,20,15,18]
# Enter 2nd input : [10,20,32,19]
# Enter 3rd input : [10,20,25,17]
# Largest  Input  :  [10, 20, 32, 19]




12.  # Write  a  program  to  print   '>'  if  1st  input  >  2nd  input,'<'  if  1st  input  <  2nd  input  and '='  if  inputs  are  same
x=eval(input('Enter 1st input : '))  # reads string input and converts to appropriate object
y=eval(input('Enter 2st input : '))  # reads string input and converts to appropriate object
print('Result:>' if x>y  else 'Result:<' if x<y else 'Result:=')
# Outputs
# Enter 1st input : 10
# Enter 2nd input : 20
# Result :   <




13.  # Write  a  program  to  print  1  if  input  is  +ve  ,  -1    if  input  is  -ve  and  0  if  input  is  0
x=eval(input('Enter any number : '))  # reads string input and converts to appropriate object
print('Result:1' if x>0 else 'Result:-1' if x<0 else 'Result:0')
# Outputs
# Enter any number : -25
# Result :  -1





14.  # Write  a  program  to  test  input  is  even  number  or  odd  number
x=eval(input('Enter any number : '))  # reads string input and converts to appropriate object
print('Even number' if x%2==0 else 'Odd number')
# Outputs
# Enter any +ve integer : 26
# Even  number


