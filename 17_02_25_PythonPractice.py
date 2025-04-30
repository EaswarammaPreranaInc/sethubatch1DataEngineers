#  Write  a  program  to  remove  all  15's  from  the  list
a = [10 , 20 , 15 , 18 , 12 , 15 , 19 , 25 , 15 , 14 , 12]
while 15 in a:   # Repeat  until  there  is  no  15  in  the  list:
	a.remove(15)#How  to  remove  each  15  from  the  list
print(a) # [10, 20, 18, 12, 19, 25, 14, 12]
#  Find  outputs  (Home  work)
a = (25 , 10.8 , 'Hyd' , True , 3+4j , None , 'Hyd' , 25)
print(a) # (25 , 10.8 , 'Hyd' , True , 3+4j , None , 'Hyd' , 25)
print(*a) # 25 10.8 Hyd True (3+4j) None Hyd 25
print(type(a)) # <class 'tuple'>
print(len(a)) # 8
print(a[2 : 5]) # ('Hyd', True, (3+4j))
print(*a[2 : 5]) # Hyd True 3+4j
#a[2] = 'Sec' # Error: 'tuple' object does not support item assignment
#a . append('Sec') # Error no method append in tuple
#a . remove('Hyd') # Error no method remove in tuple
b =  10 , 20 , 30
print(b) # (10,20,30)
print(b * 2) # (10,20,30,10,20,30)
c = 40 , 50 , 60,
print(c) # (40,50,60)
print(type(c)) # <class 'tuple'>
# Find  outputs  (Home  work)
a = (25) # 25
b = 25, # (25,)
c = 25 # 25
d = (25,) # (25,)
print(type(a)) # <class 'int'>
print(type(b)) # <class 'tuple'>
print(type(c)) # <class 'int'>
print(type(d)) # <class 'tuple'>
print(a * 4) # 100
print(b * 4) # (25,25,25,25)
print(c * 4) # 100
print(d * 4) # (25,25,25,25)
# tuple()  function  demo  program  (Home  work)
a = tuple('Hyd')
print(a) # ('H','y','d')
print(type(a)) # <class 'tuple'>
print(len(a)) # 3
b = [10 , 20 , 15 , 18]
print(tuple(b)) # (10,20,15,18)
print(tuple(range(5))) # (0,1,2,3,4)
#print(tuple(25)) # error becoz of non sequence 25 ('int' object is not iterable)



# Find  outputs (Home  work)
a = ()
print(type(a)) # <class 'tuple'>
print(a) # ()
print(len(a)) # 0
b = tuple() 
print(b) # ()
print(len(b)) # 0
#  Gift
# Find  outputs (Home  work)
a = (10 , 20 , 30)
print(a) # (10 , 20 , 30)
print(id(a)) # Address of a
a = a * 2
print(a) # (10 , 20 , 30 , 10 , 20 , 30)
print(id(a)) # Address of a changes becoz of new tuple
#  set  object  demo  program  (Home  work)
a = {25 , 10.8 , 'Hyd' , True , 3+4j , None , 25 , 'Hyd'}
print(a) # {25 , 10.8 , 'Hyd' , True , 3+4j , None}
print(type(a)) # <class 'set'>
print(len(a)) #  6
#print(a[2]) # Error becoz no indexxing in set
#print(a[1 : 4]) # Error No Slicing in set becoz no indexes
#a[2] = 'Sec'
#print(a * 2) # Error: unsupported operand type(s) for *: 'set' and 'int'
#print(a * a) # Error: unsupported operand type(s) for *: 'set' and 'set'
# Gift 
# Find  outputs (Home  work)
a = {1 , 'Hyd' , False , True , 0.0 , '' , 1.0 ,  0}
print(a) # {1 , 'Hyd' , False , ''}
print(len(a)) # 4
print(type(a)) # <class 'set'>
#  set()  function demo  program
a = set('Rama rAo')
print(a) # {'R','a','m',' ','r','A','0'}
print(len(a)) # 7
print(set([10 , 20 , 15 , 20])) # {10,20,15} 
print(set((25 , 10.8 , 'Hyd' , 10.8))) # {25,10.8,'Hyd'}
print(set(range(10 , 20 , 3))) # {10,13,16,19}
#print(set(25)) # Error becoz of int is not iterable




#  Gift
# Find  outputs  (Home  work)
a =   [ ]
b =   ( )
c =   { }
d =   set()
print(type(a)) # <class 'list'>
print(type(b)) # <class 'tuple'>
print(type(c)) # <class 'dict'>
print(type(d)) # <class 'set'>
print(a) # []
print(b) # ()
print(c) # {}
print(d) # set()
#  Gift
# add()  and  remove()  methods  (Home  work)
a = set() 
a . add(25) # {25}
a . add(10.8) # {25,10.8}
a . add('Hyd') # {25,10.8,'Hyd'}
a . add(True) # {25,10.8,'Hyd',True}
a . add(None) # {25,10.8,'Hyd',True,None}
a . add('Hyd') # {25,10.8,'Hyd',True,None}
a . add(1) # {25,10.8,'Hyd',True,None}
print(a) # {25,10.8,'Hyd',True,None}
a . remove(25) 
print(a) # {10.8,'Hyd',True,None}
#a . append(100)  # Error: 'set' object has no attribute 'append'
#a . add(set())  # Error: unhashable type: 'set'
# How  to  print  set  in  two  differnet ways  (Home  work)
a = {25 , True , 'Hyd' , 10.8}
print('set with print function')#'set  with  print  function'
print(a) # How  to  print  set
print('Iterate  elements  of  set  with  for  loop') # 'Iterate  elements  of  set  with  for  loop'
for x in a:# How  to  iterate  set  with  for  loop
    print(x)