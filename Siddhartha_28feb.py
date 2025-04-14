# Identify  error
#else:                        #Error
#		print('else  suite')  #Error
print('Outside')


# Identify  error
if  9 > 5 :          #Error because : missing
	print('Hello')  
print('Bye') 


# Identify  error
if  9 > 12:
	print('Hyd')
else :               #Error because : missing
	print('Sec')


# Identify  error
if  (10,20,15): 
	print('Hyd')  
else:
	print('Sec')    #indented missing 
	

# Identify  error
if  ():
			print('Hyd')
else:                       #Error indented missing
					print('Sec')
print('Bye')

if  { }:
# {               #Error
	print('One')
	print('Two')
	print('Three')
# }              #Error
else:
# {
	print('Four')
	print('Five')
	print('Six')
# }            #Error
print('Bye')



# Identify  error
if  ():
	print('One')
	print('Two')
	print('Three')
else:
# if  []:       #Error
	print('Four')
	print('Five')
	print('Six')
# else:          #Error
if  {}:
	print('Seven')
	print('Eight')
	print('Nine')
else:
	print('Hyd')
	print('Sec')
	print('Cyb')
print('Bye')



num = int(input("Enter a number: "))
if num %2 == 0 :
	print("Even")
else:
	print("Odd")


# Find outputs  (Home  work)
if():
        print('Hyd')
        print('Sec')
        print('Cyb')
else:
        print('One')    #one
        print('Two')    #two
        print('Three')  #Three
print('Bye')            #Bye


# Find  outputs  (Home  work)
if{10 : 20 , 30 : 40}:
        print('Hyd')
        print('Sec')
        print('Cyb')
print('Bye')


# Find  outputs  (Home  work)
if{10 : 20 , 30 : 40}:
        print('Hyd')  #Hyd
        print('Sec')  #Sec
        print('Cyb')  #Cyb
print('Bye')          #Bye


# Find outputs  (Home  work)
if { }:
	print('Hyd')
	print('Sec')
	print('Cyb')
print('Bye')     #Bye


try:
    month = float(input("Enter month number: "))
    if month == 1:
        print("Jan")
    elif month == 2:
        print("Feb")
    elif month == 3:
        print("March")
    elif month == 4:
        print("April")
    elif month == 5:
        print("May")
    elif month == 6:
        print("Jun")
    elif month == 7:
        print("Jul")
    elif month == 8:
        print("Aug")
    elif month == 9:
        print("Sept")
    elif month == 10:
        print("Oct")
    elif month == 11:
        print("Nov")
    elif month == 12:
        print("Dec")
    elif month < 1 or month > 12:
        print("Input should be 1 to 12")
except:
		print("invalid month")
    


num = float(input("Enter 4 digits year: "))
if (num % 4 == 0 and num % 100 != 0) or num % 400 == 0:
    print("Leap year")
else:
	print("Not a Leap year")



num1 = int(input("Enter 4 digits num1: "))
num2 = int(input("Enter 4 digits num2: "))
num3 = int(input("Enter 4 digits num3: "))
if num1 > num2 and num1 > num3:
    print("Largest number:", num1)
elif num2 > num1 and num2 > num3:
    print("Largest number:", num2)
else:
    print("Largest number:", num3)


a = float(input("Enter first input: "))
b = float(input("Enter second input: "))
c = float(input("Enter third input: "))
max = a
if b > max:
    max = b
if c > max:
    max = c

min = a
if b < min:
    min = b
if c < min:
    min = c

mid = (a + b + c) - (max + min)
print(f'Largest number: {max}')
print(f'Smallest number: {min}')
print(f'Middle number: {mid}')



# Find  outputs  (Home  work)
m = 4
match  m:
	case  1:
		print('One')
	case  2:
		print('Two')
	case  3:
		print('Three')
print('Bye')    #Bye



# Identify  Error
i = 2
match  i:
	case  1:
		print('One')
	#case  _:
	#	print('None of   the  above')  #Error
	case  2:
		print('Two')
print('Bye')



# Find  outputs  (Home  work)
m = 2
match  m:
	case  1:
		print('One')
# 	case  _:
# 		print('Hello')
# 	case  _:
# 		print('Bye')
print('End')


#  Find  outputs  (Home  work)
m = 1
match  m:
	case  1:
		print('Hyd') #Hyd
	case  1:
		print('Sec')
	case  1:
		print('Cyb')
print('Bye')         #Bye


# Find  outputs  (Home  work)
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
print('Bye')          #Bye

'''
1) What  are  the  outputs  if  input  is  -6 ? ---> Hyd, Sec,Cyb, Bye
2) What  are  the  outputs  if  input  is  15  ?  --->One ,Two ,Three
3) What  are  the  outputs  if  input  is  10.8  ?  --->India, China, Usa
4) What  are  the  outputs  if  input  is  0  ?  --->Hyd, Sec,Cyb, Bye
5) What  are  the  outputs  if  input  is  -10  ?  --->One ,Two ,Three
6) What  are  the  outputs  if  input  is  7  ?  --->Hyd, Sec,Cyb, Bye
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
	#case  _:
	    #print('Not  a  point')

	'''
   1) What  is  the  output  when  input  is  (-10 , -20) ?  --->Quadrant
   2) What  is  the  output  when  input  is  (10 , 0) ?  --->x - axis
   3) What  is  the  output  when  input  is  (0 , -20) ?  --->y - axis
   4) What  is  the  output  when  input  is  (0 , 0) ?  --->Origin
   5) What  is  the  output  when  input  is  (10 , 20 , 30) ?  --->Not  a  point
   6) What  is  the  output  when  input  is  [10 , 20]  ?  --->Quadrant
   7) What  is  the  output  when  input  is  [0 , -25]  ?  --->y - axis
   8) What  is  the  output  when  input  is  ()  ?  --->Not  a  point
   9) What  is  the  output  when  input  is  {10 , 20} ?  --->Quadrant
  10) What  is  the  output  when  input  is  (25,) ?  --->Not  a  point
'''

try:
    
   day = int(input("Enter your day: "))
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
            print("invalid day")
except:
    print("Enter only integer numbers")
        
    
try:
    
   num = int(input("Enter your num: "))
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
        case _:
            print("Not a digit")
except:
    print("Enter only integer numbers")

try:
    x = int(input("Enter value of x: "))
    a = 0
    b = 1
    if x == 0:
        print(x)
    else:
        print(a)
        print(b)
    c = a+b
    while(c <= x):
        print(c)
        a,b = b,c
        c = a+b
except:
    print("Enter integers only")

    
#  Find  outputs
while  True:
	print('Hello')  #infinity time
print('Bye')


while  False:
	print('Hello')  
print('Bye')       #Bye


x=int(input("Enter 1 to celsius to farenheit and 2 for Fareheit  to celsius: "))
try:
    if x==1:
        y=int(input("Enter Celsius temperature : "))
        fah=1.8*y+32
        print("Farenheit Equivalent :",fah)
    elif x==2:
        y=int(input("Enter Farenheit temperature : "))
        cel=(y-32)/1.8
        print(f"Celsius Equivalent :{cel:.2f}")
    else:
        print("Enter a number 1 or 2")
except:
    print("Input should be integer")


import math 
x=int(input("enter value of x : "))
y=int(input("enter value of y : "))
z=int(input("enter  radius of circle : "))
 
distance=math.sqrt(x**2 + y**2)
if distance>z:
    print("point outside the circle")
elif distance==z:
    print("point on the circle")
else:
    print("point inside the circle")


x=float(input("enter value of x-coordinate : "))
y=float(input("enter value of y-coordinate  : "))
if x>0 and y>0:
    print("1st quadrant")
elif x<0 and y>0:
    print(" 2nd quadrant")
elif x<0 and y<0:
    print("3rd quadrant")
elif x>0 and y<0:
    print("4th quadrant")
elif x==0 and y==0:
    print("Origin")
elif x==0 and y!=0:
    print("On y-axis")
elif x!=0 and y==0:
    print("On x-axis")


from math import sqrt 
x=int(input("enter value of x : "))
y=int(input("enter value of y : "))
z=int(input("enter value of z: "))
# conditions
if x!=0:
    dis=y**2-4*x*z
    if dis>0:
        root1=(-y+sqrt(dis))/(2*x)
        root2=(-y-sqrt(dis))/(2*x)
        print("Roots are Real and Distinct")
        print(f"Root1: {root1:.2f}")
        print(f"Root2: {root2:.2f}")
    elif dis==0:
        root1=-y/(2*x)
        root2=-y/(2*x)
        print("Roots are Real and Equal")
        print(f"Root1: {root1:.2f}")
        print(f"Root2: {root2:.2f}")
    else:
        real=-y/(2*x)
        imaginary=sqrt(abs(dis))/(2*x)

        print("Roots are Imaginary or complex")
        print(f"Root1: {real}+{imaginary}")
        print(f"Root2: {real}-{imaginary}")

else:
    print("Value of 'x' can not be 0 ")


import math
x=int(input("enter 1st side : "))
y=int(input("enter 2nd side : "))
z=int(input("enter  3rd side  : "))
#sum of two sides
X=x+y
Y=y+z
Z=z+x
# conditions
if X>z and Y>x and Z>y:
    #equilateral triangle condition
    if x==y==z :
        print("Equilateral Triangle")
        area=math.sqrt(3)/4*x**2
        print(f"Area of Equilateral triangle : {area:.2f}")
    # Isoscles triangle condition
    elif x==y or y==z or z==x: 
        print("Isoscles Triangle")
        perimeter=x+y+z
        print(f"Perimeter of Isosceles triangle : {perimeter}")
    # Scalene triangle condition
    else:
        print("Scalene Triangle")
        s=(x+y+z)/2
        area=math.sqrt(s*(s-x)*(s-y)*(s-z))
        perimeter=x+y+z
        print(f"Area of Scalene triangle : {area:.2f}")
        print(f"Perimeter  of Scalene triangle : {perimeter}")                
else:
    print("Not a Triangle")


        
    


			
	
		





    



