#  How  to  iterate  zip  object  in  differenet  ways  (Home  work)
'''
import   time
a = ['Telangana' , 'Andhra Pradesh' , 'Karnataka ', 'Tamilnadu']
b = ['Hyderabad' , 'Amaravathi' , 'Bangalore', 'Chennai']
z = zip(a , b)  #  Creates  an  empty  zip  class  object
print(type(z)) # <class  'zip'>
print(z) # _str_()  returns  type and address of the object
print('Iterate  zip  object  with   next()   function')
while   True:  # How  to   iterate  zip  object  with  next  function
	try:
		print(next(z))  #  ('Telangana', 'Hyderabad')  <next  line>  ('Andhra Pradesh', 'Amaravathi')  <next  line>  ('Karnataka ', 'Bangalore')  <next  line>  ('Tamilnadu', 'Chennai')
		time . sleep(1)
	except  StopIteration:
		break
print('Iterate  zip  object  with  _next_  method')
z = zip(a , b)  #   Creates  another  zip  object  to  iterate  again
while   True:  #How  to   iterate  zip  object  with  _next_  method
	try:
		print(z . _next_()) #  ('Telangana', 'Hyderabad')  <next  line>  ('Andhra Pradesh', 'Amaravathi')  <next  line>  ('Karnataka ', 'Bangalore')  <next  line>  ('Tamilnadu', 'Chennai')
		time . sleep(1)
	except:
		break
print('Iterate  zip  object  with   for  loop')
for  x  in   zip(a , b):  #  Creates  another  zip  object  to  iterate  again  with  for  loop
	print(x)  #  ('Telangana', 'Hyderabad')  <next  line>  ('Andhra Pradesh', 'Amaravathi')  <next  line>  ('Karnataka ', 'Bangalore')  <next  line>  ('Tamilnadu', 'Chennai')
	time . sleep(1)
print('Iterate  elements  of  each  tuple  in  zip  object')
for x , y in  zip(a , b):  #  x  and  y  are  elements  of  each  tuple  yielded  by  zip   iterator
	print(x , y, sep = '...')  #  Telangana ... Hyderabad <next  line>  Andhra Pradesh ... Amaravathi  <next  line>  Karnataka ... Bangalore  <next  line>  Tamilnadu ... Chennai
	time . sleep(1)
print('Unpacks  zip  object  with   *  operator')
print(*zip(a , b)) #  All  the  tuples  are  stored  in   zip  object  which  are   unpacked  i.e.('Telangana', 'Hyderabad')  <space>  ('Andhra Pradesh', 'Amaravathi')  <space>  ('Karnataka ', 'Bangalore')  <space>  ('Tamilnadu', 'Chennai')
print()
print('zip   object  in  the  form  of   list')
print(list(zip(a , b))) # All  the  tuples  are  stored  in   zip  object  which   is  converted  to  list  i.e. [('Telangana', 'Hyderabad'), ('Andhra Pradesh', 'Amaravathi'), ('Karnataka ', 'Bangalore'), ('Tamilnadu', 'Chennai')]
print()
print('zip   object  in  the  form  of   dictionary')
print(dict(zip(a , b))) # All  the  tuples  are  stored  in   zip  object  which   is  converted  to   dictionary  i.e.  {'Telangana': 'Hyderabad', 'Andhra Pradesh': 'Amaravathi', 'Karnataka ': 'Bangalore', 'Tamilnadu': 'Chennai'}

output:
<class 'zip'>
<zip object at 0x0000028696E1FDC0>
Iterate  zip  object  with   next()   function
('Telangana', 'Hyderabad')
('Andhra Pradesh', 'Amaravathi')
('Karnataka ', 'Bangalore')
('Tamilnadu', 'Chennai')
Iterate  zip  object  with  _next_  method
Iterate  zip  object  with   for  loop
('Telangana', 'Hyderabad')
('Andhra Pradesh', 'Amaravathi')
('Karnataka ', 'Bangalore')
('Tamilnadu', 'Chennai')
Iterate  elements  of  each  tuple  in  zip  object
Telangana...Hyderabad
Andhra Pradesh...Amaravathi
Karnataka ...Bangalore
Tamilnadu...Chennai
Unpacks  zip  object  with   *  operator
('Telangana', 'Hyderabad') ('Andhra Pradesh', 'Amaravathi') ('Karnataka ', 'Bangalore') ('Tamilnadu', 'Chennai')

zip   object  in  the  form  of   list
[('Telangana', 'Hyderabad'), ('Andhra Pradesh', 'Amaravathi'), ('Karnataka ', 'Bangalore'), ('Tamilnadu', 'Chennai')]

zip   object  in  the  form  of   dictionary
{'Telangana': 'Hyderabad', 'Andhra Pradesh': 'Amaravathi', 'Karnataka ': 'Bangalore', 'Tamilnadu': 'Chennai'}
'''


#  Find  outputs  (Home  work)
'''
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

output:
('Empno', 25)
('Emp Name', 'Rama  Rao')
('Salary', 10000.0)
'''


#  Find  outputs  (Home  work)
'''
import   time
a = ['Telangana' , 'Andhra  Pradesh' , 'Karnataka' , 'TamilNadu' , 'Maharastra']
b = ['Hyderabad' , 'Amaravathi' , 'Banglore' , 'Chennai' , 'Mumbai']
c = [50000000 , 40000000 , 70000000 , 60000000 , 30000000]
for   x   in   zip(a , b , c):
	print(x)
	time . sleep(1)

output:
('Telangana', 'Hyderabad', 50000000)
('Andhra  Pradesh', 'Amaravathi', 40000000)
('Karnataka', 'Banglore', 70000000)
('TamilNadu', 'Chennai', 60000000)
('Maharastra', 'Mumbai', 30000000)
'''


# Find  outputs   (Home  work)
'''
import   time
a = [1 , 2 , 3]
b = [4 , 5 , 6 , 7 , 8]
for  x , y  in   zip(a , b):
	print(x + y)
	time . sleep(1)

output:
5
7
9
'''


# Find outputs  (Home  work)
'''
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

output:
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
'''
z = zip(range(5) , range(20 , 25))
a = [ [x , y]  for  x , y   in   z]
print(a)

output:
[[0, 20], [1, 21], [2, 22], [3, 23], [4, 24]]
'''


#  How  to  print  reversed  object  in  different  ways  (Home  work)
'''
import   time
a = input('Enter  any  string  :  ')  #  Assume  that  input  is  HYD
r = reversed(a)  #   Creates  an  empty  reversed  object
print(type(r)) # <class  'reversed'>
print(r) # _str_()  returns type and address of the object
print('Iterate  reversed  object  with   next   function')
while   True:  #  How  to  iterate  reversed  object  'r'  with  next()  function
	try:
		print(next(r))   #  D  <next line>   Y  <next line>   H  <next line>
		time . sleep(1)
	except:
		break
print('Iterate  reversed  object  with   _next_   method')
r = reversed(a)  #  Creates   another  reversed  object  to  iterate  again
while   True:  #How  to  iterate  reversed  object   with  _next_()   method
	try:
		print(r . _next_())    #  D  <next line>   Y  <next line>   H  <next line>  StopIteration
		time . sleep(1)
	except:
		break
print('Iterate  reversed  object  with   for  loop')
for  x  in   reversed(a):  #  Creates  another  reversed  to  iterate  with  for  loop
	print(x)    #  D  <next line>   Y  <next line>   H  <next line>
	time . sleep(1)
print('Unpack  reversed  object  with   *  operator :   ' , *reversed(a)) #   Srores  all  the  characters  of  the  string  in  reverse  order  in  reversed  object  and  unpacks   i.e.  D  <space>   Y  <space>   H  <next line>
print('reversed  object  in  the  form   of  list  :  ' , list(reversed(a))) #  Srores  all  the  characters  of  the  string  in  reverse  order  in  reversed  object  and   converted  to  list   i.e.   ['D' , 'Y' , 'H']
print('Reverse  string   :   ' , '' . join(reversed(a)))  #  Stores  all  the all  the  characters  of  the  string  in  reverse  order  in  reversed  object  and  joined  to  form  a   string  i.e.   ['D' , 'Y' , 'H']How  to  convert  reversed  object  to   string  --->  DYH

output:
Enter  any  string  :  Rama Rao
<class 'reversed'>
<reversed object at 0x000002D7105FB220>
Iterate  reversed  object  with   next   function
o
a
R

a
m
a
R
Iterate  reversed  object  with   _next_   method
Iterate  reversed  object  with   for  loop
o
a
R

a
m
a
R
Unpack  reversed  object  with   *  operator :    o a R   a m a R
reversed  object  in  the  form   of  list  :   ['o', 'a', 'R', ' ', 'a', 'm', 'a', 'R']
Reverse  string   :    oaR amaR
'''


# Find  outputs (Home  work)
'''
a = 'RAMA'
b = reversed(a)
print(type(b)) # <class 'reversed'>
print(b) #<reversed object at 0x000002314571AB60>
print(id(b)) # 2410641730400
print(*b) # A M A R
#print(b[0])
#print(b[1 : 3])
#print(b * 2)
#print(len(b))

output:
<class 'reversed'>
<reversed object at 0x000002314571AB60>
2410641730400
A M A R
'''


# Can  tuple  be  reversed ?   (Home  work)
'''
import   time
a = (25 , 10.8 , 'Hyd' , True)
b = reversed(a) 
print(type(b)) # <class 'reversed'>
for  x  in   b:
	print(x)
	time . sleep(1)

output:
<class 'reversed'>
True
Hyd
10.8
25
'''


# Can  dictionary  be  reversed  ? (Home  work)
'''
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

output:
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
'''


#Write  a  program  to  reverse  a  dictionary ?
'''
Let  input  be  {'Empno' : 25 , 'Emp Name' : 'Rama  Rao' , 'Sal' : 10000.0}
What  is  the  output  ?  --->  {'Sal' : 10000.0 , 'Emp  Name' :  Rama  Rao' , 'Empno' : 25}

Hint:  Use  reversed  iterator

a=eval(input("Enter a dictionary :  "))
print('Reverse  dictionary  :  ' ,  dict(reversed(a . items())))

 output:
Enter a dictionary :  {'Empno' : 25 , 'Emp Name' : 'Rama  Rao' , 'Sal' : 10000.0}
Reverse  dictionary  :   {'Sal': 10000.0, 'Emp Name': 'Rama  Rao', 'Empno': 25}
'''

# Find outputs
'''
import  time
a = {10 : 'Rama rao', 20 : 'Sita', 15 : 'Rajesh', 18 : 'Kiran'}
print('Keys  in   reverse   order')
Write  for  loop  to  reverse  keys  of  dictionary
print('Values  in  reverse  order')
Write  for  loop  to  reverse  values  of  dictionary
print('Tuples  in   reverse  order')
Write  for  loop  to  reverse   tuples   of  dictionary
print('Elements  of  each   tuple  in  reverse  order')
Write  for  loop  to  reverse   elements  of   each   tuple  of  dictionary
print('Keys  and  values  in   reverse   order')
Write  for  loop  to  print  each   key  and   the  corresponding  value  of  dictionary  in  reverse  order
#  Write  outputs  here
'''


#  How  to  print  list_reverseiterator  object  in  different  ways  (Home   work)
'''
import   time
a = [25 , 10.8 , 'Hyd' , True]
r = reversed(a)  #  Creates  an  empty  list_reverseiterator  object
print(type(r)) # <class 'list_reverseiterator'>
print(r) # _str_()  returns type and address of  object  'r'
print('Iterate  list_reverseiterator  object  with   next()   function')
while   True:   # How  to  iterate   list_reverseiterator  object  with   next()   function
	try:
		print(next(r))  #  True  <next line>  Hyd  <next line>  10.8  <next line>   25  <next line>
		time . sleep(1)
	except:
		break
print('Iterate  list_reverseiterator  object  with   _next_()   method')
r = reversed(a)  #  Creates  another  object to  iterate  again
while   True:  # How  to  iterate   list_reverseiterator  object  with   _next_()  method
	try:
		print(r._next_()) #  True  <next line>  Hyd  <next line>  10.8  <next line>   25  <next line>
		time . sleep(1)
	except:
		break
print('Iterate  list_reverseiterator  object  with   for  loop')
for  x  in   reversed(a):  #   Creates   another  list_reverseiterator  object   to  iterate  with  for  loop
	print(x)  #  True  <next line>  Hyd  <next line>  10.8  <next line>   25  <next line>
	time . sleep(1)
print('Unpack  list_reverseiterator  object  with   *  operator   :  ' , *reversed(a)) #  Stores  all   the  elements  in  reverse  order  in  list_reverseiterator  object  and  unpacks
														#  i.e.  True  <space>  Hyd  <space>  10.8  <space>   25  <next line>
print('Reverse  list  :  '  ,  list(reversed(a))) #   Stores  all   the  elements  in  reverse  order  in  list_reverseiterator  object  and   converted  to  list  i.e.   [True , 'Hyd' , 10.8  ,   25]
 
 output:
<class 'list_reverseiterator'>
<list_reverseiterator object at 0x000002BEDE63B220>
Iterate  list_reverseiterator  object  with   next()   function
True
Hyd
10.8
25
Iterate  list_reverseiterator  object  with   _next_()   method
Iterate  list_reverseiterator  object  with   for  loop
True
Hyd
10.8
25
Unpack  list_reverseiterator  object  with   *  operator   :   True Hyd 10.8 25
Reverse  list  :   [True, 'Hyd', 10.8, 25]
'''

# How  to  iterate   list_iterator  in  different  ways
'''
import   time
list  =  [10  ,  20  ,  15  ,  18]
print('Iterate  list  with  for  loop')
for x in list:  #  'x'  is  each  element  of  the  list
	print(x)  #  10  <next  line>  20   <next  line>  15 <next  line> 18 <next  line>
#print(next(list)) #  Error :  list is  not  an  iterator
list_itr  =  iter(list)  #  Converts  list  to  list_iterator
print(type(list_itr)) # <class 'list_iterator'>
print(list_itr) # _str_() method  returns type and address  of  list_itr
print('Iterate  List_iterator  with  next()  function')
while   True:  # How  to  iterate  list_iterator  with  next()  function
	try:
		print(next(list_itr))  #  10  <next  line>  20   <next  line>  15 <next  line> 18 <next  line>
		time . sleep(1)
	except  StopIteration:
		break
print('Iterate  List_iterator  with   _next_()  method')
list_itr  =  iter(list)  # Convert  again  to  iterate  one  more  time
while   True:  #How  to  iterate  list_iterator  with   next  method
	try:
		print(list_itr  . _next_())  #  10  <next  line>  20   <next  line>  15 <next  line> 18 <next  line>
		time . sleep(1)
	except:
		break
print('Iterate  List_iterator  with   for    loop')
for  x  in  iter(list):  #How  to  iterate  list_iterator  with  for  loop
	print(x)  #  10  <next  line>  20   <next  line>  15 <next  line> 18 <next  line>
	time . sleep(1)
print('Unpacks  List_iterator  with  *  operator')
print(*iter(list)) # How  to  unpack  list_iterator    --->   #  10  <space>  20   <space>  15 <space> 18
 
 output:
Iterate  list  with  for  loop
10
20
15
18
<class 'list_iterator'>
<list_iterator object at 0x000001B99C98B4F0>
Iterate  List_iterator  with  next()  function
10
20
15
18
Iterate  List_iterator  with   _next_()  method
Iterate  List_iterator  with   for    loop
10
20
15
18
Unpacks  List_iterator  with  *  operator
10 20 15 18
'''


# Find  outputs
'''
a = 25
print(a) # 25
#for  x   in   a: # a is in integer Error
	#print(x)
#print(iter(a)) # iter function doesn't converts into non-seq
#print(next(a)) # only seq  can be converted but not non-seq
'''
