#1
# Find  outputs   (Home  work)
a = 25 , 10.8 , 3 + 4j , 'Hyd' , True , None , 'Hyd' , 25
print(a)
print(type(a))
#a[3] = 'Sec'#tuple doesnot support the assignments
#a[3 : 6] = 60 , 70 , 80 'Sec' #tuple doesnot support the assignments

#2
#  What   are  the  outputs  if  input  is  (10 , 20 , 30 , 40) ?   (Home  work)
a = input('Enter  Tuple  :  ')#10,20,True,10.8
print(a)#10,20,True,10.8
print(type(a))#str
b = eval(a)
print(b)#(10, 20, True, 10.8)
print(type(b))#<class 'tuple'>
print(len(b))#4

#3
# Find  outputs  (Home  work)
a = (10 , [20 , 30 , 40] , 50 , 60)
a[1][0] = 70#(10, [70, 30, 40], 50, 60)
print(a)#(10, [70, 30, 40], 50, 60)
#a[1] = [80 , 90 , 100] #error
print(a)#(10, [70, 30, 40], 50, 60)

#4
# Find  outputs  (Home  work)
a = [10 , (20 , 30 , 40) , 50 , 60]
#a[1][0] = 70#error
print(a)#[10 , (20 , 30 , 40) , 50 , 60]
a[1] = [80 , 90]
print(a)#[10, [80, 90], 50, 60]

#5
a = 25
b = 10.8
c = 'Hyd'
d = True
x = a , b , c , d
print(x)#(25, 10.8, 'Hyd', True)
print(type(x))#<class 'tuple'>

#6
# Find  outputs   (Home  work)
x = 25 , 10.8 , 'Hyd' , True
a , b , c , d = x
print(a)#25
print(b)#10.8
print(c)#hyd
print(d)#True
p , q , r =  x
print(x)
#a , b , c , d  , e = x#error

#7
# Find  outputs   (Home  work)
x = 25 , 10.8 , 'Hyd' , True
a , *b , c = x
print(a)#25
print(b)#10.8,hyd
print(c)#True

#8
# Find  outputs   (Home  work)
tpl = 25 , 10.8 , 'Hyd' , True
print(tpl)
a , b , *c , d , e = tpl
print(a)#25
print(b)#10.8
print(c)#[]
print(d)#hyd
print(e)#True

#9
x = 25 , 10.8 , 'Hyd' , True , 3 + 4j
a , b , _ , d , _= x
print(a)#25
print(b)#10.8
print(_)#3+4j
print(d)#True
print(_)#3+4j

#10
# tuple()  function  demo  program   (Home  work)
a = range(100 , 150 , 10)
b = tuple(a)
print(b)#(100, 110, 120, 130, 140)
print(type(b))#<class 'tuple'>
c = [10 , 20 , 15, 18]
d = tuple(c)
print(d)#(10, 20, 15, 18)
e = tuple('Vamsi')#
print(e)#('V', 'a', 'm', 's', 'i')
#print(tuple(25))
print(tuple())#()

#11
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
15  is  found  3  times
'''

#12
a  =  10 ,  20 ,  30 ,   40 ,  50
#     0      1       2       3      4
#a[2] = 35#error
print(a)
print(id(a))
c=list(a)
c[2]=35
#How  to  modify  30  in  tuple  to  35
print(tuple(c))
print(id(c))

#13
# How  to  delete  an  element  of  tuple ?   (Home  work)
a  = 10 , 20 , 30 , 40 , 50
#    0     1      2     3      4
#a . remove(30)
#del  a[2]
#a . pop(2)
print(a)
print(id(a))
#How  to  remove  30  from  tuple  'a'
v=list(a)
v.pop(2)
print(tuple(v))
print(id(v))

#14
#  Nested   tuple  (Home  work)
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

#15
# Find  outputs  (Home  work)
a = ((10 , 20 , 30),)
print(a[0])
print(*a)
print(a[0][0])
print(a[0][1])
print(a[0][2])
b = ((),)
print(b[0])
#print(b[1])#error

#16
a = ((10 , 20 , 30))
print(a)#((10 , 20 , 30))
print(*a)#10 , 20 , 30
b = (())
print(b)#()
print(*b)
print("a")

#17
# What  are  the  outputs  if  input  is  {10 , 20 , 15 , 18 , 20 , 12 , 18}
a = input('Enter  Set  :  ')#
print(a)#10,10,20,30,40
print(type(a))#str
b = eval(a)
print(b)#(10, 10, 20, 30, 40)
print(type(b))#<class 'tuple'>

#18
#  Find  outputs  (Home  work)
print({(10 , 20 , 30)})#{(10 , 20 , 30)}
#print({[10 , 20 , 30]})#error
#print({{10 , 20 , 30}})#unhashable type: 'set'
#print({{}})#unhashable type: 'set'

#19
# How  to  print  set  in  differnet ways  (Home  work)
a = {25 , True , 'Hyd' , 10.8}
print('set  with  print  function')
print(a)
print('Iterate  elements  of  set  with  for  loop')
for i in a:
    print(i)

#20
# Find  outputs  (Home  work)
a = 'Hyd'
b = True
c = 25
d = 1
e = 'Hyd'
s = {a , b , c , d , e}
print(s)
print(len(s))#3
print(type(s))#<class 'set'>

#21
# Find  outputs  (Home  work)
s = {'Hyd',  25,  True,  10.8 }
print(s)
a , b , c , d = s
print(a)#hyd
print(b)#25
print(c)#True
print(d)#10.8

#22
# Find  outputs  (Home  work)
s = {'Hyd',  25,  True,  10.8}
print(s)#{'Hyd',  25,  True,  10.8 }
a , *b = s
print(a)#'Hyd'
print(b)#
print(type(b))

#23
# Find  outputs  (Home  work)
s = {'Hyd',  25,  True,  10.8 }
print(s)#{'Hyd',  25,  True,  10.8 }
a , *b , c = s
print(a)#hud
print(b)#[25,True}
print(c)#10.8

#24
# Find  outputs  (Home  work)
s = {20 , 10 , 20 , 10}
print(s)#{20 , 10 , 20 , 10}
x , y = s
print(x)#20
print(y)#10

#25
# set()  function  demo  program  (Home  work)
a = range(100 , 151 , 10)
b = set(a)
print(b)#{130, 100, 140, 110, 150, 120}
c = [10 , 20 , 15 , 18 , 10 , 50 , 20 , 12 , 18]
d = set(c)
print(d)#{10, 12, 15, 18, 50, 20}
e = set('Rama  rAo')
print(e)#{'a', 'A', 'm', ' ', 'o', 'R', 'r'}
#print(set(25))#error
print(set())#set()

#26
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
print(a)#{TRue,25,10.8,'hyd',None}
#a . add(10 , 20 , 30)#error onlu one argument
#a . add([10,20,30])#error onlu one argument

#27
# Find  outputs  (Home  work)
a = {25 , 10.8 , 'Hyd' , True}
tpl = (10 , 20 , 30)
print(a)#{25 , 10.8 , 'Hyd' , True}
print(id(a))#address
a . add(tpl)
a . add('Sec')
print(a)#{True, 'Hyd', 10.8, 'Sec', (10, 20, 30), 25}
print(id(a))#address
print(len(a))#6
#a . add([100 , 200 , 300])#error
#a . add(set())#error
#a . add({ })#error


#28
# Find  outputs (Home  work)
s = set()
tpl = (10 , 20 , 15 , 18)
s . add(tpl)
print(s)#{(10, 20, 15, 18)}
print(len(s))#1

#29
# update()  method  demo program  (Home  work)
tpl = (10 , 20 , 15, 18 , 10 , 20)
s = set()
s . update(tpl)
print(len(s))#4
print(s)#
#s . update(25)

#30
# Find  outputs  (Home  work)
a = [10 , 20 , 30]
b = {30 , 40,50 }
c = (50 , 60 , 70)
s = set()
s . update(a , b , c)
print(s)#{50, 20, 70, 40, 10, 60, 30}
print(len(s))#7
#s . add(a , b , c)#error

#31
# Find  outputs  (Home  work)
a = set()
a . update('Rama Rao')
print(a)#{' ', 'a', 'o', 'R', 'm'}
print(len(a))#5
#a . update(3 + 4j , 10.8 , True)#error

#32
# copy()  method  demo  program  (Home  work)
a = {10 , 20 , 15 , 18}
print(a)
b = a . copy()
print(b)#{10 , 20 , 15 , 18}
print(a  is  b)#false
print(a  ==  b)#True
c = a
print(a  is  c)#True

#33
# remove()  method  demo  program  (Home  work)
a = {25 , 10.8 , 'Hyd' , True}
print(a)
a . remove('Hyd')
print(a)
#a . remove('Sec')#error

#34
# discard()  method  demo  program (Home  work)
a = {25 , 10.8 , 'Hyd' , True}
print(a)#{25, 10.8, 'Hyd', True}
a . discard('Hyd')
print(a)#{25, 10.8, True}
a . discard('Sec')#
print(a)
#a . remove('Sec')error

#35
# clear()  method  demo  program (Home  work)
a = {10 , 20 , 15 , 18}
print(a)#{10 , 20 , 15 , 18}
a . clear()
print(a)#set()
print(len(a))#0

#36
# Find  outputs  (Home work)
a = {10 , 20 , 30 , 40}
b = [30 , 40 , 50 , 60]
print(a . union(b))#{40, 10, 50, 20, 60, 30}
#print(a | b)#unsupported operand b/w set and list
#print(b . union(a))#error
#print(a + b)#error