# Identify  error
else:
        print('else  suite')
print('Outside')
# we cant use else without if

# Identify  error
if  9 > 5
    print('Hello')
print('Bye')
# there is no ':' in the if statement

# Identify  error
if  9 > 12:
    print('Hyd')
else
    print('Sec')
# there is no ':' in the else statement

# Identify  error
if  (10,20,15):
print('Hyd')
else:
print('Sec')
# Indentation error after 'if' and also after 'else'

# Identify  error
if  ():
            print('Hyd')
    else:
                    print('Sec')
print('Bye')
#indentation error for 'else'

# Identify  error
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
#braces are not used in python for block statements

# Identify  error
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
#Indentation errors after else blocks

# Write  a  program  to  determine  a  number  is  even  or  odd  with   if  statement
a = int(input("Enter integer number : "))
if a%2==0:
    print("Even")
else:
    print("Odd")
# output:
# Enter integer number : 234
# Even

# Find outputs  (Home  work)
if():
        print('Hyd')
        print('Sec')
        print('Cyb')
else:
        print('One')
        print('Two')
        print('Three')
print('Bye')
#output:
# One
# Two
# Three
# Bye

# Find  outputs  (Home  work)
if{10 : 20 , 30 : 40}:
        print('Hyd')
        print('Sec')
        print("Cyb")
print('Bye')
# Output:
# Hyd
# Sec
# Cyb
# Bye

# Find outputs  (Home  work)
if { }:
	print('Hyd')
	print('Sec')
	print('Cyb')
print('Bye')
# output:
# Bye

# Write   a  program  to  print  month  name  for  input  month  number  by  using  if  and  elif  (Homework)
try:
    a = int(input("Enter month number (1-12) : "))
    if a == 1:
        print("january")
    elif a == 2:
        print("february")
    elif a == 3:
        print("march")
    elif a == 4:
        print("april")
    elif a == 5:
        print("may")
    elif a == 6:
        print("june")
    elif a == 7:
        print("july")
    elif a == 8:
        print("august")
    elif a == 9:
        print("september")
    elif a == 10:
        print("october")
    elif a == 11:
        print("november")
    elif a == 12:
        print("december")
    else:
        print("Input  should  be  between  1  and   12")
except:
    print("Input  should  be  an  integer")

# output:
# Enter month number (1-12) : 2
# february

'''
Write  a  program  to  test  year  is  leap  year  or  not

1) What  is  leap  year ?  --->  Divisible  by  4  but  not  by  100   (or)  divisible  by  400

2) Are  2016 , 2020 , 2024  leap  years ? --->  Yes  becoz  leap  year  for  every  4  years

3) Are  1700 , 1800 , 1900  leap  years ? --->  No  becoz  no  leap  year  for  every  100  years

4) Are  1600 , 2000 , 2400  leap  years ?  --->  Yes  becoz  leap  year  for  every  400  years

5) Hint:  3  conditions
'''
a = eval(input("Enter  4-digit  year : "))
if a%4==0 and a%100!=0 or a%400==0:
        print("leap year")
else:
        print("Not a leap year")
# Output:
# Enter  4-digit  year : 2024
# leap year

'''
Write  a  program  to  determine  largest  of  three  numbers  with  if  and  else

Hint:  Write  multiple  conditions
'''
a = eval(input("Enter 1st input : "))
b = eval(input("Enter 2st input : "))
c = eval(input("Enter 3st input : "))
if a > b and a > c:
        print("a")
elif b > a and b > c:
        print("b")
else:
        print("c")
# Output:
# Enter 1st input : 10
# Enter 2st input : 20
# Enter 3st input : 9
# b

'''
Write  a  program  to  convert  celsius  temperature  to  fahrenheit  and  vice-versa

1) What  is  the  formula  to  convert  celsius  to  fahrenheit ? --->  1.8 * temp + 32

2) What  is  the  formula  to  convert  fahrenheit  to  celsius ?  --->  (temp - 32) / 1.8
'''
try:
        a = eval(input(F"Enter 1  to  convert  celsius  to  fahrenheit  and  2  to  convert  fahrenheit  to  celsius : "))
        if a == 1 :
                b = float(input("Enter  celsius  temperature : "))
                print(F"Fahrenheit Equivalent : {1.8*b+32}")
        elif a == 2:
                d = float(input("Enter fahrenheit temperature : "))
                print(F"Celsius Equivalent : {(d - 32) / 1.8:.2f}")
        else:
                print("Enter valid input")
except:
        print("Invalid input")

# output:
# Enter 1  to  convert  celsius  to  fahrenheit  and  2  to  convert  fahrenheit  to  celsius : 2
# Enter fahrenheit temperature : 123
# Celsius Equivalent : 50.56

'''
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
'''
try:
        a = int(input("Enter X input : "))
        b = int(input("Enter Y input : "))
        if  a >=1 <=b:
                print("1st Quadrant")
        elif a <=-1 >=b:
                print("3rd Quadrant")
        elif a >= 1 and b<=-1:
                print("4th Quadrant")
        elif a <= -1 and b>=1:
                print("2nd Quadrant")
        elif a>=1 or a<=-1 and b==0:
                print("X axis")
        elif a==0 and b>=1 or b<=-1:
                print("Y axis")
        elif a==0==b:
                print("Origin")
        else:
                print("Enter valid value")
except:
        print("Enter only integers")

# output:
# Enter X input : 2
# Enter Y input : -2
# 4th Quadrant

'''
Write  a  program  to  determine  largest , smallest  and  middle  of  three  numbers
'''
a = eval(input("Enter 1st integer : "))
b = eval(input("Enter 2nd integer : "))
c = eval(input("Enter 3rd integer : "))
Max_num = a
if b>Max_num:
 Max_num = b
if c>Max_num:
 Max_num =c
print(F"Max number : {Max_num}")
Min_num = a
if Min_num>b:
 Min_num = b
if Min_num>c:
 Min_num = c
print(F"Min number : {Min_num}")
print(F"Mid Number : {(a+b+c)-(Max_num+Min_num)}")
# Output:
# Enter 1st integer : 12
# Enter 2nd integer : 45
# Enter 3rd integer : 30
# Max number : 45
# Min number : 12
# Mid Number : 30

'''
Write  a  program  to  determine  three  sides  form  a  triangle  or  not

1) Find  area  if  it  is  an  equilateral  triangle
    What  is  an  equilateral  triangle ?  ---> All  the  three  sides  should  be  same
    What  is  the  area  of  equilateral  triangle ?  --->  sqrt(3) / 4 * a ^ 2

2) Find  perimeter  if  it  is  an  isosceles  triangle
    What  is  an  isosceles  triangle ?  ---> Any  two  sides  are  same
    What   is  the  perimeter  of  isosceles  triangle ?  ---> a + b + c

3) Find  both  if  it  is  scalene  triangle
    What  is  a  scalene  triangle ?  ---> All  the  three  sides  are  different
    What  is  the  area  of  scalene  triangle ?  ---> sqrt(s * (s - a) * (s - b) * (s - c))
	What  is  the  value  of  's'  ?  --->  	(a + b + c) / 2
    What   is  the  perimeter  of  scalene  triangle ?  --->  a + b + c

4) What  is  the  qualification  of  triangle  ?  --->  Sum  of  every  two  sides  should  be  >  3rd  side

5) Hint: Use  nested  if
'''

try:
        import math
        a = float(input("enter 1st side : "))
        b = float(input("enter 2nd side : "))
        c = float(input("enter 3rd side : "))
        if a+b>c and b+c>a and c+a>b:
         if a==b==c:
                print("Equilateral Triangle")
                print(F"Area : {math.sqrt(3)/4*pow(a,2):.2f}")
         elif a!=b and b!=c and c!=a:
                print("Scalene Triangle")
                s = (a+b+c)/2
                print(F'Area : {math.sqrt((s * (s - a) * (s - b) * (s - c)))}')
                print(F'Perimeter : {a+b+c}')
         else:
                print("Isosceles  triangle")
                print(F'Perimeter : {a + b + c}')


        else:
                print("Not a triangle")
except:
        print("Enter Valid Value")
# Output:
# enter 1st side : 7
# enter 2nd side : 7
# enter 3rd side : 7
# Equilateral Triangle
# Area : 21.22

'''
Write  a  program  to  determine  roots  of  a  quadratic  equation  a * x ^ 2 + b * x + c = 0  where  a  ! = 0

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
'''
import math

a = float(input("enter 1st value where a!=0: "))
b = float(input("enter 2nd value : "))
c = float(input("enter 3rd value : "))
disc = b**2 - 4 *a *c
if a==0:
        print("a cannot be 0")
elif disc>0:
        print("Real  and  distinct")
        print(F'Root 1 :{(-b + math.sqrt(disc)) / (2 * a):.2f}')
        print(F'Root 2 :{(-b - math.sqrt(disc)) / (2 * a):.2f}')
elif disc==0:
        print("Real  and  same")
        print(F"Root : {-b/2*a:.2f}")
else:
        print("Complex  (or)  Imaginary  roots")
        realpart = -b/2*a
        imagpart = math.sqrt(-disc)/(2*a)
        print(f"Real part : {realpart:.2f}")
        print(f'Imag part : {imagpart:.2f}')
# Output:
# enter 1st value where a!=0: 3
# enter 2nd value : 10
# enter 3rd value : 3
# Real  and  distinct
# Root 1 :-0.33
# Root 2 :-3.00

'''
Write  a  program   to  determine  a  point (x , y)  lies  inside , outside  or  on  the  circle.
Center  is  origin  and  radius  is  'r'

1) What  is  the  distance  between  origin  and  point (x , y) ?  --->  sqrt(x ^ 2 + y ^ 2)

2) Where  is  the  point  if  distance >  raidus ?  --->  Outside  the  circle

3) Where  is  the  point  if  distance < raidus ?  --->  Inside  the  circle

4) Where  is  the  point  if  distance  and  raidus   are  same ?  ---> On  the  circle
'''
import math

a = eval(input("Enter the value of x : "))
b = eval(input("Enter the value of y : "))
c = eval(input("Enter radius of circle : "))
d = math.sqrt((a**2)+(b**2))
if d>c:
        print("Outside the circle")
elif d <c:
        print("Inside the Circle")
else:
        print("On the Circle")
# output:
# Enter the value of x : 2
# Enter the value of y : 3
# Enter radius of circle : 4
# Inside the Circle

# Find  outputs  (Home  work)
m = 4
match  m:
	case  1:
		print('One')
	case  2:
		print('Two')
	case  3:
		print('Three')
print('Bye')
# Bye

# Identify  Error
i = 2
match  i:
	case  1:
		print('One')
	case  _:
		print('None of   the  above')
	case  2:
		print('Two')
print('Bye')
#case _ : must come after all the cases

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
# error we cant use multiple case _ :

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
# Hyd
# Bye

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
# Book
# Bye

'''
1) What  are  the  outputs  if  input  is  -6 ? ---> Hyd<nextline> Sec<nextline> Cyb<nextline> Bye
2) What  are  the  outputs  if  input  is  15  ?  ---> One<nextline> Two <nextline>Three<nextline> Bye
3) What  are  the  outputs  if  input  is  10.8  ?  ---> India<nextline> China<nextline> Usa<nextline> Bye
4) What  are  the  outputs  if  input  is  0  ?  --->Hyd<nextline> Sec <nextline>Cyb<nextline> Bye
5) What  are  the  outputs  if  input  is  -10  ?  ---> One<nextline> Two<nextline> Three<nextline> Bye
6) What  are  the  outputs  if  input  is  7  ?  --->Hyd <nextline>Sec<nextline> Cyb<nextline> Bye
'''
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
What  is  '|'  operator  called ?  --->  Bitwise  or  operator
'''


'''  (Home  work)
Write  a   program  to  print  day  of  the  week
1  - Monday
2  - Tuesday
3  - Wednesday
....
7 - Sunday
8 - Invalid

Hint:  Use  match ... case
'''
a = eval(input("Enter digit (1-7) : "))
match a:
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
        case 8:
                print("invalid")
        case _:
                print("Please enter (1-7) Only")
# Output:
# Enter digit (1-7) : 2
# Tuesday

'''  (Home  work)
Write  a   program  to  print  day  of  the  week
1  - Monday
2  - Tuesday
3  - Wednesday
....
7 - Sunday
8 - Invalid

Hint:  Use  match ... case
'''
a = eval(input("Enter digit (1-10) : "))
match a:
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
                print("Not a digit")
        case _:
                print("please enter between 1-10")
# Output:
# Enter digit (1-10) : 2
# Two

#  Find  outputs
while  True:
	print('Hello')
print('Bye')
# Infinite Hello

#  Find  outputs
while  False:
	print('Hello')
print('Bye')
# Bye

'''
Write  a  program  to  print  fibonacci  series  upto   x

Let  input  be   10
What  are  the  outputs  ?  ---> 0 , 1 , 1 , 2 , 3 , 5 , 8

1) What  is  10th  term ?  --->  9th  term + 8th  term
    What  is  3rd  term ?  --->  2nd  term + 1st  term
    What  is  ith  term ?  --->  (i - 1)th  term +  (i - 2)  term

2) What  are  the  first  two  terms ?  --->  0  and  1

3) Hint:  Use  while  loop
'''
x= int(input("Enter the Limit : "))
a,b =0,1
print("Fibonacci series")
while a<=x:
        print(a)
        a,b=b,a+b
# output:
# Enter the Limit : 10
# Fibonacci series
# 0
# 1
# 1
# 2
# 3
# 5
# 8
