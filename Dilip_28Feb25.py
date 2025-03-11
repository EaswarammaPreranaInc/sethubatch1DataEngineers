#1
try:
	x=int(input("Enter a number :"))
	if x%2==0:
		print("Even")
	else:
		print("Odd")
except:
	print("Enter integer number...")

#2
try:
	x=int(input("Enter month number (1-12) :"))
	if x==1:
		print("January")
	elif x==2:
		print("February")
	elif x==3:
		print("March")
	elif x==4:
		print("April")
	elif x==5:
		print("May")
	elif x==6:
		print("June")
	elif x==7:
		print("July")
	elif x==8:
		print("August")
	elif x==9:
		print("September")
	elif x==10:
		print("October")
	elif x==11:
		print("November")
	elif x==12:
		print("December")
	else:
		print("Input should be between 1 and 12")
except:
	print("Input should be an integer")

#3
try:
	x=int(input("Enter 4-digit year : "))
	if (x%4 == 0 and x%100 !=0) or x%400 == 0:
		print("Leap year")
	else:
		print("Not a leap year")
except:
	print("Enter valid input")

#4
try:
	x=eval(input("Enter 1st input :"))
	y=eval(input("Enter 2nd input :"))
	z=eval(input("Enter 3rd input :"))
	if x>y and x>z:
		print("Largest number :",x)
	elif y>x and y>z:
		print("Largest number :",y)
	else:
		print("Largest number :",z)
except:
	print("Input should be of same kind....")

#5
try:
	x=float(input('Enter 1 to convert celsius to fahrenheit and 2 to convert fahrenheit to celsius :'))
	if x==1:
		temp=float(input("Enter celsius temperature :"))
		fahren=1.8*temp+32
		print("fahrenheit equivalent :",f"{fahren:.2f}")
	elif x==2:
		temp=float(input("Enter fahrenheit temperature :"))
		cel=(temp-32)/1.8
		print("celsius equivalent :",f"{cel:.2f}")
	else:
		print("Invalid input...")
except:
	print("Enter integer input...")

#6
try:
	x=float(input("Enter value of x co-ordinate :"))
	y=float(input("Enter value of y co-ordinate :"))
	if x>0 and y>0:
		print("1st quadrant")
	elif x<0 and y>0:
		print("2nd quadrant")
	elif x<0 and y<0:
		print("3rd quadrant")
	elif x>0 and y<0:
		print("4th quadrant")
	elif x!=0 and y==0:
		print("On x-axis")
	elif x==0 and y!=0:
		print("On y-axis")
	else:
		print("Origin")
except:
	print("Enter valid inputs...")

#7
import random
a=float(input("Enter first input :"))
b=float(input("Enter second input :"))
c=float(input("Enter third input :"))
max = random.choice([a,b,c])
min = random.choice([a,b,c])
if a>max:
	max=a
if b>max:
	max=b
if c>max:
	max=c
print(f"{max=}")
if a<min:
	min=a
if b<min:
	min=b
if c<min:
	min=c
print(f"{min=}")
mid=(a+b+c)-min-max
print(f"{mid=}")

#8
try:
	import math
	x=float(input("Enter 1st side :"))
	y=float(input("Enter 2nd side :"))
	z=float(input("Enter 3rd side :"))
	if x+y>z and x+z>y:
		if x==y==z:
			print("Equilateral triangle")
			area = math.sqrt(3)/4*x**2
			print("Area :"f"{area:.2f}")
		elif x==y or x==z:
			print("Isoscles triangle")
			perimeter = x+y+z
			print("Perimeter :"f"{perimeter:.2f}")
		else:
			print("Scalene triangle")
			s = (x+y+z)/2
			area = math.sqrt(s*(s-x)*(s-y)*(s-z))
			perimeter = x+y+z
			print("Area :"f"{area:.2f}")
			print("Perimeter :"f"{perimeter:.2f}")
	else:
		print("Not a valid triangle...")
except:
	print("Enter valid inputs...")

#9
from math import sqrt
a=int(input("Enter value of a :"))
if a!=0:
	b=int(input("Enter value of b :"))
	c=int(input("Enter value of c :"))
	dis = b**2-(4*a*c)
	if dis==0:
		print("Roots are real and equal")
		root = -b/(2*a)
		print("Root1 :"f"{root:.2f}")
		print("Root2 :"f"{root:.2f}")
	elif dis>0:
		print("Roots are real and distinct")
		root1 = (-b+sqrt(dis))/(2*a)
		print("Root1 :"f"{root1:.2f}")
		root2 = (-b-sqrt(dis))/(2*a)
		print("Root2 :"f"{root2:.2f}")
	else:
		print("Roots are complex (or) imaginary")
		real = -b/(2*a)
		imag = sqrt(-dis)/(2*a)
		print("Root1 :"f"{real:}"" + "f"{imag:}j")
		print("Root2 :"f"{real:}"" - "f"{imag:}j")
else:
	print("Value of a cannot be 0")

#10
try:
	import math
	x=float(input("Enter value of x :"))
	y=float(input("Enter value of y :"))
	r=float(input("Enter radius of circle :"))
	dis = math.sqrt(x**2+y**2)
	if dis<r:
		print("Point is inside the circle...")
	elif dis>r:
		print("Point is outside the circle...")
	else:
		print("Point is on the circle...")
except:
	print("Enter valid inputs...")

#11
try:
	x=int(input("Enter any digit :"))
	match x:
		case 1:
			print("Monday")
		case 2:
			print("Tuesday")
		case 3:
			print("Wednesday")
		case 4:
			print("Thursday")
		case 5:
			print("Friday")
		case 6:
			print("Saturday")
		case 7:
			print("Sunday")
		case _:
			print("Invalid input")
except:
	print("Enter digits from 1-7")

#12
try:
	x=int(input("Enter any digit :"))
	match x:
		case 0:
			print("Zero")
		case 1:
			print("One")
		case 2:
			print("Two")
		case 3:
			print("Three")
		case 4:
			print("Four")
		case 5:
			print("Five")
		case 6:
			print("Six")
		case 7:
			print("Seven")
		case 8:
			print("Eight")
		case 9:
			print("Nine")
		case _:
			print("Not a digit")
except:
	print("Enter digits from 1-9")

#13
units = int(input('Enter  units :   '))
match  int(units/100):
	case 0:
		cost =units*3
	case 1:
	    cost =100*3+(units-100)*3.5
	case 2 | 3:
		cost =100*3+100*3.5+(units-200)*4
	case  4 | 5 | 6:
		cost =100*3+100*3.5+100*4+(units-300)*4.5
	case _:
		cost=100*3+100*3.5+100*4+100*4.5+(units-400)*5
print('Bill  amount  :  ',cost)


