#program1:
#Area and Perimeter of reactangle
try:
	l=float(input("Enter length of reactangle: "))
	b=float(input("Enter breath of reactangle: "))
	area=l*b
	perimeter=2*(l+b)
	print(f'Area: {area:.2f}')
	print(f'Perimeter: {perimeter:.2f}')
except:
	print('Enter the values only')

#program2:
#Volume of Sphere
import math
try:
	r=float(input('Enter radius: '))
	v=4/3*math.pi*r**3
	print(f'Volume: {v:.2f}')
except:
	print('Enter the number only')

#program3:
#Determine Simple Interest and Compound Interest
try:
	p=float(input("Enter Principle: "))
	t=float(input('Enter time: '))
	r=float(input('Enter rate of interest: '))
	SI=(p*t*r)/100
	CI=p*(1+r/100)**t-p
	print(f'Simple Interest: {SI}')
	print(f'Compound Interest: {CI}')
except:
	print('Enter the any number only')

#program4:
#Swap the values of two object using 3rd object
x=int(input('Enter 1st input: '))
y=int(input('Enter 2nd input: '))
print(f'Before swap: x = {x}  y = {y}')
temp=x
x=y
y=temp
print(f'After swap: x = {x}  y = {y}')

#program5:
#Swap the values of two objects without 3rd object using one addition and two subtractions
try:
	x=int(input("Enter 1st input: "))
	y=int(input("Enter 2nd input: "))
	print(f'Before swap: x = {x}  y = {y}')
	x=x+y
	y=x-y
	x=x-y
	print(f'After swap: x = {x}  y = {y}')
except:
	print("enter the integer number")

#program6:
#Swap the values of two objects without 3rd object using one multiplication and two division
try:
	x=int(input("Enter 1st input: "))
	y=int(input("Enter 2nd input: "))
	print(f'Before swap: x = {x}  y = {y}')
	x=x*y
	y=x//y
	x=x//y
	print(f'After swap: x = {x}  y = {y}')
except:
	print("enter the integer number")

#program7:
#add,subtract,product,divison of complex numbers
try:
	x=complex(input("Enter first complex number: "))
	y=complex(input("enter second complex number: "))
	sum=x+y
	diff=x-y
	multi=x*y
	div=x/y
	print(f'sum : {sum}')
	print(f'Difference : {diff}')
	print(f'Product : {multi}')
	print(f'Division : {div}')
except:
	print("Enter only complex number only")

#program8:
#Sum , difference , product , quotient , largest  and  smallest  of  two  numbers.Also  find  remainder,  sqrt  of  first  input , power, gcd  and  factorial  of  first  input

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

#program9:
#swap  values  of  any  two  objects  in  a  single  statement  without  using  3rd  object

x=input("Enter 1st input: ')
y=input("Enter 2nd input: ')
print(f'Before swap: x = {x}   y = {y}')
x,y=y,x
print(f'After swap: x = {x}   y = {y}')

#program10:
#largest  of  two  inputs  without  using  max()  function using ternary  operator

a=eval(input('Enter 1st input: '))
b=eval(input('Enter 2nd input: '))
result=a if a>b else b
print(f'Largest Input : {result}')

#program11: 
#largest  of  three  inputs  without  using  max()  function using ternary  operator

a=eval(input('Enter 1st input: '))
b=eval(input('Enter 2nd input: '))
c=eval(input('Enter 3rd input: '))
result= a if a > b and a > c else b if b > c else c
print(f'Largest Input: {result}')

#program12:
#print   '>'  if  1st  input  >  2nd  input,'<'  if  1st  input  <  2nd  input  and'='  if  inputs  are  same
a=eval(input('Enter 1st input: '))
b=eval(input('Enter 2st input: '))
result='>' if a>b else '<' if a<b else '='
print(f'result : {result}')

#program13:
#program  to  print  1  if  input  is  +ve  ,  -1    if  input  is  -ve  and  0  if  input  is  0 using ternary  operato

try:
	a=float(input('Enter any number: '))
	result=1 if a>0 else -1 if a<0 else 0
	print(f'result:{result}')
except:
	print('any number')
 
#program14:
#input  is  even  number  or  odd  number using ternary  operator
try:
	a=int(input("enter any +ve number: "))
	result='Even number' if a%2==0 else 'odd number'
	print(f'Result : {result}')
except:
	print('enter any positive number')
