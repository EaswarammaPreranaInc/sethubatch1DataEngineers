# Find  outputs   (Home  work)
a = 25 , 10.8 , 3 + 4j , 'Hyd' , True , None , 'Hyd' , 25
print(a)
print(type(a))
#a[3] = 'Sec' & tuples are not mutable
#a[3 : 6] = 60 , 70 , 80  & tuples are not mutable
#  What   are  the  outputs  if  input  is  (10 , 20 , 30 , 40) ?   (Home  work)
a = input('Enter  Tuple  :  ')
print(a) #(10 , 20 , 30 , 40)
print(type(a))# class <str>
b = eval(a) 
print(b) #(10 , 20 , 30 , 40)
print(type(b)) #  <class 'tuple'>
print(len(b)) #4
# Find  outputs  (Home  work)
a = (10 , [20 , 30 , 40] , 50 , 60)
a[1][0] = 70 
print(a) #(10 , [70 , 30 , 40] , 50 , 60)
a[1] = [80 , 90 , 100] #tuple is not mutable
print(a)# error
# Find  outputs  (Home  work)
a = [10 , (20 , 30 , 40) , 50 , 60]
a[1][0] = 70 ##tuple is not mutable error
print(a)
a[1] = [80 , 90] 
print(a)#[10 , [80 , 90] , 50 , 60]
## Find  outputs   (Home  work)
a = 25
b = 10.8
c = 'Hyd'
d = True
x = a , b , c , d
print(x) #(25,10.8,'Hyd',True)
print(type(x)) # <class 'tuple'>
# Find  outputs   (Home  work)
x = 25 , 10.8 , 'Hyd' , True
a , b , c , d = x
print(a)#25
print(b) #10.8
print(c) #Hyd
print(d) #True
p , q , r =  x #Error unpacking gives more elements
a , b , c , d  , e = x #error unpacking gives less elements
## Find  outputs   (Home  work)
x = 25 , 10.8 , 'Hyd' , True
a , *b , c = x
print(a)
print(b)
print(c)
## Find  outputs   (Home  work)
tpl = 25 , 10.8 , 'Hyd' , True
a , b , *c , d , e = tpl
print(a)#25
print(b)#10.8
print(c)#[]
print(d)# Hyd
print(e)#True
## Find  outputs   (Home  work)
x = 25 , 10.8 , 'Hyd' , True , 3 + 4j
a , b , _ , d , _= x
print(a) #25
print(b) #10.8
print(_) #(3 + 4j)
print(d) #True
print(_) #(3 + 4j)
# tuple()  function  demo  program   (Home  work)
a = range(100 , 150 , 10)
b = tuple(a) 
print(b) #(100,110,120,130,140)
print(type(b)) #<class 'tuple'>
c = [10 , 20 , 15, 18]
d = tuple(c) 
print(d) #(10 , 20 , 15, 18)
e = tuple('Vamsi') 
print(e) #('V','a','m','s','i')
print(tuple(25)) #error
print(tuple()) #()
#a = (10, 20, 15, 12, 14, 15, 18, 19, 15, 12, 25)
#    0    1    2    3    4    5    6    7    8    9    10
try:
    k = []
    i = a.index(15)
    while True:
        print('15 is found at index : ', i)
        k.append(i)
        i = a.index(15, i + 1)

except:
    print(F'15 is found {a.count(15)} times at {k} places')
##  How  to  modify  an  element  of  tuple ?    (Home  work)
a  =  10 ,  20 ,  30 ,   40 ,  50
#     0      1       2       3      4
b=list(a)
b[2] = 35
print(a)
print(id(a))
#How  to  modify  30  in  tuple  to  35
a=tuple(b)
print(a)
print(id(a))
## How  to  delete  an  element  of  tuple ?   (Home  work)
a  = 10 , 20 , 30 , 40 , 50
#    0     1      2     3      4
b=list(a)
b . remove(30)
#del  b[2]
#b . pop(2)
print(a)
print(id(a))
#How  to  remove  30  from  tuple  'a'
a=tuple(b)
print(a)
print(id(a))
#  Nested   tuple  (Home  work)
a = ( (10 , 20)  ,  (30 , 40 , 50)  ,  (60 , 70 , 80 , 90) )
print(a)
print(type(a))
print(len(a))
print("How  to  print  1st  inner  tuple",a[0],*a[0])
print("How  to  print  2nd  inner  tuple",a[1],*a[1])
print("How  to  print  3rd  inner  tuple",a[2],*a[2])
print("How  to  print  20",a[0][1])
print("How  to  print  50",a[1][2])
print("How  to  print  90",a[2][3])
# What  are  the  outputs  if  input  is  {10 , 20 , 15 , 18 , 20 , 12 , 18}
a = input('Enter  Set  :  ')
print(a) #{10 , 20 , 15 , 18 , 20 , 12 , 18}
print(type(a)) #<class 'str'>
b = eval(a)
print(b) #{18, 20, 10, 12, 15}
print(type(b)) #<class 'set'>
#  Find  outputs  (Home  work)
print({(10 , 20 , 30)}) #
#print({[10 , 20 , 30]}) #unhashable list
#print({{10 , 20 , 30}}) #unhashable set
#print({{}}) #unhashable dict
# How  to  print  set  in  differnet ways  (Home  work)
a = {25 , True , 'Hyd' , 10.8}
print('set  with  print  function',a)
print(a)
print('Iterate  elements  of  set  with  for  loop')
for i in a:
    print(i)
#How  to  iterate  set  with  for  loop
# Find  outputs  (Home  work)
a = 'Hyd'
b = True
c = 25
d = 1
e = 'Hyd'
s = {a , b , c , d , e}
print(s) #{'Hyd', True, 25}
print(len(s)) #3
print(type(s)) #<class 'set'>
## Find  outputs  (Home  work)
s = {'Hyd',  25,  True,  10.8 }
print(s)
a , b , c , d = s
print(a) # Hyd
print(b) #25
print(c) #10.8
print(d) #True
# Find  outputs  (Home  work)
s = {'Hyd',  25,  True,  10.8 }
print(s) #{'Hyd',  25,  True,  10.8 }
a , *b = s #
print(a)#Hyd
print(b)#[25,  True,  10.8]
print(type(b)) #<class 'list'>
## Find  outputs  (Home  work)
s = {'Hyd',  25,  True,  10.8 }
print(s) #{'Hyd',  25,  True,  10.8 }
a , *b , c = s #
print(a) #Hyd
print(b) #[25,10.8]
print(c) #True
## Find  outputs  (Home  work)
s = {20 , 10 , 20 , 10}
print(s) #{20 , 10 }
x , y = s
print(x)#20
print(y) #10
# set()  function  demo  program  (Home  work)
a = range(100 , 151 , 10)
b = set(a)
print(b) #{100,110,120,130,140,150}
c = [10 , 20 , 15 , 18 , 10 , 50 , 20 , 12 , 18]
d = set(c) 
print(d) #{10,15,20,18,50,12}
e = set('Rama  rAo')
print(e) #{"R","a","A","r","m","o"," "}
#print(set(25)) #error non sequence 
print(set()) #set()
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
a . add((10 , 20 , 30))
#a . add([10,20,30])
print(a)
#{None, True, 'Hyd', 10.8, 25}
#{None, True, 'Hyd', 10.8, (10, 20, 30), 25}
## Find  outputs  (Home  work)
a = {25 , 10.8 , 'Hyd' , True}
tpl = (10 , 20 , 30)
print(a) #{25 , 10.8 , 'Hyd' , True}
print(id(a)) # 
a . add(tpl) #{25 , 10.8 , 'Hyd' , True,(10 , 20 , 30)}
a . add('Sec') #{25 , 10.8 , 'Hyd' , True,(10 , 20 , 30),'Sec'}
print(a) #{25 , 10.8 , 'Hyd' , True,(10 , 20 , 30),'Sec'}
print(id(a)) #
print(len(a)) #6
#a . add([100 , 200 , 300]) # error unhashable obj
#a . add(set()) ## error unhashable obj
#a . add({ }) # error unhashable obj
# Find  outputs (Home  work)
s = set()
tpl = (10 , 20 , 15 , 18)
s . add(tpl) 
print(s) ##{(10 , 20 , 15 , 18)}
print(len(s)) #1
# update()  method  demo program  (Home  work)
tpl = (10 , 20 , 15, 18 , 10 , 20)
tpl1=(40,50,10)
s = set()
s . update(tpl,tpl1,(150,)) #update() can take multiple sequences
print(len(s))
print(s)
#s . update(25) #error non sequences not allowed
# Find  outputs  (Home  work)
a = [10 , 20 , 30]
b = {30 , 40,50 }
c = (50 , 60 , 70)
s = set()
s . update(a , b , c)
print(s) #{10,20,30,40,50,60,70}
print(len(s)) #7
#s . add(a , b , c) #error add can take only 1 arg 
# Find  outputs  (Home  work)
a = set()
a . update('Rama Rao') #
print(a) ##{"R","a","m","o"," "}
print(len(a)) #5
#a . update(3 + 4j , 10.8 , True) #
# copy()  method  demo  program  (Home  work)
a = {10 , 20 , 15 , 18}
print(a) #{10 , 20 , 15 , 18}
b = a . copy()
print(b) #{10 , 20 , 15 , 18}
print(a  is  b) #False
print(a  ==  b) #True
c = a
print(a  is  c) #True
# remove()  method  demo  program  (Home  work)
a = {25 , 10.8 , 'Hyd' , True}
print(a) #{25 , 10.8 , 'Hyd' , True}
a . remove('Hyd')
print(a) #{25 , 10.8 , True}
a . remove('Sec') #error
# discard()  method  demo  program (Home  work)
a = {25 , 10.8 , 'Hyd' , True}
print(a) # {25 , 10.8 , 'Hyd' , True}
a . discard('Hyd')
print(a) # {25 , 10.8 , True}
a . discard('Sec') #ignores
print(a) # {25 , 10.8 , True}
#a . remove('Sec') #error
## clear()  method  demo  program (Home  work)
a = {10 , 20 , 15 , 18}
print(a) #{10 , 20 , 15 , 18}
a . clear() 
print(a) #set()
print(len(a)) #0
# Find  outputs  (Home work)
a = {10 , 20 , 30 , 40}
b = [30 , 40 , 50 , 60]
print(a . union(b)) #
print(a | b)
print(b . union(a))
#print(a + b)
