# Write  a  program  to  determine  a  number  is  even  or  odd  with   if  statement
'''a=int(input("enter a value:"))
if a%2==0:
	 print("even number")
else:
	print("odd number")

prog-2	-to find outputs 
if():
        print('Hyd')
        print('Sec')
        print('Cyb')
else:
        print('One')
        print('Two')
        print('Three')
print('Bye')

outputs--
One
Two
Three
Bye

#prog to find outputs
if{10 : 20 , 30 : 40}:
        print('Hyd')
        print('Sec')
        print('Cyb')
print('Bye')

outputs--
One
Two
Three
Bye


#prog-# Write   a  program  to  print  month  name  for  input  month  number  by  using  if  and  elif 
try:
	a=int(input("enter month number:"))
	if a==1:
		print("jan")
	elif a==2:
		print("feb")
	elif a==3:
		print("mar")

	elif a==4:
		print("april")
	elif a==5:
		print("may")
	elif a==6:
		print("june")
	elif a==7:
		print("july")
	elif a==8:
		print("aug")
	elif a==9:
		print("sep")
	elif a==10:
		print("oct")
	elif a==11:
		print("nov")
	elif a==12:
		print("dec")
	else:
		 print("enter valid month number:")
except:
	print("input must be integer")

outputs---

enter month number:3
mar

enter month number:13
enter valid month number

enter month number:5.9
input must be integer


#prog-Write  a  program  to  test  year  is  leap  year  or  not
year=int(input("enter a year:"))
if year%4==0 and year%100!=0 or year%400==0:
	print("leap year")
else:
	print("not a leap year")

outputs---
enter a year:2400
leap year

enter a year:2354
not a leap year

#prog-Write  a  program  to  determine  largest  of  three  numbers  with  if  and  else
a=eval(input("enter a number:"))
b=eval(input("enter b number:"))
c=eval(input("enter c number:"))
if a>b and a>c :
	print("largest number:",a)
else:
	if b>c and b>a:
		print(b,'largest')
	else:
		print(c,'largest')


#outputs--
enter a number:10
enter b number:20
enter c number:30
largest nuber: 30

a=eval(input("Enter  1  to  convert  celsius  to  farenheit  and  2  to  convert  fahrenheit  to  celsius : "))
if a==1:
	ct=int(input("enter celsius temp :"))
	ft=1.8*ct+32
	print(ft)
elif a==2:
	ft=int(input("enter farenheit temp:"))
	ct=(ft-32)/1.8
	print(ct)


Enter  1  to  convert  celsius  to  farenheit  and  2  to  convert  fahrenheit  to  celsius : 2
enter farenheit temp:100
37.77777777777778

Enter  1  to  convert  celsius  to  farenheit  and  2  to  convert  fahrenheit  to  celsius : 1
enter celsius temp :30
86.0

#-prog-Write  a  program  to  test  a  point  (x , y)  lies  in  1st  quadrant , 2nd  quadrant , 3rd  quadrant ,
#4th  quadrant , x - axis , y - axis   or  origin
x=eval(input("enter value of x qudinate:"))
y=eval(input("enter y qudinate:"))
if x>0 and y>0:
	print("1st quardant")
elif x<0 and y>0:
	print("2nd quardant")
elif x<0 and y<0:
	print("3rd quardant")
elif x>0 and y<0:
	print("4th quardant")
elif x!=0 and y==0:
	print("x-axis")
elif x==0 and y!=0:
	print("y-axis")
else:
	print("origin")

#outputs--
enter value of x qudinate:0
enter y qudinate:0
origin

#prog-Write  a  program  to  determine  largest , smallest  and  middle  of  three  numbers
a=eval(input("enter first input:"))
b=eval(input("enter second input:"))
c=eval(input("enter third input:"))
if a>b and a>c:
	print("a is largest number:",a)
	max=a
elif b>a and b>c:
	print("b is the largest number:",b)
	max=b
else:
	print("c is the largest number:",c)
	max=c
if a<b and a<c:
	print("a is smallest number:",a)
	min=a
elif b<a and b<c:
	print("b is the smallest number:",b)
	min=b
else:
	print("c is the smallest number:",c)
	min=c
mid=(a+b+c)-(max+min)
print("mid value:",mid)


enter first input:30
enter second input:10
enter third input:3
a is largest number: 30
c is the smallest number: 3
mid value: 10


# prog--Write  a  program  to  determine  three  sides  form  a  triangle  or  not
import math
a1=eval(input("enter first side:"))
b1=eval(input("enter second side:"))
c1=eval(input("enter third side:"))
if a1==b1==c1:
	
	area=math.sqrt(3)/4*a1**2
	print('eqvuivalent area:',area)
elif a1==b1!=c1 or b1==c1!=a1:
	p=a1+b1+c1
	print('isosles perimeter:',p)
elif a1!=b1!=c1:
	s=(a1+b1+c1)/2
	area=math.sqrt(s * (s - a1) * (s - b1) * (s - c1))
	print('area of scalane triangle:',area)
	p=a1+b1+c1
	print('perimeter of scalane triangle:',p)


#outputs---
enter first side:2
enter second side:3
enter third side:4
area of scalane triangle: 2.9047375096555625
perimeter of scalane triangle: 9


#outputs--
enter first side:7
enter second side:7
enter third side:7
eqvuivalent area: 21.217622392718745


#outputs--
enter first side:7
enter second side:8
enter third side:7
isosles perimeter: 22
#prog--Write  a  program  to  determine  roots  of  a  quadtratic  equation  a * x ^ 2 + b * x + c = 0  where  a  ! = 0
import math
a=float(input("enter a value:"))
if a==0:
	print('a cant be zero')
b=float(input("enter b value:"))
c=float(input("enter c value:"))
disc=b**2-4*a*c
if disc>0:
	root1=(-b+math.sqrt(disc))/(2*a)
	root2=(-b-math.sqrt(disc))/(2*a)
	print(F'roots are real and distinct:, \n root1={root1:.2f}\n root2={root2:}')
elif disc==0:
	root=(-b)/(2*a)
	print(F'roots are real and equal:, \n root={root:} \n root={root:}')
else:
	disc=b**2-4*a*c
	rp=(-b)/(2*a)
	ip=(math.sqrt(-disc))/(2*a)
	print(F'roots are imaginary:,{rp:}+{ip:}j' )
	print(F'roots are imaginary:,{rp:}-{ip:}j' )
#outputs---

 a value:3
enter b value:10
enter c value:3
roots are real and distinct:,
 root1=-0.33
 root2=-3.0

outputs---
enter a value:5
enter b value:10
enter c value:5
roots are real and equal:,
 root=-1.0
 root=-1.0

#outputs--
enter a value:5
enter b value:6
enter c value:5
roots are imaginary:,-0.6+0.8j
roots are imaginary:,-0.6-0.8j

#outputs--
enter a value:0
a cant be zero
#prog-Write  a  program   to  determine  a  point (x , y)  lies  inside , outside  or  on  the  circle.
import math
x=eval(input("enter a value of x:"))
y=eval(input("enter value of y:"))
d=math.sqrt(x**2+y**2)
r=int(input("enter radius value:"))
if d>r:
	print("outside the circle")
elif d<r:
	print("inside the circle")
else:
	print("on the cirlce")

#outputs--
enter a value of x:3
enter value of y:4
enter radius value:5
on the cirlce

#prog-Write  a   program  to  print  day  of  the  week
a=eval(input("enter a value(1-7):"))
match a:
	case 1:
		print("monday")
	case 2:
		print("tuesday")
	case 3:
		print("wenesday")
	case 4:
		print("thursday")
	case 5:
		print("friday")
	case 6:
		print("saturday")
	case 7:
		print("sunday")
print('okAY BYE')

#outputs--
enter a value(1-7):3
wenesday
okAY BYE


#prog-Write  a  program  to  print  digit in  words

a=eval(input("enter a value (0-9):"))
match a:
	case 0:
		print('zero')
	case 1:
		print('one')
	case 2:
		print('two')
	case 3:
		print('three')
	case 4:
		print('four')
	case 5:
		print('five')
	case 6:
		print('six')
	case 7:
		print('seven')
	case 8:
		print('eight')
	case 9:
		print('nine')
print('bye')
	

	#outputs---
enter a value (0-9):3
three
bye

#prog-Write  a  program  to  determine  bill  amount  and  input  is  units
unit=eval(input('enter unit:'))
cost1= 100 * 3.00 
cost2=100*3.50
cost3=200*4.0
cost4=300*4.50
cost5=500*5.00
billamount=100 * 3.00 + 100 * 3.50 + 200 * 4.00 + 300 * 4.50 +  500 * 5.00
match unit:
	case 0:
		print(F'first 100 units:,cost={cost1:}')
	case 1:
		print(F'second 100 units:,cost={cost2:}')
	case 2:
		print(F'next 200 units :,cost={cost3:}')
	case 3:
		print(F'next 300 units :,cost={cost4:}')
	case 4:
		print(F'next 500 units:,cost={cost5:}')
	case 5:
		print(F'total bill amount:,cost={billamount:}')
print('this is bill ')

#outputs---




enter unit:0
first 100 units:,cost=300.0
this is bill

enter unit:1
second 100 units:,cost=350.0
this is bill

enter unit:2
next 200 units :,cost=800.0
this is bill

enter unit:3
next 300 units :,cost=1350.0
this is bill

enter unit:4
next 500 units:,cost=2500.0
this is bill

enter unit:5
total bill amount:,cost=5300.0
this is bill'''


