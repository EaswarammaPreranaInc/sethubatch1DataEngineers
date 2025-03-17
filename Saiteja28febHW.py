# program for odd and even in if else
'''
try:
 x = int(input("enter the number: ",))
 if x%2==0 :
	 print('Even number')
 else :
	 print('odd number')
except:
	print('input should be number')
'''
'''
month name
try:
	month = ['january','febrauary','march','april','may','june','august','september','octber','november','december']
	x = int(input('enter the month(1-12):'))
	if x<=12 :
		print(month[x-1])
	else:
		print("input should be from 1- 12")
except:
	print("input should be inetger")
'''
'''
#leap year
x = int(input("enter the year:"))
if x%4==0 and x%100!=0 or x%400==0:
	print('Leap year')
else:
	print('Not a leap year')
'''
'''
#largest number
a=int(input('enter the 1st input:'))
b=int(input('enter the 2nd input:'))
c=int(input('enter the 3rd input:'))
if a>b>c:
	print('Largest number:',a)
elif b>a>c:
	print('Largest number:',b)
else:
	print('Largest number:',c)

'''

'''
#temp
x = int(input('Enter  1  to  convert  celsius  to  farenheit  and  2  to  convert  fahrenheit  to  celsius :'))
if (x == 1):
	t=int(input("enter the celsius:"))
	y= (1.8*t)+32
	print(F'farenheit equivalent: {y:.2f}')
elif(x==2) :
	a=int(input("enter the farenheit :"))
	z=(a-32)/1.8 
	print(F'Celsius equivalent: {z:.2f}')
else:
	print('valid input')
	'''

'''
co-ordinate
x=int(input("enter the x co-ordinate:"))
y=int(input("enter the y co-ordinate:"))
if x>0 and y>0:
	print('1st quadrant')
elif x<0 and y>0:
	print('2nd quadrant')
elif x<0 and y<0:
	print('3rd quadrant')
elif x>0 and y<0:
	print('4th quadrant')
elif x!=0 and y==0:
	print('5th quadrant')
elif x==0 and y!=0:
	print('6th quadrant')
elif x==0 and y==0:
	print("origin")
else:
	print("valid input")
'''
'''
a=int(input("enter 1st input"))
b=int(input("enter 2nd input"))
c=int(input("enter 3rd input"))
if :
	max=
'''
'''
import math
a=int(input("enter 1st input:"))
b=int(input("enter 2nd input:"))
c=int(input("enter 3rd input:"))
if a==b==c:
	print('Equilateral triangle')
	Area=math.sqrt(3)/4*(a**2)
	print(F'Area:{Area:.2f}')
elif a==b or b==c or c==a:
	print('isosseles traiangle')
	P=a+b+c
	print(F'Perimeter:{P}')
if a+b>c or b+c>a or c+a>b:
	print('scalene triangle')
	s=(a+b+c)/2
	area=math.sqrt(s*(s-a)*(s-b)*(s-c))
	p=(a+b+c)
	print(F'Area:{area:.2f}')
	print(F'Perimeter:{p}')
else :
	print("not a triangle")
'''

'''
try:
	import math
	a=int(input("enter 1st input:"))
   
b=int(input("enter 2nd input:"))
c=int(input("enter 3rd input:"))
disc=(b**2-(4*a*c))
if disc>0:
	print("Real and distinct")
	r1=(-b + math.sqrt(disc)) / (2*a)
	r2=(-b - math.sqrt(disc)) / (2*a)
	print(F'r1={r1:.2f} r2={r2} ')
elif disc<0:
	print("complex or imaginary")
	real= -b/2*a
	imag= math.sqrt(-disc)/2*a
	print(F'root1 :{real}+{imag:.2f}j')
	print(F'root1 :{real}+{imag:.2f}j')
elif disc==0:
	print("Real and equal")
	r1=(-b / 2*a)
	r2=(-b / 2*a)
	print(F'r1:{r1} r2:{r2}')
'''


'''
circle point
import math
x=float(input("enter value of x :"))
y=float(input("enter value of y:"))
r=float(input("enter value of r:"))
dis=math.sqrt(x**2+y**2)
if dis>r:
	print("Outside of Circle")
elif dis<r:
	print("Inside of Circle")
elif dis==r:
	print(" Point on the Circle")

'''
'''
x=int(input('Enter the week number(1-7):'))
match x:
	case 1:
		print('Sunday')
	case 2:
		print('Monday')
	case 3:
		print('Tuesday')
	case 4:
		print('Wednesday')
	case 5:
		print('Thursday')
	case 6:
		print('Friday')
	case 7:
		print('Saturday')
'''

'''
units = int(input('Enter  units :   '))
match units//100 :
	case  0 :
		cost =units*3
	case  1:
		cost =100*3.0+(units-100)*3.5
	case  2 |3 :
		cost=100*3.0+100*3.50+(units-200)*4.0
	case  4 | 5 | 6:
		cost =100*3.0+100*3.50+200*4.0+(units-300)*4.50
	case  _:
		cost =100*3.0+100*3.50+200*4.0+300*4.50+(units-700)*5.0
print('Bill  amount  :  ' , cost)
'''
'''
a=int(input("enter 1st input: "))
b=int(input("enter 2nd input: "))
c=int(input("enter 3rd input: "))
if a>b>c or a>c>b:
	max=int(a)
elif b>a>c or b>c>a :
	max=int(b)
elif c>a>b or c>b>a:
	max= int(c)
elif b<a<c or b<c<a:
	min=int(b)
elif a<c<b or a<b<c:
	min=int(a)
elif c<b<a or c<a<b:
	min=int(c)
mid=(a+b+c)-((max)+(min))
print(F'lagrest number is : {max}')
print(F'smallest number is : {min}')
print(F'mid number is : {mid}')

'''
'''
x=eval(input('enter the number: '))
if x==0:
	print(0)
else:
	a=0
	b=1
	print(a)
	print(b)
	c=a+b
	while c<=x:
		print(c)
		a=b
		b=c
		c=a+b

	'''




