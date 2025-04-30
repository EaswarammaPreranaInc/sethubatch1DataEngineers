# Find  outputs (Home  work)
'''import  time
a = [25 , 10.8 , 3 + 4j , 'Hyd' , False]
f = filter(lambda   x : True ,   a)
while  True:
	try:
		print(next(f)) #25 10.8 3+4j 'Hyd' false
		time . sleep(1)
	except:
		break

#  Find  outputs (Home  work)
import  time
a = [25 , 10.8 , 3 + 4j ,  'Hyd' , True]
f = filter(lambda  x  :  False ,  a)
while  True:
	try:
		print(next(f))# empty becoz every condition is False
		time . sleep(1)
	except:
		break

# Find  outputs (Home  work)
import  time
a = [25 , 10.8 , False ,  3 + 4j , 0 , 'Hyd' , '' , (25,)  ,  () ]
f = filter(lambda   x   :   x   ,   a)
while  True:
	try:
		print(next(f)) #[25 , 10.8 , False ,  3 + 4j , 0 , 'Hyd' , (25,) ]
		time . sleep(1)
	except:
		break

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
f1 = filter(lambda  x : None  , list)#
print('Filter  f1')
disp(f1)#empty
f2 = filter(None  , list)
print('Filter  f2')
disp(f2)#10<next line>-25<next line>(25,)<next line>'Hyd'<next line>10.8<next line>[10,20]<next line>True

# Find outputs  (Home  work)
import  time
a = ['Rama Rao' , 'Sita' , 'Rajesh' , 'Kiran' , 'Amar' , 'Manohar' , 'Vamsi']
f = filter(lambda  x  :   len(x) >= 5  , a)
while   True:
	try:
		print(next(f))#'Rama Rao'<next line>'Rajesh'<next line>'Rajesh'<next line>'Manohar'<next line>'Vamsi
		time . sleep(1)
	except:
		break

# Find  outputs (Home  work)
import   time
list=[('A' , 10) , ('B' , 20) , ('C' , 15) , ('D' , 5) , ('E' , 18)]
f = filter(lambda   x  :   x[1]  >=  12 , list)
while   True:
	try:
		print(next(f))#('B',20)<next line>('C',15)<next line>('E',18)
		time . sleep(1)
	except:
		break

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
outputs--
  {'Roll Num' :  10 ,'Stud Name' : 'Rama Rao' ,'Marks' : 75}
  <next line>
   {'Roll Num'  :  15 ,'Stud Name' : 'Kiran' ,'Marks' : 65}
  <next line>
   {'Roll Num' :  5 ,'Stud Name' : 'Rajesh' ,'Marks' : 82}

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

outputs---
'Filter  f1'
{ 'country' : 'USA' , 'sale' : 300.3} 
{'country' : 'UK' , 'sale' : 210.4}
'Filter  f2'
{ 'country' : 'china' , 'sale' : 200.2} 
{ 'country' : 'USA' , 'sale' : 300.3} 
{ 'country' : 'UK' , 'sale' : 210.4} 

# How  to  print  fliter  object  in  different  ways ?
import   time
a = [10 , 15 , 20 , 17 , 18 , 19 , 26]
f = filter(lambda  x  :  x  %  2  ==  0 , a)
print( 'Iterate  filter  object  with   next   function')
while True:
	try:
		print(next(f))
		time.sleep(0.5)
	except:
		break #How  to iterate  filter  object  with  next()  function
print('Iterate  filter  object  with   for  loop')
f = filter(lambda  x  :  x  %  2  ==  0 , a)
for i in f:
	print(i)#How  to iterate  filter  object  with  for  loop
f = filter(lambda  x  :  x  %  2  ==  0 , a)
print('Unpacking  filter  object :  ' ,  *f ) #How  to  unpack  filter  object)
print()
f = filter(lambda  x  :  x  %  2  ==  0 , a)
print('filter  object  in  the  form  of  list  :  ' , list(f))#How  to  convert  filter  object  to  list)
outputs--
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

#  Write  a  program  to  print  odd  numbers  between  1  and  20  with  filter  iterator
import time
a=range(21)
f=filter(lambda x:x%2!=0,a)
while True:
	try:
		
		print(next(f))
		time.sleep(1)
	except:
		break
Write  a  program  to  print  distinct  vowels  of  the  string  using  filter.
Input  is  string  and  output  is  set
a=input('enter mixed case string:').upper()
b='AEIOU'
f=filter(lambda x: x in b,a)
while True:
		try:
			next(f)
			
		except:
			break

print(set(filter(lambda x: x in b,a)))
outputs--
enter mixed case string:rama rao
{'A', 'O'}
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

OUTPUTS--
(10, 'Rama', 10000.0)
(15, 'Rajesh', 15000.0)

#  Modify  following  program  with  regular  function  and  for  loop
import  time
a = [10 , 20 , 15 , 18 , 5]
m = map(lambda  x :  x  *  x ,  a)
print(type(m))
print(m)
for i in m:
	print(i)
	time.sleep(1)

# Find  outputs (Home  work)
import  time
a = [ ('A' , 10) , ('B' , 20) , ('C' , 15) , ('D' , 5) , ('E' , 18) ]
m = map(lambda   x  :  x[1]  ,  a)
while   True:
	try:
		print(next(m)) #
		time . sleep(1)
	except  StopIteration:
		break
outputs--
10
20
15
5
18

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
outputs--
Map   m1
India
China
USA
UK
Map   m2
150.5
200.2
300.3
210.4'''

'''
Write  a  program  to  convert  each  celsius  temperature  of  the  list  to  farenheit  temperature

1) What  is  the  formula  to  convert  celsius  temperature  to  farenheit ?  --->   1.8 * celsius  temp + 32

2) Let  input  be   list  of  celsius  temperatures  such  as  [30 , 40 , 50 , 25]
    What  is  the  output ?  --->   1.8 * 30 + 32
							                      1.8 * 40 +32
								                  1.8 * 50 + 32
								                  1.8 * 25 + 32

import time
a=eval(input('enter list elements:'))
m=map(lambda x:1.8*x+32 ,a)
while True:
	try:
		print(next(m))
		time.sleep(1)
	except:
		break
outputs--
enter list elements:[30 , 40 , 50 , 25]
86.0
104.0
122.0
77.0

# Write  a  program  to  print  2 ^ 0 , 2 ^ 1 , 2 ^ 2 , ....... 2 ^ 9  using  map   object (Home  work)
import time
a=range(0,10)
m=map(lambda x:2**x ,a)
print('powers of 2:')
for i in m:
		print(i)
outputs---
powers of 2:
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


Write  a  program  to  determine  area  of  circle  for  each  radius  in  the  list

1) What  is  area  of  circle ?  --->  pi * r * r

2) Let  input  be  [3.5 , 2.8 , 4.2  , 1.9]
    What  are  the  outputs ?  --->  Area  of  radius  3.5
						                              Area  of  radius  2.8
						                              Area  of  radius  4.2
						                              Area  of  radius  1.9

import math
import time
a=eval(input('enter list elements:'))
m=map(lambda x:math.pi*x*x,a)
for i in m:
	print(i)
	time.sleep(1)
outputs--
enter list elements:[1,2,3,4]
3.141592653589793
12.566370614359172
28.274333882308138
50.26548245743669


Write  a  program  to  add  two  tuples  of  difierent  sizes  and  store  the  results  in  3rd  tuple

Let  1st  tuple  be  (10 , 20 , 30 , 40)  and  2nd  tuple  be  (1 , 2 , 3 , 4 ,  5  ,  6)
What  is  the  3rd  tuple ?  --->  (10 + 1 , 20 + 2 , 30 + 3 , 40 + 4)   and  5  and 6  are  ignored

import time
a=eval(input('enter tuple values:'))
b=eval(input('enter tuple values:'))
m=map(lambda x,y:x+y ,a,b)
while True:
		try:
			next(m)
			time.sleep(1)

		except:
			break
m=map(lambda x,y:x+y ,a,b)
print(f'Addition Tuple is: {tuple(m)}')
outputs---
enter tuple values:(1,2,3)
enter tuple values:(4,5,6)
Addition Tuple is:(5, 7, 9)


Write  a  program  to  multiply  two  lists  and  store  results  in  3rd  list

Let  1st  list  be  [10 , 20 , 15 , 18 , 19 , 17]  and  2nd  list  be  [1 , 5 , 3 , 2]
What  is  the  3rd  list ?  ---> [10 * 1 , 20 * 5 , 15 * 3 , 18 * 2]  and  ignores  19  and  17

Hint:  Use  map

import time
a=eval(input('enter list elements:'))
b=eval(input('enter list elements:'))
m=map(lambda x,y:x*y,a,b)
while True:
		try:
			next(m)
			time.sleep(1)
		except:
			break
m=map(lambda x,y:x*y,a,b)
print(f'Multiplication of lists:{list(m)}')
outputs--
enter list elements:[1,2,3]
enter list elements:[4,5,6,6,7]
Multiplication of lists:[4, 10, 18]

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
output--
40
30
36
50
34

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
outputs--
100
400
144
324
196

# Find  outputs  (Home  work)
from  functools  import  reduce
a = [ 10 , 20 , 15 , 5 , 12 , 18 , 25 , 14]
ans = reduce( lambda  x , y  : x + y , map(lambda  y :  y ** 2 , filter(lambda  x  :  x  >= 15 , a)))
print(ans)
#1574


Write  a  program  to  determine  largest  element  of  the  list  with  reduce()  function

Let  list   be  [10 , 20 , 15 , 30 , 25 , 40 , 35]
What  is   the  largest  element  of  list ?  ---> 40

Hint:  Use  reduce()  function
'''
from functools import reduce
a=eval(input('enter list elements:'))
ans=reduce(lambda x,y: max(a),a)
print(ans)
output--
enter list elements:[10 , 20 , 15 , 30 , 25 , 40 , 35]
40
