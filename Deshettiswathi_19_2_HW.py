#*19_2_25_HW*
# Gift
# How  to  print  dictionary  in  different  ways
a  =  {10 : 'Ramesh' ,  20 : 'Kiran' , 15 : 'Amar' , 18 : 'Sita'}
print('Dictionary  with  print  function')
print(a)    #{10: 'Ramesh', 20: 'Kiran', 15: 'Amar', 18: 'Sita'}
print('Keys  of  dictionary')
for x in a.keys():
	print(x)
'''Keys  of  dictionary
10
20
15
18'''

print('Values  of  dictionary')
for x in a.values():
	print(x)
'''Values  of  dictionary
Ramesh
Kiran
Amar
Sita'''

print('All  the  tuples  of  dict_items   object')
for x in a.items():
	print(x)
'''All  the  tuples  of  dict_items   object
(10, 'Ramesh')
(20, 'Kiran')
(15, 'Amar')
(18, 'Sita')'''

print('Elements  of  each   tuple')
for x,y in a.items():
	print(x,y,sep = '-')
'''Elements  of  each   tuple
10-Ramesh
20-Kiran
15-Amar
18-Sita'''

print('Keys  and  values  of  dictionary')
#How  to  print  each  key of  dictionary  with  for  loop  along   with  corresponding  value
for x in a.keys():
	print(x,a[x],sep=':')

'''Keys  and  values  of  dictionary
10:Ramesh
20:Kiran
15:Amar
18:Sita'''


# Gift
#  Find  outputs (Home  work)
a = {
		print('Hyd') ,  #prints Hyd
		print('Sec') ,  #prints Sec
		print('Cyb')    #prints Cyb
     }
print(type(a))       # prints <class 'set'>
print(a)             # prints None because whenever the object is printed it returns something i.e. none
print(len(a))        #1


#  Anonymous  object  demo  program
_ = 25 
print(_)            #prints 25
print(type(_))      #<class 'int>
a , _ , c = 10 , 20 , 30
print(a)            #prints value of a i.e. 10
print(_)            #prints value of _ i.e. 20
print(c)            #prints value of c i.e. 30
for  _  in  range(5):
	print(_ , 'Hello')   # prints range from 0 to 4 with Hello
	                     # 0 Hello
                             # 1 Hello
                             # 2 Hello
                             # 3 Hello
                             # 4 Hello
        
#  Find  outputs
a = 25
print(id(a))       #print address of object 25
a = 35
print(id(a))       #print address of object 35


# Find  outputs (Home  work)
a = 25.7
print(id(a))      #print address of object 25.7
print(a)          #print value of object i.e. 25.7
a = 35.6          # refrence a points to different object because object replacing is invalid for int
print(id(a))       #print address of object 35.6
print(a)           #print value of object i.e. 35.6
b = True      
print(id(b))       #print address of True
b = False          #ref b points to different object because replacing is invalid for bool
print(id(b))      #print address
c = None
print(id(c))      #print address
c = None          # refrence c continues pointing to c because the object is same and it is reusable
print(id(c))      #print same address as above


#  Find  outputs (Home  work)
a = 'Hyd'
print(id(a))      #print address of string
a[1] = 'e'        #error - string is immutable and no assignment of value
a = 'Sec'         # ref a points to other object 'sec'
print(id(a))      #prints address of string sec
b = (10 , 20 , 15 , 18)
print(id(b))      #print address of the tuple object
b[2] = 19         # error- tuple is immutable, cant assign new value 
b = (30 , 40 , 35 , 32)  
print(id(b))      #print address
c = range(5)
print(id(c))      #print address
c[3] = 10         #error due to range is immutable
c = range(5)      #ref c modified to another object because range is not reusable
print(id(c))      #print address
   

# Find  outputs  (Home  work)
a = 25
b = 25           # both references a and b points to same object because int is immutable and reusable.
print(a  is  b)  # True both references points to same object
c = 'Hyd'
d = 'Hyd'
print(c  is  d)  # True- both references points to same object because string is immutable and reusable
e = False
f = False
print(e  is  f)  #True- both references points to same object because Bool is immutable and reusable
g = range(10)
h = range(10)
print(g  is  h)  #False both references points to different object because range is immutable and range objects cannot reusable


#Find  outputs(Home  work)
a = [10 , 20 , 15 , 18]
b = [10 , 20 , 15 , 18]   #another new list is created i.e. b
print(a  is  b)           # False both references points to different object because List is mutable and objects cannot reusable
c =  {10 : 20, 30 : 40}
d =  {10 : 20, 30 : 40}   #another new dict is created i.e. d
print(c  is  d)          #False both references points to different object because List is mutable and objects cannot reusable
e = (10 , 20 , 15 , 18)
f = (10 , 20 , 15 , 18)
print(e  is  f)          #True both references points to same object because tuple is immutable and reusable
g = {10 , 20 , 15 , 18}
h = {10 , 20 , 15 , 18}  #another set is created i.e. h
print(g  is  h)          #False both references points to different object because List is mutable and objects cannot reusabl
 

# Find outputs (Home work)
print(10 + 20)              #30
print(10.8 + 20.6)          #31.4
print(3 + 4j + 5 + 6j)      #8+10j
print(True + False)         #1+0 = 1
print('Hyder' + 'abad')     # Hyderabad - concatenation of strings
print('Sankar' + 'Dayal' + 'Sarma')  #SankarDayalSarma
print('10' + '20')                   #1020- concatenation of strings 
print([10 , 20 , 30] + [1 , 2 , 3])  #[10 , 20 , 30,1 , 2 , 3]- concatenation of lists
print((25 , 10.8 , 'Hyd') + (3 + 4j , True , None))   # (25 , 10.8 , 'Hyd',3 + 4j , True , None)- concatenation of tuples
print({10 , 20} + {30 , 40})         # error- sets cannot combine with + operator
print({10 : 'Hyd'} + {20 : 'Sec'})   # error - dictionaries cannot combine with + operator
print(range(4) + range(5))           # error- range objects cannot concatenate with + operator
print(10 + '20')                     # error- cannot concatenate sequence and non-sequence
print([10 , 20 , 30] + 5)            # error- cannot concatenate list and int with + operator
print([10 , 20 , 30] + (40 , 50 , 60)) # error- cannot concatenate list and tuple.


# Find outputs (Home work)
print(25 * 3)              # 75  
print(10.8 * 25.6)         # 276.48
print(True * False)        # 1*0 = 0
print((3 + 4j) * (5 + 6j)) # 15+18j+20j+24 = -9+38j
print(3 + 4j * 5 + 6j)     # 3+20j+6j= 3+26j
print('25' * 3)            #252525    
print(3 * '25')            #252525
print('Hyd' * 4)           #HydHydHydHyd
print([10 , 20 , 15] * 2)  # [10 , 20 , 15,10 , 20 , 15]
print((25, 10.8, 'Hyd', True) * 3)  # (25, 10.8, 'Hyd', True,25, 10.8, 'Hyd', True,25, 10.8, 'Hyd', True)
print([10 , 20 , 15] * 3.0) # error because multiplier is float. 
print({10 , 20 , 15} * 2)   # error- set is not repeated becuase duplicate values are not allowed 
print({10 : 20 , 30 : 40} * 2) #error- dict object is not repeated becuase duplicate keys will generate which are invalid 
print([10] * [20])         # error- the multiplier must be int but not list.


# Find outputs
print(7 / 0)  # error because division by 0
print(7 // 0) # error because division by 0
print(7 % 0)  # error because division by 0


# ** operator demo program
print(3 ** 4)   #  3 ^ 4 = 81
print(10 ** -2) # 10^-2 = 0.01
print(4 * 3 * 2) # 4^3^2 = 262144
print(3 + 4 * 5 - 32 / 2 ** 3)  # 3+4*5-32/8
                                #3+20-32/8
			        #3+20-4.0
			        #23-4.0 = 19.0


#  Relational  operators  demo  program (Home  work)
print(9 >= 5)  #  True  becoz  9 > 5  
print(9 >= 9)   #  True  becoz  =  is  satisfied
print(9 >= 12)   #  False  becoz both  are  not  satisfied
print(6 <= 8)    # true becoz 6 < 8
print(6 <= 6)    # true becoz 6 = 6
print(6 <= 4)    # false becoz both are not satisified
print(9 != 7)    # true 
print(6 == 8)    # false becoz 6 != 8
print(True  >  False)  # true becoz 1>0
print(3 + 4j == 3 + 4j) # true becoz both are same
print(3 + 4j == 5 + 6j) # false because 3 + 4j != 5 + 6j
print(3 + 4j != 5 + 6j) # true- condition is satisfied
print(10 == 10.0)       # true- 10 and 10.0 are same
print(3 + 4j >  3 + 4j) # error becoz complex objects cannot compare using '>'

#  Find  outputs  (Home  work)
print('Rama'   >  'Rajesh')   #   True  becoz  'm' > 'j'
print('Rama'  <  'Sita')      #   true- 'R' < 'S'
print('Hyd'  ==  'Hyd')       #   true- both are same
print('Rama'  <=   'Ramana')  #   true- 'empty string'< 'n'
print('Rama  Rao'  >=  'Rama') #  true-  'space'(unicode value 36) > 'empty string'
print('Hyd'  != 'Sec')         #  true- both are not same
print('HYD'  <   'hyd')        # true-  unicode values of A to Z (65 to 90) <  unicode values of a to z (97 to 122)

# Chaining  relational  opeartors  (Home work)
print(10 < 20 < 30)    #   True  becoz  both  are  satisfied
print(10 >= 20 < 30)   #  False  becoz  1st  cond  is  not  satisfied
print(10 < 20 > 30)    #True becoz  both  are  satisfied
print(1 < 2 < 3 < 4)   # True becoz  three conditions  are  satisfied
print(1 < 2 > 3 > 1)   # False becoz  2nd condition is not satisfied
print(4 > 3 >= 3 > 2)  #True becoz  all conditions  are  satisfied
