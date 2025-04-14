'''
# Identify  error
else:
		print('else  suite')
print('Outside')
error due to miising if block in above prgm
#-----------------------------------------------------------------------------
'''
"""
# Identify  error
if  9 > 5# error in these line becoz colon is missing
	print('Hello')
print('Bye')
"""
#----------------------------------------------------------------------------
'''
# Identify  error
if  9 > 12:
	print('Hyd')
else # here colon is missing  
	print('Sec')
'''

'''
# Identify  error
if  (10,20,15):
print('Hyd')
else:
print('Sec')
here indentioin is miising near if and else block
'''


'''
# Identify  error
if  ():
			print('Hyd')
	else:
				print('Sec')
print('Bye')
here indentioin is miising near if

'''


'''
# Identify  error
if  { }:
{ # Here error becoz braces are not allowed in between the if and else block
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
'''

'''
# Identify  error
if  ():
	print('One')
	print('Two')
	print('Three')
else:
if  []: # error here coz indention for else after if block
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
'''
#------------------------------------------------------------------------------
"""
#Even and Odd Numbers 
n= int(input(" Enter a Number :-"))
if n%2==0 :
	print("Even Number")
else :
	print ("odd Number")
"""
#------------------------------------------------------------------------------
"""
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
# prints else becoz if dont has condition
"""
#---------------------------------------------------------------------------------
"""
# Find  outputs  (Home  work)
if{10 : 20 , 30 : 40}:
        print('Hyd')
        print('Sec')
        print('Cyb')
print('Bye')
# Remember if block is printed without else Becoz But only without else 
"""
#------------------------------------------------------------------------------------



"""
# Find outputs  (Home  work)
if { }:
	print('Hyd')
	print('Sec')
	print('Cyb')
print('Bye')
# Here if should have the if condition in else block
"""
#----------------------------------------------------------------------------------------
"""

# Write   a  program  to  print  month  name  for  input  month  number  by  using  if  and  elif  (Home  work)
n=(input("Enter Month Number(1-12) :-"))
try:
	m=eval(n)
	if m==int(m):
	   m=m
	  if m==1:
		print("January")
	  elif m==2:
			print("feb")
		elif m==3:
			print("Mar")
		elif m==4:
			print("apr")
		elif m==5:
			print("may")
		elif m==6:
			print("jun")
		elif m==7:
			print("jul")
		elif m==8:
			print("aug")
		elif m==9:
			print("sep")
		elif m==10:
			print("oct")
		elif m==11:
			print("nov")
		elif m==12:
			print("dec")
		else :
			print("input should be between 1 and 12")
	else :
		print("input should be only integer")
except :
	print("invalid input")

"""
#-----------------------------------------------------------------------------------------
"""
#Leaf Year program 
l=int(input("Enter leap year :-"))
if (l%4==0)and(l%100!=0)|(l%400==0):
	print("It is a Leaf Year")
else:
	print("it is not a leaf year")
"""
#-----------------------------------------------------------------------------------------
"""
#Write  a  program  to  determine  largest  of  three  numbers  with  if  and  else
#Hint:  Write  multiple  conditions
a=int(input("Enter 1st Number :"))
b=int(input("Enter 2nd Number :"))
c=int(input("Enter 3rd Number :"))
if(a>=b):
	if(a>=c):
		print("Largest NUmber",a)
	else:
		print("largest Number",c)
else:
	if(b>=c):
		print("Largest Number",b)
	else:
		print("Largest Number",c)
"""
#---------------------------------------------------------------------------------------

'''
Write  a  program  to  convert  celsius  temperature  to  farenheit  and  vice-versa

1) What  is  the  formula  to  convert  celsius  to  farenheit ? --->  1.8 * temp + 32

2) What  is  the  formula  to  convert  farenheit  to  celsius ?  --->  (temp - 32) / 1.8
'''
"""
n=int(input("enter number 1 or 2 : " ))
if n==1:
	f=int(input("enter cel.temperture :"))
	print("Frah Equivalent : ", 1.8 * f + 32)
elif n==2:
	c=int(input("enter Fah.temperture :"))
	print("cel Equivalent : ", (c-32)/1.8)
else:
	print("Enter Valid input")
"""
#--------------------------------------------------------------------------------------
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
Enter  value  of  x  co-ordinate :  -10
Enter  value  of  y  co-ordinate :  20
2nd quadrant
'''
'''
a=int(input("Enter  value  of  x  co-ordinate : "))
b=int(input("Enter  value  of  y  co-ordinate : "))

if a>0<b :
	print('1st Quadrant')
elif a<0<b:
	print('2nd Quadrant')
elif a<0>b:
	print('3rd Quadrant')
elif a>0>b:
	print('4th Quadrant')
elif a>0==b:
	print('on x-axis')
elif a==0<b:
	print('on y-axis')
else:
	print('Both are zeroes')
'''
#------------------------------------------------------------------------
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


Enter  first  input   :  10
Enter  second   input   :  20
Enter  third  input   :  7
Largest number :  20.0
Smallest number :  7.0
Middle number :  10.0

'''
'''
a=int(input("Enter  first  input   :"))
b=int(input("Enter  second   input   :"))
c=int(input("Enter  third  input   :"))

mid=((a+b+c)-(max(a,b,c)+min(a,b,c)))
print('Largest number :',max(a,b,c))
print('Smallest number :',min(a,b,c))
print('middle number :',mid)
'''
#------------------------------------------------------------------------------------

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
	What  is  the  value  of  's'  ?  --->  	(a + b + c) / 2
    What   is  the  perimeter  of  scalene  triangle ?  --->  a + b + c

4) What  is  the  qualification  of  triangle  ?  --->  Sum  of  every  two  sides  should  be  >  3rd  side

5) Hint: Use  nested  if

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

'''
import math

a=eval(input('Enter  1st  side : '))
b=eval(input('Enter  2nd  side : '))
c=eval(input('Enter  3rd  side : '))

try:
	if ((a+b)>c and (b+c)>a and (a+c)>b):
		print("Given side Qualifies the rule of triangle")
		if(a==b==c):
			print("Equalateral triangle")
			print('Area :',math.sqrt(3)/4*a**2)
		if(a==b or b==c or c==a):
			print("Isoscles  triangle")
			print("Perimeter :", a+b+c)
		if(a!=b and b!=c and c!=a):
			print("scalene  triangle")
			s=(a+b+c)/2
			print("Area :",math.sqrt(s * (s - a) * (s - b) * (s - c)))
			print("perimeter",a+b+c)
	else:
		print("Not a triangle")

except:
	print("Enter only numbers")
'''
#--------------------------------------------------------------------------------------------------------
