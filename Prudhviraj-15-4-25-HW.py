# Find  outputs (Home  work)
import  time
a = [25 , 10.8 , 3 + 4j , 'Hyd' , False]
f = filter(lambda   x :   True ,   a)
while  True:
	try:
		print(next(f))
		time . sleep(1)
	except:
		break
"""
Output:
25
10.8
(3+4j)
Hyd
False
"""

#  Find  outputs (Home  work)
import  time
a = [25 , 10.8 , 3 + 4j ,  'Hyd' , True]
f = filter(lambda  x  :  False ,  a)
while  True:
	try:
		print(next(f))
		time . sleep(1)
	except:
		break
"""
Output:
no output
"""

# Find  outputs (Home  work)
import  time
a = [25 , 10.8 , False ,  3 + 4j , 0 , 'Hyd' , '' , (25,)  ,  () ]
f = filter(lambda   x   :   x   ,   a)
while  True:
	try:
		print(next(f))
		time . sleep(1)
	except:
		break

"""
Output:
25
10.8
3+4j
Hyd
(25)
"""

# Find outputs
import  time
def  disp(f):
	while  True:
		try:
			print(next(f))
			time . sleep(1)
		except:
			break
list = [10 , 0 ,  -25 , () , (25,) , 'Hyd', '' , [] , 10.8 , 0.0 , [10 , 20] , True , False]
f1 = filter(lambda  x : None  , list)
print('Filter  f1')
disp(f1)
f2 = filter(None  , list)
print('Filter  f2')
disp(f2)
"""
Output:
Filter  f1
Filter  f2
10
-25
(25,)
Hyd
10.8
[10, 20]
True
"""

# Find outputs  (Home  work)
import  time
a = ['Rama Rao' , 'Sita' , 'Rajesh' , 'Kiran' , 'Amar' , 'Manohar' , 'Vamsi']
f = filter(lambda  x  :   len(x) >= 5  , a)
while   True:
	try:
		print(next(f))
		time . sleep(1)
	except:
		break
"""
Output:
Rama Rao
Rajesh
Kiran
Manohar
Vamsi
"""

# Find  outputs (Home  work)
import   time
list=[('A' , 10) , ('B' , 20) , ('C' , 15) , ('D' , 5) , ('E' , 18)]
f = filter(lambda   x  :   x[1]  >=  12 , list)
while   True:
	try:
		print(next(f))
		time . sleep(1)
	except:
		break
"""
Output:
('B' , 20)
('C' , 15)
('E' , 18)
"""

# Find  outputs (Home  work)
import   time
list = [
             {
                'Roll Num' :  10 ,
                'Stud Name' : 'Rama Rao' ,
                'Marks' : 75
              } ,
              {
                'Roll Num' :  20 ,
                'Stud Name' : 'Sita' ,
                'Marks' : 52
              } ,
             {
               'Roll Num'  :  15 ,
               'Stud Name' : 'Kiran' ,
               'Marks' : 65
             } ,
             {
               'Roll Num'  :  18 ,
               'Stud Name' : 'Amar' ,
               'Marks' : 48
             } ,
             {
               'Roll Num' :  5 ,
               'Stud Name' : 'Rajesh' ,
               'Marks' : 82
             }
        ]  #  List  of  dictionaries
f = filter(lambda  x :  x['Marks'] >= 60 , list)
while   True:
	try:
		print(next(f))
		time . sleep(1)
	except:
		break
"""
Output:
{'Roll Num': 10, 'Stud Name': 'Rama Rao', 'Marks': 75}
{'Roll Num': 15, 'Stud Name': 'Kiran', 'Marks': 65}
{'Roll Num': 5, 'Stud Name': 'Rajesh', 'Marks': 82}
"""

# Find  outputs (Home  work)
import  time
def  disp(f):
	while  True:
		try:
			print(next(f))
			time . sleep(3)
		except:
			break
a = [   { 'country' : 'India' , 'sale' : 150.5} ,
          { 'country' : 'china' , 'sale' : 200.2} ,
          { 'country' : 'USA' , 'sale' : 300.3} ,
          { 'country' : 'UK' , 'sale' : 210.4} ]
f1 = filter (lambda  x  :   x['country'] . startswith('U') , a)
print('Filter  f1')
disp(f1)
f2 = filter(lambda  x  :  x['sale']  >=  200  , a)
print('Filter  f2')
disp(f2)
"""
Output:
Filter  f1
{'country': 'USA', 'sale': 300.3}
{'country': 'UK', 'sale': 210.4}
Filter  f2
{'country': 'china', 'sale': 200.2}
{'country': 'USA', 'sale': 300.3}
{'country': 'UK', 'sale': 210.4}
"""

# How  to  print  fliter  object  in  different  ways ?
import   time
a = [10 , 15 , 20 , 17 , 18 , 19 , 26]
f = filter(lambda  x  :  x  %  2  ==  0 , a)
print('Iterate  filter  object  with   next   function')
while True:
	try: 
		print(next(f))
		time.sleep(2)
	except:
		break
print('Iterate  filter  object  with   for  loop')
f = filter(lambda  x  :  x  %  2  ==  0 , a)
for i in filter(lambda  x  :  x  %  2  ==  0 , a):
	print(next(f))
	time.sleep(2)     #How  to iterate  filter  object  with  for  loop
print('Unpacking  filter  object :  ' ,*filter(lambda  x  :  x  %  2  ==  0 , a) ) #How  to  unpack  filter  object)
print()
print('filter  object  in  the  form  of  list  :  ' ,list(filter(lambda  x  :  x  %  2  ==  0 , a))) #How  to  convert  filter  object  to  list)
"""
Output:
Iterate  filter  object  with   next   function
10
20
18
26
Iterate  filter  object  with   for  loop
10
20
18
26
Unpacking  filter  object :   10 20 18 26

filter  object  in  the  form  of  list  :   [10, 20, 18, 26]
"""

# Nested  filter  i.e.  filter  on  filter
import   time
list =  [ (10 , 'Rama' , 10000.0) ,
            (20, 'Sita' , 7000.0) ,
            (15 , 'Rajesh' , 15000.0) ,
            (5 , 'Amar' ,  12000.0) ,
            (18 , 'Ramesh' , 8000.0) ]
f = filter(lambda  x :  x[1] . startswith('R')  , filter(lambda  x :  x[2] >= 10000 , list))
while   True:
	try:
		print(next(f))
		time .  sleep(1)
	except:
		break
"""
Output:
(10, 'Rama', 10000.0)
(15, 'Rajesh', 15000.0)
"""

#  Modify  following  program  with  regular  function  and  for  loop
import  time
import  time

def square(x):
    return x*x 
    
a = [10 , 20 , 15 , 18 , 5]
m = map(square ,  a)
print(type(m)) #<class 'map'>
print(m) #<map object at 0xaddress>

for i in m:
    print(i)
    time.sleep(1)

"""
Output:
<class 'map'>
<map object at 0x00000265BD4CB010>
100
400
225
324
25
"""

# Find  outputs (Home  work)
import  time
a = [ ('A' , 10) , ('B' , 20) , ('C' , 15) , ('D' , 5) , ('E' , 18) ]
m = map(lambda   x  :  x[1]  ,  a)
while   True:
	try:
		print(next(m))
		time . sleep(1)
	except  StopIteration:
		break
"""
Output:
10
20
15
5
18
"""

# Find  outputs (Home  work)
import   time
def  disp(m):
	while   True:
		try:
			print(next(m))
			time . sleep(1)
		except:
			break
list = [    { 'country' : 'India' , 'sale' : 150.5} ,
              { 'country' : 'China' , 'sale' : 200.2} ,
              { 'country' : 'USA' , 'sale' : 300.3} ,
              { 'country' : 'UK' , 'sale' : 210.4} ]
m1 = map(lambda  x  :  x['country'] , list)
print('Map   m1')
disp(m1)
m2 = map(lambda  x  :  x['sale']  , list)
print('Map   m2')
disp(m2)
"""
Output:
Map   m1
India
China
USA
UK
Map   m2
150.5
200.2
300.3
210.4
"""

# filter  inside  map
import  time
a = [10 , 20 , 15 , 12 , 18 , 5 , 14 , 25 , 17]
m = map(lambda  y  :   y + y ,  filter(lambda  x  :  x >= 15 , a))
while   True:
	try:
		print(next(m))
		time . sleep(1)
	except:
		break

"""
Output:
40
30
36
50
34
"""

# map  inside  filter (Home  work)
import   time
a = [10 , 20 , 15 , 12 , 18 , 5 , 14 , 25 , 17]
f = filter(lambda  y  :   y  % 2 == 0 , map (lambda  x : x ** 2 , a))
while   True:
	try:
		print(next(f))
		time . sleep(1)
	except:
		break
"""
Output:
100
400
144
324
196
"""

# Find  outputs  (Home  work)
from  functools  import  reduce
a = [ 10 , 20 , 15 , 5 , 12 , 18 , 25 , 14]
ans = reduce( lambda  x , y  : x + y , map(lambda  y :  y ** 2 , filter(lambda  x  :  x  >= 15 , a)))
print(ans)
"""
Output:
1574
"""


#  Write  a  program  to  print  odd  numbers  between  1  and  20  with  filter  iterator
import time
f=filter(lambda x:x%2==1,range(1,21))
while True:
	try:
		print(next(f))
		time.sleep(1)
	except:
		break
"""
Output:
Odd  numbers  between  1  and  20
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
"""
#2
'''
Write  a  program  to  print  distinct  vowels  of  the  string  using  filter.
Input  is  string  and  output  is  set
'''
s=input("Enter the mixed case letters: ").upper()
S=set()
f=filter(lambda y: y in "AEIOU",s)
for i in f:
	S.add(i)
print(S)
"""
Output:
Enter the mixed case letters: Rama Rao
{'A', 'O'}
"""
'''
Write  a  program  to  convert  each  celsius  temperature  of  the  list  to  farenheit  temperature

1) What  is  the  formula  to  convert  celsius  temperature  to  farenheit ?  --->   1.8 * celsius  temp + 32

2) Let  input  be   list  of  celsius  temperatures  such  as  [30 , 40 , 50 , 25]
    What  is  the  output ?  --->   1.8 * 30 + 32
							                      1.8 * 40 +32
								                  1.8 * 50 + 32
								                  1.8 * 25 + 32
'''
import time
s=eval(input("Enter the List of Temperatures: "))
m=map(lambda x:x*1.8+32,s)
for i in m:
	print(i)
	time.sleep(2)
"""
Output:
Enter the List of Temperatures: [30 , 40 , 50 , 25]
86.0
104.0
122.0
77.0
"""
# Write  a  program  to  print  2 ^ 0 , 2 ^ 1 , 2 ^ 2 , ....... 2 ^ 9  using  map   object (Home  work)
m=map(lambda x:2**x,range(10))
print("Power of 2")
for i in m:
	print(i)
"""
Output:
Powers  of   2
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
"""
'''
Write  a  program  to  determine  area  of  circle  for  each  radius  in  the  list

1) What  is  area  of  circle ?  --->  pi * r * r

2) Let  input  be  [3.5 , 2.8 , 4.2  , 1.9]
    What  are  the  outputs ?  --->  Area  of  radius  3.5
						                              Area  of  radius  2.8
						                              Area  of  radius  4.2
						                              Area  of  radius  1.9
'''
import time
s=eval(input("Enter the List: "))
m=map(lambda x:3.14*x*x,s)
for i in m:
	print(i)
	time.sleep(2)
"""
Output:
Enter the List: [3.5 , 2.8 , 4.2  , 1.9]
38.465
24.6176
55.3896
11.3354
"""
'''
Write  a  program  to  add  two  tuples  of  difierent  sizes  and  store  the  results  in  3rd  tuple

Let  1st  tuple  be  (10 , 20 , 30 , 40)  and  2nd  tuple  be  (1 , 2 , 3 , 4 ,  5  ,  6)
What  is  the  3rd  tuple ?  --->  (10 + 1 , 20 + 2 , 30 + 3 , 40 + 4)   and  5  and 6  are  ignored
'''
a=eval(input("Enter the Tuple 1: "))
b=eval(input("Enter the Tuple 2: "))
c=[]
m=map(lambda x,y:x+y,a,b)
for i in m:
	c.append(i)
print(F"Added List:{tuple(c)}")
"""
Output:
Enter the Tuple 1: (10 , 20 , 30 , 40)
Enter the Tuple 2: (1 , 2 , 3 , 4 ,  5  ,  6)
Added List:(11, 22, 33, 44)
"""
#Write  a  program  to  multiply  two  lists  and  store  results  in  3rd  list
#Let  1st  list  be  [10 , 20 , 15 , 18 , 19 , 17]  and  2nd  list  be  [1 , 5 , 3 , 2]
#What  is  the  3rd  list ?  ---> [10 * 1 , 20 * 5 , 15 * 3 , 18 * 2]  and  ignores  19  and  17
#Hint:  Use  map
a=eval(input("Enter the Tuple 1: "))
b=eval(input("Enter the Tuple 2: "))
c=[]
m=map(lambda x,y:x*y,a,b)
for i in m:
	c.append(i)
print(F"Multiplied List:{c}")

"""
Output:
Enter the Tuple 1: (10 , 20 , 30 , 40)
Enter the Tuple 2: (1 , 2 , 3 , 4 ,  5  ,  6)
Multiplied List:[10, 40, 90, 160]
"""
#7)
'''
Write  a  program  to  determine  largest  element  of  the  list  with  reduce()  function

Let  list   be  [10 , 20 , 15 , 30 , 25 , 40 , 35]
What  is   the  largest  element  of  list ?  ---> 40

Hint:  Use  reduce()  function
'''
from functools import reduce 
s=eval(input("Enter the List: "))
r=reduce(lambda x,y:max(x,y),s)
print(F"Largest Element:{r}")
"""
Output:
Enter list of numbers (or) strings:[10 , 20 , 15 , 30 , 25 , 40 , 35]
Largest  element  :    40
"""
