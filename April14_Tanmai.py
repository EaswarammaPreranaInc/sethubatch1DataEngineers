
#How  to  iterate  zip  object  in  differenet  ways  (Home  work)
import   time
a = ['Telangana' , 'Andhra Pradesh' , 'Karnataka ', 'Tamilnadu']
b = ['Hyderabad' , 'Amaravathi' , 'Bangalore', 'Chennai']
z = zip(a , b)
print(type(z)) #class Zip
print(z) # Type and Adress
print('Iterate  zip  object  with   next()   function') 
while True:
	try:
		print(next(z))
		time.sleep(1)
	except:
		break
#How  to   iterate  zip  object  with  next  function
print('Iterate  zip  object  with  next  method')
z = zip(a , b)
while True:
	try:
		print(z.__next__())
		time.sleep(1)
	except:
		break
#How  to   iterate  zip  object  with  next  method
print('Iterate  zip  object  with   for  loop')
z=zip(a,b)
for x in z:
	print(x)
#How  to   iterate  zip  object  with  for  loop
print('Iterate  elements  of  each  tuple  in  zip  object')
z=zip(a,b)
for x,y in z:
	print(x,y)
#How  to   iterate  elements  of  each  tuple  of  zip  object  with  for  loop
z=zip(a,b)
print('Unpacks  zip  object  with   *  operator  :  ' , *z)#How  to   unpack  zip  object   with  *  operator)
print()
print()
z=zip(a,b)
print('zip   object  in  the  form  of   list  :  ' , list(z)) #How  to  convert  zip  object  to  list)

print()
z=zip(a,b)
print('zip   object  in  the  form  of   dictionary :  ' ,  dict(z) )#How  to  convert  zip  object  to  dictionary)
#  Write  all  the  outputs  here
'''
<class 'zip'>
<zip object at 0x000002207BBCBC00>
Iterate  zip  object  with   next()   function
('Telangana', 'Hyderabad')
Iterate  zip  object  with  next  method
('Andhra Pradesh', 'Amaravathi')
Iterate  zip  object  with   for  loop
('Telangana', 'Hyderabad')
('Andhra Pradesh', 'Amaravathi')
('Karnataka ', 'Bangalore')
('Tamilnadu', 'Chennai')
Iterate  elements  of  each  tuple  in  zip  object
Telangana Hyderabad
Andhra Pradesh Amaravathi
Karnataka  Bangalore
Tamilnadu Chennai
Unpacks  zip  object  with   *  operator  :   ('Telangana', 'Hyderabad') ('Andhra Pradesh', 'Amaravathi') ('Karnataka ', 'Bangalore') ('Tamilnadu', 'Chennai')


zip   object  in  the  form  of   list  :   [('Telangana', 'Hyderabad'), ('Andhra Pradesh', 'Amaravathi'), ('Karnataka ', 'Bangalore'), ('Tamilnadu', 'Chennai')]

zip   object  in  the  form  of   dictionary :   {'Telangana': 'Hyderabad', 'Andhra Pradesh': 'Amaravathi', 'Karnataka ': 'Bangalore', 'Tamilnadu': 'Chennai'}
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
('Empno', 25)
('Emp Name', 'Rama  Rao')
('Salary', 10000.0)
'''
#  Find  outputs  (Home  work)
import   time
a = ['Telangana' , 'Andhra  Pradesh' , 'Karnataka' , 'TamilNadu' , 'Maharastra']
b = ['Hyderabad' , 'Amaravathi' , 'Banglore' , 'Chennai' , 'Mumbai']
c = [50000000 , 40000000 , 70000000 , 60000000 , 30000000]
for   x   in   zip(a , b , c):
	print(x)
	time . sleep(1)
'''('Telangana', 'Hyderabad', 50000000)
('Andhra  Pradesh', 'Amaravathi', 40000000)
('Karnataka', 'Banglore', 70000000)
('TamilNadu', 'Chennai', 60000000)
('Maharastra', 'Mumbai', 30000000)'''
import   time
a = [1 , 2 , 3]
b = [4 , 5 , 6 , 7 , 8]
for  x , y  in   zip(a , b):
	print(x + y)
	time . sleep(1)
'''
5
7
9 ''' 

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
i = zip()
disp(i)
'''
(10, 1)
(20, 3)
(30, 5)

(10, 2)
(20, 4)
(30, 6)

(10, (1, 2))
(20, (3, 4))
(30, (5, 6))

(10, 1)
(20, 3)
(30, 5)

(10,)
(20,)
(30,)

(1,)
(3,)
(5,)

''' 
# Find  outputs  (Home  work)
z = zip(range(5) , range(20 , 25))
a = [ [x , y]  for  x , y   in   z] 
print(a) # [[0,20],[1,21],[2,22],[3,23],[4,24]]

#  How  to  print  reversed  object  in  different  ways  (Home  work)
import   time
a = input('Enter  any  string  :  ')  #  Assume  that  input  is  HYD
r = reversed(a) #  Empty object D <next line> Y<next line> H
print(type(r)) # class Reversed
print(r) # Type n address
print('Iterate  reversed  object  with   next   function')
while True:
	try:

		print(next(r)) 
		sleep.time(1)
	except:
		break
#How  to  iterate  reversed  object  'r'  with  next()  function
print('Iterate  reversed  object  with   next   method')
r = reversed(a)
while True:
	try:
		print(r.__next__())
		sleep.time(1)
	except:
		break

# How  to  iterate  reversed  object   with  next()   method
print('Iterate  reversed  object  with   for  loop')
for x in r:
	print(x)
#How  to  iterate  reversed  object   with  for  loop
r = reversed(a)
print('Unpack  reversed  object  with   *  operator :   ' , *r) #How  to   unpack  reversed  object   with  *  operator)
print()
r = reversed(a)
print('reversed  object  in  the  form   of  list  :  ' ,  list(r))#How  to  convert  reversed  object  to  list)
r = reversed(a)
print('Reverse  string   :   ' ,  ''.join(r))#How  to  convert  reversed  object  to   string)
#  Write all  the  outputs  here
'''Enter  any  string  :  HYD
<class 'reversed'>
<reversed object at 0x000001941578AF20>
Iterate  reversed  object  with   next   function
D
Iterate  reversed  object  with   next   method
Y
Iterate  reversed  object  with   for  loop
H
Unpack  reversed  object  with   *  operator :    D Y H

reversed  object  in  the  form   of  list  :   ['D', 'Y', 'H']
Reverse  string   :    DYH'''

# Find  outputs (Home  work) 
a = 'RAMA'
b = reversed(a) # Empty object 
print(type(b)) # class Reversed 
print(b) # type n address
print(id(b)) # address
print(*b) # A M A R
#print(b[0]) # error 
#print(b[1 : 3]) cant be used iterators 
#print(b * 2)
#print(len(b)) 

# Can  tuple  be  reversed ?   (Home  work)
import   time
a = (25 , 10.8 , 'Hyd' , True)
b = reversed(a) # empty object is created 
print(type(b)) # class reversed 
for  x  in   b:
	print(x)
	time . sleep(1)
'''
True
Hyd
10.8
25
'''

# Can  dictionary  be  reversed  ? Yes (Home  work) 
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
18
15
20
10

Amar
Kiran
Sita
Rama

(18, 'Amar')
(15, 'Kiran')
(20, 'Sita')
(10, 'Rama')

18
15
20
10'''

'''
Write  a  program  to  reverse  a  dictionary ?

Let  input  be  {'Empno' : 25 , 'Emp Name' : 'Rama  Rao' , 'Sal' : 10000.0}
What  is  the  output  ?  --->  {'Sal' : 10000.0 , 'Emp  Name' :  Rama  Rao' , 'Empno' : 25}

Hint:  Use  reversed  iterator
''' 

a= eval(input("Enter a dict: "))
print( dict((reversed(a.items()))))


# Find outputs
import  time
a = {10 : 'Rama rao', 20 : 'Sita', 15 : 'Rajesh', 18 : 'Kiran'}
print('Keys  in   reverse   order')
r=reversed(a)
for x in r:
	print(x)
#Write  for  loop  to  reverse  keys  of  dictionary
print('Values  in  reverse  order')
r=reversed(a.values())
for x in r:
	print(x)
#Write  for  loop  to  reverse  values  of  dictionary
print('Tuples  in   reverse  order')
r=reversed(a.items())
for x,y in r:
	print(x,y)
#Write  for  loop  to  reverse   tuples   of  dictionary
print('Elements  of  each   tuple  in  reverse  order')
r=reversed(a.items())
for x,y in r:
	print(x,y,sep='...')
#Write  for  loop  to  reverse   elements  of   each   tuple  of  dictionary
print('Keys  and  values  in   reverse   order')
for x in reversed(a):
	print(x,a[x])

#Write  for  loop  to  print  each   key  and   the  corresponding  value  of  dictionary  in  reverse  order
#  Write  outputs  here
'''
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
18 Kiran
15 Rajesh
20 Sita
10 Rama rao
Elements  of  each   tuple  in  reverse  order
Kiran 18
Rajesh 15
Sita 20
Rama rao 10 
Keys  and  values  in   reverse   order'''  

#  How  to  print  list_reverseiterator  object  in  different  ways  (Home   work)
import   time
a = [25 , 10.8 , 'Hyd' , True]
r = reversed(a)
print(type(r)) #list_reverseiterator
print(r) # type n address
print('Iterate  list_reverseiterator  object  with   next()   function')
print(next(r)) # ccan use while loop also
#How  to  iterate   list_reverseiterator  object  with   next()   function
print('Iterate  list_reverseiterator  object  with   next()   method')
#How  to  iterate   list_reverseiterator  object  with   next()  method
print(r.__next__()) # ccan use while loop also
print('Iterate  list_reverseiterator  object  with   for  loop')
#How  to  iterate   list_reverseiterator  object  with   for  loop
for x in r:
	print(x)
r = reversed(a)
print('Unpack  list_reverseiterator  object  with     operator   :  ' , *r)#How  to  unpack   list_reverseiterator  object   with     operator)
print()
r = reversed(a)
print('Reverse  list  :  '  ,  list(r)) #How  to  convert  list_reverseiterator  object  to  list) 

# How  to  iterate   list_iterator  in  different  ways
import   time
list  =  [10  ,  20  ,  15  ,  18]
print('Iterate  list  with  for  loop')
a=reversed(list)
for x in a:
	print(x)
#How  to  iterate  list  with  for  loop
a=reversed(list)
#print(next(list)) # error next cant be used for sequences 
list_itr = iter(list) # conver t list to iterator 
print(type(list_itr)) # iterator 
print(list_itr) # type n address
print('Iterate  List_iterator  with  next()  function')

print(next(list_itr))
#How  to  iterate  list_iterator  with  next()  function
print('Iterate  List_iterator  with   _next_()  method')
print(list_itr.__next__())
#How  to  iterate  list_iterator  with   _next_  method
print('Iterate  List_iterator  with   for    loop')

for x in list_itr:
	print(x)
#How  to  iterate  list_iterator  with  for  loop

list_itr = iter(list)
print('Unpacks  List_iterator  with  *  operator  :    ' ,  *list_itr)# How  to  unpack  list_iterator)

# Find  outputs
a = 25
print(a) #25
#for  x   in   a: # error
	#print(x) 
#print(iter(a)) # error
#print(next(a)) # error 
