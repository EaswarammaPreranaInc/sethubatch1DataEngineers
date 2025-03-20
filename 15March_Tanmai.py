
# 1.Find  outputs   (Home  work)
a = 25 , 10.8 , 3 + 4j , 'Hyd' , True , None , 'Hyd' , 25
print(a) #25 , 10.8 , 3 + 4j , 'Hyd' , True , None , 'Hyd' , 25
print(type(a))#Class Tuple
#a[3] = 'Sec'# Error its immutable  'tuple' object does not support item assignment
#a[3 : 6] = 60 , 70 , 80 #Error cant be modified 

# 2. What   are  the  outputs  if  input  is  (10 , 20 , 30 , 40) ?   (Home  work)
a = input('Enter  Tuple  :  ') 
print(a)#'( <tuple>)' str of tuple
print(type(a))# class str
b = eval(a)
print(b)#tuple 
print(type(b))# class Tuple
print(len(b))# no .of of tuple elements  

# 3. * Find  outputs  (Home  work)
a = (10 , [20 , 30 , 40] , 50 , 60)
a[1][0] = 70 #Error
print(a)# (10 , [70 , 30 , 40] , 50 , 60)
#a[1] = [80 , 90 , 100] Error 
#print(a) 

# 4. Find  outputs  (Home  work)
a = [10 , (20 , 30 , 40) , 50 , 60]
#a[1][0] = 70 # tuple is imuttable 
print(a)# [10 , (20 , 30 , 40) , 50 , 60]
a[1] = [80 , 90]
print(a)#[10,[80,90],50,60]

# 5.  Find  outputs   (Home  work)
a = 25
b = 10.8
c = 'Hyd'
d = True
x = a , b , c , d
print(x)#25,10.8,'Hyd',True
print(type(x))#class Tuple  

# 6.Find  outputs   (Home  work)
x = 25 , 10.8 , 'Hyd' , True
a , b , c , d = x
print(a)#25
print(b)#10.8
print(c)#'Hyd'
print(d)#True
#p , q , r =  x #too many values to unpack
#a , b , c , d  , e = x # not enough values to unpack 

# 7. Find  outputs   (Home  work)
x = 25 , 10.8 , 'Hyd' , True
a , *b , c = x
print(a)#25
print(b)#[10.8,'Hyd']
print(c)#True
 
# 8. Find  outputs   (Home  work)
tpl = 25 , 10.8 , 'Hyd' , True
a , b , *c , d , e = tpl 
print(a) # 25
print(b)#10.8
print(c)#[]
print(d)#'Hyd'
print(e)#True 

# 9. Find  outputs   (Home  work)
x = 25 , 10.8 , 'Hyd' , True , 3 + 4j
a , b , _ , d , _= x
print(a)#25
print(b)#10.8
print(_)#(3+4j)
print(d)#True
print(_)#(3+4j)

# 10. tuple()  function  demo  program   (Home  work)
a = range(100 , 150 , 10)
b = tuple(a)
print(b)#(100,110,120,130,140)
print(type(b))#Class<Tuple>
c = [10 , 20 , 15, 18]
d = tuple(c)
print(d)#(10,20,15,18)
e = tuple('Vamsi')
print(e)#('V', 'a', 'm', 's', 'i')
#print(tuple(25))# Error 
print(tuple())#()


'''
tuple()  function
--------------------
1) What  does  tuple(sequence)  do  ?  ---> Converts  sequence  to  tuple

2) What  does  tuple(No-args)  do  ?  --->  Returns  an  empty  tuple

3) Is  tuple(non-sequence)  valid ?  --->  No  becoz  argument  should  be  sequence  only

4) How  many  arguments  can  tuple()  function  take ?  --->  1 (or)  none  but  not  more  than  one
'''

# 11. index()  and  count()  methods  demo  program   (Home  work)
a = (10 , 20 , 15 , 12 , 14 , 15 , 18 , 19 , 15 , 12 , 25)
#     0    1    2     3    4   5     6   7     8    9    10
try:
	i = a . index(15)
	while  True:
		print('15 is found at index : ' , i)
		i = a . index(15 , i + 1)
except:
		print(F'15  is  found  {a . count(15)}  times') 
#  12. How  to  modify  an  element  of  tuple ?    (Home  work)
a  =  10 ,  20 ,  30 ,   40 ,  50
#     0      1       2       3      4
#a[2] = 35 #Error Tuple is immutable
print(a) #(10,20,30,40,50)
print(id(a)) # Address of a 

a= a[:2]+(35,)+a[2:]
#How  to  modify  30  in  tuple  to  35
print(a)#(10, 20, 35, 30, 40, 50)
print(id(a))# different address 


# 13. How  to  delete  an  element  of  tuple ?   (Home  work)
a  = 10 , 20 , 30 , 40 , 50
#    0     1    2     3      4
#a . remove(30) #error no remove method in tuple class
#del  a[2] # can't modify tuple elements 
#a . pop(2)# no pop method  in tuple class
print(a)#(10,20,30,40,50)
print(id(a)) # address of a 
#How  to  remove  30  from  tuple  'a'
a=a[:2]+a[3:]
print(a) #(10,20,40,50)
print(id(a))# a has new address

# 14. Nested   tuple  (Home  work)
a = ( (10 , 20)  ,  (30 , 40 , 50)  ,  (60 , 70 , 80 , 90) )
print(a) #( (10 , 20)  ,  (30 , 40 , 50)  ,  (60 , 70 , 80 , 90) )
print(type(a)) # class<Tuple>
print(len(a))#3
print(a[0])#(How  to  print  1st  inner  tuple)
print(a[1])#(How  to  print  2nd  inner  tuple)
print(a[2])#(How  to  print  3rd  inner  tuple)
print(a[0][1])#(How  to  print  20)
print(a[1][2])#(How  to  print  50)
print(a[2][3])#(How  to  print  90) 

# 15. Find  outputs  (Home  work)
a = ((10 , 20 , 30),)# Nested tuple 
print(a[0])#(How  to   print  inner  tuple)
print(*a)#(How  to   print  inner  tuple  in  another  way)
print(a[0][0])#(How   to  print   10)
print(a[0][1])#(How   to  print   20)
print(a[0][2])#(How   to  print   30)
b = ((),) # Nested tuple 
print(b[0]) #(How  to   print  inner  tuple  of  tuple  'b')
print(*b) #(How  to   print  inner  tuple  of  tuple  'b'  in  another  way)


# 16. Find  outputs (Home  work)
a = ((10 , 20 , 30)) # its a regular tuple bcz no comma
print(a)#(10 , 20 , 30)
print(*a)#10  20  30
b = (())# its a regular tuple bcz no comma
print(b)#()
print(*b)#Empty 

# 17. What  are  the  outputs  if  input  is  {10 , 20 , 15 , 18 , 20 , 12 , 18}
a = input('Enter  Set  :  ')
print(a) #'{10 , 20 , 15 , 18 , 20,12,18}'
print(type(a))# class<Str>
b = eval(a) 
print(b) #{10 , 20 , 15 , 18 , 12}
print(type(b)) #class  <set> 

# 18. Find  outputs  (Home  work)
print({(10 , 20 , 30)}) #{(10 , 20 , 30)}
#print({[10 , 20 , 30]}) # Error set cant have list inside it bcz set cant hold immutable elements 
#print({{10 , 20 , 30}}) # Error  nested set not possible
#print({{}}) # {{}}  error set containing an empty dict 

# 19. How  to  print  set  in  differnet ways  (Home  work)
a = {25 , True , 'Hyd' , 10.8}
print (a)#('set  with  print  function')
print(a) #{25 , True , 'Hyd' , 10.8}
#print('Iterate  elements  of  set  with  for  loop')
#How  to  iterate  set  with  for  loop

for x in a:
	print(x) 

# 20.  Find  outputs  (Home  work)
a = 'Hyd'
b = True
c = 25
d = 1
e = 'Hyd'
s = {a , b , c , d , e}
print(s) # {'Hyd',True,25}
print(len(s))#3
print(type(s))# class Set

# 21. Find  outputs  (Home  work)
s = {'Hyd',  25,  True,  10.8 }
print(s) # {'Hyd',  25,  True,  10.8 } in any order
a , b , c , d = s
print(a) # 1 st element 
print(b) # 2 element 
print(c) # 3 rd
print(d) # 4 th   

# 22. Find  outputs  (Home  work)
s = {'Hyd',  25,  True,  10.8 }
print(s) #{'Hyd',  25,  True,  10.8 }
a , *b = s
print(a) # 1 st element 
print(b) # [2 nd ,3 rd, 4 th]
print(type(b)) # class list 

# 23.Find  outputs  (Home  work)
s = {'Hyd',  25,  True,  10.8 }
print(s) # {'Hyd',  25,  True,  10.8 }
a , *b , c = s
print(a) #  1s t element 
print(b) # [ 2nd , 3rd elements ]
print(c) # last element 

# 24. Find  outputs  (Home  work)
s = {20 , 10 , 20 , 10}
print(s) # {20,10}
x , y = s
print(x) # 1 st element 
print(y)  # 2 nd  
# 25. set()  function  demo  program  (Home  work)
a = range(100 , 151 , 10)
b = set(a)
print(b) # {100,110,120,130,140,150}
c = [10 , 20 , 15 , 18 , 10 , 50 , 20 , 12 , 18]
d = set(c)
print(d) #{10,20,15,18,50,12} in any order
e = set('Rama  rAo')
print(e) #{'R','a','m','r','A','o',' '}
#print(set(25)) # Error 
print(set()) # set()



'''
set()  function
-----------------
1) What  does  set(sequence)  do ?  --->  Converts  sequence  to  set

2) What  does  set(No-args)  do ?  --->  Returns  an  empty  set

3) How  many  arguments  can  set()  function  take ?  --->  Zero  (or) One  but  not  more  than  one

4) Is  set(non-sequence)  valid ?  --->  No  becoz  argument  should  be  sequence
'''
# 26. add()  method  demo  program  (Home  work)
a = set()
a . add(True) # {True}
a . add(25) # {True,25}
a . add(10.8)# {True,25,10.8}
a . add(1) # {True,25,10.8} 1 not added 
a . add('Hyd') # # {True,25,10.8,'Hyd'}
a . add(25)# {True,25,10.8,'Hyd'}
a . add(None)#{True,25,10.8,'Hyd',None}
a . add('Hyd')
a . add(1.0)
print(a) #{True,25,10.8,'Hyd',None}
#a.add(10,20,30)#added  set.add() takes exactly one argument (3 given)
a . add((10 , 20 , 30)) 
print(a) # tuple is added 
#a . add([10,20,30]) # errpr cant add mutable elements 



'''
add()   method
-----------------
1) What  does  add(x)  do ?  --->  Inserts   'x'  any  where  in  the  set  becoz  set  is  unordered

2) How  many  arguments  can  add()  method  take ?  --->  Single

3) Is  set . add(mutable  object)  valid ? --->  No  becoz  set  can  not  hold  mutable  element

4) In  other  words,  argument  of  add()  method  should  be  immutable  object  only

5) What  does  set .  add(sequence)  do  ?  ---> Inserts  sequence  any  where  in  the  set  but  not  elements  of  sequence
												                          (Like  append()  method  of  list  class)
''' 
# 27. Find  outputs  (Home  work)
a = {25 , 10.8 , 'Hyd' , True}
tpl = (10 , 20 , 30)
print(a) #  {25 , 10.8 , 'Hyd' , True}
print(id(a)) # address of a 
a . add(tpl) # {25 , 10.8 , 'Hyd' , True,(10,20,30)}
a . add('Sec') # {25 , 10.8 , 'Hyd' , True,(10,20,30),Sec}
print(a) # {25 , 10.8 , 'Hyd' , True,(10,20,30),Sec}
print(id(a)) # Same address
print(len(a)) # 6
#a . add([100 , 200 , 300]) # error 
#a . add(set()) # error
#a . add({ }) # error 

# 28. Find  outputs (Home  work)
s = set()
tpl = (10 , 20 , 15 , 18)
s . add(tpl) 
print(s) # {(10 , 20 , 15 , 18)}
print(len(s))# 1  

# 29. update()  method  demo program  (Home  work)
tpl = (10 , 20 , 15, 18 , 10 , 20)
s = set()
s . update(tpl) 
print(len(s)) # 4
print(s)#{10 , 20 , 15, 18 } Any order
#s . update(25) # error 



'''
update()  method
--------------------
1) What  does  update(sequence)  do ?  ---> Inserts  elements  of  sequence  anywhere  in  the  set  but  not  sequence
											                        (Like  extend()  method  of  list  class)

2) Is  update(non-sequnece)  valid ?   --->  No  becoz  agument  should  be  sequence  only

3) How  many  arguments  can  update()  method  take ?  --->  One  (or)  more  than   one
''' 

# 30. Find  outputs  (Home  work)
a = [10 , 20 , 30]
b = {30 , 40,50 }
c = (50 , 60 , 70)
s = set()
s . update(a , b , c)
print(s) #{ 10 , 20 , 30,40,50,60,70}
print(len(s)) #7
#s . add(a , b , c) # error only one argument 

# 31. Find  outputs  (Home  work)
a = set()
a . update('Rama Rao')
print(a) # {'R','a','m',' ','o'}
print(len(a))# 5
# a . update(3 + 4j , 10.8 , True) # nonsequences cant be updated  

# 32. ()  method  demo  program  (Home  work)
a = {10 , 20 , 15 , 18}
print(a) # {10,20,15,18}
b = a . copy() 
print(b) #  {10,20,15,18}
print(a  is  b) # False
print(a  ==  b) # True copies the same set in same sequence .. so values will be in same order 
c = a
print(a  is  c) # True 



'''
1) What  does  copy()  method  do ?  --->  Copies  elements  of  a  set  to  another  set   i.e. Object  copy

2) a = b
    What  does  the  above  statement  do  when  'b'  is   a  set ?  --->   Reference  copy
																										       i.e.  id  is  copied

3) What  is  shallow  clone ?  ---> Reference  copy
     What  is  deep  clone ?  ---> Object  copy
''' 

# 33. remove()  method  demo  program  (Home  work)
a = {25 , 10.8 , 'Hyd' , True}
print(a) # {25 , 10.8 , 'Hyd' , True}
a . remove('Hyd')
print(a) # {25 , 10.8 , True}
# a . remove('Sec') # error  Sec is not found in set 



'''
remove()   method
----------------------
1) What  does  remove(x)  do ?  ---> Removes  'x'  from  the   set

2) What  does  remove(Invalid-element)  do ?  ---> Throws  error

3) What  is  the  argument  of  remove()  method ?  --->  Element  to  be  removed
'''

# 34. discard()  method  demo  program (Home  work)
a = {25 , 10.8 , 'Hyd' , True}
print(a) # {25 , 10.8 , 'Hyd' , True}
a . discard('Hyd')
print(a)#{25 , 10.8 , True}
a . discard('Sec')
print(a) # {25 , 10.8 , True}
#a . remove('Sec') # error 


'''
1) What  does  discard(x)  do ?  --->  Removes  'x'  from  the  set

2) Does  discard(Invalid  element)  throw  error ?  --->  No
'''

# 35.clear()  method  demo  program (Home  work)
a = {10 , 20 , 15 , 18}
print(a) #{10 , 20 , 15 , 18}
a . clear()
print(a)# set()
print(len(a))# 0



'''
What  does  clear()  method  do ?  ---> Removes  all  the  elements  of  set  and  set  becomes  empty
'''

# 36. Find  outputs  (Home work)
a = {10 , 20 , 30 , 40}
b = [30 , 40 , 50 , 60]
print(a . union(b)) # {10,20,30,40,50,60}
#print(a | b) # error
#print(b . union(a)) # list does not have unioin method
#print(a + b) # error 
