# program to find max,min and middle of three numbers
#  Reading inputs
x=int(input("enter first number : "))
y=int(input("enter second  number : "))
z=int(input("enter  third number : "))
# taking initial max,min values
max=x
min=y
#condition for max
if y>max: #if y is greater than current max
    max=y # max is y
    
elif z>max: #if z is greater than current max
    max=z # max is z
    
else:
    max=x # maximum is X
# condition for min    
if x<min:#if x is less than current min
    min=x #min is x
elif z<min: #if z is less than current min
    min=z  # min is z
else:
    min=y  # min is y
# finding middle   
middle=(x+y+z)-(max+min)
#printing outputs
print("max = ",max)
print("min = ",min)
print("middle = ",middle)

# wrute program to convert farenheit to celsius and celsius to Farenheit
# reading inputs 

x=int(input("Enter 1 to celsius to farenheit and 2 for Fareheit  to celsius: "))

# logic
try:
    if x==1:
        y=int(input("Enter Celsius temperature : "))
        fah=1.8*y+32
        print("Farenheit Equivalent :",fah)
    elif x==2:
        y=int(input("Enter Farenheit temperature : "))
        cel=(y-32)/1.8
        print(f"Celsius Equivalent :{cel:.2f}")
    else:
        print("Enter a number 1 or 2")
except:
    print("Input should be integer")


#write a program to find (x,y) points inside ,outside or on the circle

# imprting and reading inputs
import math 
x=int(input("enter value of x : "))
y=int(input("enter value of y : "))
z=int(input("enter  radius of circle : "))
#finding distance 
distance=math.sqrt(x**2 + y**2)
#logic and print outputs
if distance>z:
    print("point outside the circle")
elif distance==z:
    print("point on the circle")
else:
    print("point inside the circle")

#write a program for fibonacci series using while loop
#reading input
x=int(input("Enter a Number : "))

# initial values
a=0
b=1
c=a+b

#logic and printing output
if x==a:
    print(a)
elif x==b:
    print("Fibonacci series :",a,b,sep="\n")
else:
    print("Fibonacci series :",a,b,sep="\n")
    while c < x:
        print(c)
        a=b
        b=c
        c=a+b


# write a program to find largest of three elements
# READING INPUTS 
x=eval(input("enter first number : "))
y=eval(input("enter second  number : "))
z=eval(input("enter  third number : "))

# computations and deriving results
largest=x # taing initial largest 
if y>largest:
    largest=y
    print("Largest : ",y)
elif z>largest:
    largest=z
    print("Largest : ",z)
else:
    print("Largest : ",x)
    

# write a program to find Leap year
try:
    x=int(input("Enter year : "))

    if (x%4==0 and x%100!=0 )or (x%400==0) :
        print("Leap year")
    
    else:
        print("Not Leap year")
    
except:
    print("Year must be Integer")

# write a program to find a month name in year by nummber

try:
    x=int(input("Enter month number (1-12) : "))
    dict={1:'January',2:'Feburary',3:'March',4:'April',5:'May',6:'June',
          7:'July',8:'August',9:'September',10:'October',11:'november',12:'December'}
    if x in dict:
        print(dict[x])
    else:
        print("enter number in between (1-12)")
except:
    print("input should be integer")

# write a progam to find the position of point(x,y) Quadrants graph
#reading inputs
x=float(input("enter value of x-coordinate : "))
y=float(input("enter value of y-coordinate  : "))
#conditions for all 4 quadrants ,on x-axis,y-axis,origin
if x>0 and y>0:
    print("1st quadrant")
elif x<0 and y>0:
    print(" 2nd quadrant")
elif x<0 and y<0:
    print("3rd quadrant")
elif x>0 and y<0:
    print("4th quadrant")
elif x==0 and y==0:
    print("Origin")
elif x==0 and y!=0:
    print("On y-axis")
elif x!=0 and y==0:
    print("On x-axis")


# write aprogram to find roots 
# importing math and reading values of x,y,z
from math import sqrt 
x=int(input("enter value of x : "))
y=int(input("enter value of y : "))
z=int(input("enter value of z: "))
# conditions
if x!=0:
    dis=y**2-4*x*z
    if dis>0:
        root1=(-y+sqrt(dis))/(2*x)
        root2=(-y-sqrt(dis))/(2*x)
        print("Roots are Real and Distinct")
        print(f"Root1: {root1:.2f}")
        print(f"Root2: {root2:.2f}")
    elif dis==0:
        root1=-y/(2*x)
        root2=-y/(2*x)
        print("Roots are Real and Equal")
        print(f"Root1: {root1:.2f}")
        print(f"Root2: {root2:.2f}")
    else:
        real=-y/(2*x)
        imaginary=sqrt(abs(dis))/(2*x)

        print("Roots are Imaginary or complex")
        print(f"Root1: {real}+{imaginary}")
        print(f"Root2: {real}-{imaginary}")

else:
    print("Value of 'x' can not be 0 ")


# write a program to find type of trainge by sides
# reading inputs or sides and importing math module
import math
x=int(input("enter 1st side : "))
y=int(input("enter 2nd side : "))
z=int(input("enter  3rd side  : "))
#sum of two sides
X=x+y
Y=y+z
Z=z+x
# conditions
if X>z and Y>x and Z>y:
    #equilateral triangle condition
    if x==y==z :
        print("Equilateral Triangle")
        area=math.sqrt(3)/4*x**2
        print(f"Area of Equilateral triangle : {area:.2f}")
    # Isoscles triangle condition
    elif x==y or y==z or z==x: 
        print("Isoscles Triangle")
        perimeter=x+y+z
        print(f"Perimeter of Isosceles triangle : {perimeter}")
    # Scalene triangle condition
    else:
        print("Scalene Triangle")
        s=(x+y+z)/2
        area=math.sqrt(s*(s-x)*(s-y)*(s-z))
        perimeter=x+y+z
        print(f"Area of Scalene triangle : {area:.2f}")
        print(f"Perimeter  of Scalene triangle : {perimeter}")                
else:
    print("Not a Triangle")

# write a code to find day name in week by number using match & case 
m=int(input("Enter value :"))
try:
    match m:
        case 1:
            print("MOnday")
        case 2:
            print("Tuesday")
        case 3:
            print("Thursday")
        case 5:
            print("Wednesday")
        case 6:
            print("Friday")
        case 7:
            print("Sunday")
        case 8:
            print("invalid")
except:
    print("input should be integer")

 
