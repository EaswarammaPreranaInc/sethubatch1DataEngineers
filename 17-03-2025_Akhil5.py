#1 difference()   method  demo  program  (Home  work)
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

Output:
{10, 20}
<class 'set'>
{10, 20}
<class 'set'>
False
True

#2 symmetric_difference()   method  demo  program  (Home  work)
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

Output:
{10, 50, 20, 60}
<class 'set'>
{10, 50, 20, 60}
<class 'set'>
False
True

#3 Find  outputs  (Home  work)
a = {x * x  for   x   in   range(10)}
print(a)
print(type(a))

Output:
{0, 1, 64, 4, 36, 9, 16, 49, 81, 25}
<class 'set'>

#4 
Write  a  program  to  remove  duplicate  characters  of  the  string  using  set
1) Let  input  be   Rama  Rao   What  is  the  output  ? --->  Ram<space>o
2) Both  input  and  output  are  strings
3) How  to  convert  string  to  set  ?  --->  set(string), How  to  convert  set  to  string ?  ---> '' . join(set)
4) What  is  the  result  of  str({'H' , 'y' , 'd'})  ? --->  "{'H' , 'y' , 'd'}"  but  not  'Hyd'

s=str(input('Enter a string : '))
b=set(s)
a=''.join(b)
print(a)

Output:
Enter a string : Rama  Rao
ao mR

#5
Write  a  program  to  print  distinct  vowels  of  the  string  by  using  set
1) Let  input  be  RamA  Rao, What  is  the  output  ?  ---> AO  (case  is  ignored)
2) Both  input  and  output  are  strings
3) Hint:  Same  as  prog19  with  minor  changes

s=str(input('Enter a string : '))
v=['A','E','I','O','U','a','e','i','o','u']
c=''
b=set(s)
a=''.join(b)
for x in a:
	if x in v:
		c+=x
print(c)

Output:
Enter a string : Rama Rao
oa

#6 
Write  a  program  to  remove  duplicate  elements  of   list  using  set
1) Let  input  be  [False , 25 , 10.8 , 1  , 25 , 0 , 'Hyd' ,  10.8 , 1.0 , None , 'Sec' , 'Hyd' , True  ]
   What  is  the  output ?  --->	[False , 25 , 10.8 , 1 , 'Hyd' , None , 'Sec']
2) Both  input  and  output  are  lists

l=[False , 25 , 10.8 , 1  , 25 , 0 , 'Hyd' ,  10.8 , 1.0 , None , 'Sec' , 'Hyd' , True  ]
a=set(l)
b=list(a)
print(b)

Output:
[False, 1, 10.8, 'Hyd', 'Sec', 25, None]

#7
Write  a  program  to   obtain  common  elements  between  two  lists  using  sets
1) Let  1st  list  be  [10 , 20 , 30 , 40 , 50 , 60]  and  2nd  list  be  [30 , 40 , 70 , 80 , 20]
    What  is  the  output ?  --->	[20 , 30 , 40]
2) Both  input  and  output  are  lists

l1=  [10 , 20 , 30 , 40 , 50 , 60]
l2=  [30 , 40 , 70 , 80 , 20]
s1=set(l1)
s2=set(l2)
s3= list(s1 & s2)
print(s3)

Output:
[40, 20, 30]

#8 How  to  access  values  of  dictionary (Home  work)
a  =  {'Empno'  :  25 ,  'Ename'  :  'Rama  Rao'  ,  'Sal'  :  1000.65  }
print(a['Empno'])
print(a['Ename'])
print(a['Sal'])

Output:
25
Rama  Rao
1000.65

#9  How  to  modify  values  of  dictionary  (Home  work)
a  =  {'Empno'  :  25,  'Ename'  :  'Rama  Rao'  ,  'Sal'  :  1000.65  }
print(a)
print(id(a))
a['Sal']=2000
a['Ename']='Sita'
a['Empno']= 35
print(a)
print(id(a))

Output:
{'Empno': 25, 'Ename': 'Rama  Rao', 'Sal': 1000.65}
2321748310464
{'Empno': 35, 'Ename': 'Sita', 'Sal': 2000}
2321748310464

#10 How  to  append  key : value  pairs  to dictionary  (Home  work)
a  =  {'Empno'  :  25,  'Ename'  :  'Rama  Rao'  ,  'Sal'  :  1000.65  }
print(a)
a.update({'Gender' : 'M'})
a['Married'] =  True  
print(a)

Output:
{'Empno': 25, 'Ename': 'Rama  Rao', 'Sal': 1000.65}
{'Empno': 25, 'Ename': 'Rama  Rao', 'Sal': 1000.65, 'Gender': 'M', 'Married': True}

#11  Find  outputs (Home  work)
a = { }
a[10] = 'Rama'  
a.update({20 : 'Sita'})
a[15]= 'Rajesh' 
a.update({18 : 'Kiran' })
print(a)

Output:
{10: 'Rama', 20: 'Sita', 15: 'Rajesh', 18: 'Kiran'}

#12 How  to  remove  key : value  pairs  of  dictionary  (Home  work)
a =  {'Empno'  :  25,  'Ename'  :  'Rama  Rao'  ,  'Sal'  :  1000.65  }
print(a)
a.pop('Sal')
print(a)

Output:
{'Empno': 25, 'Ename': 'Rama  Rao', 'Sal': 1000.65}
{'Empno': 25, 'Ename': 'Rama  Rao'}

#13  in  and  not  in  operators  (Home  work)
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

Output:
True
False
True
False
True
False
False
False
True

#14 What  are  the  outputs  if  input  is  {10: 'A', 20: 'B', 15: 'C' , 20 : 'D'}
a = input('Enter  dictionary  :  ')
print(a)
print(type(a))
b = eval(a)
print(b)
print(type(b))

Output:
Enter  dictionary  :  {10: 'A', 20: 'B', 15: 'C' , 20 : 'D'}
{10: 'A', 20: 'B', 15: 'C' , 20 : 'D'}
<class 'str'>
{10: 'A', 20: 'D', 15: 'C'}
<class 'dict'>

#15 Find  outputs  (Home  work)
a = {10 : 'Rama' , 20 : 'Sita' , 15 : 'Rajesh' , 18 : 'Kiran'}
b = {**a}
print(b)
print(a  is  b)
print(a  ==  b)
c = a
print(a  is   c)
print(a  ==  c)

Output:
{10: 'Rama', 20: 'Sita', 15: 'Rajesh', 18: 'Kiran'}
False
True
True
True

#16 Find  outputs  (Home  work)
a = {10 : 'Rama' , 20 : 'Sita' , 15 : 'Rajesh'}
b = {18 : 'Kiran' , 14 : 'Amar' , 20  : 'Manohar'}
c = {25 : 'Ramesh' , 19 : 'Krishna' , 15 : 'Radha' , 14 : 'Srinivas'}
d = {*a , *b , *c}
print(d)
print(type(d))
e = {**a , **b , **c}
print(e)
print(type(e))

Output:
{10, 14, 15, 18, 19, 20, 25}
<class 'set'>
{10: 'Rama', 20: 'Manohar', 15: 'Radha', 18: 'Kiran', 14: 'Srinivas', 25: 'Ramesh', 19: 'Krishna'}
<class 'dict'>

#17 Find  outputs  (Home  work)
a = {10 : 20 , 30 : 40}
b = {30 : 50 , 10 : 60}
#print(a + b)
c = {**a , **b}
print(c)
d = a | b
print(d)

Output:
{10: 60, 30: 50}
{10: 60, 30: 50}

#18 Write  a  program  to  create  a  dictionary  with  emp  names  and  salaries
a={}
a['AAA']=10000
a['BBB']=20000
a['CCC']=15000
a['DDD']=18000
print(a)

Output:
{'AAA': 10000, 'BBB': 20000, 'CCC': 15000, 'DDD': 18000}

#19 
Write  a  program  to  convert  a  string  to  dictionary
Let  input  be   "Emp no = 25 , Emp name = Rama  Rao , sal = 10000.0 , gender = m"
What  is  the  output ?  --->  {Emp no : 25 , Emp name  :  Rama Rao , sal : 10000.0 , gender : m}
Hint :  Use  split()  method  twice
a =  "Emp no = 25 , Emp name = Rama  Rao , sal = 10000.0 , gender = m"
b = ['Emp no = 25' , 'Emp name = Rama  Rao' , 'sal = 10000.0' , 'gender = m']
c = {}
x =  'Emp no = 25'  --->  ['Emp  no' , '25']  ---> {'Emp  no': '25'}
x = 'Emp name = Rama  Rao'  --->  ['Emp name' , 'Rama  Rao']  --->  {'Emp  no': '25' , 'Emp  name': 'Rama Rao'}}

s="Emp no = 25 , Emp name = Rama  Rao , sal = 10000.0 , gender = m"
a=s.split(',')
c={}
for x in a:
    key, value = x.split(" = ", 1) 
    c[key] = value
print(c)

Output:
{'Emp no': '25 ', ' Emp name': 'Rama  Rao ', ' sal': '10000.0 ', ' gender': 'm'}

#20 len()  function  demo  program  (Home  work)
a  =  {'Empno'  :  25,  'Ename'  :  'Rama  Rao'  ,  'Sal'  :  1000.65  }
print(len(a))
b = {}
print(len(b))
#What  does  len(dict)  do ?  --->  Returns  number  of  key : value  pairs  in  the  dictionary

Output:
3
0

#21 sum()  function demo  program  (Home  work)
a = {10 : 20 , 30 : 40 , 50 : 60}
print(sum(a . keys()))
print(sum(a . values()))
print(sum(a))
#print(sum(a . items()))

Output:
90
120
90

#22 max()  and  min()   functions  demo  program  (Home  work)
a = {10 : 20 , 30 : 25 , 40 : 5 , 7 : 28 , 9 : 50}
print(max(a . keys()))
print(min(a . keys()))
print(max(a . values()))
print(min(a . values()))
print(max(a . items()))
print(min(a . items()))
print(max(a))
print(min(a))

Output:
40
7
50
5
(40, 5)
(7, 28)
40
7

#23 dict()  function  demo program (Home  work))
a = [ (10 , 'Hyd') , (20 , 'Sec') , (15 , 'Cyb') , (20 , 'Pune')]  #  List of  tuples
b = dict(a) #  Converts  list  of  tuples  to  dict
print(b)  #  {10 : 'Hyd', 20 : 'Pune' , 15 : 'Cyb'}
c = ( ['R' , 'Red'] , ['G' , 'Green'] , ['B' , 'Blue'] , ['G' , 'Gray'])
d = dict(c)
print(d)
e = [[10 , 20 , 30] , [40 , 50 , 60] , [70 , 80 , 90]]
#print(dict(e))
f = [[10] , [20] , [30]]
#print(dict(f))
#print(dict([10 , 20]))
g = [[10 , [20 , 30]] , [40 , [50 , 60]] , [70 , [80 , 90]]]
print(dict(g))
h = [[[10 , 20] , 30] , [[40 , 50] , 60] , [[70 , 80] , 90]]
#print(dict(h))
i = [[(10 , 20) , 30] , [(40 , 50) , 60] , [(70 , 80) , 90]]
print(dict(i))

Output:
{10: 'Hyd', 20: 'Pune', 15: 'Cyb'}
{'R': 'Red', 'G': 'Gray', 'B': 'Blue'}
{10: [20, 30], 40: [50, 60], 70: [80, 90]}
{(10, 20): 30, (40, 50): 60, (70, 80): 90}

#24 sorted()  function  (Home  work)
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

Output:
[5, 10, 15, 18, 20]
['Blue', 'Green', 'Red', 'White', 'Yellow']
[(5, 'White'), (10, 'Red'), (15, 'Blue'), (18, 'Yellow'), (20, 'Green')]
[20, 18, 15, 10, 5]
{10: 'Red', 20: 'Green', 15: 'Blue', 18: 'Yellow', 5: 'White'}

#25 Write  a  program  to  sort  dictionary  wrt  keys  (Home  work)
1) Let  input  be   {10 : 'A' , 20 : 'B' , 15 : 'C' , 5 : 'D' , 12 : 'E'}
    What  is  the  output ?  ---> {5 : 'D' , 10 : 'A' ,  12 : 'E' ,  15 : 'C' , 20 : 'B'}
2) Both  input  and  output  are  dictionaries
3) Hint:  Use  sorted()  function
4) a = {10 : 'A' , 20 : 'B' , 15 : 'C' , 5 : 'D' , 12 : 'E'}
    b = sorted(a . items())  --->  [(5 , 'D' ) , (10 , 'A') , (12 , 'E') , (15 , 'C') , (20, 'B')]
    dict(b)  --->  {5 : 'D' , 10 : 'A' , .....}

a={10 : 'A' , 20 : 'B' , 15 : 'C' , 5 : 'D' , 12 : 'E'}
b=sorted(a.items())
print(dict(b))

Output:
{5: 'D', 10: 'A', 12: 'E', 15: 'C', 20: 'B'}

#26 keys()  method  demo  program
a = {10 : 'Hyd' , 20 : 'Sec' , 15 : 'Cyb' , 18 : 'Pune'}
b = a . keys()
print(b)
print(type(b))
for  x  in   b:
        print(x)
#What  does  keys()  method  do  --->  Returns  dict_keys  object  which  has  list  of  all  the  dictionary  keys

Output:
dict_keys([10, 20, 15, 18])
<class 'dict_keys'>
10
20
15
18

#27 values()  method  demo  program
a = {10 : 'Hyd' , 20 : 'Sec' , 15 : 'Cyb' , 18 : 'Pune'}
b = a . values()
print(b)
print(type(b))
for  x   in   b:
	print(x)
#What  does  values()  method  do  --->  Returns  dict_values  object  which  has  list  of  all  the  dictionary  values

Output:
dict_values(['Hyd', 'Sec', 'Cyb', 'Pune'])
<class 'dict_values'>
Hyd
Sec
Cyb
Pune

#28 items()  method  demo  program
a = {10 : 'Hyd' , 20 : 'Sec' , 15 : 'Cyb' , 18 : 'Pune'}
b = a . items()
print(b)
print(type(b))
for  x   in   b:
        print(x)
for  x , y   in  b:
        print(x , y , sep = ' ... ')
#1) What  does  items()  method  do  --->  Returns  dict_items  object  which  has  list  of  tuples
#2) What  are  the  two  elements  of  each  tuple ?  --->  (key , value)

Output:
dict_items([(10, 'Hyd'), (20, 'Sec'), (15, 'Cyb'), (18, 'Pune')])
<class 'dict_items'>
(10, 'Hyd')
(20, 'Sec')
(15, 'Cyb')
(18, 'Pune')
10 ... Hyd
20 ... Sec
15 ... Cyb
18 ... Pune

#29 Find  outputs (Home  work)
a = {10 : 'Hyd' , 20 : 'Sec' , 15 : 'Cyb' , 18 : 'Pune'}
for  x , y   in  a . items():
       print(x , y , sep = ' ... ')
#for  x , y   in  a . keys():
#       print(x , y , sep = ' ... ')
#for  x , y   in  a . values():
#       print(x , y , sep = ' ... ')
#for  x , y   in  a:
#       print(x , y , sep = ' ... ')

Output:
10 ... Hyd
20 ... Sec
15 ... Cyb
18 ... Pune

#30 clear()  method  demo  program (Home  work)
a = {10 : 20 , 30 : 40 , 50 : 60}
print(a)
a . clear()
print(a)
del  a
#print(a)

Output:
{10: 20, 30: 40, 50: 60}
{}

#31  copy()  method demo  program  (Home  work)
a = {'R' : 'Red' , 'G' : 'Green' , 'B' : 'Blue'}
b = a . copy()
print(b)
print(a  is  b)
print(a  ==  b)

Output:
{'R': 'Red', 'G': 'Green', 'B': 'Blue'}
False
True

#32 Find  outputs  (Home  work)
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

Output:
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
15 Rajesh

#33 
'''Write  a program  to  determine  frequency  of  each  alphabet  in  the  string   in   alphabetical  order  (ignoring  the  case)
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
s = str(input('Enter a string : '))'''
a=s.upper()
b = {}
for x in a:
	if x.isalpha():
		b[x]=b.get(x,0)+1
print(b)

Output:
Enter a string : RamA raO
{'R': 2, 'A': 3, 'M': 1, 'O': 1}

#32 Find outputs (Home  work)
a = [ ('R' , 'Red') , ('G' , 'Green') , ('B' , 'Blue')]
b = {'Y' : 'Yellow', 'G' : 'Gray'}
b . update(a)
print(b)
#a . update(b)

Output:
{'Y': 'Yellow', 'G': 'Green', 'R': 'Red', 'B': 'Blue'}

#33 Find  outputs  (Home  work)
a = [ (10 , 20 , 30) , (40 , 50 , 60) , (70 , 80 , 90)]
b = {}
#b.update(a)
print(b)
c = [(10,) , (20,) , (30,)]
#b . update(c)
print(b)

Output:
{}
{}

#34 Find  outputs (Home  work)
d = {x : x ** 3   for    x   in  range(5)}
print(d)
print(type(d))

Output:
{0: 0, 1: 1, 2: 8, 3: 27, 4: 64}
<class 'dict'>

#35 Find outputs   (Home  work)
d = { x :  2 * x    for    x   in   range(5) }
print(d)

Output:
{0: 0, 1: 2, 2: 4, 3: 6, 4: 8}

#36  Find outputs  (Home  work)
a = {10 : 'Rama' , 15 : 'Sita' , 18 : 'Rajesh' , 17 : 'Kiran' , 12 : 'Rama Rao'}
b = { k :  v  for   k , v  in   a .items()   if    k % 2 != 0}
print(b)
c = {k : a[k]   for   k   in    a    if   a[k] . startswith('R')}
print(c)

Output:
{15: 'Sita', 17: 'Kiran'}
{10: 'Rama', 18: 'Rajesh', 12: 'Rama Rao'}