'''
1.Write  a  program  to  determine  area  and  perimeter  of  rectangle

Enter  length  of  rectangle  : 4
Enter  breadth  of  rectangle :  5
Area  :  20.00
Perimeter :  18.00

'''

'''
try:
    l=float(input("Enter  length  of  rectangle  :"))
    b=float(input("Enter  breadth  of  rectangle  :"))
    print(f"Area :{l*b:.2f}")
    print(f"Perimeter :{2*(l+b):.2f}")
    
except:
    print("for l,b enter only int or float values")

'''


'''
2.Write  a  program  to  determine  volume  of  a  sphere

Enter  radius  :  3.5
Volume  :  179.59
'''

'''
from math import pi 
try:
    r=float(input("Enter  radius of sphere :"))
    print(f"Volume :{(4/3*pi*r**3):.2f}")
    
except:
    print("for r enter only int or float values")
  
'''  

'''
3.Write  a  program  to  determine  simple  interest  and  compound  interest
Enter  principle  :  10000
Enter  time  : 3
Enter  rate  of  interest :  7.5
Simple  Interest : 2250.00
Compound  Interest : 2422.97

'''

'''
try:
    p=float(input("Enter  principle :"))
    t=float(input("Enter time :"))
    r=float(input("Enter rate of interest :"))
    print(f"Simple  Interest :{(p*t*r/100):.2f}")
    print(f"Compound  Interest :{(p*(1+r/100)**t-p):.2f}")
    
except:
    print("for p,t,r enter only int or float values")

'''

'''
4.5.6.7 Write  a  program  to  swap  values  of  two  objects  with temp,(+,-),(*,//),(^),
(one line without 3rd variable)

Enter  1st  input  : 10
Enter  2nd  input  : 25
Before  swap :  x=10      y=25
After  swap :  x=25       y=10
'''

'''
print("swap with temp")
x=eval(input("Enter  1st  input  :"))
y=eval(input("Enter  2nd  input  :"))
print(f"Before  swap : {x=} {y=}")
temp=x 
x=y 
y=temp
print(f"After  swap : {x=} {y=}")


print("swap with + and -")
x=eval(input("Enter  1st  input  :"))
y=eval(input("Enter  2nd  input  :"))
print(f"Before  swap : {x=} {y=}")
x=x+y 
y=x-y 
x=x-y 
print(f"After  swap : {x=} {y=}")


print("swap with * and /")
x=eval(input("Enter  1st  input  :"))
y=eval(input("Enter  2nd  input  :"))
print(f"Before  swap : {x=} {y=}")
x=x*y 
y=x//y 
x=x//y 
print(f"After  swap : {x=} {y=}")


print("swap with  ^")
x=eval(input("Enter  1st  input  :"))
y=eval(input("Enter  2nd  input  :"))
print(f"Before  swap : {x=} {y=}")
x=x^y 
y=x^y 
x=x^y 
print(f"After  swap : {x=} {y=}")


print("swap in one line with multiple assignment")
x=eval(input("Enter  1st  input  :"))
y=eval(input("Enter  2nd  input  :"))
print(f"Before  swap : {x=} {y=}")
x,y=y,x
print(f"After  swap : {x=} {y=}")

'''


'''
8.Write  a  program  to  add ,  subtract , multiply  and  divide  two  complex  numbers

Enter first complex number : 3+4j
Enter second complex number: 5+6j
Sum :  (8+10j)
Difference :  (-2-2j)
Product:  (-9+38j)
Division :  (0.6393442622950819+0.03278688524590165j)

'''

'''
try:
    a=complex(input("Enter first complex number :"))
    b=complex(input("Enter second complex number :"))
    
    print(f"Sum :{a+b}")
    print(f"Difference :{a-b}")
    print(f"Product :{a*b}")
    print(f"Division :{a/b}")
    
except:
    print("for a,b enter a real number")


'''


'''
9.Write  a  program  to  determine  sum , difference , product , quotient , largest  and  
smallest  of  two  numbers.Also  find  remainder,  sqrt  of  first  input , power, gcd  
and  factorial  of  first  input


Enter 1st  integer  number :  10
Enter 2nd  integer  number :  7
10 + 7 = 17
10 - 7 = 3
10 * 7 = 70
10 / 7 = 1.4285714285714286
10 % 7 = 3
max(10 , 7) = 10
min(10 , 7) = 7
10 ^ 7 = 10000000
sqrt(10) = 3.1622776601683795
gcd(10 , 7) = 1
fact(10) = 3628800

'''

'''
from math import *
try:
    a=int(input("Enter 1st  integer  number :"))
    b=int(input("Enter 2nd  integer  number :"))
    print(f"{a} + {b} = {a+b}")
    print(f"{a} - {b} = {a-b}")
    print(f"{a} * {b} = {a*b}")
    print(f"{a} / {b} = {a/b}")
    print(f"{a} % {b} = {a%b}")
    print(f"max({a} , {b}) = {max(a,b)}")
    print(f"min({a} , {b}) = {min(a,b)}")
    print(f"{a} ^ {b} = {a**b}")
    print(f"sqrt({a}) = {sqrt(a)}")
    print(f"gcd({a} , {b})= {gcd(a,b)}")
    print(f"fact({a})= {factorial(a)}")
    
except:
    print("for a,b enter only int")
    
'''


'''
10.Write  a  program  to  determine  largest  of  two  inputs  without  using  max()  function

Enter 1st input : 'Rama'
Enter 2nd input : 'Rajesh'
Largest  Input  :   Rama

'''

'''
a=eval(input("Enter 1st input :"))
b=eval(input("Enter 2nd input :"))
print(f"Largest  Input  :{a if a>b else b }")

'''

'''
11.Write  a  program  to  determine  largest  of  three  inputs  without  using  max()  function

Enter 1st input : [10,20,15,18]
Enter 2nd input : [10,20,32,19]
Enter 3rd input : [10,20,25,17]
Largest  Input  :  [10, 20, 32, 19]

'''

'''
a=eval(input("Enter 1st input :"))
b=eval(input("Enter 2nd input :"))
c=eval(input("Enter 3rd input :"))
print(f"Largest  Input  :{a if a>b and a>c else b if b>c else c }")

'''

'''
12.Write  a  program  to  print   '>'  if  1st  input  >  2nd  input,
                                  '<'  if  1st  input  <  2nd  input  and
                                  '='  if  inputs  are  same
                                
Enter 1st input : 10
Enter 2nd input : 20
Result :   <
'''

'''
a=eval(input("Enter 1st input :"))
b=eval(input("Enter 2nd input :"))
print(f"Result : {'>' if a>b else '<' if a<b else '='}")
'''


'''
13.Write  a  program  to  print  1  if  input  is  +ve  ,  -1    if  input  is  -ve  and  0  if  input  is  0

Enter any number : -25
Result :  -1

'''

'''
try:
    a=float(input("Enter any number :"))
    print(f"Result : {1 if a>0 else -1 if a<0 else 0}")
    
except:
    print("for a enter only int or float")

'''

'''
14.Write  a  program  to  test  input  is  even  number  or  odd  number

Enter any +ve integer : 26
Even  number

'''


try:
    a=int(input("Enter any +ve integer :"))
    print("Even" if a%2==0 else "Odd")
    
except:
    print("for a enter only +ve integer")
    
