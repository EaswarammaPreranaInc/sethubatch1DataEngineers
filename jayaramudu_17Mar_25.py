# Ex-1
# difference()   method  demo  program  (Home  work)
a = {10 , 20 , 30 , 40}
b = {30 , 40 , 50 , 60}
c = a . difference(b) # which elements are not present set b {10,20}
print(c) # {10,20}
print(type(c)) # class set
d = a - b  # {10,20}
print(d) # {10,20}
print(type(d)) # class set
print(c  is  d) # False because reference comparison mutable objects are not reusable
print(c  ==  d) # True because values compare
print()


Ex-2
# symmetric_difference()   method  demo  program  (Home  work)
a = {10 , 20 , 30 , 40}
b = {30 , 40 , 50 , 60}
c = a . symmetric_difference(b) # return all the elements of a and b without common elements {10,20,50,60}
print(c) # {10,20,50,60} print any ordered
print(type(c)) # class set
d = a ^ b # return all the elements of a and b without common elements {10,20,50,60}
print(d) # {10,20,50,60}
print(type(d)) # class set
print(c   is   d) # False
print(c  ==   d) # True
print()

Ex-3
# Find  outputs  (Home  work)
a = {x * x  for   x   in   range(10)}
print(a) # {0,1,4,9,16,25,36,49,64,81} in any ordered
print(type(a)) # class set
print()


Ex-4

'''
(Home  work)
Write  a  program  to  remove  duplicate  characters  of  the  string  using  set

1) Let  input  be   Rama  Rao
    What  is  the  output  ? --->  Ram<space>o

2) Both  input  and  output  are  strings

3) How  to  convert  string  to  set  ?  --->  set(string)
    How  to  convert  set  to  string ?  ---> '' . join(set)

4) What  is  the  result  of  str({'H' , 'y' , 'd'})  ? --->  "{'H' , 'y' , 'd'}"  but  not 'Hyd'
'''
a = input('Enter a string: ')
b =set(a)
c = ''.join(b)
print(c)
print()

Ex-5
'''
Write  a  program  to  print  distinct  vowels  of  the  string  by  using  set

1) Let  input  be  RamA  Rao
   What  is  the  output  ?  ---> AO  (case  is  ignored)

2) Both  input  and  output  are  strings

3) Hint:  Same  as  prog19  with  minor changes
'''
a = input('Enter a string: ')
a=a.upper()
out = ''
for x in a:
    if x in 'AEIOU':
       if x not in out:
           out +=x
b =set(out)
c = ''.join(b)
print(c)
print()


Ex-6
'''
Write  a  program  to  remove  duplicate  elements  of   list  using  set

1) Let  input  be  [False , 25 , 10.8 , 1  , 25 , 0 , 'Hyd' ,  10.8 , 1.0 , None , 'Sec' , 'Hyd' , True  ]
    What  is  the  output ?  --->	[False , 25 , 10.8 , 1 , 'Hyd' , None , 'Sec']

2) Both  input  and  output  are lists
'''
a = eval(input('Enter a list of elements: '))
print(a)
b = set(a)
c = list(b)
print(c)
print()


Ex-8
'''
Write  a  program  to   obtain  common  elements  between  two  lists  using  sets

1) Let  1st  list  be  [10 , 20 , 30 , 40 , 50 , 60]  and  2nd  list  be  [30 , 40 , 70 , 80 , 20]
    What  is  the  output ?  --->	[20 , 30 , 40]

2) Both  input  and  output  are lists
'''

a= eval(input('Enter any String: '))
b = eval(input('Enter any String: '))
c = set(a)
e = c.intersection(b)
print(e)
print()


Ex-9
#  How  to  access  values  of  dictionary (Home  work)
a  =  {'Empno'  :  25 ,  'Ename'  :  'Rama  Rao'  ,  'Sal'  :  1000.65  }
print(a['Empno']) #How  to  print  value  25  in  dict  'a')
print(a['Ename']) #How  to  print  'Rama Rao'  in  dict  'a')
print(a['Sal'])  #How  to  print  value  1000.65 in dict 'a')
print()

Ex-10
# How  to  modify  values  of  dictionary  (Home  work)
a  =  {'Empno'  :  25,  'Ename'  :  'Rama  Rao'  ,  'Sal'  :  1000.65  }
print(a) # {'Empno'  :  25,  'Ename'  :  'Rama  Rao'  ,  'Sal'  :  1000.65  }
print(id(a)) # some random address may be 1000
a['Sal']= 2000  #  How  to  modify  1000.65  to  2000
a['Ename']='Sita' #How  to  modify  'Rama  Rao'  to  'Sita'
a['Empno']= 35  #How  to  modify  25   to  35
print(a) # {'Empno': 35, 'Ename': 'Sita', 'Sal': 2000}
print(id(a)) # same address
print()

Ex-10
#  How  to  append  key : value  pairs  to dictionary  (Home  work)
a  =  {'Empno'  :  25,  'Ename'  :  'Rama  Rao'  ,  'Sal'  :  1000.65  }
print(a) # {'Empno'  :  25,  'Ename'  :  'Rama  Rao'  ,  'Sal'  :  1000.65  }
a['Gender']='M' #How  to  append  'Gender' : 'M'  to  dictionary  'a'
a['Married'] = True #How  to  append  'Married' :  True  to  dictionary 'a'
print(a) # {'Empno': 25, 'Ename': 'Rama  Rao', 'Sal': 1000.65, 'Gender': 'M', 'Married': True}
print()

Ex-11
# Find  outputs (Home  work)
a = { }
a[10]='Rama' #  How  to  append  10 : 'Rama'  to  dictionary  'a'
a[20]='Sita' # How  to  append  20 : 'Sita'  to  dictionary  'a'
a[15]='Rajesh' # How  to  append  15 : 'Rajesh'  to  dictionary  'a'
a[18]='Kiran' #  How  to  append  18 : 'Kiran'  to  dictionar 'a'
print(a) # {10: 'Rama', 20: 'Sita', 15: 'Rajesh', 18: 'Kiran'}
print()

Ex-12
#  How  to  remove  key : value  pairs  of  dictionary  (Home  work)
a =  {'Empno'  :  25,  'Ename'  :  'Rama  Rao'  ,  'Sal'  :  1000.65  }
print(a)
a.pop('Sal')   # How  to  remove  'Sal' : 1000.65  from  dictionary 'a'
print(a) # {'Empno': 25, 'Ename': 'Rama  Rao'}
print()

Ex-13
#  in  and  not  in  operators  (Home  work)
a =  {10 : 20 , 30 : 40 , 50 : 60 , 70 : 80}
print(30  in  a . keys()) # True
print(60  in  a . keys()) # False
print(60  in  a . values()) # True
print(30  in  a . values()) # False
print(50  in  a) # True
print(20  in  a) # False
print(70  not  in  a . keys()) # False
print(40  not  in  a . values()) # False
print(25 not  in a) # True
print()


Ex-14
#  What  are  the  outputs  if  input  is  {10: 'A', 20: 'B', 15: 'C' , 20 : 'D'}
a = input('Enter  dictionary  :  ')
print(a) # '{10: 'A', 20: 'B', 15: 'C' , 20 : 'D'}'
print(type(a)) # class str
b = eval(a) # {10: 'A', 20: 'B', 15: 'C' , 20 : 'D'}
print(b) # {10: 'A', 20: 'B', 15: 'C' , 20 : 'D'}
print(type(b)) # class dict
print()


Ex-15
#  Find  outputs  (Home  work)
a = {10 : 'Rama' , 20 : 'Sita' , 15 : 'Rajesh' , 18 : 'Kiran'}
b = {**a} # it   dict_items , with key and value pairs {10 : 'Rama' , 20 : 'Sita' , 15 : 'Rajesh' , 18 : 'Kiran'}
print(b) # {10 : 'Rama' , 20 : 'Sita' , 15 : 'Rajesh' , 18 : 'Kiran'}
print(a  is  b) # False
print(a  ==  b) # True
c = a #  c  is point to a ,a point to set object ,c also point to same set object
print(a  is   c) # True
print(a  == c) # True
print()


Ex-16
#Find  outputs  (Home  work)
a = {10 : 'Rama' , 20 : 'Sita' , 15 : 'Rajesh'}
b = {18 : 'Kiran' , 14 : 'Amar' , 20  : 'Manohar'}
c = {25 : 'Ramesh' , 19 : 'Krishna' , 15 : 'Radha' , 14 : 'Srinivas'}
d = {*a , *b , *c} # unpacking keys from a, b, c
print(d) # {10, 14, 15, 18, 19, 20, 25}
print(type(d)) # class set
e = {**a , **b , **c} # unpacking key and value paires from a, b, c  with a new dict {10: 'Rama', 20: 'Manohar', 15: 'Radha', 18: 'Kiran', 14: 'Srinivas', 25: 'Ramesh', 19: 'Krishna'}
print(e) # {10: 'Rama', 20: 'Manohar', 15: 'Radha', 18: 'Kiran', 14: 'Srinivas', 25: 'Ramesh', 19: 'Krishna'}
print(type(e)) # class dict
print()


Ex-17
#  Find  outputs  (Home  work)
a = {10 : 20 , 30 : 40}
b = {30 : 50 , 10 : 60}
# print(a + b)   # not support for + when concat two dict
c = {**a , **b} # unpacking a, b  and form new dict with unique keys {10:60,30:50}
print(c) # # {10:60,30:50}
d =a | b # {10:60,30:50}
print(d) # {10:60,30:50}
print()


Ex-18

'''
(Home  work)
Write  a  program  to  create  a  dictionary  with  emp  names  and  salaries

Hint:  Append  each  emp  name  and  salary  to  dictionary  'a'

'''
l = int(input('How many Employees ? : '))
a = {}
count = 0
while count < l:
    b = eval(input('Enter Emp Name :'))
    c = eval(input('Enter Salary : '))
    a[b] = c

    count +=1
print(a)
print()

Ex-19
''' (Home  work)
Write  a  program  to  convert  a  string  to  dictionary

Let  input  be   "Emp no = 25 , Emp name = Rama  Rao , sal = 10000.0 , gender = m"

What  is  the  output ?  --->  {Emp no : 25 , Emp name  :  Rama Rao , sal : 10000.0 , gender : m}

Hint :  Use  split()  method  twice
'''

# a =  "Emp no = 25 , Emp name = Rama  Rao , sal = 10000.0 , gender = m"
# b = ['Emp no = 25' , 'Emp name = Rama  Rao' , 'sal = 10000.0' , 'gender = m']
# c = {}
# x =  'Emp no = 25'  --->  ['Emp  no' , '25']  ---> {'Emp  no': '25'}
# x = 'Emp name = Rama  Rao'  --->  ['Emp name' , 'Rama  Rao']  --->  {'Emp  no': '25' , 'Emp  name':'Rama Rao'}}
a = input('Enter a string: ')
b = a.split(',')
d = {}
for x in b:
    c = x.split('=')
    d[c[0]]=c[1]
print(d)
print()


Ex-20

# len()  function  demo  program  (Home  work)
a  =  {'Empno'  :  25,  'Ename'  :  'Rama  Rao'  ,  'Sal'  :  1000.65  }
print(len(a)) # 3
b = {} # empty dict
print(len(b)) # 0
print()


Ex-21
#  sum()  function demo  program  (Home  work)
a = {10 : 20 , 30 : 40 , 50 : 60}
print(sum(a . keys()))  # sum(10,30,50) = 90
print(sum(a . values())) # sum(20,40,60) = 120
print(sum(a))  # sum(10,30,50) = 90
print(sum(a.items())) # Error because it gives list of tuples , sum()` cannot directly add tuples
print()

Ex-22
# max()  and  min()   functions  demo  program  (Home  work)
a = {10 : 20 , 30 : 25 , 40 : 5 , 7 : 28 , 9 : 50}
print(max(a.keys()))   # max(10, 30, 40, 7, 9) = 40
print(min(a.keys()))   # min(10, 30, 40, 7, 9) = 7
print(max(a.values())) # max(20, 25, 5, 28, 50) = 50
print(min(a.values())) # min(20, 25, 5, 28, 50) = 5
print(max(a.items()))  # max based on key: (40, 5)
print(min(a.items()))  # min based on key: (7, 28)
print(max(a))          # max key directly: 40
print(min(a))          # min key directly: 7
print()


Ex-23
#  dict()  function  demo program (Home  work))
a = [ (10 , 'Hyd') , (20 , 'Sec') , (15 , 'Cyb') , (20 , 'Pune')]  #  List of  tuples
b = dict(a) #  Converts  list  of  tuples  to  dict
print(b)  #  {10 : 'Hyd', 20 : 'Pune' , 15 : 'Cyb'}
c = ( ['R' , 'Red'] , ['G' , 'Green'] , ['B' , 'Blue'] , ['G' , 'Gray'])
d = dict(c) # converts tuple of lists to dict {'R': 'Red', 'G': 'Gray', 'B': 'Blue'}
print(d) # {'R': 'Red', 'G': 'Gray', 'B': 'Blue'}
e = [[10 , 20 , 30] , [40 , 50 , 60] , [70 , 80 , 90]]
#print(dict(e)) # dict() requires an iterable of two-element sequences but has 3
f = [[10] , [20] , [30]]
#print(dict(f)) # dict() requires an iterable of two-element sequences but has 1
# print(dict([10 , 20])) # [10, 20] contains individual integers, not key-value pairs, so dict() cannot convert it.
g = [[10 , [20 , 30]] , [40 , [50 , 60]] , [70 , [80 , 90]]] #
print(dict(g)) # {10: [20, 30], 40: [50, 60], 70: [80, 90]}
h = [[[10 , 20] , 30] , [[40 , 50] , 60] , [[70 , 80] , 90]]
#print(dict(h)) # [10,20] this are mutable ,in dict keys must be unique
i = [[(10 , 20) , 30] , [(40 , 50) , 60] , [(70 , 80) , 90]]
print(dict(i)) # {(10, 20): 30, (40, 50): 60, (70, 80): 90}
print()

Ex-24
# sorted()  function  (Home  work)
a = {10 : 'Red' , 20 : 'Green' , 15 : 'Blue' , 18 : 'Yellow' , 5 : 'White'}
b = sorted(a . keys()) # [5,10,15,18,20]
print(b) # [5,10,15,18,20]
c = sorted(a . values()) # ['Blue','Green','Red','White','Yellow']
print(c) # ['Blue','Green','Red','White','Yellow']
d = sorted(a . items()) # [(5, 'White'), (10, 'Red'), (15, 'Blue'), (18, 'Yellow'), (20, 'Green')]
print(d) # [(5, 'White'), (10, 'Red'), (15, 'Blue'), (18, 'Yellow'), (20, 'Green')]
f  = sorted(a  , reverse = True)
print(f) # [20, 18, 15, 10, 5]
print(a) # {10: 'Red', 20: 'Green', 15: 'Blue', 18: 'Yellow', 5: 'White'}
print()

Ex-25
'''
Gift
Write  a  program  to  sort  dictionary  wrt  keys  (Home  work)

1) Let  input  be   {10 : 'A' , 20 : 'B' , 15 : 'C' , 5 : 'D' , 12 : 'E'}
    What  is  the  output ?  ---> {5 : 'D' , 10 : 'A' ,  12 : 'E' ,  15 : 'C' , 20 : 'B'}

2) Both  input  and  output  are  dictionaries

3) Hint:  Use  sorted()  function

4) a = {10 : 'A' , 20 : 'B' , 15 : 'C' , 5 : 'D' , 12 : 'E'}
    b = sorted(a . items())  --->  [(5 , 'D' ) , (10 , 'A') , (12 , 'E') , (15 , 'C') , (20, 'B')]
    dict(b)  --->  {5 : 'D' , 10 : 'A',.....}
'''
a = eval(input("Enter a dictionary: "))
b = dict(sorted(a.items()))
print(b)
print()


Ex-26

#  keys()  method  demo  program
a = {10 : 'Hyd' , 20 : 'Sec' , 15 : 'Cyb' , 18 : 'Pune'}
b = a . keys() # dict_keys([10,20,15,18])
print(b) # dict_keys([10,20,15,18])
print(type(b)) #class dict_keys
for  x  in   b:
        print(x) # 10 <nl> 20 <nl> 15 <nl> 18
print()

Ex-27
# values()  method  demo  program
a = {10 : 'Hyd' , 20 : 'Sec' , 15 : 'Cyb' , 18 : 'Pune'}
b = a . values() # dict_values(['Hyd','Sec','Cyb','Pune'])
print(b) #  dict_values(['Hyd','Sec','Cyb','Pune'])
print(type(b)) #  dict_values
for  x   in   b:
	print(x) # 'Hyd' <nl> 'Sec' <nl> 'Cyb' <nl> 'Pune']
print()

Ex-28
#  items()  method  demo  program
a = {10 : 'Hyd' , 20 : 'Sec' , 15 : 'Cyb' , 18 : 'Pune'}
b = a . items() # dict_items([(10, 'Hyd'), (20, 'Sec'), (15, 'Cyb'), (18, 'Pune')])
print(b) # [(10, 'Hyd'), (20, 'Sec'), (15, 'Cyb'), (18, 'Pune')]
print(type(b))  # # dict_items
for  x   in   b:
        print(x) # (10,'Hyd') <nl> (20,'Sec') <nl> (15,'Cyb') <nl> (18,'Pune')
for  x , y   in  b:
        print(x , y , sep = ' ... ')  # 10 ... Hyd <nl> 20 ... Sec <nl> 15 ... Cyb <nl> 18 ... Pune
print()

Ex-29
# Find  outputs (Home  work)
a = {10 : 'Hyd' , 20 : 'Sec' , 15 : 'Cyb' , 18 : 'Pune'}
for  x , y   in  a . items():
       print(x , y , sep = ' ... ') # 10 ... Hyd <nl> 20 ... Sec <nl> 15 ... Cyb <nl> 18 ... Pune
# for  x , y   in  a . keys():
      # print(x , y , sep = ' ... ') # Error because a.keys contain single element but have 2
#for  x , y   in  a . values():
       #print(x , y , sep = ' ... ') # Error because a.values contain single element but have 2
#for  x , y   in  a:
       #print(x , y ,sep='...') # Error because a by default a.keys() contain single element but have 2
print()


Ex-30
# clear()  method  demo  program (Home  work)
a = {10 : 20 , 30 : 40 , 50 : 60}
print(a) # {10 : 20 , 30 : 40 , 50 : 60}
a . clear() # remove all key and value pairs
print(a) # {}
del a # delete dict a
#print(a) # not defined
print()


Ex-31
# copy()  method demo  program  (Home  work)
a = {'R' : 'Red' , 'G' : 'Green' , 'B' : 'Blue'}
b = a . copy() # create new object dict b
print(b) # {'R' : 'Red' , 'G' : 'Green' , 'B' : 'Blue'}
print(a  is  b) # False
print(a==b) # True
print()

Ex-32
#  Find  outputs  (Home  work)
a = {10 : 'Rama' , 20 : 'Sita' , 15 : 'Rajesh'}
x , y , z = a . keys() # [10,20,15]
print(x) # 10
print(y) # 20
print(z) # 15
print()
x , y , z = a . values() #['Rama','Sita','Rajesh']
print(x) # 'Rama'
print(y) # 'Sita'
print(z) # 'Rajesh'
print()
x , y ,  z = a . items() # [(10 ,'Rama') ,(20 , 'Sita' ), (15 ,'Rajesh')]
print(x) # (10 ,'Rama')
print(y) # (20 , 'Sita' )
print(z) # (15 ,'Rajesh')
print()
(rno1 , sname1) , (rno2 , sname2) , (rno3 , sname3) = a . items() # [(10 ,'Rama') ,(20 , 'Sita' ), (15 ,'Rajesh')]
print(rno1 , sname1) # 10 Rama
print(rno2 , sname2) # 20 Sita
print(rno3,sname3) # 15 Rajesh
print()

Ex-33
'''
(Home  work)
Write  a program  to  determine  frequency  of  each  alphabet  in  the  string   in   alphabetical  order  (ignoring  the  case)

Let  input  be   RamA raO
What  is  the  output ?  ---> {'A' : 3 , 'M' : 1 , 'O' : 1 , 'R' : 2}  in  alphabetical  order

Hint: Use  get()  method

a['R'] = a . get('R' , 0) + 1 = 0 + 1 = 1
    What  does  a['R']  =  1  do ?  ---> Appends  'R' : 1  to  dict  'a'
    What  is  dictionary  'a' ?  ---> {'R' : 1}

'''
a = input("Enter a string : ")
a = a.upper()
b = {}
for x in a:
    if x !=' ':
        b[x]=b.get(x,0)+1
print(b)
print()

Ex-34
# Find outputs (Home  work)
a = [ ('R' , 'Red') , ('G' , 'Green') , ('B' , 'Blue')]
b = {'Y' : 'Yellow', 'G' : 'Gray'}
b . update(a) # merge two dict a and b with unique keys # {'Y': 'Yellow', 'G': 'Green', 'R': 'Red', 'B': 'Blue'}
print(b)
#a.update(b) # list does not have a update method
print()

Ex-35
#  Find  outputs  (Home  work)
a = [ (10 , 20 , 30) , (40 , 50 , 60) , (70 , 80 , 90)]
b = {}
#b.update(a) # Error because list a have tuple of three elements but required only tuple two elements
print(b) # {}
c = [(10,) , (20,) , (30,)]
#b . update(c) # Error because list a have tuple of 1 element but required only tuple two elements
print(b) # {}
print()

Ex-36
#  Find  outputs (Home  work)
d = {x : x ** 3   for    x   in  range(5)}
print(d) #  {0: 0, 1: 1, 2: 8, 3: 27, 4: 64}
print(type(d)) # class dict
print()

Ex-37
# Find outputs   (Home  work)
d = { x :  2 * x    for    x   in   range(5)}
print(d) # {0: 0, 1: 2, 2: 4, 3: 6, 4: 8}
print()

Ex-38
# Find outputs  (Home  work)
a = {10 : 'Rama' , 15 : 'Sita' , 18 : 'Rajesh' , 17 : 'Kiran' , 12 : 'Rama Rao'}
b = { k :  v  for   k , v  in   a .items()   if    k % 2 != 0} # {15: 'Sita', 17: 'Kiran'}
print(b) # {15: 'Sita', 17: 'Kiran'}
c = {k : a[k]   for   k   in    a    if   a[k] . startswith('R')} # {10: 'Rama', 18: 'Rajesh', 12: 'Rama Rao'}
print(c) # {10: 'Rama', 18: 'Rajesh', 12: 'Rama Rao'}
