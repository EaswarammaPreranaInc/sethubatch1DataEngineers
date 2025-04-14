#Ex-1

# Find  outputs   (Home  work)
a = 25 , 10.8 , 3 + 4j , 'Hyd' , True , None , 'Hyd' , 25
print(a)           # (25 , 10.8 , 3 + 4j , 'Hyd' , True , None , 'Hyd' , 25)
print(type(a))    # class tuple
#a[3] = 'Sec'     # Error because tuple immutable
#a[3 : 6]=60,70,80 #   # Error because tuple immutable

print()

#  What   are  the  outputs  if  input  is  (10 , 20 , 30 , 40) ?   (Home  work)
a = input('Enter  Tuple  :  ')
print(a)         #  '(10 , 20 , 30 , 40) '
print(type(a))  # class str
b = eval(a)      # tuple  (10 , 20 , 30 , 40)
print(b)       #  (10 , 20 , 30 , 40)
print(type(b)) # class tuple
print(len(b)) # 4

print()

# Find  outputs  (Home  work)
a = (10 , [20 , 30 , 40] , 50 , 60)
a[1][0] = 70   # tuple inside list is mutable can be modified (10 , [70, 30 , 40] , 50 , 60)
print(a) (10, [70, 30, 40], 50, 60)
#a[1] = [80,90,100]  #  # Error because tuple immutable
print(a) #(10, [70, 30, 40], 50, 60)


# Find  outputs  (Home  work)
a = [10 , (20 , 30 , 40) , 50 , 60]
#a[1][0] = 70      # Error because list inside tuple is immutable
print(a) # [10 , (20 , 30 , 40) , 50 , 60]
a[1] = [80,90] # (20 , 30 , 40) tuple is modified to list [80,90]
print(a) # [10, [80, 90], 50, 60]


# Find  outputs   (Home  work)
a = 25
b = 10.8
c = 'Hyd'
d = True
x = a , b , c , d # x is tuple because () is optional so x is tuple
print(x)  # (25, 10.8, 'Hyd', True)
print(type(x)) # class tuple

print()

# Find  outputs   (Home  work)
x = 25 , 10.8 , 'Hyd' , True # x is tuple
a , b , c , d = x
print(a)  # 25
print(b)  # 10.8
print(c) # 'Hyd'
print(d) #True
#p , q , r =  x  # error because tuple cal 4 elements but left side can have 3 references
#a , b ,c,d,e=x  # error because tuple cal 4 elements but left side can have 5 references

print()

# Find  outputs   (Home  work)
x = 25 , 10.8 , 'Hyd' , True
a , *b , c = x # a = 25, c= True b = [10.8,'Hyd']
print(a) # 25
print(b) # [10.8,'Hyd']
print(c) # True
print()

# Find  outputs   (Home  work)
tpl = 25 , 10.8 , 'Hyd' , True
a , b , *c , d , e = tpl  # x # a = 25,  b = 10.8, d = 'Hyd' c [] ,e = True
print(a) # 25
print(b) # 10.8
print(c) # []
print(d) # 'Hyd'
print(e) # True
print()

# Find  outputs   (Home  work)
x = 25 , 10.8 , 'Hyd' , True , 3 + 4j
a , b , _ , d , _= x   # a = 25,  b = 10.8, _ = 'Hyd' d = True _ = 3+4j
print(a) # 25
print(b) # 10.8
print(_) # 3+4j
print(d) # True
print(_) # 3+4j
print()


# tuple()  function  demo  program   (Home  work)
a = range(100 , 150 , 10) # 100 ,110,120,130,140
b = tuple(a) #  converts range object to tuple (100 ,110,120,130,140)
print(b) # (100 ,110,120,130,140)
print(type(b))
c = [10 , 20 , 15, 18]
d = tuple(c) # converts to list to tuple (10 , 20 , 15, 18)
print(d) # (10 , 20 , 15, 18)
e = tuple('Vamsi') # converts sequence to list characters ('V','a','s','i')
print(e) # ('V','a','s','i')
#print(tuple(25)) # 25 is not sequence
print(tuple()) # empty tuple ()



#index()  and  count()  methods  demo  program   (Home  work)
a = (10 , 20 , 15 , 12 , 14 , 15 , 18 , 19 , 15 , 12 , 25)
#     0    1      2     3    4     5     6    7     8    9    10
try:
	i = a . index(15)
	while  True:
		print('15 is found at index : ' , i)
		i = a . index(15 , i + 1)
except:
		print(F'15  is  found  {a . count(15)} times')

print()


#  How  to  modify  an  element  of  tuple ?    (Home  work)
a  =  10 ,  20 ,  30 ,   40 ,  50
#     0      1       2       3      4
#a[2] = 35 error because tuple immutable
print(a) # (10, 20, 30, 40, 50)
print(id(a)) # some address 1000
a = a[:2]+(35,)+a[3:]#How  to  modify  30  in  tuple  to  35
print(a) # (10, 20, 35, 40, 50)
print(id(a)) # some address 2000
print()

# How  to  delete  an  element  of  tuple ?   (Home  work)
a  = 10 , 20 , 30 , 40 , 50
#    0     1      2     3      4
#a . remove(30) # Error there is no remove() method in tuple
#del  a[2] #  Error because delete entire tuple but not single element
#a . pop(2) #  Error there is no pop() method in tuple
print(a) # (10, 20, 30, 40, 50)
print(id(a)) # some address 1000
a=a[:2]+a[3:]#How  to  remove  30  from  tuple  'a'  # it will create new tuple  reference modified
print(a) # (10, 20, 40, 50)
print(id(a)) # some address may be 2000
print()

#  Nested   tuple  (Home  work)
a = ( (10 , 20)  ,  (30 , 40 , 50)  ,  (60 , 70 , 80 , 90) )
print(a) # ( (10 , 20)  ,  (30 , 40 , 50)  ,  (60 , 70 , 80 , 90) )
print(type(a)) # class tuple
print(len(a)) # 3
print(a[0]) #How  to  print  1st  inner  tuple)
print(a[1]) #How  to  print  2nd  inner  tuple)
print(a[2]) # How  to  print  3rd  inner  tuple)
print(a[0][1])   # How  to  print  20)
print(a[1][2]) #How  to  print  50)
print(a[2][3]) #How  to print 90)
print()

# Find  outputs  (Home  work)
a = ((10 , 20 , 30),)
print(a[0])#How  to   print  inner  tuple)
print(a[0:][0]) #How  to   print  inner  tuple  in  another  way)
print(a[0][0]) #How   to  print   10)
print(a[0][1]) #How   to  print   20)
print(a[0][2]) #How   to  print   30)
b = ((),)
print(b[0]) #How  to   print  inner  tuple  of  tuple  'b')
print(b[0:][0]) #How  to   print  inner  tuple  of  tuple  'b'  in another way)
print()


#  Find  outputs (Home  work)
a = ((10 , 20 , 30))
print(a) # ((10 , 20 , 30))
print(*a) # unpacking inside tuple 10 20 30
b = (())
print(b) # empty tuple
print(*b) # nothing because tuple does not have any element
print()

# What  are  the  outputs  if  input  is  {10 , 20 , 15 , 18 , 20 , 12 , 18}
a = input('Enter  Set  :  ')
print(a) # {10 , 20 , 15 , 18 , 20 , 12 , 18}
print(type(a)) # class str
b = eval(a)  # eval fun convert appropriate object {10 , 20 , 15 , 18 , 20 , 12 , 18}
print(b) # {10 , 20 , 15 , 18 , 20 , 12 , 18}
print(type(b)) # class set
print()

#  Find  outputs  (Home  work)
# How  to  print  set  in  differnet ways  (Home  work)
a = {25 , True , 'Hyd' , 10.8}
print('set  with  print  function')
print(a)
print('Iterate  elements  of  set  with  for  loop')
for x in a:
    print(x) #How  to  iterate  set with for loop
print()


# Find  outputs  (Home  work)
a = 'Hyd'
b = True
c = 25
d = 1
e = 'Hyd'
s = {a , b , c , d , e} # {'Hyd',True,25,1,'Hyd'} but takes unique elements
print(s) #  set is unordered  {True,25,,'Hyd'}
print(len(s)) # 3
print(type(s)) # class set

# Find  outputs  (Home  work)
s = {'Hyd',  25,  True,  10.8 }
print(s) # #  set is unordered we can not guess the output
a , b , c , d = s
print(a) #  set is unordered we can not guess a value
print(b) #  set is unordered we can not guess b value
print(c) #  set is unordered we can not guess c value
print(d) #  set is unordered we can not guess d value
print()

# Find  outputs  (Home  work)
s = {'Hyd',  25,  True,  10.8 }
print(s)
a , *b = s  #  set is unordered
print(a) # we can't guess a value
print(b) # we can't guess b value
print(type(b)) # class list
print()

#Find  outputs  (Home  work)
s = {'Hyd',  25,  True,  10.8 }
print(s) # set is unordered
a , *b , c = s  # we can't guess b value
print(a) # we can't guess a value
print(b) # we can't guess b value
print(c) # we can't guess c value
print()

# Find  outputs  (Home  work)
s = {20 , 10 , 20 , 10}
print(s) # set is unordered  we can't guess
x , y = s # we can't guess x and y value
print(x)  # we can't guess x value
print(y) # we can't guess y value
print()


# set()  function  demo  program  (Home  work)
a = range(100 , 151 , 10) # 100 ,110, 120, 130, 140, 150
b = set(a) # range object converts set
print(b) # {100 ,110, 120, 130, 140, 150}
c = [10 , 20 , 15 , 18 , 10 , 50 , 20 , 12 , 18]
d = set(c) # convert list to set and also can not contain duplicates elements
print(d) #{10 , 20 , 15 , 18 , 10 , 50 , 20 , 12 , 18}
e = set('Rama  rAo') # converts str to set {'R','a','m',' ','r','A','o'}
print(e)
#print(set(25)) # Error because 25 is non-sequence
print(set()) # empty set set()
print()

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
print(a) # set is unordered we can not guess
#a . add(10 , 20 , 30) # add method take single argument only
#a . add([10,20,30]) # set contain only immutable elements  ,list is mutable


# Find  outputs  (Home  work)
a = {25 , 10.8 , 'Hyd' , True}
tpl = (10 , 20 , 30)
print(a) # set is unordered we can not guess
print(id(a)) # some random address may be 1000
a . add(tpl) # tuple is added to set {25 , 10.8 , 'Hyd' , True, (10 , 20 , 30)}
a . add('Sec') # 'Sec' is added to set {25 , 10.8 , 'Hyd' , True, (10 , 20 , 30),'Sec'}
print(a) # set is unordered we can not guess
print(id(a)) # same address 1000
print(len(a))  # we can not guess
#a . add([100 , 200 , 300]) # set contain only immutable elements  ,list is mutable
#a . add(set()) # Error because nested set because set is mutable
#a.add({}) # empty dict  Error dict
print()


# Find  outputs (Home  work)
s = set() # empty set
tpl = (10 , 20 , 15 , 18)
s . add(tpl) # tpl is added to set {(10 , 20 , 15 , 18)}
print(s) #  # set is unordered we can not guess
print(len(s)) # we can not guess
print()


# update()  method  demo program  (Home  work)
tpl = (10 , 20 , 15, 18 , 10 , 20)
s = set() # empty set
s . update(tpl) #(10 , 20 , 15, 18 , 10 , 20) set contain unique elements (10,20,15,18)
print(len(s)) # 4
print(s) # set contain unique elements (10,20,15,18)
#s . update(25) # 25 is non sequence but arg must be sequence
print()

# Find  outputs  (Home  work)
a = [10 , 20 , 30]
b = {30 , 40,50 }
c = (50 , 60 , 70)
s = set()
s . update(a , b , c) # update method take more than one argument #{10,20,30,40,50,60,70}
print(s) # # we can not guess
print(len(s)) # 7
#s .add(a,b,c) # error because add method can take only one argument
print()


# Find  outputs  (Home  work)
a = set() # empty
a . update('Rama Rao') # added to set {'R','a','m',' ','o'}
print(a) # {'R','a','m',' ','R','o'}
print(len(a)) # 5
# a . update(3 + 4j,10,True) # Error because non-sequence object not iterable
print()

# copy()  method  demo  program  (Home  work)
a = {10 , 20 , 15 , 18}
print(a) # {10 , 20 , 15 , 18}
b = a . copy() # value copies form a to b {10 , 20 , 15 , 18}
print(b) # {10 , 20 , 15 , 18}
print(a  is  b)  # False
print(a  ==  b) # True
c = a
print(a  is  c) # True
print()


# remove()  method  demo  program  (Home  work)
a = {25 , 10.8 , 'Hyd' , True}
print(a) # {25 , 10.8 , 'Hyd' , True}
a . remove('Hyd') # remove 'Hyd' from set a
print(a) #  {25 , 10.8 , True}
#a . remove('Sec') # error 'Sec' is not present in a set
print()

# discard()  method  demo  program (Home  work)
a = {25 , 10.8 , 'Hyd' , True}
print(a) # {25 , 10.8 , 'Hyd' , True}
a . discard('Hyd') # removes "Hyd'
print(a) # {25 , 10.8 ,True}
a . discard('Sec') # 'Sec' is not present in a set discard method doest not throw an error
print(a)
#a . remove('Sec') # error 'Sec' is not present in a set
print()


# clear()  method  demo  program (Home  work)
a = {10 , 20 , 15 , 18}
print(a) # {10 , 20 , 15 , 18}
a . clear() # remove all elements present set a
print(a) # set()
print(len(a)) # 0
print()


# Find  outputs  (Home work)
a = {10 , 20 , 30 , 40}
b = [30 , 40 , 50 , 60]
print(a . union(b)) #{10,20,30,40,50,60}
#print(a | b) # | pipe operator work only two sets
#print(b . union(a)) # list doest not have union() method
#print(a+b) # can't concat set and list
