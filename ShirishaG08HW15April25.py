#Find outputs
import time
a = [25, 10.8, 3+4j, 'Hyd', False]
f = filter(lambda x:True,a)
while  True:
	try:
		print(next(f))
		time.sleep(1)
	except:
		break

#Output
25
10.8
(3+4j)
Hyd
False



#Find outputs
import time
a = [25, 10.8, 3+4j, 'Hyd', False]
f = filter(lambda x : False, a)
while  True:
	try:
		print(next(f)) 
		time.sleep(1)
	except:
		break
#No outputs as lambda function always returns false



#Find outputs
import time
a = [25, 10.8, False, 3+4j, 0, 'Hyd', '', (25,), ()]
f=filter(lambda x : x, a)
while True:
	try:
		print(next(f))
		time.sleep(1)
	except:
		break

#Outputs
25
10.8
(3+4j)
Hyd
(25,)



#Find outputs
import time
def disp(f):
	while True:
		try:
			print(next(f))
			time.sleep(1)
		except:
			break
list=[10,0,-25,(),(25,),'Hyd','',[],10.8,0.0,[10,20],True,False]
f1=filter(lambda x : None, list)
print('Filter f1')
disp(f1)
f2=filter(None,list)
print('Filter f2')
disp(f2)

#Outputs
Filter f1
Filter f2
10
-25
(25,)
Hyd
10.8
[10, 20]
True



#Find outputs
import time
a=['Rama Rao','Sita','Rajesh','Kiran','Amar','Manohar','Vamsi']
f=filter(lambda x : len(x)>=5, a)
while True:
		try:
			print(next(f))
			time.sleep(1)
		except:
			break

#Outputs
Rama Rao
Rajesh
Kiran
Manohar
Vamsi


('B',20)
#Find outputs
import time
list=[('A',10),('B',20),('C',15),('D',5),('E',18)]
f=filter(lambda x : x[1]>=12, list)
while True:
		try:
			print(next(f))
			time.sleep(1)
		except:
			break

#Output
('B',20)
('C',15)
('E',18)



#Find outputs
import time
list=[
	{
		'Roll Num' :  10 ,
		'Stud Name' : 'Rama Rao' ,
		'Marks' : 75
	},
	{
		'Roll Num' :  20 ,
		'Stud Name' : 'Sita' ,
		'Marks' : 52
	},
	{
		'Roll Num'  :  15 ,
		'Stud Name' : 'Kiran' ,
		'Marks' : 65
	},
	{
		'Roll Num'  :  18 ,
		'Stud Name' : 'Amar' ,
		'Marks' : 48
	},
	{
		'Roll Num' :  5 ,
		'Stud Name' : 'Rajesh' ,
		'Marks' : 82
	}
	]  #List of dictionaries
f=filter(lambda x : x['Marks']>=60, list)
while True:
	try:
		print(next(f))
		time.sleep(1)
	except:
		break

#Outputs
{'Roll Num': 10, 'Stud Name': 'Rama Rao', 'Marks': 75}
{'Roll Num': 15, 'Stud Name': 'Kiran', 'Marks': 65}
{'Roll Num': 5, 'Stud Name': 'Rajesh', 'Marks': 82}



#Find outputs
import time
def disp(f):
	while True:
		try:
			print(next(f))
			time.sleep(1)
		except:
			break
a=[{'country' : 'India', 'sale' : 150.5},
   {'country' : 'china', 'sale' : 200.2},
   {'country' : 'USA', 'sale' : 300.3},
   {'country' : 'UK', 'sale' : 210.4}]
f1=filter(lambda x : x['country'].startswith('U'), a)
print('Filter f1')
disp(f1)
f2=filter(lambda x : x['sale']>=200, a)
print('Filter f2')
disp(f2)

#Outputs
Filter f1
{'country' : 'USA', 'sale' : 300.3}
{'country' : 'UK', 'sale' : 210.4}
Filter f2
{'country' : 'china', 'sale' : 200.2}
{'country' : 'USA', 'sale' : 300.3}
{'country' : 'UK', 'sale' : 210.4}



#How to print filter object in different ways
import time
a=[10,15,20,17,18,19,26]
f=filter(lambda x : x%2==0, a)
print('Iterate filter object with next function')
#How to iterate filter object with next function
while True:
	try:
		print(next(f))
		time.sleep(1)
	except:
		break
print('Iterate filter object with for loop')
#How to iterate filter object with for loop
#f=filter(lambda x : x%2==0, a)
for x in filter(lambda x : x%2==0, a):
	print(x)
	time.sleep(1)
f=filter(lambda x : x%2==0, a)
print('Unpacking filter object:',*f)
print('filter object in the form of list:',list(filter(lambda x : x%2==0, a)))

#Outputs
Iterate filter object with next function
10
20
18
26
Iterate filter object with for loop
10
20
18
26
Unpacking filter object: 10 20 18 26
filter object in the form of list: [10, 20, 18, 26]



#Print odd numbers between 1 and 20 with filter iterator
import time
f=filter(lambda x : x%2!=0, range(1,21))
print('Odd numbers between 1 and 20')
while True:
	try:
		print(next(f))
		time.sleep(0.5)
	except:
		break
	
#Outputs
Odd numbers between 1 and 20
1
3
5
7
9
11
13
15
17
19



#Print distinct vowels of the string using filter
import time
v='AEIOU'
s=input('Enter mixed case string : ').upper()
res=set()
f=filter(lambda x : x in v, s)
for y in f:
	res.add(y)
	time.sleep(1)
print(res)

#Output
Enter mixed case string : RamA raO
{'A', 'O'}



#Nested filter i.e. filter on filter
import time
list=[(10, 'Rama', 10000.0),
	  (20, 'Sita', 7000.0),
	  (15, 'Rajesh', 15000.0),
	  (5, 'Amar', 12000.0),
	  (18, 'Ramesh', 8000.0)]
f=filter(lambda x : x[1].startswith('R'), filter(lambda x : x[2]>=10000, list))
while True:
	try:
		print(next(f))
		time.sleep(1)
	except:
		break

#Outputs
(10, 'Rama', 10000.0)
(15, 'Rajesh', 15000.0)



#Modify following proogram with regular function and for loop
import time
a=[10, 20, 15, 18, 5]
m=map(lambda x : x*x, a)
print(type(m))
print(m)
while True
	try:
		print(next(m))
		time.sleep(1)
	except:
		break

#Modified code
import time
a=[10, 20, 15, 18, 5]
def square(x):
	return x*x
for x in map(square,a):
	print(x)
	time.sleep(1)

#Output
100
400
225
324
25



#Find outputs
import time
a=[('A',10),('B',20),('C',15),('D',5),('E',18)]
m=map(lambda x : x[1], a)
while True:
	try:
		print(next(m))
		time.sleep(1)
	except StopIteration:
		break

#Outputs
10
20
15
5
18



#Find outputs
import time
def disp(m):
	while True:
		try:
			print(next(m))
			time.sleep(1)
		except:
			break
list=[{'country' : 'India', 'sale' : 150.5},
	  {'country' : 'China', 'sale' : 200.2},
	  {'country' : 'USA', 'sale' : 300.3},
	  {'country' : 'UK', 'sale' : 210.4}]
m1=map(lambda x : x['country'], list)
print('Map m1')
disp(m1)
m2=map(lambda x : x['sale'], list)
print('Map m2')
disp(m2)

#Outputs
Map m1
India
China
USA
UK
Map m2
150.5
200.2
300.3
210.4



#Program to convert each celsius temperature of the list to farenheit temperature
t=eval(input('Enter list of celsius temperatures : '))
print('Farenheit temperatures')
m=map(lambda x : 1.8*x+32, t)
for x in m:
	print(x)

#Outputs
Enter list of celsius temperatures : [10,20,15,18]
Farenheit temperatures
50.0
68.0
59.0
64.4



#Print 2^0, 2^1, 2^2, ....2^9 using map object
print('Powers of 2')
m=map(lambda x : pow(2,x), range(10))
for x in m:
	print(x)

#Output
Powers of 2
1
2
4
8
16
32
64
128
256
512



#Determine area of circle for each radius in the list
import math
r=eval(input('Enter list of radii : '))
print('Area of each radius in the list')
m=map(lambda x : math.pi*x*x, r)
for y in m:
	print(F'{y:.2f}')

#Output
Enter list of radii : [1,2,3,4]
Area of each radius in the list
3.14
12.57
28.27
50.27



#Add two tuples of different sizes and store the results in 3rd tuple
t1=eval(input('Enter first tuple : '))
t2=eval(input('Enter second tuple : '))
m=map(lambda x,y:x+y, t1,t2)
l=[]
for x in m:
	l.append(x)
print('Addition tuple : ',tuple(l))

#Output
Enter first tuple : (10,30,50)
Enter second tuple : (20,40,60,70,80)
Addition tuple : (30, 70, 110)



#Multiply two lists and store results in 3rd list
l1=eval(input('Enter first list : '))
l2=eval(input('Enter second list : '))
m=map(lambda x,y:x*y, l1,l2)
res=[]
for i in m:
	res.append(i)
print('Multiplication list :',res)

#Output
Enter first list : [10,20,30]
Enter second list : [1,2,3,4]
Multiplication list : [10, 40, 90]



#filter inside map
import time
a=[10,20,15,12,18,5,14,25,17]
m=map(lambda y : y+y, filter(lambda x : x>=15, a))
while True:
	try:
		print(next(m))
		time.sleep(1)
	except:
		break

#Output
40
30
36
50
34



#map inside filter
import time
a=[10,20,15,12,18,5,14,25,17]
m=filter(lambda y : y%2==0, map(lambda x : x**2, a))
while True:
	try:
		print(next(m))
		time.sleep(1)
	except:
		break

#Output
100
400
144
324
196



#Determine largest element of the list with reduce() function
from functools import reduce
a=eval(input('Enter list of numbers (or) strings : '))
res=reduce(lambda x,y : x if x>y else y, a)
print('Largest element :',res)

#Output
Enter list of numbers (or) strings : [40,30,60,50]
Largest element : 60



#Find outputs
from functools import reduce
a=[10,20,15,5,12,18,25,14]
ans=reduce(lambda x,y:x+y, map(lambda y:y**2, filter(lambda x:x>=15, a)))
print(ans) #20 15 18 25 => 400 + 225 + 324 + 625 => 1574
