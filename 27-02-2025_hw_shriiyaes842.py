
#1
b=int(input("enter the bredth :"))
l=int(input("enter the length :"))
area = l*b
perimeter=2*(l+b)
print(F'Area :{area:.2f}')
print(F'perimeter : {perimeter:.2f}')


#2
import math
r=float(input("enter the radius :"))
v=4/3 * math.pi * r**3
print(F'Volume : {v:.2f}')


#3
p=float(input("enter the amount :"))
r=float(input("enter the interest rate :"))
t=float(input("enter the time :"))
simple_interest= (p*t*r) /100
print(F"simple interest : {simple_interest:.2f}")
compound_interest=p*(1+r/100)**t - p
print(F"compound interest : {compound_interest:.2f}")


#4
x=int(input("enter the first value :"))
y=int(input("enter the second value :"))
print(F"before swap : x={x} y={y} ")
temp=x
x=y
y=temp
print(F"after swap : x={x} y={y}")

#5
x=int(input("enter the first value :"))
y=int(input("enter the second value :"))
print(F"before swap : x={x} y={y} ")
y=x+y
x=y-x
y=y-x
print(F"after swap : x={x} y={y}")

#6
x=float(input("enter the first value :"))
y=float(input("enter the second value :"))
print(F"before swap : x={x} y={y} ")
y=x*y
x=y/x
y=y/x
print(F"after swap : x={x} y={y}")


#7
c1=complex(input("enter a 1st complex number: "))
c2=complex(input("enter a 2nd complex number: "))
print(f"Addition = {c1+c2}")
print(f"Subtraction = {c1-c2}")
print(f"Multiplication = {c1*c2}")
print(f"Division = {c1/c2}")



#8
import math
a=int(input("Enter 1st  integer  number :"))
b=int(input("Enter 2nd  integer  number :"))
print(F'{a} + {b} = {a+b}')
print(F'{a} - {b} = {a-b}')
print(F'{a} * {b} = {a*b}')
print(F'{a} / {b} = {a/b}')
print(F'{a} % {b} = {a%b}')
print(f'max({a},{b}) =',max(a,b))
print(f'min({a},{b}) =',min(a,b))
print(f'sqrt({a}) =',math.sqrt(a))
print(f'gcd({a},{b}) =',math.gcd(a,b))
print(f'fa,ct({a}) =',math.factorial(a))


#9
x=(input("enter the first value :"))
y=(input("enter the second value :"))
print(F"before swap : x={x} y={y} ")
x,y=y,x
print(F"after swap : x={x} y={y} ")


#10
a=(input("Enter 1st input:"))
b=(input("Enter 2nd input:"))
if a>b:
    print(a)
else:
    print(b)

#11
a=(input("Enter 1st input:"))
b=(input("Enter 2nd input:"))
c=(input("Enter 3rd input:"))
if a>=b and a>=c:
    print("Largest  Input : ",a)
elif b>=a and b>=c:
    print("Largest  Input : ",b)
else:
    print("Largest  Input : ",c)


#12
a=(input("Enter 1st input:"))
b=(input("Enter 2nd input:"))

if a>b:
    print(">")
elif a<b:
    print("<")
else:
    print("=")



#13
n= int(input("Enter a number: "))
if n > 0:
    print('Result:',1)
elif n < 0:
    print('Result:',-1)
else:
    print('Result:',0)


#14
n= int(input("Enter a +ve number: "))
if n%2==0:
    print("even number")
else:
    print("odd number")

