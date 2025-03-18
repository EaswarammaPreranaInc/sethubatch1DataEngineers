1. # Find  outputs   (Home  work)
a = 25 , 10.8 , 3 + 4j , 'Hyd' , True , None , 'Hyd' , 25
print(a)  #(25 , 10.8 , (3 + 4j) , 'Hyd' , True , None , 'Hyd' , 25)
print(type(a)) #class 'tuple'>
#a[3] = 'Sec'  #error-cannot modify because tuple is immutable 
#a[3 : 6] = 60 , 70 , 80  #error-cannot modify tuple 
-------------------------------------------------------------------------------------------
2. #  What   are  the  outputs  if  input  is  (10 , 20 , 30 , 40) ? 
a = input('Enter  Tuple  :  ')
print(a)        #(10 , 20 , 30 , 40)
print(type(a))  #<class 'str'>   because by default input() will take as str 
b = eval(a)     
print(b)        #(10 , 20 , 30 , 40)
print(type(b))  #<class 'tuple'>
print(len(b))   #4
----------------------------------------------------------------------------------------------------
3. # Find  outputs  (Home  work)
a = (10 , [20 , 30 , 40] , 50 , 60)
a[1][0] = 70
print(a)   #(10 , [70 , 30 , 40] , 50 , 60)  -list is mutable so modification is allowed
#a[1] = [80 , 90 , 100]  #error because modifying object in tuple is not allowed
print(a)   #(10 , [70 , 30 , 40] , 50 , 60)
------------------------------------------------------------------------------------------------------
4. # Find  outputs  (Home  work)
a = [10 , (20 , 30 , 40) , 50 , 60]
#a[1][0] = 70  #error because tuple object cannot be modified
print(a)         #[10 , (20 , 30 , 40) , 50 , 60]
a[1] = [80 , 90] 
print(a)         #[10 , [80 , 90] , 50 , 60]
------------------------------------------------------------------------------------------------------
5. # Find  outputs   (Home  work)
a = 25
b = 10.8
c = 'Hyd'
d = True
x = a , b , c , d
print(x) #(25,10.8,'Hyd',True)
print(type(x)) #<class 'tuple'>
----------------------------------------------------------------------------------------------------------
6. # Find  outputs   (Home  work)
x = 25 , 10.8 , 'Hyd' , True
a , b , c , d = x
print(a) #25 
print(b) #10.8
print(c) #'Hyd' 
print(d) #True
#p , q , r =  x  #error - there are 4 objects and cannot unpack with 3 varaibles 
#a , b , c , d  , e = x #error - there are only 4 objects for 5 varaibles
-----------------------------------------------------------------------------------------------------------
7. # Find  outputs 
x = 25 , 10.8 , 'Hyd' , True
a , *b , c = x
print(a)  #25 
print(b)  #[10.8,'Hyd']
print(c)  #True
--------------------------------------------------------------------------------------------------------
8. # Find  outputs   (Home  work)
tpl = 25 , 10.8 , 'Hyd' , True
a , b , *c , d , e = tpl
print(a) # 25
print(b) #10.8
print(c) #[]
print(d) # Hyd
print(e) # True 
--------------------------------------------------------------------------------------------------------
9. # Find  outputs   (Home  work)
x = 25 , 10.8 , 'Hyd' , True , 3 + 4j
a , b , _ , d , _= x
print(a) # 25
print(b) # (3+4j)
print(_) # Hyd
print(d) # True 
print(_) # (3+4j)
-------------------------------------------------------------------------------------------------------
10. # tuple()  function  demo  program   (Home  work)
a = range(100 , 150 , 10)
b = tuple(a) # (100 , 110 , 120 , 130 , 140)
print(b)     # (100 , 110 , 120 , 130 , 140)
print(type(b)) # <class 'tuple'>
c = [10 , 20 , 15, 18]
d = tuple(c) 
print(d)     # (10,20,15,18) 
e = tuple('Vamsi') 
print(e)      # ('V','a','m','s','i')
#print(tuple(25)) #error because tuple argument must not be non-sequence
print(tuple()) #()
------------------------------------------------------------------------------------------------------
11. #index()  and  count()  methods  demo  program   
a = (10 , 20 , 15 , 12 , 14 , 15 , 18 , 19 , 15 , 12 , 25)
#     0    1    2    3    4    5    6    7    8    9   10
try:
	i = a . index(15)
	while  True:
		print('15 is found at index : ' , i)
		i = a . index(15 , i + 1)
except:
		print(F'15  is  found  {a . count(15)}  times')

OP-
15 is found at index :  2
15 is found at index :  5
15 is found at index :  8
15  is  found  3  times
---------------------------------------------------------------------------------------------------
12. #  How  to  modify  an  element  of  tuple ?  
a  =  10 ,  20 ,  30 ,   40 ,  50
#      0     1     2      3     4
#a[2] = 35 error - cannot modify tuple
print(a)     # (10 ,  20 ,  30 ,   40 ,  50)
print(id(a)) # 2184053037056
-----------------------------------------------------------------------------------------------------
13. #How  to  modify  30  in  tuple  to  35
a = list(a)
a[2]=35
a=tuple(a)
print(a)     # (10 ,  20 ,  30 ,   40 ,  50)
print(id(a)) # 2184053240384
-------------------------------------------------------------------------------------------------
14. # How  to  delete  an  element  of  tuple ?  
a  = 10 , 20 , 30 , 40 , 50
#     0    1    2    3    4
#a . remove(30) #error- tuple does not have remove method
#del  a[2]      # error - cannot delete item from tuple because it is immutable
#a . pop(2)      #error - tuple does not have pop method
print(a)          #(10 , 20 , 30 , 40 , 50)
print(id(a))      # 2683168462848
#How  to  remove  30  from  tuple  'a'
a=list(a)
a.remove(30)
a=tuple(a)
print(a)         #(10 , 20 , 40 , 50)
print(id(a))     # 2683168666096
------------------------------------------------------------------------------------------------
15. #  Nested   tuple 
a = ( (10 , 20)  ,  (30 , 40 , 50)  ,  (60 , 70 , 80 , 90) )
print(a)  #( (10 , 20)  ,  (30 , 40 , 50)  ,  (60 , 70 , 80 , 90) )
print(type(a)) #<class 'tuple'>
print(len(a))  #3
print(a[0]) #How  to  print  1st  inner  tuple
print(a[1]) #How  to  print  2nd  inner  tuple
print(a[2]) #How  to  print  3rd  inner  tuple
print(a[0][1]) #How  to  print  20
print(a[1][2]) #How  to  print  50
print(a[2][3]) #How  to  print  90
----------------------------------------------------------------------------------------------
16. # Find  outputs  (Home  work)
a = ((10 , 20 , 30),)
print(a[0]) #How  to   print  inner  tuple) ------->(10 , 20 , 30)
print(*a) #How  to   print  inner  tuple  in  another  way) --->(10 , 20 , 30)
print(a[0][0]) #How   to  print   10) ----->10
print(a[0][1]) #How   to  print   20) ----->20
print(a[0][2]) #How   to  print   30) ----->30
b = ((),)
print(b[0]) #How  to   print  inner  tuple  of  tuple  'b') ---->()
print(*b) #How  to   print  inner  tuple  of  tuple  'b'  in  another  way)---->()
------------------------------------------------------------------------------------------
17. #  Find  outputs (Home  work)
a = ((10 , 20 , 30))
print(a) #(10 , 20 , 30)
print(*a) #10 , 20 , 30
b = (())
print(b)  #()
print(*b) # empty
----------------------------------------------------------------------------------------------------
18. # What  are  the  outputs  if  input  is  {10 , 20 , 15 , 18 , 20 , 12 , 18}
a = input('Enter  Set  :  ')
print(a) # {10 , 20 , 15 , 18 , 20 , 12 , 18}
print(type(a)) #<class 'str'>
b = eval(a)  
print(b)  # {10 , 20 , 15 , 18 , 12}
print(type(b)) #<class 'set'>
--------------------------------------------------------------------------------------------------------
19. #  Find  outputs  (Home  work)
print({(10 , 20 , 30)})  # {(10 , 20 , 30)}
#print({[10 , 20 , 30]})  # error because set should not contain mutable objects - list is mutable
#print({{10 , 20 , 30}})  # error - set should not contain mutable objects - set is mutable
print({{}})               #  error - dict is mutable
-------------------------------------------------------------------------------------------------------
20. # How  to  print  set  in  differnet ways  (Home  work)
a = {25 , True , 'Hyd' , 10.8}
print('set  with  print  function')
print(a) # {25 , True , 'Hyd' , 10.8}
print('Iterate  elements  of  set  with  for  loop')
for x in a:
	print(x)
---------------------------------------------------------------------------------
21. # Find  outputs  (Home  work)
a = 'Hyd'
b = True
c = 25
d = 1
e = 'Hyd'
s = {a , b , c , d , e}
print(s) # {'Hyd',25,1}
print(len(s)) # 3
print(type(s)) # <class 'set'>
---------------------------------------------------------------------------------
22. # Find  outputs  (Home  work)
s = {'Hyd',  25,  True,  10.8 }
print(s) #{'Hyd',  25,  True,  10.8 }
a , b , c , d = s
print(a) #'Hyd'
print(b) #25
print(c) #True
print(d) #10.8
-----------------------------------------------------------------------------------
23. # Find  outputs  (Home  work)
s = {'Hyd',  25,  True,  10.8 }
print(s) #{25,'Hyd',True,10.8}
a , *b = s 
print(a) # #25
print(b) # ['Hyd',True,10.8] 
print(type(b)) # <class 'List'>
----------------------------------------------------------------------------------------
24. # Find  outputs  (Home  work)
s = {'Hyd',  25,  True,  10.8 }
print(s) #{25,10.8,True,'Hyd'}
a , *b , c = s
print(a) # 25
print(b) # [10.8,True]
print(c) # 'Hyd'
---------------------------------------------------------------------------------------
25. # Find  outputs  (Home  work)
s = {20 , 10 , 20 , 10}
print(s) #{20,10}
x , y = s
print(x) # 20
print(y) #10
-----------------------------------------------------------------------------------------
26. # set()  function  demo  program  (Home  work)
a = range(100 , 151 , 10)
b = set(a)
print(b) #{100,110,120,130,140,150}
c = [10 , 20 , 15 , 18 , 10 , 50 , 20 , 12 , 18]
d = set(c) 
print(d)  #{10,20,15,18,50,12}
e = set('Rama  rAo')
print(e)  #{'a','m',R',' ','r','o','A'}
#print(set(25)) #error- set argument must be sequence  
print(set())   #set()
----------------------------------------------------------------------------------------
27. # add()  method  demo  program  (Home  work)
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
print(a)  #{True,10.8,25,'Hyd',None'}
#a . add(10 , 20 , 30) # error - set must conatin only one argument
#a . add([10,20,30]) #error - set must not contain mutable objects-list
----------------------------------------------------------------------------------------
28. # Find  outputs  (Home  work)
a = {25 , 10.8 , 'Hyd' , True}
tpl = (10 , 20 , 30)
print(a) #{25 , 10.8 , 'Hyd' , True}
print(id(a)) # 2355199279840
a . add(tpl) # {25 , 10.8 , 'Hyd' , True , (10 , 20 , 30)}
a . add('Sec') # {25 , 10.8 , 'Hyd' , True , 'Sec' ,(10 , 20 , 30)}
print(a)     # {25 , 10.8 , 'Hyd' , True , 'Sec' ,(10 , 20 , 30)}
print(id(a)) # 2355199279840
print(len(a)) # 6 
#a . add([100 , 200 , 300]) # error - cannot insert list to set because it is mutable
#a . add(set()) # error- set is mutable
#a . add({ })   #error-dict is mutable
-----------------------------------------------------------------------------------------
29. # Find  outputs (Home  work)
s = set()
tpl = (10 , 20 , 15 , 18)
s . add(tpl) 
print(s)   #{(10,20,15,18)}
print(len(s)) # 1
--------------------------------------------------------------------------------------
30. # update()  method  demo program  (Home  work)
tpl = (10 , 20 , 15, 18 , 10 , 20)
s = set()
s . update(tpl) #{10,20,15,18}
print(len(s))   #4
print(s)        # {10,20,15,18}
#s . update(25)  # error -set argument must be sequence
-------------------------------------------------------------------------------------
31. # Find  outputs  (Home  work)
a = [10 , 20 , 30]
b = {30 , 40,50 }
c = (50 , 60 , 70)
s = set()
s . update(a , b , c) 
print(s)   #{40,50,60,10,20,30,70}
print(len(s))  #7 
#s . add(a , b , c) # error-add argument should not more than one
--------------------------------------------------------------------------------------------
32. # Find  outputs  (Home  work)
a = set()
a . update('Rama Rao')
print(a)  # {'m', 'a', 'R', ' ', 'o'}
print(len(a)) #5
#a . update(3 + 4j , 10.8 , True) # error - arguments are non-sequences cannot update
--------------------------------------------------------------------------------------------
33. # copy()  method  demo  program  (Home  work)
a = {10 , 20 , 15 , 18}
print(a) # {20,10,18,15}
b = a . copy()
print(b) # {20,10,18,15}
print(a  is  b) # False 
print(a  ==  b) # True
c = a            
print(a  is  c) # True
---------------------------------------------------------------------------------------------
34. # remove()  method  demo  program  (Home  work)
a = {25 , 10.8 , 'Hyd' , True}
print(a) #{25 , 10.8 , 'Hyd' , True}
a . remove('Hyd') 
print(a) #{25 , 10.8 , True}
#a . remove('Sec') # error- sec is not there in the set
--------------------------------------------------------------------------------------------------
35. # discard()  method  demo  program (Home  work)
a = {25 , 10.8 , 'Hyd' , True}
print(a)  #{25 , 10.8 , 'Hyd' , True}
a . discard('Hyd') 
print(a)  #{25 , 10.8 , True}
a . discard('Sec')
print(a)  #{25 , 10.8 , True}
a . remove('Sec') #error
----------------------------------------------------------------------------------------------------
36. # clear()  method  demo  program (Home  work)
a = {10 , 20 , 15 , 18}
print(a) #{10 , 20 , 15 , 18}
a . clear()
print(a) #set()
print(len(a)) #0
--------------------------------------------------------------------------------------------------
37. # Find  outputs  (Home work)
a = {10 , 20 , 30 , 40}
b = [30 , 40 , 50 , 60]
print(a . union(b)) #{10,20,30,50,60}
#print(a | b)        #error-| operator can be used to concatenate two sets but not set and list
#print(b . union(a)) #error- list object does not have union method
#print(a + b)         #error - cannot concatinate two different objects with +
