# Find  outputs   (Homework)
a = 25, 10.8, 3 + 4j, 'Hyd', True, None, 'Hyd', 25
print(a)  # (25,10.8,3+4j,'Hyd',True,None,'Hyd',25)
print(type(a))  # <class 'tuple'>
# a[3] = 'Sec'  # Error because tuple is immutable
# a[3:6] = 60, 70, 80  # Error because tuple is immutable

'''  Output
(25, 10.8, (3+4j), 'Hyd', True, None, 'Hyd', 25)
<class 'tuple'>
'''


#  What   are  the  outputs  if  input  is  (10 , 20 , 30 , 40) ?   (Homework)
a = input('Enter  Tuple  :  ')  # (10,20,30,40)
print(a)  # (10,20,30,40)
print(type(a))  # <class 'str'>
b = eval(a)  # converts string tuple to tuple
print(b)  # (10,20,30,40)
print(type(b))  # <class 'tuple'>
print(len(b))  # 4

'''  Output
Enter  Tuple  :  (10,20,30,40)
(10,20,30,40)
<class 'str'>
(10, 20, 30, 40)
<class 'tuple'>
4

'''


# Find  outputs  (Homework)
a = (10, [20, 30, 40], 50, 60)
a[1][0] = 70  # tuple at index 1 have inner list it can be modified at index 0 20 replaces with 70
print(a)  # (10,[70,30,40],50,60)
# a[1] = [80, 90,100]  # Error because tuple is immutable
print(a)  # (10,[70,30,40],50,60)

'''   Output
(10, [70, 30, 40], 50, 60)
(10, [70, 30, 40], 50, 60)
'''



# Find  outputs  (Homework)
a = [10, (20, 30, 40), 50, 60]
# a[1][0] = 70  # Error because tuple is immutable
print(a)  # [10,(20,30,40),50,60]
a[1] = [80,90]  # In list 'a' at index 1 (70,30,40) replaces with [80,90]
print(a)  # [10,[80,90],50,60]

'''   Output
[10, (20, 30, 40), 50, 60]
[10, [80, 90], 50, 60]
'''


# Find  outputs   (Homework)
a = 25
b = 10.8
c = 'Hyd'
d = True
x = a, b, c, d  # packing a,b,c,d into x tuple
print(x)  # (25,10.8,'Hyd',True)
print(type(x))  # <class 'tuple'>

'''   Output
(25, 10.8, 'Hyd', True)
<class 'tuple'>
'''



# Find  outputs (Homework)
x = 25, 10.8, 'Hyd', True
a, b, c, d = x  # unpacks the tuple into 4 elements
print(a)  # 25
print(b)  # 10.8
print(c)  # 'Hyd'
print(d)  # True
# p, q, r = x  # Error due to more elements to unpack
# a, b, c, d, e = x  # Error due to less elements to unpack

'''   Output
25
10.8
Hyd
True
'''


# Find  outputs   (Homework)
x = 25, 10.8, 'Hyd', True
a, *b, c = x  # unpacks the tuple into 3 elements
print(a)  # 25
print(b)  # [10.8,'Hyd']
print(c)  # True

'''
25
[10.8, 'Hyd']
True
'''




# Find  outputs  (Homework)
tpl = 25, 10.8, 'Hyd', True
a, b, *c, d, e = tpl   # unpacks into 5 elements
print(a)  # 25
print(b)  # 10.8
print(c)  # []
print(d)  # 'Hyd'
print(e)  # True

'''  Output
25
10.8
[]
Hyd
True
'''


# Find  outputs   (Homework)
x = 25, 10.8, 'Hyd', True, 3 + 4j
a, b, _, d, _ = x  # unpacks tuple into 4 elements
print(a)  # 25
print(b)  # 10.8
print(_)  # 3+4j
print(d)  # True
print(_)  # 3+4j

'''    Output
25
10.8
(3+4j)
True
(3+4j)
'''


# tuple()  function  demo  program   (Homework)
a = range(100, 150, 10)  # (100,110,120,130,140)
b = tuple(a)  # converts sequence to tuple
print(b)  # (100,110,120,130,140)
print(type(b))  # <class 'tuple'>
c = [10, 20, 15, 18]
d = tuple(c)  # converts list to tuple because list is a sequence
print(d)  # (10,20,15,18)
e = tuple('Vamsi')  #  converts string to tuple
print(e)  # ('V','a','m','s','i')
# print(tuple(25))  # Error because int argument it is not a sequence
print(tuple())  # Empty tuple because of no argument

'''  Output
(100, 110, 120, 130, 140)
<class 'tuple'>
(10, 20, 15, 18)
('V', 'a', 'm', 's', 'i')
()

'''


#index()  and  count()  methods  demo  program   (Home  work)
a = (10, 20, 15, 12, 14, 15, 18, 19, 15, 12, 25)
#     0    1      2     3    4     5     6    7     8    9    10
try:
	i = a . index(15)
	while  True:
		print('15 is found at index : ' , i)
		i = a . index(15 , i + 1)
except:
		print(F'15  is  found  {a . count(15)} times')
        
'''   Output
15 is found at index :  2
15 is found at index :  5
15 is found at index :  8
15  is  found  3 times
'''


#  How  to  modify  an  element  of  tuple ?    (Home  work)
a = 10, 20, 30, 40, 50
#     0      1       2       3      4
# a[2] = 35  # Error because tuple is immutable
print(a)  # (10,20,30,40,50)
print(id(a))  # Address of the tuple
a=a[:3]+(35,)+a[3:]# How  to  modify  30  in  tuple  to  35
print(a)  # (10,20,30,35,40,50)
print(id(a))  # Different address

'''   Output
(10, 20, 30, 40, 50)
2625309340864
(10, 20, 30, 35, 40, 50)
2625313497120
'''


# How  to  delete  an  element  of  tuple ?   (Homework)
a= 10, 20, 30, 40, 50
#    0     1      2     3      4
# a . remove(30)  # Error because tuple has no remove() method since tuple is immutable
# del  a[2]  # Error because tuple is immutable
# a . pop(2)  # Error because tuple has no pop() method since tuple is immutable
print(a)  # (10,20,30,40,50)
print(id(a))  # Address of the tuple 'a'
a=list(a)  # converts tuple to list  # How  to  remove  30  from  tuple  'a'
a.remove(30)  # remove element 30 in list 'a'
a=tuple(a)  # converts list to tuple
print(a)  # (10,20,40,50)
print(id(a))  # Different address


'''   Output
(10, 20, 30, 40, 50)
1463095293120
(10, 20, 40, 50)
1463100064048
'''


#  Nested   tuple  (Homework)
a = ((10, 20),  (30, 40, 50),  (60, 70, 80, 90))
print(a)  # ((10,20).(30,40,50),(60,70,80,90))
print(type(a))  # <class 'tuple'>
print(len(a))  # 3
print(a[0])  # How  to  print  1st  inner  tuple  ---> (10,20)
print(a[1])  # How  to  print  2nd  inner  tuple  ---> (30,40,50)
print(a[2])  # How  to  print  3rd  inner  tuple)  ---> (60,70,80,90)
print(a[0][1])  # How  to  print  20 --> 20
print(a[1][2])  # How  to  print  50 --> 50
print(a[2][3])  # How  to  print  90) --> 90

'''  Output
((10, 20), (30, 40, 50), (60, 70, 80, 90))
<class 'tuple'>
3
(10, 20)
(30, 40, 50)
(60, 70, 80, 90)
20
50
90

'''


# Find  outputs  (Homework)
a = ((10 , 20 , 30),)
print(a[0])  # How  to   print  inner  tuple ---> (10,20,30)
for x in a: # How  to   print  inner  tuple  in  another  way
    print(x)  # (10,20,30)
print(a[0][0])  # How   to  print   10 ---> 10
print(a[0][1])  # How   to  print   20) ---> 20
print(a[0][1])  # How   to  print   30) ---> 30
b = ((),)
print(b[0])  # How  to   print  inner  tuple  of  tuple  'b' ---> ()
for x in b: # How  to   print  inner  tuple  of  tuple  'b'  in another way
    print(x)  # ()

'''   Output
(10, 20, 30)
(10, 20, 30)
10
20
20
()
()

'''


#  Find  outputs (Homework)
a = ((10, 20 ,30))
print(a)  # (10,20,30)
print(*a)  # 10 20 30
b = (())
print(b)  # ()
print(*b)  # Empty space

'''  Output
(10, 20, 30)
10 20 30
()


'''


# What  are  the  outputs  if  input  is  {10 , 20 , 15 , 18 , 20 , 12 , 18}
a = input('Enter  Set  :  ')  # {10 , 20 , 15 , 18 , 20 , 12 , 18}
print(a)  # {10,20,15,18,12}  i.e. duplicate elements are ignored
print(type(a))  # <class 'str'>
b = eval(a)  # converts str to appropriate object
print(b)  # {10 , 20 , 15 , 18 , 12}
print(type(b))  # <class 'set'>

'''
Enter  Set  :  {10 , 20 , 15 , 18 , 20 , 12 , 18}
{10 , 20 , 15 , 18 , 20 , 12 , 18}
<class 'str'>
{18, 20, 10, 12, 15}
<class 'set'>
'''



#  Find  outputs  (Homework)
print({(10, 20, 30)})  # {(10,20,30)}
# print({[10, 20, 30]})  # Error due to list is mutable object
# print({{10, 20, 30}})  # Error due to set is mutable object
# print({{}})  # # Error due to dict is mutable object

'''  Output
{(10, 20, 30)}
'''


# How  to  print  set  in  differnet ways  (Homework)
a = {25, True, 'Hyd', 10.8}
print('set  with  print  function')
print(a)  # {25,True,'Hyd',10.8} changes its order everytime we run
print('Iterate  elements  of  set  with  for  loop')
for x in a:  # How  to  iterate  set  with for loop
    print(x)  # 25 <nextline> 10.8 <nextline> True <nextline> 'Hyd'

'''   Sample Output
set  with  print  function
{25, 10.8, 'Hyd', True}
Iterate  elements  of  set  with  for  loop
25
10.8
Hyd
True

'''


# Find  outputs  (Homework)
a = 'Hyd'
b = True
c = 25
d = 1
e = 'Hyd'
s = {a, b, c, d, e}  # packs 5 elements to set 's'
print(s)  # {'Hyd',True,25}   duplicate elements are ignored in set
print(len(s))  # 3
print(type(s))  # <class 'set'>

'''  Sample Output
{True, 'Hyd', 25}
3
<class 'set'>
'''


# Find  outputs  (Homework)
s = {'Hyd',  25,  True,  10.8}
print(s)  # {'Hyd',25,True,10.8}  i.e. changes order every time we run
a, b, c, d = s  # unpacks set into 4 elements
print(a)  # 'Hyd'
print(b)  # 25
print(c)  # True
print(d)  # 10.8

'''  Output
{25, 10.8, 'Hyd', True}
25
10.8
Hyd
True
'''


# Find  outputs  (Homework)
s = {'Hyd',  25,  True,  10.8}
print(s)  # {'Hyd',  25,  True,  10.8}   i.e. changes order every time we run
a, *b = s  # Unpacks set to 2 elements
print(a)  # 'Hyd'
print(b)  # [25,True,10.8]
print(type(b))  # <class 'list'>

'''   Output
{25, 10.8, 'Hyd', True}
25
[10.8, 'Hyd', True]
<class 'list'>

'''


# Find  outputs  (Homework)
s = {'Hyd',  25,  True,  10.8}
print(s)  # {'Hyd',25,10.8,True}  i.e. order changes
a, *b, c = s  # unpacks set into 3 elements
print(a)  # 'Hyd'
print(b)  # [25,True]
print(c)  # 10.8   i.e. order changes

'''   OUTPUT
{25, 10.8, 'Hyd', True}
25
[10.8, 'Hyd']
True
'''


# Find  outputs  (Homework)
s = {20, 10, 20, 10}
print(s)  # {20,10}  i.e. Duplicates are ignored
x, y = s  # unpacks set into 2 elements
print(x)  # 20
print(y)  # 10

'''   OUTPUT
{10, 20}
10
20
'''


# set()  function  demo  program  (Homework)
a = range(100, 151, 10)  # a=(100,110,120,130,140,150)
b = set(a)  # converts sequence to set
print(b)  # {100,110,120,130,140,150}
c = [10, 20, 15, 18, 10, 50, 20, 12, 18]
d = set(c)  # converts list to set  i.e. list is a sequence
print(d)  # {10,20,15,18,50,12}  i.e. duplicates are ignored
e = set('Rama  rAo')  # converts string to set
print(e)  # {'R','a','m',' ','r','A','o'}
# print(set(25))  # Error because 25 is not a sequence
print(set())  # Empty set  i.e. set()

'''   OUTPUT
{130, 100, 140, 110, 150, 120}
{10, 12, 15, 18, 50, 20}
{'A', 'm', 'R', 'a', 'o', 'r', ' '}
set()
'''


# add()  method  demo  program  (Homework)
a = set()  # Empty set
a . add(True)  # add True to anywhere in the list
a . add(25)  # add 25 to anywhere in the list
a . add(10.8)  # add 10.8 to anywhere in the list
a . add(1)  # True is already in the list it is ignored
a . add('Hyd')  # add 'Hyd' to anywhere in the list
a . add(25)   # 25 is already in the list it is ignored
a . add(None)  # add None to anywhere in the list
a . add('Hyd')   # 'Hyd' is already in the list it is ignored
a . add(1.0)   # True is already in the list it is ignored
print(a)  # {True,25,10.8,'Hyd',None}
# a . add(10, 20, 30)  # Error because add hold only one argument
# a . add([10,20,30])  # Error because set can not hold mutable object i.e. list,set,dictionary

'''    OUTPUT
{True, 'Hyd', 10.8, 25, None}
'''


# Find  outputs  (Homework)
a = {25, 10.8, 'Hyd', True}
tpl = (10, 20, 30)
print(a)  # {25,10.8,'Hyd',True}
print(id(a))  # Address of the set 'a'
a . add(tpl)  # inserts tuple anywhere in the set
a . add('Sec')  # inserts string anywhere in the set
print(a)  # {25,10.8,'Hyd',True,(10,20,30),'Sec'}
print(id(a))  # Same address
print(len(a))  # 6
# a . add([100, 200, 300])  # Error because set can not hold mutable objects like list
# a . add(set())  # Error because set can not hold mutable objects like set
# a.add({})  # Error because set can not hold mutable objects like dictionary

'''    OUTPUT
{'Hyd', 25, 10.8, True}
2451510093728
{'Sec', True, 10.8, (10, 20, 30), 'Hyd', 25}
2451510093728
6
'''



# Find  outputs (Homework)
s = set()  # Empty set
tpl = (10, 20, 15, 18)
s . add(tpl)  # Inserts tuple anywhere in the empty list
print(s)  # {(10,20,15,18)}
print(len(s))  # 1

'''   OUTPUT
{(10, 20, 15, 18)}
1
'''


# update()  method  demo program  (Home  work)
tpl = (10, 20, 15, 18, 10, 20)
s = set()  # Empty set
s . update(tpl)  # Inserts elements of sequence anywhere in the list
print(len(s))  # 4
print(s)  # {10,20,15,18}
# s . update(25)  # Error because update argument must be sequence

'''    OUTPUT
4
{10, 18, 20, 15}
'''


# Find  outputs  (Homework)
a = [10, 20, 30]
b = {30, 40, 50}
c = (50, 60, 70)
s = set()  # Empty list
s . update(a, b, c)  # Insert elements of sequences a,b,c anywhere in the list
print(s)  # {10,20,30,40,50,60,70}  i.e.  Duplicate are ignored
print(len(s))  # 7
# s .add(a,b,c)  # Error because add() method has only one argument

'''    OUTPUT
{50, 20, 70, 40, 10, 60, 30}
7
'''



# Find  outputs  (Homework)
a = set()  # Empty set
a . update('Rama Rao')  # Inserts characters of sequence anywhere in the list
print(a)  # {'R','a','m',' ','o'}
print(len(a))  # 5
# a . update(3 + 4j, 10.8, True)  # Error because it is not a sequence

'''   OUTPUT
{'a', 'm', ' ', 'R', 'o'}
5
'''


# copy()  method  demo  program  (Homework)
a = {10, 20, 15, 18}
print(a)  # {10,20,15,18}
b = a . copy()  # copies elements of set 'a' to set 'b'
print(b)  # {10,20,15,18}
print(a is b)  # False because ref 'a' and 'b' points to different sets
print(a == b)  # True because same elements in the sets
c = a  # points ref 'c' to 'a'
print(a is c)  # True because ref 'a' and 'c' points to same set

'''  OUTPUT
{10, 18, 20, 15}
{10, 18, 20, 15}
False
True
True
'''


# remove()  method  demo  program  (Homework)
a = {25, 10.8, 'Hyd', True}
print(a)  # {25,10.8,'Hyd',True}
a . remove('Hyd')  # removes 'Hyd' from the list
print(a)  # {25,10.8,True}
# a . remove('Sec')  # Error because 'Sec' is not in the list

'''  OUTPUT
{25, 10.8, 'Hyd', True}
{25, 10.8, True}
'''


# discard()  method  demo  program (Homework)
a = {25, 10.8, 'Hyd', True}
print(a)  # {25,10.8,'Hyd',True}
a . discard('Hyd')  # Removes 'Hyd' from the list
print(a)  # {25,10.8,True}
a . discard('Sec')  # Ignored (it does,t throws error for invalid element)
print(a)  # {25,10.8,True}
# a . remove('Sec')  # Error because 'Sec' element is not in the list(invalid element)

'''   OUTPUT
{25, 10.8, 'Hyd', True}
{25, 10.8, True}
{25, 10.8, True}

'''


# clear()  method  demo  program (Homework)
a = {10, 20, 15, 18}
print(a)  # {10,20,15,18}
a . clear()  # Removes all the elements from the set and set becomes empty
print(a)  # set()
print(len(a))  # 0

'''    OUTPUT
{10, 18, 20, 15}
set()
0
'''


# Find  outputs  (Homework)
a = {10, 20, 30, 40}
b = [30, 40, 50, 60]
print(a . union(b))  # {10,20,30,40,50,60}  i.e. Duplicates are ignored
# print(a | b)  # Error because operands should be only set for | operator
# print(b . union(a))  # Error because list has no union() method
# print(a+b)  # Error because set and list can not be concatenated by using + operator

'''   OUTPUT 
{40, 10, 50, 20, 60, 30}
'''
