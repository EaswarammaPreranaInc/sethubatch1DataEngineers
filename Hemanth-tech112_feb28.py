# Identify  error
'''
else:      # Error because if is missing
    print('else  suite')
print('Outside')'''



# Identify  error
'''
if  9 > 5   # Error because : is missing
	print('Hello')
print('Bye')      '''



# Identify  error
'''
if  9 > 12:
	print('Hyd')
else   # Error because : is missing
	print('Sec')    '''



# Identify  error
'''
if  (10,20,15):
print('Hyd')  # Error because spacebar or tab key is missing at the beginning of the statement
else:
print('Sec')  # Error because spacebar or tab key is missing at the beginning of the statement
'''



# Identify  error
'''
if  ():  
			print('Hyd')
	else:  # Error because else is not indented with if
					print('Sec')
print('Bye')
'''




# Identify  error
'''
if  { }:
{   # Error due to {
	print('One')
	print('Two')
	print('Three')
}  # Error due to }
else:
{  # Error due to {
	print('Four')
	print('Five')
	print('Six')
}  # Error due to }
print('Bye')
'''


# Identify  error
'''
if  ():
	print('One')
	print('Two')
	print('Three')
else:
if  []:  # Error because spaces are missing before the statement
	print('Four')
	print('Five')
	print('Six')
else:
if  {}:  # Error because spaces are missing before the statement
	print('Seven')
	print('Eight')
	print('Nine')
else:
	print('Hyd')
	print('Sec')
	print('Cyb')
print('Bye')
'''



# Write  a  program  to  determine  a  number  is  even  or  odd  with   if  statement
try:
	x=eval(input('Enter integer : '))  # reads string input and converts to integer object
	if (x%2==0):   # 12%2==0
		print(f'{x} is a Even number')  # prints statement
	else:  # 11%2!=0
		print(f'{x} is a Odd number')  # prints the statement
except:
	print('Input should be Integer')



# Find outputs  (Home  work)
if():  # False due to empty tuple
        print('Hyd')
        print('Sec')
        print('Cyb')
else:  
        print('One') # One
        print('Two') # Two
        print('Three') # Three
print('Bye') # Bye




# Find  outputs  (Home  work)
if{10 : 20 , 30 : 40}: # True due to non-empty dictionary 
        print('Hyd')  # Hyd
        print('Sec')  # Sec
        print('Cyb')  # Cyb
print('Bye')  # Bye



# Find outputs  (Home  work)
if { }:  # False due to empty dictionary
	print('Hyd')
	print('Sec')
	print('Cyb')
print('Bye')  # Bye



# Write a program to print month name for input month number by using if and elif(Homework)
try:
	x = eval(input('Enter month number(1-12) : '))
	if x == 1:
		print('January')
	elif x == 2:
		print('February')
	elif x == 3:
		print('March')
	elif x == 4:
		print('April')
	elif x == 5:
		print('May')
	elif x == 6:
		print('June')
	elif x == 7:
		print('July')
	elif x == 8:
		print('August')
	elif x == 9:
		print('September')
	elif x == 10:
		print('October')
	elif x == 11:
		print('November')
	elif x == 12:
		print('December')
	else:
		print('Input should be between 1 and 12.')
except:
	print('Input should be an integer.')


# Sample outputs
#Enter month number (1 - 12):7
#july

#Enter month number (1 - 12): 13
#Input  should  be  between  1  and   12

#Enter month number (1 - 12): 10.8
#Input  should  be  an  integer 



# Write  a  program  to  test  year  is  leap  year  or  not
try:
	a=int(input('Enter four digits year : '))
	if a%4==0 and a%100!=0 or a%400==0:
		print('Leap year')
	else:
		print('Not a leap year')
except:
	print('Input should be an integer')


# Sample outputs
#Enter  4-digit  year :  2024
#Leap year
#Enter  4-digit  year :  1900
#Not a leap year



# Write  a  program  to  determine  largest  of  three  numbers  with  if  and  else
try:
	a=eval(input('Enter 1st input : '))  # reads string input and converts to int object
	b=eval(input('Enter 2nd input : '))  # reads string input and converts to int object
	c=eval(input('Enter 3rd input : '))  # reads string input and converts to int object
	if a>b and a>c:
		print(f'Largest number : {a}')
	elif b>a and b>c:
		print(f'Largest number : {b}')
	else:
		print(f'Largest number : {c}')
except NameError:
	print('Input string should be in quotes')
except TypeError:
	print('Input can not be a complex number')

# Sample Outputs
#Enter 1st input : 10
#Enter 2nd input : 20
#Enter 3rd input : 15
#Laregst  number  :   20



# Write  a  program  to  convert  celsius  temperature  to  farenheit  and  vice-versa
try:
	t=int(input('Enter  1  to  convert  celsius  to  farenheit  and  2  to  convert  fahrenheit  to  celsius : '))
	if t==1:
		c=float(input('Enter celsius temperature : '))
		c_to_f=1.8*c+32
		print(f'Fahrenheit Equivalent : {c_to_f:.2f}')
	elif t==2:
		f=float(input('Enter Fahrenheit temperature : '))
		f_to_c=(f-32)/1.8
		print(f'Celsius Equivalent : {f_to_c:.2f}')
	else:
		print('Invaild input')
except:
	print('Input should be int or float')

# Sample Outputs
#Enter  1  to  convert  celsius  to  farenheit  and  2  to  convert  fahrenheit  to  celsius :  2
#Enter  fahrenheit  temperature : 100
#celsius   equivalent :  37.78

#Enter  1  to  convert  celsius  to  farenheit  and  2  to  convert  fahrenheit  to  celsius :  1
#Enter  celsius  temperature :  30
#Fahrenheit  Equivalent  :  86.0

#Enter  1  to  convert  celsius  to  farenheit  and  2  to  convert  fahrenheit  to  celsius :  3
#Invalid input



# Write a program to test point(x,y)lies in 1st quadrant,2nd quadrant,3rd quadrant,4th quadrant,x-axis,y-axis or origin
try:
	x=float(input('Enter value of x co-ordinate : '))
	y=float(input('Enter value of y co-ordinate : '))
	if x>0 and y>0:
		print('1st Quadrant')
	elif x<0 and y>0:
		print('2nd quadrant')
	elif x<0 and y<0:
		print('3rd quadrant')
	elif x>0 and y<0:
		print('4th quadrant')
	elif x!=0 and y==0:
		print('x-axis')
	elif x==0 and y!=0:
		print('y-axis')
	else:
		print('Origin')
except:
	print('Input should be a number')

# Sample Output
#Enter  value  of  x  co-ordinate :  -10
#Enter  value  of  y  co-ordinate : 20
#2nd quadrant



# Write  a  program  to  determine  largest , smallest  and  middle  of  three  numbers
a=eval(input('Enter first input : '))
b=eval(input('Enter second input : '))
c=eval(input('Enter third input : '))
max=a
if b>max:
	max=b
	print('Largest number : ',max)
else:
	max=c
	print('Largest number : ',max)
min=a
if b<min:
	min=b
	print('Smallest number : ',min)
else:
	min=c
	print('Smallest number : ',min)
mid= (a+b+c)-(max+min)
print(f'Middle number : {mid}')

# Sample inputs
#Enter  first  input   :  10
#Enter  second   input   :  20
#Enter  third  input   :  7
#Largest number :  20.0
#Smallest number :  7.0
#Middle number :  10.0



# Write a program to determine three sides form a triangle or not
import math
a=float(input('Enter first side : '))
b=float(input('Enter second side : '))
c=float(input('Enter third side : '))
if a+b>c and b+c>a and a+c>b:
    if a==b==c:
        print('Equilateral triangle')
        print(f'Area : {math.sqrt(3)/4*a**2:.2f}')
    elif a==b or b==c or a==c:
        print('Isoceles triangle')
        print('Perimeter : ', a+b+c)
    else:
        print('Scalene triangle')
        s=(a+b+c)/2
        print(f'Area : {math.sqrt(s * (s-a) * (s-b) * (s-c))}')
        print('Perimeter : ', a + b + c)
else:
    print('Not a triangle')
  
# Sample Outputs
#Enter  1st  side : 3
#Enter  2nd  side : 4
#Enter  3rd  side : 5
#Scalene  triangle
#Area : 6.00
#Perimeter : 12.0

#Enter  1st  side : 7
#Enter  2nd  side : 8
#Enter  3rd  side : 7
#Isoscles  triangle
#Perimeter : 22.0

#Enter  1st  side : 7
#Enter  2nd  side : 7
#Enter  3rd  side : 7
#Equilateral  triangle
#Area : 21.22

#Enter  1st  side : 3
#Enter  2nd  side : 4
#Enter  3rd  side : 8
#Not  a  triangle



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

# Sample Outputs
#Enter  value  of  a : 5
#Enter  value  of  b : 6
#Enter  value  of  c : 5
#Roots  are  imaginary  (or) complex
#Root 1 : -0.6 +  0.8j
#Root 2 : -0.6 -  0.8j

#Enter  value  of  a : 3
#Enter  value  of  b : 10
#Enter  value  of  c : 3
#Roots  are  real  and  distinct
#Root 1 : -0.33
#Root 2 : -3.00

#Enter  value  of  a : 5
#Enter  value  of  b : 10
#Enter  value  of  c : 5
#Roots are real and equal
#Root 1 : -1.0
#Root 2 : -1.0

#Enter  value  of  a : 0
#Value  of  a  can  not  be  0



# Write a program to determine a point(x, y)lies inside,outside or on the circle.Center is origin and radius is 'r'
import math
x=float(input('Enter value of x : '))  # 3
y=float(input('Enter value of y : '))  # 5
r=float(input('Enter radius of circle : '))  # 5
d=math.sqrt(x**2+y**2)  #  5 is distance between origin and point(x,y)
if d>r:
	print('Outside the circle')
elif d<r:
	print('Inside the circle')
else:
	print('On the circle')
  
# Sample Outputs

#Enter  value  of  x : 3
#Enter  value  of  y : 4
#Enter radius of circle : 5
#Point is on the circle



# Find  outputs  (Home  work)
m = 4 
match  m:  
	case  1:
		print('One')
	case  2:
		print('Two')
	case  3:
		print('Three')
print('Bye')  # Bye


# Identify  Error
'''i = 2
match  i:
	case  1:
		print('One')
	case  _:    # Error because it is in middle of the match
		print('None of   the  above')
	case  2:
		print('Two')
print('Bye') '''


# Find  outputs  (Home  work)
'''m = 2
match  m:
	case  1:
		print('One')
	case  _:    # Error because it is in middle of match
		print('Hello')
	case  _:  # valid
		print('Bye')
print('End')'''


#  Find  outputs  (Home  work)
m = 1
match  m:  
	case  1:
		print('Hyd')  # Hyd
	case  1:
		print('Sec')
	case  1:
		print('Cyb')
print('Bye')  # Bye


# Find  outputs  (Home  work)
ch = 'B'
match  ch:  
	case   'A':
		print('Apple')
	case  'B':
		print('Book')  # Book
	case  'C':
		print('Cafe')
	case  _:
		print('None of  the  above')
print('Bye')  # Bye



# Write  a   program  to  print  day  of  the  week

try:
	w=eval(input('Enter the number from (1-7) : '))
	match w:
			case 1 :
					print('Monday')
			case 2 :
					print('Tuesday')
			case 3 :
					print('Wednesday')
			case 4 :
					print('Thrusday')
			case 5 :
					print('Friday')
			case 6 :
					print('Saturday')
			case 7 :
					print('Sunday')
			case _:
					print('Invalid input')
	print('Bye')
except:
	print('Enter valid input')



# Write  a   program  to  print  day  of  the  week

try:
	w=eval(input('Enter the number from (1-7) : '))
	match w:
			case 1 :
					print('Monday')
			case 2 :
					print('Tuesday')
			case 3 :
					print('Wednesday')
			case 4 :
					print('Thrusday')
			case 5 :
					print('Friday')
			case 6 :
					print('Saturday')
			case 7 :
					print('Sunday')
			case _:
					print('Invalid input')
	print('Bye')
except:
	print('Enter valid input')



# Write  a   program  to  print  day  of  the  week

try:
	w=eval(input('Enter the number from (1-7) : '))
	match w:
			case 1 :
					print('Monday')
			case 2 :
					print('Tuesday')
			case 3 :
					print('Wednesday')
			case 4 :
					print('Thrusday')
			case 5 :
					print('Friday')
			case 6 :
					print('Saturday')
			case 7 :
					print('Sunday')
			case _:
					print('Invalid input')
	print('Bye')
except:
	print('Enter valid input')



# Write  a   program  to  print  day  of  the  week

try:
	w=eval(input('Enter the number from (1-7) : '))
	match w:
			case 1 :
					print('Monday')
			case 2 :
					print('Tuesday')
			case 3 :
					print('Wednesday')
			case 4 :
					print('Thrusday')
			case 5 :
					print('Friday')
			case 6 :
					print('Saturday')
			case 7 :
					print('Sunday')
			case _:
					print('Invalid input')
	print('Bye')
except:
	print('Enter valid input')

# Sample outputs
'''
Enter the number from (1-7) : 7
Sunday
Bye

Enter the number from (1-7) : 8
Invalid input
Bye

Enter the number from (1-7) : hemanth
Enter valid input
'''



# Write a program to print digits in words

try:
	d=eval(input('Enter the number from (1-9) : '))
	match d:
			case 0 :
					print('Zero')
			case 1 :
					print('One')
			case 2 :
					print('Two')
			case 3 :
					print('Three')
			case 4 :
					print('Four')
			case 5 :
					print('Five')
			case 6 :
					print('Six')
			case 7 :
				    print('Seven')
			case 8 :
				    print('Eight')
			case 9 :
				    print('Nine')
			case _:
					print('None of the above')
	print('Bye')
except:
	print('Enter valid input between (0-9)')

# Sample Outputs
'''
Enter the number from (1-9) : 8
Eight
Bye

Enter the number from (1-9) : 10
None of the above
Bye

Enter the number from (1-9) : hemanth
Enter valid input between (0-9)



# Write  a  program  to  print  fibonacci  series  upto   x
x=eval(input('Enter value of x : '))
if x==0:
	print('Fibonacci Series')
	print(0)
else:
		a=0
		b=1
		print('Fibonacci Series')
		print(a)
		print(b)
		c=a+b
		while c<=x:
			print(c)
			a=b
			b=c
			c=a+b
    
# Sample Outputs

#Enter  value  of  x  :  10
#Fibonacci  Series
#0
#1
#1
#2
#3
#5
#8

#Enter  value  of  x  :  1
#Fibonacci  Series
#0
#1
#1

#Enter  value  of  x  :  0
#Fibonacci  series
#0
'''


#  Find  outputs
#while  True:  
#	print('Hello')  # Hello executes infinite times
#print('Bye')  # Not executed due to infinite loop


#  Find  outputs
while  False: # Not executed
	print('Hello')
print('Bye')  # Bye















            

