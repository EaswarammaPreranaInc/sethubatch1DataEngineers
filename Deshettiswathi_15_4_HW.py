Q1 #Find  outputs (Home  work)
import  time
a = [25 , 10.8 , 3 + 4j , 'Hyd' , False]
f = filter(lambda   x :   True ,   a)
while  True:
	try:
		print(next(f))  #25 <\n>  10.8 <\n>  (3+4j) <\n>  Hyd <\n> False
		time . sleep(1)
	except:
		break
#-----------------------------------------------------------------------------
Q2 #Find  outputs (Home  work)

import  time
a = [25 , 10.8 , 3 + 4j ,  'Hyd' , True]
f = filter(lambda  x  :  False ,  a)
while  True:
	try:
		print(next(f))  #nothing is printed because condition is false
		time . sleep(1)
	except:
		break
#---------------------------------------------------------------------------
Q3 # Find  outputs (Home  work)

import  time
a = [25 , 10.8 , False ,  3 + 4j , 0 , 'Hyd' , '' , (25,)  ,  () ]
f = filter(lambda   x   :   x   ,   a)
while  True:
	try:
		print(next(f))   #25 <\n> 10.8 <\n> (3+4j) <\n> Hyd <\n> (25,)
		time . sleep(1)
	except:
		break
#----------------------------------------------------------------------------------
Q4 # Find outputs

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
print('Filter  f1')  #Filter f1
disp(f1)             #prints nothing because f1 returns None 
f2 = filter(None  , list)  # treats as f2 = filter(lambda x: x,list)
print('Filter  f2')  #Filter f2
disp(f2)             #10 <\n> -25 <\n> (25,) <\n>  Hyd <\n> 10.8 <\n> [10,20] <\n> True 
#-------------------------------------------------------------------------------------------
Q5 # Find outputs  

import  time
a = ['Rama Rao' , 'Sita' , 'Rajesh' , 'Kiran' , 'Amar' , 'Manohar' , 'Vamsi']
f = filter(lambda  x  :   len(x) >= 5  , a)
while   True:
	try:
		print(next(f))   #Rama Rao <\n>  Rajesh <\n> Kiran <\n> Manohar <\n> Vamsi
		time . sleep(1)
	except:
		break
#--------------------------------------------------------------------------------------
Q6 # Find  outputs (Home  work)

import   time
list=[('A' , 10) , ('B' , 20) , ('C' , 15) , ('D' , 5) , ('E' , 18)]
f = filter(lambda   x  :   x[1]  >=  12 , list)
while   True:
	try:
		print(next(f))  #('B' , 20) <\n> ('C' , 15) <\n> ('E' , 18)
		time . sleep(1)
	except:
		break
#-------------------------------------------------------------------------------
Q7 # Find  outputs (Home  work)

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

OP-
{'Roll Num': 10, 'Stud Name': 'Rama Rao', 'Marks': 75}
{'Roll Num': 15, 'Stud Name': 'Kiran', 'Marks': 65}
{'Roll Num': 5, 'Stud Name': 'Rajesh', 'Marks': 82}
#---------------------------------------------------------------------
Q8 # Find  outputs

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

OP-
Filter  f1
{'country': 'USA', 'sale': 300.3}
{'country': 'UK', 'sale': 210.4}
Filter  f2
{'country': 'china', 'sale': 200.2}
{'country': 'USA', 'sale': 300.3}
{'country': 'UK', 'sale': 210.4}
#_-----------------------------------------------------------------------------------------
Q9 # How  to  print  fliter  object  in  different  ways ?

import   time
a = [10 , 15 , 20 , 17 , 18 , 19 , 26]
f = filter(lambda  x  :  x  %  2  ==  0 , a)
print('Iterate  filter  object  with   next   function')
while True: 
	try: 
		print(next(f))  #How  to iterate  filter  object  with  next()  function
		time.sleep(1)
	except:
		break
print('Iterate  filter  object  with   for  loop')
f = filter(lambda  x  :  x  %  2  ==  0 , a)
for x in f:  
	print(x)   #How  to iterate  filter  object  with  for  loop
	time.sleep(1)
f = filter(lambda  x  :  x  %  2  ==  0 , a)
print('Unpacking  filter  object :  ' , *f )   #How  to  unpack  filter  object
print()
f = filter(lambda  x  :  x  %  2  ==  0 , a)
print('filter  object  in  the  form  of  list  :  ' ,list(f) )   #How  to  convert  filter  object  to  list

OP-
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
#--------------------------------------------------------------------------------------------------
Q10  #  Write  a  program  to  print  odd  numbers  between  1  and  20  with  filter  iterator

import time
print('Odd numbers between 1 and 20:')
for x in filter(lambda x: x%2 == 1,range(20)):
	print(x)
	time.sleep(1)

OP-
Odd numbers between 1 and 20:
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
#-----------------------------------------------------------------------------------------------------
Q11 #Write  a  program  to  print  distinct  vowels  of  the  string  using  filter. Input  is  string  and  output  is  set

a=input('Enter mixed case string: ')
a=a.upper()
f=filter(lambda ch: ch in 'AEIOU',a)
print(set(f))

OP-
Enter mixed case string: Priyanka
{'I', 'A'}
#-------------------------------------------------------------------------------------------------------
Q12 #Nested  filter  i.e.  filter  on  filter

import   time
list =  [ (10 , 'Rama' , 10000.0) ,
            (20, 'Sita' , 7000.0) ,
            (15 , 'Rajesh' , 15000.0) ,
            (5 , 'Amar' ,  12000.0) ,
            (18 , 'Ramesh' , 8000.0) ]
f = filter(lambda  x :  x[1] . startswith('R')  , filter(lambda  x :  x[2] >= 10000 , list))
while   True:
	try:
		print(next(f))  #(10, 'Rama', 10000.0) <\n> (15, 'Rajesh', 15000.0)
		time .  sleep(1)
	except:
		break
#------------------------------------------------------------------------------------------------------
Q13 #Modify  following  program  with  regular  function  and  for  loop

#import  time
#a = [10 , 20 , 15 , 18 , 5]
#m = map(lambda  x :  x  *  x ,  a)
#print(type(m))
#print(m)
#while   True
#	try:
#		print(next(m))
#		time . sleep(1)
#	except:
#		break

#with regular function
import time
def square(x):
	return x*x
a = [10 , 20 , 15 , 18 , 5]
m=map(square,a)
print(type(m))
print(m)
for x in m:
	print(x)
	time.sleep(1)

OP-
<class 'map'>
<map object at 0x00000206558DBF10>
100
400
225
324
25
#-------------------------------------------------------------------------------------------
Q14 #Find  outputs (Home  work)

import  time
a = [ ('A' , 10) , ('B' , 20) , ('C' , 15) , ('D' , 5) , ('E' , 18) ]
m = map(lambda   x  :  x[1]  ,  a)
while   True:
	try:
		print(next(m))    #10 <\n> 20 <\n> 15 <\n> 5 <\n> 18
		time . sleep(1)
	except  StopIteration:
		break
#_-------------------------------------------------------------------------------------------
Q15 # Find  outputs (Home  work)

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
print('Map   m1')  #Map m1
disp(m1)           # India China USA UK
m2 = map(lambda  x  :  x['sale']  , list)
print('Map   m2')  #Map m2
disp(m2)           #150.5 200.2 300.3 210.4
#_------------------------------------------------------------------------------------------------
Q16 #Write  a  program  to  convert  each  celsius  temperature  of  the  list  to  farenheit  temperature
What  is  the  formula  to  convert  celsius  temperature  to  farenheit ?  --->   1.8 * celsius  temp + 32

import time
a=eval(input('Enter list of celsius temperatures : '))
f=map(lambda x: 1.8*x+32,a)
print('Farenheit temperatures')
for y in f:
	print(y)
	time.sleep(1)

OP-
Enter  list  of  celsius  temperatures :  [10,20,15,18]
Farenheit   temperatures
50.0
68.0
59.0
64.4
#---------------------------------------------------------------------------------------------------------------
Q17  # Write  a  program  to  print  2 ^ 0 , 2 ^ 1 , 2 ^ 2 , ....... 2 ^ 9  using  map   object (Home  work)

import time
f=map(lambda x: 2**x,range(10))
print('Powers of 2')
for y in f:
	print(y)
	time.sleep(1)

OP-
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
#---------------------------------------------------------------------------------------------------------
Q18 Write  a  program  to  determine  area  of  circle  for  each  radius  in  the  list

import time,math
a = eval(input('Enter list of radii : '))
m=map(lambda x: math.pi*x**2,a)
print('Area of each radius in the list')
for y in m:
	print(f'{y:.2f}')
	time.sleep(1)

OP-
Enter list of radii :  [1,2,3,4]
Area of each radius in the list
3.14
12.57
28.27
50.27
#---------------------------------------------------------------------------------------------------------
Q19 Write  a  program  to  add  two  tuples  of  difierent  sizes  and  store  the  results  in  3rd  tuple

a=eval(input('Enter first tuple : '))
b=eval(input('Enter second tuple : '))
m=map(lambda x,y: x+y,a,b)
print('Addition tuple : ',tuple(m))

OP-
Enter first tuple : (10,20,15,18)
Enter second tuple : (30,40,35,12,100,200)
Addition tuple :  (40, 60, 50, 30)
#_------------------------------------------------------------------------------------------------------
Q20 Write  a  program  to  multiply  two  lists  and  store  results  in  3rd  list

a=eval(input('Enter first list : '))
b=eval(input('Enter second list : '))
m=map(lambda x,y: x*y,a,b)
print('Addition tuple : ',list(m))

OP-
Enter first list : [10,20,15,18]
Enter second list : [1,2,3,4]
Addition tuple :  [10, 40, 45, 72]
#-------------------------------------------------------------------------------------------------
Q21 # filter  inside  map

import  time
a = [10 , 20 , 15 , 12 , 18 , 5 , 14 , 25 , 17]
m = map(lambda  y  :   y + y ,  filter(lambda  x  :  x >= 15 , a))
while   True:
	try:
		print(next(m)) #40 <\n> 30 <\n> 36 <\n> 50 <\n> 34
		time . sleep(1)
	except:
		break
#-----------------------------------------------------------------------------------
Q22 # map  inside  filter (Home  work)

import   time
a = [10 , 20 , 15 , 12 , 18 , 5 , 14 , 25 , 17]
f = filter(lambda  y  :   y  % 2 == 0 , map (lambda  x : x ** 2 , a))
while   True:
	try:
		print(next(f))  #100 <\n> 400 <\n> 144 <\n> 324 <\n> 196
		time . sleep(1)
	except:
		break
#---------------------------------------------------------------------------------------------
Q23 Write  a  program  to  determine  largest  element  of  the  list  with  reduce()  function

from functools import reduce
a=eval(input('Enter list of numbers (or) strings: '))
x=reduce(lambda x,y: max(x,y),a)
print('Largest element: ',x)

OP-
Enter list of numbers (or) strings: ['PRIYA','SWATHI','SOWMYA','TANMAI']
Largest element:  TANMAI
#-------------------------------------------------------------------------------------------------------
Q24 # Find  outputs  (Home  work)

from  functools  import  reduce
a = [ 10 , 20 , 15 , 5 , 12 , 18 , 25 , 14]
ans = reduce( lambda  x , y  : x + y , map(lambda  y :  y ** 2 , filter(lambda  x  :  x  >= 15 , a)))
print(ans)  #1574
