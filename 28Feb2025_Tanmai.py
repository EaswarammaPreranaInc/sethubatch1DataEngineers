'''
# 1. Identify  error
else: # if is not used
		print('else  suite') 
print('Outside') 

# 2. Identify  error
if  9 > 5 # colon is missing
	print('Hello')
print('Bye') 
# 3. Identify  error
if  9 > 12:
	print('Hyd')
else #colon should be used
	print('Sec')
# 4. Identify  error
if  (10,20,15):
print('Hyd') # space or tab is mandatory
else:
print('Sec') # space or tab is mandatory

# 5. Identify  error
if  ():
			print('Hyd')
	else: # indentation if and else should have same indentation
					print('Sec')
print('Bye')

# 6. Identify  error
if  {}:# only else is calculated bcz {} result is false
{# braces are not  allowed for block statments
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
#7. # Identify  error
if  ():
	print('One')
	print('Two')
	print('Three')
else:
if  []:# indentation there should be a tab /space before if
	print('Four')
	print('Five')
	print('Six')
else:# indentation 
if  {}:# indentation there should be a tab /space before if
	print('Seven')#indentation
	print('Eight')#indentation
	print('Nine')#indentation
else:#indentation
	print('Hyd')#indentation
	print('Sec')#indentation
	print('Cyb')#indentation
print('Bye') '''

# corrected syntax

if  ():
	print('One')
	print('Two')
	print('Three')
else:
	if  []:# indentation there should be a tab /space before if
		print('Four')# indentation
		print('Five')#indentation
		print('Six')# indentation
	else:# indentation 
		if{}:# indentation there should be a tab /space before if
			print('Seven')#indentation
			print('Eight')#indentation
			print('Nine')#indentation
		else:
			print('Hyd')
			print('Sec')
			print('Cyb')
print('Bye') 

# 8.Find outputs  (Home  work)
if():#False so execute else statement
        print('Hyd')
        print('Sec')
        print('Cyb')
else:
        print('One')#One
        print('Two')#Two
        print('Three')#Three
print('Bye')#Bye

# 9.Find  outputs  (Home  work)
if{10 : 20 , 30 : 40}:#as the dict is non empty it is true statements under if are executed
        print('Hyd')#Hyd
        print('Sec')#Sec
        print('Cyb')#cyb
print('Bye')#Bye

# 10.Find outputs  (Home  work)
if {}:# empty dict if is not executed only bye is printed
	print('Hyd')
	print('Sec')
	print('Cyb')
print('Bye')#Bye

#11. Program to display monthname using if and elif

try:
	a=int(input("enter a number: "))
	if(a==1):
		print("January")
	elif a==2 :
		print("Febuary ")
	elif a== 3:
		print(" March")
	elif a==4 :
		print(" April")
	elif a==5 :
		print(" May")
	elif a==6 :
		print("June ")
	elif a==7 :
		print(" July")
	elif a== 8:
		print(" August")
	elif a==9 :
		print(" September")
	elif a==10 :
		print("October ")
	elif a==11 :
		print("November ")
	elif a==12 :
		print("December ")
	else:
		print("enter a number betweeb 1-12 only")
except:
	print("only a interger input") 

#12.Program to test leap year or not 
y=int(input("enter the year: "))
if(y%4==0 and y%100!=0) or (y%400==0):
	print("leap year")
else:
	print("not leap year")
#13. Program to convert celsius to farenhit

i=int(input("enter either 1 OR 2: "))
if i==1:
	a=float(input("enter temperature in celsius: "))
	b=1.8*a+32
	print("Fahrenheit  Equivalent = ",b)

else:
	a=float(input("enter temperature in farenheit: "))
	b=(a-32)/1.8
	print("celsius Equivalent = ",b) 

#Write  a  program  to  test  a  point  (x , y)  lies  in  1st  quadrant , 2nd  quadrant , 3rd  quadrant ,
#4th  quadrant , x - axis , y - axis   or  origin
a=float(input("Enter  value  of  x  co-ordinate : "))
b=float(input("Enter  value  of  y  co-ordinate : "))
if(a>0 and b >0):
	print("1st Quadrant")
elif(a<0 and b >0):
	print("2nd Quadrant")
elif(a<0 and b <0):
	print("3rd Quadrant")
elif(a>0 and b <0):
	print("4th Quadrant")
elif(a==0 and b==0):
	print('origin')
elif(b==0):
	print("x-axis")
elif(a==0):
	print("y-axis")

#Write  a  program  to  determine  largest , smallest  and  middle  of  three  numbers
a=float(input("Enter 1st number: "))
b=float(input("Enter 2nd number: "))
c=float(input("Enter 3rd number: "))
largest=a
if(b>largest):
	largest=b
if(c>largest):
	largest=c
smallest=a
if(b<smallest):
	smallest=b
if(c<smallest):
	smallest=c
middle=(a+b+c)-(largest+smallest)

print("largest",largest)
print("smallest",smallest)
print("middle",middle)


'''Write  a  program  to  determine  three  sides  form  a  triangle  or  not

1) Find  area  if  it  is  an  equilateral  triangle
    What  is  an  equilateral  triangle ?  ---> All  the  three  sides  should  be  same
    What  is  the  area  of  equilateral  triangle ?  --->  sqrt(3) / 4 * a ^ 2

2) Find  perimeter  if  it  is  an  isosceles  triangle
    What  is  an  isoscles  triangle ?  ---> Any  two  sides  are  same
    What   is  the  perimeter  of  isoscles  triangle ?  ---> a + b + c

3) Find  both  if  it  is  scalene  triangle
    What  is  a  scalene  triangle ?  ---> All  the  three  sides  are  different
    What  is  the  area  of  scalene  triangle ?  ---> sqrt(s * (s - a) * (s - b) * (s - c))
	What  is  the  value  of  's'  ?  --->  	(a + b + c) / 2
    What   is  the  perimeter  of  scalene  triangle ?  --->  a + b + c

4) What  is  the  qualification  of  triangle  ?  --->  Sum  of  every  two  sides  should  be  >  3rd  side

'''

import math
a=float(input("Enter 1st number: "))
b=float(input("Enter 2nd number: "))
c=float(input("Enter 3rd number: "))
if((a+b)>c and (b+c)>a and (c+a)>b):
	if(a==b==c):
		print("equilateral  triangle")
		area=math.sqrt(3)/4*a**2
		print("area: ",area)
	if(a==b or b==c or a==c):
		print("isoscles  triangle")
		perimeter=a+b+c
		print("perimeter: ",perimeter)
	else:
		print("scalene  triangle")
		perimeter=a+b+c
		print("perimeter: ",perimeter)
else:
	print("not a triangle")
	
	

'''
Write  a  program  to  determine  roots  of  a  quadtratic  equation  a * x ^ 2 + b * x + c = 0  where  a  ! = 0

1) What  is  the  value  of  discriminant ?  --->  b ^ 2 - 4ac

2) What  are  the  roots  called  if  disc > 0 ?  --->  Real  and  distinct
     What  is  the  formula  for  root1  ?  ---> (-b + sqrt(disc)) / 2a
     What  is  the  formula  for  root2 ?  ---> (-b - sqrt(disc)) / 2a

3) What  are  the  roots  called  if  disc  is  0 ?  --->  Real  and  same
     What  is  the  formula  for  root  ?  --->  -b / 2a

4) What  are  the  roots  called  if  disc < 0 ?  --->  Complex  (or)  Imaginary  roots
     What  is  the  formula  for  real  part ?  --->  -b / 2a
	 What  is  the  formula  for  imag  part ?  --->  sqrt(-disc) / 2a
	 What  is  root1  if  real  part  is  3  and  imag  part  is  4 ?  ---> 3 + 4j
	 what is root 2 if  real  part  is  3  and  imag  part  is  4 ?-->3-4j '''

import math
a=float(input("Enter value of a: "))
b=float(input("Enter value of b: "))
c=float(input("Enter value of c: "))
if(a!=0):

	
	disc=(b**2)-4*a*c
	if(disc>0):
		print("Real  and  distinct")
		root1=(-b + math.sqrt(disc)) / (2*a)
		root2=(-b - math.sqrt(disc)) / (2*a)
		print("root 1: ",root1)
		print("root 2: ",root2)
	elif(disc==0):
		print("Real  and  same")
		root=-b / (2*a)
		print("root 1: ",root)
		print("root 2: ",root)
	else:
		print("Complex  (or)  Imaginary  roots")
		realpart= -b/(2*a)
		complexpart=math.sqrt(-disc) / (2*a)
		print("root 1: ",realpart,"+",complexpart,"j")
		print("root 2: ",realpart,"-",complexpart,"j")
else:
	print("value of a cant be 0")
'''
Write  a  program   to  determine  a  point (x , y)  lies  inside , outside  or  on  the  circle.
Center  is  origin  and  radius  is  'r'

1) What  is  the  distance  between  origin  and  point (x , y) ?  --->  sqrt(x ^ 2 + y ^ 2)

2) Where  is  the  point  if  distance >  raidus ?  --->  Outside  the  circle

3) Where  is  the  point  if  distance < raidus ?  --->  Inside  the  circle
4) where is the point distance=radius --> On the circle
'''

import math
a=float(input("Enter value of x: "))
b=float(input("Enter value of y: "))
c=float(input("Enter value of radius: "))
d=math.sqrt(a ** 2 + b **2)
if(d>c):
	print("Outside  the  circle")
elif(d<c):
	print("inside the circle")
else:
	print("on the Circle")
	

# Find  outputs  (Home  work)
m = 4 #  it doesnot exist 
match  m:
	case  1:
		print('One')
	case  2:
		print('Two')
	case  3:
		print('Three')
print('Bye') # just bye 

# Identify  Error
i = 2 
match  i:
	case  1:
		print('One')
	case  _: # should be at he end 
		print('None of   the  above')
	case  2:
		print('Two')
print('Bye')



#modified 
i = 2 
match  i:
	case  1:
		print('One')
	
	case  2:
		print('Two')
	case  _: # should be at he end 
		print('None of   the  above')
print('Bye')


# Find  outputs  (Home  work)
m = 2
match  m:
	case  1:
		print('One')
	case  _:# only one _ object
		print('Hello')
	case  _:
		print('Bye')
print('End')

#modified 
m = 2
match  m:
	case  1:
		print('One')
	case  _:# only one _ object
		print('Hello')

#  Find  outputs  (Home  work)
m = 1
match  m:
	case  1:
		print('Hyd')#Hyd
	case  1:#ignored
		print('Sec')
	case  1:#  ignored
		print('Cyb')
print('Bye')# Bye 

# Find  outputs  (Home  work)
ch = 'B'
match  ch:
	case   'A':
		print('Apple')
	case  'B':
		print('Book')#Book
	case  'C':
		print('Cafe')
	case  _:
		print('None of  the  above')
print('Bye')#Bye

'''
1) What  are  the  outputs  if  input  is  -6 ? ---> Hyd <next line> Sec <next line> Cyb<next line> Bye
2) What  are  the  outputs  if  input  is  15  ?  ---> One <next line> Two <next line> Three <next line> Bye
3) What  are  the  outputs  if  input  is  10.8  ?  --->India <next line> China <next line> Usa <next line> Bye
4) What  are  the  outputs  if  input  is  0  ?  --->Hyd <next line> Sec <next line> Cyb<next line> Bye
5) What  are  the  outputs  if  input  is  -10  ?  --->One <next line> Two <next line> Three <next line> Bye
6) What  are  the  outputs  if  input  is  7  ?  --->Hyd <next line> Sec <next line> Cyb<next line> Bye '''

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

'''
1) What  is  the  output  when  input  is  (-10 , -20) ?  --->Quadrant
2) What  is  the  output  when  input  is  (10 , 0) ?  --->x-axis
3) What  is  the  output  when  input  is  (0 , -20) ?  --->y-axis
4) What  is  the  output  when  input  is  (0 , 0) ?  --->Origin
5) What  is  the  output  when  input  is  (10 , 20 , 30) ?  --->Not a point
6) What  is  the  output  when  input  is  [10 , 20]  ?  --->Quadrant
7) What  is  the  output  when  input  is  [0 , -25]  ?  --->y-axis
8) What  is  the  output  when  input  is  ()  ?  --->not a point
9) What  is  the  output  when  input  is  {10 , 20} ?  --->Quadrant
10) What  is  the  output  when  input  is  (25,) ?  --->not a point

'''
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
		print('Not a point') 

'''  (Home  work)
Write  a   program  to  print  day  of  the  week
1  - Monday
2  - Tuesday
3  - Wednesday
....
7 - Sunday
8 - Invalid
Hint: use match case
'''

d=int(input("enter a number 1-7: "))
match d:
		case(1):
			print("monday")
		case(2):
			print("Tuesday")
		case(3):
			print("wednesday")
		case(4):
			print("thursday")
		case(5):
			print("friday")
		case(6):
			print("saturaday")
		case(7):
			print("Sunday") 
'''  (Home  work)
Write  a  program  to  print  digit in  words
0  -   Zero
1  -   One
2  -   Two
...
9  - Nine
10 -  Not  a  digit

Hint:use match case
'''

d=int(input("enter a number 0-10: "))
match d:
		case(0):
			print("Zero")
		case(1):
			print("One")
		case(2):
			print("Two")
		case(3):
			print("Three")
		case(4):
			print("Four")
		case(5):
			print("Five")
		case(6):
			print("six")
		case(7):
			print("Seven") 
		case(8):
			print("Eight")
		case(9):
			print("Nine")
		case(10):
			print("Ten") 

'''
Write  a  program  to  determine  bill  amount  and  input  is  units

Units                                                      Cost
------------------------------------------------------------
First  100  units	(0-99 units	)						Rs. 3.00 / unit

Next  100  units	(100-199)							Rs. 3.50 / unit

Next  200  units	(200-399	)						Rs. 4.00 / unit

Next  300  units	(400-699)							Rs. 4.50 / unit

Above  700  units	(700>=)							Rs. 5.00 / unit
---------------------------------------------------------------
Let  units  be  1200
What  is  the  bill  amount ? --->  100 * 3.00 + 100 * 3.50 + 200 * 4.00 + 300 * 4.50 +  500 * 5.00

Hint:  Use  match  ...  case   but  not  if ... else

'''

units = int(input('Enter  units :   '))
match  units//100:
	case  0:
				cost =units*3.00
	case  1:
				cost =100*3.00+(units-100)*3.50
	case  2 | 3:
				cost =100*3.00+100*3.50+(units-200)*4.00
	case  4 | 5 | 6:
				cost =100*3.00+100*3.50+200*4.0+(units-400)*4.5
	case _:
				cost =100*3.00+100*3.5+200*4+300*4.5+(units-700)*5.00
print('Bill amount:  ',cost)


'''
Write  a  program  to  print  fibonacci  series  upto   x

Let  input  be   10
What  are  the  outputs  ?  ---> 0 , 1 , 1 , 2 , 3 , 5 , 8

1) What  is  10th  term ?  --->  9th  term + 8th  term
    What  is  3rd  term ?  --->  2nd  term + 1st  term
    What  is  ith  term ?  --->  (i - 1)th  term +  (i - 2)  term

2) What  are  the  first  two  terms ?  --->  0  and  1

3)Hint use while loop
'''
try:
	x = int(input('Enter a number :   '))
	if x==0:
		print(0)
	else:
		a=0
		b=1
		print(0)
		print(1)
		c=a+b
		while(c<=x):
			print(c)
			a=b
			b=c
			c=a+b
except:
	print("cant use float value")


'''#  Find  outputs
while  True:
	print('Hello') # infinite hello
print('Bye')# no executed '''

#  Find  outputs
while  False:
	print('Hello')#never executed
print('Bye')#bye
