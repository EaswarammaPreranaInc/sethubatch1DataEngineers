# write a program to print the given number is odd or even using if 
"""
try:
    a=int(input("enter the number in integer : "))
    if (a%2==0):
        print(f"{a} is even number ")
    else:
        print(f"{a} is odd number ")
except:
    print("plese enter a valid number")
    

"""
# write a program to print month name dor the user input number using if and else 
'''
try:
    a=int(input("enter the month that you want from (1-12) : "))
    if a==1:
        print("january")
    elif a==2:
        print("february")
    elif a==3:
        print("march")
    elif a==4:
        print("april")
    elif a==5:
        print("may")
    elif a==6:
        print("june")
    elif a==7:
        print("july")
    elif a==8:
        print("august")
    elif a==9:
        print("sepetember")
    elif a==10:
        print("octomber")
    elif a==11:
        print("november")
    elif a==12:
        print("december")
    else:
        print("plese enter the valid number between 1 and 12")
except:
    print("enter the valid input number")

'''

# write a program to test the leap year or not 
'''
try:
    a=eval(input("enter the year : "))
    if ((a%4==0) or (a%400==0)) and (a%100!=0) :
        print(f"{a} is leap year ")  
    else:
        print(f"{a} is not a leap year ")
except:
    print("is not the valid year")

    
'''


# write a program to determine largest of numbers with if and else 
'''
a=eval(input(" enter the 1st input : "))
b=eval(input(" enter the 2nd input : "))
c=eval(input(" enter the 3rd input : "))
if a>b and a>c:
    print("largest number is :",a)
elif b>a and b>c:
    print("largest number is :",b)
elif c>a and c>b:
    print("largest number is :",c)
else:
    print("not a valid numbers")



a=int(input("enter the a: "))
b=int(input("enter the b: "))
c=int(input("enter the c: "))
print(a if(b<a>c) else b if(a<b>c) else c if (a<c>b) else "invalid")


a=1
b=2
c=3
print((f"{a} is the largest number")if (a>b or a>c) else (f"{b} is the largest number") if (b>a or b>c) else (f"{c} is the largest number ") if (c>a or c>b) else("invalid"))
'''


# write a program to convert celsius ,temperature to farenheit and vice-versa
'''
try:
    a=int(input("enter 1 to convert celsius to farenheit : enter 2 to convert farenheit to celsius : "))
    match a:
            case 1:
                b=float(input("enter celsius to convert to farenheit : "))
                print("farenheit equalent : ",1.8*b+32)
            case 2:
                c=float(input("enter farenheit to convert to celsius : "))
                print("celsius equalent : ",(c-32)/1.8)
            case _:
                print("pick from 1 and 2")
except:
    print("given value is must be in float or integer ")

'''

# write a program to test a point (x,y) lies in 1st quadrent ,2nd ,3rd and 4th and in x-axis ,y-axis or origin 
'''
a=int(input("enter the x co-ordinate : "))
b=int(input("enter the y co-ordinate : "))
print("1st quadrant" if (a>0 and b>0) else "2nd qudrent" if (a<0 and b>0) else "3rd qudrent" if (a<0 and b<0) else "4th qudrent" if (a>0 and b<0) else "on x-axis" if (a!=0 and b==0) else "on y-axis" if (a==0,b!=0) else "in origin" if (a,b)==0 else"invalid")

'''
# write a program to determine the largest ,smallest and middle of three numbers 
'''
try:
    a=float(input("enter the first input : "))
    b=float(input("enter the second input : "))
    c=float(input("enter the third input : ")) 
    maxv=a if(b<a>c) else b if(a<b>c) else c if (a<c>b) else "invalid"
    print("Largest number : ",maxv)
    minv=a if(b>a<c) else b if(a>b<c) else c if (a>c<b) else "invalid"
    print("Smallest number : ",minv)
    middle=(a+b+c)-(maxv+minv)
    print("midddle number : ",middle)
except:
    print("invalid value")

'''
# write a program to determine the three sides from a triangle or not 
"""
import math
a=float(input("enter the 1st side : "))
b=float(input("enter the 2nd side : "))
c=float(input("enter the 3rd side : "))
if (a+b)>=c and (b+c)>=a and (c+a)>=b:
    if(a==b==c):
        print("Equilateral Triangle")
        print("Area : ",math.sqrt(3)/4*a**2)
    elif(a==b)|(b==c)|(c==a):
        print("isosceles triangle")
        print("perimeter :",a+b+c)
    elif(a!=b!=c):
        print("scalen triangle")
        s=a+b+c/2
        print("s value of the given inputs :",s)
        v=math.sqrt((s*(s-a)*(s-b)*(s-c)))
        print(f"Area :{v:.2f} ")
        print("perimeter :",a+b+c)
else:
    print("not a triangle")


"""
# write a program to determine the roots of a quadratatic equation a a*x^2+b*x+c=0 when a!=0
'''
import math
try:
    a=eval(input("enter the value of a : "))
    if a==0:
        print("value canot be zero")
    else:
        b=eval(input("enter the value of b : "))
        c=eval(input("enter the value of c : "))
        dis=b**2-(4*a*c)
        if dis>0:
            print(" Roots are Real and distinct")
            print("Root 1 : ",((-b)+math.sqrt(dis))/(2*a))
        
            print("Root 2 : ",((-b)-(math.sqrt(dis)))/(2*a))
        elif dis==0:
            print(" Roots are Real and Same")
            print("Root 1 : ",-b/(2*a))
            print("Root 2 : ",-b/(2*a))
        elif  dis<0:
            print("Roots are Complex (or) imaginary roots")
            real=-b/(2*a)
            img=(math.sqrt(-dis))/(2*a)
            print(f"Root 1 : {real} + {img}j")
            print(f"Root 1 : {real} - {img}j")
except:
    print("special characters not allowed")

'''

# write a program to determine a point (x,y) lies inside,outside,or on the circle. center is origin and radius is "r"
'''
try:
    import math
    a=int(input("enter the value of x :"))
    b=int(input("enter the value of y :"))
    d=int(input("enter the radius of the circle : "))
    r=(math.sqrt((a**2)+(b**2)))
    if d>r:
        print("outside of the circle")
    elif (d<r):
        print("inside of the circle")
    elif d==r:
        print("point is on the circle")
except:
    print("enter a valid number")


'''

# write a program to print day of the week 
'''
try:
    a=int(input("enter the value from (1-7) : "))
    match a:
        case 1:
            print("monday")
        case  2:
            print("tuesday")
        case 3:
            print("wednesday")
        case 4:
            print("thursday")
        case 5:
            print("friday")
        case 6:
            print("saturday")
        case 7:
            print("sunday")
        case 8:
            print("invalid")
except:
    print("no other characters")

'''
# write a program to print digit in words using match
'''
try:
    a=int(input("enter the value from (0-9) : "))
    if (a>=9):
        print("not a digit")
    else:
        match a:
            case 0:
                print("zero")
            case 1:
                print("one")
            case  2:
                print("two")
            case 3:
                print("three")
            case 4:
                print("four")
            case 5:
                print("five")
            case 6:
                print("six")
            case 7:
                print("seven")
            case 8:
                print("eight")
            case 9:
                print("nine")
except:
    print("not a digit")

'''
# write a program to determine bill amount and input is units 
'''
Units                                                      Cost
------------------------------------------------------------
First  100  units								Rs. 3.00 / unit

Next  100  units								Rs. 3.50 / unit

Next  200  units								Rs. 4.00 / unit

Next  300  units								Rs. 4.50 / unit

Above  700  units								Rs. 5.00 / unit
---------------------------------------------------------------
Let  units  be  1200
What  is  the  bill  amount ? --->  100 * 3.00 + 100 * 3.50 + 200 * 4.00 + 300 * 4.50 +  500 * 5.00

Hint:  Use  match  ...  case   but  not  if ... else
'''
"""
units=eval(input("enter the number of units : "))
f100=units*3.00
n100=units*3.50
n200=units*4.00
n300=units*4.50
above700=units*5.00
match units:
    case units if (units<=100):
        print(f"the cost of {units} units :",f100)
        print(f"Total bill amount of : {units} units :",f100)
    case units if (units>100 and units<=200):
        print(f"the cost of {units} units is : ",n100)
        print(f"Total bill amount of : {units} units :",n100)
    case units if (units>200 and units<=700):
        print(f"the cost of {units} units is :",n200)
        print(f"Total bill amount of : {units} units:",n200)
    case units:
        print(f"the cost of {units} units is :",above700)
        print(f"Total bill amount of : {units} units :",above700)
"""

# write a program to print fibonacci series upto x using while
"""
x=int(input("enter the value to print series upto : "))
if x==0:
    print('fibonacci')
    print(x)
else:
    a=0
    b=1
    c=a+b
    print(a)
    print(b)

while c<=x:
    print(c)
    a=b
    b=c
    c=a+b

"""
#  my method: 
"""
a=int(input("enter the number : "))
if a==0:
    print("0")
elif(a==1):
        print('0')
        print('1')
else:
    x,y,c=0,1,0
    while c<=a:
        print(c)
        x,y=y,c
        c=x+y
        """

