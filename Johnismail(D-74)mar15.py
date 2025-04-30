'''# Find  outputs   (Home  work)
a = 25 , 10.8 , 3 + 4j , 'Hyd' , True , None , 'Hyd' , 25
print(a)#(25 , 10.8 , 3 + 4j , 'Hyd' , True , None , 'Hyd' , 25)
print(type(a))#<class 'tuple'>
#a[3] = 'Sec'#error
#a[3 : 6] = 60 , 70 , 80#error

#  What   are  the  outputs  if  input  is  (10 , 20 , 30 , 40) ?   (Home  work)
a = input('Enter  Tuple  :  ')#(1,2,3)
print(a)#(1,2,3)
print(type(a))#<class 'str'>
b = eval(a)#
print(b)#(1,2,3)
print(type(b))#<class 'tuple'>
print(len(b))#3

# Find  outputs  (Home  work)
a = (10 , [20 , 30 , 40] , 50 , 60)
a[1][0] = 70
print(a)#(10 , [70 , 30 , 40] , 50 , 60)
#a[1] = [80 , 90 , 100]#error
print(a)#(10 , [70 , 30 , 40] , 50 , 60)


# Find  outputs  (Home  work)
a = [10 , (20 , 30 , 40) , 50 , 60]
a[1][0] = 70 #error
print(a)[10 , (20 , 30 , 40) , 50 , 60]
a[1] = [80 , 90]
print(a)#[10 , [80, 90] , 50 , 60]

# Find  outputs   (Home  work)
a = 25
b = 10.8
c = 'Hyd'
d = True
x = a , b , c , d
print(x)#(25,10.8,'Hyd',True)
print(type(x))#<class tuple>

# Find  outputs   (Home  work)
x = 25 , 10.8 , 'Hyd' , True
a , b , c , d = x
print(a)#( 25)
print(b)# (10.8)
print(c)#('Hyd')
print(d)#(True)
#p , q , r =  x -error due to less values to unpack
#a , b , c , d  , e = x-error

# Find  outputs   (Home  work)
x = 25 , 10.8 , 'Hyd' , True
a , *b , c = x
print(a)#(25)
print(b)#(10.8,'Hyd')
print(c)#(True)

# Find  outputs   (Home  work)
tpl = 25 , 10.8 , 'Hyd' , True
a , b , *c , d , e = tpl
print(a)#(25)
print(b)#(10.8)
print(c)#[]
print(d)#('Hyd')
print(e)#(True)

# Find  outputs   (Home  work)
x = 25 , 10.8 , 'Hyd' , True , 3 + 4j
a , b , _ , d , _ = x
print(a)#(25)
print(b)#(10.8)
print(_)#(3+4j)
print(d)#(True)
print(_)#(3+4j)

# tuple()  function  demo  program   (Home  work)
a = range(100 , 150 , 10)
b = tuple(a)
print(b)#(100,110,120,130,140)
print(type(b))#class <tuple>
c = [10 , 20 , 15, 18]
d = tuple(c)
print(d)#(10,20,15,18)
e = tuple('Vamsi')
print(e)#('v','a','m','s','i')
#print(tuple(25))#error becoz argument should be sequence
print(tuple())#()

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

15 is found at index :  2
15 is found at index :  5
15 is found at index :  8
15  is  found  3  times

#  How  to  modify  an  element  of  tuple ?    (Home  work)
a  =  10 ,  20 ,  30 ,   40 ,  50
#     0      1       2       3      4
#a[2] = 35#error becoz tuple is immutable
#print(a)#(10 ,  20 ,  30 ,   40 ,  50)
#print(id(a))#random adress
#How  to  modify  30  in  tuple  to  35
a=list(a)
a[2]=35
a=tuple(a)
print(a)#(10,20,35,40,50)
print(id(a))# (diiferent address of tuple a)

# How  to  delete  an  element  of  tuple ?   (Home  work)
a  = 10 , 20 , 30 , 40 , 50
#    0     1      2     3      4
#a . remove(30) error
#del  a[2]
#a . pop(2)
print(a)# (10 , 20 , 30 , 40 , 50)
print(id(a))#(random address of tuple a)
#How  to  remove  30  from  tuple  'a'
a=list(a)
a.remove(30)
a=tuple(a)
print(a)#( 10 , 20 , 40 , 50)
print(id(a))#( different random address of tuple a)

#  Nested   tuple  (Home  work)
a = ( (10 , 20)  ,  (30 , 40 , 50)  ,  (60 , 70 , 80 , 90) )
print(a)#( (10 , 20)  ,  (30 , 40 , 50)  ,  (60 , 70 , 80 , 90) )
print(type(a))# class <tuple>
print(len(a))#3
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

#  Find  outputs (Home  work)
a = ((10 , 20 , 30))
print(a)#((10 , 20 , 30))
print(*a)#10 , 20 , 30
b = (())
print(b)#(())
print(*b)#empty

# What  are  the  outputs  if  input  is  {10 , 20 , 15 , 18 , 20 , 12 , 18}
a = input('Enter  Set  :  ')
print(a)#{'10' , '20' , '15' , '18' , '20' , '12' , '18'}
print(type(a))#<class 'str'>
b = eval(a)
print(b)#{10,20,15,18,12}
print(type(b))#<class 'set'>

# Find  outputs  (Home  work)
print({(10 , 20 , 30)})
#print({[10 , 20 , 30]})
#print({{10 , 20 , 30}})
print({{}})

# How  to  print  set  in  differnet ways  (Home  work)
a = {25 , True , 'Hyd' , 10.8}
#print('set  with  print  function')
print(a)
#print('Iterate  elements  of  set  with  for  loop')
#How  to  iterate  set  with  for  loop
for i in a:
		print(i)
	
# Find  outputs  (Home  work)
a = 'Hyd'
b = True
c = 25
d = 1
e = 'Hyd'
s = {a , b , c , d , e}
print(s)#{'Hyd',1,25}
print(len(s))#3
print(type(s))#<class set>

# Find  outputs  (Home  work)
s = {'Hyd',  25,  True,  10.8 }
print(s)#{'Hyd',  25,  True,  10.8 }
a , b , c , d = s
print(a)#'Hyd'
print(b)#25
print(c)#True
print(d)#10.8

# Find  outputs  (Home  work)
s = {'Hyd',  25,  True,  10.8 }
print(s)#{'Hyd',  25,  True,  10.8 }
a , *b = s
print(a)#{'hyd'}
print(b)#[25,  True,  10.8]
print(type(b))#class 'list'>

# Find  outputs  (Home  work)
s = {'Hyd',  25,  True,  10.8 }
print(s)#{'Hyd',  25,  True,  10.8 }
a , *b , c = s
print(a)#{'Hyd'}
print(b)#[25,  True,]
print(c)#{10.8}

# Find  outputs  (Home  work)
s = {20 , 10 , 20 , 10}
print(s)#{10,20}
x , y = s
print(x)#{10}
print(y)#{20}

# set()  function  demo  program  (Home  work)
a = range(100 , 151 , 10)
b = set(a)#
print(b)#{100,110,120,130,140,150}
c = [10 , 20 , 15 , 18 , 10 , 50 , 20 , 12 , 18]
d = set(c)
print(d)#{10,20,15,18,50,12}
e = set('Rama  rAo')
print(e)#{'R','a','m',' ',r,'A','o'}
#print(set(25))#error argument should be sequence
print(set())#set()

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
print(a)#{True,25,10.8,'Hyd',None}
#a . add(10 , 20 , 30)#error
#a . add([10,20,30])#error

# Find  outputs  (Home  work)
a = {25 , 10.8 , 'Hyd' , True}
tpl = (10 , 20 , 30)
print(a)#{25 , 10.8 , 'Hyd' , True}
print(id(a))#some random adress
a . add(tpl)#
a . add('Sec')#
print(a)#{25 , 10.8 , 'Hyd' , True,(10,20,30),'sec'}
print(id(a))#same adress of a
print(len(a))#6
#a . add([100 , 200 , 300])#error
#a . add(set())
#a . add({ })

# Find  outputs (Home  work)
s = set()
tpl = (10 , 20 , 15 , 18)
s . add(tpl)
print(s)#{(10,20,15,18)}
print(len(s))#1

# update()  method  demo program  (Home  work)
tpl = (10 , 20 , 15, 18 , 10 , 20)
s = set()
s . update(tpl)
print(len(s))#4
print(s)#{10,20,15,18}
#s . update(25)#error argument should be sequence

# Find  outputs  (Home  work)
a = [10 , 20 , 30]
b = {30 , 40,50 }
c = (50 , 60 , 70)
s = set()
s . update(a , b , c)
print(s)#{10,20,30,40,50,60,70}
print(len(s))#7
#s . add(a , b , c)#error add method can take only single argument only

# Find  outputs  (Home  work)
a = set()
a . update('Rama Rao')
print(a)#{'R','a','m',' ','o'}
print(len(a))#5
#a . update(3 + 4j , 10.8 , True)#update arguments should be sequence only

# copy()  method  demo  program  (Home  work)
a = {10 , 20 , 15 , 18}
print(a)#{10 , 20 , 15 , 18}
b = a . copy()
print(b)#{10 , 20 , 15 , 18}
print(a  is  b)#False
print(a  ==  b)#True
c = a #
print(a  is  c)#True

# remove()  method  demo  program  (Home  work)
a = {25 , 10.8 , 'Hyd' , True}
print(a)#{25 , 10.8 , 'Hyd' , True}
a . remove('Hyd')
print(a)#{25 , 10.8 , True}
#a . remove('Sec')#error

# discard()  method  demo  program (Home  work)
a = {25 , 10.8 , 'Hyd' , True}
print(a)#{25 , 10.8 , 'Hyd' , True}
a . discard('Hyd')
print(a)#{25 , 10.8 , True}
a . discard('Sec')
print(a)#25 , 10.8 , 'Hyd' , True}
#a . remove('Sec')#error

# clear()  method  demo  program (Home  work)
a = {10 , 20 , 15 , 18}
print(a)#{10 , 20 , 15 , 18}
a . clear()
print(a)#set()
print(len(a))#0'''

# Find  outputs  (Home work)
a = {10 , 20 , 30 , 40}
b = [30 , 40 , 50 , 60]
print(a . union(b))#{10 , 20 , 30 , 40, 50, 60}
#print(a | b)#error
#print(b . union(a))#error
#print(a + b)#error


