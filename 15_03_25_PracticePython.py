# Find  outputs   (Home  work)
a = 25 , 10.8 , 3 + 4j , 'Hyd' , True , None , 'Hyd' , 25
print(a) #(25 , 10.8 , 3 + 4j , 'Hyd' , True , None , 'Hyd' , 25)
print(type(a))# <class 'tuple'>
'''a[3] = 'Sec' # Error 'tuple' object does not support item assignment
a[3 : 6] = 60 , 70 , 80 # Error 'tuple' object does not support item assignment'''
#  What   are  the  outputs  if  input  is  (10 , 20 , 30 , 40) ?   (Home  work)
a = input('Enter  Tuple  :  ')
print(a) # (10 , 20 , 30 , 40)
print(type(a)) # class<'tuple'>
b = eval(a) 
print(b) # (10 , 20 , 30 , 40)
print(type(b)) # class<'tuple'>
print(len(b)) # 4 
# Find  outputs  (Home  work)
a = (10 , [20 , 30 , 40] , 50 , 60)
a[1][0] = 70
print(a) # (10, [70, 30, 40], 50, 60)
#a[1] = [80 , 90 , 100]
#print(a) # Error becoz of tuple directly can't modify
# Find  outputs  (Home  work)
a = [10 , (20 , 30 , 40) , 50 , 60]
#a[1][0] = 70
#print(a) # Error becoz tuple can't be modify
a[1] = [80 , 90]
print(a) # [10, [80, 90], 50, 60]
# Find  outputs   (Home  work)
a = 25
b = 10.8
c = 'Hyd'
d = True
x = a , b , c , d
print(x) # (25, 10.8, 'Hyd', True)
print(type(x)) # <class 'tuple'>
# Find  outputs   (Home  work)
x = 25 , 10.8 , 'Hyd' , True
a , b , c , d = x
print(a) #25
print(b) #10.8
print(c) #Hyd
print(d) #True
'''p , q , r =  x # Error because of less variables
a , b , c , d  , e = x # Error becoz of more variables than inputs'''
# Find  outputs   (Home  work)
x = 25 , 10.8 , 'Hyd' , True
a , *b , c = x 
print(a) # 25
print(b) # [10.8, 'Hyd']
print(c) # True
# Find  outputs   (Home  work)
tpl = 25 , 10.8 , 'Hyd' , True
a , b , *c , d , e = tpl
print(a) # 25
print(b) # 10.8
print(c) # []
print(d) # Hyd
print(e) # True
# Find  outputs   (Home  work)
x = 25 , 10.8 , 'Hyd' , True , 3 + 4j
a , b , _ , d , _= x
print(a) # 25
print(b) # 10.8
print(_) # 3+4j
print(d) # True
print(_) # 3+4j
# tuple()  function  demo  program   (Home  work)
a = range(100 , 150 , 10)
b = tuple(a)
print(b) # (100, 110, 120, 130, 140)
print(type(b)) #<class 'tuple'>
c = [10 , 20 , 15, 18]
d = tuple(c)
print(d) # (10, 20, 15, 18)
e = tuple('Vamsi')
print(e) # ('V', 'a', 'm', 's', 'i')
#print(tuple(25)) # Error: 'int' object is not iterable
print(tuple()) # ()


'''
tuple()  function
--------------------
1) What  does  tuple(sequence)  do  ?  ---> Converts  sequence  to  tuple

2) What  does  tuple(No-args)  do  ?  --->  Returns  an  empty  tuple

3) Is  tuple(non-sequence)  valid ?  --->  No  becoz  argument  should  be  sequence  only

4) How  many  arguments  can  tuple()  function  take ?  --->  1 (or)  none  but  not  more  than  one
'''
#index()  and  count()  methods  demo  program   (Home  work)
a = (10 , 20 , 15 , 12 , 14 , 15 , 18 , 19 , 15 , 12 , 25)
#     0    1      2     3    4     5     6    7     8    9    10
try:
	i = a . index(15)
	while  True:
		print('15 is found at index : ' , i)
		i = a . index(15 , i + 1)
except:
		print(F'15  is  found  {a . count(15)}  times')
'''o/p: 15 is found at index :  2
        15 is found at index :  5
        15 is found at index :  8
        15  is  found  3  times '''		
		
#  How  to  modify  an  element  of  tuple ?    (Home  work)
a  =  10 ,  20 ,  30 ,   40 ,  50
#      0     1    2       3     4
#a[2] = 35
#print(a) # Error becoz tuple object does or support item assignment
#print(id(a)) # Error becoz tuple object does or support item assignment
a = a[:2] + (35,) + a[3:]#How  to  modify  30  in  tuple  to  35
print(a) # (10, 20, 35, 40, 50)
print(id(a)) # Address of a
# How  to  delete  an  element  of  tuple ?   (Home  work)
a  = 10 , 20 , 30 , 40 , 50
#    0     1   2     3    4
#a . remove(30) # Error: 'tuple' object has no attribute 'remove'
#del  a[2] # Error: 'tuple' object doesn't support item deletion
'''a . pop(2) 
print(a) # Error: 'tuple' object has no attribute 'pop'
print(id(a)) # Error: 'tuple' object has no attribute 'pop' '''
a = a[:2] + a[3:]#How  to  remove  30  from  tuple  'a'
print(a) # (10, 20, 40, 50)
print(id(a)) # Addres of a
#  Nested   tuple  (Home  work)
a = ( (10 , 20)  ,  (30 , 40 , 50)  ,  (60 , 70 , 80 , 90) )
print(a) # ((10, 20), (30, 40, 50), (60, 70, 80, 90))
print(type(a)) # <class 'tuple'>
print(len(a)) # 3
print(a[0])# How  to  print  1st  inner  tuple
print(a[1]) # How  to  print  2nd  inner  tuple
print(a[2]) # How  to  print  3rd  inner  tuple
print(a[0][1])# How  to  print  20
print(a[1][2])# How  to  print  50
print(a[2][3])# How  to  print  90
# Find  outputs  (Home  work)
a = ((10 , 20 , 30),)
print(a[0])# How  to   print  inner  tuple
print(*a)# How  to   print  inner  tuple  in  another  way
print(a[0][0])# How   to  print   10
print(a[0][1])# How   to  print   20
print(a[0][2])# How   to  print   30
b = ((),)
print(a[0])# How  to   print  inner  tuple  of  tuple  'b'
print(*a)# How  to   print  inner  tuple  of  tuple  'b'  in  another  way
#  Find  outputs (Home  work)
a = ((10 , 20 , 30))
print(a) # (10, 20, 30)
print(*a) # 10, 20, 30
b = (())
print(b) # ()
print(*b) #   
# What  are  the  outputs  if  input  is  {10 , 20 , 15 , 18 , 20 , 12 , 18}
a = input('Enter  Set  :  ')
print(a) # {10 , 20 , 15 , 18 , 20 , 12 , 18}
print(type(a)) # <class 'str'>
b = eval(a)
print(b) # {10 , 20 , 15 , 18 , 12 }
print(type(b)) # <class 'set'>
#  Find  outputs  (Home  work)
print({(10 , 20 , 30)}) # {(10, 20, 30)} 
#print({[10 , 20 , 30]}) # Error becoz list mutable cannot be in set 
#print({{10 , 20 , 30}}) # Error: unhashable type: 'set'
#print({{}}) # Error: unhashable type: 'dict'
# How  to  print  set  in  differnet ways  (Home  work)
a = {25 , True , 'Hyd' , 10.8}
print('set  with  print  function')
print(a) # {25 , True , 'Hyd' , 10.8}
print('Iterate  elements  of  set  with  for  loop')
for i in a:
	print(i)
#How  to  iterate  set  with  for  loop
# Find  outputs  (Home  work)
a = 'Hyd'
b = True
c = 25
d = 1
e = 'Hyd'
s = {a , b , c , d , e}
print(s) # {'Hyd',True,25}
print(len(s)) # 3
print(type(s)) # <class 'set'>
# Find  outputs  (Home  work)
s = {'Hyd',  25,  True,  10.8 }
print(s) # {'Hyd',  25,  True,  10.8 }
a , b , c , d = s
print(a) # Hyd
print(b) # 25
print(c) # True
print(d) # 10.8
# Find  outputs  (Home  work)
s = {'Hyd',  25,  True,  10.8 }
print(s) # {'Hyd',  25,  True,  10.8 }
a , *b = s
print(a) # Hyd
print(b) # [25 , True, 10.8]
print(type(b)) # <class 'list'>
# Find  outputs  (Home  work)
s = {'Hyd',  25,  True,  10.8 }
print(s) # {'Hyd',  25,  True,  10.8 }
a , *b , c = s
print(a) # Hyd
print(b) # [ 25, True]
print(c) # 10.8
# Find  outputs  (Home  work)
s = {20 , 10 , 20 , 10}
print(s) # {20 , 10 , 20 , 10}
x , y = s
print(x) # 10
print(y) # 20
# set()  function  demo  program  (Home  work)
a = range(100 , 151 , 10)
b = set(a)
print(b) # {100,110,120,130,140,150}
c = [10 , 20 , 15 , 18 , 10 , 50 , 20 , 12 , 18]
d = set(c)
print(d) # {10,12,15,18,20,50}
e = set('Rama  rAo')
print(e) # {'A', 'R', 'o', ' ', 'a', 'm', 'r'}
#print(set(25)) # Error: 'int' object is not iterable
print(set()) # set()


'''
set()  function
-----------------
1) What  does  set(sequence)  do ?  --->  Converts  sequence  to  set

2) What  does  set(No-args)  do ?  --->  Returns  an  empty  set

3) How  many  arguments  can  set()  function  take ?  --->  Zero  (or) One  but  not  more  than  one

4) Is  set(non-sequence)  valid ?  --->  No  becoz  argument  should  be  sequence
'''
# add()  method  demo  program  (Home  work)
a = set()
a . add(True)
a . add(25)
a . add(10.8)
a . add(1)
a . add('Hyd')
a . add(25)
a . add(None)
a . add('Hyd')
a . add(1.0)
print(a) # {None, True, 'Hyd', 10.8, 25}
#a . add(10 , 20 , 30)
#a . add([10,20,30])



'''
add()   method
-----------------
1) What  does  add(x)  do ?  --->  Inserts   'x'  any  where  in  the  set  becoz  set  is  unordered

2) How  many  arguments  can  add()  method  take ?  --->  Single

3) Is  set . add(mutable  object)  valid ? --->  No  becoz  set  can  not  hold  mutable  element

4) In  other  words,  argument  of  add()  method  should  be  immutable  object  only

5) What  does  set .  add(sequence)  do  ?  ---> Inserts  sequence  any  where  in  the  set  but  not  elements  of  sequence
												                          (Like  append()  method  of  list  class)
'''
# Find  outputs  (Home  work)
a = {25 , 10.8 , 'Hyd' , True}
tpl = (10 , 20 , 30)
print(a) # {25, 10.8, 'Hyd', True}
print(id(a)) # Address of a
a . add(tpl) 
a . add('Sec')
print(a) # {True, 'Hyd', 10.8, (10, 20, 30), 25, 'Sec'}
print(id(a)) # address of a
print(len(a)) # 6
#a . add([100 , 200 , 300]) # Error: unhashable type: 'list'
#a . add(set()) # Error: unhashable type: 'set'
#a . add({ }) # Error: unhashable type: 'dict'
# Find  outputs (Home  work)
s = set()
tpl = (10 , 20 , 15 , 18)
s . add(tpl)
print(s) # {(10, 20, 15, 18)}
print(len(s)) # 1
# update()  method  demo program  (Home  work)
tpl = (10 , 20 , 15, 18 , 10 , 20)
s = set()
s . update(tpl)
print(len(s)) # 4
print(s) # {10, 18, 20, 15}
#s . update(25) # Error: 'int' object is not iterable



'''
update()  method
--------------------
1) What  does  update(sequence)  do ?  ---> Inserts  elements  of  sequence  anywhere  in  the  set  but  not  sequence
											                        (Like  extend()  method  of  list  class)

2) Is  update(non-sequnece)  valid ?   --->  No  becoz  agument  should  be  sequence  only

3) How  many  arguments  can  update()  method  take ?  --->  One  (or)  more  than   one
'''
# Find  outputs  (Home  work)
a = [10 , 20 , 30]
b = {30 , 40,50 }
c = (50 , 60 , 70)
s = set()
s . update(a , b , c)
print(s) # {50, 20, 70, 40, 10, 60, 30}
print(len(s)) # 7
#s . add(a , b , c) # Error: set.add() takes exactly one argument (3 given)
# Find  outputs  (Home  work)
a = set()
a . update('Rama Rao')
print(a) # {'m', 'a', 'o', ' ', 'R'}
print(len(a)) # 5
#a . update(3 + 4j , 10.8 , True) # Error complex object is not iterable
# copy()  method  demo  program  (Home  work)
a = {10 , 20 , 15 , 18}
print(a) # {10, 18, 20, 15}
b = a . copy()
print(b) # {10, 18, 20, 15}
print(a  is  b) # False
print(a  ==  b) # True
c = a
print(a  is  c) # True



'''
1) What  does  copy()  method  do ?  --->  Copies  elements  of  a  set  to  another  set   i.e. Object  copy

2) a = b
    What  does  the  above  statement  do  when  'b'  is   a  set ?  --->   Reference  copy
																										       i.e.  id  is  copied

3) What  is  shallow  clone ?  ---> Reference  copy
     What  is  deep  clone ?  ---> Object  copy
'''
# remove()  method  demo  program  (Home  work)
a = {25 , 10.8 , 'Hyd' , True}
print(a) # {25, 10.8, 'Hyd', True}
a . remove('Hyd')
print(a) # {25, 10.8, True}
#a . remove('Sec') # Error: 'Sec'



'''
remove()   method
----------------------
1) What  does  remove(x)  do ?  ---> Removes  'x'  from  the   set

2) What  does  remove(Invalid-element)  do ?  ---> Throws  error

3) What  is  the  argument  of  remove()  method ?  --->  Element  to  be  removed
'''
# discard()  method  demo  program (Home  work)
a = {25 , 10.8 , 'Hyd' , True}
print(a) # {25 , 10.8 , 'Hyd' , True}
a . discard('Hyd')
print(a) # {25, 10.8, True}
a . discard('Sec')
print(a) # {25, 10.8, True}
#a . remove('Sec')


'''
1) What  does  discard(x)  do ?  --->  Removes  'x'  from  the  set

2) Does  discard(Invalid  element)  throw  error ?  --->  No
'''
# clear()  method  demo  program (Home  work)
a = {10 , 20 , 15 , 18}
print(a)# {10 , 20 , 15 , 18}
a . clear()
print(a) # set()
print(len(a)) # 0



'''
What  does  clear()  method  do ?  ---> Removes  all  the  elements  of  set  and  set  becomes  empty
'''
# Find  outputs  (Home work)
a = {10 , 20 , 30 , 40}
b = [30 , 40 , 50 , 60]
print(a . union(b)) # {40, 10, 50, 20, 60, 30}
#print(a | b) # Error: unsupported operand type(s) for |: 'set' and 'list'
#print(b . union(a)) # Error: 'list' object has no attribute 'union'
#print(a + b) # Error: unsupported operand type(s) for +: 'set' and 'list'