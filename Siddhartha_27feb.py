length = float(input("Enter length of rectangle: "))
breadth = float(input("Enter breadth of rectangle: "))
area = length * breadth
perimeter = 2 *(length + breadth)
print(f'Area: {area}')
print(f'Perimeter: {perimeter}')


import math
radius = float(input("Enter  radius  : "))
volume = (4/3) * math.pi * (radius ** 3)
print(f'Volume : {volume:.2f}')



principal = float(input("Enter principle: "))
time = float(input("Enter time: "))
rate = float(input("Enter rate of interest: "))
simpleinterest = (principal * time * rate) / 100
compoundinterest = principal * ((1 + rate/100) ** time) - principal
print(f"Simple Interest: {simpleinterest:.2f}")
print(f"Compound Interest: {compoundinterest:.2f}")



x = int(input("Enter 1st input: "))
y = int(input("Enter 2nd input: "))
print("Before swap: x =", x, "y =", y)
temp = x
x = y
y = temp
print("After swap: x =", x, "y =", y)



x = int(input("Enter 1st input: "))
y = int(input("Enter 2nd input: "))
print("Before swap: x =", x, "y =", y)
x = x + y
y = x - y
x = x - y
print("After swap: x", x, "y =", y)


x = int(input("Enter 1st input: "))
y = int(input("Enter 2nd input: "))
print("Before swap: x =", x, "y =", y)
x = x * y
y = x // y
x = x // y
print("After swap: x =", x, "y =", y)


a = eval(input("Enter your first input: "))
b = eval(input("Enter your second input: "))
Sum = a+b
Difference = a-b
Product = a*b
division = a/b
print("Sum is = ", a+b)
print("Difference is = ", a-b)
print("Product is = ", a*b)
print("division is = ", a/b)


import math
a = int(input("Enter 1st integer: "))
b = int(input("Enter 2nd integer: "))
print(f'a+b = {a+b}')
print(f'a-b = {a-b}')
print(f'a*b = {a*b}')
print(f'a/b = {a/b}')
print(f'a%b = {a%b}')
print(f'max(a,b) = {max(a,b)}')
print(f'min(a,b)= {min(a,b)}')
print(f'a^b = {a**b}')  
print(f'gcd(a,b) = {math.gcd(a,b)}')  
print(f'sqrt(10) = {math.sqrt(a)}')  
print(f'factorial(10) = {math.factorial(a)}')


x = eval(input("Enter 1st input: "))
y = eval(input("Enter 2nd input: "))
print("Before swap: x =", x, "y =", y)
temp = x
x = y
y = temp
print("After swap: x =", x, "y =", y)


a = eval(input("Enter 1st input: "))
b = eval(input("Enter 2nd input: "))
c = eval(input("Enter 3rd input: "))
result = a if a > b and a > c else b if b > a and b > c else c
print("Largest Input: ", result)


num = int(input("Enter a number: "))
result = "Even" if num % 2==0 else "Odd"
print(f'{num} is {result} number')


num = int(input("Enter a number: "))
result = 1 if num > 0 else -1 if num < 0 else 0
print(f'Result : {result}')


num1 = input("Enter 1st num: ")
num2 = input("Enter 2nd num: ")
result = '>' if num1 > num2 else '<' if num1 < num2 else '='
print(result)




