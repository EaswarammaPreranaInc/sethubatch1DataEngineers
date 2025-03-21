'''
#1)Find  outputs   (Home  work)

a = 25 , 10.8 , 3 + 4j , 'Hyd' , True , None , 'Hyd' , 25
print(a) # (25, 10.8, (3+4j), 'Hyd', True, None, 'Hyd', 25)
print(type(a)) # <class 'tuple'>
a[3] = 'Sec'# Error due to tuple cannot be modified
a[3 : 6] = 60 , 70 , 80  # Error due to Tuple cannot be modified


#2)What   are  the  outputs  if  input  is  (10 , 20 , 30 , 40) ?   (Home  work)

a = input('Enter  Tuple  :  ') #(5,6,20,40,50,60)
print(a) #(5,6,20,40,50,60)
print(type(a)) # <class 'str'>
b = eval(a)
print(b) # (5, 6, 20, 40, 50, 60)
print(type(b)) # <class 'tuple'>
print(len(b)) # 6

#3)Find  outputs  (Home  work)

a = (10 , [20 , 30 , 40] , 50 , 60)
a[1][0] = 70 # replace the 20 in the 1st inner list with 70
print(a) # (10, [70, 30, 40], 50, 60)
#a[1] = [80 , 90 , 100]  #Error due to Tuple cannot be modified
print(a)  #(10, [70, 30, 40], 50, 60)

#4) Find  outputs  (Home  work)

a = [10 , (20 , 30 , 40) , 50 , 60]
#a[1][0] = 70 # Error due to inner Tuple cannot be modified
print(a)# [10, (20, 30, 40), 50, 60]
a[1] = [80 , 90] #inner Tuple with index 1 is Replaced with another list [80,90]
print(a) #[10, [80, 90], 50, 60]

#5)Find  outputs   (Home  work)

a = 25
b = 10.8
c = 'Hyd'
d = True
x = a , b , c , d #  Assign values to Tuple 'x'.
print(x) #(25, 10.8, 'Hyd', True)
print(type(x)) #<class 'tuple'>

#6)Find  outputs   (Home  work)

x = 25 , 10.8 , 'Hyd' , True
a , b , c , d = x
print(a) # 25
print(b) # 10.8
print(c) #'Hyd'
print(d) # True
#p , q , r =  x # Error Due to Many values cannot be unpacked, Tuple can unpack only one element.
#a , b , c , d  , e = x # Error Due to Many values cannot be unpacked, Tuple can unpack only one element.

#7)Find  outputs   (Home  work)

x = 25 , 10.8 , 'Hyd' , True
a , *b , c = x
print(a) # 25
print(b) #[10.8, 'Hyd']
print(c) # True

#8)Find  outputs   (Home  work)

tpl = 25 , 10.8 , 'Hyd' , True
a , b , *c , d , e = tpl
print(a) # 25
print(b) # 10.8
print(c) # []
print(d) # Hyd
print(e) # True

#9)Find  outputs   (Home  work)

x = 25 , 10.8 , 'Hyd' , True , 3 + 4j
a , b , _ , d , _= x
print(a) # 25
print(b) # 10.8
print(_) # (3+4j)
print(d) # True
print(_) # (3+4j)

#10)tuple()  function  demo  program   (Home  work)

a = range(100 , 150 , 10)
b = tuple(a) # Convert range to Tuple of elements
print(b) # (100, 110, 120, 130, 140)
print(type(b)) # <class 'tuple'>
c = [10 , 20 , 15, 18] 
d = tuple(c) # Convert range to list of elements
print(d) # (10, 20, 15, 18)
e = tuple('Vamsi') # Convert String to Tuple of elements
print(e) # ('V', 'a', 'm', 's', 'i')
#print(tuple(25)) # Error Due to  int '25'
print(tuple()) #()

#11)index()  and  count()  methods  demo  program   (Home  work)

a = (10 , 20 , 15 , 12 , 14 , 15 , 18 , 19 , 15 , 12 , 25)
#     0    1      2     3    4     5     6    7     8    9    10
try:
	i = a . index(15)
	while  True:
		print('15 is found at index : ' , i)
		i = a . index(15 , i + 1)
except:
		print(F'15  is  found  {a . count(15)}  times')

output
-------
15 is found at index :  2
15 is found at index :  5
15 is found at index :  8
15  is  found  3  times

#12)How  to  modify  an  element  of  tuple ?    (Home  work)

a  =  10 ,  20 ,  30 ,   40 ,  50
#     0      1       2       3      4
#a[2] = 35 # Error due to Tuple cannot be modified
print(a) #(10, 20, 30, 40, 50)
print(id(a)) #2562304546576
a=list(a)a[2]=35 #How  to  modify  30  in  tuple  to  35
print(a) #[10, 20, 35, 40, 50]
print(id(a)) # 2599407712384

#13)How  to  delete  an  element  of  tuple ?   (Home  work)

a  = 10 , 20 , 30 , 40 , 50
#    0     1      2     3      4
a . remove(30) # Error due to remove,we cannot have remove method in Tuple
del  a[2] # Error due to del,we cannot have delete method in Tuple
a . pop(2) ## Error due to pop,we cannot have pop method in Tuple
print(a) # (10, 20, 30, 40, 50)
print(id(a)) # 3072842045200
a = tuple(item for item in a if item != 30) # How  to  remove  30  from  tuple  'a'
print(a) # (10, 20, 40, 50)
print(id(a)) # 3126697193728

#14)Nested   tuple  (Home  work)

a = ( (10 , 20)  ,  (30 , 40 , 50)  ,  (60 , 70 , 80 , 90) )
print(a) # ((10, 20), (30, 40, 50), (60, 70, 80, 90))
print(type(a)) # <class 'tuple'>
print(len(a)) # 3
print(a[0]) #How  to  print  1st  inner  tuple
print(a[1]) # How  to  print  2nd  inner  tuple
print(a[2]) # How  to  print  3rd  inner  tuple
print(a[0][1]) # How  to  print  20
print(a[1][2])  # How  to  print  50
print(a[2][3]) # How  to  print  90)

#15)Find  outputs  (Home  work)

a = ((10 , 20 , 30),)
print(a[0]) # How  to   print  inner  tuple
print(a[-1]) # How  to   print  inner  tuple  in  another  way
print(a[0][0]) # How   to  print   10
print(a[0][1]) # How   to  print   20
print(a[0][2]) # How   to  print   3)
b = ((),)
print(b[0]) # How  to   print  inner  tuple  of  tuple  'b')
inner_tuple_b = b[0]
print(inner_tuple_b) # (How  to   print  inner  tuple  of  tuple  'b'  in  another  way)

#16)Find  outputs (Home  work)

a = ((10 , 20 , 30))
print(a) # (10, 20, 30)
print(*a) # 10 20 30 ----> unpacking the Tuple
b = (())
print(b) # ()
print(*b) # empty tuple , so unpacking empty Tuple

#17)What  are  the  outputs  if  input  is  {10 , 20 , 15 , 18 , 20 , 12 , 18}

a = input('Enter  Set  :  ') #{10, 20, 30, 40, 50}
print(a) # {10, 20, 30, 40, 50}
print(type(a)) # <class 'str'>
print(id(a)) # 1567652313456
b = eval(a) #converts set to another set of elements 
print(b) # (10, 20, 30, 40, 50)
print(type(b)) #  <class 'set'>
print(id(b)) # 1567652004576

#18)Find  outputs  (Home  work)

print({(10 , 20 , 30)}) # {(10, 20, 30)}
print({[10 , 20 , 30]}) # Error duen to unhashable list
print({{10 , 20 , 30}}) # Error due to unhashable set
print({{}}) # Error due to unhashable dict

#19)How  to  print  set  in  differnet ways  (Home  work)


a = {25 , True , 'Hyd' , 10.8}
print('set  with  print  function')
print(a)
print('Iterate  elements  of  set  with  for  loop')
How  to  iterate  set  with  for  loop

a = {25 , True , 'Hyd' , 10.8}
print(a) # {25, 10.8, 'Hyd', True}
for element in a:
    print(element) # 25<next line> 10.8 <next line> Hyd <next line> True ----> in any order.

#20)Find  outputs  (Home  work)

a = 'Hyd'
b = True
c = 25
d = 1
e = 'Hyd'
s = {a , b , c , d , e}
print(s) # {'Hyd', True, 25} in any order
print(len(s)) # 3
print(type(s)) # <class 'set'>

#21)Find  outputs  (Home  work)

s = {'Hyd',  25,  True,  10.8 }
print(s) # {25, 10.8, 'Hyd', True} in any order
a , b , c , d = s
print(a) # 25
print(b)# 10.8
print(c)# Hyd
print(d)# True

#22)Find  outputs  (Home  work)

s = {'Hyd',  25,  True,  10.8 }
print(s) # {'Hyd', 10.8, 25, True}
a , *b = s
print(a) # Hyd
print(b) #[ 10.8, 25, True]
print(type(b)) # <class 'list'>

#23)Find  outputs  (Home  work)

s = {'Hyd',  25,  True,  10.8 }
print(s) # {25, 10.8, True, 'Hyd'}
a , *b , c = s
print(a) # 25
print(b) # [10.8, True]
print(c)  # Hyd

#24)Find  outputs  (Home  work)

s = {20 , 10 , 20 , 10}
print(s) # {10,20}
x , y = s
print(x) #10
print(y) #20

#25)set()  function  demo  program  (Home  work)

a = range(100 , 151 , 10)
b = set(a)
print(b) # {130, 100, 140, 110, 150, 120}
c = [10 , 20 , 15 , 18 , 10 , 50 , 20 , 12 , 18]
d = set(c)
print(d) # {10, 12, 15, 18, 50, 20}
e = set('Rama  rAo')
print(e) # {'o', 'm', 'R', ' ', 'r', 'a', 'A'} ---> in any order
#print(set(25)) #Error due to int 25
print(set()) # set()

#26)add()  method  demo  program  (Home  work)

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
print(a) # {None, True, 10.8, 25, 'Hyd'} 
a . add(10 , 20 , 30) # Error due to more arguments
a . add([10,20,30]) # error due to unhashable list

#27) Find  outputs  (Home  work)

a = {25 , 10.8 , 'Hyd' , True}
tpl = (10 , 20 , 30)
print(a) # {25, 10.8, 'Hyd', True}
print(id(a)) # 2097537499872
a . add(tpl)
a . add('Sec')
print(a) # {True, 'Hyd', 10.8, (10, 20, 30), 25, 'Sec'} in any orders.
print(id(a)) # 2097537499872
print(len(a)) # 6
a . add([100 , 200 , 300]) #Error due to unhashable list
a . add(set()) #Error due to unhashable set
a . add({ }) #Error due to unhashable dict

#28)Find  outputs (Home  work)

s = set()
tpl = (10 , 20 , 15 , 18)
s . add(tpl)
print(s) # {(10, 20, 15, 18)}
print(len(s)) # 1

#29) update()  method  demo program  (Home  work)

tpl = (10 , 20 , 15, 18 , 10 , 20)
s = set()
s . update(tpl)
print(len(s)) # 4
print(s) # {10, 18, 20, 15}
s . update(25) #Error due to int 25

#30)Find  outputs  (Home  work)

a = [10 , 20 , 30]
b = {30 , 40,50 }
c = (50 , 60 , 70)
s = set()
s . update(a , b , c)
print(s) # {50, 20, 70, 40, 10, 60, 30}
print(len(s)) # 7
s . add(a , b , c) # Error due to more arguments

#31)Find  outputs  (Home  work)

a = set()
a . update('Rama Rao')
print(a) # {'R', 'a', 'm', 'o', ' '}
print(len(a)) #  5
a . update(3 + 4j , 10.8 , True) # Error due to complex number

#32)copy()  method  demo  program  (Home  work)

a = {10 , 20 , 15 , 18}
print(a) # {10, 18, 20, 15}
b = a . copy()
print(b) # {10, 18, 20, 15}
print(a  is  b) # False
print(a  ==  b) # True
c = a
print(a  is  c) # True

#33)remove()  method  demo  program  (Home  work)

a = {25 , 10.8 , 'Hyd' , True}
print(a) # {25, 10.8, True, 'Hyd'}
a . remove('Hyd')
print(a) # {25, 10.8, True}
a . remove('Sec') # Error due to 'Sec' is not in 'a'

#34)discard()  method  demo  program (Home  work)

a = {25 , 10.8 , 'Hyd' , True}
print(a) # {25, 10.8, 'Hyd', True}
a . discard('Hyd')
print(a) # {25, 10.8, True}
a . discard('Sec')
print(a) # {25, 10.8, True}
a . remove('Sec') # Error  due to 'Sec' is not in 'a'

#35)clear()  method  demo  program (Home  work)

a = {10 , 20 , 15 , 18}
print(a) # {10, 18, 20, 15}
a . clear()
print(a) # set()s
print(len(a)) # 0

#36)Find  outputs  (Home work)
'''
a = {10 , 20 , 30 , 40}
b = [30 , 40 , 50 , 60]
print(a . union(b)) # {40, 10, 50, 20, 60, 30}
print(a | b) # unsupported operand type(s) for |: 'set' and 'list'
#print(b . union(a)) # Error  bcz list has no method of unions.
#print(a + b) # Error due to we cannot concatinate set and list

