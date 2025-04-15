#1 Find  outputs   (Home  work)
a = 25 , 10.8 , 3 + 4j , 'Hyd' , True , None , 'Hyd' , 25
print(a)
print(type(a))
#a[3] = 'Sec'
#a[3 : 6] = 60 , 70 , 80

Output:
(25, 10.8, (3+4j), 'Hyd', True, None, 'Hyd', 25)
<class 'tuple'>

#2 What   are  the  outputs  if  input  is  (10 , 20 , 30 , 40) ?   (Home  work)
a = input('Enter  Tuple  :  ')
print(a)
print(type(a))
b = eval(a)
print(b)
print(type(b))
print(len(b))

Output:
Enter  Tuple  :  (10 , 20 , 30 , 40)
(10 , 20 , 30 , 40)
<class 'str'>
(10, 20, 30, 40)
<class 'tuple'>
4

#3 Find  outputs  (Home  work)
a = (10 , [20 , 30 , 40] , 50 , 60)
a[1][0] = 70
print(a)
#a[1] = [80 , 90 , 100]
print(a)

Output:
(10, [70, 30, 40], 50, 60)
(10, [70, 30, 40], 50, 60)

#4 Find  outputs  (Home  work)
a = [10 , (20 , 30 , 40) , 50 , 60]
#a[1][0] = 70
print(a)
a[1] = [80 , 90]
print(a)

Output:
[10, (20, 30, 40), 50, 60]
[10, [80, 90], 50, 60]

#5 Find  outputs   (Home  work)
a = 25
b = 10.8
c = 'Hyd'
d = True
x = a , b , c , d
print(x)
print(type(x))

Output:
(25, 10.8, 'Hyd', True)
<class 'tuple'>

#6 Find  outputs   (Home  work)
x = 25 , 10.8 , 'Hyd' , True
a , b , c , d = x
print(a)
print(b)
print(c)
print(d)
#p , q , r =  x
#a , b , c , d  , e = x

Output:
25
10.8
Hyd
True

#6 Find  outputs   (Home  work)
x = 25 , 10.8 , 'Hyd' , True
a , *b , c = x
print(a)
print(b)
print(c)

Output:
25
[10.8, 'Hyd']
True

#7 Find  outputs   (Home  work)
tpl = 25 , 10.8 , 'Hyd' , True
a , b , *c , d , e = tpl
print(a)
print(b)
print(c)
print(d)
print(e)

Output:
25
10.8
[]
Hyd
True

#8 Find  outputs   (Home  work)
x = 25 , 10.8 , 'Hyd' , True , 3 + 4j
a , b , _ , d , _= x
print(a)
print(b)
print(_)
print(d)
print(_)

Output:
25
10.8
(3+4j)
True
(3+4j)

#9 tuple()  function  demo  program   (Home  work)
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

Output:
(100, 110, 120, 130, 140)
<class 'tuple'>
(10, 20, 15, 18)
('V', 'a', 'm', 's', 'i')
()

#10 index()  and  count()  methods  demo  program   (Home  work)
a = (10 , 20 , 15 , 12 , 14 , 15 , 18 , 19 , 15 , 12 , 25)
#     0    1      2     3    4     5     6    7     8    9    10
try:
	i = a . index(15)
	while  True:
		print('15 is found at index : ' , i)
		i = a . index(15 , i + 1)
except:
		print(F'15  is  found  {a . count(15)}  times')

Output:
15 is found at index :  2
15 is found at index :  5
15 is found at index :  8
15  is  found  3  times

#11 How  to  modify  an  element  of  tuple ?    (Home  work)
a  =  10 ,  20 ,  30 ,   40 ,  50
#     0      1       2       3      4
#a[2] = 35
print(a)
print(id(a))
#How  to  modify  30  in  tuple  to  35
print(a)
print(id(a))

Output:
(10, 20, 30, 40, 50)
2732449428352
(10, 20, 30, 40, 50)
2732449428352

#12 How  to  delete  an  element  of  tuple ?   (Home  work)
a  = 10 , 20 , 30 , 40 , 50
#    0     1      2     3      4
#a . remove(30)
#del  a[2]
#a . pop(2)
print(a)
print(id(a))
#How  to  remove  30  from  tuple  'a'
print(a)
print(id(a))

Output:
(10, 20, 30, 40, 50)
2464817574784
(10, 20, 30, 40, 50)
2464817574784

#13 Nested   tuple  (Home  work)
a = ( (10 , 20)  ,  (30 , 40 , 50)  ,  (60 , 70 , 80 , 90) )
print(a)
print(type(a))
print(len(a))
print(a[0])
print(a[1])
print(a[2])
print(a[0][1])
print(a[1][2])
print(a[2][3])

Output:
((10, 20), (30, 40, 50), (60, 70, 80, 90))
<class 'tuple'>
3
(10, 20)
(30, 40, 50)
(60, 70, 80, 90)
20
50
90

#14 Find  outputs  (Home  work)
a = ((10 , 20 , 30),)
(c,)=a
print(a[0])
print(c)
print(a[0][0])
print(a[0][1])
print(a[0][2])
b = ((),)
print(b[0])
(d,)=b
print(c)

Output:
(10, 20, 30)
(10, 20, 30)
10
20
30
()
()

#15 Find  outputs (Home  work)
a = ((10 , 20 , 30))
print(a)
print(*a)
b = (())
print(b)
print(*b)

Output:
(10, 20, 30)
10 20 30
()

#16 What  are  the  outputs  if  input  is  
a = input('Enter  Set  :  ')
print(a)
print(type(a))
b = eval(a)
print(b)
print(type(b))

Output:
Enter  Set  :  {10 , 20 , 15 , 18 , 20 , 12 , 18}
{10 , 20 , 15 , 18 , 20 , 12 , 18}
<class 'str'>
{18, 20, 10, 12, 15}
<class 'set'>

#17 Find  outputs  (Home  work)
print({(10 , 20 , 30)})
#print({[10 , 20 , 30]})
#print({{10 , 20 , 30}})
#print({{}})

Output:
{(10, 20, 30)}

#18 How  to  print  set  in  differnet ways  (Home  work)
a = {25 , True , 'Hyd' , 10.8}
print(a)
for x in a:
	print(x)

Output:
{25, 10.8, True, 'Hyd'}
25
10.8
True
Hyd

#19 Find  outputs  (Home  work)
a = 'Hyd'
b = True
c = 25
d = 1
e = 'Hyd'
s = {a , b , c , d , e}
print(s)
print(len(s))
print(type(s))

Output:
{True, 'Hyd', 25}
3
<class 'set'>

#20 Find  outputs  (Home  work)
s = {'Hyd',  25,  True,  10.8 }
print(s)
a , b , c , d = s
print(a)
print(b)
print(c)
print(d)

Output:
{25, 10.8, 'Hyd', True}
25
10.8
Hyd
True

#21 Find  outputs  (Home  work)
s = {'Hyd',  25,  True,  10.8 }
print(s)
a , *b = s
print(a)
print(b)
print(type(b))

Output:
{25, 'Hyd', 10.8, True}
25
['Hyd', 10.8, True]
<class 'list'>

#22 Find  outputs  (Home  work)
s = {'Hyd',  25,  True,  10.8 }
print(s)
a , *b , c = s
print(a)
print(b)
print(c)

Output:
{'Hyd', 10.8, 25, True}
Hyd
[10.8, 25]
True

#23 Find  outputs  (Home  work)
s = {20 , 10 , 20 , 10}
print(s)
x , y = s
print(x)
print(y)

Output:
{10, 20}
10
20

#24 set()  function  demo  program  (Home  work)
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

Output:
{130, 100, 140, 110, 150, 120}
{10, 12, 15, 18, 50, 20}
{' ', 'A', 'r', 'm', 'o', 'R', 'a'}
set()

#25 add()  method  demo  program  (Home  work)
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
print(a)
a . add((10 , 20 , 30))
#a . add([10,20,30])
print(a)

Output:
{True, 10.8, 'Hyd', 25, None}
{True, 10.8, (10, 20, 30), 'Hyd', 25, None}

#26 Find  outputs  (Home  work)
a = {25 , 10.8 , 'Hyd' , True}
tpl = (10 , 20 , 30)
print(a)
print(id(a))
a . add(tpl)
a . add('Sec')
print(a)
print(id(a))
print(len(a))
#a . add([100 , 200 , 300])
#a . add(set())
#a . add({ })

Output:
{25, 10.8, 'Hyd', True}
1657214839360
{True, 10.8, (10, 20, 30), 'Sec', 'Hyd', 25}
1657214839360
6

#27  Find  outputs (Home  work)
s = set()
tpl = (10 , 20 , 15 , 18)
s . add(tpl)
print(s)
print(len(s))

Output:
{(10, 20, 15, 18)}
1

#28 update()  method  demo program  (Home  work)
tpl = (10 , 20 , 15, 18 , 10 , 20)
s = set()
s . update(tpl)
print(len(s))
print(s)
#s . update(25)

Output:
4
{10, 18, 20, 15}

#29 Find  outputs  (Home  work)
a = [10 , 20 , 30]
b = {30 , 40,50 }
c = (50 , 60 , 70)
s = set()
s . update(a,b,c)
print(s)
print(len(s))
#s . add(a , b , c)

Output:
{50, 20, 70, 40, 10, 60, 30}
7

#29 Find  outputs  (Home  work)
a = set()
a . update('Rama Rao')
print(a)
print(len(a))
#a . update(3 + 4j , 10.8 , True)

Output:
{'a', ' ', 'o', 'R', 'm'}
5

#30 copy()  method  demo  program  (Home  work)
a = {10 , 20 , 15 , 18}
print(a)
b = a . copy()
print(b)
print(a  is  b)
print(a  ==  b)
c = a
print(a  is  c)

Output:
{10, 18, 20, 15}
{10, 18, 20, 15}
False
True
True

#31 remove()  method  demo  program  (Home  work)
a = {25 , 10.8 , 'Hyd' , True}
print(a)
a . remove('Hyd')
print(a)
#a . remove('Sec')

Output:
{25, 10.8, 'Hyd', True}
{25, 10.8, True}

#32 discard()  method  demo  program (Home  work)
a = {25 , 10.8 , 'Hyd' , True}
print(a)
a . discard('Hyd')
print(a)
a . discard('Sec')
print(a)
#a . remove('Sec')

Output:
{25, 10.8, 'Hyd', True}
{25, 10.8, True}
{25, 10.8, True}

#33 clear()  method  demo  program (Home  work)
a = {10 , 20 , 15 , 18}
print(a)
a . clear()
print(a)
print(len(a))

Output:
{10, 18, 20, 15}
set()
0

#34 Find  outputs  (Home work)
a = {10 , 20 , 30 , 40}
b = [30 , 40 , 50 , 60]
print(a . union(b))
#print(a | b)
#print(b . union(a))
#print(a + b)

Output:
{40, 10, 50, 20, 60, 30}