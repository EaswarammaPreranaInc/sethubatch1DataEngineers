# Find  outputs   (Home  work)
a = 25 , 10.8 , 3 + 4j , 'Hyd' , True , None , 'Hyd' , 25
print(a)
print(type(a))
a[3] = 'Sec'
a[3 : 6] = 60 , 70 , 80
#Output
[25, 10.8, (3+4j), 'Hyd', True, None, 'Hyd', 25]
<class 'list'>
[25, 10.8, (3+4j), 60, 70, 80, 'Hyd', 25]

#prgm2
#  What   are  the  outputs  if  input  is  (10 , 20 , 30 , 40) ?   (Home  work)
a = input('Enter  Tuple  :  ')
print(a)
print(type(a))
b = eval(a)
print(b)
print(type(b))
print(len(b))
#Output
(10, 20, 30, 40)
<class 'str'>
(10, 20, 30, 40)
<class 'tuple'>
4

#prgm3
# Find  outputs  (Home  work)
a = (10 , [20 , 30 , 40] , 50 , 60)
a[1][0] = 70
print(a)    #(10, [70, 30, 40], 50, 60)
a[1] = [80 , 90 , 100]
print(a)    #Error
#Output

#prgm4
# Find  outputs  (Home  work)
a = [10 , (20 , 30 , 40) , 50 , 60]
a[1][0] = 70   #TypeError: 'tuple' object does not support item assignment
print(a)
a[1] = [80 , 90]
print(a)

#prgm5
# Find  outputs   (Home  work)
a = 25
b = 10.8
c = 'Hyd'
d = True
x = a , b , c , d
print(x)        #(25, 10.8, 'Hyd', True)
print(type(x))  #<class 'tuple'>

#prgm6
# Find  outputs   (Home  work)
x = 25 , 10.8 , 'Hyd' , True
a , b , c , d = x
print(a) #25
print(b) #10.8
print(c) #'Hyd'
print(d) #True
p , q , r =  x   	    #ValueError: too many values to unpack (expected 3)
a , b , c , d  , e = x  #ValueError: not enough values to unpack (expected 5, got 4)

#prgm7
# Find  outputs   (Home  work)
x = 25 , 10.8 , 'Hyd' , True
a , *b , c = x
print(a)   #25
print(b)   #[10.8 , 'Hyd']
print(c)   #True

#prgm8
# Find  outputs   (Home  work)
tpl = 25 , 10.8 , 'Hyd' , True
a , b , *c , d , e = tpl  #Error
print(a)   #Error
print(b)   #Error
print(c)   #Error
print(d)   #Error
print(e)   #Error

#prgm9
# Find  outputs   (Home  work)
x = 25 , 10.8 , 'Hyd' , True , 3 + 4j
a , b , _ , d , _= x
print(a)    # 25
print(b)    # 10.8
print(_)    # 'Hyd'
print(d)    # True
print(_)    # 3 + 4j

#prgm10
# tuple()  function  demo  program   (Home  work)
a = range(100 , 150 , 10)
b = tuple(a)
print(b)        #(100, 110, 120, 130, 140)
print(type(b))  #<class 'tuple'>
c = [10 , 20 , 15, 18]
d = tuple(c)
print(d)        #(10, 20, 15, 18)
e = tuple('Vamsi')
print(e)        # ('V', 'a', 'm', 's', 'i')
print(tuple(25))
print(tuple())  # Error

#prgm11
#index()  and  count()  methods  demo  program   (Home  work)
a = (10 , 20 , 15 , 12 , 14 , 15 , 18 , 19 , 15 , 12 , 25)
#     0    1      2     3    4     5     6    7     8    9    10
try:
	i = a . index(15)
	while  True:
		print('15 is found at index : ' , i)
		i = a . index(15 , i + 1)
except:
		print(F'15  is  found  {a . count(15)}  times')
# Output
15 is found at index: 2
15 is found at index: 5
15 is found at index: 8
15 is found 3 times

#prgm12
#  How  to  modify  an  element  of  tuple ?    (Home  work)
a  =  10 ,  20 ,  30 ,   40 ,  50
#     0      1       2       3      4
a[2] = 35
print(a)
print(id(a))
How  to  modify  30  in  tuple  to  35
print(a)       # (10, 20, 35, 40, 50)
print(id(a))   #(A new memory address, different from the original tuple's address.)

#prgm13
# How  to  delete  an  element  of  tuple ?   (Home  work)
a  = 10 , 20 , 30 , 40 , 50
#    0     1      2     3      4
a . remove(30)
del  a[2]
a . pop(2)
print(a)  	  #(10, 20, 40, 50)
print(id(a))  #(A new memory address, different from the original tuple's address.)
How  to  remove  30  from  tuple  'a'
print(a)

#prgm14
# Nested tuple example
a = ((10, 20), (30, 40, 50), (60, 70, 80, 90))

# Print the entire nested tuple
print("Nested tuple:", a)
print("Type of 'a':", type(a))
print("Length of 'a':", len(a))
# Print each inner tuple
print("\n1st inner tuple:", a[0])
print("2nd inner tuple:", a[1])
print("3rd inner tuple:", a[2])
# Access specific elements in the nested tuple
print("\nElement 20:", a[0][1])
print("Element 50:", a[1][2])
print("Element 90:", a[2][3])

#output
Nested tuple: ((10, 20), (30, 40, 50), (60, 70, 80, 90))
Type of 'a': <class 'tuple'>
Length of 'a': 3
1st inner tuple: (10, 20)
2nd inner tuple: (30, 40, 50)
3rd inner tuple: (60, 70, 80, 90)
Element 20: 20
Element 50: 50
Element 90: 90

#prgm15
# Example 1: Tuple with one inner tuple
a = ((10, 20, 30),)
print("Inner tuple of 'a':", a[0])
inner_tuple = a[0]
print("Inner tuple of 'a' (another way):", inner_tuple)
print("Element 10:", a[0][0])
print("Element 20:", a[0][1])
print("Element 30:", a[0][2])
b = ((),)
print("\nInner tuple of 'b':", b[0])
inner_tuple_b = b[0]
print("Inner tuple of 'b' (another way):", inner_tuple_b)

#output
Inner tuple of 'a': (10, 20, 30)
Inner tuple of 'a' (another way): (10, 20, 30)
Element 10: 10
Element 20: 20
Element 30: 30
Inner tuple of 'b': ()
Inner tuple of 'b' (another way): ()

#prgm16
#  Find  outputs (Home  work)
a = ((10 , 20 , 30))
print(a)  	#(10, 20, 30)
print(*a)   #10 20 30
b = (())
print(b)    #()
print(*b)

#prgm17
# What  are  the  outputs  if  input  is  {10 , 20 , 15 , 18 , 20 , 12 , 18}
a = input('Enter  Set  :  ')
print(a)     	#{10, 20, 15, 18, 20, 12, 18}
print(type(a))  #<class 'str'>
b = eval(a)
print(b)       	#{10, 12, 15, 18, 20}
print(type(b)) 	#<class 'set'>

#prgm18
#  Find  outputs  (Home  work)
print({(10 , 20 , 30)})  #{(10, 20, 30)}
print({[10 , 20 , 30]})  # Error
print({{10 , 20 , 30}})  # Error
print({{}})              # Error

#prgm19
# How  to  print  set  in  differnet ways
a = {25, True, 'Hyd', 10.8}
print("Set with print function:")
print(a)
print("\nIterate elements of set with for loop:")
for i in a:
    print(i)
#OUTPUT
Set with print function:
{True, 10.8, 'Hyd', 25}
Iterate elements of set with for loop:
True
10.8
Hyd
25

#prgm20
# Find  outputs  (Home  work)
a = 'Hyd'
b = True
c = 25
d = 1
e = 'Hyd'
s = {a , b , c , d , e}
print(s)      	#{True, 'Hyd', 25}
print(len(s))   #3
print(type(s))  #<class 'set'>

#prgm21
# Find  outputs  (Home  work)
s = {'Hyd',  25,  True,  10.8 }
print(s)    	#{True, 10.8, 'Hyd', 25}
a , b , c , d = s
print(a)       #True
print(b)       #10.8
print(c)       #'Hyd'
print(d)       #25

#prgm22
# Find  outputs  (Home  work)
s = {'Hyd',  25,  True,  10.8 }
print(s)         #{True, 10.8, 'Hyd', 25}
a , *b = s
print(a)         #True
print(b) 	     #[10.8, 'Hyd', 25]
print(type(b))   #<class 'list'>

#prgm23
# Find  outputs  (Home  work)
s = {'Hyd',  25,  True,  10.8 }
print(s)   	#{True, 10.8, 'Hyd', 25}
a , *b , c = s
print(a)   	#True
print(b)    #10.8, 'Hyd']
print(c)    #25

#prgm24
# Find  outputs  (Home  work)
s = {20 , 10 , 20 , 10}
print(s)   #{10, 20}
x , y = s
print(x)   #10
print(y)   #20

#prgm25
# set()  function  demo  program  (Home  work)
a = range(100 , 151 , 10)
b = set(a) 
print(b)        # {100, 110, 120, 130, 140, 150}
c = [10 , 20 , 15 , 18 , 10 , 50 , 20 , 12 , 18]
d = set(c)
print(d)  	    # {10, 12, 15, 18, 20, 50}
e = set('Rama  rAo')
print(e)        # {' ', 'A', 'R', 'a', 'm', 'o', 'r'}
print(set(25))  # TypeError: 'int' object is not iterable
print(set()) 	# set()

#prgm26
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
print(a)                #{True, 10.8, 'Hyd', 25, None}
a . add(10 , 20 , 30)   #TypeError: add() takes exactly one argument (3 given)
a . add([10,20,30])     #TypeError: unhashable type: 'list'

#prgm27
# Find  outputs  (Home  work)
a = {25 , 10.8 , 'Hyd' , True}
tpl = (10 , 20 , 30)
print(a)    	#{True, 10.8, 'Hyd', 25}
print(id(a))    #(Memory address of set a)
a . add(tpl)
a . add('Sec')
print(a)        #{True, 10.8, 'Hyd', 25, (10, 20, 30), 'Sec'}
print(id(a))    	
print(len(a))   	#6
a . add([100 , 200 , 300]) 	#TypeError: unhashable type: 'list'
a . add(set())              #TypeError: unhashable type: 'list'
a . add({ })                #TypeError: unhashable type: 'dict'

#prgm28
# Find  outputs (Home  work)
s = set()
tpl = (10 , 20 , 15 , 18)
s . add(tpl)
print(s)       #{(10, 20, 15, 18)}
print(len(s))   #1

#prgm29
# update()  method  demo program  (Home  work)
tpl = (10 , 20 , 15, 18 , 10 , 20)
s = set()
s . update(tpl)
print(len(s))     #4
print(s)          #{10, 20, 15, 18}
s . update(25)    #TypeError: 'int' object is not iterable

#prgm30
# Find  outputs  (Home  work)
a = [10 , 20 , 30]
b = {30 , 40,50 }
c = (50 , 60 , 70)
s = set()
s . update(a , b , c)
print(s)    	    # {10, 20, 30, 40, 50, 60, 70}
print(len(s))       # 7
s . add(a , b , c)  #TypeError

#prgm31
# Find  outputs  (Home  work)
a = set()
a . update('Rama Rao')
print(a)    	#{'R', 'a', 'm', ' ', 'o'}
print(len(a))   #5
a . update(3 + 4j , 10.8 , True)

#prgm32
# copy()  method  demo  program  (Home  work)
a = {10 , 20 , 15 , 18}
print(a)       	 #{10, 20, 15, 18}
b = a . copy()
print(b)         #{10, 20, 15, 18}
print(a  is  b)  #False 
print(a  ==  b)  #True
c = a
print(a  is  c)  #True

#prgm33
# remove()  method  demo  program  (Home  work)
a = {25 , 10.8 , 'Hyd' , True}
print(a)          #{25, 10.8, 'Hyd', True}
a . remove('Hyd')
print(a)          #{25, 10.8, True}
a . remove('Sec') #Error

#prgm34
# discard()  method  demo  program (Home  work)
a = {25, 10.8, 'Hyd', True}
print(a)          #{25, 10.8, 'Hyd', True}
a.discard('Hyd')
print(a)          #{25, 10.8, True}
a.discard('Sec')
print(a)          #{25, 10.8, True}
a.remove('Sec')   #Error

#prgm35
# clear()  method  demo  program (Home  work)
a = {10 , 20 , 15 , 18}
print(a)       #{10, 20, 15, 18}
a . clear()
print(a)       #set()
print(len(a))  # 0

#prgm36
# Find  outputs  (Home work)
a = {10 , 20 , 30 , 40}
b = [30 , 40 , 50 , 60]
print(a . union(b))  #{10, 20, 30, 40, 50, 60}
print(a | b)         #{10, 20, 30, 40, 50, 60}
print(b . union(a))  #{10, 20, 30, 40, 50, 60}
print(a + b)         #Error












