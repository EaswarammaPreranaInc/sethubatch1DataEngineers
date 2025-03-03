#swaping of two numbers
x=float(input('enter the first number:'))
y=float(input('enter the second number:'))
print('before swaping')
print(f'x={x},y={y}')
x=x*y
y=x/y
x=x/y
print('after swaping')
print(f'x={x},y={y}')

#input=4
#input=5
"""output:
before swaping
x=4.0,y=5.0
after swaping
x=5.0,y=4.0"""
