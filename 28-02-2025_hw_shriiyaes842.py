#1
# Identify  error
else:
		print('else  suite')
print('Outside')

out put:
error

#2
if  9 > 5
	print('Hello')
print('Bye')

out put:
 expected ':'

#3
if  9 > 12:
	print('Hyd')
else
	print('Sec')

out put:
expected ':'

#4
if  (10,20,15):
print('Hyd')
else:
print('Sec')

output:
expected an indented block after 'if' statement

#5
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
outut:
error { of flower brackets

#6
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
'''
output:
if  []:
expected an indented block after 'else' statement on line 82
'''
#8
n= int(input("Enter a +ve number: "))
if n%2==0:
    print("even number")
else:
    print("odd number")

#9
if():
        print('Hyd')
        print('Sec')
        print('Cyb')
else:
        print('One')
        print('Two')
        print('Three')
print('Bye')

output:
one
Two
three

#10
if{10 : 20 , 30 : 40}:
        print('Hyd')
        print('Sec')
        print('Cyb')
print('Bye')

output:
hyd
sec
cyd
bye

#11

if { }:
	print('Hyd')
	print('Sec')
	print('Cyb')
print('Bye')

output:
hyd
sec
cyd

#12
try:

    n=int(input('enter the no(1-12) : '))
    if n==1:
        print("jan")
    elif n==2:
        print("feb")
    elif n==3:
        print("march")
    elif n==4:
        print("april")
    elif n==5:
        print("may")
    elif n==6:
        print("june")
    elif n==7:
        print("july")
    elif n==8:
        print("aug")
    elif n==9:
        print("sep")
    elif n==10:
        print("oct")
    elif n==11:
        print("nov")
    elif n==12:
        print("dec")
    elif n!=range(12):
        print("enter a integer from 1 to 12")

except:
    print("input should be integer number")

#13
n=int(input("enter a  4 digit year : "))
if (n%4==0  and n%100==0 or n%400 ==0):
    print("leap year")
else:
    print("not a leap year")

#14
a=int(input("Enter 1st input:"))
b=int(input("Enter 2nd input:"))
c=int(input("Enter 3rd input:"))
if a>b>c:
    print("Laregst  number  : ",a)
elif b>a>c:
    print("Laregst  number  : ", b)
else:
    print("Laregst  number  : ", c)

#15
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

#16
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

#17
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

#18
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

import math
a=int(input("Enter value of a:"))
b=int(input("Enter value of b:"))
c=int(input("Enter value of c:"))
disc=b**2-4*a*c
if a==0:
    print("Value  of  a  can  not  be  0")

#19
else a!=b!=c!=0:
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

#20
import math
x=int(input("Enter  value  of  x :"))
y=int(input("Enter  value  of  y :"))
r=int(input("Enter  value  of  r :"))
d=math.sqrt(x**2+y**2)
print(d)
if d>r:
    print("Outside  the  circle")
elif d<r:
    print("Inside the circle")
else:
    print("On the circle")

#21
import math
m = 4
match  m:
	case  1:
		print('One')
	case  2:
		print('Two')
	case  3:
		print('Three')
print('Bye')

#22

i = 2
match  i:
	case  1:
		print('One')
	case  _:
		print('None of   the  above')
	case  2:
		print('Two')
print('Bye')
#wildcard makes remaining patterns unreachable

#23
m = 2
match  m:
	case  1:
		print('One')
	case  _:
		print('Hello')
	case  _:
		print('Bye')
print('End')
#wildcard makes remaining patterns unreachable

#24
m = 1
match  m:
	case  1:
		print('Hyd')
	case  1:
		print('Sec')
	case  1:
		print('Cyb')
print('Bye')
hyd
bye

#25
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

#26
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

#27
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

#28
k=int(input("enter the integer no from 1 to 7 :"))
match k:
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
        print("sunday")

#29
k=int(input("enter the integer no from 0 to 7 :"))
match k:
    case 0:
        print("zero")
    case 1:
        print("one")
    case 2:
        print("Two")
    case 3:
        print("three")
    case 4:
        print("four")
    case 5:
        print("Five")
    case 6:
        print("Six")
    case 7:
        print("seven")
    case 8:
        print("eight")
    case 9:
        print("nine")
    case 10:
        print("Not  a  digit")

#30
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

#31
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

#32
while  True:
	print('Hello')
print('Bye')

#33
while  False:
	print('Hello')
print('Bye')

