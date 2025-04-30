'''#  How  to  iterate  zip  object  in  differenet  ways  (Home  work)
import   time
a = ['Telangana' , 'Andhra Pradesh' , 'Karnataka ', 'Tamilnadu']
b = ['Hyderabad' , 'Amaravathi' , 'Bangalore', 'Chennai']
z = zip(a , b)
print(type(z))#<class 'zip'>
print(z)#type and adress
print('Iterate  zip  object  with   next()   function')
print(next(z))
print(next(z))
print(next(z))
print(next(z))
print()#How  to   iterate  zip  object  with  next  function
print('Iterate  zip  object  with  _next_  method')
z=zip(a,b)
print(z.__next__())
print(z.__next__())
print(z.__next__())
print(z.__next__())
print()# How  to   iterate  zip  object  with  _next_  method
print('Iterate  zip  object  with   for  loop')
z=zip(a,b)
for i in range(len(max(a,b))):
	print(next(z))

print()	
	#How  to   iterate  zip  object  with  for  loop
print('Iterate  elements  of  each  tuple  in  zip  object')

#How  to   iterate  elements  of  each  tuple  of  zip  object  with  for  loop
z4=zip(a,b)
for i in z4:
		print(*i)
print()

print('Unpacks  zip  object  with   *  operator  :  ' ,*zip(a,b))
print()
print('zip   object  in  the  form  of   list  :  ' , list(zip(a,b)))
print()
print('zip   object  in  the  form  of   dictionary :  ' ,  dict(zip(a,b)))
#  Write  all  the  outputs  here

#  Find  outputs  (Home  work)
import   time
a = [ 'Empno' , 'Emp Name' , 'Salary']
b = [ 25 , 'Rama  Rao' , 10000.0 , 'Male' , True]
c = zip(a , b)
while   True:
	try:
		print(next(c))#('Empno',25,)<next line>('Emp Name','Rama  Rao')<next line>( 'Salary',10000.0 )
		time . sleep(1)
	except:
		break

#  Find  outputs  (Home  work)
import   time
a = ['Telangana' , 'Andhra  Pradesh' , 'Karnataka' , 'TamilNadu' , 'Maharastra']
b = ['Hyderabad' , 'Amaravathi' , 'Banglore' , 'Chennai' , 'Mumbai']
c = [50000000 , 40000000 , 70000000 , 60000000 , 30000000]
for   x   in   zip(a , b , c):
	print(x)#('Telangana','Hyderabad',50000000)<next line>('Andhra  Pradesh','Amaravathi',40000000)<next line>
	time . sleep(1)
	
# Find  outputs   (Home  work)
import   time
a = [1 , 2 , 3]
b = [4 , 5 , 6 , 7 , 8]
for  x , y  in   zip(a , b):
	print(x + y)# 5<next line>7<next line>9
	time . sleep(1)

# Find outputs  (Home  work)
import   time
def   disp(z):
	while   True:
		try:
			print(next(z))#(10,1)(20,3)(30,5)
						#(10,2)(20,4)(30,6)
						#(10,1,2)(20,3,4)(30,5,6)
						#(10,1)(20,3)(30,5)
						#(10,20,30)
						#(1,3,5)
			time . sleep(1)
		except:
			break
	print()
a = [10 , 20 ,  30]
b = {1 : 2 , 3 : 4 , 5 : 6}#{2,4,6}
c = zip(a , b . keys())#(10,1,2)(20,3,4)(30,5,6)
disp(c)
d = zip(a , b . values())#(
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

# Find  outputs  (Home  work)
z = zip(range(5) , range(20 , 25))#((0,1,2,3,4),(20,21,22,23,24))
a = [ [x , y]  for  x , y   in   z]
print(a)#[[0,20],[1,21],[2,22],[3,23],[4,24]]

#  How  to  print  reversed  object  in  different  ways  (Home  work)
import   time
a = input('Enter  any  string  :  ')  #  Assume  that  input  is  HYD
r = reversed(a)#DYH
print(type(r))#<class Reversed>
print(r)#Type and adress
print()
print('Iterate  reversed  object  with   next   function')

print(next(r))
print(next(r))
print(next(r)) #How  to  iterate  reversed  object  'r'  with  next()  function
print('Iterate  reversed  object  with   next   method')
print()
r = reversed(a)
print(r.__next__())
print(r.__next__())
print(r.__next__())#How  to  iterate  reversed  object   with  next()   method
print()
print('Iterate  reversed  object  with   for  loop')
r= reversed(a)
for i in r:
			print(*i)
#How  to  iterate  reversed  object   with  for  loop
print('Unpack  reversed  object  with   *  operator :   ' , *reversed(a))
print()
print('reversed  object  in  the  form   of  list  :  ' ,  list(reversed(a)))
print('Reverse  string   :   ' ,  reversed(a))
#  Write all  the  outputs  here

# Find  outputs (Home  work)
a = 'RAMA'
b = reversed(a)#AMAR
print(type(b))#<class 'reversed'>
print(b)#type and adress
print(id(b))#some random adress
print(*b)#AMAR
print(b[0])#'reversed' object is not subscriptable
print(b[1 : 3])#'reversed' object is not subscriptable
print(b * 2)#not supported between reverse and int
print(len(b))#reverse has no length

# Can  tuple  be  reversed ?   (Home  work)
import   time
a = (25 , 10.8 , 'Hyd' , True)
b = reversed(a)#(True,'Hyd',10.8,25)
print(type(b))#<class'reversed'>
for  x  in   b:
	print(x)#True <next line> 'Hyd'<next line> 10.8<next line> 25
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
b = reversed(a . keys())#{18,15,20,10}
disp(b)#18<next line>15<next line>20<next line>10
c = reversed(a . values())
disp(c)#'Amar'<next line>'Kiran'<next line>'Sita'<next line>'Rama'
d = reversed(a . items())
disp(d)#18 : 'Amar'<next line> 15 : 'Kiran'<next line>'Sita' , 15<next line>10 : 'Rama'
e = reversed(a)
disp(e)#18<next line>15<next line>20<next line>10


Write  a  program  to  reverse  a  dictionary ?

Let  input  be  {'Empno' : 25 , 'Emp Name' : 'Rama  Rao' , 'Sal' : 10000.0}
What  is  the  output  ?  --->  {'Sal' : 10000.0 , 'Emp  Name' :  Rama  Rao' , 'Empno' : 25}

Hint:  Use  reversed  iterator

a=eval(input('enter any dict:'))
b=reversed(a.items())
c=dict(b)
print(c)

outputs---
enter any dict:{'Empno' : 25 , 'Emp Name' : 'Rama  Rao' , 'Sal' : 10000.0}
{'Sal': 10000.0, 'Emp Name': 'Rama  Rao', 'Empno': 25}

# Find outputs
import  time
a = {10 : 'Rama rao', 20 : 'Sita', 15 : 'Rajesh', 18 : 'Kiran'}
b=reversed(a.keys())#
print(b) #print('Keys  in   reverse   order')
print()

#Write  for  loop  to  reverse  keys  of  dictionary
b=reversed(a.keys())
for i in b:
		print(i)
		time.sleep(1)
print()
b=reversed(a.values())
print('Values  in  reverse  order')
print(b)
print()
#Write  for  loop  to  reverse  values  of  dictionary
b=reversed(a.values())
for i in b:
		print(i)
		time.sleep(1)
print('Tuples  in   reverse  order')
#Write  for  loop  to  reverse   tuples   of  dictionary
b=reversed(a.items())
for i in b:
	print(i)
	time.sleep(2)
print('Elements  of  each   tuple  in  reverse  order')
print()
b=reversed(a.items())
for keys,values in b:
		print(values,keys)
#Write  for  loop  to  reverse   elements  of   each   tuple  of  dictionary
print('Keys  and  values  in   reverse   order')
b=reversed(a.items())
for keys,values in b:
		print(f'key:{keys}\tvalue:{values}')
#Write  for  loop  to  print  each   key  and   the  corresponding  value  of  dictionary  in  reverse  order
#  Write  outputs  here

# How  to  iterate   list_iterator  in  different  ways
import   time
list  =  [10  ,  20  ,  15  ,  18]
print('Iterate  list  with  for  loop')
b=iter(list)
for x in b:
		print(x) #How  to  iterate  list  with  for  loop
#print(next(list)) error
list_itr = iter(list)
print(type(list_itr))#<class 'list_iterator'>
print(list_itr)#Type and adress
print('Iterate  List_iterator  with  next()  function')
b=iter(list)
print(next(b))
print(next(b))
print(next(b))
print(next(b))#How  to  iterate  list_iterator  with  next()  function
print()
print('Iterate  List_iterator  with   __next__()  method')
b=iter(list)
print(b.__next__())
print(b.__next__())
print(b.__next__())
print(b.__next__())
#How  to  iterate  list_iterator  with   __next__  method
print('Iterate  List_iterator  with   for    loop')
b=iter(list)
for x in b:
		print(x)
#How  to  iterate  list_iterator  with  for  loop
b=iter(list)
print('Unpacks  List_iterator  with  *  operator  :    ' ,*b   )
'''
# Find  outputs
a = 25
print(a)#25
#for  x   in   a:
	#print(x)#error
print(iter(a))#error
print(next(a))#error
