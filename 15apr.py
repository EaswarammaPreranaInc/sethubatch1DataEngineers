'''
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
#outputs
25
10.8
(3+4j)
Hyd
False
'''
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
#outputs
except block executes
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
#output
25
10.8
(3+4j)
Hyd
(25,)
'''
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
print('Filter  f2')
disp(f2)
#output
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
#output
Rama Rao
Rajesh
Kiran
Manohar
Vamsi
'''
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
#output
#('B',20) , ('C',15) , ('E',18)
'''
'''
# Find  outputs (Home  work)
import   time
list = [ { 'Roll Num' :  10 ,'Stud Name' : 'Rama Rao' ,'Marks' : 75},{'Roll Num' :  20 , 'Stud Name' : 'Sita' ,'Marks': 52} ,{'Roll Num'  :  15 ,'Stud Name' : 'Kiran' ,'Marks' : 65} ,{'Roll Num'  :  18 ,'Stud Name' : 'Amar' ,'Marks' : 48} ,{'Roll Num' :  5 ,'Stud Name' : 'Rajesh' ,'Marks' : 82}]  #  List  of  dictionaries
f = filter(lambda  x :  x['Marks'] >= 60 , list)
while   True:
	try:
		print(next(f))
		time . sleep(1)
	except:
		break
#outputs
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
'''

# How  to  print  fliter  object  in  different  ways ?
import   time
a = [10 , 15 , 20 , 17 , 18 , 19 , 26]
f = filter(lambda  x  :  x  %  2  ==  0 , a)
print('Iterate  filter  object  with   next   function')
while True:
	try:
		print(next(f))
		time.sleep(1)
	except:
		break
#How  to iterate  filter  object  with  next()  function
print('Iterate  filter  object  with   for  loop')
f = filter(lambda  x  :  x  %  2  ==  0 , a)
while True:
	try:
		print(next(f))
		time.sleep(1)
	except:
		break
#How  to iterate  filter  object  with  for  loop
print('Unpacking  filter  object :  ' ,    *filter(lambda  x  :  x  %  2  ==  0 , a))
print()
print('filter  object  in  the  form  of  list  :  ' , list(filter(lambda  x  :  x  %  2  ==  0 , a)))



























	












