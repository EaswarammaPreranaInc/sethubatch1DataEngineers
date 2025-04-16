# Find  outputs (Home  work)
'''import  time
a = [25 , 10.8 , 3 + 4j , 'Hyd' , False , True]
f = filter(lambda   x :   True ,   a)
while  True:
	try:
		print(next(f))
		time . sleep(1)
	except:
		break

#output
25 <next line> 10.8 <next line> 3+4j <next line> 'Hyd' <next line> False <next line> True
'''

#  Find  outputs (Home  work)
'''import  time
a = [25 , 10.8 , 3 + 4j ,  'Hyd' , True ,False]
f = filter(lambda  x  :  False ,  a)
while  True:
	try:
		print(next(f))
		time . sleep(1)
	except:
		break
'''

# Find  outputs (Home  work)
'''import  time
a = [25 , 10.8 , False ,  3 + 4j , 0 , 'Hyd' , '' , (25,)  ,  () ]
f = filter(lambda   x   :   x   ,   a)
while  True:
	try:
		print(next(f))
		time . sleep(1)
	except:
		break

#output
25 <next line> 10.8 <next line> (3+4j) <next line> Hyd <next line> (25,)
'''

# Find outputs
'''import  time
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

#output
10 <next line> -25 <next line> (25,) <next line> Hyd <next line> 10.8 <next line> [10, 20] <next line> True
'''

# Find outputs  (Home  work)
'''import  time
a = ['Rama Rao' , 'Sita' , 'Rajesh' , 'Kiran' , 'Amar' , 'Manohar' , 'Vamsi']
f = filter(lambda  x  :   len(x) >= 5  , a)
while   True:
	try:
		print(next(f))
		time . sleep(1)
	except:
		break

#output
Rama Rao <next line> Rajesh <next line> Kiran <next line> Manohar <next line> <next line> Vamsi
'''


# Find  outputs (Home  work)
'''import   time
list=[('A' , 10) , ('B' , 20) , ('C' , 15) , ('D' , 5) , ('E' , 18)]
f = filter(lambda   x  :   x[1]  >=  12 , list)
while   True:
	try:
		print(next(f))
		time . sleep(1)
	except:
		break

#output
('B', 20) <next line> ('C', 15) <next line> ('E', 18)
'''

# Find  outputs (Home  work)
'''import   time
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
		
		
#output
{'Roll Num': 10, 'Stud Name': 'Rama Rao', 'Marks': 75}
{'Roll Num': 15, 'Stud Name': 'Kiran', 'Marks': 65}
{'Roll Num': 5, 'Stud Name': 'Rajesh', 'Marks': 82}
'''


# Find  outputs (Home  work)
'''import  time
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
print('Filter  f1')
disp(f1)
f2 = filter(lambda  x  :  x['sale']  >=  200  , a)
print('Filter  f2')
disp(f2)


#output
Filter  f1
{'country': 'USA', 'sale': 300.3}
{'country': 'UK', 'sale': 210.4}
Filter  f2
{'country': 'china', 'sale': 200.2}
{'country': 'USA', 'sale': 300.3}
{'country': 'UK', 'sale': 210.4}
'''


# How  to  print  fliter  object  in  different  ways ?
'''import   time
a = [10 , 15 , 20 , 17 , 18 , 19 , 26]
f = filter(lambda  x  :  x  %  2  ==  0 , a)
print('Iterate  filter  object  with   next   function')
while True:       # How  to iterate  filter  object  with  next()  function
	try:
		print(next(f))
		time . sleep(1)
	except:
		break
print('Iterate  filter  object  with   for  loop')
for x in filter(lambda  x  :  x  %  2  ==  0 , a):         # How  to iterate  filter  object  with  for  loop
	print(x)
	time . sleep(1)
f = filter(lambda  x  :  x  %  2  ==  0 , a)
print('Unpacking  filter  object :  ' , f)  # How  to  unpack  filter  object)
print()
f = filter(lambda  x  :  x  %  2  ==  0 , a)
print('filter  object  in  the  form  of  list  :  ' , list(f))  # How  to  convert  filter  object  to  list)


#output
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
Unpacking  filter  object :   <filter object at 0x000001582DFDB580>

filter  object  in  the  form  of  list  :   [10, 20, 18, 26]
'''


#  Write  a  program  to  print  odd  numbers  between  1  and  20  with  filter  iterator

'''odd_iterator = filter(lambda x: x % 2 != 0, range(1 , 21))
print("Odd numbers between 1 and 20:")
for num in odd_iterator:
    print(num)
'''	
'''
# Use filter with lambda to filter odd numbers
import time
odd_iterator = filter(lambda x: x % 2 == 1, range(1 , 21))

print("Odd numbers between 1 and 20:")
while True:
    try:
		print(next(odd_iterator))
		time.sleep(1)
	
	except StopIteration:
        break


'''


# Nested  filter  i.e.  filter  on  filter
'''import   time
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

#output
(10, 'Rama', 10000.0)
(15, 'Rajesh', 15000.0)
'''

#  Modify  following  program  with  regular  function  and  for  loop
'''import  time
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

#output
<class 'map'>
<map object at 0x00000214173AB0D0>
100
400
225
324
25
'''

# Find  outputs (Home  work)
'''import  time
a = [ ('A' , 10) , ('B' , 20) , ('C' , 15) , ('D' , 5) , ('E' , 18) ]
m = map(lambda   x  :  x[1]  ,  a)
while   True:
	try:
		print(next(m))
		time . sleep(1)
	except  StopIteration:
		break
		
#output
10 <next line>  20 <next line> 15 <next line> 5 <next line> 18
'''


# Find  outputs (Home  work)
'''import   time
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

#output
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

# filter  inside  map
'''import  time
a = [10 , 20 , 15 , 12 , 18 , 5 , 14 , 25 , 17]
m = map(lambda  y  :   y + y ,  filter(lambda  x  :  x >= 15 , a))
while   True:
	try:
		print(next(m))
		time . sleep(1)
	except:
		break

#output
40 <next line> 30 <next line> 36 <next line> 50 <next line> 34
'''

# map  inside  filter (Home  work)
'''import   time
a = [10 , 20 , 15 , 12 , 18 , 5 , 14 , 25 , 17]
f = filter(lambda  y  :   y  % 2 == 0 , map (lambda  x : x ** 2 , a))
while   True:
	try:
		print(next(f))
		time . sleep(1)
	except:
		break

#output
100
400
144
324
196
'''

# Find  outputs  (Home  work)
from  functools  import  reduce
a = [ 10 , 20 , 15 , 5 , 12 , 18 , 25 , 14]
ans = reduce( lambda  x , y  : x + y , map(lambda  y :  y ** 2 , filter(lambda  x  :  x  >= 15 , a)))
print(ans)  #1574


