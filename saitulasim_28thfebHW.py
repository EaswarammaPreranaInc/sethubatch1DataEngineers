#1 given number  is  even  or  odd  with   if  statement
try:
  a=int(input("Enter +ve number : "))
  if a%2==0:
    print("Even Number")
  else:
    print("Odd Number")
except:
  print("Input should be +ve integer number only ")

#2 program  to  print  month  name  for  input  month  number  by  using  if  and  elif 
try:
	month=int(input("Enter month number (1-12) : "))
	if 0<month<=1:
		print("January")
	elif 1<month<=2:
		print("February")
	elif 2<month<=3:
		print("march")
	elif 3<month<=4:
		print("April")
	elif 4<month<=5:
		print("May")
	elif 5<month<=6:
		print("June")
	elif 6<month<=7:
		print("July")
	elif 7<month<=8:
		print("Augest")
	elif 8<month<=9:
		print("September")
	elif 9<month<=10:
		print("October")
	elif 10<month<=11:
		print("November")
	elif 11<month<=12:
		print("December")
	else:
		print("Input  should  be  between  1  and   12")
except:
	print("Input should be an integer")

#3 write a  program  to  test  year  is  leap  year  or  not
try:
	year=int(input("Enter year : "))
	if year%4==0 and year%100 != 0 or year%400==0:
		print("Leap year")
	else:
		print("Not a LeapYear")
except:
	print("number should be Integer only")

#4 find the largest  of  three  numbers  with  if  and  else
a=eval(input("Enter 1st input : "))
b=eval(input("Enter 2nd input : "))
c=eval(input("Enter 3rd input : "))
if a>b and a>c:
	print(f"Largest number :{a}")
elif b>c:
	print(f"Largest number :{b}")
else:
	print(f"Largest number :{c}")

#5 Write  a  program  to  convert  celsius  temperature  to  farenheit  and  vice-versa
try:
	a=int(input("Enter  1  to  convert  celsius  to  farenheit  and  2  to  convert  fahrenheit  to  celsius :"))
	if a==1:
		ct=float(input("Enter  celsius  temperature : "))
		farenheit=1.8*ct+32
		print(f"Farenheit Equivalent : {farenheit:.2f}")
	elif a==2:
		ft=float(input("Enter farenheit temperature : "))
		celsius=(ft-32)/1.8
		print(f"Celsius Equivalent : {celsius:.2f}")
	else:
		print("Invalid input")
except:
	print("Input value is 1 or 2 only")

#6 write a program  to  test  a  point  (x , y)  lies  in  1st  quadrant , 2nd  quadrant , 3rd  quadrant ,4th  quadrant , x - axis , y - axis   or  origin
try:
	x=float(input("Enter  value  of  x  co-ordinate : "))
	y=float(input("Enter  value  of  y  co-ordinate : "))
	if x>0 and y>0:
		print("1st quadrant")
	elif x<0 and y>0:
		print("2nd quadrant")
	elif x<0 and y<0:
		print("3rd quadrant")
	elif x>0 and y<0:
		print("4th quadrant")
	elif x!=0 and y==0:
		print("x-axis")
	elif x==0 and y!=0:
		print("y-axis")
	elif x==0 and y==0:
		print("origin")
	else:
		print("Invalid values")
except:
	print("Input should numbers only")

#7 write a program  to  determine  largest , smallest  and  middle  of  three  numbers
try:
  a=float(input("enter first input : "))
  b=float(input("enter the second input : "))
  c=float(input("enter the third input : "))
  max=a
  if max<b:
  	max=b
  if max <c:
  	max=c
  min=a
  if min>b:
  	min=b
  if min > c:
  	min=c
  middle=(a+b+c)-(max+min)
  print(f'Largest number : {max}')
  print(f'Smallest number : {min}')
  print(f'Middle number : {middle}')
except:
  print("Input should be a numbers only")

#8 write a program  to  determine  three  sides  form  a  triangle  or  not
import math
try:
	a=float(input("enter 1st side : "))
	b=float(input("enter 2nd side : "))
	c=float(input("enter 3rd side : "))
	if a+b > c and b+c > a and c+a > b :
		if a==b and b==c and c==a:
			print("Equilateral triangle")
			area=math.sqrt(3)/4*a**2
			print(f"Area : {area:.2f}")
		elif a==b or b==c or a==c:
			print("Isoscles triangle")
			perimeter=a+b+c
			print(f"Perimeter : {perimeter}")
		elif a!=b and b!=c and c!=a:
			print("Scalene triangle")
			s=(a+b+c)/2
			area=math.sqrt(s*(s-a)*(s-b)*(s-c))
			perimeter=a+b+c
			print(f"Area : {area}")
			print(f"Perimeter : {perimeter}")
	else:
		print("Not a triangle")
except:
	print("Input should be a number only")

#9 write a program  to  determine  roots  of  a  quadtratic  equation  a * x ^ 2 + b * x + c = 0  where  a  ! = 0
import math
try:
	a=float(input("Enter value of a : "))
	b=float(input("Enter value of b : "))
	c=float(input("Enter value of c : "))
	D=b**2-(4*a*c)
	if a!=0:
		if D > 0:
			print("Roots are real and distinct")
			r1=(-b+math.sqrt(D))/(2*a)
			r2=(-b-math.sqrt(D))/(2*a)
			print(f'Root 1 : {r1:.2f}')
			print(f'Root 2 : {r2:.2f}')
		elif D < 0:
			print("Roots are imaginary (or) complex")
			real=-b/(2*a)
			imag=(math.sqrt(-D))/(2*a)
			print(f'Root 1 : {real} + {imag:.1f}j')
			print(f'Root 2 : {real} - {imag:.1f}j')
		elif D == 0:
			print("Roots are real and same")
			r=-b/(2*a)
			print(f'Root 1 : {r:.1f}')
			print(f'Root 2 : {r:.1f}')
	else:
		print('value of "a" can not be 0')
except:
	print("Input should be a numbers only")

#10 Write  a  program   to  determine  a  point (x , y)  lies  inside , outside  or  on  the  circle.
import math
try:
	x=float(input("Enter  value  of  x : "))
	y=float(input("Enter  value  of  y : "))
	r=float(input("Enter radius of circle : "))
	D=math.sqrt(x**2+y**2)
	if D==r:
		print("On  the  circle")
	elif D>r:
		print("Outside  the  circle")
	elif D<r:
		print("Inside  the  circle")
except:
	print("Input should be a numbes only")

#11 Write  a   program  to  print  day  of  the  week using match....case
try:
	day=int(input("Enter the number (1-7) : "))
	match day:
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
			print("Invalid")
except:
	print("Input should be a +ve integer numbers only")

#12 Write  a  program  to  print  digit in  words using match.....case
try:
	num=int(input("Enter the number (1-7) : "))
	match num:
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
		case 10:
			print('Not a digit')
		case _:
			print("enter number (1-10) only")
except:
	print("Input should be a +ve integer numbers only")

#13 Write  a  program  to  print  fibonacci  series  upto   x using while loop
try:
	x=int(input("enter the x value: "))
	if x==0:
		print("Fibonacci  series")
		print("0")
	else:
		a=0
		b=1
		print("Fibonacci  series")
		print(a)
		print(b)
		while a+b<=x:
			c=a+b
			print(c)
			a=b
			b=c
except:
	print("Input should be a integer only")

#14 Write  a  program  to  determine  bill  amount  and  input  is  units
'''Units                                                      Cost
------------------------------------------------------------
First  100  units								Rs. 3.00 / unit

Next  100  units								Rs. 3.50 / unit

Next  200  units								Rs. 4.00 / unit

Next  300  units								Rs. 4.50 / unit

Above  700  units								Rs. 5.00 / '''

try:
	unit=int(input("enter the units: "))
	match unit//100:
		case 0 :
			cost=unit*3.00
		case 1 :
			cost=100*3.00+(unit-100)*3.5
		case 2|3:
			cost=100*3.00+100*3.5+(unit-200)*4.0
		case 4|5|6:
			cost=100*3.00+100*3.5+200*4.0+(unit-400)*4.50
		case _:
			cost=100*3.00+100*3.5+200*4.0+400*4.50+(unit-700)*5.00
	print("bill amount : ",cost)
except:
	print("input should be integer numbers")
