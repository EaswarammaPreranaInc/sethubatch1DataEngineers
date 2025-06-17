x=eval(input("enter 1st number:"))
if x%2==0:
	print('even_number:')
else:
    print('odd_number:')


output..
enter 1st number:22
even_number:

'''
try:
	x=int(input('enter month number(1-12):'))
	if x==1:
		print('jan')
	elif x==2:
		print('feb')
	elif  x==3:
		print('march')
	elif x==4:
		print('april')
	elif  x==5:
		print('may')
	elif x==6:
		print('jun')
	elif  x==7:
		print('jul')
	elif  x==8:
		print('aug')
	elif  x==9:
		print('sep')
	elif x==10:
		print('oct')
	elif  x==11:
		print('nov')
	elif  x==12:
		print('Dec')
	else:
		print('input should be (1-12):')
except:
	print('invalid month number:')

output...
enter month number(1-12):6
jun


#write a program to year is leap year or not
x=int(input('enter 4-digit year number:'))
if x%4==0 and x%100!=0 or x%400==0:
	print('leap year:')
else :
	print('not leap year:')

output...
enter 4-digit year number:2025
not leap year:


#write a program to determine largest number among three numbers
x=int(input('enter 1st number:'))
y=int(input('enter 2nd number:'))
z=int(input('enter 3rd number:'))
if x>=y and x>=y:
		print(x)
elif y>=x and y>z:
		print(y)
else:
	print(z)

output..
enter 1st number:22
enter 2nd number:11
enter 3rd number:3
22


#write a program to convert celsius temparature to farenheit and vice-versa
a=int(input('enter 1 to convert celsius to farenheit and 2 to convert farenheit to celsius:'))
if a==1:
	celsius=eval(input('enter celsius temparature:'))
	farenheit=1.8*celsius+32
	print('farenheit:',farenheit)
elif a==2:
	farenheit=eval(input('enter farenheit temparature:'))
	celsius=(farenheit-32)/1.8
	print('celsius:',celsius)

output...
enter 1 to convert celsius to farenheit and 2 to convert farenheit to celsius:1
enter celsius temparature:22
farenheit: 71.6
enter farenheit temparature:33
celsius: 0.5555555555555556


#write a program to determine three sides form a triangle or not
import math
x=int(input('enter 1st side:'))
y=int(input('enter 2nd side:'))
z=int(input('enter 3rd side:'))
if x==y and x!=z and y!=z:
		print('isoscles_trianglr:')
		perimeter=x+y+z
		print('perimeter:',perimeter)
elif x==y==z:
		print('equilateral triangle:')
		area=math.sqrt(3)/4*x**2
		print('area:',area)

elif x!=y and y!=z and x!=z:
		print('scalene triangle:')
		s=(x+y+z)/2
		area=math.sqrt(s*(s-x)*(s-y)*(s-z))
		perimeter=x+y+z
		print('area:',area)
		print('perimter:',perimeter)
else:
	print("not a trianglr")


output...
enter 1st side:5
enter 2nd side:5
enter 3rd side:4
isoscles_trianglr:
perimeter: 14

enter 1st side:5
enter 2nd side:5
enter 3rd side:5
equilateral triangle:
area: 10.825317547305483

enter 1st side:4
enter 2nd side:5
enter 3rd side:6
scalene triangle:
area: 9.921567416492215
perimter: 15

write a program to test a point(x,y) lies in 1st,2nd,3rd,4th quadrant or orgin
x=eval(input('enter value of x:'))
y=eval(input('enter value of y:'))
if x>0 and y>0:
		print('first quadrant:')
elif x<0 and y>0:
		print('second quadrant:')
elif x<0 and y<0:
		print('third quadrant:')
elif x>0 and y<0:
		print('fourth quadrant:')
elif x>0 and y==0:
		print('y-axis:')
elif x==0 and y>0:
		print('x-axis:')
elif x==0 and y==0:
		print('origin:')

output..
enter value of x:22
enter value of y:44
first quadrant


#write a program to determine largest,smallest and middle among three numbers
x=int(input("enter any number:"))
y=int(input("enter any number:"))
z=int(input("enter any number:"))
largest=max(x,y,z)
smallest=min(x,y,z)
middle = (x+y+z)-(largest+smallest)
print('largest:',largest)
print('smallest:',smallest)
print('middle:',middle)

output..
enter any number:33
enter any number:66
enter any number:22
largest: 66
smallest: 22
middle: 33


#write a program to determine a point(x,y) lies inside,outside and on the circle
import math
x=eval(input('enter 1st value:'))
y=eval(input('enter 2nd value:'))
r=eval(input('enter radius value:'))
distance=math.sqrt(x**2+y**2)
if distance>r:
		print('out side the circle:')
elif distance< r:
		print('in side the circle:')
else:
	distance==r
	print('on the circle')

output...
enter 1st value:3
enter 2nd value:4
enter radius value:5
on the circle


#write a program to day of the week
x=int(input('enter day of the week:'))
match x:
		case 1:
			print('sunday') 
		case 2:
			print('monday')
		case 3:
			print('tuesday') 
		case 4:
			print('wensday')
		case 5:
			print('thursday') 
		case 6:
			print('friday')
		case 7:
			print('saturday') 
		case(_):
			print('invalid day') 

outpout...
enter day of the week:5
thursday


#write a program to print digit in words
x=int(input('enter number:'))
match x:
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
		case 0:
			print('zero') 
		case (_):
			print('enter correct number:')

output...
enter number:9
nine


write a program to determine bill amount and input is units
units = int(input('Enter  units :   '))
match  units//100:
	case  0:
			cost=units*3.00
	case  1:
			cost = 100 * 3.00 + (units-100) * 3.50
			print('bill amount:' ,cost)
	case  2 | 3:
			cost = 100 * 3.00 + 200 * 3.50 + (units-300) * 4.00		
			print('bill amount:' ,cost)
	case  4 | 5 | 6:
			cost = 100 * 3.00 +200 * 3.50 + 300 * 4.00 + (units-600) * 4.50 	
			print('bill amount:' ,cost)
	case  _:
			cost=100 * 3.00 + 200 * 3.50 + 300*4.00 + 600*4.50 +(units-700)*5.00
			print('bill amount:' ,cost)


output...
Enter  units :   800
bill amount: 5400.0
