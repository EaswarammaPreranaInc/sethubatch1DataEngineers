
#  How  to  iterate  zip  object  in  differenet  ways  (Home  work)
import   time
a = ['Telangana' , 'Andhra Pradesh' , 'Karnataka ', 'Tamilnadu']
b = ['Hyderabad' , 'Amaravathi' , 'Bangalore', 'Chennai']
z = zip(a , b)
print(type(z))# <class'zip'>
print(z)# type and address
print('Iterate  zip  object  with   next()   function')

while True:
    try:
        print(next(z))
        time.sleep(1)
    except StopIteration:
        break

print('Iterate  zip  object  with  next  method')

c=zip(a,b)
while True:
    try:
        print(c.__next__())
        time.sleep(1)
    except StopIteration:
        break

print('Iterate  zip  object  with   for  loop')
c=zip(a,b)
for x in c:
    print(x)
    time.sleep(1)

print('Iterate  elements  of  each  tuple  in  zip  object')
c=zip(a,b)
for i,j in c:
    print(i,j,sep="\n")

c=zip(a,b)
print('Unpacks  zip  object  with   *  operator  :  ' , *c)

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
(Empno,25)
(Emp Name,Rama Rao)
(Salary,10000.0)
'''
 #  Find  outputs  (Home  work)
import   time
a = ['Telangana' , 'Andhra  Pradesh' , 'Karnataka' , 'TamilNadu' , 'Maharastra']
b = ['Hyderabad' , 'Amaravathi' , 'Banglore' , 'Chennai' , 'Mumbai']
c = [50000000 , 40000000 , 70000000 , 60000000 , 30000000]
for   x   in   zip(a , b , c):
	print(x)
	time . sleep(1)
'''
('Telangana','Hyderabad,50000000)
(Andhra pradesh,Amarvathi,50000000)
(Karnataka,Bengalore,50000000)
(TamilNadu,Chennai,50000000)
(Maharastra,Mumbai,50000000)
'''
 # Find  outputs   (Home  work)
import   time
a = [1 , 2 , 3]
b = [4 , 5 , 6 , 7 , 8]
for  x , y  in   zip(a , b):
	print(x + y)
	time . sleep(1)
'''
(5)
(7)
(9)
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
'''
(10,1)
(20,3)
(30,5)

'''
d = zip(a , b . values())
disp(d)
'''
(10,2)
(20,4)
(30,6)
'''
e = zip(a , b . items())
disp(e)
'''
(10,(1,2)
(20,(3,4))
(30,(5,6))
'''
f = zip(a , b)
disp(f)
'''
(10,1)
(20,3)
(30,5)
'''
g = zip(a)
disp(g)
'''
10,
20,
30,
'''
h = zip(b)
disp(h)
'''
1,
3,
5,
'''
i = zip()
disp(i)
'''
'''
 # Find  outputs  (Home  work)
z = zip(range(5) , range(20 , 25))
a = [ [x , y]  for  x , y   in   z]
print(a)
'''
[[0,20],[1,21],[2,22],[3,23],[4,24]]
'''
#  How  to  print  reversed  object  in  different  ways  (Home  work)
import   time
a = input('Enter  any  string  :  ')  #  Assume  that  input  is  HYD
r = reversed(a)
print(type(r)) # <class 'reversed'>
print(r)# DYH
print('Iterate  reversed  object  with   next   function')
while True:
	try:
		print(next(r),end=" ")
		time.sleep(1)
	except:
		break
print()
#How  to  iterate  reversed  object  'r'  with  next()  function
print('Iterate  reversed  object  with   next   method')
r=reversed(a)
while True:
	try:
		print(r.__next__(),end=" ")
		time.sleep(1)
		
	except:
		break
print()
#How  to  iterate  reversed  object   with  next()   method
print('Iterate  reversed  object  with   for  loop')
r=reversed(a)
for x in r:
	print(x,end=" ")
print()


#How  to  iterate  reversed  object   with  for  loop
r=reversed(a)
print('Unpack  reversed  object  with   *  operator :   ' ,  *r)
print()
r=reversed(a)
print('reversed  object  in  the  form   of  list  :  ' ,  list(r))

# Find  outputs (Home  work)
a = 'RAMA'
b = reversed(a)
print(type(b))#<class 'reversed'>
print(b)
print(id(b))
print(*b)
#print(b[0])
#print(b[1 : 3])
#print(b * 2)
#print(len(b))

'''
AMAR
<class 'reversed>
AMAR
10000
A M A R
'''
import   time
a = (25 , 10.8 , 'Hyd' , True)
b = reversed(a)
print(type(b))
for  x  in   b:
	print(x)
	time . sleep(1)
'''
<class'reversed'>
True
Hyd
10.8
25
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
'''
18
15
20
10
'''
c = reversed(a . values())
disp(c)
'''
Amar
Kiran
Sita
Rama
'''
d = reversed(a . items())
disp(d)
'''
(18,Amar)
(15,Kiran)
(20,Sita)
(10,Rama)
'''
e = reversed(a)
disp(e)
'''
18
15
20
10
'''
 '''
Write  a  program  to  reverse  a  dictionary ?

Let  input  be  {'Empno' : 25 , 'Emp Name' : 'Rama  Rao' , 'Sal' : 10000.0}
What  is  the  output  ?  --->  {'Sal' : 10000.0 , 'Emp  Name' :  Rama  Rao' , 'Empno' : 25}

Hint:  Use  reversed  iterator
'''
#Enter a dictionary :  {'Empno' : 25 , 'Emp Name' : 'Rama  Rao' , 'Sal' : 10000.0}
#Reverse  dictionary  :   {'Sal': 10000.0, 'Emp Name': 'Rama  Rao', 'Empno': 25}


n=eval(input("Enter a dictionary : "))
z=reversed(n.items())
for x in z:
    print(x,end=" ")
print()
    
import  time
a = {10 : 'Rama rao', 20 : 'Sita', 15 : 'Rajesh', 18 : 'Kiran'}
print('Keys  in   reverse   order')
z=reversed(a.keys())
for x in z:
    print(z,end=" ")
print()
#Write  for  loop  to  reverse  keys  of  dictionary
print('Values  in  reverse  order')
z=reversed(a.values())
for x in z:
    print(z,end=" ")
print()
#Write  for  loop  to  reverse  values  of  dictionary
print('Tuples  in   reverse  order')
z=reversed(a.items())
for x in z:
    print(z,end=" ")
print()
#Write  for  loop  to  reverse   tuples   of  dictionary
print('Elements  of  each   tuple  in  reverse  order')
z=reversed(a)
for x in z:
    print(z,end=" ")
print()
