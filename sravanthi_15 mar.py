.......1
a = 25 , 10.8 , 3 + 4j , 'Hyd' , True , None , 'Hyd' , 25
print(a)
print(type(a))
a[3] = 'Sec'
a[3 : 6] = 60 , 70 , 80
output:
(25, 10.8, (3+4j), 'Hyd', True, None, 'Hyd', 25)
<class 'tuple'>
........2
a = input('Enter  Tuple  :  ')
print(a)
print(type(a))
b = eval(a)
print(b)
print(type(b))
print(len(b))
output:
Enter  Tuple  :  (20,30,40)
(20,30,40)
<class 'str'>
(20, 30, 40)
<class 'tuple'>
3
.............3
a = (10 , [20 , 30 , 40] , 50 , 60)
a[1][0] = 70
print(a)
#a[1] = [80 , 90 , 100]
print(a)
output:
(10, [70, 30, 40], 50, 60)
(10, [70, 30, 40], 50, 60)
.................4
a = [10 , (20 , 30 , 40) , 50 , 60]
#a[1][0] = 70
print(a)
a[1] = [80 , 90]
print(a)
output:
[10, (20, 30, 40), 50, 60]
[10, [80, 90], 50, 60]
..........5
a = 25
b = 10.8
c = 'Hyd'
d = True
x = a , b , c , d
print(x)
print(type(x))
output:
(25, 10.8, 'Hyd', True)
<class 'tuple'>
................6
x = 25 , 10.8 , 'Hyd' , True
a , b , c , d = x
print(a)
print(b)
print(c)
print(d)
#p , q , r =  x
#a , b , c , d  , e = x
output:
25
10.8
Hyd
True
............7
x = 25 , 10.8 , 'Hyd' , True
a , *b , c = x
print(a)
print(b)
print(c)
output:
25
[10.8, 'Hyd']
True
........8
tpl = 25 , 10.8 , 'Hyd' , True
a , b , *c , d , e = tpl
print(a)
print(b)
print(c)
print(d)
print(e)
output:
25
10.8
[]
Hyd
True
.......9
x = 25 , 10.8 , 'Hyd' , True , 3 + 4j
a , b , _ , d , _= x
print(a)
print(b)
print(_)
print(d)
print(_)
output:
25
10.8
(3+4j)
True
(3+4j)
.........10
a = range(100 , 150 , 10)
b = tuple(a)
print(b)
print(type(b))
c = [10 , 20 , 15, 18]
d = tuple(c)
print(d)
e = tuple('Vamsi')
print(e)
print(tuple(25))
print(tuple())
output:
(100, 110, 120, 130, 140)
<class 'tuple'>
(10, 20, 15, 18)
('V', 'a', 'm', 's', 'i')
()
..........11
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
output:
15 is found at index :  2
15 is found at index :  5
15 is found at index :  8
15  is  found  3  times
.........12
#  Nested   tuple  (Home  work)
a = ( (10 , 20)  ,  (30 , 40 , 50)  ,  (60 , 70 , 80 , 90) )
print(a)
print(type(a))
print(len(a))
print(How  to  print  1st  inner  tuple)#print(a[0])
print(How  to  print  2nd  inner  tuple)#print(a[1])
print(How  to  print  3rd  inner  tuple)#print(a[2])
print(How  to  print  20)#print(a[0][1])
print(How  to  print  50)#print(a[1][2])
print(How  to  print  90#print(a[2][3])
output:
((10, 20), (30, 40, 50), (60, 70, 80, 90))
<class 'tuple'>
3
(10, 20)
(30, 40, 50)
(60, 70, 80, 90)
20
50
90
...........13
a = ((10 , 20 , 30),)
print(How  to   print  inner  tuple)
print(How  to   print  inner  tuple  in  another  way)
print(How   to  print   10)
print(How   to  print   20)
print(How   to  print   30)
b = ((),)
print(How  to   print  inner  tuple  of  tuple  'b')
print(How  to   print  inner  tuple  of  tuple  'b'  in  another  way)
a = ((10 , 20 , 30),)
print(a[0])
print(*a)
print(a[0][0])
print(a[0][1])
print(a[0][2])
b = ((),)
print(b[0])
print(*b)
output:
(10, 20, 30)
(10, 20, 30)
10
20
30
()
()
.............14
a = ((10 , 20 , 30))
print(a)
print(*a)
b = (())
print(b)
print(*b)
output:
(10, 20, 30)
10 20 30
()
........15
a = input('Enter  Set  :  ')
print(a)
print(type(a))
b = eval(a)
print(b)
print(type(b))
Enter  Set  :  (10,20,30,40)
(10,20,30,40)
<class 'str'>
(10, 20, 30, 40)
<class 'tuple'>
.........16
print({(10 , 20 , 30)})
print({[10 , 20 , 30]})
print({{10 , 20 , 30}})
print({{}})
output:
{(10, 20, 30)}
.........17
a = 'Hyd'
b = True
c = 25
d = 1
e = 'Hyd'
s = {a , b , c , d , e}
print(s)
print(len(s))
print(type(s))
output:
{True, 'Hyd', 25}
3
<class 'set'>
........18
s = {'Hyd',  25,  True,  10.8 }
print(s)
a , b , c , d = s
print(a)
print(b)
print(c)
print(d)
output:
{25, 10.8, True, 'Hyd'}
25
10.8
True
Hyd
.......19
s = {'Hyd',  25,  True,  10.8 }
print(s)
a , *b = s
print(a)
print(b)
print(type(b))
output:
{25, 10.8, 'Hyd', True}
25
[10.8, 'Hyd', True]
<class 'list'>
.........20
s = {'Hyd',  25,  True,  10.8 }
print(s)
a , *b , c = s
print(a)
print(b)
print(c)
output:
{25, 10.8, True, 'Hyd'}
25
[10.8, True]
Hyd
.........21
s = {20 , 10 , 20 , 10}
print(s)
x , y = s
print(x)
print(y)
output;
{10, 20}
10
20
.......22
a = range(100 , 151 , 10)
b = set(a)
print(b)
c = [10 , 20 , 15 , 18 , 10 , 50 , 20 , 12 , 18]
d = set(c)
print(d)
e = set('Rama  rAo')
print(e)
print(set(25))
print(set())
output:
{130, 100, 140, 110, 150, 120}
{10, 12, 15, 18, 50, 20}
{'a', ' ', 'A', 'o', 'm', 'r', 'R'}
set()
.......23
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
print(a)
a . add(10 , 20 , 30)
a . add([10,20,30])
output:
{None, True, 'Hyd', 10.8, 25}
.......24
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
output:
{25, 10.8, 'Hyd', True}
3086899741408
{True, 'Sec', 10.8, 'Hyd', (10, 20, 30), 25}
3086899741408
6
.......25
s = set()
tpl = (10 , 20 , 15 , 18)
s . add(tpl)
print(s)
print(len(s))
output:
{(10, 20, 15, 18)}
1
......26
# update()  method  demo program  (Home  work)
tpl = (10 , 20 , 15, 18 , 10 , 20)
s = set()
s . update(tpl)
print(len(s))
print(s)
s . update(25)
output:
4
{10, 18, 20, 15}
........27
a = [10 , 20 , 30]
b = {30 , 40,50 }
c = (50 , 60 , 70)
s = set()
s . update(a , b , c)
print(s)
print(len(s))
s . add(a , b , c)
output:
{50, 20, 70, 40, 10, 60, 30}
7

