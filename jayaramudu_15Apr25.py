#Ex-1
# Find  outputs (Home  work)
import  time
a = [25 , 10.8 , 3 + 4j , 'Hyd' , False]
f = filter(lambda   x :   True ,   a) # creating empty filter
while  True:
	try:
		print(next(f)) #   Get the next element from the filter iterator 25 <nl> 10.8 <nl> (3+4j) <nl> Hyd <nl> False
		time . sleep(1)
	except:
		break

#Ex-2
#  Find  outputs (Home  work)
import  time
a = [25 , 10.8 , 3 + 4j ,  'Hyd' , True]
f = filter(lambda  x  :  False ,  a) # lambda condition is False so no elements will pass the filter
while  True:
	try:
		print(next(f))
		time . sleep(1)
	except:
		break

#Ex-3
# Find  outputs (Home  work)
import  time
a = [25 , 10.8 , False ,  3 + 4j , 0 , 'Hyd' , '' , (25,)  ,  () ]
f = filter(lambda   x   :   x   ,   a) # lambda function yielded non-zero elements
while  True:
	try:
		print(next(f)) # Get the next element  from filter  iterator # 25 <nl> 10.8 <nl> 3+4j <nl> Hyd <nl> (25,)
		time . sleep(1)
	except:
		break

#Ex-4
# Find outputs
import  time
def  disp(f):
	while  True:
		try:
			print(next(f))
			time . sleep(1)
		except:
			break
list = [10 , 0 ,  -25 , () , (25,) , 'Hyd', '' , [] , 10.8 , 0.0 , [10 , 20] , True , False] # list contains mixed data
f1 = filter(lambda  x : None  , list) # filter yielded  no elements because lambda function    lambda  x : None
print('Filter  f1') # Filter  f1
disp(f1) # call disp function and pass filter f1
f2 = filter(None  , list) # lambda function yielded non zero elements 10 <nl> -25 <nl> (25,) , Hyd <nl> 10.8 <nl> [10,20] <nl> True
print('Filter f2')
disp(f2)

#Ex-5
# Find outputs  (Home  work)
import  time
a = ['Rama Rao' , 'Sita' , 'Rajesh' , 'Kiran' , 'Amar' , 'Manohar' , 'Vamsi']
f = filter(lambda  x  :   len(x) >= 5  , a) # filter iterator list and yielded elements condition is satisfied
while   True:
	try:
		print(next(f)) # get the next element of filter iterator  Rama Rao <nl> Rajesh <nl> Kiran <nl> Manohar <nl> Vamsi
		time . sleep(1)
	except:
		break

#Ex-6
# Find  outputs (Home  work)
import   time
list=[('A' , 10) , ('B' , 20) , ('C' , 15) , ('D' , 5) , ('E' , 18)]
f = filter(lambda   x  :   x[1]  >=  12 , list) # filter iterator check lambda condition is true yielded the element
while   True:
	try:
		print(next(f)) # get the next element from filter iterator ('B', 20) <nl> ('C', 15)  <nl> ('E', 18)
		time . sleep(1)
	except:
		break

#Ex-7
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
f = filter(lambda  x :  x['Marks'] >= 60 , list) # create empty filter and when call the next element filter it will check lambda condition each element of list and condition is true yielded element
while   True:
    try:
        print(next(f)) # get the element of filter iterator
        time.sleep(1)
    except:
        break

'''
'Roll Num': 10, 'Stud Name': 'Rama Rao', 'Marks': 75}
{'Roll Num': 15, 'Stud Name': 'Kiran', 'Marks': 65}
{'Roll Num': 5, 'Stud Name': 'Rajesh', 'Marks': 82}
'''

#Ex-8
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
f1 = filter (lambda  x  :   x['country'] . startswith('U') , a) #  create empty filter and when call the next element filter it will check lambda condition each element of list and country start with U
print('Filter  f1') #  Filter  f1
disp(f1)
f2 = filter(lambda  x  :  x['sale']  >=  200  , a) # create empty filter and when call the next element filter it will check lambda condition each element of list and sale > 200
print('Filter f2') #  Filter f2
disp(f2)

'''
Filter  f1
{'country': 'USA', 'sale': 300.3}
{'country': 'UK', 'sale': 210.4}
Filter f2
{'country': 'china', 'sale': 200.2}
{'country': 'USA', 'sale': 300.3}
{'country': 'UK', 'sale': 210.4}

'''

#Ex-9
# How  to  print  fliter  object  in  different  ways ?
import   time
a = [10 , 15 , 20 , 17 , 18 , 19 , 26]
f = filter(lambda  x  :  x  %  2  ==  0 , a)
print('Iterate  filter  object  with   next   function')
while True: # How  to iterate  filter  object  with  next()  function
    try:
        print(next(f))
    except:
        break

print('Iterate  filter  object  with   for  loop')
for x in filter(lambda  x  :  x  %  2  ==  0 , a): # How  to iterate  filter  object  with  for  loop
    print(x)

print('Unpacking  filter  object :  ' , *filter(lambda  x  :  x  %  2  ==  0 , a)) #  How  to  unpack  filter  object)
print()
print('filter  object  in  the  form  of  list  :  ' , list(filter(lambda  x  :  x  %  2  ==  0 , a))) # How  to  convert  filter  object  to list)

#Ex-10
'''
#  Write  a  program  to  print  odd  numbers  between  1  and  20  with  filter iterator
'''

f = filter(lambda x: x % 2 == 1, range(1,21))
for x in f:
    print(x)


#Ex-11
'''
Write  a  program  to  print  distinct  vowels  of  the  string  using  filter.
Input  is  string  and  output  is set
'''
def distinct(s):
    out=''
    for x in s:
        if x in 'AEIOU':
            if x not in out:
                out +=x
            return x
s = input("Enter any String ")
f = set(filter(distinct,s.upper()))
print(f)

'''
s = input("Enter any String: ")
vowels = set(filter(lambda x: x.upper() in {'A', 'E', 'I', 'O', 'U'}, s))
print(vowels)
'''

#Ex-12
# Nested  filter  i.e.  filter  on  filter
import   time
list =  [ (10 , 'Rama' , 10000.0) ,
            (20, 'Sita' , 7000.0) ,
            (15 , 'Rajesh' , 15000.0) ,
            (5 , 'Amar' ,  12000.0) ,
            (18 , 'Ramesh' , 8000.0) ]
f = filter(lambda  x :  x[1] . startswith('R')  , filter(lambda  x :  x[2] >= 10000 , list)) # create empty filter and inside the filter check condition each tuple of list tuple of second element of each tuple start with R and third element each tuple of
while   True:
	try:
		print(next(f)) # get  next tuple of filter iterator # (10, 'Rama', 10000.0) <nl>  (15, 'Rajesh', 15000.0)
		time .  sleep(1)
	except:
		break

#Ex-13
#  Modify  following  program  with  regular  function  and  for  loop
import  time
a = [10 , 20 , 15 , 18 , 5]
def m1(x):
	return x * x
m = map(m1 ,  a) # create empty map and map multiply iterate each element of list give new one when call
print(type(m)) # class map
print(m) # type and address
for x in m:
	print(x)
	time.sleep(0.5)

# while True:
# 	try:
# 		print(next(m)) # get the next element of map # 100 <nl> 400 <nl> 225 <nl> 324 <nl> 25
# 		time . sleep(1)
# 	except:
# 		break


#Ex-14
# Find  outputs (Home  work)
import  time
a = [ ('A' , 10) , ('B' , 20) , ('C' , 15) , ('D' , 5) , ('E' , 18) ]
m = map(lambda   x  :  x[1]  ,  a) # map operation extracts the second element  from each tuple
while   True:
	try:
		print(next(m)) # get the next element of map 10 <n> 20 <nl> 15 <nl> 5 <nl> 18
		time . sleep(1)
	except  StopIteration:
		break

#Ex-15
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
m1 = map(lambda  x  :  x['country'] , list) # map iterate each dictionary of a list and return a value of key country
print('Map   m1') # Map   m1
disp(m1) # <India> <nl> China <nl> USA <nl> UK
m2 = map(lambda  x  :  x['sale']  , list) #  map iterate each dictionary of a list and return a value of sale (key)
print('Map m2') # Map m2
disp(m2) # 150.5 <nl> 200.2 <nl> 300.3 <nl> 210.4


#Ex-16
'''
Write  a  program  to  convert  each  celsius  temperature  of  the  list  to  farenheit  temperature

1) What  is  the  formula  to  convert  celsius  temperature  to  farenheit ?  --->   1.8 * celsius  temp + 32

2) Let  input  be   list  of  celsius  temperatures  such  as  [30 , 40 , 50 , 25]
    What  is  the  output ?  --->                 1.8 * 30 + 32
							                      1.8 * 40 +32
								                  1.8 * 50 + 32
								                  1.8 * 25 + 32
'''
import time

l = eval(input('Enter  list  of  celsius  temperatures : '))
m = map(lambda x: 1.8 * x + 32,l)
for x in m:
    print(x)
    time.sleep(1)

#Ex-17
# Write  a  program  to  print  2 ^ 0 , 2 ^ 1 , 2 ^ 2 , ....... 2 ^ 9  using  map   object (Home work)
import time

n=int(input('Powers  of  : '))
def m1(x,y):
    return pow(x,y)
p=range(10)

m = map(lambda  y: m1(n,y),p)
for x in m:
    print(x)
    time.sleep(1)

#Ex-18
'''
Write  a  program  to  determine  area  of  circle  for  each  radius  in  the  list

1) What  is  area  of  circle ?  --->  pi * r * r

2) Let  input  be  [3.5 , 2.8 , 4.2  , 1.9]
    What  are  the  outputs ?  --->  Area  of  radius  3.5
						                              Area  of  radius  2.8
						                              Area  of  radius  4.2
						                              Area  of  radius 1.9
'''
import time
from math import pi
l= eval(input('Enter  list  of  radii  : '))
def area(x):
    return pi * x * x
m= map(area,l)
print('Area  of  each  radius  in  the  list')
for x in m:
    print(f'{x:.2f}')
    time.sleep(1)


#Ex-19
'''
Write  a  program  to  add  two  tuples  of  difierent  sizes  and  store  the  results  in  3rd  tuple

Let  1st  tuple  be  (10 , 20 , 30 , 40)  and  2nd  tuple  be  (1 , 2 , 3 , 4 ,  5  ,  6)
What  is  the  3rd  tuple ?  --->  (10 + 1 , 20 + 2 , 30 + 3 , 40 + 4)   and  5  and 6  are ignored
'''
import time

t1 = eval(input('Enter first tuple : '))
t2 = eval(input("Enter second tuple : "))
m = map(lambda x,y:x+y,t1,t2)
for x in m:
    print(x)
    time.sleep(1)

#Ex-20
'''
Write  a  program  to  multiply  two  lists  and  store  results  in  3rd  list

Let  1st  list  be  [10 , 20 , 15 , 18 , 19 , 17]  and  2nd  list  be  [1 , 5 , 3 , 2]
What  is  the  3rd  list ?  ---> [10 * 1 , 20 * 5 , 15 * 3 , 18 * 2]  and  ignores  19  and  17

Hint: Use map
'''

l1 = eval(input('Enter first list : '))
l2 = eval(input("Enter second list : "))
l3=[]
m = map (lambda x,y: x*y,l1,l2)
for x in m:
    l3.append(x)
print(l3)


#Ex-21
# filter  inside  map
import  time
a = [10 , 20 , 15 , 12 , 18 , 5 , 14 , 25 , 17]
m = map(lambda  y  :   y + y ,  filter(lambda  x  :  x >= 15 , a)) # create empty map and when call map iterate on each element of list and check filter condition ,it is yielded element
while   True:
	try:
		print(next(m)) # get the next element of  m 40 <nl> 30 <nl> 36 <nl> 50 <nl> 34
		time . sleep(1)
	except:
		break

#Ex-22
# map  inside  filter (Home  work)
import   time
a = [10 , 20 , 15 , 12 , 18 , 5 , 14 , 25 , 17]
f = filter(lambda  y  :   y  % 2 == 0 , map (lambda  x : x ** 2 , a)) # Filters the squared values, keeping only those that are even
while   True:
	try:
		print(next(f)) # get the next element filter iterator
		time . sleep(1)
	except:
		break

#Ex-23
'''
Write  a  program  to  determine  largest  element  of  the  list  with  reduce()  function

Let  list   be  [10 , 20 , 15 , 30 , 25 , 40 , 35]
What  is   the  largest  element  of  list ?  ---> 40

Hint:  Use  reduce() function
'''
from functools import reduce

l1 = eval(input('Enter list of numbers (or) strings : '))
res = reduce(lambda x ,y: x if x>y else y,l1)
print('Largest  element :  ',res)

