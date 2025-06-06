

#1. Find  outputs (Home  work)

'''
import  time
a = [25 , 10.8 , 3 + 4j , 'Hyd' , False]
f = filter(lambda   x :   True ,   a)
while  True:
	try:
		print(next(f)) #25   10.8   (3 + 4j)  Hyd False
		time . sleep(1)
	except:
		break
		
'''


#2. Find  outputs (Home  work)
'''
import  time
a = [25 , 10.8 , 3 + 4j ,  'Hyd' , True]
f = filter(lambda  x  :  False ,  a)
while  True:
	try:
		print(next(f)) #SIE 
		time . sleep(1)
	except:
		break
		
'''


#3.Find  outputs (Home  work)
'''
import  time
a = [25 , 10.8 , False ,  3 + 4j , 0 , 'Hyd' , '' , (25,)  ,  () ]
f = filter(lambda   x   :   x   ,   a)
while  True:
	try:
		print(next(f)) #25  10.8  (3 + 4j)  Hyd  (25,) 
		time . sleep(1)
	except:
		break
'''


#4. Find outputs

'''
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
print('Filter  f1') #Filter f1 
disp(f1) # No output 
f2 = filter(None , list)
print('Filter  f2') #Filter f2 
disp(f2) #10 -25 (25,) Hyd 10.8 [10,20] True 
'''



#5. Find outputs  (Home  work)

'''
import  time
a = ['Rama Rao' , 'Sita' , 'Rajesh' , 'Kiran' , 'Amar' , 'Manohar' , 'Vamsi']
f = filter(lambda  x  :   len(x) >= 5  , a)
while   True:
	try:
		print(next(f)) #Rama Rao Rajesh Kiran Manohar Vamsi
		time . sleep(1)
	except:
		break
'''

#6.Find  outputs (Home  work)

'''
import   time
list=[('A' , 10) , ('B' , 20) , ('C' , 15) , ('D' , 5) , ('E' , 18)]
f = filter(lambda   x  :   x[1]  >=  12 , list)
while   True:
	try:
		print(next(f)) #('B',20) ('C' , 15) ('E' , 18)
		time . sleep(1)
	except:
		break
		
'''


#7. Find  outputs (Home  work)
"""
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
		'''
		 {'Roll Num' :  10 ,'Stud Name' : 'Rama Rao' ,'Marks' : 75}
		 {'Roll Num'  :  15 ,'Stud Name' : 'Kiran' ,'Marks' : 65}
		 {'Roll Num' :  5 , 'Stud Name' : 'Rajesh' ,'Marks' : 82}
		'''
		time . sleep(1)
	except:
		break
		
"""

#8.Find  outputs (Home  work)

"""
import  time
def  disp(f):
	while  True:
		try:
			print(next(f))
			time . sleep(1)
		except:
			break
a = [   { 'country' : 'India' , 'sale' : 150.5} ,
          { 'country' : 'china' , 'sale' : 200.2} ,
          { 'country' : 'USA' , 'sale' : 300.3} ,
          { 'country' : 'UK' , 'sale' : 210.4} ]
f1 = filter (lambda  x  :   x['country'] . startswith('U') , a)
print('Filter  f1') #Filter  f1
disp(f1)
'''
{ 'country' : 'USA' , 'sale' : 300.3} 
{ 'country' : 'UK' , 'sale' : 210.4}

'''
f2 = filter(lambda  x  :  x['sale']  >=  200  , a)
print('Filter  f2') #Filter  f2
disp(f2)
'''
 { 'country' : 'china' , 'sale' : 200.2} 
 { 'country' : 'USA' , 'sale' : 300.3} 
 { 'country' : 'UK' , 'sale' : 210.4}
'''

"""


#9. How  to  print  fliter  object  in  different  ways ?
'''
import   time
a = [10 , 15 , 20 , 17 , 18 , 19 , 26]
f = filter(lambda  x  :  x  %  2  ==  0 , a)
print('Iterate  filter  object  with   next   function')
while(True):
    try:
        print(next(f)) #How  to iterate  filter  object  with  next()  function
        time.sleep(1)
        
    except:
        break 
    
print('Iterate  filter  object  with   for  loop')
for i in filter(lambda  x  :  x  %  2  ==  0 , a):
    print(i) #How  to iterate  filter  object  with  for  loop
    time.sleep(1)
    
print('Unpacking  filter  object :  ' , *filter(lambda  x  :  x  %  2  ==  0 , a)) # How  to  unpack  filter  object
print()

print('filter  object  in  the  form  of  list  :  ' ,list(filter(lambda  x  :  x  %  2  ==  0 , a)))
# How  to  convert  filter  object  to  list

'''

'''
# 10.Write  a  program  to  print  odd  numbers  between  1  and  20  with  filter  iterator
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
'''

'''
from time import sleep
f= filter(lambda x:x%2==1,range(1,21))

print("Odd  numbers  between  1  and  20")
for i in f:
    print(i)
    sleep(1)
'''


'''
#11. Write  a  program  to  print  distinct  vowels  of  the  string  using  filter.
Input  is  string  and  output  is  set

Enter  mixed  case   string  :  RamA raO
{'O', 'A'}
'''

'''
s=input("Enter  mixed  case   string  : ").upper()
f=filter(lambda x: x in "AEIOU" ,s)
S=set()

for i in f:
    S.add(i)
    
print(S)
'''


#12. Nested  filter  i.e.  filter  on  filter
'''
import   time
list =  [ (10 , 'Rama' , 10000.0) ,
            (20, 'Sita' , 7000.0) ,
            (15 , 'Rajesh' , 15000.0) ,
            (5 , 'Amar' ,  12000.0) ,
            (18 , 'Ramesh' , 8000.0) ]
f = filter(lambda  x :  x[1] . startswith('R')  , filter(lambda  x :  x[2] >= 10000 , list))
while   True:
	try:
		print(next(f)) # (10 , 'Rama' , 10000.0) (15 , 'Rajesh' , 15000.0)
		time .  sleep(1)
	except:
		break
		
'''

#13. Modify  following  program  with  regular  function  and  for  loop
'''
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
    
'''

#14. Find  outputs (Home  work)
'''
import  time
a = [ ('A' , 10) , ('B' , 20) , ('C' , 15) , ('D' , 5) , ('E' , 18) ]
m = map(lambda   x  :  x[1]  ,  a)
while   True:
	try:
		print(next(m)) # 10 20 15 5 18 
		time . sleep(1)
	except  StopIteration:
		break
    
'''


#15. Find  outputs (Home  work)
'''
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
print('Map   m1') #Map m1 
disp(m1) # India China USA UK 
m2 = map(lambda  x  :  x['sale']  , list)
print('Map   m2') #Map m2 
disp(m2) # 150.5 200.2 300.3 210.4 

'''


'''
#16. Write  a  program  to  convert  each  celsius  temperature  of  the  list  to  farenheit  temperature

1) What  is  the  formula  to  convert  celsius  temperature  to  farenheit ?  --->   1.8 * celsius  temp + 32

2) Let  input  be   list  of  celsius  temperatures  such  as  [30 , 40 , 50 , 25]
    What  is  the  output ?  --->   1.8 * 30 + 32
							                      1.8 * 40 +32
								                  1.8 * 50 + 32
								                  1.8 * 25 + 32
								                  
Enter  list  of  celsius  temperatures :  [10,20,15,18]
Farenheit   temperatures
50.0
68.0
59.0
64.4
'''

'''
c=eval(input("Enter  list  of  celsius  temperatures : "))
m=map(lambda x:9*x/5 + 32 , c)
print("Farenheit   temperatures")
for i in m:
    print(i)
    
'''


'''
#17.Write  a  program  to  print  2 ^ 0 , 2 ^ 1 , 2 ^ 2 , ....... 2 ^ 9  using  map   object (Home  work)

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

'''

'''
from time import sleep
m=map(lambda x:2**x ,range(10))
print("Powers  of   2")

for i in m:
    print(i)
    sleep(1)
    
'''


'''
#18. Write  a  program  to  determine  area  of  circle  for  each  radius  in  the  list

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
'''

'''
from math import * 
from time import sleep 

r=eval(input("Enter  list  of  radii  : "))
m=map(lambda x:pi*x*x  , r)
print("Area  of  each  radius  in  the  list")
for i in m:
    print(round(i,2))
    sleep(1)
    
'''


'''
#19.Write  a  program  to  add  two  tuples  of  difierent  sizes  and  store  the  results  in  3rd  tuple

Let  1st  tuple  be  (10 , 20 , 30 , 40)  and  2nd  tuple  be  (1 , 2 , 3 , 4 ,  5  ,  6)
What  is  the  3rd  tuple ?  --->  (10 + 1 , 20 + 2 , 30 + 3 , 40 + 4)   and  5  and 6  are  ignored


Enter  first  tuple :  (10,20,15,18)
Enter  second  tuple :  (30,40,35,12,100,200)
Addition  tuple  :   (40, 60, 50, 30)
'''

'''
t1=eval(input("Enter  first  tuple : "))
t2=eval(input("Enter  second  tuple : "))
l=[]

m=map(lambda x,y:x+y,t1,t2)

for i in m:
    l.append(i)

print("Addition  tuple  :",tuple(l))

'''


'''
#20. Write  a  program  to  multiply  two  lists  and  store  results  in  3rd  list

Let  1st  list  be  [10 , 20 , 15 , 18 , 19 , 17]  and  2nd  list  be  [1 , 5 , 3 , 2]
What  is  the  3rd  list ?  ---> [10 * 1 , 20 * 5 , 15 * 3 , 18 * 2]  and  ignores  19  and  17

Hint:  Use  map

Enter  first  list :  [10,20,15,18]
Enter  second  list :  [1,2,3,4]
Multiplication  list :   [10, 40, 45, 72]
'''

'''
l1=eval(input("Enter  first  list : "))
l2=eval(input("Enter  second  list : "))
l=[]

m=map(lambda x,y:x*y,l1,l2)

for i in m:
    l.append(i)

print("Multiplication  list :",l)

'''

#21. filter  inside  map

'''
import  time
a = [10 , 20 , 15 , 12 , 18 , 5 , 14 , 25 , 17]
m = map(lambda  y  :   y + y ,  filter(lambda  x  :  x >= 15 , a))
while   True:
	try:
		print(next(m)) # 40 30 36 50 34 
		time . sleep(1)
	except:
		break
'''

#22. map  inside  filter (Home  work)
'''
import   time
a = [10 , 20 , 15 , 12 , 18 , 5 , 14 , 25 , 17]
f = filter(lambda  y  :   y  % 2 == 0 , map (lambda  x : x ** 2 , a))
while   True:
	try:
		print(next(f)) #100 400 144 324 196 
		time . sleep(1)
	except:
		break
		
'''

'''
#23. Write  a  program  to  determine  largest  element  of  the  list  with  reduce()  function

Let  list   be  [10 , 20 , 15 , 30 , 25 , 40 , 35]
What  is   the  largest  element  of  list ?  ---> 40

Hint:  Use  reduce()  function


Enter list of numbers (or) strings:[10 , 20 , 15 , 30 , 25 , 40 , 35]
Largest  element  :    40
'''

'''
from functools import reduce 

l=eval(input("Enter list of numbers (or) strings: "))
r=reduce(lambda x,y:max(x,y),l)
print("Largest  element  :",r)

'''


#24. Find  outputs  (Home  work)

'''
from  functools  import  reduce
a = [ 10 , 20 , 15 , 5 , 12 , 18 , 25 , 14]
ans = reduce( lambda  x , y  : x + y , map(lambda  y :  y ** 2 , filter(lambda  x  :  x  >= 15 , a)))
#[400+225+324+625] =(1574)
print(ans)

'''