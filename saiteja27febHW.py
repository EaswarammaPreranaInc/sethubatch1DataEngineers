# area and perimeter of rectangle
'''
l = int(input('Enter lenght of rectangle : '))
b = int(input('Enter breadth of rectangle: '))
area = l*b
p=2*(l+b)
print(F"Area : {area:.2f}")
print(F"Perimeter : {p:.2f}")
'''

# volume of sphere
'''
import math
r=float(input("Enter the Radius:"))
V = (4/3)*math.pi*r**3
print(F"Volume : {V:.2f}")
'''

# SI and cI
'''
p = float(input("Enter the principle :")) 
t = float(input("Enter the Time: "))
r = float(input("Enter the rate of interest:"))
SI= p*t*r / 100
CI= p*((1+r/100)**t)-p
print(F"Simple interest : {SI:.2f}")
print(F"Compound interest : {CI:.2f}")
'''

# swap numbers
'''
x = float(input("Enter 1st input: "))
y = float(input("Enter 2nd input: "))
r = x
print(F"Before swap: x = {x}  y = {y} ")
x = y
y = r
print(F"After swap: x = {x} /t y = {y} ")
'''

# swap without 3rd object
'''x = float(input("Enter 1st input: "))
y = float(input("Enter 2nd input: "))
print(F"Before swap: x = {x}  y = {y} ")
x = y + x
y = x-y
x = x - y
print(F"After swap: x = {x}  y = {y} ")
'''

# swap again
'''x = int(input("Enter 1st input: "))
y = int(input("Enter 2nd input: "))
print(F"Before swap: x = {x} /t y = {y} ")
x = y * x
y = x/y
x = x / y
print(F"After swap: x = {x} /t y = {y} ")
'''

# add, sub , multi, divide, 
'''
x = complex(input('enter the  1st complex:'))
y = complex(input('enter the  2nd complex:'))
sum = x+y
diff = x-y
pro = x*y
div = x/y
print(F"sum : {sum}")
print(F"diff : {diff}")
print(F"pro : {pro}")
print(F"div : {div}")
'''

# integer
'''import math
x = int(input('enter the  1st integer:'))
y = int(input('enter the  2nd integer:'))
sum = x+y
diff = x-y
pro = x*y
div = x/y
gcd=math.gcd(x,y)
sqrt=math.sqrt(x)
max=max(x,y)
min=min(x,y)
f=math.factorial(x)
power=math.pow(x,y)
print(F"{x}+{y} = {sum}")
print(F"{x}-{y} = {diff}")
print(F"{x}*{y}= {pro}")
print(F"{x}/{y}= {div}")
print(F"max({x},{y}) = {max}")
print(F"min({x},{y}) = {min}")
print(F"{x}^{y} = {power}")
print(F"gcd({x},{y}) = {gcd}")
print(F"sqrt({x}) = {sqrt}")
print(F"fact({x}) = {f}")
'''

#swap ref
'''
x=input('enter 1st input:')
y=input('enter 2nd input:')
print(F"Before swap: {x=} /t {y=} ")
x,y = y,x
print(F"After swap:  {x=} /t  {y=} ")
'''

# largest
'''
x=input('enter 1st input:')
y=input('enter 2nd input:')
print("largest input:", x if x>y else y)
'''

# three  inputs
'''
x=input('enter 1st input:')
y=input('enter 2nd input:')
z= input('enter 3rd input:')
print("largest input:", x if x>y else y if y>z else z if z>y else z)
'''

# large
'''
x=input('enter 1st input:')
y=input('enter 2nd input:')
print("Result:", '>' if x>y else '<' if x<y else '=')
'''

# sign
'''
x=int(input('enter any number :'))
print("Result:", 1 if x>0 else -1  if x<0 else 0 )
'''

# odd even
'''
x=int(input('enter any +ve integer :'))
print("Result:", 'Even number' if x%2==0 else 'Odd number')
 '''
