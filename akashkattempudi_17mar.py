# difference()   method  demo  program  (Home  work)
a = {10 , 20 , 30 , 40}
b = {30 , 40 , 50 , 60}
c = a . difference(b)
print(c) #{10,20}
print(type(c)) #<class 'set'>
d = a - b
print(d) #{10,20}
print(type(d)) #<class 'set'>
print(c  is  d) #False
print(c  ==  d) # True

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
'''
{10, 50, 20, 60}
<class 'set'>
{10, 50, 20, 60}
<class 'set'>
False
True'''


# Find  outputs  (Home  work)
a = {x * x  for   x   in   range(10)}
print(a)
print(type(a))
'''
{0,1,4,9,16,25,36,49,64,81} in any order
<class 'set'>'''

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
a = "Rama Rao"
b = set(a)
c= ''.join(b)
print(c)


'''
Write  a  program  to  print  distinct  vowels  of  the  string  by  using  set

1) Let  input  be  RamA  Rao
   What  is  the  output  ?  ---> AO  (case  is  ignored)

2) Both  input  and  output  are  strings

3) Hint:  Same  as  prog19  with  minor  changes
'''
a = "RamA Rao"
a = set(a.upper())
b = set("AEIOU")
c = a.intersection(b)
print("".join(c))

'''
Write  a  program  to  remove  duplicate  elements  of   list  using  set

1) Let  input  be  [False , 25 , 10.8 , 1  , 25 , 0 , 'Hyd' ,  10.8 , 1.0 , None , 'Sec' , 'Hyd' , True  ]
    What  is  the  output ?  --->	[False , 25 , 10.8 , 1 , 'Hyd' , None , 'Sec']

2) Both  input  and  output  are  lists
'''
a = [False , 25 , 10.8 , 1  , 25 , 0 , 'Hyd' ,  10.8 , 1.0 , None , 'Sec' , 'Hyd' , True  ]
a= list(set(a))
print(a)


'''
Write  a  program  to   obtain  common  elements  between  two  lists  using  sets

1) Let  1st  list  be  [10 , 20 , 30 , 40 , 50 , 60]  and  2nd  list  be  [30 , 40 , 70 , 80 , 20]
    What  is  the  output ?  --->	[20 , 30 , 40]

2) Both  input  and  output  are  lists
'''
a = [10 , 20 , 30 , 40 , 50 , 60]
b = [30 , 40 , 70 , 80 , 20]
c = list(set(a)&(set(b)))
print(c)

#  How  to  access  values  of  dictionary (Home  work)
a  =  {'Empno'  :  25 ,  'Ename'  :  'Rama  Rao'  ,  'Sal'  :  1000.65  }

# print(How  to  print  value  25  in  dict  'a')
print(a['Empno'])
# print(How  to  print  'Rama Rao'  in  dict  'a')
print(a['Ename'])
# print(How  to  print  value  1000.65   in  dict  'a')
print(a['Sal'])

# How  to  modify  values  of  dictionary  (Home  work)
a  =  {'Empno'  :  25,  'Ename'  :  'Rama  Rao'  ,  'Sal'  :  1000.65  }
print(a)
print(id(a))
a.update({'Empno':35})
a.update({'Ename':'Sita'})
a["Sal"]=2000
# How  to  modify  1000.65  to  2000
# How  to  modify  'Rama  Rao'  to  'Sita'
# How  to  modify  25   to  35
print(a)
print(id(a))

#  How  to  append  key : value  pairs  to dictionary  (Home  work)
a  =  {'Empno'  :  25,  'Ename'  :  'Rama  Rao'  ,  'Sal'  :  1000.65  }
print(a)
a.update({'Empno' : 35})
a.update({'Gender' : 'M'})
a.update({'Married' :  True})
# How  to  append  'Gender' : 'M'  to  dictionary  'a'
# How  to  append  'Married' :  True  to  dictionary  'a'
print(a)


# Find  outputs (Home  work)
a = { }
a.update({10 : 'Rama'})
a.update({20 : 'Sita'})
a.update({15 : 'Rajesh'})
a.update({18 : 'Kiran'})
# How  to  append  10 : 'Rama'  to  dictionary  'a'
# How  to  append  20 : 'Sita'  to  dictionary  'a'
# How  to  append  15 : 'Rajesh'  to  dictionary  'a'
# How  to  append  18 : 'Kiran'  to  dictionary  'a'
print(a)

#  How  to  remove  key : value  pairs  of  dictionary  (Home  work)
a =  {'Empno'  :  25,  'Ename'  :  'Rama  Rao'  ,  'Sal'  :  1000.65  }
print(a)
a.pop('Sal')
# How  to  remove  'Sal' : 1000.65  from  dictionary  'a'
print(a)


#  in  and  not  in  operators  (Home  work)
a =  {10 : 20 , 30 : 40 , 50 : 60 , 70 : 80}
print(30  in  a . keys())
print(60  in  a . keys())
print(60  in  a . values())
print(30  in  a . values())
print(50  in  a)
print(20  in  a)
print(70  not  in  a . keys())
print(40  not  in  a . values())
print(25  not  in  a)
'''
True
False
True
False
True
False
False
False
True'''

#  What  are  the  outputs  if  input  is  {10: 'A', 20: 'B', 15: 'C' , 20 : 'D'}
a = input('Enter  dictionary  :  ')
print(a)
print(type(a))
b = eval(a)
print(b)
print(type(b))
'''
Enter  dictionary  :  {10: 'A', 20: 'B', 15: 'C' , 20 : 'D'}
{10: 'A', 20: 'B', 15: 'C' , 20 : 'D'}
<class 'str'>
{10: 'A', 20: 'D', 15: 'C'}
<class 'dict'>'''


#  Find  outputs  (Home  work)
a = {10 : 'Rama' , 20 : 'Sita' , 15 : 'Rajesh' , 18 : 'Kiran'}
b = {**a}
print(b)
print(a  is  b)
print(a  ==  b)
c = a
print(a  is   c)
print(a  ==  c)
'''
{10: 'Rama', 20: 'Sita', 15: 'Rajesh', 18: 'Kiran'}
False
True
True
True'''

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
{10, 14, 15, 18, 19, 20, 25}
<class 'set'>
{10: 'Rama', 20: 'Manohar', 15: 'Radha', 18: 'Kiran', 14: 'Srinivas', 25: 'Ramesh', 19: 'Krishna'}
<class 'dict'>'''

#  Find  outputs  (Home  work)
a = {10 : 20 , 30 : 40}
b = {30 : 50 , 10 : 60}
# print(a + b) # error
c = {**a , **b} #{10:60,30:50}
print(c)
d = a | b
print(d) #{10: 60, 30: 50}


'''
(Home  work)
Write  a  program  to  create  a  dictionary  with  emp  names  and  salaries

Hint:  Append  each  emp  name  and  salary  to  dictionary  'a'
'''
a = eval(input("How many employees ? : "))
c = {}
i=0
while i<a:
    emp = input("Enter Emp name : ")
    sal = float(input("Enter Salary : "))
    c.update({emp:sal})
    i+=1
print(c)


''' (Home  work)
Write  a  program  to  convert  a  string  to  dictionary

Let  input  be   "Emp no = 25 , Emp name = Rama  Rao , sal = 10000.0 , gender = m"

What  is  the  output ?  --->  {Emp no : 25 , Emp name  :  Rama Rao , sal : 10000.0 , gender : m}

Hint :  Use  split()  method  twice
'''
a = "Emp no = 25 , Emp name = Rama  Rao , sal = 10000.0 , gender = m"
b = a.split(",")
print(b)
c={}
for i in b:
 x,y=i.split("=")
 c.update({x:y})
print(c)


# len()  function  demo  program  (Home  work)
a  =  {'Empno'  :  25,  'Ename'  :  'Rama  Rao'  ,  'Sal'  :  1000.65  }
print(len(a)) # 3
b = {}
print(len(b)) # 0

#  sum()  function demo  program  (Home  work)
a = {10 : 20 , 30 : 40 , 50 : 60}
print(sum(a . keys()))
print(sum(a . values()))
print(sum(a))
print(sum(a . items()))
'''
90
120
90
error'''

# max()  and  min()   functions  demo  program  (Home  work)
a = {10 : 20 , 30 : 25 , 40 : 5 , 7 : 28 , 9 : 50}
print(max(a . keys()))
print(min(a . keys()))
print(max(a . values()))
print(min(a . values()))
print(max(a . items()))
print(min(a . items()))
print(max(a))
print(min(a))
'''
40
7
50
5
(40, 5)
(7, 28)
40
7'''

#  dict()  function  demo program (Home  work))
a = [ (10 , 'Hyd') , (20 , 'Sec') , (15 , 'Cyb') , (20 , 'Pune')]  #  List of  tuples
b = dict(a) #  Converts  list  of  tuples  to  dict
print(b)  #  {10 : 'Hyd', 20 : 'Pune' , 15 : 'Cyb'}
c = ( ['R' , 'Red'] , ['G' , 'Green'] , ['B' , 'Blue'] , ['G' , 'Gray'])
d = dict(c)
print(d)
e = [[10 , 20 , 30] , [40 , 50 , 60] , [70 , 80 , 90]]
print(dict(e)) # error
f = [[10] , [20] , [30]]
print(dict(f)) # error
print(dict([10,  20])) # error
g = [[10 , [20 , 30]] , [40 , [50 , 60]] , [70 , [80 , 90]]]
print(dict(g)) #{10: [20, 30], 40: [50, 60], 70: [80, 90]}
h = [[[10 , 20] , 30] , [[40 , 50] , 60] , [[70 , 80] , 90]]
print(dict(h)) # error
i = [[(10 , 20) , 30] , [(40 , 50) , 60] , [(70 , 80) , 90]]
print(dict(i)) #{(10, 20): 30, (40, 50): 60, (70, 80): 90}

# sorted()  function  (Home  work)
a = {10 : 'Red' , 20 : 'Green' , 15 : 'Blue' , 18 : 'Yellow' , 5 : 'White'}
b = sorted(a . keys())
print(b)
c = sorted(a . values())
print(c)
d = sorted(a . items())
print(d)
f  = sorted(a  , reverse = True)
print(f)
print(a)
'''
[5, 10, 15, 18, 20]
['Blue', 'Green', 'Red', 'White', 'Yellow']
[(5, 'White'), (10, 'Red'), (15, 'Blue'), (18, 'Yellow'), (20, 'Green')]
[20, 18, 15, 10, 5]
{10: 'Red', 20: 'Green', 15: 'Blue', 18: 'Yellow', 5: 'White'}'''

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
a =  eval(input("Enter dictionary : "))
b= sorted(a.items())
print(dict(b))
c = {}
for i in b:
    c.update({i})
print(c)

#  keys()  method  demo  program
a = {10 : 'Hyd' , 20 : 'Sec' , 15 : 'Cyb' , 18 : 'Pune'}
b = a . keys()
print(b)
print(type(b))
for  x  in   b:
        print(x)
'''
dict_keys([10, 20, 15, 18])
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
'''
dict_values(['Hyd', 'Sec', 'Cyb', 'Pune'])
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
'''
dict_items([(10, 'Hyd'), (20, 'Sec'), (15, 'Cyb'), (18, 'Pune')])
<class 'dict_items'>
(10, 'Hyd')
(20, 'Sec')
(15, 'Cyb')
(18, 'Pune')
10 ... Hyd
20 ... Sec
15 ... Cyb
18 ... Pune'''

# Find  outputs (Home  work)
a = {10 : 'Hyd' , 20 : 'Sec' , 15 : 'Cyb' , 18 : 'Pune'}
for  x , y   in  a . items():
       print(x , y , sep = ' ... ')
for  x , y   in  a . keys():
       print(x , y , sep = ' ... ')
for  x , y   in  a . values():
       print(x , y , sep = ' ... ')
for  x , y   in  a:
       print(x , y , sep = ' ... ')
'''
10 ... Hyd
20 ... Sec
15 ... Cyb
18 ... Pune
error
error
error'''
# clear()  method  demo  program (Home  work)
a = {10 : 20 , 30 : 40 , 50 : 60}
print(a)
a . clear()
print(a)
del a
print(a)
'''
{10: 20, 30: 40, 50: 60}
{}
#ref also will be deleted error'''

# copy()  method demo  program  (Home  work)
a = {'R' : 'Red' , 'G' : 'Green' , 'B' : 'Blue'}
b = a . copy()
print(b)
print(a  is  b)
print(a  ==  b)
'''
{'R': 'Red', 'G': 'Green', 'B': 'Blue'}
False
True'''
#  Find  outputs  (Home  work)
a = {10 : 'Rama' , 20 : 'Sita' , 15 : 'Rajesh'}
x , y , z = a . keys()
print(x)
print(y)
print(z)
print()
x , y , z = a . values()
print(x)
print(y)
print(z)
print()
x , y ,  z = a . items()
print(x)
print(y)
print(z)
print()
(rno1 , sname1) , (rno2 , sname2) , (rno3 , sname3) = a . items()
print(rno1 , sname1)
print(rno2 , sname2)
print(rno3 , sname3)
'''
10
20
15

Rama
Sita
Rajesh

(10, 'Rama')
(20, 'Sita')
(15, 'Rajesh')

10 Rama
20 Sita
15 Rajesh'''
# Find outputs (Home  work)
a = [ ('R' , 'Red') , ('G' , 'Green') , ('B' , 'Blue')]
b = {'Y' : 'Yellow', 'G' : 'Gray'}
b . update(a) #{'Y': 'Yellow', 'G': 'Green', 'R': 'Red', 'B': 'Blue'}
print(b)
a . update(b)  # list doesnt have update

#  Find  outputs  (Home  work)
a = [ (10 , 20 , 30) , (40 , 50 , 60) , (70 , 80 , 90)]
b = {}
b.update(a) # error
print(b)
c = [(10,) , (20,) , (30,)]
b . update(c)
print(b) # error

#  Find  outputs (Home  work)
d = {x : x ** 3   for    x   in  range(5)}
print(d) #{0: 0, 1: 1, 2: 8, 3: 27, 4: 64}
print(type(d)) #<class 'dict'>

# Find outputs   (Home  work)
d = { x :  2 * x    for    x   in   range(5) }
print(d) #{0: 0, 1: 2, 2: 4, 3: 6, 4: 8}

# Find outputs  (Home  work)
a = {10 : 'Rama' , 15 : 'Sita' , 18 : 'Rajesh' , 17 : 'Kiran' , 12 : 'Rama Rao'}
b = { k :  v  for   k , v  in   a .items()   if    k % 2 != 0}
print(b) #{15: 'Sita', 17: 'Kiran'}
c = {k : a[k]   for   k   in    a    if   a[k] . startswith('R')}
print(c) #{10: 'Rama', 18: 'Rajesh', 12: 'Rama Rao'}


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
    What  does  a['M']  =  1  do ?  --->  Appends  'M' : 1  to  dict  'a'
    What  is  dictionary  'a' ?  --->  {'R' : 1 , 'A' : 1 , 'M' : 1}

5) a['A'] = a . get('A' , 0) + 1 = 1 + 1 = 2
    What  does  a['A']  =  2  do ?  --->  Modifies  value  of  'A'  to  2  in dict  'a'
    What  is  dictionary  'a' ?  --->  {'R' : 1 , 'A' : 2 , 'M' : 1}

6) a['R'] = a . get('R' , 0) + 1 =  1 + 1 = 2
    What  does  a['R']  =  2  do ?  ---> Modifies  value  of  'R'  to  2  in dict  'a'
    What  is  dictionary  'a' ?  --->  {'R' : 2 , 'A' : 2 , 'M' : 1}

7) a['A'] = a . get('A' , 0) + 1 =  2 + 1 = 3
    What  does  a['A']  =  3  do ?  ---> Modifies  value  of  'A'  to  3  in dict  'a'
    What  is  dictionary  'a' ?  --->  {'R' : 2 , 'A' : 3 , 'M' : 1}

8) a['O'] = a . get('O' , 0) + 1 =  0 + 1 = 1
    What  does  a['O']  =  1  do ?  --->  Appends  'O' : 1  to  dict  'a'
    What  is  dictionary  'a' ?  --->  {'R' : 2 , 'A' : 3 , 'M' : 1 , 'O' : 1}

9) Finally  what   is  dict  'a' ?  --->  {'R' : 2 , 'A' : 3 , 'M' : 1 , 'O' : 1}
'''
a="rama Rao"
b = a.upper()
print(b)
c={}
for i in b:
    if i!=" ":
     c[i]=c.get(i,0)+1
print(c)
