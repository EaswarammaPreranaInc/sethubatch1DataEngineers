 '''
#1) Find  outputs  (Home  work)
import   time
a = [ 'Empno' , 'Emp Name' , 'Salary']
b = [ 25 , 'Rama  Rao' , 10000.0 , 'Male' , True]
c = zip(a , b) # join the sequences 'a' and 'b' based on smallest sequence
while   True:
	try:
		print(next(c))
		time . sleep(1)
	except:
		break

output:-
---------
('Empno', 25) --- 1st iteration
('Emp Name', 'Rama  Rao')---> 2nd iteration
('Salary', 10000.0)---> 3rd  iteration


#2)Find  outputs  (Home  work)
import   time
a = ['Telangana' , 'Andhra  Pradesh' , 'Karnataka' , 'TamilNadu' , 'Maharastra']
b = ['Hyderabad' , 'Amaravathi' , 'Banglore' , 'Chennai' , 'Mumbai']
c = [50000000 , 40000000 , 70000000 , 60000000 , 30000000]
for   x   in   zip(a , b , c):# join the sequences 'a', 'b'and 'c' based on smallest sequence
	print(x)
	time . sleep(1)
output:-
--------
('Telangana', 'Hyderabad', 50000000)
('Andhra  Pradesh', 'Amaravathi', 40000000)
('Karnataka', 'Banglore', 70000000)
('TamilNadu', 'Chennai', 60000000)
('Maharastra', 'Mumbai', 30000000)

#3) import   time
a = ['Telangana' , 'Andhra Pradesh' , 'Karnataka ', 'Tamilnadu']
b = ['Hyderabad' , 'Amaravathi' , 'Bangalore', 'Chennai']
z = zip(a , b) # join the sequences 'a', 'b'and 'c' based on smallest sequence
print(type(z)) # <class 'zip'>
print(z)
print('Iterate  zip  object  with   next()   function')
while True:
	try:
		print(next(z))
		time . sleep(1)
	except StopIteration:
		break # How  to   iterate  zip  object  with  next  function
print('Iterate  zip  object  with  next  method')
Z = zip(a, b )
while True:
	try:
		print(z._next_())
		time . sleep(1)
	except StopIteration:
		break # How  to   iterate  zip  object  with  next  method
print('Iterate  zip  object  with   for  loop')
z = zip(a, b)
for x in zip(a , b):
	print(x)
	time .sleep (1)#How  to   iterate  zip  object  with  for  loop
print('Iterate  elements  of  each  tuple  in  zip  object')
z = zip(a, b)
for x , y  in zip(a ,b):
	print(x , y , sep = '....')
	time . sleep (1)# How  to   iterate  elements  of  each  tuple  of  zip  object  with  for  loop

z = zip(a, b)
print('Unpacks  zip  object  with   *  operator :  ' , zip( *z)) # How  to   unpack  zip  object   with  *  operator
print(*zip(a , b))
print()
z = zip(a, b)
print('zip   object  in  the  form  of   list  :  ' ,list(z)) #  How  to  convert  zip  object  to  list)
print()
z = zip(a, b)
print('zip   object  in  the  form  of   dictionary :  ' , dict (z)) # How  to  convert  zip  object  to  dictionary)
#  Write  all  the  outputs  here

output:-
-----------
<class 'zip'>
<zip object at 0x0000024D28ADFE00>
Iterate  zip  object  with   next()   function
('Telangana', 'Hyderabad')
('Andhra Pradesh', 'Amaravathi')
('Karnataka ', 'Bangalore')
('Tamilnadu', 'Chennai')
Iterate  zip  object  with  next  method
Iterate  zip  object  with   for  loop
('Telangana', 'Hyderabad')
('Andhra Pradesh', 'Amaravathi')
('Karnataka ', 'Bangalore')
('Tamilnadu', 'Chennai')
Iterate  elements  of  each  tuple  in  zip  object
Telangana....Hyderabad
Andhra Pradesh....Amaravathi
Karnataka ....Bangalore
Tamilnadu....Chennai
Unpacks  zip  object  with   *  operator :   <zip object at 0x0000024D28ADFE00>
('Telangana', 'Hyderabad') ('Andhra Pradesh', 'Amaravathi') ('Karnataka ', 'Bangalore') ('Tamilnadu', 'Chennai')

zip   object  in  the  form  of   list  :   [('Telangana', 'Hyderabad'), ('Andhra Pradesh', 'Amaravathi'), ('Karnataka ', 'Bangalore'), ('Tamilnadu', 'Chennai')]

zip   object  in  the  form  of   dictionary :   {'Telangana': 'Hyderabad', 'Andhra Pradesh': 'Amaravathi', 'Karnataka ': 'Bangalore', 'Tamilnadu': 'Chennai'}



#4) Find  outputs   (Home  work)
import   time
a = [1 , 2 , 3]
b = [4 , 5 , 6 , 7 , 8]
for  x , y  in   zip(a , b):# join the sequences 'a', 'b'and 'c' based on smallest sequence
	print(x + y) # adds 'x'elements of 'a' with 'y' elements of 'b'
	time . sleep(1)
output:-
------
5 ----> ist iteration ----(1+4)
7 ----> 2nd iteration ----(2+5)
9 ----> 3rd iteration ----(3+6)

#5)Find outputs  (Home  work)
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
c = zip(a , b . keys())  # join the sequences 'a' with elements and 'b'with keys() based on smallest sequence
disp(c)
d = zip(a , b . values())# join the sequences 'a'with elements and 'b'with values() based on smallest sequence
disp(d)
e = zip(a , b . items())# join the sequences 'a'with elements and 'b'with both keys() and values() based on smallest sequence.
disp(e)
f = zip(a , b)# join the sequences 'a'with elements and 'b' with keys(by default keys() method executes) based on smallest sequence
disp(f)
g = zip(a) # join the sequences 'a'
disp(g)
h = zip(b) # join the sequences 'b'with keys() (by default keys() method executes)
disp(h)
i = zip()
disp(i) # # join nothing bcz zip has no arguments.

output:-
--------
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

#6)Find  outputs  (Home  work)
z = zip(range(5) , range(20 , 25)) # list of list is created with 1st element of inside list is index stats from 0 and 2nd element of list is element starts from 20.
a = [ [x , y]  for  x , y   in   z]
print(a) # [[0, 20], [1, 21], [2, 22], [3, 23], [4, 24]]
output:-
---------
[[0, 20], [1, 21], [2, 22], [3, 23], [4, 24]]


#7) How  to  print  reversed  object  in  different  ways  (Home  work)
import   time
a = input('Enter  any  string  :  ')  #  Assume  that  input  is  HYD
r = reversed(a)
print(type(r))
print(next(r))
print(next(r))
print(next(r))
print(next(r))
print('Iterate  reversed  object  with   next   function')
r = reversed(a)
while True:
	try:
		print(next(r))
		time . sleep(1)
	except StopIteration:
		break 
#How  to  iterate  reversed  object  'r'  with  next()  function
print('Iterate  reversed  object  with   next   method')
r = reversed(a)
while True:
	try:
		print(r.__next__())
		time . sleep(1)
	except StopIteration:
		break 
# How  to  iterate  reversed  object   with  next()   method
print('Iterate  reversed  object  with   for  loop')
r = reversed(a)
for ch in r:
    print(ch, end=' ') # How  to  iterate  reversed  object   with  for  loop
print()
print()
print('Unpack  reversed  object  with   *  operator :   ' ,  end=' ') 
r = reversed(a)
print(*r) # How  to   unpack  reversed  object   with  *  operator)
print()
print('reversed  object  in  the  form   of  list  :  ' ,end=' ')
r = reversed(a)
print(list(r)) # How  to  convert  reversed  object  to  list)
print()
print('Reverse  string   :   ' , end=' ')
r = reversed(a)
print(''.join(r)) #How  to  convert  reversed  object  to   string)
#  Write all  the  outputs  here


output:-
-----------
Enter  any  string  :  DELL
<class 'reversed'>
L
L
E
D
Iterate  reversed  object  with   next   function
L
L
E
D
Iterate  reversed  object  with   next   method
L
L
E
D
Iterate  reversed  object  with   for  loop
L L E D

Unpack  reversed  object  with   *  operator :    L L E D

reversed  object  in  the  form   of  list  :   ['L', 'L', 'E', 'D']

Reverse  string   :    LLED



#8)Find  outputs (Home  work)
a = 'RAMA'
b = reversed(a)
print(type(b)) # <class 'reversed'>
print(b) # <reversed object at 0x0000024C8DF2AB60>-----> Type and address of 'b'
print(id(b)) # 2527822261088-----> Address of 'b'
print(*b) # A M A R -----> unpacking
print(a)
#print(b[0]) # Error : 'reversed' object is not subscriptable
#print(b[1 : 3]) # Error : 'reversed' object is not subscriptable
#print(b * 2) # Error : 'reversed' object is not repeated.
#print(len(b)) # Error : 'reversed' object is no length function here

output:-
---------
<class 'reversed'>
<reversed object at 0x0000024C8DF2AB60>
2527822261088
A M A R

#9) Can  tuple  be  reversed ?   (Home  work)----> YES
import   time
a = (25 , 10.8 , 'Hyd' , True)
b = reversed(a)
print(type(b)) # <class 'reversed'>
for  x  in   b:iterates  'a' elements in reverse
	print(x)
	time . sleep(1)
output:-
--------
<class 'reversed'>
True ----> 1st iteration of for loop
Hyd ----> 2nd iteration of for loop
10.8 ----> 3rd  iteration of for loop
25 ----> 4th iteration of for loop


#10)Can  dictionary  be  reversed  ? (Home  work)----->YES
import   time
def   disp(r):
	while  True:# iterate  reversed  object in dictionarys 
		try:
			print(next(r))
			time . sleep(1)
		except:
			break
	print()
a = {10 : 'Rama' , 20 : 'Sita' , 15 : 'Kiran' , 18 : 'Amar'}
b = reversed(a . keys()) # iterate  reversed  object of keys ()method 
disp(b)
c = reversed(a . values()) # iterate  reversed  object of values ()method 
disp(c)
d = reversed(a . items())# iterate  reversed  object of items ()method 
disp(d)
e = reversed(a) # iterate  reversed  object of keys ()method (by default keys() executes)
disp(e)

output:-
---------
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

#11)Write  a  program  to  reverse  a  dictionary ?

Let  input  be  {'Empno' : 25 , 'Emp Name' : 'Rama  Rao' , 'Sal' : 10000.0}
What  is  the  output  ?  --->  {'Sal' : 10000.0 , 'Emp  Name' :  Rama  Rao' , 'Empno' : 25}

Hint:  Use  reversed  iterator

def disp():
    a = {'Empno': 25, 'Emp Name': 'Rama Rao', 'Sal': 10000.0}
    d = reversed(a.items()) # Convert items to list before reversing
    for k, v in d:
        print(k, ':', v)

disp()
output:-
-------
Sal : 10000.0
Emp Name : Rama Rao
Empno : 25

(or)

a = {'Empno': 25, 'Emp Name': 'Rama Rao', 'Sal': 10000.0}
d = dict(reversed(a.items())) # Use reversed iterator to reverse dictionary
print("Reversed dictionary:", d)# Print the reversed dictionary

output:-
--------
Reversed dictionary: {'Sal': 10000.0, 'Emp Name': 'Rama Rao', 'Empno': 25}

#12)Find outputs
import  time
a = {10 : 'Rama rao', 20 : 'Sita', 15 : 'Rajesh', 18 : 'Kiran'}
for key in reversed(a.keys()):
    print(key)
#Write  for  loop  to  reverse  keys  of  dictionary
for key in reversed(list(a.values())):
    #print(values)
	print('Values  in  reverse  order')
for key in reversed(list(a.items())):
    print(items)
#Write  for  loop  to  reverse  values  of  dictionary
print('Tuples  in   reverse  order')
#Write  for  loop  to  reverse   tuples   of  dictionary
print('Elements  of  each   tuple  in  reverse  order')
for key, value in reversed(list(a.items())):
    print(key, '->', value)

#Write  for  loop  to  reverse   elements  of   each   tuple  of  dictionary
print('Keys  and  values  in   reverse   order')

#Write  for  loop  to  print  each   key  and   the  corresponding  value  of  dictionary  in  reverse  order
#  Write  outputs  here


a = {10: 'Rama rao', 20: 'Sita', 15: 'Rajesh', 18: 'Kiran'}

print('Keys in reverse order')
for key in reversed(list(a.keys())):
    print(key)
print('Values in reverse order')
for value in reversed(list(a.values())):
    print(value)

print('Tuples in reverse order')
for item in reversed(list(a.items())):
    print(item)

print('Elements of each tuple in reverse order')
for item in reversed(list(a.items())):
    for element in reversed(item):
        print(element)
print('Keys and values in reverse order')
for key, value in reversed(list(a.items())):
    print(key, '->', value)

output:-
---------
Keys in reverse order
18
15
20
10
Values in reverse order
Kiran
Rajesh
Sita
Rama rao
Tuples in reverse order
(18, 'Kiran')
(15, 'Rajesh')
(20, 'Sita')
(10, 'Rama rao')
Elements of each tuple in reverse order
Kiran
18
Rajesh
15
Sita
20
Rama rao
10
Keys and values in reverse order
18 -> Kiran
15 -> Rajesh
20 -> Sita
10 -> Rama rao


#13)#  How  to  print  list_reverseiterator  object  in  different  ways  (Home   work)
import   time
a = [25 , 10.8 , 'Hyd' , True]
r = reversed(a)
print(type(r))
print(r)
print('Iterate  list_reverseiterator  object  with   next()   function')
while True:
	try:
		print(next(r))
		time . sleep(1)
	except StopIteration:
		break  # How  to  iterate   list_reverseiterator  object  with   next()   function
print('Iterate  list_reverseiterator  object  with   next()   method')
r = reversed(a)
while True:
	try:
		print(r.__next__())
		time . sleep(1)
	except StopIteration:
		break  #How  to  iterate   list_reverseiterator  object  with   next()  method
print('Iterate  list_reverseiterator  object  with   for  loop')
r = reversed(a)
for item in r:
    print(item) # How  to  iterate   list_reverseiterator  object  with   for  loop
print()
print('Unpack  list_reverseiterator  object  with     operator   :  ' )
r = reversed(a)
print(*r)
 #How  to  unpack   list_reverseiterator  object   with     operator)
print()
r = reversed(a)
print('Reverse  list  :  '  ) #  How  to  convert  list_reverseiterator  object  to  list)
print(list(r))

output:-
--------
<class 'list_reverseiterator'>
<list_reverseiterator object at 0x00000209A362B2E0>
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

Unpack  list_reverseiterator  object  with     operator   :
True Hyd 10.8 25

Reverse  list  :
[True, 'Hyd', 10.8, 25]

#14) How  to  iterate   list_iterator  in  different  ways
import   time
list  =  [10  ,  20  ,  15  ,  18]
print('Iterate  list  with  for  loop')
for item in list:
    print(item)
#How  to  iterate  list  with  for  loop
#print(next(list)) # Error: next(list)
list_itr = iter(list)
print(type(list_itr))
print(list_itr)
print('Iterate  List_iterator  with  next()  function')
list_itr = iter(list)
print(next(list_itr))  # Output: 10
print(next(list_itr))  # Output: 20
print(next(list_itr))  # Output: 15
print(next(list_itr))  # Output: 18
#How  to  iterate  list_iterator  with  next()  function
print('Iterate  List_iterator  with   next()  method')
list_itr = iter(list)
print(list_itr._next_())  # Output: 10
print(list_itr._next_())  # Output: 20
print(list_itr._next_())  # Output: 15
print(list_itr._next())  # How  to  iterate  list_iterator  with   _next  method
print('Iterate  List_iterator  with   for    loop')
list_itr = iter(list)
for item in list_itr:
    print(item) #How  to  iterate  list_iterator  with  for  loop
print('Unpacks  List_iterator  with  *  operator  :    ' ,   end = ' ') #How  to  unpack  list_iterator)
list_itr = iter(list)
print(*list_itr)

output:-
--------
Iterate  list  with  for  loop
10
20
15
18
<class 'list_iterator'>
<list_iterator object at 0x0000020C6CDAB8B0>
Iterate  List_iterator  with  next()  function
10
20
15
18
Iterate  List_iterator  with   next()  method
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
#15) Find  outputs
a = 25
print(a) # 25
#for  x   in   a:# Error for single object(non-sequence ) forloop is not executed
	#print(x)
#print(iter(a))# Error for single object(non-sequence ) iterator is not executed
#print(next(a)) # Error for single object(non-sequence ) iterator is not executed

output:-
-------
25