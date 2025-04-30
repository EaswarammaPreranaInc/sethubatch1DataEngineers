'''#  How  to  print  reversed  object  in  different  ways  (Home  work)
import   time
a = input('Enter  any  string  :  ')  #  Assume  that  input  is  HYD
r = reversed(a)
print(type(r))
print(r)
print(next(r)) #('Iterate  reversed  object  with   next   function')
#How  to  iterate  reversed  object  'r'  with  next()  function
print(r.__next__())
for element in r:
	print(f'{element}')     #'Iterate  reversed  object  with   for  loop')
#print('Unpack  reversed  object  with   *  operator :   ' , *r)
print()
#print('reversed  object  in  the  form   of  list  :  ' ,  list(r))
print('Reverse  string   :   ' ,  )
#  Write all  the  outputs  here
'''
'''
#  How  to  iterate  zip  object  in  differenet  ways  (Home  work)
import   time
a = ['Telangana' , 'Andhra Pradesh' , 'Karnataka ', 'Tamilnadu']
b = ['Hyderabad' , 'Amaravathi' , 'Bangalore', 'Chennai']
z = zip(a , b)
for x in z:
    for element in x:
        print(element)
print(type(z))
print(z)
print(next(z))
print(z.__next__())
for x in z:
	print(x)
print('Unpacks  zip  object  with   *  operator  :  ' , *z) 
print()
print('zip   object  in  the  form  of   list  :  ' ,  list(next(z)))
print()
print('zip   object  in  the  form  of   dictionary :  ' ,dict(z))  
#  Write  all  the  outputs  here
'''
'''
# Find  outputs (Home  work)
a = 'RAMA'
b = reversed(a) 
print(type(b))
print(b)
print(id(b))
print(*b)
#print(b[0])
#print(b[1 : 3])
#print(b * 2)
3print(len(a))
#output
'AMAR'
<class 'reversed'>
<class and addres>
address
'A','M','A','R'
err
err
err
err
'''
'''
# Find  outputs
a = 25
print(a)
for  x   in   a:
	print(x)
print(iter(a))
print(next(a))
'''
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
#output
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
'''
#Can  tuple  be  reversed ?   (Home  work)
import   time
a = (25 , 10.8 , 'Hyd' , True)
b = reversed(a)
print(type(b))
for  x  in   b:
	print(x)
	time . sleep(1)
#output
<class 'reversed'>
True
Hyd
10.8
25
'''
'''
#  Find  outputs  (Home  work)
import   time
a = ['Telangana' , 'Andhra  Pradesh' , 'Karnataka' , 'TamilNadu' , 'Maharastra']
b = ['Hyderabad' , 'Amaravathi' , 'Banglore' , 'Chennai' , 'Mumbai']
c = [50000000 , 40000000 , 70000000 , 60000000 , 30000000]
for   x   in   zip(a , b , c):
	print(x)
	time . sleep(1)
#output
('Telangana', 'Hyderabad', 50000000)
('Andhra  Pradesh', 'Amaravathi', 40000000)
('Karnataka', 'Banglore', 70000000)
('TamilNadu', 'Chennai', 60000000)
('Maharastra', 'Mumbai', 30000000)
'''
'''
# Find  outputs   (Home  work)
import   time
a = [1 , 2 , 3]
b = [4 , 5 , 6 , 7 , 8]
for  x , y  in   zip(a , b):
	print(x + y)
	time . sleep(1)
	# output 5 7 9
'''
'''
# Find  outputs  (Home  work)
z = zip(range(5) , range(20 , 25))
a = [ [x , y]  for  x , y   in   z]
print(a)
#output: [[0, 20], [1, 21], [2, 22], [3, 23], [4, 24]]
'''
'''
Write  a  program  to  reverse  a  dictionary ?

Let  input  be  {'Empno' : 25 , 'Emp Name' : 'Rama  Rao' , 'Sal' : 10000.0}
What  is  the  output  ?  --->  {'Sal' : 10000.0 , 'Emp  Name' :  Rama  Rao' , 'Empno' : 25}

Hint:  Use  reversed  iterator

s={'Empno' : 25 , 'Emp Name' : 'Rama  Rao' , 'Sal' : 10000.0}
print( 'dictonary: ', s)
r=reversed(s.items())
print('Reversed :', dict(r))
#output : {'Sal': 10000.0, 'Emp Name': 'Rama  Rao', 'Empno': 25}
'''
'''
# How  to  iterate   list_iterator  in  different  ways
import   time
list  =  [10  ,  20  ,  15  ,  18]
for i in list:
	print(i)
#How  to  iterate  list  with  for  loop
#print(next(list))
list_itr = iter(list)
print(type(list_itr))
print(list_itr)
print(next(list_itr))#'Iterate  List_iterator  with  next()  function')
#How  to  iterate  list_iterator  with  next()  function
print(list_itr.__next__())
#How  to  iterate  list_iterator  with   _next_  method
for i in list_itr:
	print(i)
#How  to  iterate  list_iterator  with  for  loop
print('Unpacks  List_iterator  with  *  operator  :    ' , *list_itr  )#How  to  unpack  list_iterator)
'''
def is_palindrome(s):
	a=lower(s)
	if a.isalnum():
		print('palindrome')
	else:
		print('none')
























