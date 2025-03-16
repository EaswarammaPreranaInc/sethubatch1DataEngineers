# Find  outputs   (Home  work)
a = 25 , 10.8 , 3 + 4j , 'Hyd' , True , None , 'Hyd' , 25
print(a) # (25 , 10.8 , 3 + 4j , 'Hyd' , True , None , 'Hyd' , 25)
print(type(a)) # <class 'tuple'>
a[3] = 'Sec' # tuple is immutable
a[3 : 6] = 60 , 70 , 80 #Tuple is immutable

#  What   are  the  outputs  if  input  is  (10 , 20 , 30 , 40) ?   (Home  work)
a = input('Enter  Tuple  :  ')
print(a)  #(10 , 20 , 30 , 40)
print(type(a)) #<class 'str'>
b = eval(a)
print(b) # (10 , 20 , 30 , 40)
print(type(b)) #<class 'tuple'>
print(len(b)) #4

# Find  outputs  (Home  work)
a = (10 , [20 , 30 , 40] , 50 , 60)
a[1][0] = 70
print(a) # (10 , [70 , 30 , 40] , 50 , 60)
a[1] = [80 , 90 , 100] # tuple is immutable
print(a) #  (10 , [20 , 30 , 40] , 50 , 60)

# Find  outputs  (Home  work)
a = [10 , (20 , 30 , 40) , 50 , 60]
a[1][0] = 70 # error
print(a)  # [10 , (20 , 30 , 40) , 50 , 60]
a[1] = [80 , 90]
print(a) #[10, [80, 90], 50, 60]


# Find  outputs   (Home  work)
a = 25
b = 10.8
c = 'Hyd'
d = True
x = a , b , c , d
print(x) #(25, 10.8, 'Hyd', True)
print(type(x)) #<class 'tuple'>

# Find  outputs   (Home  work)
x = 25 , 10.8 , 'Hyd' , True
a , b , c , d = x
print(a) #25
print(b) #10.8
print(c) #'Hyd'
print(d) # True
p , q , r =  x # to many values to unpack
a , b , c , d  , e = x # to many values to unpack

# Find  outputs   (Home  work)
x = 25 , 10.8 , 'Hyd' , True
a , *b , c = x
print(a) # 25
print(b) # [10.8,'Hyd']
print(c) # True

# Find  outputs   (Home  work)
tpl = 25 , 10.8 , 'Hyd' , True
a , b , *c , d , e = tpl
print(a) # 25
print(b) # 10.8
print(c) #[]
print(d) # 'Hyd'
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
print(b) #(100, 110, 120, 130, 140)
print(type(b)) #<class 'tuple'>
c = [10 , 20 , 15, 18]
d = tuple(c)
print(d) #(10, 20, 15, 18)
e = tuple('Vamsi')
print(e) #('V', 'a', 'm', 's', 'i')
print(tuple(25)) # error
print(tuple()) # empty

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
'''
15 is found at index :  2
15 is found at index :  5
15 is found at index :  8
15  is  found  3  times'''

#  How  to  modify  an  element  of  tuple ?    (Home  work)
a  =  10 ,  20 ,  30 ,   40 ,  50
#     0      1       2       3      4
# a[2] = 35
print(a)
print(id(a))
# How  to  modify  30  in  tuple  to  35
a = list(a)
a[2] = 35
a = tuple(a)
print(a)
print(id(a))

# How  to  delete  an  element  of  tuple ?   (Home  work)
a  = 10 , 20 , 30 , 40 , 50
#    0     1      2     3      4
# a . remove(30)
# del  a[2]
# a . pop(2)
print(a)
print(id(a))
# How  to  remove  30  from  tuple  'a'
a = list(a)
# a . remove(30)
# del  a[2]
a . pop(2)
a= tuple(a)
print(a)
print(id(a))


#  Nested   tuple  (Home  work)
a = ( (10 , 20)  ,  (30 , 40 , 50)  ,  (60 , 70 , 80 , 90) )
print(a)
print(type(a))
print(len(a))
# print(How  to  print  1st  inner  tuple)
print(a[0])
# print(How  to  print  2nd  inner  tuple)
print(a[1])
# print(How  to  print  3rd  inner  tuple)
print(a[2])
# print(How  to  print  20)
print(a[0][1])
# print(How  to  print  50)
print(a[1][2])
# print(How  to  print  90)
print(a[2][3])


# Find  outputs  (Home  work)
a = ((10 , 20 , 30),)
# print(How  to   print  inner  tuple)
print(a[0])
# print(How  to   print  inner  tuple  in  another  way)
print(*a)
# print(How   to  print   10)
print(a[0][0])
# print(How   to  print   20)
print(a[0][1])
# print(How   to  print   30)
print(a[0][2])
b = ((),)
# print(How  to   print  inner  tuple  of  tuple  'b')
print(*b)
# print(How  to   print  inner  tuple  of  tuple  'b'  in  another  way)
print(b[0])

#  Find  outputs (Home  work)
a = ((10 , 20 , 30))
print(a)
print(*a)
b = (())
print(b)
print(*b)
'''
(10, 20, 30)
10 20 30
()
empty
'''

# What  are  the  outputs  if  input  is  {10 , 20 , 15 , 18 , 20 , 12 , 18}
a = input('Enter  Set  :  ')
print(a)
print(type(a))
b = eval(a)
print(b)
print(type(b))
'''
Enter  Set  :  {10 , 20 , 15 , 18 , 20 , 12 , 18}
{10 , 20 , 15 , 18 , 20 , 12 , 18}
<class 'str'>
{18, 20, 10, 12, 15}
<class 'set'>'''

#  Find  outputs  (Home  work)
print({(10 , 20 , 30)}) #{(10, 20, 30)}
print({[10 , 20 , 30]}) #A set only allows hashable (immutable) elements.
print({{10 , 20 , 30}}) #A set only allows hashable (immutable) elements.
print({{}}) #A set only allows hashable (immutable) elements.

# How  to  print  set  in  differnet ways  (Home  work)
a = {25 , True , 'Hyd' , 10.8}
print('set  with  print  function')
print(a)
print('Iterate  elements  of  set  with  for  loop')
# How  to  iterate  set  with  for  loop
for i in a:
	print(i)

# Find  outputs  (Home  work)
s = {'Hyd', 25, True, 10.8}
print(s)
a, b, c, d = s
print(a)
print(b)
print(c)
print(d)
'''
{'Hyd', 25, 10.8, True}
Hyd
25
10.8
True
in which order a is printed same values will be assigned'''

# Find  outputs  (Home  work)
s = {'Hyd',  25,  True,  10.8 }
print(s)
a , *b = s
print(a)
print(b)
print(type(b))
'''
{25, 10.8, 'Hyd', True}
25
[10.8, 'Hyd', True]
<class 'list'>'''

# Find  outputs  (Home  work)
s = {'Hyd',  25,  True,  10.8 }
print(s)
a , *b , c = s
print(a)
print(b)
print(c)

'''
{25, 10.8, 'Hyd', True}
25
[10.8, 'Hyd']
True'''

# Find  outputs  (Home  work)
s = {20 , 10 , 20 , 10}
print(s)
x , y = s
print(x)
print(y)
'''
{10, 20}
10
20
'''

# set()  function  demo  program  (Home  work)
a = range(100 , 151 , 10)
b = set(a)
print(b)
c = [10 , 20 , 15 , 18 , 10 , 50 , 20 , 12 , 18]
d = set(c)
print(d)
e = set('Rama  rAo')
print(e)
# print(set(25))
print(set())
'''
{130, 100, 140, 110, 150, 120}
{10, 12, 15, 18, 50, 20}
{'r', 'm', 'o', 'a', ' ', 'A', 'R'}
Error
set()'''

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
print(a)  #{None, True, 'Hyd', 10.8, 25}
a . add(10 , 20 , 30) #error
a . add([10,20,30]) # error


# Find  outputs  (Home  work)
a = {25 , 10.8 , 'Hyd' , True}
tpl = (10 , 20 , 30)
print(a)
print(id(a))
a . add(tpl)
a . add('Sec')
print(a)
print(id(a))
print(len(a))
a . add([100 , 200 , 300])
a . add(set())
a . add({ })
'''
{'Hyd', 25, 10.8, True}
2943238018592
{True, 'Sec', 'Hyd', 10.8, (10, 20, 30), 25}
2943238018592
6
error
error
error'''

# Find  outputs (Home  work)
s = set()
tpl = (10 , 20 , 15 , 18)
s . add(tpl)
print(s)
print(len(s))
'''
{(10, 20, 15, 18)}
1
'''
# update()  method  demo program  (Home  work)
tpl = (10 , 20 , 15, 18 , 10 , 20)
s = set()
s . update(tpl)
print(len(s))
print(s)
s . update(25)
'''
4
{10, 18, 20, 15}
error
'''

# Find  outputs  (Home  work)
a = [10 , 20 , 30]
b = {30 , 40,50 }
c = (50 , 60 , 70)
s = set()
s . update(a , b , c)
print(s)
print(len(s))
s . add(a , b , c)
'''
{50, 20, 70, 40, 10, 60, 30}
7
add takes only one argument error
'''

# copy()  method  demo  program  (Home  work)
a = {10 , 20 , 15 , 18}
print(a)
b = a . copy()
print(b)
print(a  is  b)
print(a  ==  b)
c = a
print(a  is  c)
'''
{10, 18, 20, 15}
{10, 18, 20, 15}
False
True
True
'''

# remove()  method  demo  program  (Home  work)
a = {25 , 10.8 , 'Hyd' , True}
print(a)
a . remove('Hyd')
print(a)
a . remove('Sec')
'''
{25, 10.8, True, 'Hyd'}
{25, 10.8, True}
Error'''

# discard()  method  demo  program (Home  work)
a = {25 , 10.8 , 'Hyd' , True}
print(a)
a . discard('Hyd')
print(a)
a . discard('Sec')
print(a)
a . remove('Sec')
'''
{'Hyd', 25, 10.8, True}
{25, 10.8, True}
{25, 10.8, True}'''

# clear()  method  demo  program (Home  work)
a = {10 , 20 , 15 , 18}
print(a)
a . clear()
print(a)
print(len(a))
'''
{10, 18, 20, 15}
set()
0'''

# Find  outputs  (Home work)
a = {10 , 20 , 30 , 40}
b = [30 , 40 , 50 , 60]
print(a . union(b))
print(a | b) # error no pipe b/w set and pipe
print(b . union(a)) # list doesnt have union
print(a + b) # error
