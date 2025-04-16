'''
#1) Find  outputs (Home  work)
import  time
a = [25 , 10.8 , 3 + 4j , 'Hyd' , False]
f = filter(lambda   x :   True ,   a) # there is a value for 'x' then lamda function executes. 
while  True: # while loop executes for 5 times + stop iteration error executes----> 6 times executes.
	try:
		print(next(f)) # 25 <next line> 10.8 <next line> (3+4j) <next line> Hyd <next line> False.
		time . sleep(1)
	except:
		break

output:-
--------
25
10.8
(3+4j)
Hyd
False

#2) Find  outputs (Home  work)
import  time
a = [25 , 10.8 , 3 + 4j ,  'Hyd' , True]
f = filter(lambda  x  :  False ,  a) # there is no  value for 'x' then lamda function executes.
while  True:
	try:
		print(next(f))
		time . sleep(1)
	except:
		break

output:-
---------
nothing 

#3) Find  outputs (Home  work)
import  time
a = [25 , 10.8 , False ,  3 + 4j , 0 , 'Hyd' , '' , (25,)  ,  () ]
f = filter(lambda   x   :   x   ,   a)  # if value for 'x'is True  then lamda function executes-----> False, 0, ''(empty string), ()(empty bracket) are not consider
while  True:
	try:
		print(next(f)) # 25 <next line> 10.8 <next line> (3+4j) <next line> Hyd <next line> (25,)
		time . sleep(1)
	except:
		break

output:-
--------
25
10.8
(3+4j)
Hyd
(25,)


#4)Find outputs
import  time
def  disp(f):
	while  True:
		try:
			print(next(f))
			time . sleep(1)
		except:
			break
list = [10 , 0 ,  -25 , () , (25,) , 'Hyd', '' , [] , 10.8 , 0.0 , [10 , 20] , True , False]
f1 = filter(lambda  x : None  , list) # prints nothing here 
print('Filter  f1') # Filter  f1
disp(f1) # prints nothing here
f2 = filter(None  , list) # prints Tota list---------> f2 = filter(lambda x: x , list) internally None is treated as like this by PVM .bcz it is not a method or function to call, so  it is a object .
print('Filter  f2') # Filter  f2
disp(f2) # prints Tota list

output:-
--------
Filter  f1
Filter  f2
10
-25
(25,)
Hyd
10.8
[10, 20]
True

#5) Find outputs  (Home  work)
import  time
a = ['Rama Rao' , 'Sita' , 'Rajesh' , 'Kiran' , 'Amar' , 'Manohar' , 'Vamsi']
f = filter(lambda  x  :   len(x) >= 5  , a) # it executes only upto 5 letters in each elements bcz od condition of lamda function here
while   True:
	try:
		print(next(f)) # Rama Rao <next line> Rajesh <next line> Kiran <next line> Manohar <next line> Vamsi
		time . sleep(1)
	except:
		break
output:-
-----------
Rama Rao
Rajesh
Kiran
Manohar
Vamsi

#6) Find  outputs (Home  work)
import   time
list=[('A' , 10) , ('B' , 20) , ('C' , 15) , ('D' , 5) , ('E' , 18)]
f = filter(lambda   x  :   x[1]  >=  12 , list) # filter executes only for >= 12 in each 2nd elements of list 'a'. 
while   True:
	try:
		print(next(f))
		time . sleep(1)
	except:
		break
output:-
----------
('B', 20)
('C', 15)
('E', 18)

#7) Find  outputs (Home  work)
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
f = filter(lambda  x :  x['Marks'] >= 60 , list) # filter executes only for >= 60 marks elements 
while   True:
	try:
		print(next(f))
		time . sleep(1)
	except:
		break

output:-
-----------
{'Roll Num': 10, 'Stud Name': 'Rama Rao', 'Marks': 75}
{'Roll Num': 15, 'Stud Name': 'Kiran', 'Marks': 65}
{'Roll Num': 5, 'Stud Name': 'Rajesh', 'Marks': 82}


#8)Find  outputs (Home  work)
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
f1 = filter (lambda  x  :   x['country'] . startswith('U') , a) # it executes for only countries starting with letter 'U'
print('Filter  f1')
disp(f1)
f2 = filter(lambda  x  :  x['sale']  >=  200  , a) # it executes for only sales are >= 200
print('Filter  f2')
disp(f2)

output:-
---------
Filter  f1
{'country': 'USA', 'sale': 300.3}
{'country': 'UK', 'sale': 210.4}
Filter  f2
{'country': 'china', 'sale': 200.2}
{'country': 'USA', 'sale': 300.3}
{'country': 'UK', 'sale': 210.4}

#9)How  to  print  fliter  object  in  different  ways ?
import   time
a = [10 , 15 , 20 , 17 , 18 , 19 , 26]
f = filter(lambda  x  :  x  %  2  ==  0 , a)
print('Iterate  filter  object  with   next   function')
while True:
	try:
		print(next(f)) 
		time . sleep (1)
	except StopIteration:
		break #How  to iterate  filter  object  with  next()  function
print('Iterate  filter  object  with   for  loop')
a = [10 , 15 , 20 , 17 , 18 , 19 , 26]
f = filter(lambda  x  :  x  %  2  ==  0 , a)
for x in f: # How  to iterate  filter  object  with  for  loop
	print(x) 
a = [10 , 15 , 20 , 17 , 18 , 19 , 26]
f = filter(lambda  x  :  x  %  2  ==  0 , a)
print('Unpacking  filter  object :  ' ) 
print(*f) #  How  to  unpack  filter  object
print()
a = [10 , 15 , 20 , 17 , 18 , 19 , 26]
f = filter(lambda  x  :  x  %  2  ==  0 , a)
print('filter  object  in  the  form  of  list  :  ' , list(f) ) # How  to  convert  filter  object  to  list)

output:-
---------
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
Unpacking  filter  object :
10 20 18 26

filter  object  in  the  form  of  list  :   [10, 20, 18, 26]

#10) Write  a  program  to  print  odd  numbers  between  1  and  20  with  filter  iterator
import time
a = range(1,20)
f = filter(lambda  x  :  x  %  2  !=  0 , a)  f = filter(lambda  x  :  x  %  2  ==  1 , a)
print(f)
while True:
	try:
		print(next(f))
		time . sleep(1)
	except StopIteration:
		break
output:-
----------
<filter object at 0x000001711520ADA0>
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

#11)Write  a  program  to  print  distinct  vowels  of  the  string  using  filter.
Input  is  string  and  output  is  set
output Enter  mixed  case   string  :  RamA raO
{'O', 'A'}
import time # no use here , time function is used only when loop is used
a = input( 'Enter  mixed  case   string:')
vowels = 'aeiouAEIOU'
f = filter(lambda x: x in vowels , a)
print(set(f))
time . sleep(1)

output:-
--------
Enter  mixed  case   string: RamA raO
{'O', 'A', 'a'}

(or)

a = input('Enter mixed case string: ') . upper()
f = filter(lambda ch : ch in 'AEIOU' , a)
print(set(f))

output:-
-----------
Enter mixed case string: RamA Rao
{'A', 'O'}

#12)Nested  filter  i.e.  filter  on  filter

import   time
list =  [ (10 , 'Rama' , 10000.0) ,
            (20, 'Sita' , 7000.0) ,
            (15 , 'Rajesh' , 15000.0) ,
            (5 , 'Amar' ,  12000.0) ,
            (18 , 'Ramesh' , 8000.0) ]
f = filter(lambda  x :  x[1] . startswith('R')  , filter(lambda  x :  x[2] >= 10000 , list)) # lamda function executes for only Name starts with 'R' and salary with >= 10000.
while   True:
	try:
		print(next(f))
		time .  sleep(1)
	except:
		break

output:-
------------
(10, 'Rama', 10000.0)
(15, 'Rajesh', 15000.0)

#13)Modify  following  program  with  regular  function  and  for  loop
import  time
a = [10 , 20 , 15 , 18 , 5]
m = map(lambda  x :  x  *  x ,  a) # map executes for all the elements -----> square function done.
print(type(m)) # <class 'map'>
print(m) # <map object at 0x000001C38F11AE60>
while   True:
	try:
		print(next(m))
		time . sleep(1)
	except:
		break
output:-
----------
<class 'map'>
<map object at 0x000001C38F11AE60>
100
400
225
324
25

#14)Find  outputs (Home  work)
import  time
a = [ ('A' , 10) , ('B' , 20) , ('C' , 15) , ('D' , 5) , ('E' , 18) ]
m = map(lambda   x  :  x[1]  ,  a) # Extracts the second element (i.e., the numbers) from each tuple in list a.----> x[1] and x[0]------> 1st element here
while   True:
	try:
		print(next(m))
		time . sleep(1)
	except  StopIteration:
		break
output:-
------------
10
20
15
5
18

#15)Find  outputs (Home  work)
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
m1 = map(lambda  x  :  x['country'] , list) # map executes only for countries
print('Map   m1')
disp(m1)
m2 = map(lambda  x  :  x['sale']  , list) # map executes only for sales
print('Map   m2')
disp(m2)

output:-
--------
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


#16)Write  a  program  to  convert  each  celsius  temperature  of  the  list  to  farenheit  temperature

1) What  is  the  formula  to  convert  celsius  temperature  to  farenheit ?  --->   1.8 * celsius  temp + 32

2) Let  input  be   list  of  celsius  temperatures  such  as  [30 , 40 , 50 , 25]
    What  is  the  output ?  --->   1.8 * 30 + 32
							                      1.8 * 40 +32
								                  1.8 * 50 + 32
								                  1.8 * 25 + 32

import time
a =  [30 , 40 , 50 , 25]
m = map(lambda x : (1.8 *x +32), a)
while True:
	try:
		print(next(m))
		time . sleep(1)
	except  StopIteration:
		break
output:-
----------
86.0
104.0
122.0
77.0


#17)Enter  list  of  celsius  temperatures :  [10,20,15,18]
Farenheit   temperatures
50.0
68.0
59.0
64.4


import time
a =  eval(input("Enter  list  of  celsius  temperatures:"))
print('Farenheit   temperatures : ')
m = map(lambda x : (1.8 *x + 32), a)
while True:
	try:
		print(next(m))
		time . sleep(1)
	except  StopIteration:
		break

output:-
-----------
Enter  list  of  celsius  temperatures:[10,20,15,18]
Farenheit   temperatures :
50.0
68.0
59.0
64.4


#18 Write  a  program  to  print  2 ^ 0 , 2 ^ 1 , 2 ^ 2 , ....... 2 ^ 9  using  map   object (Home  work)
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

import time
a =  range(0,10)
print('power of 2 : ')
m = map(lambda x :  2 ** x , a)
while True:
	try:
		print(next(m))
		time . sleep(1)
	except  StopIteration:
		break
output:-
---------
power of 2 :
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

#19)Write  a  program  to  determine  area  of  circle  for  each  radius  in  the  list

1) What  is  area  of  circle ?  --->  pi * r * r

2) Let  input  be  [3.5 , 2.8 , 4.2  , 1.9]
    What  are  the  outputs ?  --->  Area  of  radius  3.5
						                              Area  of  radius  2.8
						                              Area  of  radius  4.2
						                              Area  of  radius  1.9
Enter  list  of  radii  :   [1,2,3,4]
Area  of  each  radius  in  the  list
3.14
12.57
28.27
50.27

import time
import math
a =  eval(input("Enter  list  of  radii:"))
print('Area  of  each  radius  in  the  list : ')
m = map(lambda x : math.pi *x *x, a)
while True:
	try:
		print(next(m))
		time . sleep(1)
	except  StopIteration:
		break
output:-
---------
Enter  list  of  radii:[1,2,3,4]
Area  of  each  radius  in  the  list :
3.141592653589793
12.566370614359172
28.274333882308138
50.26548245743669


#20)Write  a  program  to  add  two  tuples  of  difierent  sizes  and  store  the  results  in  3rd  tuple

Let  1st  tuple  be  (10 , 20 , 30 , 40)  and  2nd  tuple  be  (1 , 2 , 3 , 4 ,  5  ,  6)
What  is  the  3rd  tuple ?  --->  (10 + 1 , 20 + 2 , 30 + 3 , 40 + 4)   and  5  and 6  are  ignored

Enter  first  tuple :  (10,20,15,18)
Enter  second  tuple :  (30,40,35,12,100,200)
Addition  tuple  :   (40, 60, 50, 30)

import time

a =  eval(input("Enter  first  tuple "))
b =  eval(input("Enter  second  tuple "))
print('Addition  tuple  : ')
m = map(lambda x , y : x + y, a,b)
result = []
while True:
	try:
		result . append(next(m))
		time . sleep(1)
	except  StopIteration:
		break
print(tuple(result))

(or)
a =  eval(input("Enter  first  tuple "))
b =  eval(input("Enter  second  tuple "))
m = map(lambda x , y : x + y, a,b)
print('Addition tuple : ' , tuple(m)

output:-
----------
Enter  first  tuple (10,20,15,18)
Enter  second  tuple (30,40,35,12,100,200)
Addition  tuple  :
(40, 60, 50, 30)


#21)Write  a  program  to  multiply  two  lists  and  store  results  in  3rd  list

Let  1st  list  be  [10 , 20 , 15 , 18 , 19 , 17]  and  2nd  list  be  [1 , 5 , 3 , 2]
What  is  the  3rd  list ?  ---> [10 * 1 , 20 * 5 , 15 * 3 , 18 * 2]  and  ignores  19  and  17

Hint:  Use  map

Enter  first  list :  [10,20,15,18]
Enter  second  list :  [1,2,3,4]
Multiplication  list :   [10, 40, 45, 72]


import time

a =  eval(input("Enter  first  list "))
b =  eval(input("Enter  second  list "))
print('Multiplication  list  : ')
m = map(lambda x , y : x * y, a,b)
result = []
while True:
	try:
		result . append(next(m))
		time . sleep(1)
	except  StopIteration:
		break
print(list(result))

output:-
--------
Enter  first  list [10,20,15,18]
Enter  second  list [1,2,3,4]
Multiplication  list  :
[10, 40, 45, 72]


#22)filter  inside  map
import  time
a = [10 , 20 , 15 , 12 , 18 , 5 , 14 , 25 , 17]
m = map(lambda  y  :   y + y ,  filter(lambda  x  :  x >= 15 , a)) # map executes addition only for elements >= 15.
while   True:
	try:
		print(next(m))
		time . sleep(1)
	except:
		break

output:-
---------
40
30
36
50
34


#23) map  inside  filter (Home  work)
import   time
a = [10 , 20 , 15 , 12 , 18 , 5 , 14 , 25 , 17]
f = filter(lambda  y  :   y  % 2 == 0 , map (lambda  x : x ** 2 , a)) # filter  executes multiplication only for elements which are even numbers.
while   True:
	try:
		print(next(f))
		time . sleep(1)
	except:
		break
output:-
----------
100
400
144
324
196

#24)Write  a  program  to  determine  largest  element  of  the  list  with  reduce()  function

Let  list   be  [10 , 20 , 15 , 30 , 25 , 40 , 35]
What  is   the  largest  element  of  list ?  ---> 40

Hint:  Use  reduce()  function

Enter list of numbers (or) strings:[10 , 20 , 15 , 30 , 25 , 40 , 35]
Largest  element  :    40


from functools import reduce
a =  eval(input("Enter list of numbers (or) strings "))
print('Largest  element  : ')
result = reduce(lambda x , y : x if x > y else y , a)
print(result)

'''
#25)Find  outputs  (Home  work)
from  functools  import  reduce
a = [ 10 , 20 , 15 , 5 , 12 , 18 , 25 , 14]
ans = reduce( lambda  x , y  : x + y , map(lambda  y :  y ** 2 , filter(lambda  x  :  x  >= 15 , a))) # from right to left opertions performs.
# Keeps numbers in the list a that are greater than or equal to 15 and Squares those filtered numbers abd then Sums all the squared values here.


print(ans)

output:-
-----------
1574

filter(lambda x: x >= 15, a) ? [20, 15, 18, 25]

Squared ? [400, 225, 324, 625]

Sum ? 400 + 225 + 324 + 625 = 1574