program1:
# Identify  error
else: # error because there will not be only else in if else
		print('else  suite')
print('Outside')

program2:
	# Identify  error
if  9 > 5 # error brecuse ':' must be their
	print('Hello')
print('Bye')

program3:
	if  9 > 12:
	print('Hyd')
else #error because ':' must be their
	print('Sec') 

program4:
	if  (10,20,15):
print('Hyd') #error
else:
print('Sec')

program5:
	# Identify  error
if  ():         #error format shoulb be proper
			print('Hyd')
	else:
					print('Sec')
print('Bye')

program6:
	if  { }:
{ #errror becausein ifelse there is no open and close braces

  print('One')
	print('Two')
	print('Three')
}
else:
{
	print('Four')
	print('Five')
	print('Six')
}
print('Bye')

program7:
	# Identify  error
if  ():
	print('One')
	print('Two')
	print('Three')
else:
if  []:#error
	print('Four')
	print('Five')
	print('Six')
else:
if  {}:
	print('Seven')
	print('Eight')
	print('Nine')
else:
	print('Hyd')
	print('Sec')
	print('Cyb')
print('Bye')

program8:
	write a program to determine a even or odd
n=int(input("n="))
if n%2==0:
	print("even")
else:
	print("odd")

program9:
# Find outputs  (Home  work)
if():
        print('Hyd')
        print('Sec')
        print('Cyb')
else:
        print('One')#one
        print('Two')#Two
        print('Three')#three
print('Bye')

program10:
	if{10 : 20 , 30 : 40}:
        print('Hyd')#Hyd
        print('Sec')#sec
        print('Cyb')#cyb
print('Bye')#Bye

program11:
	if { }:
	print('Hyd')
	print('Sec')
	print('Cyb')
print('Bye')#Bye

program12:
Write   a  program  to  print  month  name  for  input  month  number  by  using  if  and  elif 

n= int(input('Enter the number between 1 to 12:'))
if n==1:
	print('january')
elif n==2:
    print('febuary')
elif n==3:
	print('march')
elif n==4:
    print('April')
elif n==5:
	print('may')
elif n==6:
	print('june')
elif n==7:
	print('july')
elif n==8:
	print('August')
elif n==9:
	print('sepetember')
elif n==10:
	print('octeber')
elif n==11:
	print('november')
elif n==12:
	print('December')

program13:
Write  a  program  to  test  year  is  leap  year  or  not
year = int(input('Enter the year :'))
if(year%4)==0:
	if(year%100)==0:
		if(year%400)==0:
			print(year,'is a leap year')
		else:
			print(year,'is not a leap year')
	else:
		print(year,'is  a leap year')

program14:
Write  a  program  to  determine  largest  of  three  numbers  with  if  and  else
n1=int(input('ENter the 1st number:'))
n2=int(input('ENter the 2ndt number:'))
n3=int(input('ENter the  3rd number:'))
if n1>n2 and n1<n3:
	print(n1,'latgest number')
 elif n2>n3:
	print( n2,' is not a largest number')
else:
	print(n3,'largest number')

program15:
Write  a  program  to  convert  celsius  temperature  to  farenheit  and  vice-versa
try:
   a=int(input('Enter 1 to convert celius to farenhit and 2 to convert farenheit to celsius:'))
   if a==1:
	   celius_temp = float(input('Enter celius temperature :'))
	   farenhit= 1.8*celius_temp+32

	   print(f' farenhit equivalent:{farenhit}')
   elif a==2:
	   farenhit_temp = float(input('Enter farenhit temperature:'))
	   celius=(farenhit_temp-32)/1.8
	   print(f' celius equivalent:{celius}')
   else:
	   print("Invalid number")
except:
	print("input shoulb be integer only")

program16:
Write  a  program  to  test  a  point  (x , y)  lies  in  1st  quadrant , 2nd  quadrant , 3rd  quadrant ,4th  quadrant , x - axis , y - axis   or  origin
try:
	x=float(input("Enter the value of x-co-ordinate:"))
	y=float(input("enter the value of y -co-ordinate:"))
	if x>0 and y>0:
		print("1st quadrant")
	elif x<0 and y<0:
		print("2nd quadrant")
	elif x<0 and y<0:
		print("3rd quadrant")
	elif x>0 and y<0:
		print("4th quadrant")
	elif x!=0 and y==0:
		print("x-axis")
	elif x==0 and y!=0:
		print("y-axis")
	else:
		print("origin")
except:
	print("Input shoulb be only number")

program17:	
Write  a  program  to  determine  largest , smallest  and  middle  of  three  numbers
try:
	a=float(input("Enter the largest number:"))
	b=float(input("Enter the smallest number:"))
	c=float(input("Enter the middle number:"))
	lar=max(a,b,c)
	small=min(a,b,c)
	middle=(a+b+c)-(max+min)
	print(f'largest number:{lar}')
	print(f'small number:{small}')
	print(f'middle number:{middle}')
except:
	print("input shoulb be only number")

program18:
Write  a  program  to  determine  three  sides  form  a  triangle  or  not
import math
try:
	a=float(input("Enter 1st side"))
	b=float(input("Enter 2nd side"))
	c=float(input("Enter 3rd side"))
	if a+b>c and b+c>a and c+a>b:
		if a==b and b==c and c==a:
		print('Equivateral triangle')
		area=math.sqrt(3)/4*a**2
		print(f'Area:{area:.2f}')
		elif a==b or b==c or c==a:
		print("Isoscles triangle")
		perimeter = a+b+c
		print(f'perimeter :{perimeter}')
		elif a!=b and b!=c and c!=a:
		print(f'scalene triangle')
		s=(a+b+c)/2
		area=math.sqrt(s*(s-a)*(s-b)*(s-c)
		perimeter=a+b+c
		print(f'Area:{area:.2f}')
		print(f'perimeter:{perimeter}')
	else:
		print("not a triangle")
except:
	print("Input shoulb be a number only")

program19:
Write  a  program  to  determine  roots  of  a  quadtratic  equation  a * x ^ 2 + b * x + c = 0  where  a  ! = 0
import math
try:
	a=float(input("Enter the value of a:"))
	b=float(input("Enter the value of b:"))
	c=float(input("Enter the value of c:"))
	D=b**2-(4*a*c)
	if a!=0:
	if D>0:
		print('Roots are real and  disticnt')
		r1=(-b+math.sqrt(D))/(2*a)
		r2=(-b+math.sqrt(D))/(2*a)
		print(f'Root1:{r1:.2f}')
		print(f'Root2:{r2:.2f}')
	elif D<0:
		print('Roots are imaginary (or) complex')
		real=-b/(2*a)
		imag=math.sqrt(-D)/(2*a)
		print(f'Root1:{real}+{imag:.1f}j')
		print(f'Root2:.{real}-{imag:.1f}j')
	elif D==0:
		print('Roots are real and same')
		r=-b/2(*a)
		print(f'Root1:{r:.1f}')
		print(f'Root2:{r:.1f}')
	else:
		print('Value can not be 0')
except:
	print("Input shoulb be a number only")

program20:
Write  a  program   to  determine  a  point (x , y)  lies  inside , outside  or  on  the  circle Center  is  origin  and  radius  is  'r'
import math
try:
	x=float(input('Enter value of x:'))
	y=float(input('Enter value of y:'))
	D=math.sqrt(x**2+y**2)
	if D==r:
		print("on the circle")
	elif D>r:
		print("outside the circle")
	elif D<r:
		print("Inside the circle")
except:
	print("Input shoulb be a numbers only")

program21:
m = 4
match  m:
	case  1:
		print('One')
	case  2:
		print('Two')
	case  3:
		print('Three')
print('Bye') #Bye

program22:
i = 2
match  i:
	case  1:
		print('One')
	case  _: # Error because nameless object should be at end of the program
		print('None of   the  above')
	case  2:
		print('Two')
print('Bye)

program23:
m = 2
match  m:
	case  1:
		print('One')
	case  _: # Error because nameless object should be at end of the program
		print('Hello')
	case  _:
		print('Bye')
print('End')

program24:
m = 1
match  m:
	case  1:
		print('Hyd')#Hyd
	case  1:
		print('Sec')
	case  1:
		print('Cyb')
print('Bye') #bye

program25:
ch = 'B'
match  ch:
	case   'A':
		print('Apple')
	case  'B':
		print('Book') #Book
	case  'C':
		print('Cafe')
	case  _:
		print('None of  the  above')
print('Bye')#Bye

program26:
	x = eval(input('Enter any  number :  '))
match  x:
	case  7 |  -6  |  0:
		print('Hyd')
		print('Sec')
		print('Cyb')
	case  -10 | 15:
		print('One')
		print('Two')
		print('Three')
	case  _:
		print('India')
		print('China')
		print('Usa')
# End  of  match
print('Bye')
Output:
x=-6
Hyd
Sec
Cyb
Bye

program27:
tpl = eval(input('Enter  any  point  in  the  form  of  (x , y) :  '))
match  tpl:
	case  (0 , 0):
		print('Origin')
	case   (0 , y):
		print('y - axis')
	case   (x , 0):
		print('x - axis')
	case   (x , y):
		print('Quadrant')
	case  _:
		print('Not  a  point')
Output:
Enter  any  point  in  the  form  of  (x , y) :
-10,-20
quadrant

program28:
Write  a   program  to  print  day  of  the  week
try:
	m=eval(input('Enter week day number(1-7):'))
	match m:
		case1:
			print('Monday')
		case2:
			print('Tuesday')
		case3:
			print('wednesday')
		case4:
			print('Thrusday')
		case5:
			print('Friday')
		case6:
			print('saturday')
		case7:
			print('sunday')
print('Bye')
except:
	print('Input should be an integer')

program 29:
Write  a  program  to  print  digit in  words
try:
	m=eval(input("Enter the number (0-9):")
	match m:
		case0:
			print('Zero')
		case1:
			print('One')
		case2:
			print('Two')
		case3:
			print('Three')
		case4:
			print('Four')
		case5:
			print('Five')
		case6:
			print('six')
		case7:
			print('seven')
		case8:
			print('Eight')
		case9:
			print('Nine')
		case-:
			print('not a digit')
except:
	print('Input should be a number')

program30:
	Write  a  program  to  determine  bill  amount  and  input  is  units

Units                                                      Cost
------------------------------------------------------------
First  100  units								Rs. 3.00 / unit

Next  100  units								Rs. 3.50 / unit

Next  200  units								Rs. 4.00 / unit

Next  300  units								Rs. 4.50 / unit

Above  700  units								Rs. 5.00 / unit
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
				
		
