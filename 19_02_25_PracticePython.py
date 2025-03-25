# Gift
# How  to  print  dictionary  in  different  ways
a  =  {10 : 'Ramesh' ,  20 : 'Kiran' , 15 : 'Amar' , 18 : 'Sita'}
print('Dictionary  with  print  function')
print(a) #How  to  print  dictionary
print(a.keys())# 'Keys  of  dictionary'
for x in a:
	print(x) #How  to  print  each  key of  dictionary  with  for  loop
print(a.values())#'Values  of  dictionary'
for y in a.values():
	print(y) #How  to  print  each  value  of  dictionary  with  for  loop
print(a.items()) #'All  the  tuples  of  dict_items   object'
for z in a.items():
	print(z) #How  to  print  each  tuple  of  dictionary  with  for  loop
print('Elements  of  each   tuple')
for x,y in a.items():
	print(f'Key : {x} , Value : {y}')#How  to  print  elements  of  tuple   in  dictionary  with  for  loop
print('Keys  and  values  of  dictionary')
for x in a:
	print(f'Key : {x}')#How  to  print  each  key of  dictionary  with  for  loop  along   with  corresponding  value
# Gift
#  Find  outputs (Home  work)
a = {
		print('Hyd') ,
		print('Sec') ,
		print('Cyb')
     }
print(type(a)) # <class 'set'>
print(a) # {'Hyd','Sec','Cyb'}
print(len(a)) # 3
#  Anonymous  object  demo  program
_ = 25
print(_) # 25
print(type(_))
a , _ , c = 10 , 20 , 30
print(a) # 10
print(_) # 20
print(c) # 30
for  _  in  range(5):
	print(_ , 'Hello')
'''o/p: 0 Hello
        1 Hello
        2 Hello
        3 Hello
        4 Hello
'''	
	
#  Find  outputs
a = 25
print(id(a)) # Address of a
a = 35
print(id(a)) # diff address becoz of object
# Find  outputs (Home  work)
a = 25.7
print(id(a)) # Address of a
print(a) # 25.7
a = 35.6 
print(id(a)) # Diff address of a
print(a) # 35.6
b = True 
print(id(b)) # Address of b
b = False
print(id(b)) # diff address of b
c = None
print(id(c)) # Address of c
c = None
print(id(c)) # Same Address of c
#  Find  outputs (Home  work)
a = 'Hyd'
print(id(a)) # Adddress  of a
# a[1] = 'e' # Error: 'str' object does not support item assignment
a = 'Sec'
print(id(a)) # Diff Address of a because  a is reference to Sec
b = (10 , 20 , 15 , 18)
print(id(b)) # Address of b
#b[2] = 19 # Error: 'tuple' object does not support item assignment
b = (30 , 40 , 35 , 32) 
print(id(b)) # Address of b
c = range(5) 
print(id(c)) # Address of c
#c[3] = 10 # Error: 'range' object does not support item assignment
c = range(5) 
print(id(c)) # Diff address becoz range is not resuable
# Find  outputs  (Home  work)
a = 25
b = 25
print(a  is  b) # True
c = 'Hyd'
d = 'Hyd'
print(c  is  d) # True
e = False
f = False
print(e  is  f) # True
g = range(10)
h = range(10)
print(g  is  h) # False becoz range is not reusable
#Find  outputs(Home  work)
a = [10 , 20 , 15 , 18]
b = [10 , 20 , 15 , 18]
print(a  is  b) # False becoz list is not resuable
c =  {10 : 20, 30 : 40}
d =  {10 : 20, 30 : 40}
print(c  is  d) # False becoz dict is not resuable
e = (10 , 20 , 15 , 18)
f = (10 , 20 , 15 , 18)
print(e  is  f) # True
g = {10 , 20 , 15 , 18}
h = {10 , 20 , 15 , 18}
print(g  is  h) # False becoz set is not resuable
# Find outputs (Home work)
print(10 + 20) # 30
print(10.8 + 20.6) # 31.4
print(3 + 4j + 5 + 6j) # 8+10j
print(True + False) # 1
print('Hyder' + 'abad') # Hyderabad 
print('Sankar' + 'Dayal' + 'Sarma') # SankarDayalSarma 
print('10' + '20') # 1020
print([10 , 20 , 30] + [1 , 2 , 3]) # [10,20,30,1,2,3] 
print((25 , 10.8 , 'Hyd') + (3 + 4j , True , None))  # (25, 10.8, 'Hyd', (3+4j), True, None)
#print({10 , 20} + {30 , 40}) # Error: unsupported operand type(s) for +: 'set' and 'set'
#print({10 : 'Hyd'} + {20 : 'Sec'}) #  Error: unsupported operand type(s) for +: 'dict' and 'dict'
#print(range(4) + range(5)) # Error: unsupported operand type(s) for +: 'range' and 'range'
#print(10 + '20') # Error becoz sequence and non-sequence
#print([10 , 20 , 30] + 5)  # Error: can only concatenate list (not "int") to list
#print([10 , 20 , 30] + (40 , 50 , 60)) # Error: can only concatenate list (not "tuple") to list
# Find outputs (Home work)
print(25 * 3) # 75
print(10.8 * 25.6) #  
print(True * False) # 0
print((3 + 4j) * (5 + 6j)) # -9+38j
print(3 + 4j * 5 + 6j) # 3+26j
print('25' * 3) # 252525
print(3 * '25') # 252525
print('Hyd' * 4) # HydHydHydHyd
print([10 , 20 , 15] * 2) # [10, 20, 15, 10, 20, 15]
print((25, 10.8, 'Hyd', True) * 3) # (25, 10.8, 'Hyd', True, 25, 10.8, 'Hyd', True, 25, 10.8, 'Hyd', True)
#print([10 , 20 , 15] * 3.0) # Error becoz of float 3.0
#print({10 , 20 , 15} * 2) # Error: unsupported operand type(s) for *: 'set' and 'int'
#print({10 : 20 , 30 : 40} * 2) # Error: unsupported operand type(s) for *: 'dict' and 'int'
#print([10] * [20]) # Error: can't multiply sequence by non-int of type 'list'
# Find outputs
#print(7 / 0) # Error becoz infinite 
#print(7 // 0) # Zero division error
#print(7 % 0) # Error
# ** operator demo program
print(3 ** 4)   #  3 ^ 4 = 81
print(10 ** -2) # 10 ^ -2 = 0.01
print(4 * 3 * 2) # 24
print(3 + 4 * 5 - 32 / 2 ** 3) # 19
#  Relational  operators  demo  program (Home  work)
print(9 >= 5)  #  True  becoz  >  is  satisfied
print(9 >= 9)   #  True  becoz  =  is  satisfied
print(9 >= 12)   #  False  becoz    both  are  not  satisfied
print(6 <= 8) # True
print(6 <= 6) # True
print(6 <= 4) # False
print(9 != 7) # True 
print(6 == 8) # False
print(True  >  False) # True
print(3 + 4j == 3 + 4j) # True
print(3 + 4j == 5 + 6j) # False
print(3 + 4j != 5 + 6j) # True
print(10 == 10.0) # True
#print(3 + 4j >  3 + 4j) # Error becoz complex cant compare
#  Find  outputs  (Home  work)
print('Rama'   >  'Rajesh')   #   True  becoz  'm' > 'j'
print('Rama'  <  'Sita')  # True becoz 'S' > 'R'
print('Hyd'  ==  'Hyd') # True
print('Rama'  <=   'Ramana') # True
print('Rama  Rao'  >=  'Rama') # True
print('Hyd'  != 'Sec') # True
print('HYD'  <   'hyd') # True
'''

1) Can  strings  be  compared  with  > ,  < , == ,  >= , <=  and  != ?  --->  Yes  only  in  python  but  not  in  other  languages

2) What  are  compared  internally  when  strings  are  compared ? ---> 1st  non-matching  characters

3) Are  characters  compared  (or)  their  unicode  values ?  --->  Unicode  values

4) How  many  unicode  values  exist ?  --->  512

5) What  is  the  range  of  unicode  values ?  --->  0  to  511

6) What  are  the  unicode  values  of  'A'  to  'Z'  ?  --->  65  to  90
    W…'''
# Chaining  relational  opeartors  (Home work)
print(10 < 20 < 30)    #   True  becoz  both  are  satisfied
print(10 >= 20 < 30)   #  False  becoz  1st  cond  is  not  satisfied
print(10 < 20 > 30)   # False becoz of 20<30
print(1 < 2 < 3 < 4)  # True
print(1 < 2 > 3 > 1)  # False becoz 2<3
print(4 > 3 >= 3 > 2) # True