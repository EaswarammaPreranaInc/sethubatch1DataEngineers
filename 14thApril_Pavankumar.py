#  How  to  iterate  zip  object  in  differenet  ways  (Home  work)
import   time
a = ['Telangana' , 'Andhra Pradesh' , 'Karnataka ', 'Tamilnadu']
b = ['Hyderabad' , 'Amaravathi' , 'Bangalore', 'Chennai']
z = zip(a , b)
print(type(z))
print(z)
print(next(z))
print(z.__next__())
a=zip(a,b)
for i in a:
	time.sleep(1)
	print(i)
'''
OUTPUT:
class zip
type and address
('Telangana', 'Hyderabad')
('Andhra Pradesh', 'Amaravathi')
('Telangana', 'Hyderabad')
('Andhra Pradesh', 'Amaravathi')
('Karnataka ', 'Bangalore')
('Tamilnadu', 'Chennai')
print('Unpacks  zip  object  with   *  operator  :  ' , How  to   unpack  zip  object   with  *  operator)
print()
print('zip   object  in  the  form  of   list  :  ' ,  How  to  convert  zip  object  to  list)
print()
print('zip   object  in  the  form  of   dictionary :  ' ,  How  to  convert  zip  object  to  dictionary)

'''
#  Find  outputs  (Home  work)
import   time
a = [ 'Empno' , 'Emp Name' , 'Salary']
b = [ 25 , 'Rama  Rao' , 10000.0 , 'Male' , True]
c = zip(a , b)
while   True:
	try:
		print(next(c))
		time . sleep(1)
	except:
		break
'''
OUTPUT:
('Empno',25)
('Emp Name,'Rama Rao')
('Salary',10000.0)
'''
#  Find  outputs  (Home  work)
import   time
a = ['Telangana' , 'Andhra  Pradesh' , 'Karnataka' , 'TamilNadu' , 'Maharastra']
b = ['Hyderabad' , 'Amaravathi' , 'Banglore' , 'Chennai' , 'Mumbai']
c = [50000000 , 40000000 , 70000000 , 60000000 , 30000000]
for   x   in   zip(a , b , c):
	print(x)
	time.sleep(1)
'''
OUTPUT:
('Telangana','Hyderabad',50000000)
('Andhra  Pradesh','Amaravathi',40000000 )
('Karnataka','Banglore',70000000)
('TamilNadu','Chennai',60000000)
('Maharastra','Mumbai',30000000)
'''
# Find  outputs   (Home  work)
import   time
a = [1 , 2 , 3]
b = [4 , 5 , 6 , 7 , 8]
for  x , y  in   zip(a , b):
	print(x + y)
	time.sleep(1)
'''
OUTPUT:
5
7
9
'''
# Find outputs  (Home  work)
import   time
def   disp(z):
	while   True:
		try:
			print(next(z))
			time . sleep(1)
		except:
			break
	print()
a = [10 , 20 ,  30]
b = {1 : 2 , 3 : 4 , 5 : 6}
c = zip(a , b . keys())
disp(c)
d = zip(a , b . values())
disp(d)
e = zip(a , b . items())
disp(e)
f = zip(a , b)
disp(f)
g = zip(a)
disp(g)
h = zip(b)
disp(h)
i=zip()
disp(i)
'''
OUTPUT:
(10,1)
(20,3)
(30,5)

(10,2)
(20,4)
(30,6)

(10,(1,2))
(20,(3,4))
(30,(5,6))

(10,1)
(20,3)
(30,5)

(10,)
(20,)
(30,)

(1,)
(3,)
(5,)
'''
# Find  outputs  (Home  work)
z = zip(range(5) , range(20 , 25))
a = [[x,y] for x,y in z]
print(a)
'''
OUTPUT:
[[0,20],[1,21],[2,22],[3,23],[4,24]]
'''
#  How  to  print  reversed  object  in  different  ways  (Home  work)
import   time
a = input('Enter  any  string  :  ')  #  Assume  that  input  is  HYD
r = reversed(a)
print(type(r))
print(r)
print('Iterate  reversed  object  with   next   function')
while True:
	try:
		print(next(r))
	except:
		break
print('Iterate  reversed  object  with   next   method')
b=reversed(a)
while True:
	try:
		print(b.__next__())
	except:
		break
print('Iterate  reversed  object  with   for  loop')
for i in reversed(a):
	print(i)
print('Unpack  reversed  object  with   *  operator :   ',*reversed(a))
print()
print('reversed  object  in  the  form   of  list  :  ',list(reversed(a)))
print('Reverse  string   :   ' ,''.join(list(reversed(a))))
'''
output:
Enter  any  string  :  HYD
<class 'reversed'>
<reversed object at 0x00000276E7DB5690>
Iterate  reversed  object  with   next   function
D
Y
H
Iterate  reversed  object  with   next   method
D
Y
H
Iterate  reversed  object  with   for  loop
D
Y
H
Unpack  reversed  object  with   *  operator :    D Y H

reversed  object  in  the  form   of  list  :   ['D', 'Y', 'H']
Reverse  string   :    DYH
'''
# Find  outputs (Home  work)
a = 'RAMA'
b = reversed(a)
print(type(b))
print(b)
print(id(b))
print(*b)
#print(b[0]) ->doesn't support slicing as it doesnt have index
#print(b[1 : 3])
#print(b * 2) 
#print(len(b))->len function demands sequence
'''
OUTPUT:
<class 'reversed'>
type and address
2495948673312
A M A R
'''
# Can  tuple  be  reversed ?   (Home  work)
import   time
a = (25 , 10.8 , 'Hyd' , True)
b = reversed(a)
print(type(b))
for  x  in   b:
	print(x)
	time.sleep(1)
'''
OUTPUT:
class reversed
True
'Hyd'
10.8
25
'''
# Can  dictionary  be  reversed  ? (Home  work)
import   time
def   disp(r):
	while  True:
		try:
			print(next(r))
			time . sleep(1)
		except:
			break
	print()
a = {10 : 'Rama' , 20 : 'Sita' , 15 : 'Kiran' , 18 : 'Amar'}
b = reversed(a . keys())
disp(b)
c = reversed(a . values())
disp(c)
d = reversed(a . items())
disp(d)
e = reversed(a)
disp(e)
'''
OUTPUT:
18
15
20
10

Amar
Kiran
Sita
Rama

(18,'Amar')
(15,'Kiran')
(20,'Sita')
(10,'Rama')

18
15
20
10
'''
'''
Write  a  program  to  reverse  a  dictionary ?

Let  input  be  {'Empno' : 25 , 'Emp Name' : 'Rama  Rao' , 'Sal' : 10000.0}
What  is  the  output  ?  --->  {'Sal' : 10000.0 , 'Emp  Name' :  Rama  Rao' , 'Empno' : 25}

Hint:  Use  reversed  iterator
'''
a={'Empno':25,'Emp Name':'Rama  Rao','Sal':10000.0}
print(dict(reversed(a.items())))
'''
OUTPUT:
{'Sal': 10000.0, 'Emp Name': 'Rama  Rao', 'Empno': 25}
'''
# Find outputs
import  time
a = {10 : 'Rama rao', 20 : 'Sita', 15 : 'Rajesh', 18 : 'Kiran'}
print('Keys  in   reverse   order')
#Write  for  loop  to  reverse  keys  of  dictionary
for i in reversed(a.keys()):
	print(i)
print('Values  in  reverse  order')
#Write  for  loop  to  reverse  values  of  dictionary
for i in reversed(a.values()):
	print(i)
print('Tuples  in   reverse  order')
#Write  for  loop  to  reverse   tuples   of  dictionary
for i in reversed(a.items()):
	print(i,end=' ')
print()
print('Elements  of  each   tuple  in  reverse  order')
#Write  for  loop  to  reverse   elements  of   each   tuple  of  dictionary
for i in a.items():
	c=[]
	for j in reversed(i):
		c.append(j)
	print(tuple(c))		
print('Keys  and  values  in   reverse   order')
#Write  for  loop  to  print  each   key  and   the  corresponding  value  of  dictionary  in  reverse  order
d=[]
for i in a.items():
	c=[]
	for j in reversed(i):
		c.append(j)
	d.append(tuple(c))
print(dict(d))
#  Write  outputs  here
'''
OUTPUT:
Keys  in   reverse   order
18
15
20
10
Values  in  reverse  order
Kiran
Rajesh
Sita
Rama rao
Tuples  in   reverse  order
(18, 'Kiran') (15, 'Rajesh') (20, 'Sita') (10, 'Rama rao')
Elements  of  each   tuple  in  reverse  order
('Rama rao', 10)
('Sita', 20)
('Rajesh', 15)
('Kiran', 18)
Keys  and  values  in   reverse   order
{'Rama rao': 10, 'Sita': 20, 'Rajesh': 15, 'Kiran': 18}
'''
#  How  to  print  list_reverseiterator  object  in  different  ways  (Home   work)
import   time
a = [25 , 10.8 , 'Hyd' , True]
r = reversed(a)
print(type(r))
print(r)
print('Iterate  list_reverseiterator  object  with   next()   function')
#How  to  iterate   list_reverseiterator  object  with   next()   function
while True:
	try:
		print(next(r))
		time.sleep(0.5)
	except:
		break
print()
print('Iterate  list_reverseiterator  object  with   next()   method')
#How  to  iterate   list_reverseiterator  object  with   next()  method
c=reversed(a)
while True:
	try:
		print(c.__next__())
		time.sleep(1)
	except:
		break
print()
print('Iterate  list_reverseiterator  object  with   for  loop')
#How  to  iterate   list_reverseiterator  object  with   for  loop
for i in reversed(a):
	print(i)
	time.sleep(0.5)
print('Unpack  list_reverseiterator  object  with     operator   :  ' ,*reversed(a))
print()
print('Reverse  list  :  '  , list(reversed(a)))
'''
OUTPUT:
	<class 'list_reverseiterator'>
<list_reverseiterator object at 0x000001E9A6F65840>
Iterate  list_reverseiterator  object  with   next()   function
True
Hyd
10.8
25

Iterate  list_reverseiterator  object  with   next()   method
True
Hyd
10.8
25

Iterate  list_reverseiterator  object  with   for  loop
True
Hyd
10.8
25
Unpack  list_reverseiterator  object  with     operator   :   True Hyd 10.8 25

Reverse  list  :   [True, 'Hyd', 10.8, 25]
'''
# How  to  iterate   list_iterator  in  different  ways
import   time
list  =  [10  ,  20  ,  15  ,  18]
print('Iterate  list  with  for  loop')
#How  to  iterate  list  with  for  loop
for i in list:
	print(i)
print()
#print(next(list))
list_itr = iter(list)
print(type(list_itr))
print(list_itr)
print('Iterate  List_iterator  with  next()  function')
#How  to  iterate  list_iterator  with  next()  function
while True:
	try:
		print(next(list_itr))
	except:
		break
print()
print('Iterate  List_iterator  with   _next_()  method')
#How  to  iterate  list_iterator  with   _next_  method
itr=iter(list)
while True:
	try:
		print(itr.__next__())
	except:
		break
print()
print('Iterate  List_iterator  with   for    loop')
#How  to  iterate  list_iterator  with  for  loop
it=iter(list)
for i in it:
	print(i)
itr=iter(list)
print('Unpacks  List_iterator  with  *  operator  :    ' ,*itr)
'''
OUTPUT:
Iterate  list  with  for  loop
10
20
15
18

<class 'list_iterator'>
<list_iterator object at 0x000001F0A61A5A20>
Iterate  List_iterator  with  next()  function
10
20
15
18

Iterate  List_iterator  with   _next_()  method
10
20
15
18

Iterate  List_iterator  with   for    loop
10
20
15
18
Unpacks  List_iterator  with  *  operator  :     10 20 15 18
'''
