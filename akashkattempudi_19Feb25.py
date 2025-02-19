# How  to  print  dictionary  in  different  ways
a  =  {10 : 'Ramesh' ,  20 : 'Kiran' , 15 : 'Amar' , 18 : 'Sita'}
print('Dictionary  with  print  function')
print(a) # {10: 'Ramesh', 20: 'Kiran', 15: 'Amar', 18: 'Sita'}
print('Keys  of  dictionary')
for k in a.keys():
    print(k) # 10 <nextline> 20 <nextline> 15 <nextline> 18
print('Values  of  dictionary')
for v in a.values():
    print(v) # Ramesh <nextline> Kiran <nextline> Amar <nextline> Sita
print('All  the  tuples  of  dict_items   object')
for i in a.items():
    print(i) # (10, 'Ramesh') <nextline> (20, 'Kiran') <nextline> (15, 'Amar') <nextline> (18, 'Sita')
print('Elements  of  each   tuple')
for key,_ in a.items():
    print(key) # 10 <nextline> 20 <nextline> 15 <nextline> 18
for _,value in a.items():
    print(value) #Ramesh <nextline> Kiran <nextline> Amar <nextline> Sita
print('Keys  and  values  of  dictionary')
for key,value in a.items():
    print("keys :",key,", values :",value)# Keys : 10 , values : Ramesh <nextline> keys : 20 , values : Kiran <nextline> keys : 15 , values : Amar <nextline> keys : 18 , values : Sita



#  Find  outputs (Home  work)
a = {
		print('Hyd') , # Hyd
		print('Sec') , # Sec
		print('Cyb')   # Cyb
     }
print(type(a)) # <class 'set'>
print(a)       # {None} because print statement returns none
print(len(a))  # 1



#  Anonymous  object  demo  program
_ = 25
print(_) # 25
print(type(_)) # <class = 'int'>
a , _ , c = 10 , 20 , 30
print(a) # 10
print(_) # 20
print(c) # 30
for  _  in  range(5):
    print(_ , 'Hello') # 0 Hello <next line> 1 Hello <next line> 2 Hello <next line> 3 Hello <next line> 4 Hello



#  Find  outputs
a = 25
print(id(a)) # a ref contains the address of obj 25
a = 35
print(id(a)) # a ref contains the address of another obj 35



# Find  outputs (Homework)
a = 25.7
print(id(a)) # a ref contains the address of obj 25.7
print(a) # 25.7
a = 35.6
print(id(a)) # a ref contains the address of another obj 35.6
print(a) #35.6
b = True 
print(id(b)) # b ref contains the address of obj True
b = False
print(id(b)) # b ref contains the address of another obj False
c = None
print(id(c)) # c ref contains the address of obj None
c = None
print(id(c)) # b ref contains the address of same obj None



#  Find  outputs (Homework)
a = 'Hyd'
print(id(a)) # a ref contains the address of obj 'Hyd'
a[1] = 'e' #error because str are immutable
a = 'Sec'
print(id(a)) # a ref contains the address of another obj 'Sec'
b = (10 , 20 , 15 , 18)
print(id(b))  # b ref contains the address of obj (10 , 20 , 15 , 18)
b[2] = 19 #error because tuple are immutable
b = (30 , 40 , 35 , 32)
print(id(b))# b ref contains the address of another obj (30 , 40 , 35 , 32)
c = range(5)
print(id(c)) # c ref contains the address of obj range(5)
c[3] = 10 #error because range are immutable
c = range(5)
print(id(c)) # c ref contains the address of same obj range(5)


# Find  outputs  (Homework)
a = 25
b = 25
print(a is b)  # True
c = 'Hyd'
d = 'Hyd'
print(c is d)  # True
e = False
f = False
print(e is f)  # True
g = range(10)
h = range(10)
print(g is h)  # False because the range object creates a new object in memory every time 


#Find  outputs(Home  work)
a = [10 , 20 , 15 , 18]
b = [10 , 20 , 15 , 18]
print(a  is  b) # False
c =  {10 : 20, 30 : 40}
d =  {10 : 20, 30 : 40}
print(c  is  d) # False
e = (10 , 20 , 15 , 18)
f = (10 , 20 , 15 , 18)
print(e  is  f) # True because tuple are immutable
g = {10 , 20 , 15 , 18}
h = {10 , 20 , 15 , 18}
print(g  is  h) # False


# Find outputs (Home work)
print(10 + 20) # 30
print(10.8 + 20.6) # 31.4
print(3 + 4j + 5 + 6j) # 8+10j
print(True + False) # 1


print('Hyder' + 'abad') # Hyderabad
print('Sankar' + 'Dayal' + 'Sarma') # SankarDayalSarma
print('10' + '20') # 1020
print([10 , 20 , 30] + [1 , 2 , 3]) # [10, 20, 30, 1, 2, 3]
print((25 , 10.8 , 'Hyd') + (3 + 4j , True , None)) # (25, 10.8, 'Hyd', (3+4j), True, None)
print({10 , 20} + {30 , 40}) # error set doesnt have + operator they are unordereed
print({10 : 'Hyd'} + {20 : 'Sec'}) # error dict doesnt have + operator they are unordered
print(range(4) + range(5)) # error ranges doesnt have + operator
print(10 + '20') # error seq+seq only or nonseq+nonseq
print([10 , 20 , 30] + 5) # error seq+seq only or nonseq+nonseq
print([10 , 20 , 30] + (40 , 50 , 60)) # error list+list or tuple+tuple

# Find outputs (Home work)
print(25 * 3) # 75
print(10.8 * 25.6) # 276.48
print(True * False) # 0
print((3 + 4j) * (5 + 6j)) # (-9+38j)
print(3 + 4j * 5 + 6j) # (3+26j)
print('25' * 3) # 252525
print(3 * '25') # 252525
print('Hyd' * 4) # HydHydHydHyd
print([10 , 20 , 15] * 2) # [10, 20, 15, 10, 20, 15]
print((25, 10.8, 'Hyd', True) * 3) # (25, 10.8, 'Hyd', True, 25, 10.8, 'Hyd', True, 25, 10.8, 'Hyd', True)
# print([10 , 20 , 15] * 3.0) # error float
# print({10 , 20 , 15} * 2) # error set doesnt support *
# print({10 : 20 , 30 : 40} * 2) # error dict doesnt support *
print([10] * [20]) # error list can't multiply sequence


# Find outputs
print(7 / 0)# Error Division by zero is not allowed
print(7 // 0) #Error Floor division by zero is not allowed
print(7 % 0) #Error Modulo by zero is not allowed

# ** operator demo program
print(3 ** 4)   #  3 ^ 4 = 81
print(10 ** -2) # 0.01
print(4 ** 3 ** 2) # 262144
print(3 + 4 * 5 - 32 / 2 ** 3) # 19.0

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
print(3 + 4j == 5 + 6j) # True
print(3 + 4j != 5 + 6j) # True
print(10 == 10.0) # True
print(3 + 4j >  3 + 4j) #error complex numbers doesnt support >,<,>=,<=

#  Find  outputs  (Home  work)
print('Rama'   >  'Rajesh')   #   True  becoz  'm' > 'j'
print('Rama'  <  'Sita') # True
print('Hyd'  ==  'Hyd') # True
print('Rama'  <=   'Ramana') # True
print('Rama  Rao'  >=  'Rama') # True
print('Hyd'  != 'Sec') # True
print('HYD'  <   'hyd') # True

# Chaining  relational  opeartors  (Home work)
print(10 < 20 < 30)    #   True  becoz  both  are  satisfied
print(10 >= 20 < 30)   #  False  becoz  1st  cond  is  not  satisfied
print(10 < 20 > 30) # False
print(1 < 2 < 3 < 4) # True
print(1 < 2 > 3 > 1) # False
print(4 > 3 >= 3 > 2) # True
