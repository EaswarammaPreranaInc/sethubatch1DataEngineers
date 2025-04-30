#  Write  a  program  to  remove  all  15's  from  the  list

a = [10 , 20 , 15 , 18 , 12 , 15 , 19 , 25 , 15 , 14 , 12]
while 15  in a:   # repeat until there is no 15 in the list
	  a.remove(15)
print(a) # [10,20,15,18,12,15,19,25,15,14,12]


#  Find  outputs  (Home  work)
a = (25 , 10.8 , 'Hyd' , True , 3+4j , None , 'Hyd' , 25) # a is tuple due to ()
print(a) # (25,10.8,'Hyd',True,3+4j,None,'Hyd',25)
print(*a) # Unpacks tuple into elements i.e 25 10.8 'Hyd' True 3+4j None 'Hyd' 25
print(type(a)) # <class 'tuple'>
print(len(a)) # Length is 8
print(a[2 : 5]) # [2:5:1] tuple from indexes from 2 to 4 in steps of 1 i.e ('Hyd',True,3+4j)
print(*a[2 : 5]) # Unpacks subtuple i.e 'Hyd'<space>True<space>3+4j
a[2] = 'Sec' # Error because tuple is immutable
a . append('Sec') # Error because there is no append() method in tuple
a . remove('Hyd') # Error because there is no remove() method in tuple
b =  10 , 20 , 30 # Valid tuple because () are optional
print(b)  # (10,20,30)
print(b * 2) # repeats the tuple twice i.e (10,20,30,10,20,30)
c = 40 , 50 , 60, # valid tuple because comma is optional
print(c) # (40,50,60)
print(type(c)) # < class 'tuple'>


# Find  outputs  (Home  work)
a = (25) # integer because comma is missing
b = 25, # Tuple because of comma
c = 25 # integer because comma is missing
d = (25,) # Tuple because of comma
print(type(a)) # < class 'int'>
print(type(b)) # < class 'tuple'>
print(type(c)) # < class 'int'>
print(type(d)) # < class 'tuple'>
print(a * 4) # 25 * 4 = 100
print(b * 4) # Repeat tuple four times i.e (25,25,25,25)
print(c * 4) # 25 * 4 = 100
print(d * 4) # Repeat tuple four times i.e (25,25,25,25)


# tuple()  function  demo  program  (Home  work)
a = tuple('Hyd') # converts string to tuple because string is a sequence
print(a) # ('H','y','d')
print(type(a)) # < class 'tuple'>
print(len(a)) # Length is 3
b = [10 , 20 , 15 , 18] # b is list due to []
print(tuple(b)) # converts list to tuple i.e (10,20,15,18)
print(tuple(range(5))) # converts range object to tuple i.e (0,1,2,3,4)
print(tuple(25)) # Error because 25 is not a sequence


# Find  outputs (Home  work)
a = () # Empty tuple
print(type(a)) # < class 'tuple'>
print(a) # ()
print(len(a)) # 0
b = tuple() # function returns an empty tuple
print(b) # ()
print(len(b)) # 0


# Find  outputs (Home  work)
a = (10 , 20 , 30) # a is tuple due to ()
print(a) # (10,20,30)
print(id(a)) # Address of the tuple object
a = a * 2 # ref 'a' points to the a*2 it have six elements
print(a) # (10,20,30,10,20,30)
print(id(a)) # Address of the tuple object with 6 elements


#  set  object  demo  program  (Home  work)
a = {25 , 10.8 , 'Hyd' , True , 3+4j , None , 25 , 'Hyd'} # a is set due to {}
print(a) # {25,10.8,'Hyd',True,3+4j,None} in any order
print(type(a)) # < class 'set'>
print(len(a)) # Length is 6
print(a[2]) # Error because set is not indexed
print(a[1 : 4]) # Error because set can not be sliced
a[2] = 'Sec' # Error because set can not be modified because there is no index
print(a * 2) # Error because set can not be repeated
print(a * a) # Error because set can not be multiplied


# Find  outputs (Home  work)
a = {1 , 'Hyd' , False , True , 0.0 , '' , 1.0 ,  0} # a is set due to {}
print(a) # set can't hold duplicate elements i.e {1,'Hyd',False,''}
print(len(a)) # length is 4
print(type(a)) # < class 'set>


#  set()  function demo  program
a = set('Rama rAo') # converts string to set because it is a sequence
print(a) # {'R','a','m','','r','A','o'} 
print(len(a)) # length is 7
print(set([10 , 20 , 15 , 20])) # converts list to set i.e {10,20,15}
print(set((25 , 10.8 , 'Hyd' , 10.8))) # converts tuple to set i.e (10,20,15) 
print(set(range(10 , 20 , 3))) # converts range object to set i.e {10,13,16,19}
print(set(25)) # Error because 25 is not a sequence



# Find  outputs  (Home  work)
a =   [ ] # Empty list
b =   ( ) # Empty tuple
c =   { } # Empty dictionary
d =   set() # unction returns Empty set
print(type(a)) # < class 'list'> 
print(type(b)) # < class 'tuple'> 
print(type(c)) # < class 'dict'> 
print(type(d)) # < class 'set'> 
print(a) # []
print(b) # ()
print(c) # {}
print(d) # {}



# add()  and  remove()  methods  (Home  work)
a = set() # function returns empty set
a . add(25) # 25 element is added to empty set
a . add(10.8) # 10.8 element is added to set
a . add('Hyd') # 'Hyd' element is added to set
a . add(True) # True element is added to set
a . add(None) # None element is added to set
a . add('Hyd') # Not added because it is already exsists in the set
a . add(1) # Not added because it is already exsists in the set
print(a) # {25,10.8,'Hyd',True,None}
a . remove(25) # removes 25 in the list
print(a) # {10.8,'Hyd',True,None}
a . append(100) # Error because there is no append() method in set




# How  to  print  set  in  two  differnet ways  (Home  work)
a = {25 , True , 'Hyd' , 10.8} # a is set due to {} with elements
print(a) # print('set  with  print  function') i.e {25,True,'Hyd',10.8}
for x in a: # How  to  iterate  set  with  for  loop
    print(x) # 25
             # True
			 # 'Hyd'
			 # 10.8
