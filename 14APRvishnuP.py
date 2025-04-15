"""
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
 #  Find  outputs  (Home  work)
import   time
a = ['Telangana' , 'Andhra  Pradesh' , 'Karnataka' , 'TamilNadu' , 'Maharastra']
b = ['Hyderabad' , 'Amaravathi' , 'Banglore' , 'Chennai' , 'Mumbai']
c = [50000000 , 40000000 , 70000000 , 60000000 , 30000000]
for   x   in   zip(a , b , c):
	print(x)
	time . sleep(1)

#output
('Empno', 25)
('Emp Name', 'Rama  Rao')
('Salary', 10000.0)
('Telangana', 'Hyderabad', 50000000)
('Andhra  Pradesh', 'Amaravathi', 40000000)
('Karnataka', 'Banglore', 70000000)
('TamilNadu', 'Chennai', 60000000)
('Maharastra', 'Mumbai', 30000000)

# Find  outputs   (Home  work)
import   time
a = [1 , 2 , 3]
b = [4 , 5 , 6 , 7 , 8]
for  x , y  in   zip(a , b):
	print(x + y)
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
#output
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


# Find  outputs  (Home  work)
z = zip(range(5) , range(20 , 25))
a = [ [x , y]  for  x , y   in   z]
print(a)#[[0, 20], [1, 21], [2, 22], [3, 23], [4, 24]]

# Find  outputs (Home  work)
a = 'RAMA'
b = reversed(a)
print(type(b))#<class 'reversed'>
print(b)#<reversed object at 0x0000012F648FD6A0>
print(id(b))#address
print(*b)#A M A R
#print(b[0])
#print(b[1 : 3])
#print(b * 2)
#print(len(b))

# Can  tuple  be  reversed ?   (Home  work)
import   time
a = (25 , 10.8 , 'Hyd' , True)
b = reversed(a)
print(type(b))
for  x  in   b:
	print(x)
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
#b = reversed(a . keys())
disp(b)
#c = reversed(a . values())
#disp(c)
#d = reversed(a . items())
#disp(d)
#e = reversed(a)
#disp(e)

#output
<class 'reversed'>
True
Hyd
10.8
25


# Find  outputs
a = 25
print(a)
'''
for  x   in   a:
	print(x)
print(iter(a))
print(next(a))
'''
"""
#  How  to  iterate  zip  object  in  differenet  ways  (Home  work)
import   time
a = ['Telangana' , 'Andhra Pradesh' , 'Karnataka ', 'Tamilnadu']
b = ['Hyderabad' , 'Amaravathi' , 'Bangalore', 'Chennai']
z = zip(a , b)
print(type(z))
print(z)
print('Iterate  zip  object  with   next()   function')
print(next(z))#How  to   iterate  zip  object  with  next  function
print('Iterate  zip  object  with  next  method')
print(z.__next__())#How  to   iterate  zip  object  with  next  method
print('Iterate  zip  object  with   for  loop')
for x,y in z:
	print(next(z)) #How  to   iterate  zip  object  with  for  loop
print('Iterate  elements  of  each  tuple  in  zip  object')
#How  to   iterate  elements  of  each  tuple  of  zip  object  with  for  loop
print('Unpacks  zip  object  with   *  operator  :  ' )
z = zip(a , b) 
print(*z)#How  to   unpack  zip  object   with  *  operator)
print()
z = zip(a , b) 
print('zip   object  in  the  form  of   list  :  ' ,list(z)) #How  to  convert  zip  object  to  list)
print()
z = zip(a , b) 
print('zip   object  in  the  form  of   dictionary :  ',dict(z) )  #How  to  convert  zip  object  to  dictionary)
