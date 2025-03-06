# AREA AND CIRCUMFERENCE OF THE OF CIRCLE
import math
try:
        r=float(input("Enter the value of radius r:"))
        area=math.pi*r**2
        Cir=2*math.pi*r
        print(F'Area={area:0.2f}')
        print(F'Cirmference={Cir:0.2f}')
        # print(area)
        # print(Cir)
        # print("Area of circle:"+str(area))
        # print("Cirecumference of circle is:"+str(Cir))
except:
        print("input should be a  number")




---------------------------------------------------------------------------
# AREA AND PERIMETER OF THE RECTANGLE

import math
try:
    l=float(input("Enter the value of l:"))
    b=float(input("Enter the value of b:"))
    area=l*b
    perimeter=2*(l+b)
    print(F'Area of rectangel is={area}')
    print(F'Perimeter of the rectangel is {perimeter}')
except:
    print("Please enter the only values of l,b not string")


------------------------------------------------------------------------------------
#VOLUME OF THE SPHERE

import math
r=float(input("Enter the value of radius r:"))
vol=4/3*math.pi*r**3
print(F'Volume of the sphere is={vol:.2f}')



---------------------------------------------------------------------------------------
#SIMPLE INTEREST AND COMPOUND INTEREST PROBLEMS

import math
p=float(input("Enter the princeple amount:"))
t=float(input("Enter the time taken:"))
r=float(input("Enter the rate of interest:"))
# p,t,r=[eval(input the principle, time, rate of interest separated by comma).split(',')]
siminterest=(p*t*r)/100
cominterest=p*(1+r/100)**t-p
print(F'simple interest={siminterest}')
print(F'compound interest={cominterest:.2f}')




----------------------------------------------------------------------------------------------
#SWAPPING OF TWO NUMBERS WITH 3RD VARIABLE

x=int(input('Enter the value of x:'))#10
y=int(input('Enter the value of y:'))#25
print('Before swap:', x,y)
a=x
x=y
y=a
print('After swap:', x,y)


----------------------------------------------------------------------------------------------
#SWAPPING OF TWO NUMBERS WITHOUT 3RD VARIABLE

x=int(input('Enter the value of x:'))
y=str(input('Enter the value of y:'))
print('Before swap:', x,y)
x,y=y,x
print('After swap:', x,y)


-----------------------------------------------------------------------------------------------

#SWAPPING OF TWO NUMBERS WITHOUT ADD AND MUL

x=int(input('Enter the value of x:'))#7
y=int(input('Enter the value of y:'))#14
print('Before swap:', x,y)
# x,y=y,x
x=x+y
y=x-y
x=x-y
print('After swap:', x,y)



--------------------------------------------------------------------------------------------
#OPERATIONS OF COMPLEX NUMBERS
x1=complex(input('Enter the value of x1:'))
x2=complex(input('Enter the value of x2:'))
add=x1+x2
sub=x1-x2
mul=x1*x2
div=x1/x2
print('sum:', add)
print('Difference:', sub)
print('Product:', mul)
print('Division:', div)
