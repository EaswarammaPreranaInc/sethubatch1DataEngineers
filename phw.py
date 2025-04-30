
#1st
l = float(input('enter a number 1:'))
b = float(input('enter a number 2:'))
area = l*b
pm = 2 * (l+b)
print('area :', area)
print('perimeter :', pm)


#2nd
r = float(input('enter the radius'))
pi = 3.14159
volume = 4/3 * pi * r ** 3
print('%.2f' % volume)

#3rd
p = float(input('enter the principle'))
t = float(input('enter the time'))
r = float(input('enter the rate of interest'))
simpleinterest = p*t*r/100
compoundinterest = p * (1+r/100)**t - p
print('simple interest :', simpleinterest)
print('compound interest:', compoundinterest)

#4th
a = int(input('enter a number:'))
b = int(input('enter a number:'))
print('before swap: ', f'a={a} b={b}')
temp = a
a = b
b = temp
print('after swap:', f'a={a} b={b}')

#5th
x = float(input('enter 1st input:'))
y = float(input('enter 2nd input:'))
print('before swap: ', f'x={x} y={y}')
x = x + y
y = x - y
x = x - y
print('after swap', f'x={x} y={y}')

#6th
x = float(input('enter 1st input:'))
y = float(input('enter 2nd input:'))
print('before swap: ', f'x={x} y={y}')
x = x*y
y = x/y
x = x/y
print('after swap', f'x={x} y={y}')

#7th
x = complex(input('enter 1st input:'))
y = complex(input('enter 2nd input:'))
print('sume:',x+y)
print('differece:',x-y)
print('product:',x*y)
print('division:', x/y)

#8th
import math
x = int(input('enter 1st input:'))
y = int(input('enter 2nd input:'))
print(x+y)
print(x-y)
print(x*y)
print(x/y)
print(x%y)
print(max(10,7))
print(min(10,7))
print(10**7)
print(math.sqrt(10))
print(math.gcd(10,7))
print(math.factorial(10))

#9th
x = 25
y = 'hyd'
print('before swap: ', f'x={x} y={y}')
x, y = y, x
print('after swap: ', f'x={x} y={y}')

#10th
x = eval(input('enter 1st input:'))
y = eval(input('enter 2nd input:'))
z = x if x > y else y
print(z)

#11th
x = eval(input('enter 1st input:'))
y = eval(input('enter 2nd input:'))
z = eval(input('enter 3rd input:'))
print(x if x>y else y if y>z else z)

#12th
x = eval(input('enter 1st input:'))
y = eval(input('enter 2nd input:'))
print('>' if x>y else '<' if x<y else '=')

#13th
x = eval(input('enter  input:'))
print(1 if x>0 else -1 if x<0 else 0)

#14th
x = int(input('enter  input:'))
print('even'if x%2==0 else 'odd')

