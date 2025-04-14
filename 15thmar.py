"""
 # Find  outputs   (Homework)
a = 25 , 10.8 , 3 + 4j , 'Hyd' , True , None , 'Hyd' , 25
print(a) #(25 , 10.8 , 3 + 4j , 'Hyd' , True , None , 'Hyd' , 25)
print(type(a))#class tuple
#a[3] = 'Sec'#error
#a[3 : 6] = 60 , 70 , 80 #error


 #  What   are  the  outputs  if  input  is  (10 , 20 , 30 , 40) ?   (Homework)
a = input('Enter  Tuple  :  ')
print(a)#'(10 , 20 , 30 , 40)'
print(type(a))#class str
b = eval(a)
print(b)#(10 , 20 , 30 , 40)
print(type(b))#class tuple
print(len(b))#4

# Find  outputs  (Home work)
a = (10 , [20 , 30 , 40] , 50 , 60)
#a[1][0] = 70 #error
print(a)#(10 , [20 , 30 , 40] , 50 , 60)
#a[1] = [80 , 90 , 100]#error
print(a)#(10 , [20 , 30 , 40] , 50 , 60)
 # Find  outputs  (Homework)
a = [10 , (20 , 30 , 40) , 50 , 60]
#a[1][0] = 70#tuple cannot modify
print(a)#[10 , (20 , 30 , 40) , 50 , 60]
a[1] = [80 , 90]
print(a)#[10, [80, 90], 50, 60]

 # Find  outputs   (Homework)
a = 25
b = 10.8
c = 'Hyd'
d = True
x = a , b , c , d
print(x)#(25, 10.8, 'Hyd', True)
print(type(x))#class tuple
 # Find  outputs   (Homework)
x = 25 , 10.8 , 'Hyd' , True
a , b , c , d = x
print(a)#25
print(b)#10.8
print(c)#'Hyd
print(d)#True
#p , q , r =  x
#a , b , c , d  , e = x

 # Find  outputs   (Home  work)
x = 25 , 10.8 , 'Hyd' , True
a , *b , c = x
print(a)#25
print(b)#[10.8 , 'Hyd' ]
print(c)#True
# Find  outputs   (Home  work)
tpl = 25 , 10.8 , 'Hyd' , True
a , b , *c , d , e = tpl
print(a)#25
print(b)#10.8
print(c)#[]
print(d)#'Hyd'
print(e)#True

# Find  outputs   (Homework)
x = 25 , 10.8 , 'Hyd' , True , 3 + 4j
a , b , _ , d , _= x
print(a)#25
print(b)#10.8
print(_)#3+4j
print(d)#True
print(_)#3+4j
 # tuple()  function  demo  program   (Homework)
a = range(100 , 150 , 10)
b = tuple(a)
print(b)#(100, 110, 120, 130, 140)
print(type(b))#class tuple
c = [10 , 20 , 15, 18]
d = tuple(c)
print(d)#(10, 20, 15, 18)
e = tuple('Vamsi')
print(e)#('V', 'a', 'm', 's', 'i')
#print(tuple(25))#error int
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

#  How  to  modify  an  element  of  tuple ?    (Homework)
a  =  10 ,  20 ,  30 ,   40 ,  50
#     0      1       2       3      4
#a[2] = 35
print(a)
print(id(a))
a=list(a)
a[2]=35
a=tuple(a) #How  to  modify  30  in  tuple  to  35
print(a)
print(id(a))

# How  to  delete  an  element  of  tuple ?   (Home  work)
a  = 10 , 20 , 30 , 40 , 50
#    0     1      2     3      4
#a . remove(30)
#del  a[2]
#a . pop(2)
print(a)
print(id(a))
a= list(a)
a.remove(30)
a= tuple(a)#How  to  remove  30  from  tuple  'a'
print(a)#(10, 20, 40, 50)
print(id(a))#address
 #  Nested   tuple  (Homework)
a = ( (10 , 20)  ,  (30 , 40 , 50)  ,  (60 , 70 , 80 , 90) )
print(a)
print(type(a))
print(len(a))
print(a[0])#How  to  print  1st  inner  tuple)1
print(a[1])#How  to  print  2nd  inner  tuple)
print(a[2])#How  to  print  3rd  inner  tuple)
print(a[0][1])#How  to  print  20)
print(a[1][2])#How  to  print  50)
print(a[2][3])#How  to  print  90)

# Find  outputs  (Home  work)
a = ((10 , 20 , 30),)
print(a[0])#How  to   print  inner  tuple)
print(a[:])#How  to   print  inner  tuple  in  another  way)
print(a[0][0])#How   to  print   10)
print(a[0][1])#How   to  print   20)
print(a[0][2])#How   to  print   30)
b = ((),)
print(b[0])#How  to   print  inner  tuple  of  tuple  'b')
print(b[:])#How  to   print  inner  tuple  of  tuple  'b'  in  another  way)

# Find  outputs (Homework)
a =((10, 20, 30))
print(a)#((10, 20, 30))
print(*a)#((10, 20, 30))
b = (())
print(b)#10, 20, 30
print(*b)#()
# What  are  the  outputs  if  input  is  {10 , 20 , 15 , 18 , 20 , 12 , 18}
a = input('Enter  Set  :  ')
print(a)#{10 , 20 , 15 , 18 , 20 , 12 , 18}
print(type(a))#class str
b = eval(a)
print(b)#{10 , 20 , 15 , 18 , 20 , 12 , 18}
print(type(b))#set


#  Find  outputs  (Homework)
#print({(10 , 20 , 30)})#{(10 , 20 , 30)}
#print({[10 , 20 , 30]})#{[10 , 20 , 30]}
#print({{10 , 20 , 30}})#{{10 , 20 , 30}}
#print({{}})#{{}}
 # How  to  print  set  in  different ways  (Homework)
a = {25 , True , 'Hyd' , 10.8}
print('set  with  print  function')
print(a)
print('Iterate  elements  of  set  with  for  loop')
for x in a:
    print(x)

# How  to  iterate  set  with  for  loop
# Find  outputs  (Homework)
a = 'Hyd'
b = True
c = 25
d = 1
e = 'Hyd'
s = {a , b , c , d , e}
print(s)#{'Hyd', True, 25}
print(len(s))#3
print(type(s))# class set

 # Find  outputs  (Homework)
s = {'Hyd',  25,  True,  10.8 }
print(s)#{'Hyd',  25,  True,  10.8 }
a , b , c , d = s
print(a)#'Hyd'
print(b)#25
print(c)#True
print(d)#10.8
# Find  outputs  (Homework)
s = {'Hyd',  25,  True,  10.8 }
print(s)#{'Hyd',  25,  True,  10.8 }
a , *b = s
print(a)#
print(b)#
print(type(b))
# Find  outputs  (Homework)
s = {'Hyd',  25,  True,  10.8 }
print(s)
a , *b , c = s
print(a)
print(b)
print(c)
# Find  outputs  (Homework)
s = {20 , 10 , 20 , 10}
print(s)
x , y = s
print(x)
print(y)

# set()  function  demo  program  (Home  work)
a = range(100 , 151 , 10)
b = set(a)
print(b)#{100,110,120,130,140,150}

c = [10 , 20 , 15 , 18 , 10 , 50 , 20 , 12 , 18]
d = set(c)
print(d)#{10,15,18,12,20,50}
e = set('Rama  rAo')
print(e)#{'r', 'a', 'A', ' ', 'o', 'm', 'R'}
#print(set(25))
print(set())#set()

# add()  method  demo  program  (Homework)
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
print(a)#{None, True, 10.8, 'Hyd', 25}
# a . add(10 , 20 , 30)
# a . add([10,20,30])


 # Find  outputs  (Homework)
a = {25 , 10.8 , 'Hyd' , True}
tpl = (10 , 20 , 30)
print(a)#{25 , 10.8 , 'Hyd' , True}
print(id(a))
a . add(tpl)
a . add('Sec')
print(a)#{True, 'Hyd', 'Sec', 10.8, (10, 20, 30), 25}
print(id(a))
print(len(a))#6
# a . add([100 , 200 , 300])
# a . add(set())
# a . add({ })

 # Find  outputs (Homework)
s = set()
tpl = (10 , 20 , 15 , 18)
s . add(tpl)
print(s)#{(10, 20, 15, 18)}
print(len(s))#4

 # update()  method  demo program  (Homework)
tpl = (10 , 20 , 15, 18 , 10 , 20)
s = set()
s . update(tpl)
print(len(s))
print(s)#{10, 18, 20, 15}
# s . update(25)


# Find  outputs  (Homework)
a = [10 , 20 , 30]
b = {30 , 40,50 }
c = (50 , 60 , 70)
s = set()
s . update(a , b , c)
print(s)#{50, 20, 70, 40, 10, 60, 30}
print(len(s))#7
# s . add(a , b , c)

# Find  outputs  (Homework)
a = set()
a . update('Rama Rao')
print(a)#{'m', 'R', ' ', 'a', 'o'}
print(len(a))#5
# a . update(3 + 4j , 10.8 , True)

# copy()  method  demo  program  (Homework)
a = {10 , 20 , 15 , 18}
print(a)#{10 , 20 , 15 , 18}
b = a . copy()
print(b)#{10 , 20 , 15 , 18}
print(a  is  b)#False
print(a  ==  b)#True
c = a
print(a  is  c)#True

 # remove()  method  demo  program  (Homework)
a = {25 , 10.8 , 'Hyd' , True}
print(a)
a . remove('Hyd')
print(a)#{25, 10.8, True}
# a . remove('Sec')



 # discard()  method  demo  program (Homework)
a = {25 , 10.8 , 'Hyd' , True}
print(a)
a . discard('Hyd')
print(a)
a . discard('Sec')
print(a)
# a . remove('Sec')

# clear()  method  demo  program (Homework)
a = {10 , 20 , 15 , 18}
print(a)#{10 , 20 , 15 , 18}
a . clear()
print(a)#set()
print(len(a))#4


# Find  outputs  (Home work)
a = {10 , 20 , 30 , 40}
b = [30 , 40 , 50 , 60]
#print(a . union(b))
#print(a | b)
#print(b . union(a))
#print(a + b)

"""