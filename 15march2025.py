# Find  outputs  (Home work)
'''
a = {10 , 20 , 30 , 40}
b = [30 , 40 , 50 , 60]
print(a . union(b))# {10,20,30,40,50,60}
print(a | b)#error 
print(b . union(a))# error list has no attribute of union
print(a + b)# error
'''

# clear()  method  demo  program (Home  work)
'''
a = {10 , 20 , 15 , 18}
print(a)#{10,20,15,18}
a . clear()# removes all the elements in the set
print(a)#set()
print(len(a))#0
'''

# discard()  method  demo  program (Home  work)
'''
a = {25 , 10.8 , 'Hyd' , True}
print(a)#{25 , 10.8 , 'Hyd' , True}
a . discard('Hyd')
print(a)#{25 , 10.8 ,True}
a . discard('Sec')
print(a)#{25 , 10.8 ,True}
a . remove('Sec')# error
'''

# remove()  method  demo  program  (Home  work)
'''
a = {25 , 10.8 , 'Hyd' , True}
print(a)#{25 , 10.8 , 'Hyd' , True}
a . remove('Hyd')
print(a)#{25 , 10.8 ,True}
a . remove('Sec')# error
'''

# copy()  method  demo  program  (Home  work)
'''
a = {10 , 20 , 15 , 18}
print(a)#{10 , 20 , 15 , 18}
b = a . copy()
print(b)#{10 , 20 , 15 , 18}
print(a  is  b)# false
print(a  ==  b)#true
c = a# referance of object {10 , 20 , 15 , 18} has an another referance of c
print(a  is  c)#true
'''

# Find  outputs  (Home  work)
'''
a = set()
a . update('Rama Rao')
print(a)#{'m','r','o','a'}
print(len(a))# 5
a . update(3 + 4j , 10.8 , True)# error complex object raizes error
'''

# Find  outputs  (Home  work)
'''
a = [10 , 20 , 30]
b = {30 , 40,50 }
c = (50 , 60 , 70)
s = set()
s . update(a , b , c)# {50, 20, 70, 40, 10, 60, 30}
print(s)#{50, 20, 70, 40, 10, 60, 30}
print(len(s))# 7
s . add(a , b , c)# error becz we cant add list set tuple and set can only take one orgument 
'''

# update()  method  demo program  (Home  work)
'''
tpl = (10 , 20 , 15, 18 , 10 , 20)
s = set()
s . update(tpl)#{10,20,15,18}
print(len(s))#4
print(s)#{10,20,15,18}
s . update(25)# error int object we cant initiate it direcly it raises type error int object not itrable'
'''

# Find  outputs (Home  work)
'''
s = set()
tpl = (10 , 20 , 15 , 18)
s . add(tpl)
print(s)#{(10,20,15,18)}
print(len(s))#1
'''

# Find  outputs  (Home  work)
'''
a = {25 , 10.8 , 'Hyd' , True}
tpl = (10 , 20 , 30)
print(a)# {25 , 10.8 , 'Hyd' , True}
print(id(a)) # address 1234562346234
a . add(tpl) 
a . add('Sec')
print(a)# {25 , 10.8 , 'Hyd' , True,(10 , 20 , 30),'Sec'}
print(id(a))# address same as the above 
print(len(a))# 6
a . add([100 , 200 , 300])# error set objects can not contain mutable objects
a . add(set())#error same as above 
a . add({ })# error same as above

'''

# add()  method  demo  program  (Home  work)
'''
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
print(a)#{True,10.8,'hyd',25,none}
a . add(10 , 20 , 30)# add can take only one argument 
a . add([10,20,30])# set take only immutable objects

'''

# set()  function  demo  program  (Home  work)
'''
a = range(100 , 151 , 10)
b = set(a)
print(b)#{100,110,120,130,140,150}
c = [10 , 20 , 15 , 18 , 10 , 50 , 20 , 12 , 18]
d = set(c)#
print(d)#{10,20,15,18,50,12}
e = set('Rama  rAo')
print(e)#{'r','a','m','o','R','A'}
print(set(25))#error
print(set())#set()

'''

# Find  outputs  (Home  work)
'''
s = {'Hyd',  25,  True,  10.8 }
print(s)#{'Hyd',  25,  True,  10.8 }
a , *b , c = s
print(a)#hyd
print(b)#[25,  True]
print(c)# 10.8
'''

# Find  outputs  (Home  work)
'''
s = {20 , 10 , 20 , 10}
print(s)# {10 , 20}
x , y = s
print(x)#10
print(y)#20
'''

# Find  outputs  (Home  work)
'''
s = {'Hyd',  25,  True,  10.8 }
print(s)# {'Hyd',  25,  True,  10.8 }
a , *b = s
print(a)#hyd
print(b) #[25,  True,  10.8]
print(type(b))#<class 'list'>
'''

# Find  outputs  (Home  work)
'''
s = {'Hyd',  25,  True,  10.8 }
print(s)#{'Hyd',  25,  True,  10.8 }
a , b , c , d = s
print(a)# hyd
print(b)# 25
print(c)# true
print(d)# 10.8
'''


# Find  outputs  (Home  work)
'''
a = 'Hyd'
b = True
c = 25
d = 1
e = 'Hyd'
s = {a , b , c , d , e}
print(s)#{'hyd',True,25}
print(len(s))# 3
print(type(s)) #<class 'set()'>
'''

# How  to  print  set  in  differnet ways  (Home  work)
'''
a = {25 , True , 'Hyd' , 10.8}
print(set(a))
print(a)
print('Iterate  elements  of  set  with  for  loop')
for i in a:
    print(i)
  
'''

#  Find  outputs  (Home  work)
'''
print({(10 , 20 , 30)})#{(10 , 20 , 30)}
print({[10 , 20 , 30]})# error set can'nt take mutable objects
print({{10 , 20 , 30}})# error same as above
print({{}})# error same as above
'''

# What  are  the  outputs  if  input  is  {10 , 20 , 15 , 18 , 20 , 12 , 18}
'''
a = input('Enter  Set  :  ')
print(a)#'{1,2,3,4}'
print(type(a))#<class 'str'>
b = eval(a)#
print(b)# {1,2,3,4}
print(type(b))# <class 'set'>
'''

#  Find  outputs (Home  work)
'''
a = ((10 , 20 , 30))
print(a)#(10 , 20 , 30)
print(*a)#10 , 20 , 30
b = (())
print(b)#()
print(*b)#empty 
'''

# Find  outputs  (Home  work)
'''
a = ((10 , 20 , 30),)
print(a)
print(a[:])
print(a[0][0])
print(a[0][1])
print(a[0][2])
b = ((),)
print(b)
print(b[:])
'''

#  Nested   tuple  (Home  work)
'''
a = ( (10 , 20)  ,  (30 , 40 , 50)  ,  (60 , 70 , 80 , 90) )
print(a)#( (10 , 20)  ,  (30 , 40 , 50)  ,  (60 , 70 , 80 , 90) )
print(type(a))#<class 'tuple'>
print(len(a))# 3
print(a[0])
print(a[1])
print(a[2])
print(a[0][1])
print(a[1][2])
print(a[2][3]) 

'''

# How  to  delete  an  element  of  tuple ?   (Home  work)
'''
a  = 10 , 20 , 30 , 40 , 50
#    0     1   2     3   4
a . remove(30)# tuple is immutable error
del  a[2]#error
a . pop(2)# error
print(a)# 10,20,30,40,50
print(id(a))# addess of a
print(a.remove(30))# error
print(a)#(10 , 20 , 30 , 40 , 50)
print(id(a))# same ddress as above
'''

#  How  to  modify  an  element  of  tuple ?    (Home  work)
'''
a  =  10 ,  20 ,  30 ,   40 ,  50
#     0      1       2       3      4
#a[2] = 35 #error not initilized
print(a) #(10 ,  20 ,  30 ,   40 ,  50)
print(id(a))# address of the tuple a 
b=list(a)
b[2]=35
print(tuple(b))#(10 ,  20 , 35 ,   40 ,  50)
print(a)# (10 ,  20 ,  30 ,   40 ,  50)
print(id(a))# address of the a 
'''

# Find  outputs   (Home  work)
'''
a = 25 , 10.8 , 3 + 4j , 'Hyd' , True , None , 'Hyd' , 25
print(a)#(25 , 10.8 , 3 + 4j , 'Hyd' , True , None)
print(type(a))#<class 'tuple'>
a[3] = 'Sec'# error
a[3 : 6] = 60 , 70 , 80# error  
'''


#  What   are  the  outputs  if  input  is  (10 , 20 , 30 , 40) ?   (Home  work)
'''
a = input('Enter  Tuple  :  ')
print(a)#'(1,2,3,4)'
print(type(a))# <class 'str'>
b = eval(a)
print(b)#(1,2,3,4)
print(type(b))# <clas 'tuple'>
print(len(b))# 4
'''


# Find  outputs  (Home  work)
'''
a = (10 , [20 , 30 , 40] , 50 , 60)
a[1][0] = 70
print(a) # (10 , [70 , 30 , 40] , 50 , 60)
a[1] = [80 , 90 , 100]# we can'nt replace an entire list in a tuple  error
print(a) #(10 , [70 , 90 , 100] , 50 , 60)
'''

# Find  outputs  (Home  work)
'''
a = [10 , (20 , 30 , 40) , 50 , 60]
a[1][0] = 70
print(a)# error
a[1] = [80 , 90]
print(a)#[10 , [80 , 90] , 50 , 60]
'''

# Find  outputs   (Home  work)
'''
a = 25
b = 10.8
c = 'Hyd'
d = True
x = a , b , c , d
print(x)# (25,10.8,'hyd',True)
print(type(x))# <class 'tuple'>
'''

# Find  outputs   (Home  work)
'''
x = 25 , 10.8 , 'Hyd' , True
a , b , c , d = x
print(a)# 25
print(b)# 10.8
print(c)# hyd
print(d)# True
p , q , r =  x # error
a , b , c , d  , e = x # error
'''


# Find  outputs   (Home  work)
'''
x = 25 , 10.8 , 'Hyd' , True
a , *b , c = x
print(a)# 25
print(b)# [10.8,'hyd']
print(c)# True
'''


# Find  outputs   (Home  work)
'''
tpl = 25 , 10.8 , 'Hyd' , True
a , b , *c , d , e = tpl
print(a) # 25
print(b) # 10.8
print(c) # []
print(d) # 'Hyd'
print(e) # True
'''

# Find  outputs   (Home  work)
'''
x = 25 , 10.8 , 'Hyd' , True , 3 + 4j
a , b , _ , d , _= x
print(a) #25
print(b) #10.8
print(_) #3+4j
print(d) #True
print(_) #3+4j
'''


# tuple()  function  demo  program   (Home  work)

'''
a = range(100 , 150 , 10)
b = tuple(a)
print(b) # (100,110,120,130,140)
print(type(b)) # <class 'tuple'>
c = [10 , 20 , 15, 18]
d = tuple(c) 
print(d) # (10,20,15,18)
e = tuple('Vamsi')
print(e) #('v','a','m','s','i')
print(tuple(25))# error
print(tuple()) # ()

'''


#index()  and  count()  methods  demo  program   (Home  work)
'''
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