1
# Identify  error
else:
		print('else  suite')  #else cannot be executed without if
print('Outside')
---------------------------------------------------------------------------------------------------------------------------
2
# Identify  error
if  9 > 5
	print('Hello')  #missing colon after if 
print('Bye')
-------------------------------------------------------------------------------------------------------------------------------
3
# Identify  error
if  9 > 12:
	print('Hyd')
else
	print('Sec')  #missing colon after else 
--------------------------------------------------------------------------------------------------------------------------------
4
# Identify  error
if  (10,20,15):     #no indentation for if and else statements
print('Hyd')
else:
print('Sec')
---------------------------------------------------------------------------------------------------------------------------------
5
# Identify  error
if  ():
			print('Hyd')
	else:
					print('Sec')   #else is not indented with if
print('Bye')
-------------------------------------------------------------------------------------------------------------------------------------
6
# Identify  error
if  { }:
{
	print('One')     #{} are not allowed in if and else condition
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
-----------------------------------------------------------------------------------------------------------------------------------
7
# Identify  error
if  ():
	print('One')
	print('Two')
	print('Three')
else:
if  []:
	print('Four')
	print('Five')    #if must be indented in else statement
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
------------------------------------------------------------------------------------------------------------------------------
8
# Write  a  program  to  determine  a  number  is  even  or  odd  with   if  statement
a=int(input('Enter any positive number: '))
if(a%2==0):
	print('Even number')
else:
	print('Odd number')
-------------------------------------------------------------------------------------------------------------------------------
9
# Find outputs  (Home  work)
if():
        print('Hyd')   #if condition is false, so else part will be executed
        print('Sec')
        print('Cyb')
else:
        print('One')   #One
        print('Two')   #Two
        print('Three') #Three
print('Bye')           #Bye
--------------------------------------------------------------------------------------------------------------------------------
10
# Find  outputs  (Home  work)
if{10 : 20 , 30 : 40}:   
        print('Hyd')     #Hyd
        print('Sec')     #Sec
        print('Cyb')     #Cyb
print('Bye')             #Bye
--------------------------------------------------------------------------------------------------------------------------------
11
# Find outputs  (Home  work)
if { }:
	print('Hyd')
	print('Sec')   
	print('Cyb')
print('Bye')       #Bye , because if condition is false
--------------------------------------------------------------------------------------------------------------------------------
12
# Write   a  program  to  print  month  name  for  input  month  number  by  using  if  and  elif  (Home  work)
try:
  a=int(input('Enter month number (1 - 12): '))
  if(a==1):
	  print('Jan')
  elif(a==2):
	  print('Feb')
  elif(a==3):
	  print('Mar')
  elif(a==4):
	  print('Apr')
  elif(a==5):
	  print('May')
  elif(a==6):
	  print('June')
  elif(a==7):
	  print('July')
  elif(a==8):
	  print('Aug')
  elif(a==9):
	  print('Sep')
  elif(a==10):
	  print('Oct')
  elif(a==11):
	  print('Nov')
  elif(a==12):
	  print('Dec')
  else:
	  print('Input  should  be  between  1  and   12')
except:
	print('Input should be an integer')

sample OP:
Enter month number (1 - 12): 7
july

Enter month number (1 - 12): 13
Input  should  be  between  1  and   12

Enter month number (1 - 12): 10.8
Input  should  be  an  integer
----------------------------------------------------------------------------------------------------------------------------
13
#Write  a  program  to  test  year  is  leap  year  or  not
1) What  is  leap  year ?  --->  Divisible  by  4  but  not  by  100   (or)  divisble  by  400
2) Are  2016 , 2020 , 2024  leap  years ? --->  Yes  becoz  leap  year  for  every  4  yearrs
3) Are  1700 , 1800 , 1900  leap  years ? --->  No  becoz  no  leap  year  for  every  100  years
4) Are  1600 , 2000 , 2400  leap  years ?  --->  Yes  becoz  leap  year  for  every  400  years
5) Hint:  3  conditions

a= int(input('Enter 4-digit year: '))
if(a%400==0) or (a%4==0 and a%100!=0):
	print('Leap Year')
else:
	print('Not a leap year')

sample OP
Enter  4-digit  year :  2024
Leap year
Enter  4-digit  year :  1900
Not a leap year
---------------------------------------------------------------------------------------------------------------------------------------
14
#Write  a  program  to  determine  largest  of  three  numbers  with  if  and  else
#Hint:  Write  multiple  conditions

a=int(input('Enter 1st input: '))
b=int(input('Enter 2nd input: '))
c=int(input('Enter 3rd input: '))
if a>b and a>c:
	print('Largest number: ',a)
elif(b>c):
	print('Largest number: ',b)
else:
	print('Largest number: ',c)

sample OP
Enter 1st input : 10
Enter 2nd input : 20
Enter 3rd input : 15
Laregst  number  :   20
--------------------------------------------------------------------------------------------------------------------------------------------
15
Write  a  program  to  convert  celsius  temperature  to  farenheit  and  vice-versa
1) What  is  the  formula  to  convert  celsius  to  farenheit ? --->  1.8 * temp + 32
2) What  is  the  formula  to  convert  farenheit  to  celsius ?  --->  (temp - 32) / 1.8

a = int(input('Enter  1  to  convert  celsius  to  farenheit  and  2  to  convert  fahrenheit  to  celsius : '))
if(a==1):
	temp =float(input('Enter celsius temperature: '))
	CtoF=(1.8*temp)+32
	print('Fahrenheit Equivalent: ',CtoF)
elif(a==2):
	temp =float(input('Enter farenheit temperature: '))
	FtoC=(temp-32)/1.8
	print(f'Celsius Equivalent:  {FtoC:.2f}')
else:
	print('Invalid input')

sample OP
Enter  1  to  convert  celsius  to  farenheit  and  2  to  convert  fahrenheit  to  celsius :  2
Enter  fahrenheit  temperature : 100
celsius   equivalent :  37.78

Enter  1  to  convert  celsius  to  farenheit  and  2  to  convert  fahrenheit  to  celsius :  1
Enter  celsius  temperature :  30
Fahrenheit  Equivalent  :  86.0

Enter  1  to  convert  celsius  to  farenheit  and  2  to  convert  fahrenheit  to  celsius :  3
Invalid input
----------------------------------------------------------------------------------------------------------------------------------------------------
16
Write  a  program  to  test  a  point  (x , y)  lies  in  1st  quadrant , 2nd  quadrant , 3rd  quadrant ,
4th  quadrant , x - axis , y - axis   or  origin

1) What  are  the  values  of  x  and  y  in  1st  quadrant ?  --->  Both  are  +ve
2) What  are  the  values  of  x  and  y  in  2nd  quadrant ?  --->  'x'  is  -ve  and  'y'  is  +ve
3) What  are  the  values  of  x  and  y  in  3rd  quadrant ?  ---> Both   are  -ve
4) What  are  the  values  of  x  and  y  in  4th  quadrant ?  --->  'x'  is   +ve  and  'y'  is  -ve
5) What  are  the  values  of  x  and  y  on  x - axis ?  ---> 'x'  is  non-zero  and  'y'  is  0
6) What  are  the  values  of  x  and  y  on  y - axis ?  --->  'x'  is  0  and  'y'  is  non-zero
7) What  are  the  values  of  x  and  y  if  point  is  origin ?  --->  Both  are  zeroes
8) Hint:  Use  if  ..   elif

a=int(input('Enter  value  of  x  co-ordinate: '))
b=int(input('Enter  value  of  y  co-ordinate: '))
if(a>0 and b>0):
	print('1st quadrant')
elif(a<0 and b>0):
	print('2nd quadrant')
elif(a<0 and b<0):
	print('3rd quadrant')
elif(a>0 and b<0):
	print('4th quadrant')
elif(a!=0 and b==0):
	print('x-axis')
elif(a==0 and b!=0):
	print('y-axis')
else:
	print('origin (0,0)')

sample OP:
Enter  value  of  x  co-ordinate :  -10
Enter  value  of  y  co-ordinate :  20
2nd quadrant
------------------------------------------------------------------------------------------------------------------------------------------------------------
17
Write  a  program  to  determine  largest , smallest  and  middle  of  three  numbers

1) What  is  the  initial  value  of  max  ?  --->  a
2) Whichever  input >  max,  copy  that  input  to  max
3) What  is  the  initial  value  of  min  ?  --->  'a'
4) Whichever  input  <  min,  copy  that  input  to  min
5) How  to  obtain  middle  number ?  --->   Eliminate  max  and  min  from  a , b , c


a=float(input('Enter first input: '))
b=float(input('Enter second input: '))
c=float(input('Enter third input: '))
max=a
min=a
if(b>max):
	max=b
if(c>max):
	max=c
if(b<min):
    min=b
if(c<min):
	min=c
Mid=(a+b+c)-(max+min)
print('Largest number: ',max)
print('Smallest number: ',min)
print('Middle number: ',Mid)

sample OP
Enter  first  input   :  10
Enter  second   input   :  20
Enter  third  input   :  7
Largest number :  20.0
Smallest number :  7.0
Middle number :  10.0
------------------------------------------------------------------------------------------------------------------------------------------------------
18
Write  a  program  to  determine  three  sides  form  a  triangle  or  not

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
5) Hint: Use  nested  if

from math import sqrt
a = float(input('Enter 1st side: '))
b = float(input('Enter 2nd side: '))
c = float(input('Enter 3rd side: '))
if (a + b > c and b + c > a and a + c > b):
    if a == b == c:
        print('Equilateral triangle')
        area = (sqrt(3) / 4) * (a ** 2) 
        print('Area:', area)
    elif a == b or a == c or b == c:
        print('Isosceles triangle')
        per = a + b + c
        print('Perimeter:', per)
    elif a != b and a != c and b != c:
        print('Scalene triangle')
        per = a + b + c
        s = per / 2
        area = sqrt(s * (s - a) * (s - b) * (s - c))
        print(f'Area: {area:.2f}')
        print('Perimeter:', per)
else:
    print('Not a triangle')

sample OP
Enter  1st  side : 3
Enter  2nd  side : 4
Enter  3rd  side : 5
Scalene  triangle
Area : 6.00
Perimeter : 12.0

Enter  1st  side : 3
Enter  2nd  side : 4
Enter  3rd  side : 8
Not  a  triangle
----------------------------------------------------------------------------------------------------------------------------------------------------
19
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
	 What  is  root2  if  real  part  is  3  and  imag  part  is  4 ?  --->  3 - 4j

import math
a = float(input("Enter value of a: "))
b = float(input("Enter value of b: "))
c = float(input("Enter value of c: "))
if a == 0:
    print("Value  of  a  can  not  be  0")
else:
    disc = b**2 - 4*a*c  
    print(f"Discriminant: {disc}")

    if disc > 0:
        print("Roots are Real and Distinct")
        root1 = (-b + math.sqrt(disc)) / (2*a)
        root2 = (-b - math.sqrt(disc)) / (2*a)
    elif disc == 0:
        print("Roots are Real and Same")
        root1 = root2 = -b / (2*a)
    else:
        print("Roots are imaginary  (or) complex")
        real_part = -b / (2*a)
        imag_part = math.sqrt(-disc) / (2*a)
        root1 = complex(real_part, imag_part)
        root2 = complex(real_part, -imag_part)
    
    print(f"Root 1: {root1}")
    print(f"Root 2: {root2}")

sample OP
Enter  value  of  a : 5
Enter  value  of  b : 6
Enter  value  of  c : 5
Roots  are  imaginary  (or) complex
Root 1 : -0.6 +  0.8j
Root 2 : -0.6 -  0.8j

Enter value of a: 0
Enter value of b: 2
Enter value of c: 4
Value  of  a  can  not  be  0
------------------------------------------------------------------------------------------------------------------------------------------------------
20
Write  a  program   to  determine  a  point (x , y)  lies  inside , outside  or  on  the  circle.
Center  is  origin  and  radius  is  'r'

1) What  is  the  distance  between  origin  and  point (x , y) ?  --->  sqrt(x ^ 2 + y ^ 2)
2) Where  is  the  point  if  distance >  raidus ?  --->  Outside  the  circle
3) Where  is  the  point  if  distance < raidus ?  --->  Inside  the  circle
4) Where  is  the  point  if  distance  and  raidus   are  same ?  ---> On  the  circle

from math import sqrt
x=int(input('Enter value of x: '))
y=int(input('Enter value of y: '))
r=int(input('Enter radius of circle: '))
dis=sqrt(x**2+y**2)
if(dis>r):
	print('Point is outside the circle')
elif(dis<r):
	print('Point is inside the circle')
else:
	print('Point is on the circle')

sample OP
Enter  value  of  x : 3
Enter  value  of  y : 4
Enter radius of circle : 5
Point is on the circle
----------------------------------------------------------------------------------------------------------------------------------------------------
21
# Find  outputs  (Home  work)

m = 4
match  m:
	case  1:
		print('One')   
	case  2:
		print('Two')
	case  3:
		print('Three')
print('Bye')            #Bye  because m=4 doesnt match any case
---------------------------------------------------------------------------------------------------------------------------------------------------
22
# Identify  Error
i = 2
match  i:
	case  1:
		print('One')
	case  _:
		print('None of   the  above')   #anonymous case must be at the end of match because it interupts reading of other cases
	case  2:
		print('Two')
print('Bye')
------------------------------------------------------------------------------------------------------------------------------------------------------
23
# Find  outputs  (Home  work)
m = 2
match  m:
	case  1:
		print('One')
	case  _:
		print('Hello')    #error-anonymous case must be at the end of match and it must be apppear only once
	case  _:
		print('Bye')    
print('End')
-----------------------------------------------------------------------------------------------------------------------------------------------------
24
#  Find  outputs  (Home  work)
m = 1
match  m:
	case  1:
		print('Hyd')   #Hyd
	case  1:
		print('Sec')    #duplicates cases- only case 1 will be executed
	case  1:
		print('Cyb')
print('Bye')          #Bye
----------------------------------------------------------------------------------------------------------------------------------------------------
25
# Find  outputs  (Home  work)
ch = 'B'
match  ch:
	case   'A':
		print('Apple')    
	case  'B':
		print('Book')              #Book 
	case  'C':
		print('Cafe')
	case  _:
		print('None of  the  above')
print('Bye')                       #Bye
-----------------------------------------------------------------------------------------------------------------------------------------------------
26
1) What  are  the  outputs  if  input  is  -6 ? --->Hyd Sec Cyb Bye (print each word in next line)
2) What  are  the  outputs  if  input  is  15  ?  ---> One Two Three Bye (print each word in next line)
3) What  are  the  outputs  if  input  is  10.8  ?  ---> India China Usa Bye ('case _' holds 10.8),(print each word in next line)
4) What  are  the  outputs  if  input  is  0  ?  --->Hyd Sec Cyb Bye (print each word in next line)
5) What  are  the  outputs  if  input  is  -10  ?  ---> One Two Three Bye (print each word in next line)
6) What  are  the  outputs  if  input  is  7  ?  ---> Hyd Sec Cyb Bye (print each word in next line)

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
------------------------------------------------------------------------------------------------------------------------------------------------------
27
What  is  '|'  operator  called ?  --->  Bitwise  or  operator

1) What  is  the  output  when  input  is  (-10 , -20) ?  ---> Quadrant 
2) What  is  the  output  when  input  is  (10 , 0) ?  ---> x - axis
3) What  is  the  output  when  input  is  (0 , -20) ?  ---> y - axis
4) What  is  the  output  when  input  is  (0 , 0) ?  ---> Origin
5) What  is  the  output  when  input  is  (10 , 20 , 30) ?  ---> Not  a  point 
6) What  is  the  output  when  input  is  [10 , 20]  ?  ---> Quadrant
7) What  is  the  output  when  input  is  [0 , -25]  ?  ---> y - axis
8) What  is  the  output  when  input  is  ()  ?  --->  Not  a  point
9) What  is  the  output  when  input  is  {10 , 20} ?  --->  Not  a  point
10) What  is  the  output  when  input  is  (25,) ?  ---> Not  a  point

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
-----------------------------------------------------------------------------------------------------------------------------------------------
28
(Home  work)
Write  a   program  to  print  day  of  the  week
1  - Monday
2  - Tuesday
3  - Wednesday
....
7 - Sunday
8 - Invalid
Hint:  Use  match ... case

try:
    x = int(input('Enter any day of the week (1-7): '))
    match x:
        case 1:
            print('Monday')    
        case 2:
            print('Tuesday')             
        case 3:
            print('Wednesday')
        case 4:
            print('Thursday')
        case 5:
            print('Friday')
        case 6:
            print('Saturday')
        case 7:
            print('Sunday')
        case _:
            print('Invalid')
except:
    print('Input must be integer')
---------------------------------------------------------------------------------------------------------------------------------------------------
29
(Home  work)
Write  a  program  to  print  digit in  words
0  -   Zero
1  -   One
2  -   Two
...
9  - Nine
10 -  Not  a  digit
Hint:  Use  match  ..  case

x = input("Enter a digit (0-9): ")
match x:
    case '0':
        print("0 - Zero")
    case '1':
        print("1 - One")
    case '2':
        print("2 - Two")
    case '3':
        print("3 - Three")
    case '4':
        print("4 - Four")
    case '5':
        print("5 - Five")
    case '6':
        print("6 - Six")
    case '7':
        print("7 - Seven")
    case '8':
        print("8 - Eight")
    case '9':
        print("9 - Nine")
    case _:
        print(f"{x} - Not a digit")
----------------------------------------------------------------------------------------------------------------------------------------------------------
30
Write  a  program  to  determine  bill  amount  and  input  is  units

Units                                                      Cost
-------------------------------------------------------------------------
First  100  units(0-99)					Rs. 3.00 / unit

Next  100  units(100-199)				Rs. 3.50 / unit

Next  200  units(200-299)				Rs. 4.00 / unit

Next  300  units(300-399)				Rs. 4.50 / unit

Above  700  units(>=700)				Rs. 5.00 / unit
-------------------------------------------------------------------------
Let  units  be  1200
What  is  the  bill  amount ? --->  100 * 3.00 + 100 * 3.50 + 200 * 4.00 + 300 * 4.50 +  500 * 5.00
Hint:  Use  match  ...  case   but  not  if ... else

units=int(input('Enter  units :   '))
match units//100:
	case 0:
		cost= 100*3.00
	case 1:
		cost= 100*3.00+(units-100)*3.50
	case 2|3:
		cost= 100*3.00+100*3.50+(units-200)*4.00
	case 4|5|6:
		cost = 100*3.00+100*3.50+200*4.00+(units-400)*4.50
	case _:
		cost= 100*3.00+100*3.50+200*4.00+300*4.50+(units-700)*5.00
print('Bill amount : ',cost)
-----------------------------------------------------------------------------------------------------------------------------------------
31
Write  a  program  to  print  fibonacci  series  upto   x

Let  input  be   10
What  are  the  outputs  ?  ---> 0 , 1 , 1 , 2 , 3 , 5 , 8

1) What  is  10th  term ?  --->  9th  term + 8th  term
    What  is  3rd  term ?  --->  2nd  term + 1st  term
    What  is  ith  term ?  --->  (i - 1)th  term +  (i - 2)  term
2) What  are  the  first  two  terms ?  --->  0  and  1
3) Hint:  Use  while  loop

x= int(input('Enter value of x: '))
if x==0:
	print('Fibonacci series')
	print(0)
else:
	a=0
	b=1
	print('Fibonacci series')
	print(a)
	print(b)
	c=a+b
	while(c<=x):
		print(c)
		a=b
		b=c
		c=a+b

Enter  value  of  x  :  1
Fibonacci  Series
0
1
1

Enter  value  of  x  :  0
Fibonacci  series
0
------------------------------------------------------------------------------------------------------------------------------------
32
#  Find  outputs
while  True:
	print('Hello')   #prints hello forever because condition is true
print('Bye')
-----------------------------------------------------------------------------------------------------------------------------
33
#  Find  outputs
while  False:
	print('Hello')   
print('Bye')        #Bye - condition is false
 

