# Identify  error
'''else: # Error becoz no if condition to else
		print('else  suite')
print('Outside') '''
# Identify  error
#if  9 > 5 # Error becoz of no : after the if condition
	#print('Hello')
#print('Bye')
# Identify  error
if  9 > 12:
	print('Hyd')
#else # Error becoz of no : after else conditon
	print('Sec')
# Identify  error
if  (10,20,15):
#print('Hyd') # Indentation Error becoz after if condition no space or tab 
#else:
#print('Sec') ## Indentation Error becoz after if condition no space or tab 
# Identify  error
#if  ():
			print('Hyd')
	#else:  # if and else condition should be indented and same for print stmnts inside condition
					#print('Sec')
print('Bye')
# Identify  error
'''if  { }: # Error becoz of print stmnt are in suite
{
	print('One')
	print('Two')
	print('Three')
}
else:  # Error becoz of print stmnt are in suite
{
	print('Four')
	print('Five')
	print('Six')
}
print('Bye')'''
# Identify  error
if  ():
	print('One')
	print('Two')
	print('Three')
else:
#if  []: # Error becoz of if condition should be after inside else Indentation Error
	print('Four')
	print('Five')
	print('Six')
#else:  # Error becoz of if condition should be after inside else Indentation Error
if  {}:
	print('Seven')
	print('Eight')
	print('Nine')
else:
	print('Hyd') # Hyd
	print('Sec') # Sec
	print('Cyb') # Cyb
print('Bye') #Bye
# Write  a  program  to  determine  a  number  is  even  or  odd  with   if  statement
n = int(input('Enter a Integer No:'))
if n%2==0:
		print('Even',n)
else:
		print('Odd',n)	
# Find outputs  (Home  work)
if():
        print('Hyd') 
        print('Sec')
        print('Cyb')
else:
        print('One') # One
        print('Two') # Two
        print('Three') # Three
print('Bye') # Bye
# Find  outputs  (Home  work)
if{10 : 20 , 30 : 40}:
        print('Hyd') # Hyd
        print('Sec') # Sec
        print('Cyb') # Cyb
print('Bye') # Bye
# Find outputs  (Home  work)
if { }:
	print('Hyd')
	print('Sec')
	print('Cyb')
print('Bye') # Bye
# Write   a  program  to  print  month  name  for  input  month  number  by  using  if  and  elif  (Home  work)
try:
	n = int(input('Enter month number (1 - 12)')) # 7
	if n==1:
		print('January')
	elif n==2:
		print('February')
	elif n==3:
		print('March')
	elif n==4:
		print('april')
	elif n==5:
		print('May')
	elif n==6:
		print('June')
	elif n==7:
		print('July')
	elif n==8:
		print('August')
	elif n==9:
		print('September')
	elif n==10:
		print('October')
	elif n==11:
		print('November')
	elif n==12:
		print('December')											
	else:
		print('Input Should be b/w 1 and 12')
except:
	print('Input should be Integer:')

#Enter month number (1 - 12): 13
#Input  should  be  between  1  and   12
#Enter month number (1 - 12): 10.8
#Input  should  be  an  integer

'''Write  a  program  to  test  year  is  leap  year  or  not

1) What  is  leap  year ?  --->  Divisible  by  4  but  not  by  100   (or)  divisble  by  400

2) Are  2016 , 2020 , 2024  leap  years ? --->  Yes  becoz  leap  year  for  every  4  yearrs

3) Are  1700 , 1800 , 1900  leap  years ? --->  No  becoz  no  leap  year  for  every  100  years

4) Are  1600 , 2000 , 2400  leap  years ?  --->  Yes  becoz  leap  year  for  every  400  years

5) Hint:  3  conditions'''

x = int(input('Enter  4-digit  year :')) #  2024
if(x%4==0 & x%100!=0):
	print('Leap Year:',x)
elif(x%400==0):
	print('Leap Year:',x)	
else:
	print('Not Leap Year:',x)	


#Write  a  program  to  determine  largest  of  three  numbers  with  if  and  else

#Hint:  Write  multiple  conditions

x=int(input('Enter 1st input : ')) #10
y=int(input('Enter 2nd input : ')) #20
z=int(input('Enter 3rd input : ')) #15
if x>y and x>z:
    print('x is greater: ',x)
if y>x and y>z:
    print('y is greater: ',y)
else:
    print('z is greater: ',z)	

'''Write  a  program  to  convert  celsius  temperature  to  farenheit  and  vice-versa

1) What  is  the  formula  to  convert  celsius  to  farenheit ? --->  1.8 * temp + 32

2) What  is  the  formula  to  convert  farenheit  to  celsius ?  --->  (temp - 32) / 1.8'''

x=int(input('Enter  1  to  convert  celsius  to  farenheit  and  2  to  convert  fahrenheit  to  celsius : '))
if x==1:
    temp = float(input('Enter the temperature in Celsius: '))
    f = 1.8 * temp + 32
    print(F'Fahrenheit : {f : .2f}')
elif x==2:
    temp = float(input('Enter the temperature in Fahrenheit: '))    
    c = (temp-32) / 1.8
    print(F'Celsius : {c : .2f}')
else:
    print('Enter 1 or 2 only: ') 

'''Write  a  program  to  test  a  point  (x , y)  lies  in  1st  quadrant , 2nd  quadrant , 3rd  quadrant ,
4th  quadrant , x - axis , y - axis   or  origin

1) What  are  the  values  of  x  and  y  in  1st  quadrant ?  --->  Both  are  +ve

2) What  are  the  values  of  x  and  y  in  2nd  quadrant ?  --->  'x'  is  -ve  and  'y'  is  +ve

3) What  are  the  values  of  x  and  y  in  3rd  quadrant ?  ---> Both   are  -ve

4) What  are  the  values  of  x  and  y  in  4th  quadrant ?  --->  'x'  is   +ve  and  'y'  is  -ve

5) What  are  the  values  of  x  and  y  on  x - axis ?  ---> 'x'  is  non-zero  and  'y'  is  0

6) What  are  the  values  of  x  and  y  on  y - axis ?  --->  'x'  is  0  and  'y'  is  non-zero

7) What  are  the  values  of  x  …
'''
x=int(input("Enter  value  of  x  co-ordinate : "))
y=int(input("Enter  value  of  y  co-ordinate : "))
if x>0 and y>0:
	print("1st  quadrant ")
elif x<0 and y>0:
    print("2dn  quadrant ")
elif x<0 and y<0:
    print("3rd  quadrant ")
elif x>0 and y<0:
    print("4th  quadrant ")
elif (x<0 or x>0) and y==0:
    print("x - axis ")
elif x==0 and (y<0 or y>0):
    print("y - axis ")
else :
    print("origin")
'''
Write  a  program  to  determine  largest , smallest  and  middle  of  three  numbers

a = 10
b = 20
c = 7
max = 20
min =  7
mid =  (10 + 20 + 7) - (20 + 7) = 37 - 27 = 10

1) What  is  the  initial  value  of  max  ?  --->  a

2) Whichever  input >  max,  copy  that  input  to  max

3) What  is  the  initial  value  of  min  ?  --->  'a'

4) Whichever  input  <  min,  copy  that  input  to  min

5) How  to  obtain  middle  number ?  --->   Eliminate  max  and  min  from  a , b , c
'''
a=int(input("Enter 1st input:"))
b=int(input("Enter 2nd input:"))
c=int(input("Enter 3rd input:"))
if a>b>c:
    max=a
    print("max=",a)
elif b>a>c:
    max=b
    print('max=',b)
else:
    max=c
    print('max=',c)
if a<b<c:
    min=a
    print('min=',a)
elif b<a<c:
    min = b
    print("min=",b)
else:
    min = c
    print("main=",c)

print(f'mid ={(a+b+c)-(min+max)}')
'''
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
	What  is  the  value  of  's'  ?  --->  	(a…
Enter  1st  side : 3
Enter  2nd  side : 4
Enter  3rd  side : 5
Scalene  triangle
Area : 6.00
Perimeter : 12.0
Enter  1st  side : 7
Enter  2nd  side : 8
Enter  3rd  side : 7
Isoscles  triangle
Perimeter : 22.0
Enter  1st  side : 7
Enter  2nd  side : 7
Enter  3rd  side : 7
Equilateral  triangle
Area : 21.22
Enter  1st  side : 3
Enter  2nd  side : 4
Enter  3rd  side : 8
Not  a  triangle
'''
try:
    import math

    a = int(input("Enter 1st side:"))
    b = int(input("Enter 2nd side:"))
    c = int(input("Enter 3rd side:"))
    if (a + b > c) and (b + c > a) and (a + c > b):
        if a == b == c:
            print("equilateral  triangle")
            print(f'area={math.sqrt(3 / 4) * a ** 2}')
            print(f'perimeter={a + b + c}')
        elif a == b or b == c or c == a:
            print("isoscles  triangle ")
            print(f'perimeter={a + b + c}')
        elif a != b or b != c or c != a:
            print("scalene  triangle")
            s = (a + b + c) / 2
            k = s * (s - a) * (s - b) * (s - c)
            y = math.sqrt(k)
            print(f'area={y:.2f}')
            print(f'perimeter={a + b + c}')
    else:
        print("not a triangle, sum of every two sides should be > 3rd side")
except:
    print("inputs should be an integer")
    
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
	 What  is  roo…
Enter  value  of  a : 5
Enter  value  of  b : 6
Enter  value  of  c : 5
Roots  are  imaginary  (or) complex
Root 1 : -0.6 +  0.8j
Root 2 : -0.6 -  0.8j
Enter  value  of  a : 3
Enter  value  of  b : 10
Enter  value  of  c : 3
Roots  are  real  and  distinct
Root 1 : -0.33
Root 2 : -3.00
Enter  value  of  a : 5
Enter  value  of  b : 10
Enter  value  of  c : 5
Roots are real and equal
Root 1 : -1.0
Root 2 : -1.0
Enter  value  of  a : 0
Value  of  a  can  not  be  0
'''

import math
a=int(input("Enter value of a:"))
b=int(input("Enter value of b:"))
c=int(input("Enter value of c:"))
disc=b**2-4*a*c
if a==0:
    print("Value  of  a  can  not  be  0")


else :
    if disc==0:
        print("Roots are real and equal")
        print(f'Root1 = {-b/(2*a)}')
        print(f'Root2 = {-b/(2*a)}')
    elif disc>0:
        print("Roots  are  real  and  distinct")
        k=(-b + math.sqrt(disc))/(2*a)
        g=(-b - math.sqrt(disc))/(2*a)
        print((f'Root1 = {k:.2f}'))
        print(f'Root2 = {g:.2f}')
    elif disc<0:
        print("Roots  are  imaginary  (or) complex")
        real=-b/(2*a)
        imag=math.sqrt(-disc)/(2*a)
        k=(f'{imag}j')
        print(f'Root1 = {real}+ {k}j')
        print(f'Root1 = {real}-{k}j')





'''
Write  a  program  to  determine  bill  amount  and  input  is  units

Units                                                      Cost
------------------------------------------------------------
First  100  units								Rs. 3.00 / unit

Next  100  units								Rs. 3.50 / unit

Next  200  units								Rs. 4.00 / unit

Next  300  units								Rs. 4.50 / unit

Above  700  units								Rs. 5.00 / unit
---------------------------------------------------------------
Let  units  be  1200
What  is  the  bill  amount ? --->  100 * 3.00 + 100 * 3.50 + 200 * 4.00 + 300 * 4.50 +  500 * 5.00

Hint:  Use  match  ...  case   but  not  if ... else'''

units = int(input('Enter  units :   '))

match  int(units/100):
	case 0:
		cost =units*3
	case 1:
	    cost =100*3 + (units-100)*3.5
	case 2 | 3:
		cost =100*3 + 100*3.5 + (units-200)*4
	case  4 | 5 | 6:
		cost =100*3 + 100*3.5 + 200*4 + (units-400)*4.5
	case _:
		cost=100*3 + 100*3.5 + 200*4 + 300*4.5 + (units-700)*5
print('Bill  amount  :  ',cost)
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

x = int(input("Enter a Number : "))
a = 0
b = 1
c = a + b
if x == a:
    print(a)
elif x == b:
    print("Fibonacci series :", a, b, sep="\n")
else:
    print("Fibonacci series :", a, b, sep="\n")
    while c < x:
        print(c)
        a = b
        b = c
        c = a + b

#  Find  outputs
while  True:
	print('Hello') # Hello
print('Bye') # Bye
#  Find  outputs
while  False: 
	print('Hello')
print('Bye') # Bye
