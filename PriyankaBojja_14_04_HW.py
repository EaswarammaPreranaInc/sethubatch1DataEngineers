Q1 #How  to  iterate  zip  object  in  differenet  ways  (Home  work)
import   time
a = ['Telangana' , 'Andhra Pradesh' , 'Karnataka ', 'Tamilnadu']
b = ['Hyderabad' , 'Amaravathi' , 'Bangalore', 'Chennai']
z = zip(a , b)
print(type(z))
print(z)
print('Iterate  zip  object  with   next()   function') 
while True:
	try:
		print(next(z))  #How  to   iterate  zip  object  with  next  function
		time.sleep(1)
	except:
		break
print('Iterate  zip  object  with  next  method')
z=zip(a,b)  
while True:
	try:
		print(z.__next__())  #How  to   iterate  zip  object  with  next method
		time.sleep(1)
	except:
		break
print('Iterate  zip  object  with   for  loop')
z3=zip(a,b)
for x in z3:  #How  to   iterate  zip  object  with  for  loop
	print(x)
	time.sleep(1)
print('Iterate  elements  of  each  tuple  in  zip  object')
z4=zip(a,b)  
for x,y in z4:
	print(x,y)     #How  to   iterate  elements  of  each  tuple  of  zip  object  with  for  loop
	time.sleep(1)
z5=zip(a,b)
print('Unpacks  zip  object  with   *  operator  :  ' , *z5)  #How  to   unpack  zip  object   with  *  operator
print()
z6=zip(a,b)
print('zip   object  in  the  form  of   list  :  ' ,list(z6))  #How  to  convert  zip  object  to  list
print()
z7=zip(a,b)
print('zip   object  in  the  form  of   dictionary :  ' ,dict(z7) )  # How  to  convert  zip  object  to  dictionary

OP-
<zip object at 0x0000029D503CF300>
Iterate  zip  object  with   next()   function
('Telangana', 'Hyderabad')
('Andhra Pradesh', 'Amaravathi')
('Karnataka ', 'Bangalore')
('Tamilnadu', 'Chennai')
Iterate  zip  object  with  next  method
('Telangana', 'Hyderabad')
('Andhra Pradesh', 'Amaravathi')
('Karnataka ', 'Bangalore')
('Tamilnadu', 'Chennai')
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
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------
Q2 #Find  outputs
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

OP-
('Empno', 25)
('Emp Name', 'Rama  Rao')
('Salary', 10000.0)
#------------------------------------------------------------------------------------------------------
Q3 #Find  outputs  
import   time
a = ['Telangana' , 'Andhra  Pradesh' , 'Karnataka' , 'TamilNadu' , 'Maharastra']
b = ['Hyderabad' , 'Amaravathi' , 'Banglore' , 'Chennai' , 'Mumbai']
c = [50000000 , 40000000 , 70000000 , 60000000 , 30000000]
for   x   in   zip(a , b , c):
	print(x)
	time . sleep(1)

OP-
('Telangana', 'Hyderabad', 50000000)
('Andhra  Pradesh', 'Amaravathi', 40000000)
('Karnataka', 'Banglore', 70000000)
('TamilNadu', 'Chennai', 60000000)
('Maharastra', 'Mumbai', 30000000)
#--------------------------------------------------------------------------------------------------
Q4 #Find  outputs 
import   time
a = [1 , 2 , 3]
b = [4 , 5 , 6 , 7 , 8]
for  x , y  in   zip(a , b):
	print(x + y)  # 5 7 9 
	time . sleep(1)
#------------------------------------------------------------------------------------------
Q5 #Find outputs  (Home  work)
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

OP-
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


#---------------------------------------------------------------------------------------------------
Q6 #Find  outputs 
z = zip(range(5) , range(20 , 25))
a = [ [x , y]  for  x , y   in   z]
print(a)  #[[0, 20], [1, 21], [2, 22], [3, 23], [4, 24]]
#----------------------------------------------------------------------------------------------------------------
Q7 #How  to  print  reversed  object  in  different  ways  (Home  work)
import   time
a = input('Enter  any  string  :  ')  #  Assume  that  input  is  HYD
r = reversed(a)
print(type(r))
print(r)
print('Iterate  reversed  object  with   next   function')
while True:
	try:
		print(next(r))  #How  to  iterate  reversed  object  'r'  with  next()  function
		time.sleep(1)
	except:
		break
r = reversed(a)
print('Iterate  reversed  object  with   next   method')
while True: 
	try:
		print(r.__next__())   #How  to  iterate  reversed  object   with  next()   method
		time.sleep(1)
	except:
		break
print('Iterate  reversed  object  with   for  loop')
for r in reversed(a):   #How  to  iterate  reversed  object   with  for  loop
	print(r)
	time.sleep(1)
print('Unpack  reversed  object  with   *  operator :   ' ,*reversed(a))  #How  to   unpack  reversed  object   with  *  operator
print()
print('reversed  object  in  the  form   of  list  :  ' ,  list(reversed(a)))  #How  to  convert  reversed  object  to  list
print('Reverse  string   :   ' , ''.join(reversed(a))) #How  to  convert  reversed  object  to   string

OP-
Enter  any  string  :  Priya
<class 'reversed'>
<reversed object at 0x00000189FF35BFD0>
Iterate  reversed  object  with   next   function
a
y
i
r
P
Iterate  reversed  object  with   next   method
a
y
i
r
P
Iterate  reversed  object  with   for  loop
a
y
i
r
P
Unpack  reversed  object  with   *  operator :    a y i r P

reversed  object  in  the  form   of  list  :   ['a', 'y', 'i', 'r', 'P']
Reverse  string   :    ayirP
#---------------------------------------------------------------------------------------
Q8 #Find  outputs (Home  work)
a = 'RAMA'
b = reversed(a)
print(type(b))  #<class 'reversed'>
print(b)        #<reversed object at 0x0000017DDAF0BFD0>
print(id(b))    #1640055750608
print(*b)       #A M A R
#print(b[0])     #error- reversed iterator does not have index
#print(b[1 : 3]) #error- reversed iterator does not support slicing
#print(b * 2)    #error- iterators cannot be repeated
#print(len(b))   #error- reversed is empty does not have length
#------------------------------------------------------------------------------------
Q9 # Can  tuple  be  reversed ?  

import   time
a = (25 , 10.8 , 'Hyd' , True)
b = reversed(a)
print(type(b))
for  x  in   b:
	print(x)
	time . sleep(1)

OP-
<class 'reversed'>
True
Hyd
10.8
25
#------------------------------------------------------------------------------
Q10 #Can  dictionary  be  reversed  ? (Home  work)
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

OP-
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
10
#-----------------------------------------------------------------------------------------------
Q11 #Write  a  program  to  reverse  a  dictionary ?

Let  input  be  {'Empno' : 25 , 'Emp Name' : 'Rama  Rao' , 'Sal' : 10000.0}
What  is  the  output  ?  --->  {'Sal' : 10000.0 , 'Emp  Name' :  Rama  Rao' , 'Empno' : 25}
Hint:  Use  reversed  iterator


a=eval(input('Enter dictionary : '))
print('Reverse dictionary : ',dict(reversed(a.items())))

OP-
Enter dictionary : {'Empno' : 25 , 'Emp Name' : 'Rama  Rao' , 'Sal' : 10000.0}
Reverse dictionary :  {'Sal': 10000.0, 'Emp Name': 'Rama  Rao', 'Empno': 25}
#--------------------------------------------------------------------------------------------
Q12 #Find outputs
import  time
a = {10 : 'Rama rao', 20 : 'Sita', 15 : 'Rajesh', 18 : 'Kiran'}
print('Keys  in   reverse   order')
for x in reversed(a):   #Write  for  loop  to  reverse  keys  of  dictionary
	print(x)
	time.sleep(1)
print('Values  in  reverse  order')
for x in reversed(a.values()):   #Write  for  loop  to  reverse  values  of  dictionary
	print(x)
	time.sleep(1)
print('Tuples  in   reverse  order')
for x in reversed(a.items()):     #Write  for  loop  to  reverse   tuples   of  dictionary
	print(x)
	time.sleep(1)
print('Elements  of  each   tuple  in  reverse  order')
for x,y in reversed(a.items()):   #Write  for  loop  to  reverse   elements  of   each   tuple  of  dictionary
	print(x,y,sep=':')
	time.sleep(1)
print('Keys  and  values  in   reverse   order')
for x in reversed(a.keys()):    #Write  for  loop  to  print  each   key  and   the  corresponding  value  of  dictionary  in  reverse  order
	print(x,a[x],sep=':')
	time.sleep(1)

OP-
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
(18, 'Kiran')
(15, 'Rajesh')
(20, 'Sita')
(10, 'Rama rao')
Elements  of  each   tuple  in  reverse  order
18:Kiran
15:Rajesh
20:Sita
10:Rama rao
Keys  and  values  in   reverse   order
18:Kiran
15:Rajesh
20:Sita
10:Rama rao
#--------------------------------------------------------------------------------------------------
Q13 #How  to  print  list_reverseiterator  object  in  different  ways  (Home   work)
import   time
a = [25 , 10.8 , 'Hyd' , True]
r = reversed(a)
print(type(r))
print(r)
print('Iterate  list_reverseiterator  object  with   next()   function')
while True:
	try:
		print(next(r))   #How  to  iterate   list_reverseiterator  object  with   next()   function
		time.sleep(1)
	except:
		break
rev_itr=reversed(a)
print('Iterate  list_reverseiterator  object  with   next()   method')
while True:
	try:
		print(rev_itr.__next__())  #How  to  iterate   list_reverseiterator  object  with   next()  method
		time.sleep(1)
	except:
		break
print('Iterate  list_reverseiterator  object  with   for  loop')
for x in reversed(a):   #How  to  iterate   list_reverseiterator  object  with   for  loop
	print(x)
	time.sleep(1)
print('Unpack  list_reverseiterator  object  with     operator   :  ' , *reversed(a))   #How  to  unpack   list_reverseiterator  object   with     operator
print()
print('Reverse  list  :  '  ,list(reversed(a)) )  # How  to  convert  list_reverseiterator  object  to  list

OP-
<class 'list_reverseiterator'>
<list_reverseiterator object at 0x00000153D872BFD0>
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
#----------------------------------------------------------------------------------------------
Q14 #How  to  iterate   list_iterator  in  different  ways
import   time
list  =  [10  ,  20  ,  15  ,  18]
print('Iterate  list  with  for  loop')
for x in list:    #How  to  iterate  list  with  for  loop
	print(x)
#print(next(list))  #error- for next argument must be iterator but not sequence
list_itr = iter(list)
print(type(list_itr))
print(list_itr)
print('Iterate  List_iterator  with  next()  function')
while True:  #How  to  iterate  list_iterator  with  next()  function
	try:
		print(next(list_itr))
		time.sleep(1)
	except:
		break
print('Iterate  List_iterator  with   _next_()  method')
list_itr = iter(list)
while True:
	try:
		print(list_itr.__next__())    #How  to  iterate  list_iterator  with   _next_  method
		time.sleep(1)
	except:
		break
print('Iterate  List_iterator  with   for    loop')
for x in iter(list):    #How  to  iterate  list_iterator  with  for  loop
	print(x)
	time.sleep(1)
print('Unpacks  List_iterator  with  *  operator  :    ' ,  *iter(list) )  #How  to  unpack  list_iterator

OP-
Iterate  list  with  for  loop
10
20
15
18
<class 'list_iterator'>
<list_iterator object at 0x000002A0EE60BFD0>
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
#------------------------------------------------------------------------------------
Q15 #Find  outputs
a = 25
print(a)   #25
'''
for  x   in   a:
	print(x)    #error - 25 is not sequence and not iterator
print(iter(a))  #25 is not a sequence
print(next(a))  #25 is not iterator
'''
