#  1 rectangle area and perimeter
#### rectangle.area.perimeter
length=float(input("length:"))
breadth=float(input("breadth:"))
area=length*breadth
perimeter=2*(length+breadth)
print("area:",length*breadth)
print("perimeter:",2*(length+breadth))
print(f"area:{area:.2f}")
print(f"perimeter:{perimeter:.2f}")
#2 Write  a  program  to  determine  volume  of  a  sphere
from math import *
radius=float(input("enter radius:"))
volume=(4/3)*pi*pow(radius,3)
print(f"volume:{volume:.2f}")
#3 Write  a  program  to  determine  simple  interest  and  compound  interest
from math import *
p=float(input("enter principal amount:"))
t=float(input("enter Time period:"))
r=float(input("enter rate of interest:"))
si=p*t*r/100
ci=(p*pow((1+r/100),t))-p
print(f" simple interest:{si:.2f}")
print(f" compound interest:{ci:.2f}")
#4 Write  a  program  to  swap  values  of  two  objects  using  3rd   object
x=0
y=6
temp=x
x=y
y=temp
print(x)
print(y)
print(" before swap x: ",y, "after swap x: ",x)
print(" before swap y: ",x ,"after swap y: ",y)
# 5 Write  a  program  to  swap  values  of  two  objects  without  using  3rd  object
x=5
y=4
print((x+y)-x)
print((x+y)-y)
print((x*y)//x)
print((x*y)//y)
# 6 Write  a  program  to  add ,  subtract , multiply  and  divide  two  complex  numbers
a = complex(input("Enter a: "))
b = complex(input("Enter b: "))
print('sum :',a+b)
print('Difference :',a-b)
print('Product :',a*b)
print('Division:',a/b)
#7 Write  a  program  to  determine  sum , difference , product , quotient , largest  and  smallest  of  two  numbers.
#Also  find  remainder,  sqrt  of  first  input , power, gcd  and  factorial  of  first  input
a = int(input("Enter 1st  integer  number : "))
b = int(input("Enter 2nd  integer  number : "))
print(f"{a}+{b}={a+b}")
print(f"{a}-{b}={a-b}")
print(f"{a}*{b}={a*b}")
print(f"{a}/{b}={a/b}")
print(f"{a}//{b}={a//b}")
print(f"{a}%{b}={a%b}")
print(f"max({a},{b})={max(a,b)}")
print(f"min({a},{b})={min(a,b)}")
print(f"{a}^{b}={a**b}")
print(f"sqrt({a} and {b})={a**0.5} and {b**0.5}")
from math import *
print(f"{a}^{b}={pow(a,b)}")
print(f"sqrt({a} and {b})={sqrt(a)} and {sqrt(b)}")
def gcd(x,y):
    for i in range(1,min(x,y)+1):
        gcd=1
        if x%i==0 and y%i==0:
            gcd=i
    return gcd
print(f"gcd({a},{b})={gcd(a,b)}")
def fact(number):
    f=1
    for i in range(1,number+1):
        f=f*i
    return f
print(f"fact({a} and {b})={fact(a), fact(b)}")
# 8 Write  a  program  to  swap  values  of  any  two  objects  in  a  single  statement  without  using  3rd  object
x="hyd"
y=4
x,y=y,x
print(x)
print(y)
# 9 Write  a  program  to  determine  largest  of  two  inputs  without  using  max()  function
a = (input("Enter 1st input : "))
b = (input("Enter 2nd input : "))
print("Largest  Input  :",a if a>b else b)
# 10 Write  a  program  to  determine  largest  of  three  inputs  without  using  max()  function
a = (input("Enter 1st input : "))
b = (input("Enter 2nd input : "))
c = (input("Enter 3rd input : "))
print("Largest  Input  :",a if (a>b and a>c) else (b if b>c  else c ))
# 11 Write  a  program  to  print   '>'  if  1st  input  >  2nd  input,
#'<'  if  1st  input  <  2nd  input  and
# '='  if  inputs  are  same use ternary
a = (input("Enter 1st input : "))
b = (input("Enter 2nd input : "))
print(">" if a>b else("<" if a<b else "="))
# 12 Write  a  program  to  print  1  if  input  is  +ve  ,  -1    if  input  is  -ve  and  0  if  input  is  0
a = int(input("Enter any integer : "))
print(1 if a>0 else(-1 if a<0 else 0))
# 13 Write  a  program  to  test  input  is  even  number  or  odd  number
a = int(input("Enter any integer : "))
print("even" if a%2==0 else "odd")
