# Find  outputs (Home  work)
import  time
a = [25 , 10.8 , 3 + 4j , 'Hyd' ,False]
f = filter(lambda   x : True ,   a)
while  True:
	try:
		print(next(f))
		time . sleep(1)
	except:
		break
'''
OUTPUT:
25
10.8
3+4j
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
'''
OUTPUT:no output
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
f2 = filter(None  , list)
print('Filter  f2')
disp(f2)

'''
OUTPUT:
Filter f1
Filter f2
10
-25
(25,)
Hyd
10.8
[10, 20]
True
'''
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
'''
OUTPUT:
25
10.8
(3+4j)
Hyd
(25,)
'''
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
		print(next(f))
		time . sleep(1)
	except:
		break
'''
OUTPUT:
('B',20)
('C' , 15)
('E' , 18)
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
		time . sleep(1)
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
disp(f1)
f2 = filter(lambda  x  :  x['sale']  >=  200  , a)
print('Filter  f2')
disp(f2)
'''
OUTPUT:
Filter f1
{ 'country' : 'USA' , 'sale' : 300.3}
{ 'country' : 'UK' , 'sale' : 210.4} 
Filter f2
{ 'country' : 'china' , 'sale' : 200.2} 
{ 'country' : 'USA' , 'sale' : 300.3} 
{ 'country' : 'UK' , 'sale' : 210.4}
'''
# How  to  print  fliter  object  in  different  ways ?
import   time
a = [10 , 15 , 20 , 17 , 18 , 19 , 26]
f = filter(lambda  x  :  x  %  2  ==  0 , a)
print('Iterate  filter  object  with   next   function')
#How  to iterate  filter  object  with  next()  function
while True:
	try:
		print(next(f))
	except:
		break
print('Iterate  filter  object  with   for  loop')
#How  to iterate  filter  object  with  for  loop
for i in filter(lambda y: y%2==0,a):
	print(i)
print('Unpacking  filter  object :  ' ,*(filter(lambda x:x%2==0,a)))
print()
b=filter(lambda z:z%2==0,a)
print('filter  object  in  the  form  of  list  :',b)
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
#  Write  a  program  to  print  odd  numbers  between  1  and  20  with  filter  iterator
a=filter(lambda x: x%2!=0,range(1,20))
for i in a:
	print(i)
'''
output:
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
PROGRAM: 

Write  a  program  to  print  distinct  vowels  of  the  string  using  filter.
Input  is  string  and  output  is  set
'''
a=input("Enter a string :")
f=filter(lambda x: x in ['A','E','I','O','U'],set(a))
print(set(f))
'''
output:
Enter a string :HYDERABAD
{'A', 'E'}
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
Output:
(10 , 'Rama' , 10000.0)
(15 , 'Rajesh' , 15000.0)
'''
#  Modify  following  program  with  regular  function  and  for  loop
import  time
a = [10 , 20 , 15 , 18 , 5]
m = map(lambda  x :  x  *  x ,  a)
print(type(m))
print(m)
while   True:
	try:
		print(next(m))
		time . sleep(1)
	except:
		break
for i in a:
	print(i*i)
'''
OUTPUT:
class map
type and address
100
400
225
324
25
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
output:
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
print('Map   m2')
disp(m2)
'''
Output:
Map  m1
India
China
USA
UK
MAp   m2
150.5
200.2
300.3
210.4
'''
'''
PROGRAM:
Write  a  program  to  convert  each  celsius  temperature  of  the  list  to  farenheit  temperature

1) What  is  the  formula  to  convert  celsius  temperature  to  farenheit ?  --->   1.8 * celsius  temp + 32

2) Let  input  be   list  of  celsius  temperatures  such  as  [30 , 40 , 50 , 25]
    What  is  the  output ?  --->   1.8 * 30 + 32
							                      1.8 * 40 +32
								                  1.8 * 50 + 32
								                  1.8 * 25 + 32
'''
a=eval(input("Enter input list of celsius temperature : "))
m=map(lambda x: 1.8*x +32,a)
for i in m:
	print(i)
'''
Output:
Enter input list of celsius temperature : [30 , 40 , 50 , 25]
86.0
104.0
122.0
77.0
'''
# Write  a  program  to  print  2 ^ 0 , 2 ^ 1 , 2 ^ 2 , ....... 2 ^ 9  using  map   object (Home  work)
def f1(x):
	return 2**x
a=map(f1,range(10))
for i in a:
	print(i)
'''
Output:
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
PROGRAM:
Write  a  program  to  determine  area  of  circle  for  each  radius  in  the  list

1) What  is  area  of  circle ?  --->  pi * r * r

2) Let  input  be  [3.5 , 2.8 , 4.2  , 1.9]
    What  are  the  outputs ?  --->  Area  of  radius  3.5
						                              Area  of  radius  2.8
						                              Area  of  radius  4.2
						                              Area  of  radius  1.9
'''
from math import pi
a=eval(input("Enter list of radius : "))
m=map(lambda x:pi*x*x,a)
while True:
	try:
		print(f'{next(m):.2f}')
	except:
		break
'''
Output:
Enter list of radius : [3.5 , 2.8 , 4.2  , 1.9]
38.48
24.63
55.42
11.34
'''
'''
PROGRAM:
Write  a  program  to  add  two  tuples  of  difierent  sizes  and  store  the  results  in  3rd  tuple

Let  1st  tuple  be  (10 , 20 , 30 , 40)  and  2nd  tuple  be  (1 , 2 , 3 , 4 ,  5  ,  6)
What  is  the  3rd  tuple ?  --->  (10 + 1 , 20 + 2 , 30 + 3 , 40 + 4)   and  5  and 6  are  ignored
'''
a=eval(input("Enter first tuple : "))
b=eval(input("Enter second tuple : "))
print(tuple(map(lambda x,y:x+y,a,b)))
'''
Output:
Enter first tuple : (10,20,30,40)
Enter first tuple : (1,2,3,4,5,6)
(11, 22, 33, 44)
'''
'''
PROGRAM:

Write  a  program  to  multiply  two  lists  and  store  results  in  3rd  list
Let  1st  list  be  [10 , 20 , 15 , 18 , 19 , 17]  and  2nd  list  be  [1 , 5 , 3 , 2]
What  is  the  3rd  list ?  ---> [10 * 1 , 20 * 5 , 15 * 3 , 18 * 2]  and  ignores  19  and  17
'''
a=eval(input("Enter first list : "))
b=eval(input("Enter second list : "))
def f1(x,y):
	return x*y
print(list(map(f1,a,b)))
'''
Output:
Enter first list : [10 , 20 , 15 , 18 , 19 , 17]
Enter second list : [1,5,3,2]
[10, 100, 45, 36]
'''
# filter  inside  map
import  time
a = [10 , 20 , 15 , 12 , 18 , 5 , 14 , 25 , 17]
m = map(lambda  y  :   y + y ,  filter(lambda  x  :  x >= 15 , a))#20,15,18,25,17
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
f = filter(lambda  y  :   y  % 2 == 0 , map (lambda  x : x ** 2 , a))#100,400,225,144,324,25,196,625,289
while   True:
	try:
		print(next(f))
		time . sleep(1)
	except:
		break
'''
Output:
100
400
144
324
196
'''
'''
PROGRAM:
Write  a  program  to  determine  largest  element  of  the  list  with  reduce()  function

Let  list   be  [10 , 20 , 15 , 30 , 25 , 40 , 35]
What  is   the  largest  element  of  list ?  ---> 40

Hint:  Use  reduce()  function
'''
from functools import reduce
a=eval(input("Enter input list : "))
r=reduce(lambda x,y:max(x,y),a)
print(r)
'''
Output:
Enter input list : [10 , 20 , 15 , 30 , 25 , 40 , 35]
40
'''
