# Find  outputs   (Home  work)
a = 25 , 10.8 , 3 + 4j , 'Hyd' , True , None , 'Hyd' , 25
print(a)
print(type(a))
#a[3] = 'Sec'
#a[3 : 6] = 60 , 70 , 80
'''
OUTPUT:
(25, 10.8, (3+4j), 'Hyd', True, None, 'Hyd', 25)
<class 'tuple'>
'''

#  What   are  the  outputs  if  input  is  (10 , 20 , 30 , 40) ?   (Home  work)
a = input('Enter  Tuple  :  ')
print(a)
print(type(a))
b = eval(a)
print(b)
print(type(b))
print(len(b))
'''
OUTPUT:
Enter  Tuple  :  (10 , 20 , 30 , 40)
(10 , 20 , 30 , 40)
<class 'str'>
(10, 20, 30, 40)
<class 'tuple'>
4
'''


# Find  outputs  (Home  work)
a = (10 , [20 , 30 , 40] , 50 , 60)
a[1][0] = 70
print(a)
#a[1] = [80 , 90 , 100]
print(a)
'''
OUTPUT:
(10, [70, 30, 40], 50, 60)
(10, [70, 30, 40], 50, 60)
'''



# Find  outputs  (Home  work)
a = [10 , (20 , 30 , 40) , 50 , 60]
#a[1][0] = 70
print(a)
a[1] = [80 , 90]
print(a)
'''
OUTPUT:
[10, (20, 30, 40), 50, 60]
[10, [80, 90], 50, 60]
'''



# Find  outputs   (Home  work)
a = 25
b = 10.8
c = 'Hyd'
d = True
x = a , b , c , d
print(x)
print(type(x))
'''
OUTPUT:
(25, 10.8, 'Hyd', True)
<class 'tuple'>
'''



# Find  outputs   (Home  work)
x = 25 , 10.8 , 'Hyd' , True
a , b , c , d = x
print(a)
print(b)
print(c)
print(d)
#p , q , r =  x
#a , b , c , d  , e = x
'''
OUTPUT:
25
10.8
Hyd
True
'''



# Find  outputs   (Home  work)
x = 25 , 10.8 , 'Hyd' , True
a , *b , c = x
print(a)
print(b)
print(c)
'''
OUTPUT:
25
[10.8, 'Hyd']
True
'''



# Find  outputs   (Home  work)
tpl = 25 , 10.8 , 'Hyd' , True
a , b , *c , d , e = tpl
print(a)
print(b)
print(c)
print(d)
print(e)
'''
OUTPUT:
25
10.8
[]
Hyd
True
'''




# Find  outputs   (Home  work)
x = 25 , 10.8 , 'Hyd' , True , 3 + 4j
a , b , _ , d , _= x
print(a)
print(b)
print(_)
print(d)
print(_)
'''
OUTPUT:
25
10.8
(3+4j)
True
(3+4j)
'''




# tuple()  function  demo  program   (Home  work)
a = range(100 , 150 , 10)
b = tuple(a)
print(b)
print(type(b))
c = [10 , 20 , 15, 18]
d = tuple(c)
print(d)
e = tuple('Vamsi')
print(e)
#print(tuple(25))
print(tuple())

'''
OUTPUT:
(100, 110, 120, 130, 140)
<class 'tuple'>
(10, 20, 15, 18)
('V', 'a', 'm', 's', 'i')
()
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
'''
OUTPUT:
15 is found at index :  2
15 is found at index :  5
15 is found at index :  8
15  is  found  3  times
'''




#  How  to  modify  an  element  of  tuple ?    (Home  work)
a  =  10 ,  20 ,  30 ,   40 ,  50
#     0      1       2       3      4
#a[2] = 35
print(a)
print(id(a))
#How  to  modify  30  in  tuple  to  35
b=list(a)
b[2]=35
print(b)
print(tuple(b))
print(a)
print(id(a))
'''
OUTPUT:
(10, 20, 30, 40, 50)
2098679093008
[10, 20, 35, 40, 50]
(10, 20, 35, 40, 50)
(10, 20, 30, 40, 50)
2098679093008
'''




# How  to  delete  an  element  of  tuple ?   (Home  work)
a  = 10 , 20 , 30 , 40 , 50
#    0     1      2     3      4
#a . remove(30)
#del  a[2]
#a . pop(2)
print(a)
print(id(a))
#How  to  remove  30  from  tuple  'a'
b=list(a)
b.remove(30)
print(b)
print(tuple(b))
print(a)
print(id(a))
'''
OUTPUT:
(10, 20, 30, 40, 50)
1934392268560
[10, 20, 40, 50]
(10, 20, 40, 50)
(10, 20, 30, 40, 50)
1934392268560
'''



#  Nested   tuple  (Home  work)
a = ( (10 , 20)  ,  (30 , 40 , 50)  ,  (60 , 70 , 80 , 90) )
print(a)
print(type(a))
print(len(a))
#print(How  to  print  1st  inner  tuple)
print(a[0])
#print(How  to  print  2nd  inner  tuple)
print(a[1])
#print(How  to  print  3rd  inner  tuple)
print(a[2])
#print(How  to  print  20)
print(a[0][1])
#print(How  to  print  50)
print(a[1][2])
#print(How  to  print  90)
print(a[2][3])
'''
OUTPUT:
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




# Find  outputs  (Home  work)
a = ((10 , 20 , 30),)
#print(How  to   print  inner  tuple)
print(a[0])
#print(How  to   print  inner  tuple  in  another  way)
print(*a)
#print(How   to  print   10)
print(a[0][0])
#print(How   to  print   20)
print(a[0][1])
#print(How   to  print   30)
print(a[0][2])
b = ((),)
#print(How  to   print  inner  tuple  of  tuple  'b')
print(b[0])
#print(How  to   print  inner  tuple  of  tuple  'b'  in  another  way)
print(*b)
'''
OUTPUT:
(10, 20, 30)
(10, 20, 30)
10
20
30
()
()
'''





#  Find  outputs (Home  work)
a = ((10 , 20 , 30))
print(a)
print(*a)
b = (())
print(b)
print(*b)
'''
OUTPUT:
(10, 20, 30)
10 20 30
()
'''




# What  are  the  outputs  if  input  is  {10 , 20 , 15 , 18 , 20 , 12 , 18}
a = input('Enter  Set  :  ')
print(a)
print(type(a))
b = eval(a)
print(b)
print(type(b))
'''
OUTPUT:
Enter  Set  :  {10 , 20 , 15 , 18 , 20 , 12 , 18}
{10 , 20 , 15 , 18 , 20 , 12 , 18}
<class 'str'>
{18, 20, 10, 12, 15}
<class 'set'>
'''




#  Find  outputs  (Home  work)
print({(10 , 20 , 30)})
#print({[10 , 20 , 30]})
#print({{10 , 20 , 30}})
#print({{}})
'''
OUTPUT:
{(10, 20, 30)}
'''




# How  to  print  set  in  differnet ways  (Home  work)
a = {25 , True , 'Hyd' , 10.8}
print('set  with  print  function')
print(a)
print(a)
print('Iterate  elements  of  set  with  for  loop')
for i in a:
	print(i)

'''
OUTPUT:
set  with  print  function
{25, 10.8, 'Hyd', True}
{25, 10.8, 'Hyd', True}
Iterate  elements  of  set  with  for  loop
25
10.8
Hyd
True
'''





# Find  outputs  (Home  work)
a = 'Hyd'
b = True
c = 25
d = 1
e = 'Hyd'
s = {a , b , c , d , e}
print(s)
print(len(s))
print(type(s))
'''
OUTPUT:
{True, 'Hyd', 25}
3
<class 'set'>
'''





# Find  outputs  (Home  work)
s = {'Hyd',  25,  True,  10.8 }
print(s)
a , b , c , d = s
print(a)
print(b)
print(c)
print(d)
'''
OUTPUT:
{25, 10.8, True, 'Hyd'}
25
10.8
True
Hyd
'''
print()




# Find  outputs  (Home  work)
s = {'Hyd',  25,  True,  10.8 }
print(s)
a , *b = s
print(a)
print(b)
print(type(b))
'''
OUTPUT:
{25, 10.8, 'Hyd', True}
25
[10.8, 'Hyd', True]
<class 'list'>
'''



# Find  outputs  (Home  work)
s = {'Hyd',  25,  True,  10.8 }
print(s)
a , *b , c = s
print(a)
print(b)
print(c)
'''
OUTPUT:
25
[10.8, True]
Hyd
'''




# Find  outputs  (Home  work)
s = {20 , 10 , 20 , 10}
print(s)
x , y = s
print(x)
print(y)
'''
OUTPUT:
10
20
'''
print()



# set()  function  demo  program  (Home  work)
a = range(100 , 151 , 10)
b = set(a)
print(b)
c = [10 , 20 , 15 , 18 , 10 , 50 , 20 , 12 , 18]
d = set(c)
print(d)
e = set('Rama  rAo')
print(e)
#print(set(25))
print(set())
'''
OUTPUT:

{130, 100, 140, 110, 150, 120}
{10, 12, 15, 18, 50, 20}
{'o', 'm', 'A', 'R', 'a', 'r', ' '}
set()
'''



