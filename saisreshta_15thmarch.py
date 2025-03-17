program1:
# Find  outputs   
a = 25 , 10.8 , 3 + 4j , 'Hyd' , True , None , 'Hyd' , 25
print(a)       #  (25 , 10.8 , 3 + 4j , 'Hyd' , True , None , 'Hyd' , 25)
print(type(a))  # <class 'tuple'>
a[3] = 'Sec'   # error due to tuple is immmutable
a[3 : 6] = 60 , 70 , 80  # error due to tuple is immmutable

program2:
#  What   are  the  outputs  if  input  is  (10 , 20 , 30 , 40) ?   (Home  work)
a = input('Enter  Tuple  :  ')   #  (10 , 20 , 30 , 40)
print(a)        # (10 , 20 , 30 , 40)
print(type(a))  #<class 'str'>
b = eval(a)     #  (10 , 20 , 30 , 40)
print(b)        #  (10 , 20 , 30 , 40)
print(type(b))  #  <class 'tuple'>
print(len(b))   #  4  

program3:
# Find  outputs  (Home  work)
a = (10 , [20 , 30 , 40] , 50 , 60)
a[1][0] = 70
print(a)   #  (10 , [70 , 30 , 40] , 50 , 60)
a[1] = [80 , 90 , 100]  # error tuple is immutable
print(a) #  (10 , [70 , 30 , 40] , 50 , 60) 

program4:
# Find  outputs  (Home  work)
a = [10 , (20 , 30 , 40) , 50 , 60]
#a[1][0] = 70  # error
print(a)  #    [10 , (20 , 30 , 40) , 50 , 60]
a[1] = [80 , 90]
print(a)  #  [10 , [80 , 90] , 50 , 60]  

program5:
# Find  outputs   (Home  work)
a = 25
b = 10.8
c = 'Hyd'
d = True
x = a , b , c , d
print(x)   #  (25 , 10.8 , 'Hyd' , True)
print(type(x))  #  <class 'tuple'>  

program6:
# Find  outputs   (Home  work)
x = 25 , 10.8 , 'Hyd' , True
a , b , c , d = x
print(a)  #  25
print(b)  # 10.8
print(c)  # 'Hyd'
print(d)  # True
p , q , r =  x   # error to many values
a , b , c , d  , e = x  # error excepceted 5 but 4 values here  

program7:
# Find  outputs   (Home  work)
x = 25 , 10.8 , 'Hyd' , True
a , *b , c = x 
print(a)  # 25
print(b)  # [10.8 , 'Hyd']
print(c)  # True   '''

program8:
# Find  outputs   (Home  work)
tpl = 25 , 10.8 , 'Hyd' , True
a , b , *c , d , e = tpl
print(a)  # 25
print(b)  # 10.8
print(c)  # []
print(d)  # 'Hyd'
print(e)  #  True  

program9:
# Find  outputs   (Home  work)
x = 25 , 10.8 , 'Hyd' , True , 3 + 4j
a , b , _ , d , _= x
print(a)  # 25
print(b)  # 10.8
print(_)  # {3+4j)
print(d)  # True
print(_)  # (3+4j) 

program10:
# tuple()  function  demo  program   (Home  work)
a = range(100 , 150 , 10)
b = tuple(a)
print(b)  #  (100 , 110 , 120 , 130 , 140)
print(type(b))  # <class 'tuple'>
c = [10 , 20 , 15, 18]
d = tuple(c)  #   (10 , 20 , 15, 18)
print(d)   #  (10 , 20 , 15, 18)
e = tuple('Vamsi')
print(e)  # ('V' , 'a' , 'm' , 's' , 'i')
print(tuple(25))  # error
print(tuple())    #() 

program11:
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

program12:
#How  to  modify  an  element  of  tuple ?    (Home  work)
a  =  10 ,  20 ,  30 ,   40 ,  50
#     0      1       2       3      4
#a[2] = 35  # error
print(a)  # (10 ,  20 ,  30 ,   40 ,  50)
print(id(a))  # address of a may be 100004567
a=a[:2]+ (35,) + a[2:]
print(a) # (10 ,  20 ,  35 , 30 ,   40 ,  50)
print(id(a)) # id of the a different  

program13:
# How  to  delete  an  element  of  tuple ?   (Home  work)
a  = 10 , 20 , 30 , 40 , 50
#    0     1      2     3      4
#a . remove(30)  # error
#del  a[2]  # error
#a . pop(2)  #  error 
print(a)    #  (10 , 20 , 30 , 40 , 50)
print(id(a)) # id of the a may be 23457544554365
a=a[:2]+a[3:]
print(a)   #  (10 , 20 , 40 , 50)
print(id(a))  #  id of a different from above a  

program14:
#  Nested   tuple  (Home  work)
a = ( (10 , 20)  ,  (30 , 40 , 50)  ,  (60 , 70 , 80 , 90) )
print(a)     #  ( (10 , 20)  ,  (30 , 40 , 50)  ,  (60 , 70 , 80 , 90) )
print(type(a))  # <class 'tuple'>
print(len(a))   #  3
print(a[0])   # print  1st  inner  tuple i.e (10 , 20)
print(a[1])   #  print  2nd  inner  tuple i.e (30 , 40 , 50)
print(a[2])   # print  3rd  inner  tuple i.e (60 , 70 , 80 , 900
print(a[0][1])  # print  20
print(a[1][2])  #  print  50
print(a[2][3])  #  print  90   

program15:
# Find  outputs  (Home  work)
a = ((10 , 20 , 30),)
print(a[0])  # print  inner  tuple i.e  (10 , 20 , 30)
for x in a:
	print(x)
print(*a)
print(a[0][0])  #  print   10
print(a[0][1])  #  print   20
print(a[0][2])  #  print   30
b = ((),)
print(b[0])  #   print  inner  tuple  of  tuple  'b'
print(*b) #  print  inner  tuple  of  tuple  'b'  in  another  way
for x in b:
	print(x)  

program16:
#  Find  outputs (Home  work)
a = ((10 , 20 , 30))
print(a)  # (10 , 20 , 30)
print(*a) # 10 , 20 , 30
b = (())   
print(b)  # ()
print(*b) # empty  

program17:
# What  are  the  outputs  if  input  is   {10 , 20 , 15 , 18 , 20 , 12 , 18}
a = input('Enter  Set  :  ')   #  input is {10 , 20 , 15 , 18 , 20 , 12 , 18}
print(a) #  {10 , 20 , 15 , 18 , 20 , 12 , 18}
print(type(a))  # <class 'str'>
b = eval(a)    
print(b)    #  {10 , 20 , 15 , 12 , 18}
print(type(b)) # <class 'set'>  

program18:
#  Find  outputs  (Home  work)
print({(10 , 20 , 30)})   # (10 , 20 , 30)
print({[10 , 20 , 30]})   #  error due set doesn't contain mutable objects such as list , set , dict
print({{10 , 20 , 30}})    #  error due set doesn't contain mutable objects such as list , set , dict
print({{}})     #  error due set doesn't contain mutable objects such as list , set , dict  

program19:
# How  to  print  set  in  differnet ways  (Home  work)
a = {25 , True , 'Hyd' , 10.8}
print('set  with  print  function')
print(a)        # {'Hyd' , True , 10.8 , 25}
print('Iterate  elements  of  set  with  for  loop')
for x in a:
	print(x)   

porgram20:
# Find  outputs  (Home  work)
a = 'Hyd'
b = True
c = 25
d = 1
e = 'Hyd'
s = {a , b , c , d , e} # {'Hyd' , True , 25}
print(s)  #  {'Hyd' , True , 25}
print(len(s))  #  3
print(type(s))  # <class 'set'>  

program21:
'''# Find  outputs  (Home  work)
s = {'Hyd',  25,  True,  10.8 }
print(s)   #  {25 , True , 10.8 , 'Hyd'}
a , b , c , d = s
print(a)  #  25
print(b)  # True 
print(c)  # 10.8
print(d)  # 'Hyd'  

program22:
# Find  outputs  (Home  work)
s = {'Hyd',  25,  True,  10.8 }
print(s)   #  {25 , True , 10.8 , 'Hyd'}
a , *b = s 
print(a)  # 25
print(b)  # [True , 10.8 ,'Hyd']
print(type(b))  # <class 'list'>  

program23:
# Find  outputs  (Home  work)
s = {'Hyd',  25,  True,  10.8 }
print(s)  #  {'Hyd' , 10.8 , True , 25}
a , *b , c = s
print(a) # Hyd
print(b) # [10.8 , True]
print(c) # 25  

program24:
# Find  outputs  (Home  work)
s = {20 , 10 , 20 , 10}
print(s)  # {10 , 20}
x , y = s 
print(x)  # 10
print(y)  # 20  

program25:
# set()  function  demo  program  (Home  work)
a = range(100 , 151 , 10)
b = set(a)  # {100 , 120 , 110 , 140 , 130 , 150}
print(b)    # {100 , 120 , 110 , 140 , 130 , 150}
c = [10 , 20 , 15 , 18 , 10 , 50 , 20 , 12 , 18]
d = set(c)  #  {20 , 10 ,15 , 12 , 50 , 18}
print(d)    #   {20 , 10 ,15 , 12 , 50 , 18}
e = set('Rama  rAo')  #  {'R' , 'A' ,'r' , 'a' , 'm' , 'o'}
print(e)    #  {'R' , 'A' ,'r' , 'a' , 'm' , 'o', ''}
print(set(25)) # error
print(set())   # set()  

program26:
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
print(a)    #  {25 , 10.8 , True ,'Hyd' , None}
a . add(10 , 20 , 30)  # error
a . add([10,20,30])   # error  

program27:
# Find  outputs  (Home  work)
a = {25 , 10.8 , 'Hyd' , True}
tpl = (10 , 20 , 30)
print(a)  #  {'Hyd' , 25 , 10.8 , True}
print(id(a)) # id of the set a maybe 232289756553
a . add(tpl) 
a . add('Sec')
print(a)   # {'Sec' , (10 , 20 ,30) , 'Hyd' , True , 10.8 , 25}
print(id(a))   # id of the set a maybe 232289756553
print(len(a))  # 5
a . add([100 , 200 , 300])  # error
a . add(set())    #  error
a . add({ })    #  error  

program28:
# Find  outputs (Home  work)
s = set()
tpl = (10 , 20 , 15 , 18)
s . add(tpl)
print(s)  # {(10 , 20 , 15 , 18)}
print(len(s))  #  1  

program29:
# update()  method  demo program  (Home  work)
tpl = (10 , 20 , 15, 18 , 10 , 20)
s = set()
s . update(tpl)
print(len(s)) # 4
print(s)   # {20 , 10 , 15 , 18}
#s . update(25) # error  

program30:
# Find  outputs  (Home  work)
a = [10 , 20 , 30]
b = {30 , 40,50 }
c = (50 , 60 , 70)
s = set()
s . update(a , b , c)
print(s)  # {20 , 10 , 30 , 50 , 70 , 60 , 40}
print(len(s))   #  7
s . add(a , b , c)  # error 

program31:
# Find  outputs  (Home  work)
a = set()
a . update('Rama Rao')
print(a)  #  {'a' , 'R' , ' ' , 'm' , 'o'}
print(len(a))  # 5
a . update(3 + 4j , 10.8 , True) # error due to update contains only sequence 

program32:
# copy()  method  demo  program  (Home  work)
a = {10 , 20 , 15 , 18}
print(a)  # {20 , 18 , 15 , 10}
b = a . copy()
print(b)  #  {20 , 18 , 15 , 10}
print(a  is  b)  # False
print(a  ==  b)  # True
c = a    # c point the same set where a points
print(a  is  c)  # True  

program33:
# remove()  method  demo  program  (Home  work)
a = {25 , 10.8 , 'Hyd' , True}
print(a)   # {True , 'Hyd' , 25 , 10.8}
a . remove('Hyd')
print(a)   # {10.8 , 25 , True}
a . remove('Sec')  # error  

program34:
# discard()  method  demo  program (Home  work)
a = {25 , 10.8 , 'Hyd' , True}
print(a)    # {True , 10.8 , 25 , 'Hyd'}
a . discard('Hyd')
print(a)  # {True , 10.8 , 25}
a . discard('Sec') 
print(a)   #  {True , 10.8 , 25} 
a . remove('Sec')  # error  

program35:
# clear()  method  demo  program (Home  work)
a = {10 , 20 , 15 , 18}
print(a)  # {18 , 20 , 15 , 10}
a . clear()
print(a)  # set()
print(len(a))  # 0  

program36:
# Find  outputs  (Home work)
a = {10 , 20 , 30 , 40}
b = [30 , 40 , 50 , 60]
print(a . union(b))  # {10 , 40 , 20 , 30 , 60 , 50}
#print(a | b)  # error becz merge only set & set
print(b . union(a))  # error
print(a + b)  # error  
