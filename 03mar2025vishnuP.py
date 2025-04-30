
# 03march2025
a=[1,2,3]
b=[3,2,1]
c=[a[0]+b[0],a[1]+b[1],a[2]+b[2]]
for i in c:
    print(i)

# 03march2025
# Find  outputs  (Home  work)
for  i   in   range(1 , 8):
	print(i)
	if   i % 3 == 0:
		exit()
	else:
		print('Sec')
	print('Hello')
# End  of  the  loop
print('Outside loop')

# Find  outputs  (Home  work)
for  i   in   range(1 , 8):
	print(i)
	if   i % 3 == 0:
		pass
		print('Hyd')
	else:
		print('Sec')
	print('Hello')
# End  of  the  loop
print('Outside loop')

# Identify Error  (Home  work)
if(10 , 20 , 30):
	print('Hyd')
	break
	print('Sec')
    

# Find outputs (Home  work)
for  i   in   range(1 , 8):
	print(i)
	if   i % 3 == 0:
		break
	else:
		print('Sec')
	print('Hello')
# End  of  the  loop
print('Outside loop')

i=1
while i <=10:
    print(i*2-1)
    i += 1

for i in range(10,0,-1):
    print(i)

# sum of n terms
n= float(input("enter a number"))
i=1
sum=0
while i<=n:
    m=1.1*i
    sum=sum+m
    i+=1
print(sum)

# sum of n even terms
n= float(input("enter a number"))
i=1
sum=0
while i<=n:
    m=2*i
    sum=sum+m
    i+=1
print(sum)

# sum of n odd terms
n= float(input("enter a number"))
i=1
sum=0
while i<=n:
    m=2*i-1
    sum=sum+m
    i+=1
print(sum)

# sum of n natural terms
n= float(input("enter a number"))
i=1
sum=0
while i<=n:
    sum=sum+i
    i+=1
print(sum)

# fibbino  with n terms
a=0
b=1
n=range(eval(input("enter a number")))
sum = 0
print(a)
for x in n:
    a=b
    b= sum
    sum = a + b
    print(sum)
#1
x = int(input('enter  input:'))
if x%2==0:
	print('even')
else:
	print('odd')
#2
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
# Find  outputs  (Home  work)
if{10 : 20 , 30 : 40}:
        print('Hyd')
        print('Sec')
        print('Cyb')
print('Bye')

#3
try:
	x = int(input('enter  input:'))
	if x==1:
		print('Jan')
	elif x==2:
		print('feb')
	elif x==3:
		print('mar')
	elif x==4:
		print('apr')
	elif x==5:
		print('may')
	elif x==6:
		print('june')
	elif x==7:
		print('july')
	elif x==8:
		print('aug')
	elif x==9:
		print('sep')
	elif x==10:
		print('oct')
	elif x==11:
		print('nov')
	elif x==12:
		print('dec')
	else:
		print('enter number between 1 and 12')
except:
	print('number should be integer')

#4
x = eval(input('enter 1st input:'))
if x%4==0 and not x%100==0 or x%400==0:
    print(f'{x} is leap year')
else:
    print(f'{x} is not leap year' )

#5
x = float(input('enter 1st input:'))
y = float(input('enter 2nd input:'))
z = float(input('enter 3rd input:'))
if x>y>z:
    print('f{x} is largest')
elif y>x>z:
    print(f'{y} is largest')
else:
    print(f'{z} is largest')

#6
print('enter 1 to  convert  celsius  to  fahrenheit \n   2  to  convert  fahrenheit  to  celsius ')
x = float(input('enter 1st input:'))
if x==1:
    temp = float(input('Enter  celsius  temperature:'))
    cel = 1.8 * temp + 32
    print(f'fahrenheit Equivalent :{cel}')
elif x==2:
    temp = float(input('Enter  fahrenheit  temperature:'))
    far =  (temp-32)/1.8
    print(f'celsius Equivalent :{far}')
else:
    print('enter valid number')

#7
try:
    x = float(input('enter value  of  x  co-ordinate:'))
    y = float(input('enter value  of  y  co-ordinate:'))
    if x>0 and y>0:
        print('1st quadrant')
    elif x<0 and y>0:
        print('2nd quadrant')
    elif x<0 and y<0:
        print('3rd quadrant')
    elif x>0 and y<0:
        print('4th quadrant')
    elif x>0 and y==0:
        print('x axis')
    elif x==0 and y>0:
        print('y axis')
    elif x==0 and y==0:
        print('origin')
except:
    print('enter numbers only')

#8
x = float(input('enter 1st input:'))
y = float(input('enter 2nd input:'))
z = float(input('enter 3rd input:'))
largest = max(x,y,z)
smallest = min(x,y,z)
middle = x+y+z -(largest+smallest)
print('largest:',largest)
print('smallest',smallest)
print('middle',middle)

#9
try:
    import math
    x = float(input('enter 1st input:'))
    y = float(input('enter 2nd input:'))
    z = float(input('enter 3rd input:'))
    if (x+y)>z or (y+z)>x or (x+z)>y:
        if x==y==z:
            print('equilateral  triangle')
            area = math.sqrt(3) / 4 * x ** 2
            print('area',area)

        elif x==y or y==z or x==z:
            print('isosceles triangle')
            pm = x+y+z
            print('pm:',pm)

        elif x!=y!=z:
            s = (x+y+z)/2
            area =math.sqrt(s * (s - x) * (s - y) * (s - z))
            print('scalene triangle')
            print('area:',area)
            pm = x+y+z
            print('pm:',pm)
except:
    print('not a triangle')

#10
n= int(input("enter a number"))
a,b=0,1
while a<=n:
    print(a)
    a,b=b,a+b