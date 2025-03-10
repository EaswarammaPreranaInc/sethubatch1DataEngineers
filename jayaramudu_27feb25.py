# Ex-1.py
l=eval(input("Enter a length l : "))
b=eval(input("Enter a breadth b : "))
a = l * b
p = 2 * (l + b)
print(F'Area       : {a:.2f}')
print(F'Perimeter  : {p:.2f}')

# Ex-2.py
import math
r=eval(input("Enter a radius r : "))
pi=math.pi
volume = (4 / 3) * pi * (r ** 3)
print(F'Volume : {volume: .2f}')

# Ex-3.py
principle = eval(input("Enter a principle : " ))
time = eval(input("Enter a time  : " ))
rate = eval(input("Enter a rate of interest : " ))
si = (principle * rate * time) / 100
ci = principle * (((1+rate/100)) ** time) - principle
print(F'Simple  Interest {si: .2f}')
print(F'Compound  Interest {ci: .2f}')

# Ex-4.py
x = eval(input("Enter  1st  input  :" ))
y = eval(input("Enter  2st  input  : " ))
print(F'Before Swap {x = } and  { y= }')
z = x
x = y
y = z
print(F'After  Swap {x = } and  { y= }')

# Ex-5.py
x = eval(input("Enter  1st  input  :" ))
y = eval(input("Enter  2st  input  : " ))
print(F'Before Swap {x = } and  { y= }')
y = y + x
x = y - x
y = y - x
print(F'After Swap {x = }  and  { y= }')

# Ex-6.py
x = eval(input("Enter  1st  input  :" ))
y = eval(input("Enter  2st  input  : " ))
print(F'Before Swap {x = } and  { y= }')
x = x * y
y = x / y
x = x / y
print(F'After Swap {x = }  and  { y= }')

# Ex-7.py
a = eval(input('Enter first complex number : '))
b = eval(input('Enter second complex number : '))
sum  = a + b
difference  = a - b
product  =  a * b
division  =  a / b
print(F'Sum : {sum}')
print((F'Difference : {difference}'))
print((F'Product : {product}'))
print(F'Division : {division :}')

# Ex-8.py
a = eval(input('Enter 1st  integer  number  : '))
b = eval(input('Enter 2st  integer  number  : '))
import  math
print(F'{a} + {b} = {a+b}')
print(F'{a} - {b} = {a-b}')
print(F'{a} * {b} = {a*b}')
print(F'{a} / {b} = {a/b}')
print(F'{a} % {b} = {a%b}')
print(F'max({a},{b}) = {max(a,b)}')
print(F'min({a},{b}) = {min(a,b)}' )
print(F'{a} ^ {b} = {a ** b}')
print(F'sqrt({a}) = {math.sqrt(a)}')
print(F'gcd({a},{b}) = {math.gcd(a,b)}')
print(F'fact({a}) = {math.factorial(a)}')

# Ex-9.py
a = eval(input('Enter  1st  input : '))
b = eval(input('Enter  2st  input : '))
print(F'Before  swap :  {a = } and {b = }')
a,b=b,a
print(F'After  swap :  {a = } and {b = }')

# Ex-10.py
a = eval(input('Enter  1st  input : '))
b = eval(input('Enter  2st  input : '))
res = a if a > b else b
print(F'Largest Input : {res}')

# Ex-13.py
try:
    a = int(input('Enter  1st  input : '))
    res = '1' if a > 0 else ('-1' if a < 0 else '0')
    print(F'Result : {res} ')
except:
    print("Input Should Integer")

# Ex-14.py
try:
    a = int(input('Enter any +ve integer :'))
    res = 'Even Number' if a % 2 == 0 else 'Odd'
    print(res)
except:
    print('Input Should be integer')
