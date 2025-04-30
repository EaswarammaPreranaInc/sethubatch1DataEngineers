# Find  outputs (Home  work)
import  time
a = [25 , 10.8 , 3 + 4j , 'Hyd' , False]
f = filter(lambda   x :   True ,   a)
while  True:
	try:
		print(next(f)) # 25 <nextline> 10.8 <nextline> 3+4j <nextline> 'Hyd' <nextline> False
		time . sleep(1)
	except:
		break
'''
OUTPUT:
25
10.8
(3+4j)
Hyd
False
'''


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

# Find  outputs (Home  work)
import  time
a = [25 , 10.8 , False ,  3 + 4j , 0 , 'Hyd' , '' , (25,)  ,  () ]
f = filter(lambda   x   :   x   ,   a)
while  True:
	try:
		print(next(f))  # 25 <nextline> 10.8 <nextline> False <nextline> 3+4j <nextline> 'Hyd' <nextline> (25,)
		time . sleep(1)
	except:
		break
'''
OUTPUT:
25
10.8
(3+4j)
Hyd
(25,)
'''

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
f2 = filter(None , list)
print('Filter  f2')
disp(f2) #f=f2

'''
OUTPUT:
Filter  f1
Filter  f2
10
-25
(25,)
Hyd
10.8
[10, 20]
True
'''


# Find outputs  (Home  work)
import  time
a = ['Rama Rao' , 'Sita' , 'Rajesh' , 'Kiran' , 'Amar' , 'Manohar' , 'Vamsi']
f = filter(lambda  x  :   len(x) >= 5  , a)
while   True:
	try:
		print(next(f))   #'Rama Rao' <nextline> 'Rajesh' <nextline> 'Kiran' <nextline> 'Manohar' <nextline> 'Vamsi'
		time . sleep(1)
	except:
		break
'''
OUTPUT:
Rama Rao
Rajesh
Kiran
Manohar
Vamsi
'''


# Find  outputs (Home  work)
import   time
list=[('A' , 10) , ('B' , 20) , ('C' , 15) , ('D' , 5) , ('E' , 18)]
f = filter(lambda   x  :   x[1]  >=  12 , list)
while   True:
	try:
		print(next(f))  #('B' , 20) <nextline> ('C' , 15) <nextline> ('E' , 18) 
		time . sleep(1)
	except:
		break

'''
OUTPUT:
('B', 20)
('C', 15)
('E', 18)
'''



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
		time . sleep(1)   #{'Roll Num': 10, 'Stud Name': 'Rama Rao', 'Marks': 75} <nextline> {'Roll Num': 15, 'Stud Name': 'Kiran', 'Marks': 65} <nextline> {'Roll Num': 5, 'Stud Name': 'Rajesh', 'Marks': 82} 
	except:
		break
'''
OUTPUT:
{'Roll Num': 10, 'Stud Name': 'Rama Rao', 'Marks': 75}
{'Roll Num': 15, 'Stud Name': 'Kiran', 'Marks': 65}
{'Roll Num': 5, 'Stud Name': 'Rajesh', 'Marks': 82}
'''



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
disp(f1)  #{ 'country' : 'USA' , 'sale' : 300.3} <nextline> { 'country' : 'UK' , 'sale' : 210.4} 
f2 = filter(lambda  x  :  x['sale']  >=  200  , a)
print('Filter  f2')
disp(f2)  #{ 'country' : 'china' , 'sale' : 200.2} <nextline> { 'country' : 'USA' , 'sale' : 300.3} <nextline> { 'country' : 'UK' , 'sale' : 210.4} 

'''
OUTPUT:
Filter  f1
{'country': 'USA', 'sale': 300.3}
{'country': 'UK', 'sale': 210.4}
Filter  f2
{'country': 'china', 'sale': 200.2}
{'country': 'USA', 'sale': 300.3}
{'country': 'UK', 'sale': 210.4}
'''



# How  to  print  fliter  object  in  different  ways ?
import   time
a = [10 , 15 , 20 , 17 , 18 , 19 , 26]
f = filter(lambda  x  :  x  %  2  ==  0 , a)
print('Iterate  filter  object  with   next   function')
while True:
	try:
		print(next(f))
	except:
		break
#How  to iterate  filter  object  with  next()  function
print('Iterate  filter  object  with   for  loop')
for x in filter(lambda  x  :  x  %  2  ==  0 , a):
	print(x)
#How  to iterate  filter  object  with  for  loop
print('Unpacking  filter  object :  ' ,  *filter(lambda  x  :  x  %  2  ==  0 , a))
print()
print('filter  object  in  the  form  of  list  :  ' ,list(filter(lambda  x  :  x  %  2  ==  0 , a)))


'''
OUTPUT:
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
'''



#  Write  a  program  to  print  odd  numbers  between  1  and  20  with  filter  iterator

a=range(1,21)
for x in filter(lambda  x  :  x  %  2  !=  0 , a):
	print(x)
'''
OUTPUT:
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
'''



'''
Write  a  program  to  print  distinct  vowels  of  the  string  using  filter.
Input  is  string  and  output  is  set'''

s = input("Enter a string: ")
t=s.upper()
vowels = 'AEIOU'
vowel_chars = filter(lambda x: x in vowels, t)
distinct_vowels = set(vowel_chars)
print("Distinct vowels:", distinct_vowels)


'''
OUTPUT:
Enter a string: Rama Rao
Distinct vowels: {'A', 'O'}
'''



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

'''
OUTPUT:
(10, 'Rama', 10000.0)
(15, 'Rajesh', 15000.0)
'''



#  Modify  following  program  with  regular  function  and  for  loop
import  time
a = [10 , 20 , 15 , 18 , 5]
m = map(lambda  x :  x  *  x ,  a)
print(type(m))
print(m)
while   True:
	try:
		print(next(m))   #100 <nextline> 400 <nextline> 225 <nextline> 324 <nextline> 25
		time . sleep(1)
	except:
		break
'''
OUTPUT:
<class 'map'>
<map object at 0x000001BA76A6BA60>
100
400
225
324
25
'''



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
'''
OUTPUT:
10
20
15
5
18
'''



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

'''
OUTPUT:
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
'''



'''
Write  a  program  to  convert  each  celsius  temperature  of  the  list  to  farenheit  temperature

1) What  is  the  formula  to  convert  celsius  temperature  to  farenheit ?  --->   1.8 * celsius  temp + 32

2) Let  input  be   list  of  celsius  temperatures  such  as  [30 , 40 , 50 , 25]
    What  is  the  output ?  --->   1.8 * 30 + 32
							                      1.8 * 40 +32
								                  1.8 * 50 + 32
								                  1.8 * 25 + 32'''
import time
a=eval(input())
c=[]
for i in range(len(a)):
	b=1.8*a[i]+32
	c.append(b)
m1 = map(lambda  x  :  x , c)
while True:
	try:
		print(next(m1))
		time.sleep(1)
	except:
		break

'''
OUTPUT:
[10,20,15,18]
50.0
68.0
59.0
64.4
'''



# Write  a  program  to  print  2 ^ 0 , 2 ^ 1 , 2 ^ 2 , ....... 2 ^ 9  using  map   object (Home  work)
import time
a=range(0,10)
c=[]
for i in range(len(a)):
	b=2**i
	c.append(b)
m1=map(lambda x: x,c)
while True:
	try:
		print(next(m1))
		time.sleep(0.5)
	except:
		break

'''
OUTPUT:
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
'''


'''
Write  a  program  to  determine  area  of  circle  for  each  radius  in  the  list

1) What  is  area  of  circle ?  --->  pi * r * r

2) Let  input  be  [3.5 , 2.8 , 4.2  , 1.9]
    What  are  the  outputs ?  --->  Area  of  radius  3.5
						                              Area  of  radius  2.8
						                              Area  of  radius  4.2
						                              Area  of  radius  1.9'''

import time
import math
a=eval(input())
c=[]
for i in range(len(a)):
	b=math.pi*a[i]*a[i]
	c.append(b)
m1=map(lambda x: x,c)
while True:
	try:
		print(next(m1))
		time.sleep(0.5)
	except:
		break
'''
OUTPUT:
[1,2,3,4]
3.141592653589793
12.566370614359172
28.274333882308138
50.26548245743669
'''


import math
radii = [1, 2.5, 3, 4.2, 5]
def area_of_circle(radius):
    return math.pi * radius ** 2
areas = map(area_of_circle, radii)
areas_list = list(areas)
print("Areas of circles:", areas_list)

'''
OUTPUT:
[1,2,3,4]
3.141592653589793
12.566370614359172
28.274333882308138
50.26548245743669
'''



'''
Write  a  program  to  add  two  tuples  of  difierent  sizes  and  store  the  results  in  3rd  tuple
Let  1st  tuple  be  (10 , 20 , 30 , 40)  and  2nd  tuple  be  (1 , 2 , 3 , 4 ,  5  ,  6)
What  is  the  3rd  tuple ?  --->  (10 + 1 , 20 + 2 , 30 + 3 , 40 + 4)   and  5  and 6  are  ignored'''

import time
a=(10,20,30,40)
b=(1,2,3,4,5,6)
d=[]
for i in range(min(len(a),len(b))):
	c=a[i]+b[i]
	d.append(c)
m1=map(lambda x: x,d)
while True:
	try:
		print(next(m1))
		time.sleep(0.5)
	except:
		break

'''
OUTPUT:
11
22
33
44
'''

a = (10, 20, 30, 40)
b = (1, 2, 3, 4)
res = tuple(map(lambda x, y: x + y, a, b))
print(res)
'''
OUTPUT:
(11, 22, 33, 44)
'''



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
'''
OUTPUT:
40
30
36
50
34
'''



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
'''
OUTPUT:
100
400
144
324
196
'''



'''
Write  a  program  to  determine  largest  element  of  the  list  with  reduce()  function

Let  list   be  [10 , 20 , 15 , 30 , 25 , 40 , 35]
What  is   the  largest  element  of  list ?  ---> 40

Hint:  Use  reduce()  function
'''
from functools import reduce
numbers = [10, 20, 15, 30, 25, 40, 35]
largest = reduce(lambda x, y: x if x > y else y, numbers)
print(largest)

'''
OUTPUT:
40
'''
