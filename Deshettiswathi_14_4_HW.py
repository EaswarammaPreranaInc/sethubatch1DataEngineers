#14/04/25
'''
#1)
#  How  to  iterate  zip  object  in  differenet  ways  (Home  work)
import   time
a = ['Telangana' , 'Andhra Pradesh' , 'Karnataka ', 'Tamilnadu']
b = ['Hyderabad' , 'Amaravathi' , 'Bangalore', 'Chennai']
z = zip(a , b)
print(type(z))
print(z)
print('Iterate  zip  object  with   next()   function')
print(next(z))# Telangana Hyderabad
print(next(z))
print(next(z))
print(next(z))#Tamilnadu Chennai
#print(next(z))
#How  to   iterate  zip  object  with  next  function
print('Iterate  zip  object  with  next  method')
z1=zip(a , b)
print(z1.__next__())
print(z1.__next__())
print(z1.__next__())
print(z1.__next__())
#print(z1.__next__())

#How  to   iterate  zip  object  with  next  method
print('Iterate  zip  object  with   for  loop')
z2=zip(a,b)
for state, capital in z2:
    print(state, '->', capital)
#How  to   iterate  zip  object  with  for  loop
print('Iterate  elements  of  each  tuple  in  zip  object')
z3=zip(a,b)
for pair in z3:
    for item in pair:
        print(item)
#How  to   iterate  elements  of  each  tuple  of  zip  object  with  for  loop
print('Unpacks  zip  object  with   *  operator  :  ')
z4=zip(a,b)
print(*z4)
print('zip   object  in  the  form  of   list  :  ' )
z5=zip(a,b)
print(list(z5))
print('zip   object  in  the  form  of   dictionary :  ' )
z6=zip(a,b)
print(dict(z6))
#  Write  all  the  outputs  here
# <class 'zip'>
# <zip object at 0x000002998129BE40>
# Iterate  zip  object  with   next()   function
# ('Telangana', 'Hyderabad')
# ('Andhra Pradesh', 'Amaravathi')
# ('Karnataka ', 'Bangalore')
# ('Tamilnadu', 'Chennai')
# Iterate  zip  object  with  next  method
# ('Telangana', 'Hyderabad')
# ('Andhra Pradesh', 'Amaravathi')
# ('Karnataka ', 'Bangalore')
# ('Tamilnadu', 'Chennai')
# Iterate  zip  object  with   for  loop
# Telangana -> Hyderabad
# Andhra Pradesh -> Amaravathi
# Karnataka  -> Bangalore
# Tamilnadu -> Chennai
# Iterate  elements  of  each  tuple  in  zip  object
# Telangana
# Hyderabad
# Andhra Pradesh
# Amaravathi
# Karnataka
# Bangalore
# Tamilnadu
# Chennai
# Unpacks  zip  object  with   *  operator  :
# ('Telangana', 'Hyderabad') ('Andhra Pradesh', 'Amaravathi') ('Karnataka ', 'Bangalore') ('Tamilnadu', 'Chennai')
# zip   object  in  the  form  of   list  :
# [('Telangana', 'Hyderabad'), ('Andhra Pradesh', 'Amaravathi'), ('Karnataka ', 'Bangalore'), ('Tamilnadu', 'Chennai')]
# zip   object  in  the  form  of   dictionary :
# {'Telangana': 'Hyderabad', 'Andhra Pradesh': 'Amaravathi', 'Karnataka ': 'Bangalore', 'Tamilnadu': 'Chennai'}

#================================================================================================================
#  Find  outputs  (Home  work)
import   time
a = [ 'Empno' , 'Emp Name' , 'Salary']
b = [ 25 , 'Rama  Rao' , 10000.0 , 'Male' , True]
c = zip(a , b)
while   True:
	try:
		print(next(c))#('Empno', 25)<NL>('Emp Name', 'Rama  Rao')<NL>('Salary', 10000.0)
		time . sleep(1)
	except:
		break
#====================================================================================================

#  Find  outputs  (Home  work)
import   time
a = ['Telangana' , 'Andhra  Pradesh' , 'Karnataka' , 'TamilNadu' , 'Maharastra']
b = ['Hyderabad' , 'Amaravathi' , 'Banglore' , 'Chennai' , 'Mumbai']
c = [50000000 , 40000000 , 70000000 , 60000000 , 30000000]
for   x   in   zip(a , b , c):
	print(x)
	time.sleep(1)
	#outputs
	#--------------------------
#('Telangana', 'Hyderabad', 50000000)
#('Andhra  Pradesh','Amaravathi',40000000 )
#('Karnataka','Amaravathi',70000000)
#('TamilNadu','Chennai',60000000)
#('Maharastra','Mumbai',30000000)
#==========================================================================================

# Find  outputs   (Home  work)
import   time
a = [1 , 2 , 3]
b = [4 , 5 , 6 , 7 , 8]
for  x , y  in   zip(a , b):
	print(x + y)
	time.sleep(1)
#output
#------------------------
#5
#7
#9
#====================================================================================

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
#output
#-------------------------------------
#(10,1)
#(20,3)
#(30,5)

#(10,2)
#(20,4)
#(30,6)

#(10,(1,2))
#(20,(3,4))
#(30,(5,6))

#(10,1)
#(20,3)
#(30,5)

#(10,)
#(20,)
#(30,)

#(1,)
#(3,)
#(5,)
#========================================================

# Find  outputs  (Home  work)
z = zip(range(5) , range(20 , 25))
a = [ [x , y]  for  x , y   in z]
print(a)
#output
#----------------------------------
#[[0,20],[1,21],[2,22],[3,23],[4,24]]
#======================================================

#  How  to  print  reversed  object  in  different  ways  (Home  work)
import   time
a = input('Enter  any  string  :  ')  #  Assume  that  input  is  HYD
r = reversed(a)
print(type(r))
print(r)
print('Iterate  reversed  object  with   next   function')
r1=reversed(a)
print(next(r1))
print(next(r1))
print(next(r1))

print('Iterate  reversed  object  with   next   method')
r2=reversed(a)
print(r2.__next__())
print(r2.__next__())
print(r2.__next__())

print('Iterate  reversed  object  with   for  loop')
r3=reversed(a)
for char in r3:
    print(char)

print('Unpack  reversed  object  with   *  operator :   ')
r4=reversed(a)
print(*r4)
print()
print('reversed  object  in  the  form   of  list  :  ')
r5=reversed(a)
print(list(r5))
print('Reverse  string   :   ' )
r6=reversed(a)
print(''.join(r6))

#  Write all  the  outputs  here
# Enter  any  string  :  hyd
# <class 'reversed'>
# <reversed object at 0x000002645D97B6D0>
# Iterate  reversed  object  with   next   function
# d
# y
# h
# Iterate  reversed  object  with   next   method
# d
# y
# h
# Iterate  reversed  object  with   for  loop
# d
# y
# h
# Unpack  reversed  object  with   *  operator :
# d y h

# reversed  object  in  the  form   of  list  :
# ['d', 'y', 'h']
# Reverse  string   :
# dyh
#=======================================================

# Find  outputs (Home  work)
a = 'RAMA'
b = reversed(a)
print(type(b))#class reversed
print(b)#type and addrss
print(id(b))#address
print(*b)#A M A R
#print(b[0])#ERROR
#print(b[1 : 3])#ERROR
#print(b * 2)#ERROR
#print(len(b))#ERROR
#=========================================================

# Can  tuple  be  reversed ?   (Home  work)
import   time
a = (25 , 10.8 , 'Hyd' , True)
b = reversed(a)
print(type(b))#Class reversed
for  x  in   b:
	print(x)# True<NL>Hyd<NL>10.8<NL>25
	time.sleep(1)
#==========================================================

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
disp(b)#18<NL>15<NL>20<NL>10)
c = reversed(a . values())
disp(c)#Amar<NL>Kiran<NL>SitaVRama
d = reversed(a . items())
disp(d)#((18 , 'Amar')<NL>(15 , 'Kiran')<NL>(20 , 'Sita'')<NL>(10 , 'Rama'))
e = reversed(a)
disp(e)#18<NL>15<NL>20<NL>10)
#===================================================================================

x=eval(input("Enter a dictionary:"))

b = {key: x[key] for key in reversed(list(x))}

print(f'Reverse dictionary:{b}')
#=========================================================

import time

a = {10: 'Rama rao', 20: 'Sita', 15: 'Rajesh', 18: 'Kiran'}

print('Keys in reverse order')
for k in reversed(list(a)):
    print(k)

print('Values in reverse order')
for k in reversed(list(a)):
    print(a[k])

print('Tuples in reverse order')
for item in reversed(list(a.items())):
    print(item)

print('Elements of each tuple in reverse order')
for item in reversed(list(a.items())):
    print(item[::-1])  # reverse key and value in the tuple

print('Keys and values in reverse order')
for k in reversed(list(a)):
    print(f"{k} --> {a[k]}")
#===============================================================
import time

a = [25, 10.8, 'Hyd', True]
r = reversed(a)

print(type(r))  # <class 'list_reverseiterator'>
print(r)        # Just prints something like <list_reverseiterator object at ...>

print('Iterate list_reverseiterator object with next() function')
# Using next() function manually
r1 = reversed(a)
print(next(r1))
print(next(r1))
print(next(r1))
print(next(r1))
# If you call next() one more time, you'll get StopIteration

print('Iterate list_reverseiterator object with next() method')
# Same as above, using next() method is not different in syntax—Python uses the function.
r2 = reversed(a)
while True:
    try:
        print(next(r2))
    except StopIteration:
        break

print('Iterate list_reverseiterator object with for loop')
# Using a for loop directly
r3 = reversed(a)
for item in r3:
    print(item)

print('Unpack list_reverseiterator object with * operator: ', *reversed(a))

print()

print('Reverse list: ', list(reversed(a)))
#======================================================================================

import time
lst = [10, 20, 15, 18]
print('Iterate list with for loop')
for item in lst:
    print(item)
list_itr = iter(lst)
print(type(list_itr))  
print(list_itr)        

print('Iterate List_iterator with next() function')

print(next(list_itr))
print(next(list_itr))
print(next(list_itr))
print(next(list_itr))

list_itr2 = iter(lst)

print('Iterate List_iterator with __next__() method')
#============================================================

# Find  outputs
a = 25
print(a)#25
#for  x   in   a:
#	print(x)
#print(iter(a))#error due to non sequence
#print(next(a))#error
#==========================================================
'''


