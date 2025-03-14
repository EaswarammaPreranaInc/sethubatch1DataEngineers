#p1: Write a program area and perimeter of reactangle

try:
	l=float(input("Enter length of reactangle : "))
	b=float(input("Enter breath of reactangle : "))
	a=l*b
	p=2*(l+b)
	print(f'Area: {a:.2f}')
	print(f'Perimeter: {p:.2f}')
except:
	print("Enter numeric values only")

#p2: Write a program to determine volume of a sphere

try:
	r=float(input("Enter radius : "))
	v=4/3*pi*r**3
	print(f'volume: {v:.2f}')
except:
	print("Enter numeric value only")

#p3: Write a program to determine simple interest and compound interest

try:
	p=float(input("Enter principle: "))
	t=float(input("Enter time: "))
	r=float(input("Enter rate of interest: "))
	SI=(p*t*r)/100
	CI=p*(1+r/100)**t-p
	print(f'Simple Interest: {SI:.2f}')
	print(f'Compound Interest: {CI:.2f}')
except:
	print(Enter numeric values only')

#p4: Write a program Swap the values of two object using 3rd object

x=int(input('Enter 1st input: '))
y=int(input('Enter 2nd input: '))
print(f'Before swap: x = {x}  y = {y}')
temp=x
x=y
y=temp
print(f'After swap: x = {x}  y = {y}')

#p5: Write a program Swap the values of two objects without 3rd object using one addition and two subtractions
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

#p6: Write a program Swap the values of two objects without 3rd object using one multiplication and two division
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

#p7: Write a program add,subtract,product,divison of complex numbers
try:
	x=complex(input("Enter first complex number: "))
	y=complex(input("enter second complex number: "))
	sum=x+y
	diff=x-y
	multi=x*y
	div=x/y
	print(f'Sum : {sum}')
	print(f'Difference : {diff}')
	print(f'Product : {multi}')
	print(f'Division : {div}')
except:
	print("Enter only complex number only")

#p8: Write a program Sum , difference , product , quotient , largest  and  smallest  of  two  numbers.
Also  find  remainder,  sqrt  of  first  input , power, gcd  and  factorial  of  first  input

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
po=math.pow(a,b)
gcd=math.gcd(a,b)
fact=math.factorial(a)
print(f'{a} + {b} = {sum}')
print(f'{a} - {b} = {diff}')
print(f'{a} * {b} = {prod}')
print(f'{a} / {b} = {quot}')
print(f'{a} % {b} = {rem}')
print(f'max({a},{b}) = {large}')
print(f'min({a},{b}) = {small}')
print(f'{a}^{b} = {po}')
print(f'sqrt({a}) = {sqrt}')
print(f'gcd({a},{b}) = {gcd}')
print(f'fact({a}) = {fact}')

#p9: Write a program swap  values  of  any  two  objects  in  a  single  statement  without  using  3rd  object

x=input("Enter 1st input: ')
y=input("Enter 2nd input: ')
print(f'Before swap: x = {x}   y = {y}')
x,y=y,x
print(f'After swap: x = {x}   y = {y}')

#p10: Write a program largest  of  two  inputs  without  using  max()  function using ternary  operator

a=eval(input('Enter 1st input: '))
b=eval(input('Enter 2nd input: '))
res=a if a>b else b
print(f'Largest Input : {res}')

#p11: Write a program largest  of  three  inputs  without  using  max()  function using ternary  operator

a=eval(input('Enter 1st input: '))
b=eval(input('Enter 2nd input: '))
c=eval(input('Enter 3rd input: '))
res= a if a > b and a > c else b if b > c else c
print(f'Largest Input: {res}')

#p12: Write a program to print   '>'  if  1st  input  >  2nd  input,
                   '<'  if  1st  input  <  2nd  input  and
                   '='  if  inputs  are  same
a=eval(input('Enter 1st input: '))
b=eval(input('Enter 2st input: '))
res='>' if a>b else '<' if a<b else '='
print(f'result : {res}')

#program13:program  to  print  1  if  input  is  +ve  ,  -1    if  input  is  -ve  and  0  if  input  is  0 using ternary  operato

try:
	a=float(input('Enter any number: '))
	res=1 if a>0 else -1 if a<0 else 0
	print(f'result:{res}')
except:
	print('any number')
 
#p14: Write a program to input  is  even  number  or  odd  number using ternary  operator
try:
	a=int(input("enter any +ve number: "))
	res='Even number' if a%2==0 else 'odd number'
	print(f'Result : {res}')
except:
	print('enter any positive number')
