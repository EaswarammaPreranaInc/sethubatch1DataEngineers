1 PROGRAM rectangle area and perimeter
length=float(input("length:"))
breadth=float(input("breadth:"))
area=length*breadth
perimeter=2*(length+breadth)
print("area:",length*breadth)
print("perimeter:",2*(length+breadth))
print(f"area:{area:.2f}")
print(f"perimeter:{perimeter:.2f}") 

#2 Write a program to determine volume of sphere
from math import *
radius=float(input("enter radius:"))
volume=(4/3)*pi*pow(radius,3)
print(f"volume:{volume:.2f}")

#3 determine simple interest and compound interest
from math import *
p=float(input("enter principal amount:"))
t=float(input("enter Time period:"))
r=float(input("enter rate of interest:"))
si=p*t*r/100
ci=(p*pow((1+r/100),t))-p
print(f" simple interest:{si:.2f}")
print(f" compound interest:{ci:.2f}")

#4 swap values of two objects using 3rd object
x=0
y=6
temp=x
x=y
y=temp
print(x)
print(y)
print(" before swap x: ",y, "after swap x: ",x)
print(" before swap y: ",x ,"after swap y: ",y)

#5 Swap the values of two objects without 3rd object using one addition and two subtractions
x=int(input("Enter 1st input: "))
y=int(input("Enter 2nd input: "))
print(f'Before swap: x = {x}  y = {y}')
x=x+y
y=x-y
x=x-y
print(f'After swap: x = {x}  y = {y}')

# 6 swap values of two objects without using 3rd object
x=5
y=4
print((x+y)-x)
print((x+y)-y)
print((x*y)//x)
print((x*y)//y)

# 7 add, subtract ,multiply and divide two complex numbers
a = complex(input("Enter a: "))
b = complex(input("Enter b: "))
print('sum :',a+b)
print('Difference :',a-b)
print('Product :',a*b)
print('Division:',a/b)

#8 sum , difference , product , quotient ,largest and smallest of two numbers.
#find  remainder,  sqrt  of  first  input , power, gcd  and factorial  of  first  input
import math
a=int(input('Enter 1st integer number: '))
b=int(input('Enter 2nd integer number: '))
sum=a+b
diff=a-b
prod=a*b
quot=a/b
large=max(a,b)
small=min(a,b)
rem=a%b
sqrt=math.sqrt(a)
power=math.pow(a,b)
gcd=math.gcd(a,b)
fact=math.factorial(a)
print(f'{a} + {b} = {sum}')
print(f'{a} - {b} = {diff}')
print(f'{a} * {b} = {prod}')
print(f'{a} / {b} = {quot}')
print(f'{a} % {b} = {rem}')
print(f'max({a},{b}) = {large}')
print(f'min({a},{b}) = {small}')
print(f'{a}^{b} = {power}')
print(f'sqrt({a}) = {sqrt}')
print(f'gcd({a},{b}) = {gcd}')
print(f'fact({a}) = {fact}')

# 9 swap values of any two objects in a single statement without using 3rd object
x="hyd"
y=4
x,y=y,x
print(x)
print(y)

# 10 find largest of two inputs without using max() function
a=eval(input('Enter 1st input: '))
b=eval(input('Enter 2nd input: '))
c=a if a>b else b
print(f'Largest Input : {c}')


# 11 find largest of three inputs without using max() function
a=eval(input('Enter 1st input: '))
b=eval(input('Enter 2nd input: '))
c=eval(input('Enter 3rd input: '))
result= a if a > b and a > c else b if b > c else c
print(f'Largest Input: {result}')


# 12 print  '>'  if  1st input  >  2nd  input,
#'<'  if  1st  input  <  2nd  input  and
# '='  if  inputs  are  same use ternary
a=eval(input('Enter 1st input: '))
b=eval(input('Enter 2st input: '))
result='>' if a>b else '<' if a<b else '='
print(f'result : {result}')


# 13 print 1 if input is +ve , -1 if input is -ve and 0 if input is 0

try:
	a=float(input('Enter any number: '))
	result=1 if a>0 else -1 if a<0 else 0
	print(f'result:{result}')
except:
	print('any number')
 
# 14 test the input is even number or odd number
try:
	a=int(input("enter any +ve number: "))
	result='Even number' if a%2==0 else 'odd number'
	print(f'Result : {result}')
exc4pt:
