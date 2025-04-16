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

'''
25
10.8
3+4j
hyd
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
25
10.8
3+4j
hyd
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
'''
Fliter F1
'''
f2 = filter(None  , list)
print('Filter  f2')
disp(f2)
'''
Fliter f2
10
-25
(25,)
hyd
10.8
[10,20]
True
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
Rama Rao
Rajesh
Kiran
Manohar
vamsi
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
(B,20)
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
        ]  
#  List  of  dictionaries
f = filter(lambda  x :  x['Marks'] >= 60 , list)
while   True:
	try:
		print(next(f))
		time . sleep(1)
	except:
		break
'''
{'Roll Num' :  10 ,'Stud Name' : 'Rama Rao' ,'Marks' : 75} 
{'Roll Num' :  15 ,'Stud Name' : 'Kiran' ,'Marks' : 65}
{'Roll Num' :  5 ,'Stud Name' : 'Rajesh' ,'Marks' : 82}

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
'''
Filter  f1
{ 'country' : 'USA' , 'sale' : 300.3} 
{ 'country' : 'UK' , 'sale' : 210.4} 
'''
f2 = filter(lambda  x  :  x['sale']  >=  200  , a)
print('Filter  f2')
disp(f2)
'''
Filter  f2
{ 'country' : 'china' , 'sale' : 200.2} 
{ 'country' : 'USA' , 'sale' : 300.3} 
{ 'country' : 'UK' , 'sale' : 210.4} 
'''
# How  to  print  fliter  object  in  different  ways ?
import   time
a = [10 , 15 , 20 , 17 , 18 , 19 , 26]
f = filter(lambda  x  :  x  %  2  ==  0 , a)
#print('Iterate  filter  object  with   next   function')
while True:
	try:
		print(next(f))
		time.sleep(0.5)
	except:
		break
#How  to iterate  filter  object  with  next()  function
print('Iterate  filter  object  with   for  loop')
for y in filter(lambda  x  :  x  %  2  ==  0 , a):
	print(y)
#How  to iterate  filter  object  with  for  loop
print('Unpacking  filter  object :  ' ,  *filter(lambda  x  :  x  %  2  ==  0 , a))
print()

z=list(filter(lambda x:x%2==0 ,a))
print('filter  object  in  the  form  of  list  :  ',z )

# Odd  numbers  between  1  and  20
#  Write  a  program  to  print  odd  numbers  between  1  and  20  with  filter  iterator
print("Odd numbers between 1 to 20 ")
f=filter(lambda x: x % 2!=0 ,range(20))
for y in f:
    print(y)


#Write  a  program  to  print  distinct  vowels  of  the  string  using  filter.

n=input("Enter a string :").upper()
vowel=['A','E','I','O','U']
f=filter(lambda x:x in vowel,n)
distinct=set(f)
print(distinct)


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
(10 , 'Rama' , 10000.0) 
(15 , 'Rajesh' , 15000.0)

'''
#  Modify  following  program  with  regular  function  and  for  loop
import  time
def mul(x):
	return x*x
a = [10 , 20 , 15 , 18 , 5]
m = map(mul,  a)
print(type(m))
print(m)
while  True:
	try:
		print(next(m))
		time . sleep(1)
	except:
		break
'''
<class 'map'>
type and address
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
'''
Map m1
India
China
USA
UK
'''
m2 = map(lambda  x  :  x['sale']  , list)
print('Map   m2')
disp(m2)
'''
map m2
150.0
200.2
300.3
210.4
'''
# Write  a  program  to  print  2 ^ 0 , 2 ^ 1 , 2 ^ 2 , ....... 2 ^ 9  using  map   object
f=map(lambda x: 2**x,range(10))
print('Power of 2')
for y in f:
    print(y)


#Write  a  program  to  determine  area  of  circle  for  each  radius  in  the  list
import math
n=eval(input("Enter list of radii : "))
f=map(lambda x: math.pi*x*x,n)
for y in f:
    print("Area if a circle: ",y)

#Write  a  program  to  convert  each  celsius  temperature  of  the  list  to  farenheit  temperature
n=eval(input("Enter list : "))
f=map(lambda x: 1.8*x + 32,n)
for y in f:
    print(y)

#Write  a  program  to  add  two  tuples  of  difierent  sizes  and  store  the  results  in  3rd  tuple
m=eval(input("Enter a first tuple : "))
n=eval(input("Enter a second tuple : "))
f=tuple(map(lambda x,y:x+y,m,n))
print("Addittion tuple :",f)

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
100
400
144
324
196
'''
#Write  a  program  to  determine  largest  element  of  the  list  with  reduce()  function
from  functools  import  reduce
n=eval(input("Enter list : "))
ans=reduce(lambda x,y:x if x>y else y,n)
print("largest element :",ans)

# Find  outputs  (Home  work)
from  functools  import  reduce
a = [ 10 , 20 , 15 , 5 , 12 , 18 , 25 , 14]
ans = reduce( lambda  x , y  : x + y , map(lambda  y :  y ** 2 , filter(lambda  x  :  x  >= 15 , a)))
print(ans)
'''
1574
'''
"""
