length=int(input("Enter length of rectangle:" ))
breadth=int(input("Enter breadth of rectangle:" ))
print("Area :",length*breadth)
print("Perimeter :",2*(length+breadth))

import math
radius=eval(input("Enter radius :"))
volume=4/3*math.pi*radius**3
print("Volume : ",f"{volume:.2f}")

r=eval(input("Enter rate of interest :"))
s=(p*t*r)/100
c=p*(1+r/100)**t-p
print("Simple Interest :",f"{s:.2f}")
print("Compound Interest :",f"{c:.2f}")

x=int(input("Enter 1st input :"))
y=int(input("Enter 2nd input :"))
print("Before swap :"f"{x=}",f"{y=}")
c=x
x=y
y=c
print("After swap :"f"{x=}",f"{y=}")

x=int(input("Enter 1st input :"))
y=int(input("Enter 2nd input :"))
print("Before swap :"f"{x=}",f"{y=}")
x=x+y
y=x-y
x=x-y
print("After swap :"f"{x=}",f"{y=}")

x=int(input("Enter 1st input :"))
y=int(input("Enter 2nd input :"))
print("Before swap :"f"{x=}",f"{y=}")
x=x*y
y=x/y
x=x/y
print("After swap :"f"{x=}",f"{y=}")

c1=complex(input("enter a 1st complex number: "))
c2=complex(input("enter a 2nd complex number: "))
addition=c1+c2
substract=c1-c2
multiplication=c1*c2
division=c1/c2
print(f"Addition = {addition}")
print(f"Subtraction = {substract}")
print(f"Multiplication = {multiplication}")
print(f"Division = {division}")

import math
x=int(input("Enter 1st integer number :"))
y=int(input("Enter 2nd integer number :"))
print(x,"+",y,"=",x+y)
print(x,"-",y,"=",x-y)
print(x,"*",y,"=",x*y)
print(x,"/",y,"=",x/y)
print(x,"%",y,"=",x%y)
print(max(x,y))
print(min(x,y))
print(pow(x,y))
print(math.sqrt(x))
print(math.gcd(x,y))
print(math.factorial(x))

x=eval(input("Enter 1st input :"))
y=eval(input("Enter 2nd input :"))
print("Before swap :"f"{x=}",f"{y=}")
x,y=y,x
print("After swap :"f"{x=}",f"{y=}")

x=eval(input("Enter 1st input :"))
y=eval(input("Enter 2nd input :"))
print(x if x>y else y)

x=eval(input("Enter 1st input :"))
y=eval(input("Enter 2nd input :"))
z=eval(input("Enter 3rd input :"))
print(x if (x>y and x>z) else (y if (y>x and y>z) else z))

x=int(input("Enter 1st input :"))
y=int(input("Enter 2nd input :"))
print('<' if x<y else ('>' if (x>y) else '='))

x=int(input("Enter 1st input :"))
print('1' if x>0 else ('-1' if (x<0) else '0'))

x=int(input("Enter 1st input :"))
print('Even' if x%2==0 else 'Odd')

