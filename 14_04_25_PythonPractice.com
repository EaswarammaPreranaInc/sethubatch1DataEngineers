#  How  to  iterate  zip  object  in  differenet  ways  (Home  work)
import   time
a = ['Telangana' , 'Andhra Pradesh' , 'Karnataka ', 'Tamilnadu']
b = ['Hyderabad' , 'Amaravathi' , 'Bangalore', 'Chennai']
z = zip(a , b)
print(type(z)) # <class 'zip'>
print(z) # Type and address of z
print('Iterate  zip  object  with   next()   function')
#How  to   iterate  zip  object  with  next  function
while True:
    try:
        print(next(z)) # ('Telangana','Hyderabad') <nxt line> ('Andhra Pradesh','Amaravathi') <nxt line> ('Karnataka','Bangalore') <nxt line> ('Tamilnadu','Chennai')
        time.sleep(1)
    except:
        break

print('Iterate  zip  object  with  next  method')
z = zip(a,b) #How  to   iterate  zip  object  with  next  method
while True:
    try:
        print(z.__next__())
        time.sleep(1)
    except:
        break
print('Iterate  zip  object  with   for  loop')
#How  to   iterate  zip  object  with  for  loop
for x in zip(a,b):
    print(x)
    time.sleep(1)
print('Iterate  elements  of  each  tuple  in  zip  object')
#How  to   iterate  elements  of  each  tuple  of  zip  object  with  for  loop
for x,y in zip(a,b):
    print(x,y,sep='...')
    time.sleep(1)
print('Unpacks  zip  object  with   *  operator  :  ') 
z = zip(a,b)# How  to   unpack  zip  object   with  *  operator
print(*z)
print()
print('zip   object  in  the  form  of   list  :  ') 
z = zip(a,b)# How  to  convert  zip  object  to  list
print(list(z))
print()
print('zip   object  in  the  form  of   dictionary :  ')
z = zip(a,b)# How  to  convert  zip  object  to  dictionary
print(dict(z))
'''o/p: Iterate  zip  object  with  next  method
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
        Telangana...Hyderabad
        Andhra Pradesh...Amaravathi
        Karnataka ...Bangalore
        Tamilnadu...Chennai
        Unpacks  zip  object  with   *  operator  :  
        ('Telangana', 'Hyderabad') ('Andhra Pradesh', 'Amaravathi') ('Karnataka ', 'Bangalore') ('Tamilnadu', 'Chennai')

        zip   object  in  the  form  of   list  :
        [('Telangana', 'Hyderabad'), ('Andhra Pradesh', 'Amaravathi'), ('Karnataka ', 'Bangalore'), ('Tamilnadu', 'Chennai')]

        zip   object  in  the  form  of   dictionary :
        {'Telangana': 'Hyderabad', 'Andhra Pradesh': 'Amaravathi', 'Karnataka ': 'Bangalore', 'Tamilnadu': 'Chennai'} '''
#  Write  all  the  outputs  here
#  Find  outputs  (Home  work)
import   time
a = [ 'Empno' , 'Emp Name' , 'Salary']
b = [ 25 , 'Rama  Rao' , 10000.0 , 'Male' , True]
c = zip(a , b)
while   True:
	try:
		print(next(c)) # ('Empno',25) <nxt line> ('Emp Name','Rama Rao') <nxt line> ('Salary',10000.0)
		time . sleep(1)
	except:
		break
#  Find  outputs  (Home  work)
import   time
a = ['Telangana' , 'Andhra  Pradesh' , 'Karnataka' , 'TamilNadu' , 'Maharastra']
b = ['Hyderabad' , 'Amaravathi' , 'Banglore' , 'Chennai' , 'Mumbai']
c = [50000000 , 40000000 , 70000000 , 60000000 , 30000000]
for   x   in   zip(a , b , c):
	print(x) # ('Telangana','Hyderabad',50000000) <nxt line> ('Andhra Pradesh','Amaravathi',40000000) <nxt line> ('Karnataka','Bangalore',70000000) <nxt line> ('Tamilnadu','Chennai',60000000) <nxt line> ('Maharastra','Mumbai',30000000)
	time . sleep(1)
# Find  outputs   (Home  work)
import   time
a = [1 , 2 , 3]
b = [4 , 5 , 6 , 7 , 8]
for  x , y  in   zip(a , b):
	print(x + y) # (5) <nxt line> (7) <nxt line> (9)
	time . sleep(1)
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
disp(c) # (10,1)  <nxt line> (20,3) <nxt line> (30,5)
d = zip(a , b . values())
disp(d) # (10,2)  <nxt line> (20,4) <nxt line> (30,6)
e = zip(a , b . items())
disp(e) # (10,(1,2))  <nxt line> (20,(3,4)) <nxt line> (30,(5,6))
f = zip(a , b)
disp(f) # (10,1)  <nxt line> (20,3) <nxt line> (30,5)
g = zip(a)
disp(g) # 10, <nxt line> 20, <nxt line> 30,
h = zip(b)
disp(h) # 1, <nxt line> 3, <nxt line> 5,
i = zip()
disp(i) # StopIterationError
# Find  outputs  (Home  work)
z = zip(range(5) , range(20 , 25))
a = [ [x , y]  for  x , y   in   z]
print(a) # [[0,20] ,[1,21],[2,22],[3,23],[4,24]]
#  How  to  print  reversed  object  in  different  ways  (Home  work)
import   time
a = input('Enter  any  string  :  ')  #  Assume  that  input  is  HYD
r = reversed(a)
print(type(r)) # <class 'reversed'>
print(r) # Type and address of r
print('Iterate  reversed  object  with   next   function')
while True:#How  to  iterate  reversed  object  'r'  with  next()  function
	try:
		print(next(r))
		time.sleep(1)
	except:
	    break

print('Iterate  reversed  object  with   next   method')
r = reversed(a)#How  to  iterate  reversed  object   with  next()   method
while True:
	try:
		print(r.__next__())
		time.sleep(1)
	except:
		break	
print('Iterate  reversed  object  with   for  loop')
r = reversed(a)#How  to  iterate  reversed  object   with  for  loop
for x in r:
	print(x)
	time.sleep(1)
print('Unpack  reversed  object  with   *  operator :   ') 
r = reversed(a)# How  to   unpack  reversed  object   with  *  operator
print(*r)
print()
print('reversed  object  in  the  form   of  list  :  ') 
r = reversed(a)# How  to  convert  reversed  object  to  list
print(list(r))
print('Reverse  string   :   ') 
r = reversed(a)# How  to  convert  reversed  object  to   string
print(''.join(reversed(a)))

#  Write all  the  outputs  here
# Find  outputs (Home  work)
a = 'RAMA'
b = reversed(a) # creates empty objct
print(type(b)) # <class 'reversed'>
print(b) # Type and address of b
print(id(b)) # Address of b
print(*b) # Unpacks b A M A R
#print(b[0]) # No Indexing because iterator have no index
#print(b[1 : 3]) # No Slicing
#print(b * 2) # No repetation
#print(len(b)) # No it is not sequence
# Can  tuple  be  reversed ?   (Home  work)
import   time
a = (25 , 10.8 , 'Hyd' , True)
b = reversed(a) # creates empty objct
print(type(b)) # <class 'reversed'>
for  x  in   b:
	print(x) # True <nxt line> Hyd <nxt line> 10.8 <nxt line> 25
	time . sleep(1)
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
b = reversed(a . keys()) # creates empty objt
disp(b) # 18 <nxt line> 15 <nxt line> 20 <nxt line> 10
c = reversed(a . values())
disp(c) # Amar <nxt line> Kiran <nxt line> Sita <nxt line> Rama
d = reversed(a . items())
disp(d) # (18,Amar) <nxt line> (15,Kiran) <nxt line> (20,Sita) <nxt line> (10,Amar)
e = reversed(a)
disp(e) # 18 <nxt line> 15 <nxt line> 20 <nxt line> 10
'''
Write  a  program  to  reverse  a  dictionary ?

Let  input  be  {'Empno' : 25 , 'Emp Name' : 'Rama  Rao' , 'Sal' : 10000.0}
What  is  the  output  ?  --->  {'Sal' : 10000.0 , 'Emp  Name' :  Rama  Rao' , 'Empno' : 25}

Hint:  Use  reversed  iterator
'''
a = eval(input('Enter a dictionary : ')) # {'Empno' : 25 , 'Emp Name' : 'Rama  Rao' , 'Sal' : 10000.0}
print('Reverse  dictionary  :', dict(reversed(a.items())))  #{'Sal': 10000.0, 'Emp Name': 'Rama  Rao', 'Empno': 25}
# Find outputs
import  time
a = {10 : 'Rama rao', 20 : 'Sita', 15 : 'Rajesh', 18 : 'Kiran'}
print('Keys  in   reverse   order')
#Write  for  loop  to  reverse  keys  of  dictionary
print('Values  in  reverse  order')
#Write  for  loop  to  reverse  values  of  dictionary
print('Tuples  in   reverse  order')
#Write  for  loop  to  reverse   tuples   of  dictionary
print('Elements  of  each   tuple  in  reverse  order')
#Write  for  loop  to  reverse   elements  of   each   tuple  of  dictionary
print('Keys  and  values  in   reverse   order')
#Write  for  loop  to  print  each   key  and   the  corresponding  value  of  dictionary  in  reverse  order
#  Write  outputs  here
#  How  to  print  list_reverseiterator  object  in  different  ways  (Home   work)
import   time
a = [25 , 10.8 , 'Hyd' , True]
r = reversed(a) # creates empty objct
print(type(r)) # <class 'reversed'>
print(r) # Type and address
print('Iterate  list_reverseiterator  object  with   next()   function')
while True:
    try:
        print(next(r))
        time.sleep(1)
    except:
        break
print('Iterate  list_reverseiterator  object  with   next()   method')
while True: #How  to  iterate   list_reverseiterator  object  with   next()  method
	try:
		print(r.__next__())
		time.sleep(1)
	except:
		break
print('Iterate  list_reverseiterator  object  with   for  loop')
r = reversed(a)
for x in r:
	print(x)
	time.sleep(1)
print('Unpack  list_reverseiterator  object  with     operator   :  ') # How  to  unpack   list_reverseiterator  object   with     operator)
r = reversed(a)
print(*r)
print()
print('Reverse  list  :  ') #  How  to  convert  list_reverseiterator  object  to  list)
r = reversed(a)
print(list(r))
# How  to  iterate   list_iterator  in  different  ways
import   time
list  =  [10  ,  20  ,  15  ,  18]
print('Iterate  list  with  for  loop')
for x in list:#How  to  iterate  list  with  for  loop
    print(x)
print(next(list))	
list_itr = iter(list)
print(type(list_itr))
print(list_itr)
print('Iterate  List_iterator  with  next()  function')
#How  to  iterate  list_iterator  with  next()  function
while True:
	try:
		print(next(list_itr))
		time.sleep(1)
	except:
		break	
print('Iterate  List_iterator  with   _next_()  method')
#How  to  iterate  list_iterator  with   _next_  method
list_itr = iter(list)
while True:
	try:
		print(list_itr.__next__())
		time.sleep(1)
	except:
		break
print('Iterate  List_iterator  with   for    loop')
#How  to  iterate  list_iterator  with  for  loop
for x in list_itr:
	print(x)

print('Unpacks  List_iterator  with  *  operator  :  ') 
#  How  to  unpack  list_iterator)
list_itr = iter(list)
print(*list_itr)
# Find  outputs
a = 25
print(a) # 25
for  x   in   a:
	print(x) # Error becoz 25 is int
print(iter(a)) # Error becoz Iterator takes only sequence but not non-sequence
print(next(a)) # Error becoz It takes only iterators