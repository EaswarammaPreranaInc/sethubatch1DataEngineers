# symmetric_difference()   method  demo  program  (Home  work)
a = {10 , 20 , 30 , 40}
b = {30 , 40 , 50 , 60}
c = a . symmetric_difference(b)
print(c)
print(type(c))
d = a ^ b
print(d)
print(type(d))
print(c   is   d)
print(c  ==   d)
## difference()   method  demo  program  (Home  work)
a = {10 , 20 , 30 , 40}
b = {30 , 40 , 50 , 60}
c = a . difference(b)
print(c)
print(type(c))
d = a - b
print(d)
print(type(d))
print(c  is  d)
print(c  ==  d)
# Find  outputs  (Home  work)
a = {x * x  for   x   in   range(10)}
print(a) #{0,1,4,9,16,25,36,49,64,81}
print(type(a)) #<class 'set'>
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
s=input("enter input:")
b=set(s)
j=str(b)
k=''.join(b)
print("output using join method: ",k,"\n output using str method: ",b)
'''
Write  a  program  to  print  distinct  vowels  of  the  string  by  using  set

1) Let  input  be  RamA  Rao
   What  is  the  output  ?  ---> AO  (case  is  ignored)

2) Both  input  and  output  are  strings

3) Hint:  Same  as  prog19  with  minor  changes
'''
s=input("enter input:")
v=['A','E','I','O','U']
g=set()
for i in s.upper():
    if i in v:
        g.add(i)

k=sorted(list(g))
m="".join(k)
print(m)
'''
Write  a  program  to  remove  duplicate  elements  of   list  using  set

1) Let  input  be  [False , 25 , 10.8 , 1  , 25 , 0 , 'Hyd' ,  10.8 , 1.0 , None , 'Sec' , 'Hyd' , True  ]
    What  is  the  output ?  --->	[False , 25 , 10.8 , 1 , 'Hyd' , None , 'Sec']

2) Both  input  and  output  are  lists
'''
a=eval(input("enter list:"))
b=set(a)
print(list(b))
'''
Write  a  program  to   obtain  common  elements  between  two  lists  using  sets

1) Let  1st  list  be  [10 , 20 , 30 , 40 , 50 , 60]  and  2nd  list  be  [30 , 40 , 70 , 80 , 20]
    What  is  the  output ?  --->	[20 , 30 , 40]

2) Both  input  and  output  are  lists
'''
a=eval(input("enter  1st list:"))
b=eval(input("enter 2nd list:"))
k,m=set(a),set(b)
c=k&m
print(list(c))
#  How  to  access  values  of  dictionary (Home  work)
a  =  {'Empno'  :  25 ,  'Ename'  :  'Rama  Rao'  ,  'Sal'  :  1000.65  }
k=list(a.values())
print("How  to  print  value  25  in  dict  'a'",k[0])
print("How  to  print  'Rama Rao'  in  dict  'a'",k[1])
print("How  to  print  value  1000.65   in  dict  'a'",k[2])
# How  to  modify  values  of  dictionary  (Home  work)
a  =  {'Empno'  :  25,  'Ename'  :  'Rama  Rao'  ,  'Sal'  :  1000.65  }
print(a)
print(id(a))
a['Empno']=35
a['Ename']='Sita'
a['Sal']=2000
print("How  to  modify  1000.65  to  2000",a['Sal'])
print("How  to  modify  'Rama  Rao'  to  'Sita'",a['Ename'])
print("How  to  modify  25   to  35",a['Empno'])
print(a)
print(id(a))
#  How  to  append  key : value  pairs  to dictionary  (Home  work)
a  =  {'Empno'  :  25,  'Ename'  :  'Rama  Rao'  ,  'Sal'  :  1000.65  }
print(a)
a.update({'Gender':'M','Married':True})
#How  to  append  'Gender' : 'M'  to  dictionary  'a'
#How  to  append  'Married' :  True  to  dictionary  'a'
print(a)
# Find  outputs (Home  work)
a = { }
a.update({10:'Rama'})
a.setdefault(20,'Sita')
a.setdefault(30,'Rajesh')
a.setdefault(40,'Kiran')
#How  to  append  10 : 'Rama'  to  dictionary  'a'
#How  to  append  20 : 'Sita'  to  dictionary  'a'
#How  to  append  15 : 'Rajesh'  to  dictionary  'a'
#How  to  append  18 : 'Kiran'  to  dictionary  'a'
print(a)
#  How  to  remove  key : value  pairs  of  dictionary  (Home  work)
a =  {'Empno'  :  25,  'Ename'  :  'Rama  Rao'  ,  'Sal'  :  1000.65  }
print(a)
a.pop('Sal')
#a.popitem('Empno') # pops item from the end of the dictionary & it doesn't take any arguments
#How  to  remove  'Sal' : 1000.65  from  dictionary  'a'
print(a)
#  in  and  not  in  operators  (Home  work)
a =  {10 : 20 , 30 : 40 , 50 : 60 , 70 : 80}
print(30  in  a . keys()) #True
print(60  in  a . keys()) #False
print(60  in  a . values()) #True
print(30  in  a . values()) #False
print(50  in  a) #True
print(20  in  a) #False
print(70  not  in  a . keys()) #False
print(40  not  in  a . values()) #False
print(25  not  in  a) #True
#  What  are  the  outputs  if  input  is  {10: 'A', 20: 'B', 15: 'C' , 20 : 'D'}
a = input('Enter  dictionary  :  ')
print(a) 
print(type(a))
b = eval(a)
print(b)
print(type(b))
'''Enter  dictionary  :   {10: 'A', 20: 'B', 15: 'C' , 20 : 'D'}
{10: 'A', 20: 'B', 15: 'C' , 20 : 'D'}
<class 'str'>
{10: 'A', 20: 'D', 15: 'C'}
<class 'dict'>'''
##  Find  outputs  (Home  work)
a = {10 : 'Rama' , 20 : 'Sita' , 15 : 'Rajesh' , 18 : 'Kiran'}
b = {**a}
print(b)
print(a  is  b) #False
print(a  ==  b) #True
c = a
print(a  is   c) #True
print(a  ==  c) #True
#  Find  outputs  (Home  work)
a = {10 : 20 , 30 : 40}
b = {30 : 50 , 10 : 60}
#print(a + b)
c = {**a , **b}
print(c)
d = a | b
print(d)
#Find  outputs  (Home  work)
a = {10 : 'Rama' , 20 : 'Sita' , 15 : 'Rajesh'}
b = {18 : 'Kiran' , 14 : 'Amar' , 20  : 'Manohar'}
c = {25 : 'Ramesh' , 19 : 'Krishna' , 15 : 'Radha' , 14 : 'Srinivas'}
d = {*a , *b , *c}
print(d)
print(type(d))
e = {**a , **b , **c}
print(e)
print(type(e))
'''
(Home  work)
Write  a  program  to  create  a  dictionary  with  emp  names  and  salaries

Hint:  Append  each  emp  name  and  salary  to  dictionary  'a'
'''
a={}
n=int(input("How many Employees ? :"))
for i in range(n):
    e=input("Enter Emp Name :")
    s=input("Enter Salary :")
    #a.update({e:s})
    #a.setdefault({e:s})
    a[e]=s
print(a)
''' (Home  work)
Write  a  program  to  convert  a  string  to  dictionary

Let  input  be   "Emp no = 25 , Emp name = Rama  Rao , sal = 10000.0 , gender = m"

What  is  the  output ?  --->  {Emp no : 25 , Emp name  :  Rama Rao , sal : 10000.0 , gender : m}

Hint :  Use  split()  method  twice
'''
a=input()
c=a.split(",")
print(c)
d={}
for i in c:
    k=(i.split('='))
    d[k[0]]=k[1]
print(d)
# len()  function  demo  program  (Home  work)
a  =  {'Empno'  :  25,  'Ename'  :  'Rama  Rao'  ,  'Sal'  :  1000.65  }
print(len(a))
b = {}
print(len(b))
#  sum()  function demo  program  (Home  work)
a = {10 : 20 , 30 : 40 , 50 : 60}
print(sum(a . keys()))
print(sum(a . values()))
print(sum(a))
#print(sum(a . items()))   error as the items are tuple of key values and cannot be added using sum
# max()  and  min()   functions  demo  program  (Home  work)
a = {10 : 20 , 30 : 25 , 40 : 5 , 7 : 28 , 9 : 50}
print(max(a . keys()))#40
print(min(a . keys()))#7
print(max(a . values()))#50
print(min(a . values()))#5
print(max(a . items()))#(40, 5)
print(min(a . items()))#(7, 28)
print(max(a)) #40
print(min(a))#7
#  dict()  function  demo program (Home  work))
a = [ (10 , 'Hyd') , (20 , 'Sec') , (15 , 'Cyb') , (20 , 'Pune')]  #  List of  tuples
b = dict(a) #  Converts  list  of  tuples  to  dict
print(b)  #  {10 : 'Hyd', 20 : 'Pune' , 15 : 'Cyb'}
c = ( ['R' , 'Red'] , ['G' , 'Green'] , ['B' , 'Blue'] , ['G' , 'Gray'])
d = dict(c)
print(d)
e = [[10 , 20 ] , [40 , 50 ] , [70 , 80 ]]
print(dict(e))
f = [[10,20]]
print(dict(f))
print(dict([{10 , 20}])) #will not accept if its given as tuple of single element other sequences 
g = [[10 , [20 , 30]], [40 , [50 , 60]] , [70 , [80 , 90]]]
print(dict(g))
#h = [[[10 , 20] , 30] , [[40 , 50] , 60] , [[70 , 80] , 90]]
#print(dict(h))
i = [[(10 , 20) , 30] , [(40 , 50) , {50}] , [(70 , 80) , 90]]
print(dict(i))
# sorted()  function  (Home  work)
a = {10 : 'Red' , 20 : 'Green' , 15 : 'Blue' , 18 : 'Yellow' , 5 : 'White'}
b = sorted(a . keys()) #keys
print(b)
c = sorted(a . values()) #valu4s
print(c)
d = sorted(a . items()) #keyvalu but key as they come first
print(d)
f  = sorted(a  , reverse = True) #keys
print(f)
print(a)
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
a=eval(input("a:"))
b=sorted(a.items())
print(dict(b))
#  keys()  method  demo  program
a = {10 : 'Hyd' , 20 : 'Sec' , 15 : 'Cyb' , 18 : 'Pune'}
b = a . keys()
print(b)
print(type(b))
for  x  in   b:
        print(x)
'''dict_keys([10, 20, 15, 18])
<class 'dict_keys'>
10
20
15
18'''
# values()  method  demo  program
a = {10 : 'Hyd' , 20 : 'Sec' , 15 : 'Cyb' , 18 : 'Pune'}
b = a . values()
print(b)
print(type(b))
for  x   in   b:
	print(x)
'''dict_values(['Hyd', 'Sec', 'Cyb', 'Pune'])
<class 'dict_values'>
Hyd
Sec
Cyb
Pune'''
#  items()  method  demo  program
a = {10 : 'Hyd' , 20 : 'Sec' , 15 : 'Cyb' , 18 : 'Pune'}
b = a . items()
print(b)
print(type(b))
for  x   in   b:
        print(x)
for  x , y   in  b:
        print(x , y , sep = ' ... ')
'''dict_items([(10, 'Hyd'), (20, 'Sec'), (15, 'Cyb'), (18, 'Pune')])
<class 'dict_items'>
(10, 'Hyd')
(20, 'Sec')
(15, 'Cyb')
(18, 'Pune')
10 ... Hyd
20 ... Sec
15 ... Cyb
18 ... Pune'''
# clear()  method  demo  program (Home  work)
a = {10 : 20 , 30 : 40 , 50 : 60}
print(a)
a . clear()
print(a)
del  a
#print(a) it del obj a at all 
# copy()  method demo  program  (Home  work)
a = {'R' : 'Red' , 'G' : 'Green' , 'B' : 'Blue'}
b = a . copy()
print(b)
print(a  is  b)
print(a  ==  b)
'''
(Home  work)
Write  a program  to  determine  frequency  of  each  alphabet  in  the  string   in   alphabetical  order  (ignoring  the  case)

Let  input  be   RamA raO
What  is  the  output ?  ---> {'A' : 3 , 'M' : 1 , 'O' : 1 , 'R' : 2}  in  alphabetical  order

'''
a=input("dodo")
s=a.upper()
d={}
for i in set(s):
    s.count(i)
    
    d.update({i:s.count(i)})
print(d)
m=input("enter the alphabet you want to fetch")
d.get(m)
# Find outputs (Home  work)
a = [ ('R' , 'Red') , ('G' , 'Green') , ('B' , 'Blue')]
b = {'Y' : 'Yellow', 'G' : 'Gray'}
b . update(a) #{'Y': 'Yellow', 'G': 'Green', 'R': 'Red', 'B': 'Blue'}
print(b)
a . extend(b)
print(a) #[('R', 'Red'), ('G', 'Green'), ('B', 'Blue'), 'Y', 'G', 'R', 'B']
#  Find  outputs  (Home  work)
a = [ (10 , 20 , 30) , (40 , 50 , 60) , (70 , 80 , 90)]
b = {}
#b.update(a)
print(b)
c = [(10,) , (20,) , (30,)]
#b . update(c) # while updating the length of the inner sequence of object, C should be to 2
#print(b)
#  Find  outputs (Home  work)
d = {x : x ** 3   for    x   in  range(5)}
print(d)
print(type(d))
'''{0: 0, 1: 1, 2: 8, 3: 27, 4: 64}
<class 'dict'>'''
# Find outputs   (Home  work)
d = { x :  2 * x    for    x   in   range(5) }
print(d)
#{0: 0, 1: 2, 2: 4, 3: 6, 4: 8}
# Find outputs  (Home  work)
a = {10 : 'Rama' , 15 : 'Sita' , 18 : 'Rajesh' , 17 : 'Kiran' , 12 : 'Rama Rao'}
b = { k :  v  for   k , v  in   a .items()   if    k % 2 != 0}
print(b)
c = {k : a[k]   for   k   in    a    if   a[k] . startswith('R')}
print(c)
'''{15: 'Sita', 17: 'Kiran'}
{10: 'Rama', 18: 'Rajesh', 12: 'Rama Rao'}'''
