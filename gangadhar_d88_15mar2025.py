# Find  outputs   (Home  work)
a = 25 , 10.8 , 3 + 4j , 'Hyd' , True , None , 'Hyd' , 25
print(a) #(25 , 10.8 , 3 + 4j , 'Hyd' , True , None , 'Hyd' , 25)
print(type(a))# <class "tuple">
#a[3] = 'Sec'  #error due to tuple immutable
#a[3 : 6] = 60 , 70 , 80 #error due to tuple immutable

#  What   are  the  outputs  if  input  is  (10 , 20 , 30 , 40) ?   (Home  work)
a = input('Enter  Tuple  :  ')
print(a) #(10,20,30)
print(type(a))#<class 'str'>
b = eval(a)
print(b)#(10,20,30)
print(type(b))#<class 'tuple'>
print(len(b))# 3

# Find  outputs  (Home  work)
a = (10 , [20 , 30 , 40] , 50 , 60)
a[1][0] = 70 # insert 70 in place of 20
print(a)#(10 , [70 , 30 , 40] , 50 , 60)
#a[1] = [80 , 90 , 100]
#print(a)#error due tuple is immmutable, item assignment is not allowed

# Find  outputs  (Home  work)
a = [10 , (20 , 30 , 40) , 50 , 60]
#a[1][0] = 70
#print(a)#error 
a[1] = [80 , 90]
print(a)#[10 , [80 , 90] , 50 , 60]

# Find  outputs   (Home  work)
a = 25
b = 10.8
c = 'Hyd'
d = True
x = a , b , c , d
print(x)#(25,10.8,'hyd',True)
print(type(x))# <class 'tuple'>

# Find  outputs   (Home  work)
x = 25 , 10.8 , 'Hyd' , True
a , b , c , d = x # assignig a,b,c,d 
print(a)# 25
print(b)#10.8
print(c)#'hyd'
print(d)#True
#p , q , r =  x # value error, due to one item less in leftside
#a , b , c , d  , e = x # value error, due to one item more in leftside

# Find  outputs   (Home  work)
x = 25 , 10.8 , 'Hyd' , True
a , *b , c = x # assign values of a,b,c
print(a)#25
print(b)#[10.8,'hyd]
print(c)# True

# Find  outputs   (Home  work)
tpl = 25 , 10.8 , 'Hyd' , True
a , b , *c , d , e = tpl
print(a)#25
print(b)#10.8
print(c)#[]
print(d) #"hyd"
print(e)# True

# Find  outputs   (Home  work)
x = 25 , 10.8 , 'Hyd' , True , 3 + 4j
a , b , _ , d , _= x
print(a)#25
print(b)#10.8
print(_)#'hyd'
print(d)# True
print(_)#3+4j

# tuple()  function  demo  program   (Home  work)
a = range(100 , 150 , 10)
b = tuple(a)
print(b)#(100,110,120,130,140)
print(type(b))#<class'tuple'>
c = [10 , 20 , 15, 18]
d = tuple(c)
print(d)#(10 , 20 , 15, 18)
e = tuple('Vamsi')
print(e)#('V', 'a', 'm', 's', 'i')
#print(tuple(25))# Error ,becoz tuple function should be a sequence or empty,but not non sequence
print(tuple())#()

#index()  and  count()  methods  demo  program   (Home  work)
a = (10 , 20 , 15 , 12 , 14 , 15 , 18 , 19 , 15 , 12 , 25)
#     0    1      2     3    4     5     6    7     8    9    10
try:

	i = a . index(15) # Find the first occurrence of 15
	while  True:
		print('15 is found at index : ' , i)#2 <nexlt line> 5 <nexlt line>8
		i = a . index(15 , i + 1) # Find next occurrence of 15
except:
		print(F'15  is  found  {a . count(15)}  times')# 3 times

#  How  to  modify  an  element  of  tuple ?    (Home  work)
a  =  10 ,  20 ,  30 ,   40 ,  50
#     0      1       2       3      4

#a[2] = 35 #error Tuples are immutable, so elements cannot be modified directly.

#print(a)
#print(id(a))
#How  to  modify  30  in  tuple  to  35

print(a)
print(id(a))

# How  to  delete  an  element  of  tuple ?   (Home  work)
a  = 10 , 20 , 30 , 40 , 50
#    0     1      2     3      4
#a . remove(30) # error due to tuple not have a remove method ,immutable
#del  a[2] # error due to tuple not have a deletion ,immutable
#a . pop(2) # error due to tuple not have a pop method ,immutable
print(a)#(10,20,30,40,50)
print(id(a)) # 456700111
#How  to  remove  30  from  tuple  'a'
print(a)
print(id(a))

# add()  method  demo  program  (Home  work)
a = set()
a . add(True)#True insert to set
a . add(25)# 25 is insert to set
a . add(10.8)# 10.8 is insert to set
a . add(1)#  1 is  insert to set
a . add('Hyd')#"hyd " insert to set
a . add(25)# not insert to set
a . add(None)# None insert to set
a . add('Hyd')# not insert to set
a . add(1.0)# not insert to set
print(a)#{True,25,10.8,1,'hyd',None}
#a . add(10 , 20 , 30)#error ,add method takes only one argument
#a . add([10,20,30])# error ,add()  method  should  be single immutable  object  

#Find  outputs  (Home  work)
print({(10 , 20 , 30)})#{(10, 20, 30)}
#print({[10 , 20 , 30]})# error ,immutable objects are allowed
#print({{10 , 20 , 30}})# error ,immutable objects are allowed
#print({{}})#error,it allowed nested set

a = ( (10 , 20)  ,  (30 , 40 , 50)  ,  (60 , 70 , 80 , 90) )
print(a)#( (10 , 20) , (30 , 40 , 50) , (60 , 70 , 80 , 90) )
print(type(a))#<class'tuple'>
print(len(a))#3
print("How  to  print  1st  inner  tuple")
print(a[0])
print("How  to  print  2nd inner  tuple")
print(a[1])
print("How  to  print  3rd inner  tuple")
print(a[2])
print("How  to  print  30")
print(a[0][1])
print("How  to  print  50")
print(a[1][-1])
print("How  to  print  90")
print(a[2][-1])


# How  to  print  set  in  differnet ways  (Home  work)
a = {25 , True , 'Hyd' , 10.8}
print('set  with  print  function')
print(a)
print('Iterate  elements  of  set  with  for  loop')
for i in a:
    print(i)

# Find  outputs  (Home  work)
a = 'Hyd'
b = True
c = 25
d = 1
e = 'Hyd'
s = {a , b , c , d , e}
print(s)#{"hyd",True,25}
print(len(s))#3
print(type(s))#<class 'set'>

# Find  outputs  (Home  work)
s = {'Hyd',  25,  True,  10.8 }
print(s)#{'Hyd',  25,  True,  10.8 }
a , b , c , d = s
print(a)#'hyd
print(b)#25
print(c)#True
print(d)# 10.8

# Find  outputs  (Home  work)
a = {25 , 10.8 , 'Hyd' , True}
tpl = (10 , 20 , 30)
print(a)#(10 , 20 , 30)
print(id(a))#may be 2468704398
a . add(tpl)#{25 , 10.8 , 'Hyd' , True,(10 , 20 , 30)}
a . add('Sec')#insert "sec" into set
print(a) #{25 , 10.8 , 'Hyd' , True,(10 , 20 , 30),"sec"}
print(id(a))# same as above  2468704398
print(len(a))#6
#a . add([100 , 200 , 300])#error,set not hold mutuable bject
#a . add(set()) #error,set not hold mutuable bject
#a . add({ }) #error , set not hold mutuable bject
# Find  outputs  (Home  work)
s = {'Hyd',  25,  True,  10.8 }
print(s)# {'Hyd',  25,  True,  10.8 }
a , *b = s
print(a)#'hyd'
print(b)#[25,  True,  10.8 ]
print(type(b))#<class 'list'>

# set()  function  demo  program  (Home  work)
a = range(100 , 151 , 10)
b = set(a)
print(b)#{100,110,120,130,140,150}
c = [10 , 20 , 15 , 18 , 10 , 50 , 20 , 12 , 18]
d = set(c)
print(d)#{10,15,20,18,12}
e = set('Rama  rAo')
print(e)#{'r', 'o', 'R', 'm', ' ', 'a', 'A'} any order
#print(set(25))#error ,because set must be sequence 
print(set())# set()

# Find  outputs  (Home  work)
s = {'Hyd',  25,  True,  10.8 }
print(s)# {'Hyd',  25,  True,  10.8 } any order
a , *b , c = s
print(a)#'hyd' any element
print(b)#[25,  True] any 2 element
print(c)#10.8 any element

# Find  outputs  (Home  work)
s = {20 , 10 , 20 , 10}
print(s)#{20,10}
x , y = s
print(x)#10 any order
print(y)#20 any order

# Find  outputs  (Home  work)
a = set()
a . update('Rama Rao')# Rama rao insert into set 
print(a)#{'R', 'o', ' ', 'a', 'm'}
print(len(a))#5
#a . update(3 + 4j , 10.8 , True) # error because multiple objects insert at time

# copy()  method  demo  program  (Home  work)
a = {10 , 20 , 15 , 18}
print(a)#{10 , 20 , 15 , 18}
b = a . copy()# copy a to b
print(b)#{10 , 20 , 15 , 18}
print(a  is  b) # False
print(a  ==  b)#True
c = a # c point to reference a
print(a  is  c)#True

# remove()  method  demo  program  (Home  work)
a = {25 , 10.8 , 'Hyd' , True}
print(a)#{25 , 10.8 , 'Hyd' , True} 
a . remove('Hyd')#delete 'hyd'
print(a)#{25 , 10.8 , True}
#a . remove('Sec')# error due to there is no 'sec'

# discard()  method  demo  program (Home  work)
a = {25 , 10.8 , 'Hyd' , True}
print(a)#{25 , 10.8 , 'Hyd' , True}
a . discard('Hyd')
print(a)#{25 , 10.8 , True}
#a . discard('Sec') # error due to there is no 'sec'
#print(a)
#a . remove('Sec')# error due to there is no 'sec'

# clear()  method  demo  program (Home  work)
a = {10 , 20 , 15 , 18}
print(a)#{10 , 20 , 15 , 18}
a . clear()#delete all elements is set ,return empty
print(a)#set()
print(len(a))#0


