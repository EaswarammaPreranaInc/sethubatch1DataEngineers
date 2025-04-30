
#1.How  to  iterate  zip  object  in  differenet  ways  (Home  work)

'''
import   time
a = ['Telangana' , 'Andhra Pradesh' , 'Karnataka ', 'Tamilnadu']
b = ['Hyderabad' , 'Amaravathi' , 'Bangalore', 'Chennai']
z = zip(a , b)
print(type(z)) #<class 'zip'>
print(z) #<zip' object at 0xaddress>

print('Iterate  zip  object  with   next()   function')
while(True):
    try:
        print(next(z)) #How  to   iterate  zip  object  with  next  function
        time.sleep(1)
    except StopIteration:
        break 
print()

z = zip(a , b)
print('Iterate  zip  object  with  next  method')
while(True):
    try:
        print(z.__next__()) #How  to   iterate  zip  object  with  next  method
        time.sleep(1)
    except StopIteration:
        break 
print()

z = zip(a , b)
print('Iterate  zip  object  with   for  loop')
for i in z:
    print(i) #How  to   iterate  zip  object  with  for  loop
print()

print('Iterate  elements  of  each  tuple  in  zip  object')
z = zip(a , b)
for i in z: 
    print(*i) #How  to   iterate  elements  of  each  tuple  of  zip  object  with  for  loop
print()

print('Unpacks  zip  object  with   *  operator  :  ' ,*zip(a,b)) # How  to   unpack  zip  object   with  *  operator
print()
print('zip   object  in  the  form  of   list  :  ' , list(zip(a,b))) #How  to  convert  zip  object  to  list
print()
print('zip   object  in  the  form  of   dictionary :  ' ,dict(zip(a,b)))#How  to  convert  zip  object  to  dictionary
#  Write  all  the  outputs  here

#Unpacks  zip  object  with   *  operator  :   ('Telangana','Hyderabad') ('Andhra Pradesh','Amaravathi') ('Karnataka','Bangalore') ('Tamilnadu','Chennai')
#zip   object  in  the  form  of   list  : [('Telangana','Hyderabad'),('Andhra Pradesh','Amaravathi'),('Karnataka','Bangalore'),('Tamilnadu','Chennai')]
#zip   object  in  the  form  of   dictionary : {'Telangana':'Hyderabad','Andhra Pradesh':'Amaravathi','Karnataka':'Bangalore','Tamilnadu':'Chennai'}

'''

#2. Find  outputs  (Home  work)

'''
import   time
a = [ 'Empno' , 'Emp Name' , 'Salary']
b = [ 25 , 'Rama  Rao' , 10000.0 , 'Male' , True]
c = zip(a , b)
while   True:
	try:
		print(next(c)) # 9'Empno',25)  ('Emp Name','Rama Rao')  ('Salary',10000.0) 
		time . sleep(1)
	except:
		break
		
'''

#3.Find  outputs  (Home  work)

'''
import   time
a = ['Telangana' , 'Andhra  Pradesh' , 'Karnataka' , 'TamilNadu' , 'Maharastra']
b = ['Hyderabad' , 'Amaravathi' , 'Banglore' , 'Chennai' , 'Mumbai']
c = [50000000 , 40000000 , 70000000 , 60000000 , 30000000]
for   x   in   zip(a , b , c):
	print(x)
	time . sleep(1)
'''

'''
('Telangana','Hyderabad',50000000 ) 
('Andhra Pradesh','Amaravathi',40000000 ) 
('Karnataka','Bangalore',70000000 ) 
('Tamilnadu','Chennai',60000000 )
('Maharastra','Mumbai',30000000 )

'''

#5. Find  outputs   (Home  work)
'''
import   time
a = [1 , 2 , 3]
b = [4 , 5 , 6 , 7 , 8]
for  x , y  in   zip(a , b):
	print(x + y) #5 7 9 
	time . sleep(1)

'''

#6. Find  outputs  (Home  work)

'''
z = zip(range(5) , range(20 , 25))
a = [ [x , y]  for  x , y   in   z]
print(a) # [[0,20],[1,21],[2,22],[3,23],[4,24]]

'''

#7. How  to  print  reversed  object  in  different  ways  (Home  work)

'''
import   time
a = input('Enter  any  string  :  ')  #  Assume  that  input  is  HYD
r = reversed(a)
print(type(r)) #<class 'reversed'>
print(r) #<'reversed' object at 0xaddress>

print('Iterate  reversed  object  with   next   function')
while(True):
    try:
        print(next(r)) # D Y H
        time.sleep(1)
        #How  to  iterate  reversed  object  'r'  with  next()  function
        
    except StopIteration:
        break
print()

r = reversed(a)
print('Iterate  reversed  object  with   next   method')
while(True):
    try:
        print(r.__next__()) # D Y H 
        time.sleep(1)
        #How  to  iterate  reversed  object   with  next()   method
        
    except StopIteration:
        break 
print()

r = reversed(a)
print('Iterate  reversed  object  with   for  loop')
for i in r:
    print(i) #How  to  iterate  reversed  object   with  for  loop
    time.sleep(1)
    #D Y H
print()

print('Unpack  reversed  object  with   *  operator :   ' ,*reversed(a) )#How  to   unpack  reversed  object   with  *  operator
print()
print('reversed  object  in  the  form   of  list  :  ' ,list(reversed(a))) #How  to  convert  reversed  object  to  list
print()
print('Reverse  string   :   ' , str(reversed(a))) #How  to  convert  reversed  object  to   string
#  Write all  the  outputs  here

'''

'''
#Unpack  reversed  object  with   *  operator :  
#reversed  object  in  the  form   of  list  : ['D','Y','H']
#Reverse  string   :   <reversed object at 0xaddress>

'''

#8. Find  outputs (Home  work)

'''
a = 'RAMA'
b = reversed(a)
print(type(b)) #<class 'reversed'>
print(b) # <reversed object at 0xaddress>
print(id(b)) #decimal(0xaddress)
print(*b)# A M A R
#print(b[0]) #Error 
#print(b[1 : 3]) #Error 
#print(b * 2) #Error 
#print(len(b)) #Error

'''

#9.Can  tuple  be  reversed ?   (Home  work)

'''
import   time
a = (25 , 10.8 , 'Hyd' , True)
b = reversed(a)
print(type(b)) #<class 'reversed'>
for  x  in   b:
	print(x) # True 'Hyd' 10.8 25 
	time . sleep(1)
'''


#10. Can  dictionary  be  reversed  ? (Home  work)

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
disp(b) # 18 15 20 10 
c = reversed(a . values())
disp(c) # 'Amar' 'Kiran' 'Sita' 'Rama'
d = reversed(a . items())
disp(d) # (18:'Amar')  (15:'Kiran')  (20:'Sita')  (10:'Rama')
e = reversed(a)
disp(e) #18 15 20 10 

'''

'''
11.
Write  a  program  to  reverse  a  dictionary ?

Let  input  be  {'Empno' : 25 , 'Emp Name' : 'Rama  Rao' , 'Sal' : 10000.0}
What  is  the  output  ?  --->  {'Sal' : 10000.0 , 'Emp  Name' :  Rama  Rao' , 'Empno' : 25}

Hint:  Use  reversed  iterator

Enter a dictionary :  {'Empno' : 25 , 'Emp Name' : 'Rama  Rao' , 'Sal' : 10000.0}
Reverse  dictionary  :   {'Sal': 10000.0, 'Emp Name': 'Rama  Rao', 'Empno': 25}

'''

'''
d=eval(input("Enter a dictionary: "))
r=reversed(d.items())
R=dict(r)
print("Reverse dictionary : ",R)

'''

#12.Find outputs

'''
import  time
a = {10 : 'Rama rao', 20 : 'Sita', 15 : 'Rajesh', 18 : 'Kiran'}
print('Keys  in   reverse   order')
for i in reversed(a):
    print(i,end=" ") #Write  for  loop  to  reverse  keys  of  dictionary
    time.sleep(1)
print()

print('Values  in  reverse  order')
for i in reversed(a.values()):
    print(i,end=" ") #Write  for  loop  to  reverse  values  of  dictionary
    time.sleep(1)
print()

print('Tuples  in   reverse  order')
for i in reversed(a.items()):
    print(i,end=" ") #Write  for  loop  to  reverse   tuples   of  dictionary
    time.sleep(1)
print()
    
print('Elements  of  each   tuple  in  reverse  order')
for i in a.items():
    print(*reversed(i)) #Write  for  loop  to  reverse   elements  of   each   tuple  of  dictionary
    time.sleep(1)
print()

print('Keys  and  values  in   reverse   order')
for i in reversed(a.items()):
    print(*i) #Write  for  loop  to  print  each   key  and   the  corresponding  value  of  dictionary  in  reverse  order
    time.sleep(1)
#  Write  outputs  here
'''

'''
Keys  in   reverse   order
18 15 20 10 
Values  in  reverse  order
Kiran Rajesh Sita Rama rao 
Tuples  in   reverse  order
(18, 'Kiran') (15, 'Rajesh') (20, 'Sita') (10, 'Rama rao') 
Elements  of  each   tuple  in  reverse  order
Rama rao 10
Sita 20
Rajesh 15
Kiran 18

Keys  and  values  in   reverse   order
18 Kiran
15 Rajesh
20 Sita
10 Rama rao

'''


#13. How  to  print  list_reverseiterator  object  in  different  ways  (Home   work)
'''
import   time
a = [25 , 10.8 , 'Hyd' , True]
r = reversed(a)
print(type(r)) #<class 'list_reverseiterator'>
print(r) #<list_reverseiterator object at 0xaddress>

print('Iterate  list_reverseiterator  object  with   next()   function')
while(True):
    try:
        print(next(r)) #How  to  iterate   list_reverseiterator  object  with   next()   function
        time.sleep(1)
    except:
        break 
    
r = reversed(a)
print('Iterate  list_reverseiterator  object  with   next()   method')
while(True):
    try:
        print(r.__next__()) # How  to  iterate   list_reverseiterator  object  with   next()  method
        time.sleep(1)
    except:
        break 

r = reversed(a)
print('Iterate  list_reverseiterator  object  with   for  loop')
for i in r:
    print(i) #How  to  iterate   list_reverseiterator  object  with   for  loop
    time.sleep(1)
    
r=reversed(a)
print('Unpack  list_reverseiterator  object  with     operator   :  ',*reversed(a)) # How  to  unpack   list_reverseiterator  object   with     operator)
print()
print('Reverse  list  :  '  ,  list(reversed(a))) #How  to  convert  list_reverseiterator  object  to  list

'''

#14. How  to  iterate   list_iterator  in  different  ways
'''
import   time
list  =  [10  ,  20  ,  15  ,  18]
print('Iterate  list  with  for  loop')
for i in reversed(list):
    print(i)#How  to  iterate  list  with  for  loop
    time.sleep(1)
    
#print(next(list)) #Error 

list_itr = iter(list)
print(type(list_itr)) #<class 'iter'>
print(list_itr) #<iter object at 0xaddress>

print('Iterate  List_iterator  with  next()  function')
while(True):
    try:
        print(next(list_itr)) #How  to  iterate  list_iterator  with  next()  function
        time.sleep(1)
    except StopIteration:
        break 
print()

list_itr = iter(list)
print('Iterate  List_iterator  with   _next_()  method')
while(True):
    try:
        print(list_itr.__next__()) # How  to  iterate  list_iterator  with   _next_  method
        time.sleep(1)
    except StopIteration:
        break 
print()

list_itr = iter(list)
print('Iterate  List_iterator  with   for    loop')
for i in list_itr:
    print(i)#How  to  iterate  list_iterator  with  for  loop
    time.sleep(1)
    
print('Unpacks  List_iterator  with  *  operator  :    ' ,*iter(list))#How  to  unpack  list_iterator

'''

#15. outputs 

'''
a = 25
print(a) #25 
#for  x   in   a: #Error 
	#print(x)
#print(iter(a)) #Error only seq arg 
#print(next(a)) #Error only iter arg

'''