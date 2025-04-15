# difference()   method  demo  program  (Home  work)
a = {10 , 20 , 30 , 40}
b = {30 , 40 , 50 , 60}
c = a . difference(b)
print(c) # {10,20}
print(type(c)) # <class 'set'>
d = a - b 
print(d) # {10,20}
print(type(d)) # <class 'set'>
print(c  is  d) # False becoz the set is mutable but not resuable 
print(c  ==  d) # True becoz objects are same in both sets

# symmetric_difference()   method  demo  program  (Home  work)
a = {10 , 20 , 30 , 40}
b = {30 , 40 , 50 , 60}
c = a . symmetric_difference(b)
print(c) # {10,20,50,60}
print(type(c)) # <class 'set'>
d = a ^ b
print(d) # {10,20,50,60}
print(type(d)) # <class 'set'>
print(c   is   d) # False becoz the set is mutable but not resuable
print(c  ==   d) # True becoz objects are same in both sets

# Find  outputs  (Home  work)
a = {x * x  for   x   in   range(10)}
print(a) # {0,1,4,9,16,25,36,49,64,81}
print(type(a)) # <class 'set'>

'''
(Home  work)
Write  a  program  to  remove  duplicate  characters  of  the  string  using  set

1) Let  input  be   Rama  Rao
    What  is  the  output  ? --->  Ram<space>o

2) Both  input  and  output  are  strings

3) How  to  convert  string  to  set  ?  --->  set(string)
    How  to  convert  set  to  string ?  ---> '' . join(set)

4) What  is  the  result  of  str({'H' , 'y' , 'd'})  ? --->  "{'H' , 'y' , 'd'}"  but  not  'Hyd'
'''

a = 'Rama Rao'
b = set(a)
c = ''.join(b)
print(c)

# o/p: Ram o

'''
Write  a  program  to  print  distinct  vowels  of  the  string  by  using  set

1) Let  input  be  RamA  Rao
   What  is  the  output  ?  ---> AO  (case  is  ignored)

2) Both  input  and  output  are  strings

3) Hint:  Same  as  prog19  with  minor  changes
'''
a = 'RamA Rao'
b = set(a.lower())
vowels = {'a','e','i','o','u'}
c = ''.join(sorted(b & vowels)).upper()
print(c)
# o/p: AO
'''
Write  a  program  to  remove  duplicate  elements  of   list  using  set

1) Let  input  be  [False , 25 , 10.8 , 1  , 25 , 0 , 'Hyd' ,  10.8 , 1.0 , None , 'Sec' , 'Hyd' , True  ]
    What  is  the  output ?  --->	[False , 25 , 10.8 , 1 , 'Hyd' , None , 'Sec']

2) Both  input  and  output  are  lists
'''
a = [False , 25 , 10.8 , 1  , 25 , 0 , 'Hyd' ,  10.8 , 1.0 , None , 'Sec' , 'Hyd' , True  ]
b = list(set(a))
print(b)
# o/p: [False , 25 , 10.8 , 1 , 'Hyd' , None , 'Sec']
'''
Write  a  program  to   obtain  common  elements  between  two  lists  using  sets

1) Let  1st  list  be  [10 , 20 , 30 , 40 , 50 , 60]  and  2nd  list  be  [30 , 40 , 70 , 80 , 20]
    What  is  the  output ?  --->	[20 , 30 , 40]

2) Both  input  and  output  are  lists
'''

a = [10 , 20 , 30 , 40 , 50 , 60]
b = [30 , 40 , 70 , 80 , 20]
c = list(set(a) & set(b))
# o/p: [40, 20, 30]
print(c)
#  How  to  access  values  of  dictionary (Home  work)
a  =  {'Empno'  :  25 ,  'Ename'  :  'Rama  Rao'  ,  'Sal'  :  1000.65  }
print(a['Empno']) #How  to  print  value  25  in  dict  'a'
print(a['Ename'])#How  to  print  'Rama Rao'  in  dict  'a'
print(a['Sal'])#How  to  print  value  1000.65   in  dict  'a'
# How  to  modify  values  of  dictionary  (Home  work)
a  =  {'Empno'  :  25,  'Ename'  :  'Rama  Rao'  ,  'Sal'  :  1000.65  }
print(a) # {'Empno'  :  25,  'Ename'  :  'Rama  Rao'  ,  'Sal'  :  1000.65  }
print(id(a)) # Address of a
a['Sal'] = 2000 #How  to  modify  1000.65  to  2000
a['Ename'] = 'Sita'#How  to  modify  'Rama  Rao'  to  'Sita'
a['Empno'] = 35 #How  to  modify  25   to  35 print(a)
print(a) # {'Empno': 35, 'Ename': 'Sita', 'Sal': 2000}
print(id(a)) # Same Address of a becoz of values are modified
#  How  to  append  key : value  pairs  to dictionary  (Home  work)
a  =  {'Empno'  :  25,  'Ename'  :  'Rama  Rao'  ,  'Sal'  :  1000.65  }
print(a) # {'Empno'  :  25,  'Ename'  :  'Rama  Rao'  ,  'Sal'  :  1000.65  }
a['Gender'] = 'M'#How  to  append  'Gender' : 'M'  to  dictionary  'a'
a['Married'] = True#How  to  append  'Married' :  True  to  dictionary  'a'
print(a) # {'Empno': 25, 'Ename': 'Rama  Rao', 'Sal': 1000.65, 'Gender': 'M', 'Married': True}
# Find  outputs (Home  work)
a = { }
a['10'] = 'Rama'#How  to  append  10 : 'Rama'  to  dictionary  'a'
a['20'] = 'Sita'#How  to  append  20 : 'Sita'  to  dictionary  'a'
a['15'] = 'Rajesh'#How  to  append  15 : 'Rajesh'  to  dictionary  'a'
a['18'] = 'Kiran'#How  to  append  18 : 'Kiran'  to  dictionary  'a'
print(a)#{'10': 'Rama', '20': 'Sita', '15': 'Rajesh', '18': 'Kiran'}
#  How  to  remove  key : value  pairs  of  dictionary  (Home  work)
a =  {'Empno'  :  25,  'Ename'  :  'Rama  Rao'  ,  'Sal'  :  1000.65  }
print(a) #{'Empno'  :  25,  'Ename'  :  'Rama  Rao'  ,  'Sal'  :  1000.65  }
a.pop('Sal')#How  to  remove  'Sal' : 1000.65  from  dictionary  'a'
print(a)#{'Empno': 25, 'Ename': 'Rama  Rao'}
#  in  and  not  in  operators  (Home  work)'''
a =  {10 : 20 , 30 : 40 , 50 : 60 , 70 : 80}
print(30  in  a . keys()) # True
print(60  in  a . keys()) # False
print(60  in  a . values()) # True
print(30  in  a . values()) # False
print(50  in  a) # True
print(20  in  a) # False
print(70  not  in  a . keys()) # False
print(40  not  in  a . values()) # False
print(25  not  in  a) # True
#  What  are  the  outputs  if  input  is  {10: 'A', 20: 'B', 15: 'C' , 20 : 'D'}
a = input('Enter  dictionary  :  ')
print(a) # {10: 'A', 20: 'B', 15: 'C' , 20 : 'D'}
print(type(a)) # <class 'str'>
b = eval(a)
print(b) # {10: 'A', 20: 'D', 15: 'C'}
print(type(b)) # <class 'dict'>
#  Find  outputs  (Home  work)
a = {10 : 'Rama' , 20 : 'Sita' , 15 : 'Rajesh' , 18 : 'Kiran'}
b = {**a}
print(b) # {10 : 'Rama' , 20 : 'Sita' , 15 : 'Rajesh' , 18 : 'Kiran'}
print(a  is  b) # False
print(a  ==  b) # True
c = a
print(a  is   c) # True
print(a  ==  c) # True
#Find  outputs  (Home  work)
a = {10 : 'Rama' , 20 : 'Sita' , 15 : 'Rajesh'}
b = {18 : 'Kiran' , 14 : 'Amar' , 20  : 'Manohar'}
c = {25 : 'Ramesh' , 19 : 'Krishna' , 15 : 'Radha' , 14 : 'Srinivas'}
d = {*a , *b , *c}
print(d) # {10, 14, 15, 18, 19, 20, 25}
print(type(d)) # <class 'set'>
e = {**a , **b , **c}
print(e) #{10: 'Rama', 20: 'Manohar', 15: 'Radha', 18: 'Kiran', 14: 'Srinivas', 25: 'Ramesh', 19: 'Krishna'}
print(type(e)) # <class 'dict'>
#  Find  outputs  (Home  work)
a = {10 : 20 , 30 : 40}
b = {30 : 50 , 10 : 60}
#print(a + b) # Error becoz '+' operator is not valid in dict 
c = {**a , **b}
print(c) # {10: 60, 30: 50}
d = a | b
print(d) # {10: 60, 30: 50}

'''(Home  work)
Write  a  program  to  create  a  dictionary  with  emp  names  and  salaries

Hint:  Append  each  emp  name  and  salary  to  dictionary  'a'
'''
a = {}
n = int(input('Hw many Employees:'))
for _ in range(n):
    name = input('Enter Emp Name:')
    sal = float(input('Enter sal:'))
    a[name] = sal
print(a)    
'''o/p: Hw many Employees:4
        Enter Emp Name:AAA
        Enter sal:10000
        Enter Emp Name:BBB 
        Enter sal:20000
        Enter Emp Name:CCC
        Enter sal:15000
        Enter Emp Name:DDD
        Enter sal:18000
        {'AAA': 10000.0, 'BBB': 20000.0, 'CCC': 15000.0, 'DDD': 18000.0}'''
'''
a = {}
a['AAA'] = 10000  --->   {'AAA': 10000}
a['BBB'] = 20000  --->   {'AAA': 10000 , 'BBB' : 20000}
'''
''' (Home  work)
Write  a  program  to  convert  a  string  to  dictionary

Let  input  be   "Emp no = 25 , Emp name = Rama  Rao , sal = 10000.0 , gender = m"

What  is  the  output ?  --->  {Emp no : 25 , Emp name  :  Rama Rao , sal : 10000.0 , gender : m}

Hint :  Use  split()  method  twice
'''

a =  "Emp no = 25 , Emp name = Rama  Rao , sal = 10000.0 , gender = m"
b = [x.strip() for x in a.split(",")]
c = {}
for x in b:
    key,value = x.split("=",1)
    c[key.strip()] = value.strip()
print(c)    
# o/p: {'Emp no': '25', 'Emp name': 'Rama  Rao', 'sal': '10000.0', 'gender': 'm'}
# len()  function  demo  program  (Home  work)
a  =  {'Empno'  :  25,  'Ename'  :  'Rama  Rao'  ,  'Sal'  :  1000.65  }
print(len(a)) # 3
b = {}
print(len(b)) # 0

#  sum()  function demo  program  (Home  work)
a = {10 : 20 , 30 : 40 , 50 : 60}
print(sum(a . keys())) # 90
print(sum(a . values())) # 120
print(sum(a)) # 90
#print(sum(a . items()))
# max()  and  min()   functions  demo  program  (Home  work)
a = {10 : 20 , 30 : 25 , 40 : 5 , 7 : 28 , 9 : 50}
print(max(a . keys())) # 40
print(min(a . keys())) # 7
print(max(a . values())) # 50
print(min(a . values())) # 5
print(max(a . items())) # (40,5)
print(min(a . items())) # (7,28)
print(max(a)) # 40
print(min(a)) # 7
#  dict()  function  demo program (Home  work))
a = [ (10 , 'Hyd') , (20 , 'Sec') , (15 , 'Cyb') , (20 , 'Pune')]  #  List of  tuples
b = dict(a) #  Converts  list  of  tuples  to  dict
print(b)  #  {10 : 'Hyd', 20 : 'Pune' , 15 : 'Cyb'}
c = ( ['R' , 'Red'] , ['G' , 'Green'] , ['B' , 'Blue'] , ['G' , 'Gray'])
d = dict(c)
print(d) # {'R': 'Red', 'G': 'Gray', 'B': 'Blue'}
e = [[10 , 20 , 30] , [40 , 50 , 60] , [70 , 80 , 90]]
#print(dict(e)) # Error due to 3 values 
f = [[10] , [20] , [30]]
#print(dict(f))# Error becoz of 1 value
#print(dict([10 , 20])) # Error: cannot convert dictionary update sequence element
g = [[10 , [20 , 30]] , [40 , [50 , 60]] , [70 , [80 , 90]]]
print(dict(g)) # {10: [20, 30], 40: [50, 60], 70: [80, 90]}
h = [[[10 , 20] , 30] , [[40 , 50] , 60] , [[70 , 80] , 90]]
#print(dict(h)) #Error: unhashable type: 'list'
i = [[(10 , 20) , 30] , [(40 , 50) , 60] , [(70 , 80) , 90]]
print(dict(i)) #{(10, 20): 30, (40, 50): 60, (70, 80): 90}
# sorted()  function  (Home  work)
a = {10 : 'Red' , 20 : 'Green' , 15 : 'Blue' , 18 : 'Yellow' , 5 : 'White'}
b = sorted(a . keys())
print(b) # [5, 10, 15, 18, 20]
c = sorted(a . values())
print(c) # ['Blue', 'Green', 'Red', 'White', 'Yellow']
d = sorted(a . items())
print(d)#[(5, 'White'), (10, 'Red'), (15, 'Blue'), (18, 'Yellow'), (20, 'Green')]
f  = sorted(a  , reverse = True)
print(f)#[20, 18, 15, 10, 5]
print(a)#{10: 'Red', 20: 'Green', 15: 'Blue', 18: 'Yellow', 5: 'White'}
'''
Gift
Write  a  program  to  sort  dictionary  wrt  keys  (Home  work)

1) Let  input  be   {10 : 'A' , 20 : 'B' , 15 : 'C' , 5 : 'D' , 12 : 'E'}
    What  is  the  output ?  ---> {5 : 'D' , 10 : 'A' ,  12 : 'E' ,  15 : 'C' , 20 : 'B'}

2) Both  input  and  output  are  dictionaries

3) Hint:  Use  sorted()  function

4) a = {10 : 'A' , 20 : 'B' , 15 : 'C' , 5 : 'D' , 12 : 'E'}
    b = sorted(a . items())  --->  [(5 , 'D' ) , (10 , 'A') , (12 , 'E') , (15 , 'C') , (20, 'B')]
    dict(b)  --->  {5 : 'D' , 10 : 'A' , .....}
'''
#Enter  dictionary  :  {10 : 'A' , 20 : 'B' , 15 : 'C' , 5 : 'D' , 12 : 'E'}
{5: 'D', 10: 'A', 12: 'E', 15: 'C', 20: 'B'}
#  keys()  method  demo  program
a = {10 : 'Hyd' , 20 : 'Sec' , 15 : 'Cyb' , 18 : 'Pune'}
b = a . keys()
print(b) #dict_keys([10, 20, 15, 18])
print(type(b)) # <class 'dict_keys'>
for  x  in   b:
        print(x)
'''o/p: 10
        20
        15
        18'''        


'''
What  does  keys()  method  do  --->  Returns  dict_keys  object  which  has  list  of  all  the  dictionary  keys
'''
# values()  method  demo  program
a = {10 : 'Hyd' , 20 : 'Sec' , 15 : 'Cyb' , 18 : 'Pune'}
b = a . values()
print(b)# dict_values(['Hyd', 'Sec', 'Cyb', 'Pune'])
print(type(b)) # <class 'dict_values'>
for  x   in   b:
	print(x)
'''o/p: Hyd
        Sec
        Cyb
        Pune'''


'''
What  does  values()  method  do  --->  Returns  dict_values  object  which  has  list  of  all  the  dictionary  values
'''
#  items()  method  demo  program
a = {10 : 'Hyd' , 20 : 'Sec' , 15 : 'Cyb' , 18 : 'Pune'}
b = a . items()
print(b) # dict_items([(10, 'Hyd'), (20, 'Sec'), (15, 'Cyb'), (18, 'Pune')])
print(type(b)) # <class 'dict_items'>
for  x   in   b:
        print(x) 
'''o/p: (10, 'Hyd')
        (20, 'Sec')
        (15, 'Cyb')
        (18, 'Pune') '''        
for  x , y   in  b:
        print(x , y , sep = ' ... ')
'''o/p: 10 ... Hyd
        20 ... Sec
        15 ... Cyb
        18 ... Pune
        '''        


'''
1) What  does  items()  method  do  --->  Returns  dict_items  object  which  has  list  of  tuples

2) What  are  the  two  elements  of  each  tuple ?  --->  (key , value)
'''
# Find  outputs (Home  work)
a = {10 : 'Hyd' , 20 : 'Sec' , 15 : 'Cyb' , 18 : 'Pune'}
for  x , y   in  a . items():
       print(x , y , sep = ' ... ') 
'''o/p: 10 ... Hyd
        20 ... Sec
        15 ... Cyb
        18 ... Pune
        '''         
'''for  x , y   in  a . keys():
       print(x , y , sep = ' ... ') # Error: cannot unpack non-iterable int object
for  x , y   in  a . values():
       print(x , y , sep = ' ... ')
for  x , y   in  a:
       print(x , y , sep = ' ... ')'''
# clear()  method  demo  program (Home  work)
a = {10 : 20 , 30 : 40 , 50 : 60}
print(a) # {10 : 20 , 30 : 40 , 50 : 60}
a . clear()
print(a) # {}
del  a
#print(a) # Error
# copy()  method demo  program  (Home  work)
a = {'R' : 'Red' , 'G' : 'Green' , 'B' : 'Blue'}
b = a . copy()
print(b) # {'R': 'Red', 'G': 'Green', 'B': 'Blue'}
print(a  is  b) # False
print(a  ==  b) # True
#  Find  outputs  (Home  work)
a = {10 : 'Rama' , 20 : 'Sita' , 15 : 'Rajesh'}
x , y , z = a . keys()
print(x) # 10
print(y) # 20
print(z) # 15
print()
x , y , z = a . values()
print(x) # Rama
print(y) # Sita
print(z) # Rajesh
print()
x , y ,  z = a . items()
print(x) # (10,'Rama')
print(y) # (20, 'Sita')
print(z) # (15, 'Rajesh')
print()
(rno1 , sname1) , (rno2 , sname2) , (rno3 , sname3) = a . items()
print(rno1 , sname1) # 10 Rama
print(rno2 , sname2) # 20 Sita
print(rno3 , sname3) # 15 Rajesh
'''
(Home  work)
Write  a program  to  determine  frequency  of  each  alphabet  in  the  string   in   alphabetical  order  (ignoring  the  case)

Let  input  be   RamA raO
What  is  the  output ?  ---> {'A' : 3 , 'M' : 1 , 'O' : 1 , 'R' : 2}  in  alphabetical  order

Hint: Use  get()  method 


1) a = { }

2) a['R'] = a . get('R' , 0) + 1 = 0 + 1 = 1
    What  does  a['R']  =  1  do ?  ---> Appends  'R' : 1  to  dict  'a'
    What  is  dictionary  'a' ?  ---> {'R' : 1}

3) a['A'] = a . get('A' , 0) + 1 =  0 + 1 = 1
    What  does  a['A']  =  1  do ?  ---> Appends  'A' : 1  to  dict  'a'
    What  is  dictionary  'a' ?  ---> {'R' : 1 , 'A' : 1}

4) a['M'] = a . get('M' , 0) + 1 =  0 + 1 = 1
    What  does  a['M']  =  1  do ?  --->  Appends  'M' : 1  to  dict…
Enter  mixed  case  string : RamA raO
{'A': 3, 'M': 1, 'O': 1, 'R': 2}  '''

a = 'RamA raO'
a = a.upper()
b = {}

for x in a:
       if x.isalpha():
              b[x] = b.get(x,0) + 1
c = dict(sorted(b.items()))
print(c)      
# o/p: {'A': 3, 'M': 1, 'O': 1, 'R': 2}        


# Find outputs (Home  work)
a = [ ('R' , 'Red') , ('G' , 'Green') , ('B' , 'Blue')]
b = {'Y' : 'Yellow', 'G' : 'Gray'}
#b . update(a) # # Error: 'list' object has no attribute 'update'
#print(b) # # Error: 'list' object has no attribute 'update'
#a . update(b)
#  Find  outputs  (Home  work)
a = [ (10 , 20 , 30) , (40 , 50 , 60) , (70 , 80 , 90)]
b = {}
#b.update(a) # Error: dictionary update sequence element #0 has length 3; 2 is required
print(b) # {}
c = [(10,) , (20,) , (30,)]
#b . update(c) # Error: dictionary update sequence element #0 has length 1; 2 is required
print(b) # {}
#  Find  outputs (Home  work)
d = {x : x ** 3   for    x   in  range(5)}
print(d) #{0: 0, 1: 1, 2: 8, 3: 27, 4: 64}
print(type(d)) # <class 'dict'>
# Find outputs   (Home  work)
d = { x :  2 * x    for    x   in   range(5) }
print(d) # {0: 0, 1: 1, 2: 8, 3: 27, 4: 64}
# Find outputs  (Home  work)
a = {10 : 'Rama' , 15 : 'Sita' , 18 : 'Rajesh' , 17 : 'Kiran' , 12 : 'Rama Rao'}
b = { k :  v  for   k , v  in   a .items()   if    k % 2 != 0}
print(b) # {15: 'Sita', 17: 'Kiran'}
c = {k : a[k]   for   k   in    a    if   a[k] . startswith('R')}
print(c) # {10: 'Rama', 18: 'Rajesh', 12: 'Rama Rao'}
