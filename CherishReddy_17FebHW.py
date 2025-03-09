#  Write  a  program  to  remove  all  15's  from  the  list
a = [10 , 20 , 15 , 18 , 12 , 15 , 19 , 25 , 15 , 14 , 12]
#while   Repeat  until  there  is  no  15  in  the  list:
#	How  to  remove  each  15  from  the  list
#print(a)


'''
while  cond:
		statements
statements
'''
# PROGRAM 1

a = [10,20,15,18,12,15,19,25,15,14,12]
while 15 in a:
    a.remove(15)
print(a)

# PROGRAM 2
#  Find  outputs  (Home  work)
a = (25 , 10.8 , 'Hyd' , True , 3+4j , None , 'Hyd' , 25)
print(a) # prints the entire tuple
print(*a) # unpacks and prints the entire elements of the tuple
print(type(a)) # <class 'tuple'>
print(len(a)) # length of tuple is 6 hyd and 25 are duplicates
print(a[2 : 5]) # prints the elements from 2 to 4 i.e., 10.8 hyd true in a tuple
print(*a[2 : 5]) # prints only elements from 2 to 4 
#a[2] = 'Sec' # throws error as tuple is imutable
#a . append('Sec') # throws error as tuple is imutable
#a . remove('Hyd') # throws error as tuple is imutable
b =  10 , 20 , 30
print(b) # prints (10,20,30)
print(b * 2) # prints (10,20,30,10,20,30)
c = 40 , 50 , 60,
print(c) # prints (40,50,60)
print(type(c))# <class 'tuple'>

# PROGRAM 3
# Find  outputs  (Home  work)
a = (25)
b = 25,
c = 25
d = (25,)
print(type(a)) #<class 'int'>
print(type(b)) #<class 'tuple'>
print(type(c)) #<class 'int'>
print(type(d)) #<class 'tuple'>
print(a * 4)   # prints 100
print(b * 4)   # prints (25,25,25,25)
print(c * 4)   # prints int*int i.e., 100
print(d * 4)   # prints (25,25,25,25)

#PROGRAM 4
# tuple()  function  demo  program  (Home  work)
a = tuple('Hyd')
print(a) # prints ('H','y','d')
print(type(a))# <class'tuple'>
print(len(a))# length 3
b = [10 , 20 , 15 , 18]
print(tuple(b))# length 4
print(tuple(range(5)))# (0,1,2,3,4)
#print(tuple(25))# throws error as 25 is integer which is not possible.

# PROGRAM 5
# Find  outputs (Home  work)
a = ()
print(type(a))# <class'tuple'>
print(a)# prints ()
print(len(a))# length 0
b = tuple()
print(b)# prints ()
print(len(b))# length 0

# PROGRAM 6
#  Gift
# Find  outputs (Home  work)
a = (10 , 20 , 30)
print(a)# prints (10,20,30)
print(id(a))# prints some random address say 1000
a = a * 2
print(a)# prints the tuple a 2 times
print(id(a))# prints some random address say 1001

#PROGRAM 7
#  set  object  demo  program  (Home  work)
a = {25 , 10.8 , 'Hyd' , True , 3+4j , None , 25 , 'Hyd'}
print(a)# prints the entire set
print(type(a))# prints <class'set'>
print(len(a))# prints length of tuple i.e.,6
#print(a[2])# throws error as set is not indexed
#print(a[1 : 4])# throws error as set is not indexed
#a[2] = 'Sec'# throws error as set cannot be modified
#print(a * 2)# set cannot be repeated
#print(a * a)# set cannot be multiplied upon set

# PROGRAM 8
# Gift 
# Find  outputs (Home  work)
a = {1 , 'Hyd' , False , True , 0.0 , '' , 1.0 ,  0}
print(a)# prints {False,1,'Hyd',''}
print(len(a))# prints set length 4
print(type(a))# <class'set'>

# PROGRAM 9
#  set()  function demo  program
a = set('Rama rAo')
print(a)# prints a set with unique characters separated by commas.
print(len(a))# set length 7
print(set([10 , 20 , 15 , 20]))# prints {10,20,15}
print(set((25 , 10.8 , 'Hyd' , 10.8)))# prints {25,10.8,'Hyd'}
print(set(range(10 , 20 , 3)))# prints {10,13,16,19}
#print(set(25))# throws error as 25 is a integer which is not acceptable here.

#PROGRAM 10
#  Gift
# Find  outputs  (Home  work)
a =   [ ]
b =   ( )
c =   { }
d =   set()
print(type(a))# <class'list'>
print(type(b))# <class'set'>
print(type(c))# class'dict'>
print(type(d))# class 'set'>
print(a)# prints []
print(b)# prints ()
print(c)# prints {}
print(d)# prints set()

#PROGRAM 11
#  Gift
# add()  and  remove()  methods  (Home  work)
a = set()
a . add(25)
a . add(10.8)
a . add('Hyd')
a . add(True)
a . add(None)
a . add('Hyd')
a . add(1)
print(a)# prints {None,True,10.8,'Hyd',25}
a . remove(25)
print(a)# prints {None,True,10.8,'Hyd'}
#a . append(100)# throws error as append operation is not allowed in set.
#a . add(set())# throws error as set() cannot be added

#PROGRAM 12
# How  to  print  set  in  two  different ways  (Home  work)
a = {25 , True , 'Hyd' , 10.8}
print(a)
print(set(a))
#print('set  with  print  function') 
print(a)
print(set())#print(How  to  print  set)
#'Iterate  elements  of  set  with  for  loop'

for x in a:
   print(x)

#How  to  iterate  set  with  for  loop
a={'1234'}
for x in a:
  print(set(x))




