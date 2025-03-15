x=input('Enter input:')
print(type(x))
print(x)
x=int(input('Enter any integer number:'))
print(type(x))
print(x)
x=eval(input('Enter any input:'))
print(type(x))
print(x)
'''
'''
x=eval(input('Enter length of rectangle:'))
y=eval(input('Enter breadth of rectangle:'))
Area = x*y
print(F'Area:{Area}')
Perimeter=2*(x+y)
print(F'Perimeter:{Perimeter}')
'''
'''
import math
x=eval(input('Enter radius:'))
Volume=4/3*(math.pi)*x**3
print(F'Volume:{'%g'  %Volume}')
'''
'''
x=eval(input('Enter principle:'))
y=eval(input('Enter time:'))
z=eval(input('Enter rate of interest:'))
SimpleInterest=x*y*z/100
print(F'SimpleInterest:{'%g' %SimpleInterest}')
CompoundInterest=x*(1+z/100)**y-z
print(F'CompoundInterest:{'%g' %CompoundInterest}')
'''
'''
x=eval(input('Enter 1st input:'))
y=eval(input('Enter 2nd input:'))
x,y=y,x
print(x,y)
'''
'''
x=eval(input('Enter 1st input:'))
y=eval(input('Enter 2nd input:'))
x=x+y
y=x-y
x=x-y
print(x)
print(y)
'''
'''
x=eval(input('Enter 1st input:'))
y=eval(input('Enter 2nd input:'))
x=x*y
y=x/y
x=x/y
print(x)
print(y)
'''
'''
x=eval(input('Enter first complex number:'))
y=eval(input('Enter second complex number:'))
Sum=x+y
Difference=x-y
Product=x*y
Division= x/y
print(f'Sum:{sum}')                   
print(f'Difference:{Difference}') 
print(f'Product:{Product}')
print(f'Division:{Division}') 
'''
'''
from builtins import pow
import math
x=eval(input('Enter 1st integer number:'))
y=eval(input('Enter 2nd integer number:'))
Sum=x+y
Difference=x-y
Product=x*y
Division= x/y
quotient=x%y
max(10,7)
print(f'Sum:{Sum}')                   
print(f'Difference:{Difference}') 
print(f'Product:{Product}')
print(f'Division:{Division}')
print(f'quotient:{quotient}')
print(max(10,7))
print(min(10,7))
print(pow(10,7))
print(math.sqrt(10))
print(math.gcd(10,7))
print(math.factorial(10))
