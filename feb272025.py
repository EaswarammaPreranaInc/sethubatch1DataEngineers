# write a program to determine the area and perimeter of rectangle 
"""try:
    a=eval(input("Enter the length of a rectangle: "))
    b=eval(input("Enter the breath of yhe rectangle: "))
    c=a*b#area
    d=2*(a+b)#breadth 
    print(f"Area :{c:.2f}")
    print(f"perimeter:{d:.2f}")
except:
    print("values must be an integer or a float to find the area and perimeter of a rectangle")"""


# write a program to determine the volume of a sphere
"""
import math
try:
    a=eval(input("enter the radius of the sphere :"))
    s=(4/3)*(math.pi)*(a**3)
    print(f"{s:.2f}")
except:
    print("value cannot be a character ")"""


# write a program to determine simple and compound intrest
"""
try:
    a=eval(input("enter the principle amount : "))
    b=eval(input("enter the tenure time : "))
    c=eval(input("enter the rate of intrest : "))
    if a<0:
        print("not possible")
    else:
        si=((a*b*c)/100)
        ci=a*(1+c/100)**b-a
        print(f"simple intrest :{si:.2f}")
        print(f"compount intrest :{ci:.2f}")
except:
    print("enter the valid value")"""

# write a program to swap the values of two objects using third object 
"""
a=input("enter the 1st value: ")
b=input("enter the 2nd value: ")
print(f"before swap :a : {b} \t b :{a}")
c=a
a=b
b=c
print(f"before swap :a :{a}\t b :{b}")"""

# with out third object swap tow numbers 
"""
a=input("enter the 1st value: ")
b=input("enter the 2nd value: ")
print(f"before swap :a : {b} \t b :{a}")
a,b=b,a
print(f"after swap  : a: {a} \t b :{b}") 
"""
#wite a program to swap values of two objects without using 3rd object 
# hint : one addition and two subtractions 
'''
a=eval(input("enter the 1st value : "))
b=eval(input("enter the 2nd value : "))
print(f"before swaping a: {a} \t b: {b}")
a+=b
b=a-b
a=a-b
print(f"before swaping a: {a} \t b: {b}")


a=int(input(""))
b=int(input(""))
c=int(input(""))
print(a,b,c)
a,b,c=c,a,b
print(a,b,c)


'''

# write a program to swap values of two objects with out using 3rd object
# hint : one multiplicatioln and two divisions

"""
a=eval(input("enter the 1st value : "))
b=eval(input("enter the 2nd value : "))
print(f"before swaping a: {a} \t b: {b}")
a*=b
b=a/b
a=a/b
print(f"after swaping a: {a} \t b: {b}")"""

# write a program to add, subtract,multiply,divide two comlpex numbers 
"""
a=eval(input("enter the first complex number : "))
b=eval(input("enter the second complex number : "))
c=a+b
print("sum:",c)
d=a-b
print("Difference :",d)
e=a*b
print("product : ",e)
f=a/b
print("division : ",f)"""

# write a program to determine sum,difference,product,quotient,largest and smallest of two numbers and also find reminder,sqrt of first input,power,gcd and factorial of first input
#hint : using F string to print results 
"""import math
import builtins
a=int(input("Enter the 1st number : "))
b=int(input("Enter the 2nd number : "))
c=a+b
print(f"{a}+{b}={c}")
c=a-b
print((f"{a}-{b}={c}"))
c=a*b
print((f"{a}*{b}={c}"))
c=a/b
print((f"{a}/{b}={c}"))
c=a%b
print((f"{a}%{b}={c}"))
c=max(a,b)
print((f"max({a},{b})={c:.2f}"))
c=min(a,b)
print((f"min({a},{b})={c}"))
c=a**b
print(f"{a}^{b}={c}")
c=math.sqrt(a)
print((f"sqrt({a})={c}"))
c=builtins.pow(a,b)
print((f"pow({a},{b})={c}"))
c=math.factorial(a)
print((f"fact({a})={c}"))
c=math.gcd(a,b)
print((f"gcd({a},{b})={c}"))
"""
# write a program to determine largest of two inputs without using max() function
'''
a=eval(input("enter the 1st value : "))
b=eval(input("enter the 2nd value : "))
print(a if a>b else b)

a=eval(input("enter the 1st value : "))
b=eval(input("enter the 2nd value : "))
c=max(a,b)
print(c)
'''

# write a program to determine largest of three inputs without using max() function
"""a=eval(input("enter the 1st value : "))
b=eval(input("enter the 2nd value : "))
c=eval(input("enter the 3rd value : "))
print(a if (a>b and a>c) else b if (b>c and b>a) else c)


a=eval(input("enter the 1st value : "))
b=eval(input("enter the 2nd value : "))
c=eval(input("enter the 3rd value : "))
print(a if (a>b>c) else b if (b>c) else c)
"""

# write a program to print even or odd 
"""

print("even" if int(input("enter the number : "))%2==0 else "odd")

"""
# write a program to print '>' if 1st input is >,<,= to 2nd input
"""
a=input("enter the 1st value : ")
b=input("enter the 2nd value : ")
print('>' if (a>b) else '<' if (b>a) else '=')
"""

#write a program to print 1 if input is +ve and -1 if input is -ve and 0 if input is 0
'''a=int(input("enter any number :  "))
print('1' if (a>0) else '-1' if (a<0) else '0')'''
