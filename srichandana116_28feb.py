# Identify  error
else 1:
		print('else  suite')
print('Outside')
#we cant give else without if 
if  9 > 5
	print('Hello')
print('Bye')
#no colon after condition in if statement
if  9 > 12:
	print('Hyd')
else
	print('Sec')
#no colon after else in statement    
if  (10,20,15):
print('Hyd')
else:
print('Sec')
#indentation error
if  ():
			print('Hyd')
	else:
					print('Sec')
print('Bye')
#irregular indentation error
if  { }:
{
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
#the flower braces should be indented as they resemble set the print statements should have comma seperation
if  ():
	print('One')
	print('Two')
	print('Three')
else:
if  []:
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
#the if statemnet is not indented after given else at every step and improper if else formation
# Write  a  program  to  determine  a  number  is  even  or  odd  with   if  statement
#a=int(input("enter number:"))
if a%2==0:
    print("Even")
else:
    print("Odd")
# Find outputs  (Home  work-1)
if():
        print('Hyd')
        print('Sec')
        print('Cyb')
else:
        print('One')
        print('Two')
        print('Three')
print('Bye')
# Find outputs  (Home  work-2)
if{10 : 20 , 30 : 40}:
        print('Hyd')
        print('Sec')
        print('Cyb')
print('Bye')
# Find outputs  (Home  work-3)
if { }:
	print('Hyd')
	print('Sec')
	print('Cyb')
print('Bye')
# Write   a  program  to  print  month  name  for  input  month  number  by  using  if  and  elif  (Home  work)
try:
    m=int(input("Enter month number (1 - 12): "))
    if m==1:
        print(" January")
    elif m==2:
        print(" February")
    elif m==3:
        print(" March")
    elif m==4:
        print(" April")
    elif m==5:
        print(" May")
    elif m==6:
        print(" June")
    elif m==7:
        print(" July")
    elif m==8:
        print(" August")
    elif m==9:
        print(" September")
    elif m==10:
        print(" October")
    elif m==11:
        print(" November")
    elif m==12:
        print(" December")
    else:
        print("Input  should  be  between  1  and   12")
except:
    print("Input  should  be  an  integer")
#Write  a  program  to  test  year  is  leap  year  or  not
try:
    y=int(input("Enter 4-digit year: "))
    if len(y)==4:
        if (y % 4==0 and y % 100!=0) or y % 400==0 :
            print("Leap year")
        else:
            print("Not a Leap year")
except:
    print("Input  should  be a 4 digit integer ")
#Write  a  program  to  determine  largest  of  three  numbers  with  if  and  else
try:
    a = int(input("Enter 1st input : "))
    b = int(input("Enter 2nd input : "))
    c = int(input("Enter 3rd input : "))
    if a>b and a>c:
        print("Largest  Input  :",a)
    if b>c:
        print("Largest  Input  :",b)
    else:
        print("Largest  Input  :",c)
except:
    print("Input  should  be  an  integer")
#Write  a  program  to  convert  celsius  temperature  to  farenheit  and  vice-versa
try:
    a = int(input("Enter  1  to  convert  celsius  to  farenheit  and  2  to  convert  fahrenheit  to  celsius : "))

    if a==1:
        temp = float(input("Enter celsius  temperature: "))
        fah=(1.8*temp)+32
        print(f"Fahrenheit  Equivalent  :{fah:.2f}")
    elif a==2:
        tem = float(input("Enter fahrenheit  temperature: "))
        cel=(tem-32)/1.8
        print(f"celsius  Equivalent  :{cel:.2f}")
    else:
        print("Input  should  be  1 or 2")
except:
    print("Input  should  be  an  integer")
#Write  a  program  to  test  a  point  (x , y)  lies  in  1st  quadrant , 2nd  quadrant , 3rd  quadrant ,
#4th  quadrant , x - axis , y - axis   or  origin
try:
    x = float(input("Enter x-axis co-ordinate : "))
    y = float(input("Enter y-axis co-ordinate : "))
    if x>0 and y>0:
        print("1st quadrant")
    elif x>0 and y<0:
        print("4th quadrant")
    elif x<0 and y>0:
        print("2nd quadrant")
    elif x<0 and y<0:
        print("3rd quadrant")
    elif x==0 and y!=0:
        print("on y-axis")
    elif y==0 and x!=0:
        print("on x-axis")
    elif x==0 and y==0:
        print("Origin")
except:
    print("Input  should  be  an  integer")
#Write  a  program  to  determine  largest , smallest  and  middle  of  three  numbers
#1 method
try:
    a = int(input("Enter 1st input : "))
    b = int(input("Enter 2nd input : "))
    c = int(input("Enter 3rd input : "))
    max_num=a
    min_num=a
    if b>max_num:
        max_num=b
    if c>max_num:
        max_num=c
    if b<min_num:
        min_num=b
    if c<min_num:
        min_num=c
    mid_num=(a+b+c)-(max_num+min_num)
    print("Largest number:", max_num)
    print("Smallest number :", min_num)
    print("Middle number :", mid_num)
        
except:
    print("Input  should  be  an  integer")
#2 method
  try:
    a = int(input("Enter 1st input : "))
    b = int(input("Enter 2nd input : "))
    c = int(input("Enter 3rd input : "))
    x=max(a,b,c)
    y=min(a,b,c)
    print("Largest number  :",x)
    print("Smallest number  :",y)
    print("Middle number :",(a+b+c)-(x+y))
    
        
except:
    print("Input  should  be  an  integer")
#Write  a  program  to  determine  three  sides  form  a  triangle  or  not
try:
    from math import *
    a = int(input("Enter 1st side : "))
    b = int(input("Enter 2nd side : "))
    c = int(input("Enter 3rd side : "))
    if (a+b>c) and (b+c>a) and (a+c>b):
        if a==b and b==c:
            print("equilateral triangle")
            Area= (sqrt(3))/4*(pow(a,2))
            print(f"Area: {Area:.2f}")
        elif a==b or b==c or c==a:
            print("isoscles triangle")
            s=(a+b+c)/2
            Area= sqrt(s * (s - a) * (s - b) * (s - c))
            print(f"Area: {Area:.2f}")
        else:
            print("scalene triangle")
            s=(a+b+c)/2
            Area= sqrt(s * (s - a) * (s - b) * (s - c))
            print(f"Area: {Area:.2f}")
        print("perimeter: ",a+b+c)
    else:
        print("Not  a  triangle, Sum  of  every  two  sides  should  be  >  3rd  side")
except:
    print("Input  should  be  an  integer")
#Write  a  program  to  determine  roots  of  a  quadtratic  equation  a * x ^ 2 + b * x + c = 0  where  a  ! = 0
try :
    from math import *
    print("enter values of quadtratic  equation  respectively a * x ^ 2 + b * x + c = 0")
    a = float(input("Enter value of a: "))
    if a == 0:
        print("Value of a cannot be 0")
    else:
        b = float(input("Enter value of b: "))
        c = float(input("Enter value of c: "))
        disc=(b**2-4*a*c)
        if disc>0:
            print("Real  and  distinct roots")
            root1=(-b+(sqrt(b**2-4*a*c)))/(2*a)
            root2=(-b-(sqrt(b**2-4*a*c)))/(2*a)
            print(f"root 1:{root1:.2f}")
            print(f"root 2: {root2:.2f}")
        elif disc<0:
            print("Complex  (or)  Imaginary  roots")
            real=-(b/(2*a))
            imag=sqrt(-(disc))/(2*a)
            print(f"root 1:{real:.2f} + {imag:.2f}j")
            print(f"root 2:{real:.2f} - {imag:.2f}j")
        else:
            print("Real  and  equal")
            print("root 1 & 2:",-(b)/(2*a))
except:
    print("Input  should  be  an  integer")
##Write  a  program   to  determine  a  point (x , y)  lies  inside , outside  or  on  the  circle.
#Center  is  origin  and  radius  is  'r'
  try:
    from math import *
    x = int(input("Enter value  of  x: "))
    y = int(input("Enter value  of  y: "))
    r = int(input("Enter radius of circle : "))
    dist= sqrt(x**2+y**2)
    if dist==r:
        print("Point is on the circle")
    elif dist<r:
        print("Inside the circle")
    elif dist>r:
        print("Outside the circle")
except:
    print("Input  should  be  an  integer")
## Find  outputs  (Home  work
m = 4
match  m:
	case  1:
		print('One')
	case  2:
		print('Two')
	case  3:
		print('Three')
print('Bye')
#prints 'Bye' as match m doesn't match with any case
# Identify  Error
i = 2
match  i:
	case  1:
		print('One')
	#case  _:
		print('None of   the  above')
	case  2:
		print('Two')
print('Bye')
#_ case should be given at last
# Find  outputs  (Home  work)
m = 2
match  m:
	case  1:
		print('One')
	case  _:
		print('Hello')
	case  _:
		print('Bye')
print('End')
#error there cannot be 2 _ anonymous cases
#  Find  outputs  (Home  work)
m = 1
match  m:
	case  1:
		print('Hyd')
	case  1:
		print('Sec')
	case  1:
		print('Cyb')
print('Bye')
#prints "hyd" case 1 gets executed and doesn't go to remaining lines
# Find  outputs  (Home  work)
ch = 'B'
match  ch:
	case   'A':
		print('Apple')
	case  'B':
		print('Book')
	case  'C':
		print('Cafe')
	case  _:
		print('None of  the  above')
print('Bye')
#matches ch ="B" and prints book and bye
#practice bitwise or (pipe operator)
try:
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
except:
    print("Input  should  be  an  integer")

'''  (Home  work)
Write  a   program  to  print  day  of  the  week
1  - Monday  2  - Tuesday 3  - Wednesday
Hint:  Use  match ... case '''

try:
    x = int(input('Enter any number: '))
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
    # End of match
    print('Bye')
except ValueError:
    print("Input should be an integer")

#match with tuple conditions
try:
    tpl = tuple(map(int, input('Enter any point in the form of x,y: ').split(',')))  # Read input safely
    match tpl:
        case (0, 0):
            print('Origin')
        case (0, y):
            print('y-axis')
        case (x, 0):
            print('x-axis')
        case (x, y):
            if x > 0 and y > 0:
                print('1st Quadrant')
            elif x < 0 and y > 0:
                 print('2nd Quadrant')
            elif x < 0 and y < 0:
                print('3rd Quadrant')
            elif x > 0 and y < 0:
                print('4th Quadrant') 
        case _:
            print('Not a valid point')
except ValueError:
    print("Input should be in the format x,y with integer values")
'''  (Home  work)
Write  a  program  to  print  digit in  words
0  -   Zero
1  -   One'''
try:
    x = int(input('Enter any number: '))
    match x:
        case 0:
            print('Zero')
        case 1:
            print('One')
        case 2:
            print('Two')
        case 3:
            print('Three')
        case 4:
            print('Four')
        case 5:
            print('Five')
        case 6:
            print('Six')
        case 7:
            print('Seven')
        case 8:
            print('Eight')
        case 9:
            print('Nine')
        case 10:
            print('Not a digit')
        case _:
            print("Not a valid input, input should be in 0-9")
except ValueError:
    print("Input should be an integer")
#Write  a  program  to  determine  bill  amount  and  input  is  units
try:
    u = float(input("Enter units of power used: "))
    
    match u // 100:  # Corrected match statement
        case 0:
            b = u * 3.00
        case 1:
            b = 300 + (u - 100) * 3.50
        case 2 | 3:
            b = 650 + (u - 200) * 4.00
        case 4 | 5 | 6:
            b = 1450 + (u - 400) * 4.50
        case _:
            b = 2800 + (u - 700) * 5.00
    
    print(f"Bill amount: {b:.2f}")  # Print outside of match
except ValueError:
    print("Input should be a number")
#Write  a  program  to  print  fibonacci  series  upto   x
n = int(input("Enter a value up to which you want to print Fibonacci series: "))
a=0
b = 1  
print("Fibonacci series:")
while a <= n: 
    print(a) 
    a=b
    b=a+b
#



